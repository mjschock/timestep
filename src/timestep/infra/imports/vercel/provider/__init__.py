'''
# `provider`

Refer to the Terraform Registory for docs: [`vercel`](https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs).
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


class VercelProvider(
    _cdktf_9a9027ec.TerraformProvider,
    metaclass=jsii.JSIIMeta,
    jsii_type="vercel.provider.VercelProvider",
):
    '''Represents a {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs vercel}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        alias: typing.Optional[builtins.str] = None,
        api_token: typing.Optional[builtins.str] = None,
        team: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs vercel} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param alias: Alias name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs#alias VercelProvider#alias}
        :param api_token: The Vercel API Token to use. This can also be specified with the ``VERCEL_API_TOKEN`` shell environment variable. Tokens can be created from your `Vercel settings <https://vercel.com/account/tokens>`_. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs#api_token VercelProvider#api_token}
        :param team: The default Vercel Team to use when creating resources or reading data sources. This can be provided as either a team slug, or team ID. The slug and ID are both available from the Team Settings page in the Vercel dashboard. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs#team VercelProvider#team}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a76442ddc8fa3d61424ee83e1256b56c1ed616d9bde572f7da225e2dcc011fc0)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = VercelProviderConfig(alias=alias, api_token=api_token, team=team)

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
        '''Generates CDKTF code for importing a VercelProvider resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the VercelProvider to import.
        :param import_from_id: The id of the existing VercelProvider that should be imported. Refer to the {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the VercelProvider to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c50a26a45c68030ef4057918e274e5900c253ce965948bcc363b9022358c956)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="resetAlias")
    def reset_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlias", []))

    @jsii.member(jsii_name="resetApiToken")
    def reset_api_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApiToken", []))

    @jsii.member(jsii_name="resetTeam")
    def reset_team(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTeam", []))

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
    @jsii.member(jsii_name="apiTokenInput")
    def api_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="teamInput")
    def team_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "teamInput"))

    @builtins.property
    @jsii.member(jsii_name="alias")
    def alias(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alias"))

    @alias.setter
    def alias(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7210ba14c4bf244f5163906ea20889b14cfb721d9007a0bd9c6ef83a3125cf68)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alias", value)

    @builtins.property
    @jsii.member(jsii_name="apiToken")
    def api_token(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiToken"))

    @api_token.setter
    def api_token(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4aa04fcf9a99a30fdd6fb0a383d2c73f8b3c6cf72dfa7ed8a7146daeb4031382)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiToken", value)

    @builtins.property
    @jsii.member(jsii_name="team")
    def team(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "team"))

    @team.setter
    def team(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7113217f0508903a934f98b0c2fb2d21f2386ff2b6372968e02904d0fec6675)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "team", value)


@jsii.data_type(
    jsii_type="vercel.provider.VercelProviderConfig",
    jsii_struct_bases=[],
    name_mapping={"alias": "alias", "api_token": "apiToken", "team": "team"},
)
class VercelProviderConfig:
    def __init__(
        self,
        *,
        alias: typing.Optional[builtins.str] = None,
        api_token: typing.Optional[builtins.str] = None,
        team: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param alias: Alias name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs#alias VercelProvider#alias}
        :param api_token: The Vercel API Token to use. This can also be specified with the ``VERCEL_API_TOKEN`` shell environment variable. Tokens can be created from your `Vercel settings <https://vercel.com/account/tokens>`_. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs#api_token VercelProvider#api_token}
        :param team: The default Vercel Team to use when creating resources or reading data sources. This can be provided as either a team slug, or team ID. The slug and ID are both available from the Team Settings page in the Vercel dashboard. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs#team VercelProvider#team}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8afbe0304d327d453acba5ff5946811e99b737e59aa30a37c2439dad1530ad0c)
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
            check_type(argname="argument api_token", value=api_token, expected_type=type_hints["api_token"])
            check_type(argname="argument team", value=team, expected_type=type_hints["team"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if alias is not None:
            self._values["alias"] = alias
        if api_token is not None:
            self._values["api_token"] = api_token
        if team is not None:
            self._values["team"] = team

    @builtins.property
    def alias(self) -> typing.Optional[builtins.str]:
        '''Alias name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs#alias VercelProvider#alias}
        '''
        result = self._values.get("alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def api_token(self) -> typing.Optional[builtins.str]:
        '''The Vercel API Token to use.

        This can also be specified with the ``VERCEL_API_TOKEN`` shell environment variable. Tokens can be created from your `Vercel settings <https://vercel.com/account/tokens>`_.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs#api_token VercelProvider#api_token}
        '''
        result = self._values.get("api_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def team(self) -> typing.Optional[builtins.str]:
        '''The default Vercel Team to use when creating resources or reading data sources.

        This can be provided as either a team slug, or team ID. The slug and ID are both available from the Team Settings page in the Vercel dashboard.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs#team VercelProvider#team}
        '''
        result = self._values.get("team")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VercelProviderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "VercelProvider",
    "VercelProviderConfig",
]

publication.publish()

def _typecheckingstub__a76442ddc8fa3d61424ee83e1256b56c1ed616d9bde572f7da225e2dcc011fc0(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    alias: typing.Optional[builtins.str] = None,
    api_token: typing.Optional[builtins.str] = None,
    team: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c50a26a45c68030ef4057918e274e5900c253ce965948bcc363b9022358c956(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7210ba14c4bf244f5163906ea20889b14cfb721d9007a0bd9c6ef83a3125cf68(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4aa04fcf9a99a30fdd6fb0a383d2c73f8b3c6cf72dfa7ed8a7146daeb4031382(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7113217f0508903a934f98b0c2fb2d21f2386ff2b6372968e02904d0fec6675(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8afbe0304d327d453acba5ff5946811e99b737e59aa30a37c2439dad1530ad0c(
    *,
    alias: typing.Optional[builtins.str] = None,
    api_token: typing.Optional[builtins.str] = None,
    team: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
