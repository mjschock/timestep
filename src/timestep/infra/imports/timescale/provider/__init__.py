'''
# `provider`

Refer to the Terraform Registory for docs: [`timescale`](https://registry.terraform.io/providers/timescale/timescale/1.11.0/docs).
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


class TimescaleProvider(
    _cdktf_9a9027ec.TerraformProvider,
    metaclass=jsii.JSIIMeta,
    jsii_type="timescale.provider.TimescaleProvider",
):
    '''Represents a {@link https://registry.terraform.io/providers/timescale/timescale/1.11.0/docs timescale}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        project_id: builtins.str,
        access_key: typing.Optional[builtins.str] = None,
        access_token: typing.Optional[builtins.str] = None,
        alias: typing.Optional[builtins.str] = None,
        secret_key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/timescale/timescale/1.11.0/docs timescale} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param project_id: Project ID. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/timescale/timescale/1.11.0/docs#project_id TimescaleProvider#project_id}
        :param access_key: Access Key. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/timescale/timescale/1.11.0/docs#access_key TimescaleProvider#access_key}
        :param access_token: Access Token. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/timescale/timescale/1.11.0/docs#access_token TimescaleProvider#access_token}
        :param alias: Alias name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/timescale/timescale/1.11.0/docs#alias TimescaleProvider#alias}
        :param secret_key: Secret Key. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/timescale/timescale/1.11.0/docs#secret_key TimescaleProvider#secret_key}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e28fd153a5734ed8ecf26b48d03d5d6bf491b8258c3378322f2d21e65dc1fe2)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = TimescaleProviderConfig(
            project_id=project_id,
            access_key=access_key,
            access_token=access_token,
            alias=alias,
            secret_key=secret_key,
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
        '''Generates CDKTF code for importing a TimescaleProvider resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the TimescaleProvider to import.
        :param import_from_id: The id of the existing TimescaleProvider that should be imported. Refer to the {@link https://registry.terraform.io/providers/timescale/timescale/1.11.0/docs#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the TimescaleProvider to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98f99988258701107e608255950018a1330138eac0a61dd84a141d37e5e4972c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="resetAccessKey")
    def reset_access_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessKey", []))

    @jsii.member(jsii_name="resetAccessToken")
    def reset_access_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessToken", []))

    @jsii.member(jsii_name="resetAlias")
    def reset_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlias", []))

    @jsii.member(jsii_name="resetSecretKey")
    def reset_secret_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretKey", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="accessKeyInput")
    def access_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="accessTokenInput")
    def access_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="aliasInput")
    def alias_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aliasInput"))

    @builtins.property
    @jsii.member(jsii_name="projectIdInput")
    def project_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectIdInput"))

    @builtins.property
    @jsii.member(jsii_name="secretKeyInput")
    def secret_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="accessKey")
    def access_key(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessKey"))

    @access_key.setter
    def access_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c03782326f369876828ef49cc3b0478c081663f330a71d4b50abdf0d69f863bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessKey", value)

    @builtins.property
    @jsii.member(jsii_name="accessToken")
    def access_token(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessToken"))

    @access_token.setter
    def access_token(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dfb5762c7cd37662439d3d50e184ece654b7b6f4b3aa0fa91f266f0f450cdb81)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessToken", value)

    @builtins.property
    @jsii.member(jsii_name="alias")
    def alias(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alias"))

    @alias.setter
    def alias(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3a64658fb5a974b0fa3abc88bfe3af6258f355d4032c35710f0aa268eaeb5e4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alias", value)

    @builtins.property
    @jsii.member(jsii_name="projectId")
    def project_id(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectId"))

    @project_id.setter
    def project_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2a575c6510b7ee7ca6fb404495795795107119ac1ad5734882565b49c8fce2b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectId", value)

    @builtins.property
    @jsii.member(jsii_name="secretKey")
    def secret_key(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretKey"))

    @secret_key.setter
    def secret_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d19f8d1735e00f0926e9c0c21f757f8d94013ce4dbf2b4b02fdf839943eb605b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretKey", value)


@jsii.data_type(
    jsii_type="timescale.provider.TimescaleProviderConfig",
    jsii_struct_bases=[],
    name_mapping={
        "project_id": "projectId",
        "access_key": "accessKey",
        "access_token": "accessToken",
        "alias": "alias",
        "secret_key": "secretKey",
    },
)
class TimescaleProviderConfig:
    def __init__(
        self,
        *,
        project_id: builtins.str,
        access_key: typing.Optional[builtins.str] = None,
        access_token: typing.Optional[builtins.str] = None,
        alias: typing.Optional[builtins.str] = None,
        secret_key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param project_id: Project ID. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/timescale/timescale/1.11.0/docs#project_id TimescaleProvider#project_id}
        :param access_key: Access Key. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/timescale/timescale/1.11.0/docs#access_key TimescaleProvider#access_key}
        :param access_token: Access Token. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/timescale/timescale/1.11.0/docs#access_token TimescaleProvider#access_token}
        :param alias: Alias name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/timescale/timescale/1.11.0/docs#alias TimescaleProvider#alias}
        :param secret_key: Secret Key. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/timescale/timescale/1.11.0/docs#secret_key TimescaleProvider#secret_key}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7bb4f079762358296ba59536173ebdf8c5463422904edf78a25fc05eeba83b7b)
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument access_key", value=access_key, expected_type=type_hints["access_key"])
            check_type(argname="argument access_token", value=access_token, expected_type=type_hints["access_token"])
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
            check_type(argname="argument secret_key", value=secret_key, expected_type=type_hints["secret_key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "project_id": project_id,
        }
        if access_key is not None:
            self._values["access_key"] = access_key
        if access_token is not None:
            self._values["access_token"] = access_token
        if alias is not None:
            self._values["alias"] = alias
        if secret_key is not None:
            self._values["secret_key"] = secret_key

    @builtins.property
    def project_id(self) -> builtins.str:
        '''Project ID.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/timescale/timescale/1.11.0/docs#project_id TimescaleProvider#project_id}
        '''
        result = self._values.get("project_id")
        assert result is not None, "Required property 'project_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_key(self) -> typing.Optional[builtins.str]:
        '''Access Key.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/timescale/timescale/1.11.0/docs#access_key TimescaleProvider#access_key}
        '''
        result = self._values.get("access_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def access_token(self) -> typing.Optional[builtins.str]:
        '''Access Token.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/timescale/timescale/1.11.0/docs#access_token TimescaleProvider#access_token}
        '''
        result = self._values.get("access_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def alias(self) -> typing.Optional[builtins.str]:
        '''Alias name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/timescale/timescale/1.11.0/docs#alias TimescaleProvider#alias}
        '''
        result = self._values.get("alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secret_key(self) -> typing.Optional[builtins.str]:
        '''Secret Key.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/timescale/timescale/1.11.0/docs#secret_key TimescaleProvider#secret_key}
        '''
        result = self._values.get("secret_key")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TimescaleProviderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "TimescaleProvider",
    "TimescaleProviderConfig",
]

publication.publish()

def _typecheckingstub__6e28fd153a5734ed8ecf26b48d03d5d6bf491b8258c3378322f2d21e65dc1fe2(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    project_id: builtins.str,
    access_key: typing.Optional[builtins.str] = None,
    access_token: typing.Optional[builtins.str] = None,
    alias: typing.Optional[builtins.str] = None,
    secret_key: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98f99988258701107e608255950018a1330138eac0a61dd84a141d37e5e4972c(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c03782326f369876828ef49cc3b0478c081663f330a71d4b50abdf0d69f863bb(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dfb5762c7cd37662439d3d50e184ece654b7b6f4b3aa0fa91f266f0f450cdb81(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3a64658fb5a974b0fa3abc88bfe3af6258f355d4032c35710f0aa268eaeb5e4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2a575c6510b7ee7ca6fb404495795795107119ac1ad5734882565b49c8fce2b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d19f8d1735e00f0926e9c0c21f757f8d94013ce4dbf2b4b02fdf839943eb605b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7bb4f079762358296ba59536173ebdf8c5463422904edf78a25fc05eeba83b7b(
    *,
    project_id: builtins.str,
    access_key: typing.Optional[builtins.str] = None,
    access_token: typing.Optional[builtins.str] = None,
    alias: typing.Optional[builtins.str] = None,
    secret_key: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
