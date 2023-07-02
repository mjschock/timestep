"""
# `digitalocean_record`

Refer to the Terraform Registory for docs: [`digitalocean_record`](https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/record).
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


class Record(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.record.Record",
):
    """Represents a {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/record digitalocean_record}."""

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        domain: builtins.str,
        name: builtins.str,
        type: builtins.str,
        value: builtins.str,
        flags: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        priority: typing.Optional[jsii.Number] = None,
        tag: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[jsii.Number] = None,
        weight: typing.Optional[jsii.Number] = None,
        connection: typing.Optional[
            typing.Union[
                typing.Union[
                    _cdktf_9a9027ec.SSHProvisionerConnection,
                    typing.Dict[builtins.str, typing.Any],
                ],
                typing.Union[
                    _cdktf_9a9027ec.WinrmProvisionerConnection,
                    typing.Dict[builtins.str, typing.Any],
                ],
            ]
        ] = None,
        count: typing.Optional[
            typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]
        ] = None,
        depends_on: typing.Optional[
            typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]
        ] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[
            typing.Union[
                _cdktf_9a9027ec.TerraformResourceLifecycle,
                typing.Dict[builtins.str, typing.Any],
            ]
        ] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[
            typing.Sequence[
                typing.Union[
                    typing.Union[
                        _cdktf_9a9027ec.FileProvisioner,
                        typing.Dict[builtins.str, typing.Any],
                    ],
                    typing.Union[
                        _cdktf_9a9027ec.LocalExecProvisioner,
                        typing.Dict[builtins.str, typing.Any],
                    ],
                    typing.Union[
                        _cdktf_9a9027ec.RemoteExecProvisioner,
                        typing.Dict[builtins.str, typing.Any],
                    ],
                ]
            ]
        ] = None,
    ) -> None:
        """Create a new {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/record digitalocean_record} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param domain: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/record#domain Record#domain}.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/record#name Record#name}.
        :param type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/record#type Record#type}.
        :param value: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/record#value Record#value}.
        :param flags: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/record#flags Record#flags}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/record#id Record#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param port: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/record#port Record#port}.
        :param priority: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/record#priority Record#priority}.
        :param tag: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/record#tag Record#tag}.
        :param ttl: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/record#ttl Record#ttl}.
        :param weight: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/record#weight Record#weight}.
        :param connection:
        :param count:
        :param depends_on:
        :param for_each:
        :param lifecycle:
        :param provider:
        :param provisioners:
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__285190bf7f700f7f47f27ae76a4b9e688a658e6445109cd20e91b53d7b8e5caf
            )
            check_type(
                argname="argument scope", value=scope, expected_type=type_hints["scope"]
            )
            check_type(
                argname="argument id_", value=id_, expected_type=type_hints["id_"]
            )
        config = RecordConfig(
            domain=domain,
            name=name,
            type=type,
            value=value,
            flags=flags,
            id=id,
            port=port,
            priority=priority,
            tag=tag,
            ttl=ttl,
            weight=weight,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetFlags")
    def reset_flags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFlags", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @jsii.member(jsii_name="resetPriority")
    def reset_priority(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPriority", []))

    @jsii.member(jsii_name="resetTag")
    def reset_tag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTag", []))

    @jsii.member(jsii_name="resetTtl")
    def reset_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTtl", []))

    @jsii.member(jsii_name="resetWeight")
    def reset_weight(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWeight", []))

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
    @jsii.member(jsii_name="fqdn")
    def fqdn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fqdn"))

    @builtins.property
    @jsii.member(jsii_name="domainInput")
    def domain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainInput"))

    @builtins.property
    @jsii.member(jsii_name="flagsInput")
    def flags_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "flagsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(
            typing.Optional[jsii.Number], jsii.get(self, "priorityInput")
        )

    @builtins.property
    @jsii.member(jsii_name="tagInput")
    def tag_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tagInput"))

    @builtins.property
    @jsii.member(jsii_name="ttlInput")
    def ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ttlInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="weightInput")
    def weight_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "weightInput"))

    @builtins.property
    @jsii.member(jsii_name="domain")
    def domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domain"))

    @domain.setter
    def domain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__516bdd5f2c8d568d77c4ceef3849647c31fa9e6a5aa6712e17cfcf5daaba929b
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "domain", value)

    @builtins.property
    @jsii.member(jsii_name="flags")
    def flags(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "flags"))

    @flags.setter
    def flags(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__3df31f4251b554fc3b941082688f1e2c98777cf8c497e366030d3272b7c15e12
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "flags", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__a979844a6a332dfb0f64ff9a4d963f9c4ff6702836fa7a559ed4583697bb03f6
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__61cfd4ecb8301dd17723d64dcab6560639744b4145346f7a5052d394a64691c6
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__e6e694d32c2da0b253b72b4486c359a82c76a97e25ff4574846439f322fcf3eb
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__9ccee3415ddc59b5941f86d1ecb3d1eb854585ae5377476ef6681349735bb636
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="tag")
    def tag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tag"))

    @tag.setter
    def tag(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__bcfa15192a7ac459993fed9f9561437a9c62d3d5c7dd6f29950f51bf63fb6744
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "tag", value)

    @builtins.property
    @jsii.member(jsii_name="ttl")
    def ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ttl"))

    @ttl.setter
    def ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__829681bb1f175fb7943008ac4897ea9da084e50e56b3de97410b9b11f76ce989
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "ttl", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__a4cb7f9985ec18c844d0754b40f22916903f71d10e0653d8fc5b0ee164399adf
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__43593861809d2b87620e6d8dd7857334bdabf8729f46db03801d925c60522e7d
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="weight")
    def weight(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "weight"))

    @weight.setter
    def weight(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__919dd5e2e3306c17b167758402887416f4c43d53a99a41d72bcc6daf36dc2b17
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "weight", value)


@jsii.data_type(
    jsii_type="digitalocean.record.RecordConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "domain": "domain",
        "name": "name",
        "type": "type",
        "value": "value",
        "flags": "flags",
        "id": "id",
        "port": "port",
        "priority": "priority",
        "tag": "tag",
        "ttl": "ttl",
        "weight": "weight",
    },
)
class RecordConfig(_cdktf_9a9027ec.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[
            typing.Union[
                typing.Union[
                    _cdktf_9a9027ec.SSHProvisionerConnection,
                    typing.Dict[builtins.str, typing.Any],
                ],
                typing.Union[
                    _cdktf_9a9027ec.WinrmProvisionerConnection,
                    typing.Dict[builtins.str, typing.Any],
                ],
            ]
        ] = None,
        count: typing.Optional[
            typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]
        ] = None,
        depends_on: typing.Optional[
            typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]
        ] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[
            typing.Union[
                _cdktf_9a9027ec.TerraformResourceLifecycle,
                typing.Dict[builtins.str, typing.Any],
            ]
        ] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[
            typing.Sequence[
                typing.Union[
                    typing.Union[
                        _cdktf_9a9027ec.FileProvisioner,
                        typing.Dict[builtins.str, typing.Any],
                    ],
                    typing.Union[
                        _cdktf_9a9027ec.LocalExecProvisioner,
                        typing.Dict[builtins.str, typing.Any],
                    ],
                    typing.Union[
                        _cdktf_9a9027ec.RemoteExecProvisioner,
                        typing.Dict[builtins.str, typing.Any],
                    ],
                ]
            ]
        ] = None,
        domain: builtins.str,
        name: builtins.str,
        type: builtins.str,
        value: builtins.str,
        flags: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        priority: typing.Optional[jsii.Number] = None,
        tag: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[jsii.Number] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        """
        :param connection:
        :param count:
        :param depends_on:
        :param for_each:
        :param lifecycle:
        :param provider:
        :param provisioners:
        :param domain: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/record#domain Record#domain}.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/record#name Record#name}.
        :param type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/record#type Record#type}.
        :param value: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/record#value Record#value}.
        :param flags: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/record#flags Record#flags}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/record#id Record#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param port: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/record#port Record#port}.
        :param priority: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/record#priority Record#priority}.
        :param tag: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/record#tag Record#tag}.
        :param ttl: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/record#ttl Record#ttl}.
        :param weight: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/record#weight Record#weight}.
        """
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__dfd5ffd62dad165885a2100dc6efc2928b6d1b9ea8b6b0c548747499992a1beb
            )
            check_type(
                argname="argument connection",
                value=connection,
                expected_type=type_hints["connection"],
            )
            check_type(
                argname="argument count", value=count, expected_type=type_hints["count"]
            )
            check_type(
                argname="argument depends_on",
                value=depends_on,
                expected_type=type_hints["depends_on"],
            )
            check_type(
                argname="argument for_each",
                value=for_each,
                expected_type=type_hints["for_each"],
            )
            check_type(
                argname="argument lifecycle",
                value=lifecycle,
                expected_type=type_hints["lifecycle"],
            )
            check_type(
                argname="argument provider",
                value=provider,
                expected_type=type_hints["provider"],
            )
            check_type(
                argname="argument provisioners",
                value=provisioners,
                expected_type=type_hints["provisioners"],
            )
            check_type(
                argname="argument domain",
                value=domain,
                expected_type=type_hints["domain"],
            )
            check_type(
                argname="argument name", value=name, expected_type=type_hints["name"]
            )
            check_type(
                argname="argument type", value=type, expected_type=type_hints["type"]
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
            check_type(
                argname="argument flags", value=flags, expected_type=type_hints["flags"]
            )
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(
                argname="argument port", value=port, expected_type=type_hints["port"]
            )
            check_type(
                argname="argument priority",
                value=priority,
                expected_type=type_hints["priority"],
            )
            check_type(
                argname="argument tag", value=tag, expected_type=type_hints["tag"]
            )
            check_type(
                argname="argument ttl", value=ttl, expected_type=type_hints["ttl"]
            )
            check_type(
                argname="argument weight",
                value=weight,
                expected_type=type_hints["weight"],
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain": domain,
            "name": name,
            "type": type,
            "value": value,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if flags is not None:
            self._values["flags"] = flags
        if id is not None:
            self._values["id"] = id
        if port is not None:
            self._values["port"] = port
        if priority is not None:
            self._values["priority"] = priority
        if tag is not None:
            self._values["tag"] = tag
        if ttl is not None:
            self._values["ttl"] = ttl
        if weight is not None:
            self._values["weight"] = weight

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.SSHProvisionerConnection,
            _cdktf_9a9027ec.WinrmProvisionerConnection,
        ]
    ]:
        """
        :stability: experimental
        """
        result = self._values.get("connection")
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.SSHProvisionerConnection,
                    _cdktf_9a9027ec.WinrmProvisionerConnection,
                ]
            ],
            result,
        )

    @builtins.property
    def count(
        self,
    ) -> typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]]:
        """
        :stability: experimental
        """
        result = self._values.get("count")
        return typing.cast(
            typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]],
            result,
        )

    @builtins.property
    def depends_on(
        self,
    ) -> typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]]:
        """
        :stability: experimental
        """
        result = self._values.get("depends_on")
        return typing.cast(
            typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]], result
        )

    @builtins.property
    def for_each(self) -> typing.Optional[_cdktf_9a9027ec.ITerraformIterator]:
        """
        :stability: experimental
        """
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle]:
        """
        :stability: experimental
        """
        result = self._values.get("lifecycle")
        return typing.cast(
            typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle], result
        )

    @builtins.property
    def provider(self) -> typing.Optional[_cdktf_9a9027ec.TerraformProvider]:
        """
        :stability: experimental
        """
        result = self._values.get("provider")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[
        typing.List[
            typing.Union[
                _cdktf_9a9027ec.FileProvisioner,
                _cdktf_9a9027ec.LocalExecProvisioner,
                _cdktf_9a9027ec.RemoteExecProvisioner,
            ]
        ]
    ]:
        """
        :stability: experimental
        """
        result = self._values.get("provisioners")
        return typing.cast(
            typing.Optional[
                typing.List[
                    typing.Union[
                        _cdktf_9a9027ec.FileProvisioner,
                        _cdktf_9a9027ec.LocalExecProvisioner,
                        _cdktf_9a9027ec.RemoteExecProvisioner,
                    ]
                ]
            ],
            result,
        )

    @builtins.property
    def domain(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/record#domain Record#domain}."""
        result = self._values.get("domain")
        assert result is not None, "Required property 'domain' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/record#name Record#name}."""
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/record#type Record#type}."""
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/record#value Record#value}."""
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def flags(self) -> typing.Optional[jsii.Number]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/record#flags Record#flags}."""
        result = self._values.get("flags")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/record#id Record#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        """
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/record#port Record#port}."""
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/record#priority Record#priority}."""
        result = self._values.get("priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tag(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/record#tag Record#tag}."""
        result = self._values.get("tag")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ttl(self) -> typing.Optional[jsii.Number]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/record#ttl Record#ttl}."""
        result = self._values.get("ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def weight(self) -> typing.Optional[jsii.Number]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/record#weight Record#weight}."""
        result = self._values.get("weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RecordConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Record",
    "RecordConfig",
]

publication.publish()


def _typecheckingstub__285190bf7f700f7f47f27ae76a4b9e688a658e6445109cd20e91b53d7b8e5caf(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    domain: builtins.str,
    name: builtins.str,
    type: builtins.str,
    value: builtins.str,
    flags: typing.Optional[jsii.Number] = None,
    id: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
    priority: typing.Optional[jsii.Number] = None,
    tag: typing.Optional[builtins.str] = None,
    ttl: typing.Optional[jsii.Number] = None,
    weight: typing.Optional[jsii.Number] = None,
    connection: typing.Optional[
        typing.Union[
            typing.Union[
                _cdktf_9a9027ec.SSHProvisionerConnection,
                typing.Dict[builtins.str, typing.Any],
            ],
            typing.Union[
                _cdktf_9a9027ec.WinrmProvisionerConnection,
                typing.Dict[builtins.str, typing.Any],
            ],
        ]
    ] = None,
    count: typing.Optional[
        typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]
    ] = None,
    depends_on: typing.Optional[
        typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]
    ] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.TerraformResourceLifecycle,
            typing.Dict[builtins.str, typing.Any],
        ]
    ] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[
        typing.Sequence[
            typing.Union[
                typing.Union[
                    _cdktf_9a9027ec.FileProvisioner,
                    typing.Dict[builtins.str, typing.Any],
                ],
                typing.Union[
                    _cdktf_9a9027ec.LocalExecProvisioner,
                    typing.Dict[builtins.str, typing.Any],
                ],
                typing.Union[
                    _cdktf_9a9027ec.RemoteExecProvisioner,
                    typing.Dict[builtins.str, typing.Any],
                ],
            ]
        ]
    ] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__516bdd5f2c8d568d77c4ceef3849647c31fa9e6a5aa6712e17cfcf5daaba929b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__3df31f4251b554fc3b941082688f1e2c98777cf8c497e366030d3272b7c15e12(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a979844a6a332dfb0f64ff9a4d963f9c4ff6702836fa7a559ed4583697bb03f6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__61cfd4ecb8301dd17723d64dcab6560639744b4145346f7a5052d394a64691c6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__e6e694d32c2da0b253b72b4486c359a82c76a97e25ff4574846439f322fcf3eb(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__9ccee3415ddc59b5941f86d1ecb3d1eb854585ae5377476ef6681349735bb636(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__bcfa15192a7ac459993fed9f9561437a9c62d3d5c7dd6f29950f51bf63fb6744(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__829681bb1f175fb7943008ac4897ea9da084e50e56b3de97410b9b11f76ce989(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a4cb7f9985ec18c844d0754b40f22916903f71d10e0653d8fc5b0ee164399adf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__43593861809d2b87620e6d8dd7857334bdabf8729f46db03801d925c60522e7d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__919dd5e2e3306c17b167758402887416f4c43d53a99a41d72bcc6daf36dc2b17(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__dfd5ffd62dad165885a2100dc6efc2928b6d1b9ea8b6b0c548747499992a1beb(
    *,
    connection: typing.Optional[
        typing.Union[
            typing.Union[
                _cdktf_9a9027ec.SSHProvisionerConnection,
                typing.Dict[builtins.str, typing.Any],
            ],
            typing.Union[
                _cdktf_9a9027ec.WinrmProvisionerConnection,
                typing.Dict[builtins.str, typing.Any],
            ],
        ]
    ] = None,
    count: typing.Optional[
        typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]
    ] = None,
    depends_on: typing.Optional[
        typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]
    ] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.TerraformResourceLifecycle,
            typing.Dict[builtins.str, typing.Any],
        ]
    ] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[
        typing.Sequence[
            typing.Union[
                typing.Union[
                    _cdktf_9a9027ec.FileProvisioner,
                    typing.Dict[builtins.str, typing.Any],
                ],
                typing.Union[
                    _cdktf_9a9027ec.LocalExecProvisioner,
                    typing.Dict[builtins.str, typing.Any],
                ],
                typing.Union[
                    _cdktf_9a9027ec.RemoteExecProvisioner,
                    typing.Dict[builtins.str, typing.Any],
                ],
            ]
        ]
    ] = None,
    domain: builtins.str,
    name: builtins.str,
    type: builtins.str,
    value: builtins.str,
    flags: typing.Optional[jsii.Number] = None,
    id: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
    priority: typing.Optional[jsii.Number] = None,
    tag: typing.Optional[builtins.str] = None,
    ttl: typing.Optional[jsii.Number] = None,
    weight: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass
