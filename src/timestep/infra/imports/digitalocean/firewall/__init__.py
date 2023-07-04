"""
# `digitalocean_firewall`

Refer to the Terraform Registory for docs: [`digitalocean_firewall`](https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/firewall).
"""
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


class Firewall(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.firewall.Firewall",
):
    """Represents a {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/firewall digitalocean_firewall}."""

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        droplet_ids: typing.Optional[typing.Sequence[jsii.Number]] = None,
        id: typing.Optional[builtins.str] = None,
        inbound_rule: typing.Optional[
            typing.Union[
                _cdktf_9a9027ec.IResolvable,
                typing.Sequence[
                    typing.Union[
                        "FirewallInboundRule", typing.Dict[builtins.str, typing.Any]
                    ]
                ],
            ]
        ] = None,
        outbound_rule: typing.Optional[
            typing.Union[
                _cdktf_9a9027ec.IResolvable,
                typing.Sequence[
                    typing.Union[
                        "FirewallOutboundRule", typing.Dict[builtins.str, typing.Any]
                    ]
                ],
            ]
        ] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
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
        """Create a new {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/firewall digitalocean_firewall} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/firewall#name Firewall#name}.
        :param droplet_ids: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/firewall#droplet_ids Firewall#droplet_ids}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/firewall#id Firewall#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param inbound_rule: inbound_rule block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/firewall#inbound_rule Firewall#inbound_rule}
        :param outbound_rule: outbound_rule block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/firewall#outbound_rule Firewall#outbound_rule}
        :param tags: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/firewall#tags Firewall#tags}.
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
                _typecheckingstub__06c9a9a2487be772a5aa63b915a9ff83462b784ed047e3d747e97b03bcae85f1
            )
            check_type(
                argname="argument scope", value=scope, expected_type=type_hints["scope"]
            )
            check_type(
                argname="argument id_", value=id_, expected_type=type_hints["id_"]
            )
        config = FirewallConfig(
            name=name,
            droplet_ids=droplet_ids,
            id=id,
            inbound_rule=inbound_rule,
            outbound_rule=outbound_rule,
            tags=tags,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putInboundRule")
    def put_inbound_rule(
        self,
        value: typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.Sequence[
                typing.Union[
                    "FirewallInboundRule", typing.Dict[builtins.str, typing.Any]
                ]
            ],
        ],
    ) -> None:
        """
        :param value: -
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__6e3a53e9270c4b82d2db25ce300fb1b307222a3bcf0c0499cee86b480c44a2d0
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        return typing.cast(None, jsii.invoke(self, "putInboundRule", [value]))

    @jsii.member(jsii_name="putOutboundRule")
    def put_outbound_rule(
        self,
        value: typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.Sequence[
                typing.Union[
                    "FirewallOutboundRule", typing.Dict[builtins.str, typing.Any]
                ]
            ],
        ],
    ) -> None:
        """
        :param value: -
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__1d47ed32533921f7c4bf1c70a9b219ba5d5695d83c07213732dc73b1d564b0ab
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        return typing.cast(None, jsii.invoke(self, "putOutboundRule", [value]))

    @jsii.member(jsii_name="resetDropletIds")
    def reset_droplet_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDropletIds", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInboundRule")
    def reset_inbound_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInboundRule", []))

    @jsii.member(jsii_name="resetOutboundRule")
    def reset_outbound_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOutboundRule", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

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
    @jsii.member(jsii_name="createdAt")
    def created_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdAt"))

    @builtins.property
    @jsii.member(jsii_name="inboundRule")
    def inbound_rule(self) -> "FirewallInboundRuleList":
        return typing.cast("FirewallInboundRuleList", jsii.get(self, "inboundRule"))

    @builtins.property
    @jsii.member(jsii_name="outboundRule")
    def outbound_rule(self) -> "FirewallOutboundRuleList":
        return typing.cast("FirewallOutboundRuleList", jsii.get(self, "outboundRule"))

    @builtins.property
    @jsii.member(jsii_name="pendingChanges")
    def pending_changes(self) -> "FirewallPendingChangesList":
        return typing.cast(
            "FirewallPendingChangesList", jsii.get(self, "pendingChanges")
        )

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="dropletIdsInput")
    def droplet_ids_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(
            typing.Optional[typing.List[jsii.Number]], jsii.get(self, "dropletIdsInput")
        )

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="inboundRuleInput")
    def inbound_rule_input(
        self,
    ) -> typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["FirewallInboundRule"]]
    ]:
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.IResolvable, typing.List["FirewallInboundRule"]
                ]
            ],
            jsii.get(self, "inboundRuleInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="outboundRuleInput")
    def outbound_rule_input(
        self,
    ) -> typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["FirewallOutboundRule"]]
    ]:
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.IResolvable, typing.List["FirewallOutboundRule"]
                ]
            ],
            jsii.get(self, "outboundRuleInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(
            typing.Optional[typing.List[builtins.str]], jsii.get(self, "tagsInput")
        )

    @builtins.property
    @jsii.member(jsii_name="dropletIds")
    def droplet_ids(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "dropletIds"))

    @droplet_ids.setter
    def droplet_ids(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__4e4d0003e6bda5eaa18654db34da87ff9b94f5f826370c3a4c91c8220fd08dd7
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "dropletIds", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__14324cb6637c1e9de260ecbede03ec1658cafceb3bad396f8e4b7a8e1cdf5378
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
                _typecheckingstub__776e0e1af9ed875a4ece21cf7fee71892cb96587762ec033d8ad24cb732e598e
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__26132bef5a37f8285a77fe67d903d6ba2fcfd581c41a3b581cdb5945c0f72948
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="digitalocean.firewall.FirewallConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "name": "name",
        "droplet_ids": "dropletIds",
        "id": "id",
        "inbound_rule": "inboundRule",
        "outbound_rule": "outboundRule",
        "tags": "tags",
    },
)
class FirewallConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        name: builtins.str,
        droplet_ids: typing.Optional[typing.Sequence[jsii.Number]] = None,
        id: typing.Optional[builtins.str] = None,
        inbound_rule: typing.Optional[
            typing.Union[
                _cdktf_9a9027ec.IResolvable,
                typing.Sequence[
                    typing.Union[
                        "FirewallInboundRule", typing.Dict[builtins.str, typing.Any]
                    ]
                ],
            ]
        ] = None,
        outbound_rule: typing.Optional[
            typing.Union[
                _cdktf_9a9027ec.IResolvable,
                typing.Sequence[
                    typing.Union[
                        "FirewallOutboundRule", typing.Dict[builtins.str, typing.Any]
                    ]
                ],
            ]
        ] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        """
        :param connection:
        :param count:
        :param depends_on:
        :param for_each:
        :param lifecycle:
        :param provider:
        :param provisioners:
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/firewall#name Firewall#name}.
        :param droplet_ids: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/firewall#droplet_ids Firewall#droplet_ids}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/firewall#id Firewall#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param inbound_rule: inbound_rule block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/firewall#inbound_rule Firewall#inbound_rule}
        :param outbound_rule: outbound_rule block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/firewall#outbound_rule Firewall#outbound_rule}
        :param tags: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/firewall#tags Firewall#tags}.
        """
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__921ee68b8d0c2c0acbcf20ce4f61bfa36e5b0a6bbaee1d1587b6ce77534b8596
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
                argname="argument name", value=name, expected_type=type_hints["name"]
            )
            check_type(
                argname="argument droplet_ids",
                value=droplet_ids,
                expected_type=type_hints["droplet_ids"],
            )
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(
                argname="argument inbound_rule",
                value=inbound_rule,
                expected_type=type_hints["inbound_rule"],
            )
            check_type(
                argname="argument outbound_rule",
                value=outbound_rule,
                expected_type=type_hints["outbound_rule"],
            )
            check_type(
                argname="argument tags", value=tags, expected_type=type_hints["tags"]
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
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
        if droplet_ids is not None:
            self._values["droplet_ids"] = droplet_ids
        if id is not None:
            self._values["id"] = id
        if inbound_rule is not None:
            self._values["inbound_rule"] = inbound_rule
        if outbound_rule is not None:
            self._values["outbound_rule"] = outbound_rule
        if tags is not None:
            self._values["tags"] = tags

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
    def name(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/firewall#name Firewall#name}."""
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def droplet_ids(self) -> typing.Optional[typing.List[jsii.Number]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/firewall#droplet_ids Firewall#droplet_ids}."""
        result = self._values.get("droplet_ids")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/firewall#id Firewall#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        """
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def inbound_rule(
        self,
    ) -> typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["FirewallInboundRule"]]
    ]:
        """inbound_rule block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/firewall#inbound_rule Firewall#inbound_rule}
        """
        result = self._values.get("inbound_rule")
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.IResolvable, typing.List["FirewallInboundRule"]
                ]
            ],
            result,
        )

    @builtins.property
    def outbound_rule(
        self,
    ) -> typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["FirewallOutboundRule"]]
    ]:
        """outbound_rule block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/firewall#outbound_rule Firewall#outbound_rule}
        """
        result = self._values.get("outbound_rule")
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.IResolvable, typing.List["FirewallOutboundRule"]
                ]
            ],
            result,
        )

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/firewall#tags Firewall#tags}."""
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FirewallConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="digitalocean.firewall.FirewallInboundRule",
    jsii_struct_bases=[],
    name_mapping={
        "protocol": "protocol",
        "port_range": "portRange",
        "source_addresses": "sourceAddresses",
        "source_droplet_ids": "sourceDropletIds",
        "source_kubernetes_ids": "sourceKubernetesIds",
        "source_load_balancer_uids": "sourceLoadBalancerUids",
        "source_tags": "sourceTags",
    },
)
class FirewallInboundRule:
    def __init__(
        self,
        *,
        protocol: builtins.str,
        port_range: typing.Optional[builtins.str] = None,
        source_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
        source_droplet_ids: typing.Optional[typing.Sequence[jsii.Number]] = None,
        source_kubernetes_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        source_load_balancer_uids: typing.Optional[
            typing.Sequence[builtins.str]
        ] = None,
        source_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        """
        :param protocol: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/firewall#protocol Firewall#protocol}.
        :param port_range: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/firewall#port_range Firewall#port_range}.
        :param source_addresses: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/firewall#source_addresses Firewall#source_addresses}.
        :param source_droplet_ids: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/firewall#source_droplet_ids Firewall#source_droplet_ids}.
        :param source_kubernetes_ids: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/firewall#source_kubernetes_ids Firewall#source_kubernetes_ids}.
        :param source_load_balancer_uids: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/firewall#source_load_balancer_uids Firewall#source_load_balancer_uids}.
        :param source_tags: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/firewall#source_tags Firewall#source_tags}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__c850b93898f14fc39ef334349101452206b1b0abdf77f8a0aef9c33386f095b0
            )
            check_type(
                argname="argument protocol",
                value=protocol,
                expected_type=type_hints["protocol"],
            )
            check_type(
                argname="argument port_range",
                value=port_range,
                expected_type=type_hints["port_range"],
            )
            check_type(
                argname="argument source_addresses",
                value=source_addresses,
                expected_type=type_hints["source_addresses"],
            )
            check_type(
                argname="argument source_droplet_ids",
                value=source_droplet_ids,
                expected_type=type_hints["source_droplet_ids"],
            )
            check_type(
                argname="argument source_kubernetes_ids",
                value=source_kubernetes_ids,
                expected_type=type_hints["source_kubernetes_ids"],
            )
            check_type(
                argname="argument source_load_balancer_uids",
                value=source_load_balancer_uids,
                expected_type=type_hints["source_load_balancer_uids"],
            )
            check_type(
                argname="argument source_tags",
                value=source_tags,
                expected_type=type_hints["source_tags"],
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "protocol": protocol,
        }
        if port_range is not None:
            self._values["port_range"] = port_range
        if source_addresses is not None:
            self._values["source_addresses"] = source_addresses
        if source_droplet_ids is not None:
            self._values["source_droplet_ids"] = source_droplet_ids
        if source_kubernetes_ids is not None:
            self._values["source_kubernetes_ids"] = source_kubernetes_ids
        if source_load_balancer_uids is not None:
            self._values["source_load_balancer_uids"] = source_load_balancer_uids
        if source_tags is not None:
            self._values["source_tags"] = source_tags

    @builtins.property
    def protocol(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/firewall#protocol Firewall#protocol}."""
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port_range(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/firewall#port_range Firewall#port_range}."""
        result = self._values.get("port_range")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_addresses(self) -> typing.Optional[typing.List[builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/firewall#source_addresses Firewall#source_addresses}."""
        result = self._values.get("source_addresses")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def source_droplet_ids(self) -> typing.Optional[typing.List[jsii.Number]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/firewall#source_droplet_ids Firewall#source_droplet_ids}."""
        result = self._values.get("source_droplet_ids")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    @builtins.property
    def source_kubernetes_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/firewall#source_kubernetes_ids Firewall#source_kubernetes_ids}."""
        result = self._values.get("source_kubernetes_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def source_load_balancer_uids(self) -> typing.Optional[typing.List[builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/firewall#source_load_balancer_uids Firewall#source_load_balancer_uids}."""
        result = self._values.get("source_load_balancer_uids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def source_tags(self) -> typing.Optional[typing.List[builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/firewall#source_tags Firewall#source_tags}."""
        result = self._values.get("source_tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FirewallInboundRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FirewallInboundRuleList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.firewall.FirewallInboundRuleList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        """
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__153bca6d76ba9c15ab7cfbbc4e73f5179c7c049b9a6ca6c7b216c822a2d0ef30
            )
            check_type(
                argname="argument terraform_resource",
                value=terraform_resource,
                expected_type=type_hints["terraform_resource"],
            )
            check_type(
                argname="argument terraform_attribute",
                value=terraform_attribute,
                expected_type=type_hints["terraform_attribute"],
            )
            check_type(
                argname="argument wraps_set",
                value=wraps_set,
                expected_type=type_hints["wraps_set"],
            )
        jsii.create(
            self.__class__, self, [terraform_resource, terraform_attribute, wraps_set]
        )

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "FirewallInboundRuleOutputReference":
        """
        :param index: the index of the item to return.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__06a555c5a191f8c3a009b8aedfe8d15cfbbc4339e20d0bc63951d281d8af26d4
            )
            check_type(
                argname="argument index", value=index, expected_type=type_hints["index"]
            )
        return typing.cast(
            "FirewallInboundRuleOutputReference", jsii.invoke(self, "get", [index])
        )

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        """The attribute on the parent resource this class is referencing."""
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__bbecf497993653d3ccb78ef7d12ca188485301c32952d7fd8fd49ff689e3e6e6
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        """The parent resource."""
        return typing.cast(
            _cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource")
        )

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__a0f622e757be216edfeaffe212ce5f56cfe69d7e48ef38ba2e61681afae59ae2
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        """whether the list is wrapping a set (will add tolist() to be able to access an item via an index)."""
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__4709ff596d3e42906782f9913881834052a4a2f255c1370bdacf002b90423f41
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[FirewallInboundRule]]
    ]:
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.IResolvable, typing.List[FirewallInboundRule]
                ]
            ],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[
            typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[FirewallInboundRule]]
        ],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__88e7e768d4044c759007ce558c4faf4ef0edd0b0e0493d5177e417327bfa9b6a
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


class FirewallInboundRuleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.firewall.FirewallInboundRuleOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        """
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__cd58997e150dc5a84f49bc34ac7887633e9ba3c6e024c20055de73d37604f8f6
            )
            check_type(
                argname="argument terraform_resource",
                value=terraform_resource,
                expected_type=type_hints["terraform_resource"],
            )
            check_type(
                argname="argument terraform_attribute",
                value=terraform_attribute,
                expected_type=type_hints["terraform_attribute"],
            )
            check_type(
                argname="argument complex_object_index",
                value=complex_object_index,
                expected_type=type_hints["complex_object_index"],
            )
            check_type(
                argname="argument complex_object_is_from_set",
                value=complex_object_is_from_set,
                expected_type=type_hints["complex_object_is_from_set"],
            )
        jsii.create(
            self.__class__,
            self,
            [
                terraform_resource,
                terraform_attribute,
                complex_object_index,
                complex_object_is_from_set,
            ],
        )

    @jsii.member(jsii_name="resetPortRange")
    def reset_port_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPortRange", []))

    @jsii.member(jsii_name="resetSourceAddresses")
    def reset_source_addresses(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceAddresses", []))

    @jsii.member(jsii_name="resetSourceDropletIds")
    def reset_source_droplet_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceDropletIds", []))

    @jsii.member(jsii_name="resetSourceKubernetesIds")
    def reset_source_kubernetes_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceKubernetesIds", []))

    @jsii.member(jsii_name="resetSourceLoadBalancerUids")
    def reset_source_load_balancer_uids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceLoadBalancerUids", []))

    @jsii.member(jsii_name="resetSourceTags")
    def reset_source_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceTags", []))

    @builtins.property
    @jsii.member(jsii_name="portRangeInput")
    def port_range_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "portRangeInput")
        )

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "protocolInput")
        )

    @builtins.property
    @jsii.member(jsii_name="sourceAddressesInput")
    def source_addresses_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(
            typing.Optional[typing.List[builtins.str]],
            jsii.get(self, "sourceAddressesInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="sourceDropletIdsInput")
    def source_droplet_ids_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(
            typing.Optional[typing.List[jsii.Number]],
            jsii.get(self, "sourceDropletIdsInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="sourceKubernetesIdsInput")
    def source_kubernetes_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(
            typing.Optional[typing.List[builtins.str]],
            jsii.get(self, "sourceKubernetesIdsInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="sourceLoadBalancerUidsInput")
    def source_load_balancer_uids_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(
            typing.Optional[typing.List[builtins.str]],
            jsii.get(self, "sourceLoadBalancerUidsInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="sourceTagsInput")
    def source_tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(
            typing.Optional[typing.List[builtins.str]],
            jsii.get(self, "sourceTagsInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="portRange")
    def port_range(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "portRange"))

    @port_range.setter
    def port_range(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__1b5530d3302e9f90c68cdd819565c978f3b3233500a1b82048db06cc208f697e
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "portRange", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__942510ca97cb43c45cd429a5a3bfcaef3cc837e43b1df6cc79bc9d64cdb8e6bf
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="sourceAddresses")
    def source_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sourceAddresses"))

    @source_addresses.setter
    def source_addresses(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__f32667a61fbb3e664e8780ecdeb2290d3f2abb6eaa7e50c345d94c9afd29b80e
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "sourceAddresses", value)

    @builtins.property
    @jsii.member(jsii_name="sourceDropletIds")
    def source_droplet_ids(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "sourceDropletIds"))

    @source_droplet_ids.setter
    def source_droplet_ids(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__666e7c210d2b6b444c12a3807e663e8379b74240d609ef9b84dcf34c2dbe7c50
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "sourceDropletIds", value)

    @builtins.property
    @jsii.member(jsii_name="sourceKubernetesIds")
    def source_kubernetes_ids(self) -> typing.List[builtins.str]:
        return typing.cast(
            typing.List[builtins.str], jsii.get(self, "sourceKubernetesIds")
        )

    @source_kubernetes_ids.setter
    def source_kubernetes_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__dcd4af2032cf273d002679ab41cf23aa6e462a6c58dc3ce73cbf50325c5ceff4
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "sourceKubernetesIds", value)

    @builtins.property
    @jsii.member(jsii_name="sourceLoadBalancerUids")
    def source_load_balancer_uids(self) -> typing.List[builtins.str]:
        return typing.cast(
            typing.List[builtins.str], jsii.get(self, "sourceLoadBalancerUids")
        )

    @source_load_balancer_uids.setter
    def source_load_balancer_uids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__08d8fd7aa0718bfe3b6dc5ab189d249f9fa413594f05e5bedaadd239c656437f
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "sourceLoadBalancerUids", value)

    @builtins.property
    @jsii.member(jsii_name="sourceTags")
    def source_tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sourceTags"))

    @source_tags.setter
    def source_tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__015c41bf9483afce4c2639c4a4ef21a1148bb8b6e16c053083da71482fc3755f
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "sourceTags", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, FirewallInboundRule]
    ]:
        return typing.cast(
            typing.Optional[
                typing.Union[_cdktf_9a9027ec.IResolvable, FirewallInboundRule]
            ],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[
            typing.Union[_cdktf_9a9027ec.IResolvable, FirewallInboundRule]
        ],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__4eb4e5bf9e59da7da4f7414bd2824bfc396df1adf2c45f781e17115a865d7ecc
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="digitalocean.firewall.FirewallOutboundRule",
    jsii_struct_bases=[],
    name_mapping={
        "protocol": "protocol",
        "destination_addresses": "destinationAddresses",
        "destination_droplet_ids": "destinationDropletIds",
        "destination_kubernetes_ids": "destinationKubernetesIds",
        "destination_load_balancer_uids": "destinationLoadBalancerUids",
        "destination_tags": "destinationTags",
        "port_range": "portRange",
    },
)
class FirewallOutboundRule:
    def __init__(
        self,
        *,
        protocol: builtins.str,
        destination_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
        destination_droplet_ids: typing.Optional[typing.Sequence[jsii.Number]] = None,
        destination_kubernetes_ids: typing.Optional[
            typing.Sequence[builtins.str]
        ] = None,
        destination_load_balancer_uids: typing.Optional[
            typing.Sequence[builtins.str]
        ] = None,
        destination_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        port_range: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param protocol: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/firewall#protocol Firewall#protocol}.
        :param destination_addresses: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/firewall#destination_addresses Firewall#destination_addresses}.
        :param destination_droplet_ids: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/firewall#destination_droplet_ids Firewall#destination_droplet_ids}.
        :param destination_kubernetes_ids: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/firewall#destination_kubernetes_ids Firewall#destination_kubernetes_ids}.
        :param destination_load_balancer_uids: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/firewall#destination_load_balancer_uids Firewall#destination_load_balancer_uids}.
        :param destination_tags: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/firewall#destination_tags Firewall#destination_tags}.
        :param port_range: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/firewall#port_range Firewall#port_range}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__c276892f629148e40548e0f13588d9795fe7dde4a52446b94a4b1c9d030d0d00
            )
            check_type(
                argname="argument protocol",
                value=protocol,
                expected_type=type_hints["protocol"],
            )
            check_type(
                argname="argument destination_addresses",
                value=destination_addresses,
                expected_type=type_hints["destination_addresses"],
            )
            check_type(
                argname="argument destination_droplet_ids",
                value=destination_droplet_ids,
                expected_type=type_hints["destination_droplet_ids"],
            )
            check_type(
                argname="argument destination_kubernetes_ids",
                value=destination_kubernetes_ids,
                expected_type=type_hints["destination_kubernetes_ids"],
            )
            check_type(
                argname="argument destination_load_balancer_uids",
                value=destination_load_balancer_uids,
                expected_type=type_hints["destination_load_balancer_uids"],
            )
            check_type(
                argname="argument destination_tags",
                value=destination_tags,
                expected_type=type_hints["destination_tags"],
            )
            check_type(
                argname="argument port_range",
                value=port_range,
                expected_type=type_hints["port_range"],
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "protocol": protocol,
        }
        if destination_addresses is not None:
            self._values["destination_addresses"] = destination_addresses
        if destination_droplet_ids is not None:
            self._values["destination_droplet_ids"] = destination_droplet_ids
        if destination_kubernetes_ids is not None:
            self._values["destination_kubernetes_ids"] = destination_kubernetes_ids
        if destination_load_balancer_uids is not None:
            self._values[
                "destination_load_balancer_uids"
            ] = destination_load_balancer_uids
        if destination_tags is not None:
            self._values["destination_tags"] = destination_tags
        if port_range is not None:
            self._values["port_range"] = port_range

    @builtins.property
    def protocol(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/firewall#protocol Firewall#protocol}."""
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def destination_addresses(self) -> typing.Optional[typing.List[builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/firewall#destination_addresses Firewall#destination_addresses}."""
        result = self._values.get("destination_addresses")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def destination_droplet_ids(self) -> typing.Optional[typing.List[jsii.Number]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/firewall#destination_droplet_ids Firewall#destination_droplet_ids}."""
        result = self._values.get("destination_droplet_ids")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    @builtins.property
    def destination_kubernetes_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/firewall#destination_kubernetes_ids Firewall#destination_kubernetes_ids}."""
        result = self._values.get("destination_kubernetes_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def destination_load_balancer_uids(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/firewall#destination_load_balancer_uids Firewall#destination_load_balancer_uids}."""
        result = self._values.get("destination_load_balancer_uids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def destination_tags(self) -> typing.Optional[typing.List[builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/firewall#destination_tags Firewall#destination_tags}."""
        result = self._values.get("destination_tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def port_range(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/firewall#port_range Firewall#port_range}."""
        result = self._values.get("port_range")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FirewallOutboundRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FirewallOutboundRuleList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.firewall.FirewallOutboundRuleList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        """
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__6c18fe9d03d93864450e960bdfa408993908cdafe009e8c1e9f05e9e3adcf313
            )
            check_type(
                argname="argument terraform_resource",
                value=terraform_resource,
                expected_type=type_hints["terraform_resource"],
            )
            check_type(
                argname="argument terraform_attribute",
                value=terraform_attribute,
                expected_type=type_hints["terraform_attribute"],
            )
            check_type(
                argname="argument wraps_set",
                value=wraps_set,
                expected_type=type_hints["wraps_set"],
            )
        jsii.create(
            self.__class__, self, [terraform_resource, terraform_attribute, wraps_set]
        )

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "FirewallOutboundRuleOutputReference":
        """
        :param index: the index of the item to return.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__bfff1f36f1807bda9e554565e97d167de036499199ed33921027088f75bd1c46
            )
            check_type(
                argname="argument index", value=index, expected_type=type_hints["index"]
            )
        return typing.cast(
            "FirewallOutboundRuleOutputReference", jsii.invoke(self, "get", [index])
        )

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        """The attribute on the parent resource this class is referencing."""
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__f1c5b5608e63e14b7d84fa78e54db7da1321b0468e03df2d5d9d4a9237c59488
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        """The parent resource."""
        return typing.cast(
            _cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource")
        )

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__ba1f14fe30ecb8f409e4f93699f0a7a1be5d087a5b9d3df02b47bf15027005b1
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        """whether the list is wrapping a set (will add tolist() to be able to access an item via an index)."""
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__82c4c87c9727ad0426f07a3d57a3c5ecd56d372de4c7b7d997c8a742d6d0c04d
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[FirewallOutboundRule]]
    ]:
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.IResolvable, typing.List[FirewallOutboundRule]
                ]
            ],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[
            typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[FirewallOutboundRule]]
        ],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__7a25a1f3ea16aef0fc0b84ed36af37a012687f102faad4c86773a929d8011bbb
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


class FirewallOutboundRuleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.firewall.FirewallOutboundRuleOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        """
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__73cf9f6d5071e7f638db629613f10e1e3113c7ecf1719cc4a8a0600c6db3dbc5
            )
            check_type(
                argname="argument terraform_resource",
                value=terraform_resource,
                expected_type=type_hints["terraform_resource"],
            )
            check_type(
                argname="argument terraform_attribute",
                value=terraform_attribute,
                expected_type=type_hints["terraform_attribute"],
            )
            check_type(
                argname="argument complex_object_index",
                value=complex_object_index,
                expected_type=type_hints["complex_object_index"],
            )
            check_type(
                argname="argument complex_object_is_from_set",
                value=complex_object_is_from_set,
                expected_type=type_hints["complex_object_is_from_set"],
            )
        jsii.create(
            self.__class__,
            self,
            [
                terraform_resource,
                terraform_attribute,
                complex_object_index,
                complex_object_is_from_set,
            ],
        )

    @jsii.member(jsii_name="resetDestinationAddresses")
    def reset_destination_addresses(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestinationAddresses", []))

    @jsii.member(jsii_name="resetDestinationDropletIds")
    def reset_destination_droplet_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestinationDropletIds", []))

    @jsii.member(jsii_name="resetDestinationKubernetesIds")
    def reset_destination_kubernetes_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestinationKubernetesIds", []))

    @jsii.member(jsii_name="resetDestinationLoadBalancerUids")
    def reset_destination_load_balancer_uids(self) -> None:
        return typing.cast(
            None, jsii.invoke(self, "resetDestinationLoadBalancerUids", [])
        )

    @jsii.member(jsii_name="resetDestinationTags")
    def reset_destination_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestinationTags", []))

    @jsii.member(jsii_name="resetPortRange")
    def reset_port_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPortRange", []))

    @builtins.property
    @jsii.member(jsii_name="destinationAddressesInput")
    def destination_addresses_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(
            typing.Optional[typing.List[builtins.str]],
            jsii.get(self, "destinationAddressesInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="destinationDropletIdsInput")
    def destination_droplet_ids_input(
        self,
    ) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(
            typing.Optional[typing.List[jsii.Number]],
            jsii.get(self, "destinationDropletIdsInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="destinationKubernetesIdsInput")
    def destination_kubernetes_ids_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(
            typing.Optional[typing.List[builtins.str]],
            jsii.get(self, "destinationKubernetesIdsInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="destinationLoadBalancerUidsInput")
    def destination_load_balancer_uids_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(
            typing.Optional[typing.List[builtins.str]],
            jsii.get(self, "destinationLoadBalancerUidsInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="destinationTagsInput")
    def destination_tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(
            typing.Optional[typing.List[builtins.str]],
            jsii.get(self, "destinationTagsInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="portRangeInput")
    def port_range_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "portRangeInput")
        )

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "protocolInput")
        )

    @builtins.property
    @jsii.member(jsii_name="destinationAddresses")
    def destination_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(
            typing.List[builtins.str], jsii.get(self, "destinationAddresses")
        )

    @destination_addresses.setter
    def destination_addresses(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__dd7f5e5f3b1e0d64f3747dd18594197392d4006d81b8649400a9098a1b1ee773
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "destinationAddresses", value)

    @builtins.property
    @jsii.member(jsii_name="destinationDropletIds")
    def destination_droplet_ids(self) -> typing.List[jsii.Number]:
        return typing.cast(
            typing.List[jsii.Number], jsii.get(self, "destinationDropletIds")
        )

    @destination_droplet_ids.setter
    def destination_droplet_ids(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__0bf5660dcb30615c8ed81c69fbf245f81547945f33cd16a36926b9a911c98e9f
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "destinationDropletIds", value)

    @builtins.property
    @jsii.member(jsii_name="destinationKubernetesIds")
    def destination_kubernetes_ids(self) -> typing.List[builtins.str]:
        return typing.cast(
            typing.List[builtins.str], jsii.get(self, "destinationKubernetesIds")
        )

    @destination_kubernetes_ids.setter
    def destination_kubernetes_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__9279dd55b776c243af816ab55aed67dce2ac632a595198512976c0fa90ccf3b0
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "destinationKubernetesIds", value)

    @builtins.property
    @jsii.member(jsii_name="destinationLoadBalancerUids")
    def destination_load_balancer_uids(self) -> typing.List[builtins.str]:
        return typing.cast(
            typing.List[builtins.str], jsii.get(self, "destinationLoadBalancerUids")
        )

    @destination_load_balancer_uids.setter
    def destination_load_balancer_uids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__ca1c29d1a4f9ae9ddc643763642709d20a7a88717f97dcb089ed8c55f184e65c
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "destinationLoadBalancerUids", value)

    @builtins.property
    @jsii.member(jsii_name="destinationTags")
    def destination_tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "destinationTags"))

    @destination_tags.setter
    def destination_tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__5f7cf59d3ccaa077b42da8e3152341fb4ba0c24e226fe62a8e09b5cc9ee66a8a
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "destinationTags", value)

    @builtins.property
    @jsii.member(jsii_name="portRange")
    def port_range(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "portRange"))

    @port_range.setter
    def port_range(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__6b9dbdf7eb0f74255b4feb03677fcd05d228221b4774c890e49ad738eef63501
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "portRange", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__a4c4a9726e714eda1c618ef5b77957fddef3ab19d56a0bd3a102ed161d404a9a
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, FirewallOutboundRule]
    ]:
        return typing.cast(
            typing.Optional[
                typing.Union[_cdktf_9a9027ec.IResolvable, FirewallOutboundRule]
            ],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[
            typing.Union[_cdktf_9a9027ec.IResolvable, FirewallOutboundRule]
        ],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__620d8fae1eccc9400af7d6b641783a31c98e53a4509a547c3d62b1f0070945d8
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="digitalocean.firewall.FirewallPendingChanges",
    jsii_struct_bases=[],
    name_mapping={},
)
class FirewallPendingChanges:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FirewallPendingChanges(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FirewallPendingChangesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.firewall.FirewallPendingChangesList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        """
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__bdd718498a0d53813f7f73cb31e488385308ff11cd2e9ece072357461f22d9e8
            )
            check_type(
                argname="argument terraform_resource",
                value=terraform_resource,
                expected_type=type_hints["terraform_resource"],
            )
            check_type(
                argname="argument terraform_attribute",
                value=terraform_attribute,
                expected_type=type_hints["terraform_attribute"],
            )
            check_type(
                argname="argument wraps_set",
                value=wraps_set,
                expected_type=type_hints["wraps_set"],
            )
        jsii.create(
            self.__class__, self, [terraform_resource, terraform_attribute, wraps_set]
        )

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "FirewallPendingChangesOutputReference":
        """
        :param index: the index of the item to return.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__d537f66a378d7343166fa4a3bac75c594cbc869808a930e26e65063941d53a70
            )
            check_type(
                argname="argument index", value=index, expected_type=type_hints["index"]
            )
        return typing.cast(
            "FirewallPendingChangesOutputReference", jsii.invoke(self, "get", [index])
        )

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        """The attribute on the parent resource this class is referencing."""
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__aa679ce58da46daf569951772ddcf80c519cbec39ff9d8cd6ec3e37a0912f1aa
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        """The parent resource."""
        return typing.cast(
            _cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource")
        )

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__54805386f7c1c669ebbd14be811ec730b08440363e11d499e1bdfd77e17074e1
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        """whether the list is wrapping a set (will add tolist() to be able to access an item via an index)."""
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__7f3bcd2bf5ff71ab749fe75e444443f5436733adcd43d808570d73d71340a734
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "wrapsSet", value)


class FirewallPendingChangesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.firewall.FirewallPendingChangesOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        """
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__1559c1c1c9aae80c49021df8f7208d5fb0129025318673970884babddc54ffb3
            )
            check_type(
                argname="argument terraform_resource",
                value=terraform_resource,
                expected_type=type_hints["terraform_resource"],
            )
            check_type(
                argname="argument terraform_attribute",
                value=terraform_attribute,
                expected_type=type_hints["terraform_attribute"],
            )
            check_type(
                argname="argument complex_object_index",
                value=complex_object_index,
                expected_type=type_hints["complex_object_index"],
            )
            check_type(
                argname="argument complex_object_is_from_set",
                value=complex_object_is_from_set,
                expected_type=type_hints["complex_object_is_from_set"],
            )
        jsii.create(
            self.__class__,
            self,
            [
                terraform_resource,
                terraform_attribute,
                complex_object_index,
                complex_object_is_from_set,
            ],
        )

    @builtins.property
    @jsii.member(jsii_name="dropletId")
    def droplet_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "dropletId"))

    @builtins.property
    @jsii.member(jsii_name="removing")
    def removing(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "removing"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[FirewallPendingChanges]:
        return typing.cast(
            typing.Optional[FirewallPendingChanges], jsii.get(self, "internalValue")
        )

    @internal_value.setter
    def internal_value(self, value: typing.Optional[FirewallPendingChanges]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__074626ecc50a8def3547124c0658bd6c5ef7548bf94e75503379a4b8e635190b
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


__all__ = [
    "Firewall",
    "FirewallConfig",
    "FirewallInboundRule",
    "FirewallInboundRuleList",
    "FirewallInboundRuleOutputReference",
    "FirewallOutboundRule",
    "FirewallOutboundRuleList",
    "FirewallOutboundRuleOutputReference",
    "FirewallPendingChanges",
    "FirewallPendingChangesList",
    "FirewallPendingChangesOutputReference",
]

publication.publish()


def _typecheckingstub__06c9a9a2487be772a5aa63b915a9ff83462b784ed047e3d747e97b03bcae85f1(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    droplet_ids: typing.Optional[typing.Sequence[jsii.Number]] = None,
    id: typing.Optional[builtins.str] = None,
    inbound_rule: typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.Sequence[
                typing.Union[FirewallInboundRule, typing.Dict[builtins.str, typing.Any]]
            ],
        ]
    ] = None,
    outbound_rule: typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.Sequence[
                typing.Union[
                    FirewallOutboundRule, typing.Dict[builtins.str, typing.Any]
                ]
            ],
        ]
    ] = None,
    tags: typing.Optional[typing.Sequence[builtins.str]] = None,
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


def _typecheckingstub__6e3a53e9270c4b82d2db25ce300fb1b307222a3bcf0c0499cee86b480c44a2d0(
    value: typing.Union[
        _cdktf_9a9027ec.IResolvable,
        typing.Sequence[
            typing.Union[FirewallInboundRule, typing.Dict[builtins.str, typing.Any]]
        ],
    ],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__1d47ed32533921f7c4bf1c70a9b219ba5d5695d83c07213732dc73b1d564b0ab(
    value: typing.Union[
        _cdktf_9a9027ec.IResolvable,
        typing.Sequence[
            typing.Union[FirewallOutboundRule, typing.Dict[builtins.str, typing.Any]]
        ],
    ],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__4e4d0003e6bda5eaa18654db34da87ff9b94f5f826370c3a4c91c8220fd08dd7(
    value: typing.List[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__14324cb6637c1e9de260ecbede03ec1658cafceb3bad396f8e4b7a8e1cdf5378(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__776e0e1af9ed875a4ece21cf7fee71892cb96587762ec033d8ad24cb732e598e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__26132bef5a37f8285a77fe67d903d6ba2fcfd581c41a3b581cdb5945c0f72948(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__921ee68b8d0c2c0acbcf20ce4f61bfa36e5b0a6bbaee1d1587b6ce77534b8596(
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
    name: builtins.str,
    droplet_ids: typing.Optional[typing.Sequence[jsii.Number]] = None,
    id: typing.Optional[builtins.str] = None,
    inbound_rule: typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.Sequence[
                typing.Union[FirewallInboundRule, typing.Dict[builtins.str, typing.Any]]
            ],
        ]
    ] = None,
    outbound_rule: typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.Sequence[
                typing.Union[
                    FirewallOutboundRule, typing.Dict[builtins.str, typing.Any]
                ]
            ],
        ]
    ] = None,
    tags: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__c850b93898f14fc39ef334349101452206b1b0abdf77f8a0aef9c33386f095b0(
    *,
    protocol: builtins.str,
    port_range: typing.Optional[builtins.str] = None,
    source_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
    source_droplet_ids: typing.Optional[typing.Sequence[jsii.Number]] = None,
    source_kubernetes_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    source_load_balancer_uids: typing.Optional[typing.Sequence[builtins.str]] = None,
    source_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__153bca6d76ba9c15ab7cfbbc4e73f5179c7c049b9a6ca6c7b216c822a2d0ef30(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__06a555c5a191f8c3a009b8aedfe8d15cfbbc4339e20d0bc63951d281d8af26d4(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__bbecf497993653d3ccb78ef7d12ca188485301c32952d7fd8fd49ff689e3e6e6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a0f622e757be216edfeaffe212ce5f56cfe69d7e48ef38ba2e61681afae59ae2(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__4709ff596d3e42906782f9913881834052a4a2f255c1370bdacf002b90423f41(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__88e7e768d4044c759007ce558c4faf4ef0edd0b0e0493d5177e417327bfa9b6a(
    value: typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[FirewallInboundRule]]
    ],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__cd58997e150dc5a84f49bc34ac7887633e9ba3c6e024c20055de73d37604f8f6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__1b5530d3302e9f90c68cdd819565c978f3b3233500a1b82048db06cc208f697e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__942510ca97cb43c45cd429a5a3bfcaef3cc837e43b1df6cc79bc9d64cdb8e6bf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__f32667a61fbb3e664e8780ecdeb2290d3f2abb6eaa7e50c345d94c9afd29b80e(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__666e7c210d2b6b444c12a3807e663e8379b74240d609ef9b84dcf34c2dbe7c50(
    value: typing.List[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__dcd4af2032cf273d002679ab41cf23aa6e462a6c58dc3ce73cbf50325c5ceff4(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__08d8fd7aa0718bfe3b6dc5ab189d249f9fa413594f05e5bedaadd239c656437f(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__015c41bf9483afce4c2639c4a4ef21a1148bb8b6e16c053083da71482fc3755f(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__4eb4e5bf9e59da7da4f7414bd2824bfc396df1adf2c45f781e17115a865d7ecc(
    value: typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, FirewallInboundRule]
    ],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__c276892f629148e40548e0f13588d9795fe7dde4a52446b94a4b1c9d030d0d00(
    *,
    protocol: builtins.str,
    destination_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
    destination_droplet_ids: typing.Optional[typing.Sequence[jsii.Number]] = None,
    destination_kubernetes_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    destination_load_balancer_uids: typing.Optional[
        typing.Sequence[builtins.str]
    ] = None,
    destination_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    port_range: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__6c18fe9d03d93864450e960bdfa408993908cdafe009e8c1e9f05e9e3adcf313(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__bfff1f36f1807bda9e554565e97d167de036499199ed33921027088f75bd1c46(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__f1c5b5608e63e14b7d84fa78e54db7da1321b0468e03df2d5d9d4a9237c59488(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__ba1f14fe30ecb8f409e4f93699f0a7a1be5d087a5b9d3df02b47bf15027005b1(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__82c4c87c9727ad0426f07a3d57a3c5ecd56d372de4c7b7d997c8a742d6d0c04d(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__7a25a1f3ea16aef0fc0b84ed36af37a012687f102faad4c86773a929d8011bbb(
    value: typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[FirewallOutboundRule]]
    ],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__73cf9f6d5071e7f638db629613f10e1e3113c7ecf1719cc4a8a0600c6db3dbc5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__dd7f5e5f3b1e0d64f3747dd18594197392d4006d81b8649400a9098a1b1ee773(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__0bf5660dcb30615c8ed81c69fbf245f81547945f33cd16a36926b9a911c98e9f(
    value: typing.List[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__9279dd55b776c243af816ab55aed67dce2ac632a595198512976c0fa90ccf3b0(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__ca1c29d1a4f9ae9ddc643763642709d20a7a88717f97dcb089ed8c55f184e65c(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__5f7cf59d3ccaa077b42da8e3152341fb4ba0c24e226fe62a8e09b5cc9ee66a8a(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__6b9dbdf7eb0f74255b4feb03677fcd05d228221b4774c890e49ad738eef63501(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a4c4a9726e714eda1c618ef5b77957fddef3ab19d56a0bd3a102ed161d404a9a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__620d8fae1eccc9400af7d6b641783a31c98e53a4509a547c3d62b1f0070945d8(
    value: typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, FirewallOutboundRule]
    ],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__bdd718498a0d53813f7f73cb31e488385308ff11cd2e9ece072357461f22d9e8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d537f66a378d7343166fa4a3bac75c594cbc869808a930e26e65063941d53a70(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__aa679ce58da46daf569951772ddcf80c519cbec39ff9d8cd6ec3e37a0912f1aa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__54805386f7c1c669ebbd14be811ec730b08440363e11d499e1bdfd77e17074e1(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__7f3bcd2bf5ff71ab749fe75e444443f5436733adcd43d808570d73d71340a734(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__1559c1c1c9aae80c49021df8f7208d5fb0129025318673970884babddc54ffb3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__074626ecc50a8def3547124c0658bd6c5ef7548bf94e75503379a4b8e635190b(
    value: typing.Optional[FirewallPendingChanges],
) -> None:
    """Type checking stubs"""
    pass
