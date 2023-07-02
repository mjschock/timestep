"""
# `provider`

Refer to the Terraform Registory for docs: [`cloudinit`](https://registry.terraform.io/providers/hashicorp/cloudinit/2.3.2/docs).
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


class CloudinitProvider(
    _cdktf_9a9027ec.TerraformProvider,
    metaclass=jsii.JSIIMeta,
    jsii_type="cloudinit.provider.CloudinitProvider",
):
    """Represents a {@link https://registry.terraform.io/providers/hashicorp/cloudinit/2.3.2/docs cloudinit}."""

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        alias: typing.Optional[builtins.str] = None,
    ) -> None:
        """Create a new {@link https://registry.terraform.io/providers/hashicorp/cloudinit/2.3.2/docs cloudinit} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param alias: Alias name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/cloudinit/2.3.2/docs#alias CloudinitProvider#alias}
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__c723c9c3e0d3cb240dc6e30a21b6520fe06a08e37d57f85f8c52bf5eafc996a0
            )
            check_type(
                argname="argument scope", value=scope, expected_type=type_hints["scope"]
            )
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = CloudinitProviderConfig(alias=alias)

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
                _typecheckingstub__6f6c4ea01fd0b22884e0b3eea5b408310344c950bfb04b217137e9b93657cdf4
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "alias", value)


@jsii.data_type(
    jsii_type="cloudinit.provider.CloudinitProviderConfig",
    jsii_struct_bases=[],
    name_mapping={"alias": "alias"},
)
class CloudinitProviderConfig:
    def __init__(self, *, alias: typing.Optional[builtins.str] = None) -> None:
        """
        :param alias: Alias name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/cloudinit/2.3.2/docs#alias CloudinitProvider#alias}
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__5d70decf233f70c9341d274a19c531b3ace4b547787ac7f41ac2036839eafd6c
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/cloudinit/2.3.2/docs#alias CloudinitProvider#alias}
        """
        result = self._values.get("alias")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudinitProviderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CloudinitProvider",
    "CloudinitProviderConfig",
]

publication.publish()


def _typecheckingstub__c723c9c3e0d3cb240dc6e30a21b6520fe06a08e37d57f85f8c52bf5eafc996a0(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    alias: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__6f6c4ea01fd0b22884e0b3eea5b408310344c950bfb04b217137e9b93657cdf4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__5d70decf233f70c9341d274a19c531b3ace4b547787ac7f41ac2036839eafd6c(
    *,
    alias: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
