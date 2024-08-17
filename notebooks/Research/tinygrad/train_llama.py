import argparse
import json
from pathlib import Path
from typing import List

import numpy as np
from llama import Transformer, convert_from_huggingface, fix_bf16

# np.set_printoptions(linewidth=200)
from sentencepiece import SentencePieceProcessor
from tinygrad import Device, Tensor, nn
from tinygrad.helpers import JIT, Context, getenv
from tinygrad.nn.state import (
    get_state_dict,
    load_state_dict,
    safe_load,
    safe_save,
    torch_load,
)

MAX_CONTEXT = getenv("MAX_CONTEXT", 4096)
MODEL_PARAMS = {
  "tiny": {
    "1B-Chat": {
      # https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0/blob/main/config.json#L25
      "args": {"dim": 2048, "n_layers": 22, "n_heads": 32, "n_kv_heads": 4, "norm_eps": 1e-05, "vocab_size": 32000, "hidden_dim": 5632},
      "files": 1,
    },
    "tokenizer": SentencePieceProcessor,
  }
}

# **** helper functions ****
def concat_weights(models, device=None):
  def convert(name) -> Tensor:
    disk_tensors: List[Tensor] = [model[name] for model in models]
    if len(disk_tensors) == 1 or len(disk_tensors[0].shape) == 1:
      return disk_tensors[0].to(device=device)
    axis = 1 if name.startswith("tok_embeddings.") or name.endswith(".attention.wo.weight") or name.endswith(".feed_forward.w2.weight") else 0
    lazy_tensors = [data.to(device=device) for data in disk_tensors]
    return lazy_tensors[0].cat(*lazy_tensors[1:], dim=axis)
  return {name: convert(name) for name in {name: None for model in models for name in model}}

def load(fn:str):
  if fn.endswith('.index.json'):
    with open(fn) as fp: weight_map = json.load(fp)['weight_map']
    parts = {n: load(str(Path(fn).parent / Path(n).name)) for n in set(weight_map.values())}
    return {k: parts[n][k] for k, n in weight_map.items()}
  elif fn.endswith(".safetensors"):
    return safe_load(fn)
  else:
    return torch_load(fn)

class LLaMa:
  @staticmethod
  def build(model_path, tokenizer_path, model_gen="1", model_size="7B", quantize=None, device=None):
    params = MODEL_PARAMS[model_gen][model_size]
    tokenizer = MODEL_PARAMS[model_gen]['tokenizer'](model_file=str(tokenizer_path))
    assert tokenizer.vocab_size() == params["args"]["vocab_size"], f"{tokenizer.vocab_size()=} not equal to {params['args']['vocab_size']}"

    if quantize == "int8":
      from llama3 import Int8Linear
      linear = Int8Linear
    elif quantize == "nf4":
      from llama3 import NF4Linear
      linear = NF4Linear(64)
    else:
      linear = nn.Linear

    model = Transformer(**params["args"], linear=linear, max_context=MAX_CONTEXT, jit=bool(JIT))

    if model_path.is_dir():
      weights = concat_weights([load(filename) for filename in [f"{model_path}/consolidated.{i:02d}.pth" for i in range(params["files"])]], device[0] if isinstance(device, tuple) else device)
    else:
      weights = load(str(model_path))
    if "model.embed_tokens.weight" in weights:
      weights = convert_from_huggingface(weights, model, params["args"]["n_heads"], params["args"].get("n_kv_heads", params["args"]["n_heads"]))

    weights = fix_bf16(weights)

    with Context(BEAM=0):
      # quantize
      if quantize is not None:
        weights = linear.quantize(weights, device)
        for _,v in weights.items(): v.realize()

      # shard
      if isinstance(device, tuple):
        for k,v in nn.state.get_state_dict(model).items():
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
      load_state_dict(model, weights, strict=False, consume=True)

    return LLaMa(model, tokenizer)

  def __init__(self, model, tokenizer):
    self.model = model
    self.tokenizer = tokenizer

  def greedy_until(self, prompt:str, until, max_length, temperature):
    toks = [self.tokenizer.bos_id()] + self.tokenizer.encode(prompt)
    start_pos = 0
    for i in range(max_length):
      probs = llama.model(Tensor([toks[start_pos:]]), start_pos, temperature).realize()
      probs_np = probs.numpy()
      tok = int(np.random.choice(len(probs_np), p=probs_np))
      start_pos = len(toks)
      toks.append(tok)

      if tok == self.tokenizer.eos_id(): break
      output = self.tokenizer.decode(toks)
      for s in until:
        if output.endswith(s): return output[0:-len(s)]
    return output

if __name__ == "__main__":
  Tensor.no_grad = True
  print(f"using {Device.DEFAULT} backend")

  parser = argparse.ArgumentParser(description="Run LLaMA in tinygrad", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument("--prompt", type=str, default=None, help="Phrase to start with. Without this, it goes into chatbot mode")
  parser.add_argument("--count", type=int, default=1000, help="Max number of tokens to generate")
  parser.add_argument("--personality", type=str, default="Stacy", help="Personality, can be Stacy, George, Gary, or Lexie")
  parser.add_argument("--temperature", type=float, default=0.7, help="Temperature in the softmax")
  parser.add_argument("--timing", action="store_true", help="Print timing per token")
  parser.add_argument("--profile", action="store_true", help="Output profile data to out.prof")
  parser.add_argument("--gen", default="1", help=f"""Generation of the model to use {list(MODEL_PARAMS.keys())}""")
  parser.add_argument("--size", type=str, default=None, help=f"""Size of model to use {", ".join([f"{list(v.keys())} for gen '{k}'" for k, v in MODEL_PARAMS.items()])}""")
  parser.add_argument("--quantize", type=str, default=None, help="Quantize the weights to int8 or nf4 in memory")
  parser.add_argument("--model", type=Path, default=None, help="Folder with the original weights to load, or single .index.json, .safetensors or .bin file")
  parser.add_argument("--shard", type=int, default=1, help="number of devices to load the weights to")

  args = parser.parse_args()
  if args.gen not in MODEL_PARAMS: raise ValueError("Invalid model generation")
  if args.size is None: args.size = list(MODEL_PARAMS[args.gen].items())[0][0]

  LLAMA_SUFFIX = {"1": "", "2": "-2", "3": "-3", "code": "-code", "tiny": "-tiny"}[args.gen]
  MODEL_PATH = args.model or Path(__file__).parents[1] / f"weights/LLaMA{LLAMA_SUFFIX}/{args.size}"
  TOKENIZER_PATH = (MODEL_PATH if MODEL_PATH.is_dir() else MODEL_PATH.parent) / "tokenizer.model"
  print(f"using LLaMA{LLAMA_SUFFIX}-{args.size} model")
  device = tuple(f"{Device.DEFAULT}:{i}" for i in range(args.shard)) if args.shard > 1 else Device.DEFAULT
  llama = LLaMa.build(MODEL_PATH, TOKENIZER_PATH, model_gen=args.gen, model_size=args.size, quantize=args.quantize, device=device)

  file_path = "model.safetensors"
  state_dict = get_state_dict(llama.model)

  for k, v in state_dict.items():
    if k == 'freqs_cis':
      print(k)

    if 'tok' in k:
      print(k)

    if 'cache' in k:
      print(k)

  safe_save(state_dict, file_path)
