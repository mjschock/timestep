'''
# `provider`

Refer to the Terraform Registory for docs: [`supabase`](https://registry.terraform.io/providers/supabase/supabase/1.4.0/docs).
'''
from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)

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


class SupabaseProvider(
    _cdktf_9a9027ec.TerraformProvider,
    metaclass=jsii.JSIIMeta,
    jsii_type="supabase.provider.SupabaseProvider",
):
    '''Represents a {@link https://registry.terraform.io/providers/supabase/supabase/1.4.0/docs supabase}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        access_token: typing.Optional[builtins.str] = None,
        alias: typing.Optional[builtins.str] = None,
        endpoint: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/supabase/supabase/1.4.0/docs supabase} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param access_token: Supabase access token. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/supabase/supabase/1.4.0/docs#access_token SupabaseProvider#access_token}
        :param alias: Alias name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/supabase/supabase/1.4.0/docs#alias SupabaseProvider#alias}
        :param endpoint: Supabase API endpoint. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/supabase/supabase/1.4.0/docs#endpoint SupabaseProvider#endpoint}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bba1f5e9d2e13739e01c03711bce88af9fdaf36d359ccac8d4a83b7acf07d6a9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = SupabaseProviderConfig(
            access_token=access_token, alias=alias, endpoint=endpoint
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="generateConfigForImport")
    @builtins.classmethod
    def generate_config_for_import(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        import_to_id: builtins.str,
        import_from_id: builtins.str,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    ) -> _cdktf_9a9027ec.ImportableResource:
        '''Generates CDKTF code for importing a SupabaseProvider resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the SupabaseProvider to import.
        :param import_from_id: The id of the existing SupabaseProvider that should be imported. Refer to the {@link https://registry.terraform.io/providers/supabase/supabase/1.4.0/docs#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the SupabaseProvider to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3be9c7283ac6c766faf9bdc2e52f282dea5f108e979d1b98cd87b373259733e2)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="resetAccessToken")
    def reset_access_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessToken", []))

    @jsii.member(jsii_name="resetAlias")
    def reset_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlias", []))

    @jsii.member(jsii_name="resetEndpoint")
    def reset_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndpoint", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="accessTokenInput")
    def access_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="aliasInput")
    def alias_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aliasInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointInput")
    def endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointInput"))

    @builtins.property
    @jsii.member(jsii_name="accessToken")
    def access_token(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessToken"))

    @access_token.setter
    def access_token(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49eb79e6cfe6f2e024244c4d89a3e6a58cc0e2839c87718ffe3ce2ebd592813f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessToken", value)

    @builtins.property
    @jsii.member(jsii_name="alias")
    def alias(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alias"))

    @alias.setter
    def alias(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c03b25452798c860c8064cdc9c1b9eb797c39b78dfa3a13f75823d9f4da832a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alias", value)

    @builtins.property
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpoint"))

    @endpoint.setter
    def endpoint(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2bc19da6df4c24191ee151df40eebd500fc7aab419398d4d17fa3f86ad2bf4e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpoint", value)


@jsii.data_type(
    jsii_type="supabase.provider.SupabaseProviderConfig",
    jsii_struct_bases=[],
    name_mapping={
        "access_token": "accessToken",
        "alias": "alias",
        "endpoint": "endpoint",
    },
)
class SupabaseProviderConfig:
    def __init__(
        self,
        *,
        access_token: typing.Optional[builtins.str] = None,
        alias: typing.Optional[builtins.str] = None,
        endpoint: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param access_token: Supabase access token. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/supabase/supabase/1.4.0/docs#access_token SupabaseProvider#access_token}
        :param alias: Alias name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/supabase/supabase/1.4.0/docs#alias SupabaseProvider#alias}
        :param endpoint: Supabase API endpoint. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/supabase/supabase/1.4.0/docs#endpoint SupabaseProvider#endpoint}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1526c1e02f50bc83e6806d6e7564c8822719d14bf23b81752976ca78ad79257)
            check_type(argname="argument access_token", value=access_token, expected_type=type_hints["access_token"])
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
            check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if access_token is not None:
            self._values["access_token"] = access_token
        if alias is not None:
            self._values["alias"] = alias
        if endpoint is not None:
            self._values["endpoint"] = endpoint

    @builtins.property
    def access_token(self) -> typing.Optional[builtins.str]:
        '''Supabase access token.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/supabase/supabase/1.4.0/docs#access_token SupabaseProvider#access_token}
        '''
        result = self._values.get("access_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def alias(self) -> typing.Optional[builtins.str]:
        '''Alias name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/supabase/supabase/1.4.0/docs#alias SupabaseProvider#alias}
        '''
        result = self._values.get("alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def endpoint(self) -> typing.Optional[builtins.str]:
        '''Supabase API endpoint.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/supabase/supabase/1.4.0/docs#endpoint SupabaseProvider#endpoint}
        '''
        result = self._values.get("endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SupabaseProviderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "SupabaseProvider",
    "SupabaseProviderConfig",
]

publication.publish()

def _typecheckingstub__bba1f5e9d2e13739e01c03711bce88af9fdaf36d359ccac8d4a83b7acf07d6a9(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    access_token: typing.Optional[builtins.str] = None,
    alias: typing.Optional[builtins.str] = None,
    endpoint: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3be9c7283ac6c766faf9bdc2e52f282dea5f108e979d1b98cd87b373259733e2(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49eb79e6cfe6f2e024244c4d89a3e6a58cc0e2839c87718ffe3ce2ebd592813f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c03b25452798c860c8064cdc9c1b9eb797c39b78dfa3a13f75823d9f4da832a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bc19da6df4c24191ee151df40eebd500fc7aab419398d4d17fa3f86ad2bf4e7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1526c1e02f50bc83e6806d6e7564c8822719d14bf23b81752976ca78ad79257(
    *,
    access_token: typing.Optional[builtins.str] = None,
    alias: typing.Optional[builtins.str] = None,
    endpoint: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
