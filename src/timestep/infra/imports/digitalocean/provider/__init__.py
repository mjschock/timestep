'''
# `provider`

Refer to the Terraform Registory for docs: [`digitalocean`](https://www.terraform.io/docs/providers/digitalocean).
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from .._jsii import *

import cdktf as _cdktf_9a9027ec
import constructs as _constructs_77d1e7e8


class DigitaloceanProvider(
    _cdktf_9a9027ec.TerraformProvider,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.provider.DigitaloceanProvider",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/digitalocean digitalocean}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        alias: typing.Optional[builtins.str] = None,
        api_endpoint: typing.Optional[builtins.str] = None,
        http_retry_max: typing.Optional[jsii.Number] = None,
        http_retry_wait_max: typing.Optional[jsii.Number] = None,
        http_retry_wait_min: typing.Optional[jsii.Number] = None,
        requests_per_second: typing.Optional[jsii.Number] = None,
        spaces_access_id: typing.Optional[builtins.str] = None,
        spaces_endpoint: typing.Optional[builtins.str] = None,
        spaces_secret_key: typing.Optional[builtins.str] = None,
        token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/digitalocean digitalocean} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean#alias DigitaloceanProvider#alias}
        :param api_endpoint: The URL to use for the DigitalOcean API. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean#api_endpoint DigitaloceanProvider#api_endpoint}
        :param http_retry_max: The maximum number of retries on a failed API request. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean#http_retry_max DigitaloceanProvider#http_retry_max}
        :param http_retry_wait_max: The maximum wait time (in seconds) between failed API requests. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean#http_retry_wait_max DigitaloceanProvider#http_retry_wait_max}
        :param http_retry_wait_min: The minimum wait time (in seconds) between failed API requests. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean#http_retry_wait_min DigitaloceanProvider#http_retry_wait_min}
        :param requests_per_second: The rate of requests per second to limit the HTTP client. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean#requests_per_second DigitaloceanProvider#requests_per_second}
        :param spaces_access_id: The access key ID for Spaces API operations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean#spaces_access_id DigitaloceanProvider#spaces_access_id}
        :param spaces_endpoint: The URL to use for the DigitalOcean Spaces API. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean#spaces_endpoint DigitaloceanProvider#spaces_endpoint}
        :param spaces_secret_key: The secret access key for Spaces API operations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean#spaces_secret_key DigitaloceanProvider#spaces_secret_key}
        :param token: The token key for API operations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean#token DigitaloceanProvider#token}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37aca39c60bf013192f0de47b37cf69c010976b0230411789b839f95129d385c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = DigitaloceanProviderConfig(
            alias=alias,
            api_endpoint=api_endpoint,
            http_retry_max=http_retry_max,
            http_retry_wait_max=http_retry_wait_max,
            http_retry_wait_min=http_retry_wait_min,
            requests_per_second=requests_per_second,
            spaces_access_id=spaces_access_id,
            spaces_endpoint=spaces_endpoint,
            spaces_secret_key=spaces_secret_key,
            token=token,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetAlias")
    def reset_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlias", []))

    @jsii.member(jsii_name="resetApiEndpoint")
    def reset_api_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApiEndpoint", []))

    @jsii.member(jsii_name="resetHttpRetryMax")
    def reset_http_retry_max(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpRetryMax", []))

    @jsii.member(jsii_name="resetHttpRetryWaitMax")
    def reset_http_retry_wait_max(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpRetryWaitMax", []))

    @jsii.member(jsii_name="resetHttpRetryWaitMin")
    def reset_http_retry_wait_min(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpRetryWaitMin", []))

    @jsii.member(jsii_name="resetRequestsPerSecond")
    def reset_requests_per_second(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestsPerSecond", []))

    @jsii.member(jsii_name="resetSpacesAccessId")
    def reset_spaces_access_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSpacesAccessId", []))

    @jsii.member(jsii_name="resetSpacesEndpoint")
    def reset_spaces_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSpacesEndpoint", []))

    @jsii.member(jsii_name="resetSpacesSecretKey")
    def reset_spaces_secret_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSpacesSecretKey", []))

    @jsii.member(jsii_name="resetToken")
    def reset_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetToken", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="aliasInput")
    def alias_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aliasInput"))

    @builtins.property
    @jsii.member(jsii_name="apiEndpointInput")
    def api_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="httpRetryMaxInput")
    def http_retry_max_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "httpRetryMaxInput"))

    @builtins.property
    @jsii.member(jsii_name="httpRetryWaitMaxInput")
    def http_retry_wait_max_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "httpRetryWaitMaxInput"))

    @builtins.property
    @jsii.member(jsii_name="httpRetryWaitMinInput")
    def http_retry_wait_min_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "httpRetryWaitMinInput"))

    @builtins.property
    @jsii.member(jsii_name="requestsPerSecondInput")
    def requests_per_second_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "requestsPerSecondInput"))

    @builtins.property
    @jsii.member(jsii_name="spacesAccessIdInput")
    def spaces_access_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "spacesAccessIdInput"))

    @builtins.property
    @jsii.member(jsii_name="spacesEndpointInput")
    def spaces_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "spacesEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="spacesSecretKeyInput")
    def spaces_secret_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "spacesSecretKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenInput")
    def token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenInput"))

    @builtins.property
    @jsii.member(jsii_name="alias")
    def alias(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alias"))

    @alias.setter
    def alias(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9fd13e68fb1fc7204d9bf0476c18feeceb20453aecdc51450383876f0ba70abc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alias", value)

    @builtins.property
    @jsii.member(jsii_name="apiEndpoint")
    def api_endpoint(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiEndpoint"))

    @api_endpoint.setter
    def api_endpoint(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a27c2e1f87e360d0cf3d6a5c7a2534c85b46da6cff271dd1ffa95f44435821c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="httpRetryMax")
    def http_retry_max(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "httpRetryMax"))

    @http_retry_max.setter
    def http_retry_max(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b899134b72364bcfdf89567ce2585a91eccbad4d2f799ffb3d35fe7dce436f22)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpRetryMax", value)

    @builtins.property
    @jsii.member(jsii_name="httpRetryWaitMax")
    def http_retry_wait_max(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "httpRetryWaitMax"))

    @http_retry_wait_max.setter
    def http_retry_wait_max(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1285ab7e49f6fdd0a91a5ebcaf2e81c5cfb7544a008cd099fe7d4395991e3572)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpRetryWaitMax", value)

    @builtins.property
    @jsii.member(jsii_name="httpRetryWaitMin")
    def http_retry_wait_min(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "httpRetryWaitMin"))

    @http_retry_wait_min.setter
    def http_retry_wait_min(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__805803b6fa7d4bd3f5e4860418695743989d7f68ff030749c23d567f8862b669)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpRetryWaitMin", value)

    @builtins.property
    @jsii.member(jsii_name="requestsPerSecond")
    def requests_per_second(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "requestsPerSecond"))

    @requests_per_second.setter
    def requests_per_second(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f34202919204d9c84d4fc87bb09dbff22f4069a37c47994d4b2321f21ff46e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestsPerSecond", value)

    @builtins.property
    @jsii.member(jsii_name="spacesAccessId")
    def spaces_access_id(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "spacesAccessId"))

    @spaces_access_id.setter
    def spaces_access_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__770ee09975f7d1d4445600042f1c178b5e456ac21560e0e8f0999393341b2d54)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spacesAccessId", value)

    @builtins.property
    @jsii.member(jsii_name="spacesEndpoint")
    def spaces_endpoint(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "spacesEndpoint"))

    @spaces_endpoint.setter
    def spaces_endpoint(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aee9ff097b08a0e59d15c9d299e620cacc23de782f940bcf24a6a3e5a1e40158)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spacesEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="spacesSecretKey")
    def spaces_secret_key(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "spacesSecretKey"))

    @spaces_secret_key.setter
    def spaces_secret_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f17164bf6387001bfc829b9753aea1e48405aebac6781868e75988021ea9e4d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spacesSecretKey", value)

    @builtins.property
    @jsii.member(jsii_name="token")
    def token(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "token"))

    @token.setter
    def token(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ad0d39aa38cdd6b078d4256e9714611050b76259737abe91679a9152ec30d22)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "token", value)


@jsii.data_type(
    jsii_type="digitalocean.provider.DigitaloceanProviderConfig",
    jsii_struct_bases=[],
    name_mapping={
        "alias": "alias",
        "api_endpoint": "apiEndpoint",
        "http_retry_max": "httpRetryMax",
        "http_retry_wait_max": "httpRetryWaitMax",
        "http_retry_wait_min": "httpRetryWaitMin",
        "requests_per_second": "requestsPerSecond",
        "spaces_access_id": "spacesAccessId",
        "spaces_endpoint": "spacesEndpoint",
        "spaces_secret_key": "spacesSecretKey",
        "token": "token",
    },
)
class DigitaloceanProviderConfig:
    def __init__(
        self,
        *,
        alias: typing.Optional[builtins.str] = None,
        api_endpoint: typing.Optional[builtins.str] = None,
        http_retry_max: typing.Optional[jsii.Number] = None,
        http_retry_wait_max: typing.Optional[jsii.Number] = None,
        http_retry_wait_min: typing.Optional[jsii.Number] = None,
        requests_per_second: typing.Optional[jsii.Number] = None,
        spaces_access_id: typing.Optional[builtins.str] = None,
        spaces_endpoint: typing.Optional[builtins.str] = None,
        spaces_secret_key: typing.Optional[builtins.str] = None,
        token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean#alias DigitaloceanProvider#alias}
        :param api_endpoint: The URL to use for the DigitalOcean API. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean#api_endpoint DigitaloceanProvider#api_endpoint}
        :param http_retry_max: The maximum number of retries on a failed API request. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean#http_retry_max DigitaloceanProvider#http_retry_max}
        :param http_retry_wait_max: The maximum wait time (in seconds) between failed API requests. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean#http_retry_wait_max DigitaloceanProvider#http_retry_wait_max}
        :param http_retry_wait_min: The minimum wait time (in seconds) between failed API requests. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean#http_retry_wait_min DigitaloceanProvider#http_retry_wait_min}
        :param requests_per_second: The rate of requests per second to limit the HTTP client. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean#requests_per_second DigitaloceanProvider#requests_per_second}
        :param spaces_access_id: The access key ID for Spaces API operations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean#spaces_access_id DigitaloceanProvider#spaces_access_id}
        :param spaces_endpoint: The URL to use for the DigitalOcean Spaces API. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean#spaces_endpoint DigitaloceanProvider#spaces_endpoint}
        :param spaces_secret_key: The secret access key for Spaces API operations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean#spaces_secret_key DigitaloceanProvider#spaces_secret_key}
        :param token: The token key for API operations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean#token DigitaloceanProvider#token}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2024831e6f341e4c23b2b485c0754309455893369abf4845e11f68b5ee6ba8f6)
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
            check_type(argname="argument api_endpoint", value=api_endpoint, expected_type=type_hints["api_endpoint"])
            check_type(argname="argument http_retry_max", value=http_retry_max, expected_type=type_hints["http_retry_max"])
            check_type(argname="argument http_retry_wait_max", value=http_retry_wait_max, expected_type=type_hints["http_retry_wait_max"])
            check_type(argname="argument http_retry_wait_min", value=http_retry_wait_min, expected_type=type_hints["http_retry_wait_min"])
            check_type(argname="argument requests_per_second", value=requests_per_second, expected_type=type_hints["requests_per_second"])
            check_type(argname="argument spaces_access_id", value=spaces_access_id, expected_type=type_hints["spaces_access_id"])
            check_type(argname="argument spaces_endpoint", value=spaces_endpoint, expected_type=type_hints["spaces_endpoint"])
            check_type(argname="argument spaces_secret_key", value=spaces_secret_key, expected_type=type_hints["spaces_secret_key"])
            check_type(argname="argument token", value=token, expected_type=type_hints["token"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if alias is not None:
            self._values["alias"] = alias
        if api_endpoint is not None:
            self._values["api_endpoint"] = api_endpoint
        if http_retry_max is not None:
            self._values["http_retry_max"] = http_retry_max
        if http_retry_wait_max is not None:
            self._values["http_retry_wait_max"] = http_retry_wait_max
        if http_retry_wait_min is not None:
            self._values["http_retry_wait_min"] = http_retry_wait_min
        if requests_per_second is not None:
            self._values["requests_per_second"] = requests_per_second
        if spaces_access_id is not None:
            self._values["spaces_access_id"] = spaces_access_id
        if spaces_endpoint is not None:
            self._values["spaces_endpoint"] = spaces_endpoint
        if spaces_secret_key is not None:
            self._values["spaces_secret_key"] = spaces_secret_key
        if token is not None:
            self._values["token"] = token

    @builtins.property
    def alias(self) -> typing.Optional[builtins.str]:
        '''Alias name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean#alias DigitaloceanProvider#alias}
        '''
        result = self._values.get("alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def api_endpoint(self) -> typing.Optional[builtins.str]:
        '''The URL to use for the DigitalOcean API.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean#api_endpoint DigitaloceanProvider#api_endpoint}
        '''
        result = self._values.get("api_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def http_retry_max(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of retries on a failed API request.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean#http_retry_max DigitaloceanProvider#http_retry_max}
        '''
        result = self._values.get("http_retry_max")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def http_retry_wait_max(self) -> typing.Optional[jsii.Number]:
        '''The maximum wait time (in seconds) between failed API requests.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean#http_retry_wait_max DigitaloceanProvider#http_retry_wait_max}
        '''
        result = self._values.get("http_retry_wait_max")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def http_retry_wait_min(self) -> typing.Optional[jsii.Number]:
        '''The minimum wait time (in seconds) between failed API requests.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean#http_retry_wait_min DigitaloceanProvider#http_retry_wait_min}
        '''
        result = self._values.get("http_retry_wait_min")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def requests_per_second(self) -> typing.Optional[jsii.Number]:
        '''The rate of requests per second to limit the HTTP client.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean#requests_per_second DigitaloceanProvider#requests_per_second}
        '''
        result = self._values.get("requests_per_second")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def spaces_access_id(self) -> typing.Optional[builtins.str]:
        '''The access key ID for Spaces API operations.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean#spaces_access_id DigitaloceanProvider#spaces_access_id}
        '''
        result = self._values.get("spaces_access_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def spaces_endpoint(self) -> typing.Optional[builtins.str]:
        '''The URL to use for the DigitalOcean Spaces API.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean#spaces_endpoint DigitaloceanProvider#spaces_endpoint}
        '''
        result = self._values.get("spaces_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def spaces_secret_key(self) -> typing.Optional[builtins.str]:
        '''The secret access key for Spaces API operations.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean#spaces_secret_key DigitaloceanProvider#spaces_secret_key}
        '''
        result = self._values.get("spaces_secret_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def token(self) -> typing.Optional[builtins.str]:
        '''The token key for API operations.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean#token DigitaloceanProvider#token}
        '''
        result = self._values.get("token")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DigitaloceanProviderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DigitaloceanProvider",
    "DigitaloceanProviderConfig",
]

publication.publish()

def _typecheckingstub__37aca39c60bf013192f0de47b37cf69c010976b0230411789b839f95129d385c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    alias: typing.Optional[builtins.str] = None,
    api_endpoint: typing.Optional[builtins.str] = None,
    http_retry_max: typing.Optional[jsii.Number] = None,
    http_retry_wait_max: typing.Optional[jsii.Number] = None,
    http_retry_wait_min: typing.Optional[jsii.Number] = None,
    requests_per_second: typing.Optional[jsii.Number] = None,
    spaces_access_id: typing.Optional[builtins.str] = None,
    spaces_endpoint: typing.Optional[builtins.str] = None,
    spaces_secret_key: typing.Optional[builtins.str] = None,
    token: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fd13e68fb1fc7204d9bf0476c18feeceb20453aecdc51450383876f0ba70abc(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a27c2e1f87e360d0cf3d6a5c7a2534c85b46da6cff271dd1ffa95f44435821c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b899134b72364bcfdf89567ce2585a91eccbad4d2f799ffb3d35fe7dce436f22(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1285ab7e49f6fdd0a91a5ebcaf2e81c5cfb7544a008cd099fe7d4395991e3572(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__805803b6fa7d4bd3f5e4860418695743989d7f68ff030749c23d567f8862b669(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f34202919204d9c84d4fc87bb09dbff22f4069a37c47994d4b2321f21ff46e6(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__770ee09975f7d1d4445600042f1c178b5e456ac21560e0e8f0999393341b2d54(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aee9ff097b08a0e59d15c9d299e620cacc23de782f940bcf24a6a3e5a1e40158(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f17164bf6387001bfc829b9753aea1e48405aebac6781868e75988021ea9e4d6(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ad0d39aa38cdd6b078d4256e9714611050b76259737abe91679a9152ec30d22(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2024831e6f341e4c23b2b485c0754309455893369abf4845e11f68b5ee6ba8f6(
    *,
    alias: typing.Optional[builtins.str] = None,
    api_endpoint: typing.Optional[builtins.str] = None,
    http_retry_max: typing.Optional[jsii.Number] = None,
    http_retry_wait_max: typing.Optional[jsii.Number] = None,
    http_retry_wait_min: typing.Optional[jsii.Number] = None,
    requests_per_second: typing.Optional[jsii.Number] = None,
    spaces_access_id: typing.Optional[builtins.str] = None,
    spaces_endpoint: typing.Optional[builtins.str] = None,
    spaces_secret_key: typing.Optional[builtins.str] = None,
    token: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
