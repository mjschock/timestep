from datetime import date, datetime  # noqa: F401
from typing import Dict, List  # noqa: F401

from timestep.api.openai.v1 import util
from timestep.api.openai.v1.models.base_model import Model
from timestep.api.openai.v1.models.chat_completion_functions import \
    ChatCompletionFunctions  # noqa: E501
from timestep.api.openai.v1.models.chat_completion_request_message import \
    ChatCompletionRequestMessage  # noqa: E501
from timestep.api.openai.v1.models.chat_completion_stream_options import \
    ChatCompletionStreamOptions  # noqa: E501
from timestep.api.openai.v1.models.chat_completion_tool import \
    ChatCompletionTool  # noqa: E501
from timestep.api.openai.v1.models.chat_completion_tool_choice_option import \
    ChatCompletionToolChoiceOption  # noqa: E501
from timestep.api.openai.v1.models.create_chat_completion_request_function_call import \
    CreateChatCompletionRequestFunctionCall  # noqa: E501
from timestep.api.openai.v1.models.create_chat_completion_request_model import \
    CreateChatCompletionRequestModel  # noqa: E501
from timestep.api.openai.v1.models.create_chat_completion_request_response_format import \
    CreateChatCompletionRequestResponseFormat  # noqa: E501
from timestep.api.openai.v1.models.create_chat_completion_request_stop import \
    CreateChatCompletionRequestStop  # noqa: E501


class CreateChatCompletionRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, messages=None, model=None, frequency_penalty=0, logit_bias=None, logprobs=False, top_logprobs=None, max_tokens=None, n=1, presence_penalty=0, response_format=None, seed=None, service_tier=None, stop=None, stream=False, stream_options=None, temperature=1, top_p=1, tools=None, tool_choice=None, parallel_tool_calls=True, user=None, function_call=None, functions=None):  # noqa: E501
        """CreateChatCompletionRequest - a model defined in OpenAPI

        :param messages: The messages of this CreateChatCompletionRequest.  # noqa: E501
        :type messages: List[ChatCompletionRequestMessage]
        :param model: The model of this CreateChatCompletionRequest.  # noqa: E501
        :type model: CreateChatCompletionRequestModel
        :param frequency_penalty: The frequency_penalty of this CreateChatCompletionRequest.  # noqa: E501
        :type frequency_penalty: float
        :param logit_bias: The logit_bias of this CreateChatCompletionRequest.  # noqa: E501
        :type logit_bias: Dict[str, int]
        :param logprobs: The logprobs of this CreateChatCompletionRequest.  # noqa: E501
        :type logprobs: bool
        :param top_logprobs: The top_logprobs of this CreateChatCompletionRequest.  # noqa: E501
        :type top_logprobs: int
        :param max_tokens: The max_tokens of this CreateChatCompletionRequest.  # noqa: E501
        :type max_tokens: int
        :param n: The n of this CreateChatCompletionRequest.  # noqa: E501
        :type n: int
        :param presence_penalty: The presence_penalty of this CreateChatCompletionRequest.  # noqa: E501
        :type presence_penalty: float
        :param response_format: The response_format of this CreateChatCompletionRequest.  # noqa: E501
        :type response_format: CreateChatCompletionRequestResponseFormat
        :param seed: The seed of this CreateChatCompletionRequest.  # noqa: E501
        :type seed: int
        :param service_tier: The service_tier of this CreateChatCompletionRequest.  # noqa: E501
        :type service_tier: str
        :param stop: The stop of this CreateChatCompletionRequest.  # noqa: E501
        :type stop: CreateChatCompletionRequestStop
        :param stream: The stream of this CreateChatCompletionRequest.  # noqa: E501
        :type stream: bool
        :param stream_options: The stream_options of this CreateChatCompletionRequest.  # noqa: E501
        :type stream_options: ChatCompletionStreamOptions
        :param temperature: The temperature of this CreateChatCompletionRequest.  # noqa: E501
        :type temperature: float
        :param top_p: The top_p of this CreateChatCompletionRequest.  # noqa: E501
        :type top_p: float
        :param tools: The tools of this CreateChatCompletionRequest.  # noqa: E501
        :type tools: List[ChatCompletionTool]
        :param tool_choice: The tool_choice of this CreateChatCompletionRequest.  # noqa: E501
        :type tool_choice: ChatCompletionToolChoiceOption
        :param parallel_tool_calls: The parallel_tool_calls of this CreateChatCompletionRequest.  # noqa: E501
        :type parallel_tool_calls: bool
        :param user: The user of this CreateChatCompletionRequest.  # noqa: E501
        :type user: str
        :param function_call: The function_call of this CreateChatCompletionRequest.  # noqa: E501
        :type function_call: CreateChatCompletionRequestFunctionCall
        :param functions: The functions of this CreateChatCompletionRequest.  # noqa: E501
        :type functions: List[ChatCompletionFunctions]
        """
        self.openapi_types = {
            'messages': List[ChatCompletionRequestMessage],
            'model': CreateChatCompletionRequestModel,
            'frequency_penalty': float,
            'logit_bias': Dict[str, int],
            'logprobs': bool,
            'top_logprobs': int,
            'max_tokens': int,
            'n': int,
            'presence_penalty': float,
            'response_format': CreateChatCompletionRequestResponseFormat,
            'seed': int,
            'service_tier': str,
            'stop': CreateChatCompletionRequestStop,
            'stream': bool,
            'stream_options': ChatCompletionStreamOptions,
            'temperature': float,
            'top_p': float,
            'tools': List[ChatCompletionTool],
            'tool_choice': ChatCompletionToolChoiceOption,
            'parallel_tool_calls': bool,
            'user': str,
            'function_call': CreateChatCompletionRequestFunctionCall,
            'functions': List[ChatCompletionFunctions]
        }

        self.attribute_map = {
            'messages': 'messages',
            'model': 'model',
            'frequency_penalty': 'frequency_penalty',
            'logit_bias': 'logit_bias',
            'logprobs': 'logprobs',
            'top_logprobs': 'top_logprobs',
            'max_tokens': 'max_tokens',
            'n': 'n',
            'presence_penalty': 'presence_penalty',
            'response_format': 'response_format',
            'seed': 'seed',
            'service_tier': 'service_tier',
            'stop': 'stop',
            'stream': 'stream',
            'stream_options': 'stream_options',
            'temperature': 'temperature',
            'top_p': 'top_p',
            'tools': 'tools',
            'tool_choice': 'tool_choice',
            'parallel_tool_calls': 'parallel_tool_calls',
            'user': 'user',
            'function_call': 'function_call',
            'functions': 'functions'
        }

        self._messages = messages
        self._model = model
        self._frequency_penalty = frequency_penalty
        self._logit_bias = logit_bias
        self._logprobs = logprobs
        self._top_logprobs = top_logprobs
        self._max_tokens = max_tokens
        self._n = n
        self._presence_penalty = presence_penalty
        self._response_format = response_format
        self._seed = seed
        self._service_tier = service_tier
        self._stop = stop
        self._stream = stream
        self._stream_options = stream_options
        self._temperature = temperature
        self._top_p = top_p
        self._tools = tools
        self._tool_choice = tool_choice
        self._parallel_tool_calls = parallel_tool_calls
        self._user = user
        self._function_call = function_call
        self._functions = functions

    @classmethod
    def from_dict(cls, dikt) -> 'CreateChatCompletionRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CreateChatCompletionRequest of this CreateChatCompletionRequest.  # noqa: E501
        :rtype: CreateChatCompletionRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def messages(self) -> List[ChatCompletionRequestMessage]:
        """Gets the messages of this CreateChatCompletionRequest.

        A list of messages comprising the conversation so far. [Example Python code](https://cookbook.openai.com/examples/how_to_format_inputs_to_chatgpt_models).  # noqa: E501

        :return: The messages of this CreateChatCompletionRequest.
        :rtype: List[ChatCompletionRequestMessage]
        """
        return self._messages

    @messages.setter
    def messages(self, messages: List[ChatCompletionRequestMessage]):
        """Sets the messages of this CreateChatCompletionRequest.

        A list of messages comprising the conversation so far. [Example Python code](https://cookbook.openai.com/examples/how_to_format_inputs_to_chatgpt_models).  # noqa: E501

        :param messages: The messages of this CreateChatCompletionRequest.
        :type messages: List[ChatCompletionRequestMessage]
        """
        if messages is None:
            raise ValueError("Invalid value for `messages`, must not be `None`")  # noqa: E501
        if messages is not None and len(messages) < 1:
            raise ValueError("Invalid value for `messages`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._messages = messages

    @property
    def model(self) -> CreateChatCompletionRequestModel:
        """Gets the model of this CreateChatCompletionRequest.


        :return: The model of this CreateChatCompletionRequest.
        :rtype: CreateChatCompletionRequestModel
        """
        return self._model

    @model.setter
    def model(self, model: CreateChatCompletionRequestModel):
        """Sets the model of this CreateChatCompletionRequest.


        :param model: The model of this CreateChatCompletionRequest.
        :type model: CreateChatCompletionRequestModel
        """
        if model is None:
            raise ValueError("Invalid value for `model`, must not be `None`")  # noqa: E501

        self._model = model

    @property
    def frequency_penalty(self) -> float:
        """Gets the frequency_penalty of this CreateChatCompletionRequest.

        Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.  [See more information about frequency and presence penalties.](/docs/guides/text-generation/parameter-details)   # noqa: E501

        :return: The frequency_penalty of this CreateChatCompletionRequest.
        :rtype: float
        """
        return self._frequency_penalty

    @frequency_penalty.setter
    def frequency_penalty(self, frequency_penalty: float):
        """Sets the frequency_penalty of this CreateChatCompletionRequest.

        Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.  [See more information about frequency and presence penalties.](/docs/guides/text-generation/parameter-details)   # noqa: E501

        :param frequency_penalty: The frequency_penalty of this CreateChatCompletionRequest.
        :type frequency_penalty: float
        """
        if frequency_penalty is not None and frequency_penalty > 2:  # noqa: E501
            raise ValueError("Invalid value for `frequency_penalty`, must be a value less than or equal to `2`")  # noqa: E501
        if frequency_penalty is not None and frequency_penalty < -2:  # noqa: E501
            raise ValueError("Invalid value for `frequency_penalty`, must be a value greater than or equal to `-2`")  # noqa: E501

        self._frequency_penalty = frequency_penalty

    @property
    def logit_bias(self) -> Dict[str, int]:
        """Gets the logit_bias of this CreateChatCompletionRequest.

        Modify the likelihood of specified tokens appearing in the completion.  Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token.   # noqa: E501

        :return: The logit_bias of this CreateChatCompletionRequest.
        :rtype: Dict[str, int]
        """
        return self._logit_bias

    @logit_bias.setter
    def logit_bias(self, logit_bias: Dict[str, int]):
        """Sets the logit_bias of this CreateChatCompletionRequest.

        Modify the likelihood of specified tokens appearing in the completion.  Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token.   # noqa: E501

        :param logit_bias: The logit_bias of this CreateChatCompletionRequest.
        :type logit_bias: Dict[str, int]
        """

        self._logit_bias = logit_bias

    @property
    def logprobs(self) -> bool:
        """Gets the logprobs of this CreateChatCompletionRequest.

        Whether to return log probabilities of the output tokens or not. If true, returns the log probabilities of each output token returned in the `content` of `message`.  # noqa: E501

        :return: The logprobs of this CreateChatCompletionRequest.
        :rtype: bool
        """
        return self._logprobs

    @logprobs.setter
    def logprobs(self, logprobs: bool):
        """Sets the logprobs of this CreateChatCompletionRequest.

        Whether to return log probabilities of the output tokens or not. If true, returns the log probabilities of each output token returned in the `content` of `message`.  # noqa: E501

        :param logprobs: The logprobs of this CreateChatCompletionRequest.
        :type logprobs: bool
        """

        self._logprobs = logprobs

    @property
    def top_logprobs(self) -> int:
        """Gets the top_logprobs of this CreateChatCompletionRequest.

        An integer between 0 and 20 specifying the number of most likely tokens to return at each token position, each with an associated log probability. `logprobs` must be set to `true` if this parameter is used.  # noqa: E501

        :return: The top_logprobs of this CreateChatCompletionRequest.
        :rtype: int
        """
        return self._top_logprobs

    @top_logprobs.setter
    def top_logprobs(self, top_logprobs: int):
        """Sets the top_logprobs of this CreateChatCompletionRequest.

        An integer between 0 and 20 specifying the number of most likely tokens to return at each token position, each with an associated log probability. `logprobs` must be set to `true` if this parameter is used.  # noqa: E501

        :param top_logprobs: The top_logprobs of this CreateChatCompletionRequest.
        :type top_logprobs: int
        """
        if top_logprobs is not None and top_logprobs > 20:  # noqa: E501
            raise ValueError("Invalid value for `top_logprobs`, must be a value less than or equal to `20`")  # noqa: E501
        if top_logprobs is not None and top_logprobs < 0:  # noqa: E501
            raise ValueError("Invalid value for `top_logprobs`, must be a value greater than or equal to `0`")  # noqa: E501

        self._top_logprobs = top_logprobs

    @property
    def max_tokens(self) -> int:
        """Gets the max_tokens of this CreateChatCompletionRequest.

        The maximum number of [tokens](/tokenizer) that can be generated in the chat completion.  The total length of input tokens and generated tokens is limited by the model's context length. [Example Python code](https://cookbook.openai.com/examples/how_to_count_tokens_with_tiktoken) for counting tokens.   # noqa: E501

        :return: The max_tokens of this CreateChatCompletionRequest.
        :rtype: int
        """
        return self._max_tokens

    @max_tokens.setter
    def max_tokens(self, max_tokens: int):
        """Sets the max_tokens of this CreateChatCompletionRequest.

        The maximum number of [tokens](/tokenizer) that can be generated in the chat completion.  The total length of input tokens and generated tokens is limited by the model's context length. [Example Python code](https://cookbook.openai.com/examples/how_to_count_tokens_with_tiktoken) for counting tokens.   # noqa: E501

        :param max_tokens: The max_tokens of this CreateChatCompletionRequest.
        :type max_tokens: int
        """

        self._max_tokens = max_tokens

    @property
    def n(self) -> int:
        """Gets the n of this CreateChatCompletionRequest.

        How many chat completion choices to generate for each input message. Note that you will be charged based on the number of generated tokens across all of the choices. Keep `n` as `1` to minimize costs.  # noqa: E501

        :return: The n of this CreateChatCompletionRequest.
        :rtype: int
        """
        return self._n

    @n.setter
    def n(self, n: int):
        """Sets the n of this CreateChatCompletionRequest.

        How many chat completion choices to generate for each input message. Note that you will be charged based on the number of generated tokens across all of the choices. Keep `n` as `1` to minimize costs.  # noqa: E501

        :param n: The n of this CreateChatCompletionRequest.
        :type n: int
        """
        if n is not None and n > 128:  # noqa: E501
            raise ValueError("Invalid value for `n`, must be a value less than or equal to `128`")  # noqa: E501
        if n is not None and n < 1:  # noqa: E501
            raise ValueError("Invalid value for `n`, must be a value greater than or equal to `1`")  # noqa: E501

        self._n = n

    @property
    def presence_penalty(self) -> float:
        """Gets the presence_penalty of this CreateChatCompletionRequest.

        Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics.  [See more information about frequency and presence penalties.](/docs/guides/text-generation/parameter-details)   # noqa: E501

        :return: The presence_penalty of this CreateChatCompletionRequest.
        :rtype: float
        """
        return self._presence_penalty

    @presence_penalty.setter
    def presence_penalty(self, presence_penalty: float):
        """Sets the presence_penalty of this CreateChatCompletionRequest.

        Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics.  [See more information about frequency and presence penalties.](/docs/guides/text-generation/parameter-details)   # noqa: E501

        :param presence_penalty: The presence_penalty of this CreateChatCompletionRequest.
        :type presence_penalty: float
        """
        if presence_penalty is not None and presence_penalty > 2:  # noqa: E501
            raise ValueError("Invalid value for `presence_penalty`, must be a value less than or equal to `2`")  # noqa: E501
        if presence_penalty is not None and presence_penalty < -2:  # noqa: E501
            raise ValueError("Invalid value for `presence_penalty`, must be a value greater than or equal to `-2`")  # noqa: E501

        self._presence_penalty = presence_penalty

    @property
    def response_format(self) -> CreateChatCompletionRequestResponseFormat:
        """Gets the response_format of this CreateChatCompletionRequest.


        :return: The response_format of this CreateChatCompletionRequest.
        :rtype: CreateChatCompletionRequestResponseFormat
        """
        return self._response_format

    @response_format.setter
    def response_format(self, response_format: CreateChatCompletionRequestResponseFormat):
        """Sets the response_format of this CreateChatCompletionRequest.


        :param response_format: The response_format of this CreateChatCompletionRequest.
        :type response_format: CreateChatCompletionRequestResponseFormat
        """

        self._response_format = response_format

    @property
    def seed(self) -> int:
        """Gets the seed of this CreateChatCompletionRequest.

        This feature is in Beta. If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same `seed` and parameters should return the same result. Determinism is not guaranteed, and you should refer to the `system_fingerprint` response parameter to monitor changes in the backend.   # noqa: E501

        :return: The seed of this CreateChatCompletionRequest.
        :rtype: int
        """
        return self._seed

    @seed.setter
    def seed(self, seed: int):
        """Sets the seed of this CreateChatCompletionRequest.

        This feature is in Beta. If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same `seed` and parameters should return the same result. Determinism is not guaranteed, and you should refer to the `system_fingerprint` response parameter to monitor changes in the backend.   # noqa: E501

        :param seed: The seed of this CreateChatCompletionRequest.
        :type seed: int
        """
        if seed is not None and seed > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `seed`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if seed is not None and seed < -9223372036854775808:  # noqa: E501
            raise ValueError("Invalid value for `seed`, must be a value greater than or equal to `-9223372036854775808`")  # noqa: E501

        self._seed = seed

    @property
    def service_tier(self) -> str:
        """Gets the service_tier of this CreateChatCompletionRequest.

        Specifies the latency tier to use for processing the request. This parameter is relevant for customers subscribed to the scale tier service:   - If set to 'auto', the system will utilize scale tier credits until they are exhausted.   - If set to 'default', the request will be processed using the default service tier with a lower uptime SLA and no latency guarentee.    When this parameter is set, the response body will include the `service_tier` utilized.   # noqa: E501

        :return: The service_tier of this CreateChatCompletionRequest.
        :rtype: str
        """
        return self._service_tier

    @service_tier.setter
    def service_tier(self, service_tier: str):
        """Sets the service_tier of this CreateChatCompletionRequest.

        Specifies the latency tier to use for processing the request. This parameter is relevant for customers subscribed to the scale tier service:   - If set to 'auto', the system will utilize scale tier credits until they are exhausted.   - If set to 'default', the request will be processed using the default service tier with a lower uptime SLA and no latency guarentee.    When this parameter is set, the response body will include the `service_tier` utilized.   # noqa: E501

        :param service_tier: The service_tier of this CreateChatCompletionRequest.
        :type service_tier: str
        """
        allowed_values = [None,"auto", "default"]  # noqa: E501
        if service_tier not in allowed_values:
            raise ValueError(
                "Invalid value for `service_tier` ({0}), must be one of {1}"
                .format(service_tier, allowed_values)
            )

        self._service_tier = service_tier

    @property
    def stop(self) -> CreateChatCompletionRequestStop:
        """Gets the stop of this CreateChatCompletionRequest.


        :return: The stop of this CreateChatCompletionRequest.
        :rtype: CreateChatCompletionRequestStop
        """
        return self._stop

    @stop.setter
    def stop(self, stop: CreateChatCompletionRequestStop):
        """Sets the stop of this CreateChatCompletionRequest.


        :param stop: The stop of this CreateChatCompletionRequest.
        :type stop: CreateChatCompletionRequestStop
        """

        self._stop = stop

    @property
    def stream(self) -> bool:
        """Gets the stream of this CreateChatCompletionRequest.

        If set, partial message deltas will be sent, like in ChatGPT. Tokens will be sent as data-only [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format) as they become available, with the stream terminated by a `data: [DONE]` message. [Example Python code](https://cookbook.openai.com/examples/how_to_stream_completions).   # noqa: E501

        :return: The stream of this CreateChatCompletionRequest.
        :rtype: bool
        """
        return self._stream

    @stream.setter
    def stream(self, stream: bool):
        """Sets the stream of this CreateChatCompletionRequest.

        If set, partial message deltas will be sent, like in ChatGPT. Tokens will be sent as data-only [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format) as they become available, with the stream terminated by a `data: [DONE]` message. [Example Python code](https://cookbook.openai.com/examples/how_to_stream_completions).   # noqa: E501

        :param stream: The stream of this CreateChatCompletionRequest.
        :type stream: bool
        """

        self._stream = stream

    @property
    def stream_options(self) -> ChatCompletionStreamOptions:
        """Gets the stream_options of this CreateChatCompletionRequest.


        :return: The stream_options of this CreateChatCompletionRequest.
        :rtype: ChatCompletionStreamOptions
        """
        return self._stream_options

    @stream_options.setter
    def stream_options(self, stream_options: ChatCompletionStreamOptions):
        """Sets the stream_options of this CreateChatCompletionRequest.


        :param stream_options: The stream_options of this CreateChatCompletionRequest.
        :type stream_options: ChatCompletionStreamOptions
        """

        self._stream_options = stream_options

    @property
    def temperature(self) -> float:
        """Gets the temperature of this CreateChatCompletionRequest.

        What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.  We generally recommend altering this or `top_p` but not both.   # noqa: E501

        :return: The temperature of this CreateChatCompletionRequest.
        :rtype: float
        """
        return self._temperature

    @temperature.setter
    def temperature(self, temperature: float):
        """Sets the temperature of this CreateChatCompletionRequest.

        What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.  We generally recommend altering this or `top_p` but not both.   # noqa: E501

        :param temperature: The temperature of this CreateChatCompletionRequest.
        :type temperature: float
        """
        if temperature is not None and temperature > 2:  # noqa: E501
            raise ValueError("Invalid value for `temperature`, must be a value less than or equal to `2`")  # noqa: E501
        if temperature is not None and temperature < 0:  # noqa: E501
            raise ValueError("Invalid value for `temperature`, must be a value greater than or equal to `0`")  # noqa: E501

        self._temperature = temperature

    @property
    def top_p(self) -> float:
        """Gets the top_p of this CreateChatCompletionRequest.

        An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.  We generally recommend altering this or `temperature` but not both.   # noqa: E501

        :return: The top_p of this CreateChatCompletionRequest.
        :rtype: float
        """
        return self._top_p

    @top_p.setter
    def top_p(self, top_p: float):
        """Sets the top_p of this CreateChatCompletionRequest.

        An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.  We generally recommend altering this or `temperature` but not both.   # noqa: E501

        :param top_p: The top_p of this CreateChatCompletionRequest.
        :type top_p: float
        """
        if top_p is not None and top_p > 1:  # noqa: E501
            raise ValueError("Invalid value for `top_p`, must be a value less than or equal to `1`")  # noqa: E501
        if top_p is not None and top_p < 0:  # noqa: E501
            raise ValueError("Invalid value for `top_p`, must be a value greater than or equal to `0`")  # noqa: E501

        self._top_p = top_p

    @property
    def tools(self) -> List[ChatCompletionTool]:
        """Gets the tools of this CreateChatCompletionRequest.

        A list of tools the model may call. Currently, only functions are supported as a tool. Use this to provide a list of functions the model may generate JSON inputs for. A max of 128 functions are supported.   # noqa: E501

        :return: The tools of this CreateChatCompletionRequest.
        :rtype: List[ChatCompletionTool]
        """
        return self._tools

    @tools.setter
    def tools(self, tools: List[ChatCompletionTool]):
        """Sets the tools of this CreateChatCompletionRequest.

        A list of tools the model may call. Currently, only functions are supported as a tool. Use this to provide a list of functions the model may generate JSON inputs for. A max of 128 functions are supported.   # noqa: E501

        :param tools: The tools of this CreateChatCompletionRequest.
        :type tools: List[ChatCompletionTool]
        """

        self._tools = tools

    @property
    def tool_choice(self) -> ChatCompletionToolChoiceOption:
        """Gets the tool_choice of this CreateChatCompletionRequest.


        :return: The tool_choice of this CreateChatCompletionRequest.
        :rtype: ChatCompletionToolChoiceOption
        """
        return self._tool_choice

    @tool_choice.setter
    def tool_choice(self, tool_choice: ChatCompletionToolChoiceOption):
        """Sets the tool_choice of this CreateChatCompletionRequest.


        :param tool_choice: The tool_choice of this CreateChatCompletionRequest.
        :type tool_choice: ChatCompletionToolChoiceOption
        """

        self._tool_choice = tool_choice

    @property
    def parallel_tool_calls(self) -> bool:
        """Gets the parallel_tool_calls of this CreateChatCompletionRequest.

        Whether to enable [parallel function calling](/docs/guides/function-calling/parallel-function-calling) during tool use.  # noqa: E501

        :return: The parallel_tool_calls of this CreateChatCompletionRequest.
        :rtype: bool
        """
        return self._parallel_tool_calls

    @parallel_tool_calls.setter
    def parallel_tool_calls(self, parallel_tool_calls: bool):
        """Sets the parallel_tool_calls of this CreateChatCompletionRequest.

        Whether to enable [parallel function calling](/docs/guides/function-calling/parallel-function-calling) during tool use.  # noqa: E501

        :param parallel_tool_calls: The parallel_tool_calls of this CreateChatCompletionRequest.
        :type parallel_tool_calls: bool
        """

        self._parallel_tool_calls = parallel_tool_calls

    @property
    def user(self) -> str:
        """Gets the user of this CreateChatCompletionRequest.

        A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse. [Learn more](/docs/guides/safety-best-practices/end-user-ids).   # noqa: E501

        :return: The user of this CreateChatCompletionRequest.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user: str):
        """Sets the user of this CreateChatCompletionRequest.

        A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse. [Learn more](/docs/guides/safety-best-practices/end-user-ids).   # noqa: E501

        :param user: The user of this CreateChatCompletionRequest.
        :type user: str
        """

        self._user = user

    @property
    def function_call(self) -> CreateChatCompletionRequestFunctionCall:
        """Gets the function_call of this CreateChatCompletionRequest.


        :return: The function_call of this CreateChatCompletionRequest.
        :rtype: CreateChatCompletionRequestFunctionCall
        """
        return self._function_call

    @function_call.setter
    def function_call(self, function_call: CreateChatCompletionRequestFunctionCall):
        """Sets the function_call of this CreateChatCompletionRequest.


        :param function_call: The function_call of this CreateChatCompletionRequest.
        :type function_call: CreateChatCompletionRequestFunctionCall
        """

        self._function_call = function_call

    @property
    def functions(self) -> List[ChatCompletionFunctions]:
        """Gets the functions of this CreateChatCompletionRequest.

        Deprecated in favor of `tools`.  A list of functions the model may generate JSON inputs for.   # noqa: E501

        :return: The functions of this CreateChatCompletionRequest.
        :rtype: List[ChatCompletionFunctions]
        """
        return self._functions

    @functions.setter
    def functions(self, functions: List[ChatCompletionFunctions]):
        """Sets the functions of this CreateChatCompletionRequest.

        Deprecated in favor of `tools`.  A list of functions the model may generate JSON inputs for.   # noqa: E501

        :param functions: The functions of this CreateChatCompletionRequest.
        :type functions: List[ChatCompletionFunctions]
        """
        if functions is not None and len(functions) > 128:
            raise ValueError("Invalid value for `functions`, number of items must be less than or equal to `128`")  # noqa: E501
        if functions is not None and len(functions) < 1:
            raise ValueError("Invalid value for `functions`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._functions = functions