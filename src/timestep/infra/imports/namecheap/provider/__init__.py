'''
# `provider`

Refer to the Terraform Registory for docs: [`namecheap`](https://registry.terraform.io/providers/namecheap/namecheap/2.1.0/docs).
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


class NamecheapProvider(
    _cdktf_9a9027ec.TerraformProvider,
    metaclass=jsii.JSIIMeta,
    jsii_type="namecheap.provider.NamecheapProvider",
):
    '''Represents a {@link https://registry.terraform.io/providers/namecheap/namecheap/2.1.0/docs namecheap}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        api_key: builtins.str,
        api_user: builtins.str,
        user_name: builtins.str,
        alias: typing.Optional[builtins.str] = None,
        client_ip: typing.Optional[builtins.str] = None,
        use_sandbox: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/namecheap/namecheap/2.1.0/docs namecheap} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param api_key: The namecheap API key. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/namecheap/namecheap/2.1.0/docs#api_key NamecheapProvider#api_key}
        :param api_user: A registered api user for namecheap. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/namecheap/namecheap/2.1.0/docs#api_user NamecheapProvider#api_user}
        :param user_name: A registered user name for namecheap. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/namecheap/namecheap/2.1.0/docs#user_name NamecheapProvider#user_name}
        :param alias: Alias name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/namecheap/namecheap/2.1.0/docs#alias NamecheapProvider#alias}
        :param client_ip: Client IP address. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/namecheap/namecheap/2.1.0/docs#client_ip NamecheapProvider#client_ip}
        :param use_sandbox: Use sandbox API endpoints. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/namecheap/namecheap/2.1.0/docs#use_sandbox NamecheapProvider#use_sandbox}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e8296e4cd4ed43ef2fb357d86c488288a909c4655223c3ace96996d1483bf59)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = NamecheapProviderConfig(
            api_key=api_key,
            api_user=api_user,
            user_name=user_name,
            alias=alias,
            client_ip=client_ip,
            use_sandbox=use_sandbox,
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
        '''Generates CDKTF code for importing a NamecheapProvider resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the NamecheapProvider to import.
        :param import_from_id: The id of the existing NamecheapProvider that should be imported. Refer to the {@link https://registry.terraform.io/providers/namecheap/namecheap/2.1.0/docs#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the NamecheapProvider to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9fa3bda4281148660778fe89fd10a29e7dc67efc06cacb926c6ef7b498133bbf)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="resetAlias")
    def reset_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlias", []))

    @jsii.member(jsii_name="resetClientIp")
    def reset_client_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientIp", []))

    @jsii.member(jsii_name="resetUseSandbox")
    def reset_use_sandbox(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseSandbox", []))

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
    @jsii.member(jsii_name="apiKeyInput")
    def api_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="apiUserInput")
    def api_user_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiUserInput"))

    @builtins.property
    @jsii.member(jsii_name="clientIpInput")
    def client_ip_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIpInput"))

    @builtins.property
    @jsii.member(jsii_name="userNameInput")
    def user_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userNameInput"))

    @builtins.property
    @jsii.member(jsii_name="useSandboxInput")
    def use_sandbox_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "useSandboxInput"))

    @builtins.property
    @jsii.member(jsii_name="alias")
    def alias(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alias"))

    @alias.setter
    def alias(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c853e2215e5e4193e0e779bd5cad7b563dad9b076879d4b15ce0f8241418bb66)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alias", value)

    @builtins.property
    @jsii.member(jsii_name="apiKey")
    def api_key(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiKey"))

    @api_key.setter
    def api_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b2844e4214d768a5c6c2a3f0d1890d15b5d175a5a9718249246ef32ed1c3664)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiKey", value)

    @builtins.property
    @jsii.member(jsii_name="apiUser")
    def api_user(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiUser"))

    @api_user.setter
    def api_user(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0bda5570cd10f30f90fdd3e8431c717ebf719eaf30cc57d477ddc2af49606eef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiUser", value)

    @builtins.property
    @jsii.member(jsii_name="clientIp")
    def client_ip(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIp"))

    @client_ip.setter
    def client_ip(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ad1fa9574e708be6128b8fd15481e16b84292270569b5da851a26f3d839d27b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientIp", value)

    @builtins.property
    @jsii.member(jsii_name="userName")
    def user_name(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userName"))

    @user_name.setter
    def user_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bccefd916ae5a0e785a449f0d7c1796c5fb3a8b9343ade511cd7ceb2a3083ac5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userName", value)

    @builtins.property
    @jsii.member(jsii_name="useSandbox")
    def use_sandbox(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "useSandbox"))

    @use_sandbox.setter
    def use_sandbox(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a1902c95ed0e4284ef571896b023f7a0ab2f66adaf2cd17c07ce0464a9daf82)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useSandbox", value)


@jsii.data_type(
    jsii_type="namecheap.provider.NamecheapProviderConfig",
    jsii_struct_bases=[],
    name_mapping={
        "api_key": "apiKey",
        "api_user": "apiUser",
        "user_name": "userName",
        "alias": "alias",
        "client_ip": "clientIp",
        "use_sandbox": "useSandbox",
    },
)
class NamecheapProviderConfig:
    def __init__(
        self,
        *,
        api_key: builtins.str,
        api_user: builtins.str,
        user_name: builtins.str,
        alias: typing.Optional[builtins.str] = None,
        client_ip: typing.Optional[builtins.str] = None,
        use_sandbox: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param api_key: The namecheap API key. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/namecheap/namecheap/2.1.0/docs#api_key NamecheapProvider#api_key}
        :param api_user: A registered api user for namecheap. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/namecheap/namecheap/2.1.0/docs#api_user NamecheapProvider#api_user}
        :param user_name: A registered user name for namecheap. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/namecheap/namecheap/2.1.0/docs#user_name NamecheapProvider#user_name}
        :param alias: Alias name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/namecheap/namecheap/2.1.0/docs#alias NamecheapProvider#alias}
        :param client_ip: Client IP address. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/namecheap/namecheap/2.1.0/docs#client_ip NamecheapProvider#client_ip}
        :param use_sandbox: Use sandbox API endpoints. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/namecheap/namecheap/2.1.0/docs#use_sandbox NamecheapProvider#use_sandbox}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2bbe67cb9997df680cfc0ead837d5c20cf2b21da7a92e63a090950d3fc9bc5d9)
            check_type(argname="argument api_key", value=api_key, expected_type=type_hints["api_key"])
            check_type(argname="argument api_user", value=api_user, expected_type=type_hints["api_user"])
            check_type(argname="argument user_name", value=user_name, expected_type=type_hints["user_name"])
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
            check_type(argname="argument client_ip", value=client_ip, expected_type=type_hints["client_ip"])
            check_type(argname="argument use_sandbox", value=use_sandbox, expected_type=type_hints["use_sandbox"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_key": api_key,
            "api_user": api_user,
            "user_name": user_name,
        }
        if alias is not None:
            self._values["alias"] = alias
        if client_ip is not None:
            self._values["client_ip"] = client_ip
        if use_sandbox is not None:
            self._values["use_sandbox"] = use_sandbox

    @builtins.property
    def api_key(self) -> builtins.str:
        '''The namecheap API key.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/namecheap/namecheap/2.1.0/docs#api_key NamecheapProvider#api_key}
        '''
        result = self._values.get("api_key")
        assert result is not None, "Required property 'api_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def api_user(self) -> builtins.str:
        '''A registered api user for namecheap.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/namecheap/namecheap/2.1.0/docs#api_user NamecheapProvider#api_user}
        '''
        result = self._values.get("api_user")
        assert result is not None, "Required property 'api_user' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_name(self) -> builtins.str:
        '''A registered user name for namecheap.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/namecheap/namecheap/2.1.0/docs#user_name NamecheapProvider#user_name}
        '''
        result = self._values.get("user_name")
        assert result is not None, "Required property 'user_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def alias(self) -> typing.Optional[builtins.str]:
        '''Alias name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/namecheap/namecheap/2.1.0/docs#alias NamecheapProvider#alias}
        '''
        result = self._values.get("alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_ip(self) -> typing.Optional[builtins.str]:
        '''Client IP address.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/namecheap/namecheap/2.1.0/docs#client_ip NamecheapProvider#client_ip}
        '''
        result = self._values.get("client_ip")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def use_sandbox(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Use sandbox API endpoints.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/namecheap/namecheap/2.1.0/docs#use_sandbox NamecheapProvider#use_sandbox}
        '''
        result = self._values.get("use_sandbox")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NamecheapProviderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "NamecheapProvider",
    "NamecheapProviderConfig",
]

publication.publish()

def _typecheckingstub__0e8296e4cd4ed43ef2fb357d86c488288a909c4655223c3ace96996d1483bf59(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    api_key: builtins.str,
    api_user: builtins.str,
    user_name: builtins.str,
    alias: typing.Optional[builtins.str] = None,
    client_ip: typing.Optional[builtins.str] = None,
    use_sandbox: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fa3bda4281148660778fe89fd10a29e7dc67efc06cacb926c6ef7b498133bbf(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c853e2215e5e4193e0e779bd5cad7b563dad9b076879d4b15ce0f8241418bb66(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b2844e4214d768a5c6c2a3f0d1890d15b5d175a5a9718249246ef32ed1c3664(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0bda5570cd10f30f90fdd3e8431c717ebf719eaf30cc57d477ddc2af49606eef(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ad1fa9574e708be6128b8fd15481e16b84292270569b5da851a26f3d839d27b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bccefd916ae5a0e785a449f0d7c1796c5fb3a8b9343ade511cd7ceb2a3083ac5(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a1902c95ed0e4284ef571896b023f7a0ab2f66adaf2cd17c07ce0464a9daf82(
    value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bbe67cb9997df680cfc0ead837d5c20cf2b21da7a92e63a090950d3fc9bc5d9(
    *,
    api_key: builtins.str,
    api_user: builtins.str,
    user_name: builtins.str,
    alias: typing.Optional[builtins.str] = None,
    client_ip: typing.Optional[builtins.str] = None,
    use_sandbox: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass
