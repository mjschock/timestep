from datetime import datetime
import json
from pathlib import Path
from typing import Any, Dict, Optional, Tuple, Union

import numpy as np
from tinygrad import Device, dtypes, nn, Tensor, TinyJit, Variable
from tinygrad.helpers import Context, getenv, JIT
from tinygrad.nn.state import load_state_dict, safe_load, torch_load
from transformers import PreTrainedModel
from transformers.generation import GenerationConfig
# from transformers.modeling_outputs import CausalLMOutputWithPast

# from .configuration_llama import LlamaConfig
from transformers.models.llama.configuration_llama import LlamaConfig

from notebooks.Research.src.tinygrad.examples.llama import concat_weights, load, MAX_CONTEXT, MODEL_PARAMS, LLaMa
from notebooks.Research.src.tinygrad.extra.models.llama import convert_from_huggingface, fix_bf16, Transformer, sample


class ModifiedTransformer(Transformer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def forward(self, tokens:Tensor, start_pos:Union[Variable,int], temperature:float, top_k:int, top_p:float, alpha_f:float, alpha_p:float):
        _bsz, seqlen = tokens.shape
        freqs_cis = self.freqs_cis.shrink((None, (start_pos, start_pos+seqlen),None,None,None))

        h = self.tok_embeddings(tokens)
        mask = Tensor.full((1, 1, seqlen, start_pos+seqlen), float("-inf"), dtype=h.dtype, device=h.device).triu(start_pos+1).realize() if seqlen > 1 else None
        for layer in self.layers: h = layer(h, start_pos, freqs_cis, mask)
        logits = self.output(self.norm(h)).float()[:, -1, :]

        # return sample(logits.flatten(), temperature, top_k, top_p, alpha_f, alpha_p).realize()
        return logits

    def __call__(self, tokens:Tensor, start_pos:Variable, temperature:float=0.0, top_k:int=0, top_p:float=0.8, alpha_f:float=0.0, alpha_p:float=0.0):
        # TODO: better way to handle the first call v.s. the rest?
        if tokens.shape[0:2] == (1,1) and self.forward_jit is not None:
            return self.forward_jit(tokens, Variable("start_pos", 0, self.max_context).bind(start_pos), temperature, top_k, top_p, alpha_f, alpha_p)

        # return self.forward(tokens, start_pos, temperature, top_k, top_p, alpha_f, alpha_p)
        # raise Exception("Forward should always be jitted but was not")

# class CausalLMOutputWithPast:
#     def __init__(self, attentions: Optional[Tuple[Tensor]] = None, hidden_states: Optional[Tuple[Tensor]] = None, logits: Optional[Tensor] = None, loss: Optional[Tensor] = None, past_key_values: Optional[Tuple[Tuple[Tensor]]] = None):
#         self.attentions = attentions
#         self.hidden_states = hidden_states
#         self.logits = logits
#         self.loss = loss
#         self.past_key_values = past_key_values

class TinygradLlamaForCausalLM(PreTrainedModel):
    config_class = LlamaConfig

    def __init__(self, config: LlamaConfig, device: str = None, model_path: str = None, quantize: str = None):
        self.config = config
        self.device = device
        self.name_or_path = config.name_or_path
        self.generation_config = GenerationConfig.from_model_config(config) if self.can_generate() else None
        self.warnings_issued = {}

        if quantize == "int8":
            from llama3 import Int8Linear
            linear = Int8Linear

        elif quantize == "nf4":
            from llama3 import NF4Linear
            linear = NF4Linear(64)

        else:
            linear = nn.Linear

        self.model = ModifiedTransformer(
            dim=self.config.hidden_size,
            hidden_dim=self.config.intermediate_size,
            jit=bool(JIT),
            linear=linear,
            max_context=MAX_CONTEXT,
            n_heads=self.config.num_attention_heads,
            n_kv_heads=self.config.num_key_value_heads,
            n_layers=self.config.num_hidden_layers,
            norm_eps=self.config.rms_norm_eps,
            vocab_size=self.config.vocab_size,
        )

        if model_path.is_dir():
            weights = concat_weights([load(filename) for filename in [f"{model_path}/consolidated.{i:02d}.pth" for i in range(params["files"])]], device[0] if isinstance(device, tuple) else device)
        
        else:
            weights = load(str(model_path))
        
        if "model.embed_tokens.weight" in weights:
            weights = convert_from_huggingface(weights, self.model, self.config.num_attention_heads, self.config.num_key_value_heads)

        weights = fix_bf16(weights)

        with Context(BEAM=0):
            # quantize
            if quantize is not None:
                weights = linear.quantize(weights, device)
                for _,v in weights.items(): v.realize()

            # shard
            if isinstance(device, tuple):
                for k,v in nn.state.get_state_dict(self.model).items():
                    if 'scale' in k: v.shard_(device, axis=None)  # from quantized
                    elif '.attention.' in k:
                        if getenv("SHARD_KVCACHE") and ('.wq.' in k or '.wk.' in k or '.wv.' in k): v.shard_(device, axis=0)
                        else: v.shard_(device, axis=-1)
                    elif '.feed_forward.w1.' in k: v.shard_(device, axis=0)
                    elif '.feed_forward.w3.' in k: v.shard_(device, axis=0)
                    elif '.feed_forward.' in k: v.shard_(device, axis=-1)
                    elif 'tok_embeddings.weight' in k: v.shard_(device, axis=0)
                    elif 'output.weight' in k: v.shard_(device, axis=-1)
                    #elif k.endswith('.weight'): v.shard_(device, axis=-1)
                    #elif 'norm.' in k: v.shard_(device, axis=-1)
                    else: v.shard_(device, axis=None)
                    #print(k, v.shape, v.lazydata.axis)

            # replace weights in model
            load_state_dict(self.model, weights, strict=False, consume=True)

    @classmethod
    def can_generate(cls) -> bool:
        """
        Returns whether this model can generate sequences with `.generate()`.

        Returns:
            `bool`: Whether this model can generate sequences with `.generate()`.
        """
        # Detects whether `prepare_inputs_for_generation` has been overwritten, which is a requirement for generation.
        # Alternativelly, the model can also have a custom `generate` function.
        # if "GenerationMixin" in str(cls.prepare_inputs_for_generation) and "GenerationMixin" in str(cls.generate):
        #     return False
        return True

    # @property
    # def framework(self) -> str:
    #     """
    #     :str: Identifies that this is a Tinygrad model.
    #     """
    #     return "tinygrad"

    def generate(
        self,
        # inputs: Optional[torch.Tensor] = None,
        # inputs: Optional[Tensor] = None,
        input_ids: Optional[Tensor] = None,
        max_new_tokens: Optional[int] = None,
        temperature: Optional[float] = 0.0,
        # generation_config: Optional[GenerationConfig] = None,
        # logits_processor: Optional[LogitsProcessorList] = None,
        # stopping_criteria: Optional[StoppingCriteriaList] = None,
        # prefix_allowed_tokens_fn: Optional[Callable[[int, torch.Tensor], List[int]]] = None,
        # synced_gpus: Optional[bool] = None,
        # assistant_model: Optional["PreTrainedModel"] = None,
        # streamer: Optional["BaseStreamer"] = None,
        # negative_prompt_ids: Optional[torch.Tensor] = None,
        # negative_prompt_attention_mask: Optional[torch.Tensor] = None,
        **kwargs,
    ) -> Tensor:
        if input_ids is None:
            input_ids = Tensor([[self.config.bos_token_id]], device=self.device)

        if max_new_tokens is None:
            max_new_tokens = 100

        batch_size, sequence_length = input_ids.shape

        assert input_ids.shape == (batch_size, sequence_length), f"{input_ids.shape} != ({batch_size}, {sequence_length})"

        new_token_ids = Tensor.zeros(batch_size, max_new_tokens, device=self.device)
        assert new_token_ids.shape == (batch_size, max_new_tokens), f"{new_token_ids.shape} != ({batch_size}, {max_new_tokens})"

        # input_ids = input_ids.cat(Tensor.zeros(batch_size, max_new_tokens, device=self.device))
        output_ids = input_ids.cat(new_token_ids, dim=-1)
        assert output_ids.shape == (batch_size, sequence_length + max_new_tokens), f"{output_ids.shape} != ({batch_size}, {sequence_length + max_new_tokens})"

        for start_pos in range(sequence_length + max_new_tokens):
            print('start_pos:', start_pos)

            tokens = output_ids[:, start_pos:start_pos+1]
            assert type(tokens) == Tensor, f"{type(tokens)} != {Tensor}"
            assert tokens.shape == (batch_size, 1), f"{tokens.shape} != ({batch_size}, 1)"

            logits = self.model(
                start_pos=start_pos,
                temperature=temperature,
                tokens=tokens,
            )

        return output_ids
        # return [
        #     output_ids,
        # ]

        # timings = {
        #     "logits": [],
        #     "sample": [],
        #     "reshape": [],
        #     "assign": [],
        #     "all": [],
        # }

        # # assert input_ids[:, 0].all() == self.config.bos_token_id, f"{input_ids[:, 0]} != {self.config.bos_token_id}"

        # batch_size, sequence_length = input_ids.shape
        # do_sample: bool = kwargs.get("do_sample", False)
        # logits: Tensor = None
        # start_pos: int = 0
        # stop_pos: int = start_pos + 1

        # maximum_sequence_length = sequence_length + max_new_tokens
        # # placeholder = np.full((batch_size, maximum_sequence_length), self.config.pad_token_id, dtype=np.int32)
        # # placeholder = np.full((batch_size, maximum_sequence_length), self.config.eos_token_id, dtype=np.int32)
        # # token_ids = np.copy(placeholder)
        # # token_ids[:, :sequence_length] = input_ids.numpy()
        # # token_ids = np.concatenate((input_ids.numpy(), np.full((batch_size, max_new_tokens), self.config.pad_token_id, dtype=np.int32)), axis=1)
        # token_ids = np.concatenate((input_ids.numpy(), np.full((batch_size, max_new_tokens), self.config.eos_token_id, dtype=np.int32)), axis=1)
        # assert token_ids.shape == (batch_size, maximum_sequence_length), f"{token_ids.shape} != ({batch_size}, {maximum_sequence_length})"

        # assert token_ids[:, 0].all() == self.config.bos_token_id, f"{token_ids[:, 0]} != {self.config.bos_token_id}"

        # # token_ids = np.concatenate((input_ids.numpy())

        # # assert token_ids.shape == (batch_size, sequence_length)
        # # assert token_ids.shape == (batch_size, sequence_length), f"{token_ids.shape} != ({batch_size}, {sequence_length})

        # start = datetime.now()

        # for i in range(sequence_length-1):
        #     # start_i = datetime.now()

        #     tokens = Tensor(token_ids[:, start_pos:stop_pos])

        #     logits = self.model(
        #         start_pos=start_pos,
        #         temperature=temperature,
        #         tokens=tokens,
        #     )

        #     assert logits.shape == (batch_size, self.config.vocab_size)

        #     start_pos += 1
        #     stop_pos += 1

        #     # print(f"Elapsed: {datetime.now() - start_i}")

        # assert start_pos == sequence_length-1, f"{start_pos} != {sequence_length-1}"

        # print(f"Warmup: {datetime.now() - start}")

        # # start = datetime.now()

        # for i in range(max_new_tokens):
        #     start_i = datetime.now()

        #     tokens = Tensor(token_ids[:, start_pos:start_pos+1])

        #     logits = self.model(
        #        start_pos=start_pos,
        #        temperature=temperature,
        #        tokens=tokens,
        #     )
        #     # ).realize()

        #     timings["logits"].append(datetime.now() - start_i)
        #     start_i = datetime.now()

        #     assert logits.shape == (batch_size, self.config.vocab_size)

        #     if do_sample:
        #         # top_k:int=0, top_p:float=0.8, alpha_f:float=0.0, alpha_p:float=0.0
        #         # output_ids = sample(
        #         #     logits.flatten(),
        #         #     temperature,
        #         #     k=0,
        #         #     p=0.8,
        #         #     af=0.0,
        #         #     ap=0.0,
        #         # )
        #         # ).realize()
        #         output_ids = logits.argmax(axis=-1, keepdim=True)

        #     else:
        #         # output_ids = logits.argmax(dim=-1)
        #         # output_ids = logits.flatten().argmax().realize()
        #         raise NotImplementedError

        #     timings["sample"].append(datetime.now() - start_i)
        #     start_i = datetime.now()

        #     # output_ids = output_ids.numpy().reshape(batch_size, 1)
        #     # output_ids = output_ids.reshape(batch_size, 1)
        #     # output_ids = output_ids.reshape(batch_size, 1).numpy()
        #     output_ids = output_ids.numpy()
        #     assert output_ids.shape == (batch_size, 1), f"{output_ids.shape} != ({batch_size}, 1)"

        #     timings["reshape"].append(datetime.now() - start_i)
        #     start_i = datetime.now()

        #     # start_pos = token_ids.shape[1]
        #     start_pos += 1
        #     # token_ids = np.concatenate((token_ids, output_ids), axis=1)
        #     token_ids[:, start_pos:start_pos+1] = output_ids
        #     # token_ids = np.hstack((token_ids, output_ids))

        #     timings["assign"].append(datetime.now() - start_i)
        #     start_i = datetime.now()

        #     # assert token_ids.shape == (batch_size, sequence_length + i + 1), f"{token_ids.shape} != ({batch_size}, {sequence_length + i + 1})"

        #     # print(f"Elapsed: {datetime.now() - start_i}")

        #     # if np.any(token_ids[:, -1] == self.config.eos_token_id):
        #     #     break
        #     # if np.all(token_ids[:, -1] == self.config.eos_token_id): # TODO: should be "<|im_end|>"
        #     if np.all(output_ids[:, 0] == self.config.eos_token_id): # TODO: should be "<|im_end|>"
        #         break

        #     timings["all"].append(datetime.now() - start_i)

        # # return outputs
        # # return CausalLMOutputWithPast(
        # #     attentions=attentions,
        # #     hidden_states=hidden_states,
        # #     logits=logits,
        # #     loss=loss,
        # #     past_key_values=past_key_values,
        # # )

        # # print(f"Elapsed: {datetime.now() - start}")

        # print(f"Timings: {timings}")

        # for k,v in timings.items():
        #     print(f"{k}: {np.mean(v)}")

        # return token_ids
