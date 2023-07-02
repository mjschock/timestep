"""
# `provider`

Refer to the Terraform Registory for docs: [`multipass`](https://registry.terraform.io/providers/larstobi/multipass/1.4.1/docs).
"""
import abc
import builtins
import datetime
import enum
import typing

import cdktf as _cdktf_9a9027ec
import constructs as _constructs_77d1e7e8
import jsii
import publication
import typing_extensions
from typeguard import check_type

from .._jsii import *


class MultipassProvider(
    _cdktf_9a9027ec.TerraformProvider,
    metaclass=jsii.JSIIMeta,
    jsii_type="multipass.provider.MultipassProvider",
):
    """Represents a {@link https://registry.terraform.io/providers/larstobi/multipass/1.4.1/docs multipass}."""

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        alias: typing.Optional[builtins.str] = None,
    ) -> None:
        """Create a new {@link https://registry.terraform.io/providers/larstobi/multipass/1.4.1/docs multipass} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param alias: Alias name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/larstobi/multipass/1.4.1/docs#alias MultipassProvider#alias}
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__e1f94d75d367044a5687d31d87490ca6ef27d410e65a2b3c574ca66776de6d89
            )
            check_type(
                argname="argument scope", value=scope, expected_type=type_hints["scope"]
            )
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = MultipassProviderConfig(alias=alias)

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetAlias")
    def reset_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlias", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(
            typing.Mapping[builtins.str, typing.Any],
            jsii.invoke(self, "synthesizeAttributes", []),
        )

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="aliasInput")
    def alias_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aliasInput"))

    @builtins.property
    @jsii.member(jsii_name="alias")
    def alias(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alias"))

    @alias.setter
    def alias(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__9348b67499328ff8d5bee728a38204dd08461142604142d7ff8ab4612955b8dd
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "alias", value)


@jsii.data_type(
    jsii_type="multipass.provider.MultipassProviderConfig",
    jsii_struct_bases=[],
    name_mapping={"alias": "alias"},
)
class MultipassProviderConfig:
    def __init__(self, *, alias: typing.Optional[builtins.str] = None) -> None:
        """
        :param alias: Alias name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/larstobi/multipass/1.4.1/docs#alias MultipassProvider#alias}
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__b713be3a6889bc8e1233255dd9189fa318357c8ea2a6abd150b6bd3f65c93ccc
            )
            check_type(
                argname="argument alias", value=alias, expected_type=type_hints["alias"]
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if alias is not None:
            self._values["alias"] = alias

    @builtins.property
    def alias(self) -> typing.Optional[builtins.str]:
        """Alias name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/larstobi/multipass/1.4.1/docs#alias MultipassProvider#alias}
        """
        result = self._values.get("alias")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MultipassProviderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "MultipassProvider",
    "MultipassProviderConfig",
]

publication.publish()


def _typecheckingstub__e1f94d75d367044a5687d31d87490ca6ef27d410e65a2b3c574ca66776de6d89(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    alias: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__9348b67499328ff8d5bee728a38204dd08461142604142d7ff8ab4612955b8dd(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__b713be3a6889bc8e1233255dd9189fa318357c8ea2a6abd150b6bd3f65c93ccc(
    *,
    alias: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
