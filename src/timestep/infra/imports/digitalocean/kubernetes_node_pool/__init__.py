"""
# `digitalocean_kubernetes_node_pool`

Refer to the Terraform Registory for docs: [`digitalocean_kubernetes_node_pool`](https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_node_pool).
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


class KubernetesNodePool(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.kubernetesNodePool.KubernetesNodePool",
):
    """Represents a {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_node_pool digitalocean_kubernetes_node_pool}."""

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        cluster_id: builtins.str,
        name: builtins.str,
        size: builtins.str,
        auto_scale: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        max_nodes: typing.Optional[jsii.Number] = None,
        min_nodes: typing.Optional[jsii.Number] = None,
        node_count: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        taint: typing.Optional[
            typing.Union[
                _cdktf_9a9027ec.IResolvable,
                typing.Sequence[
                    typing.Union[
                        "KubernetesNodePoolTaint", typing.Dict[builtins.str, typing.Any]
                    ]
                ],
            ]
        ] = None,
        timeouts: typing.Optional[
            typing.Union[
                "KubernetesNodePoolTimeouts", typing.Dict[builtins.str, typing.Any]
            ]
        ] = None,
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
        """Create a new {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_node_pool digitalocean_kubernetes_node_pool} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param cluster_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_node_pool#cluster_id KubernetesNodePool#cluster_id}.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_node_pool#name KubernetesNodePool#name}.
        :param size: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_node_pool#size KubernetesNodePool#size}.
        :param auto_scale: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_node_pool#auto_scale KubernetesNodePool#auto_scale}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_node_pool#id KubernetesNodePool#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_node_pool#labels KubernetesNodePool#labels}.
        :param max_nodes: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_node_pool#max_nodes KubernetesNodePool#max_nodes}.
        :param min_nodes: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_node_pool#min_nodes KubernetesNodePool#min_nodes}.
        :param node_count: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_node_pool#node_count KubernetesNodePool#node_count}.
        :param tags: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_node_pool#tags KubernetesNodePool#tags}.
        :param taint: taint block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_node_pool#taint KubernetesNodePool#taint}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_node_pool#timeouts KubernetesNodePool#timeouts}
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
                _typecheckingstub__b5c4aa0c51eae12b1f0df7d700d3335dedd76038ab785c6f17ede68aa2446998
            )
            check_type(
                argname="argument scope", value=scope, expected_type=type_hints["scope"]
            )
            check_type(
                argname="argument id_", value=id_, expected_type=type_hints["id_"]
            )
        config = KubernetesNodePoolConfig(
            cluster_id=cluster_id,
            name=name,
            size=size,
            auto_scale=auto_scale,
            id=id,
            labels=labels,
            max_nodes=max_nodes,
            min_nodes=min_nodes,
            node_count=node_count,
            tags=tags,
            taint=taint,
            timeouts=timeouts,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putTaint")
    def put_taint(
        self,
        value: typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.Sequence[
                typing.Union[
                    "KubernetesNodePoolTaint", typing.Dict[builtins.str, typing.Any]
                ]
            ],
        ],
    ) -> None:
        """
        :param value: -
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__4a08cfb062c2e124ce09d1890934d2cbb1e702956e02e0dc8ee564f0d6081c12
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        return typing.cast(None, jsii.invoke(self, "putTaint", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param create: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_node_pool#create KubernetesNodePool#create}.
        :param delete: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_node_pool#delete KubernetesNodePool#delete}.
        """
        value = KubernetesNodePoolTimeouts(create=create, delete=delete)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAutoScale")
    def reset_auto_scale(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoScale", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetMaxNodes")
    def reset_max_nodes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxNodes", []))

    @jsii.member(jsii_name="resetMinNodes")
    def reset_min_nodes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinNodes", []))

    @jsii.member(jsii_name="resetNodeCount")
    def reset_node_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodeCount", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTaint")
    def reset_taint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTaint", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

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
    @jsii.member(jsii_name="actualNodeCount")
    def actual_node_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "actualNodeCount"))

    @builtins.property
    @jsii.member(jsii_name="nodes")
    def nodes(self) -> "KubernetesNodePoolNodesList":
        return typing.cast("KubernetesNodePoolNodesList", jsii.get(self, "nodes"))

    @builtins.property
    @jsii.member(jsii_name="taint")
    def taint(self) -> "KubernetesNodePoolTaintList":
        return typing.cast("KubernetesNodePoolTaintList", jsii.get(self, "taint"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "KubernetesNodePoolTimeoutsOutputReference":
        return typing.cast(
            "KubernetesNodePoolTimeoutsOutputReference", jsii.get(self, "timeouts")
        )

    @builtins.property
    @jsii.member(jsii_name="autoScaleInput")
    def auto_scale_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "autoScaleInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="clusterIdInput")
    def cluster_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "clusterIdInput")
        )

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(
            typing.Optional[typing.Mapping[builtins.str, builtins.str]],
            jsii.get(self, "labelsInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="maxNodesInput")
    def max_nodes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(
            typing.Optional[jsii.Number], jsii.get(self, "maxNodesInput")
        )

    @builtins.property
    @jsii.member(jsii_name="minNodesInput")
    def min_nodes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(
            typing.Optional[jsii.Number], jsii.get(self, "minNodesInput")
        )

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeCountInput")
    def node_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(
            typing.Optional[jsii.Number], jsii.get(self, "nodeCountInput")
        )

    @builtins.property
    @jsii.member(jsii_name="sizeInput")
    def size_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sizeInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(
            typing.Optional[typing.List[builtins.str]], jsii.get(self, "tagsInput")
        )

    @builtins.property
    @jsii.member(jsii_name="taintInput")
    def taint_input(
        self,
    ) -> typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable, typing.List["KubernetesNodePoolTaint"]
        ]
    ]:
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.IResolvable, typing.List["KubernetesNodePoolTaint"]
                ]
            ],
            jsii.get(self, "taintInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, "KubernetesNodePoolTimeouts"]
    ]:
        return typing.cast(
            typing.Optional[
                typing.Union[_cdktf_9a9027ec.IResolvable, "KubernetesNodePoolTimeouts"]
            ],
            jsii.get(self, "timeoutsInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="autoScale")
    def auto_scale(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "autoScale"),
        )

    @auto_scale.setter
    def auto_scale(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__8ef248345de022da6678b40c9c3f413fe8e8e683a6739eb91b3b9e673f49b73c
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "autoScale", value)

    @builtins.property
    @jsii.member(jsii_name="clusterId")
    def cluster_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterId"))

    @cluster_id.setter
    def cluster_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__7625860cd2a39b0761dd97945b2f8db96295035ea1a9c45fffe6dc987325e365
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "clusterId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__ecbb9bc6281b65f7f0aaed71186508101618b0c44dfa3e06449d1fb2ed0f79c5
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(
            typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels")
        )

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__6ab2cbd70ef974d65c1c5543b20cade0ecea764a7ddc38ff0801ddc34250f0f8
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="maxNodes")
    def max_nodes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxNodes"))

    @max_nodes.setter
    def max_nodes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__984e8000f7f88c47bccd2d502451a8d537e3a66a08c56cef6829df03f80ea444
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "maxNodes", value)

    @builtins.property
    @jsii.member(jsii_name="minNodes")
    def min_nodes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minNodes"))

    @min_nodes.setter
    def min_nodes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__9f3664b824e7a3e075da042c2c40a27e8787fa86890d22ff2a7b66431f1f324a
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "minNodes", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__2a21d9fa960648c86f33f88846e6b9b14dcc5e8c92b4ff490c15add137a6c850
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="nodeCount")
    def node_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "nodeCount"))

    @node_count.setter
    def node_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__9698bda0f347a5aa5b955513be3680c6baa6f808a9404251a58e0527898983f3
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "nodeCount", value)

    @builtins.property
    @jsii.member(jsii_name="size")
    def size(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "size"))

    @size.setter
    def size(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__caaeacd0e52f756311e615dc8f93e0d5c0f0a32f18ae78593493e1d43bf508df
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "size", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__dddc46293d3bda332b4b9016e1757cc5b15dca4bd0910458d42fa984a32c1468
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="digitalocean.kubernetesNodePool.KubernetesNodePoolConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "cluster_id": "clusterId",
        "name": "name",
        "size": "size",
        "auto_scale": "autoScale",
        "id": "id",
        "labels": "labels",
        "max_nodes": "maxNodes",
        "min_nodes": "minNodes",
        "node_count": "nodeCount",
        "tags": "tags",
        "taint": "taint",
        "timeouts": "timeouts",
    },
)
class KubernetesNodePoolConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        cluster_id: builtins.str,
        name: builtins.str,
        size: builtins.str,
        auto_scale: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        max_nodes: typing.Optional[jsii.Number] = None,
        min_nodes: typing.Optional[jsii.Number] = None,
        node_count: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        taint: typing.Optional[
            typing.Union[
                _cdktf_9a9027ec.IResolvable,
                typing.Sequence[
                    typing.Union[
                        "KubernetesNodePoolTaint", typing.Dict[builtins.str, typing.Any]
                    ]
                ],
            ]
        ] = None,
        timeouts: typing.Optional[
            typing.Union[
                "KubernetesNodePoolTimeouts", typing.Dict[builtins.str, typing.Any]
            ]
        ] = None,
    ) -> None:
        """
        :param connection:
        :param count:
        :param depends_on:
        :param for_each:
        :param lifecycle:
        :param provider:
        :param provisioners:
        :param cluster_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_node_pool#cluster_id KubernetesNodePool#cluster_id}.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_node_pool#name KubernetesNodePool#name}.
        :param size: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_node_pool#size KubernetesNodePool#size}.
        :param auto_scale: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_node_pool#auto_scale KubernetesNodePool#auto_scale}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_node_pool#id KubernetesNodePool#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_node_pool#labels KubernetesNodePool#labels}.
        :param max_nodes: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_node_pool#max_nodes KubernetesNodePool#max_nodes}.
        :param min_nodes: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_node_pool#min_nodes KubernetesNodePool#min_nodes}.
        :param node_count: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_node_pool#node_count KubernetesNodePool#node_count}.
        :param tags: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_node_pool#tags KubernetesNodePool#tags}.
        :param taint: taint block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_node_pool#taint KubernetesNodePool#taint}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_node_pool#timeouts KubernetesNodePool#timeouts}
        """
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = KubernetesNodePoolTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__bdd53c4bb006d5535e30e1248bf10cd5876a0647b14470268503191afbad9e4b
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
                argname="argument cluster_id",
                value=cluster_id,
                expected_type=type_hints["cluster_id"],
            )
            check_type(
                argname="argument name", value=name, expected_type=type_hints["name"]
            )
            check_type(
                argname="argument size", value=size, expected_type=type_hints["size"]
            )
            check_type(
                argname="argument auto_scale",
                value=auto_scale,
                expected_type=type_hints["auto_scale"],
            )
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(
                argname="argument labels",
                value=labels,
                expected_type=type_hints["labels"],
            )
            check_type(
                argname="argument max_nodes",
                value=max_nodes,
                expected_type=type_hints["max_nodes"],
            )
            check_type(
                argname="argument min_nodes",
                value=min_nodes,
                expected_type=type_hints["min_nodes"],
            )
            check_type(
                argname="argument node_count",
                value=node_count,
                expected_type=type_hints["node_count"],
            )
            check_type(
                argname="argument tags", value=tags, expected_type=type_hints["tags"]
            )
            check_type(
                argname="argument taint", value=taint, expected_type=type_hints["taint"]
            )
            check_type(
                argname="argument timeouts",
                value=timeouts,
                expected_type=type_hints["timeouts"],
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster_id": cluster_id,
            "name": name,
            "size": size,
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
        if auto_scale is not None:
            self._values["auto_scale"] = auto_scale
        if id is not None:
            self._values["id"] = id
        if labels is not None:
            self._values["labels"] = labels
        if max_nodes is not None:
            self._values["max_nodes"] = max_nodes
        if min_nodes is not None:
            self._values["min_nodes"] = min_nodes
        if node_count is not None:
            self._values["node_count"] = node_count
        if tags is not None:
            self._values["tags"] = tags
        if taint is not None:
            self._values["taint"] = taint
        if timeouts is not None:
            self._values["timeouts"] = timeouts

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
    def cluster_id(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_node_pool#cluster_id KubernetesNodePool#cluster_id}."""
        result = self._values.get("cluster_id")
        assert result is not None, "Required property 'cluster_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_node_pool#name KubernetesNodePool#name}."""
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def size(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_node_pool#size KubernetesNodePool#size}."""
        result = self._values.get("size")
        assert result is not None, "Required property 'size' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auto_scale(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_node_pool#auto_scale KubernetesNodePool#auto_scale}."""
        result = self._values.get("auto_scale")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_node_pool#id KubernetesNodePool#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        """
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_node_pool#labels KubernetesNodePool#labels}."""
        result = self._values.get("labels")
        return typing.cast(
            typing.Optional[typing.Mapping[builtins.str, builtins.str]], result
        )

    @builtins.property
    def max_nodes(self) -> typing.Optional[jsii.Number]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_node_pool#max_nodes KubernetesNodePool#max_nodes}."""
        result = self._values.get("max_nodes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_nodes(self) -> typing.Optional[jsii.Number]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_node_pool#min_nodes KubernetesNodePool#min_nodes}."""
        result = self._values.get("min_nodes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def node_count(self) -> typing.Optional[jsii.Number]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_node_pool#node_count KubernetesNodePool#node_count}."""
        result = self._values.get("node_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_node_pool#tags KubernetesNodePool#tags}."""
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def taint(
        self,
    ) -> typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable, typing.List["KubernetesNodePoolTaint"]
        ]
    ]:
        """taint block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_node_pool#taint KubernetesNodePool#taint}
        """
        result = self._values.get("taint")
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.IResolvable, typing.List["KubernetesNodePoolTaint"]
                ]
            ],
            result,
        )

    @builtins.property
    def timeouts(self) -> typing.Optional["KubernetesNodePoolTimeouts"]:
        """timeouts block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_node_pool#timeouts KubernetesNodePool#timeouts}
        """
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["KubernetesNodePoolTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesNodePoolConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="digitalocean.kubernetesNodePool.KubernetesNodePoolNodes",
    jsii_struct_bases=[],
    name_mapping={},
)
class KubernetesNodePoolNodes:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesNodePoolNodes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KubernetesNodePoolNodesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.kubernetesNodePool.KubernetesNodePoolNodesList",
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
                _typecheckingstub__9b5bc966ec1e6e3d8f3fcf62bbb51b2035b4c8fec4097e81a0df3bd24023ebf2
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
    def get(self, index: jsii.Number) -> "KubernetesNodePoolNodesOutputReference":
        """
        :param index: the index of the item to return.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__04423caeb0206a79d94771f84b3a73deb60be29558a3fbb5847ea369beee8a12
            )
            check_type(
                argname="argument index", value=index, expected_type=type_hints["index"]
            )
        return typing.cast(
            "KubernetesNodePoolNodesOutputReference", jsii.invoke(self, "get", [index])
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
                _typecheckingstub__bb8379b64a8c03d5918a9d1a58dee10ac3ecbd0c2dee2c27d3295a60d15b9402
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
                _typecheckingstub__9d5920b6aa1553d56e49f9c298cb92e13ed75b96fa90e061fb1013ce1b116bd8
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
                _typecheckingstub__4aa065952e359a82153e665f79898076135e0894412c39047dd26d1dc8afc5ed
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "wrapsSet", value)


class KubernetesNodePoolNodesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.kubernetesNodePool.KubernetesNodePoolNodesOutputReference",
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
                _typecheckingstub__b3ca4989e0160f2dd1e766db6b4ba88c9418334b3a5152d37e8d5a51c773c032
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
    @jsii.member(jsii_name="createdAt")
    def created_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdAt"))

    @builtins.property
    @jsii.member(jsii_name="dropletId")
    def droplet_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dropletId"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="updatedAt")
    def updated_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "updatedAt"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[KubernetesNodePoolNodes]:
        return typing.cast(
            typing.Optional[KubernetesNodePoolNodes], jsii.get(self, "internalValue")
        )

    @internal_value.setter
    def internal_value(self, value: typing.Optional[KubernetesNodePoolNodes]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__ddc0c7e5c10dfc0728ad943d022601391bdbf599a1764503fda710d1fe247314
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="digitalocean.kubernetesNodePool.KubernetesNodePoolTaint",
    jsii_struct_bases=[],
    name_mapping={"effect": "effect", "key": "key", "value": "value"},
)
class KubernetesNodePoolTaint:
    def __init__(
        self,
        *,
        effect: builtins.str,
        key: builtins.str,
        value: builtins.str,
    ) -> None:
        """
        :param effect: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_node_pool#effect KubernetesNodePool#effect}.
        :param key: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_node_pool#key KubernetesNodePool#key}.
        :param value: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_node_pool#value KubernetesNodePool#value}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__6ca09b9351c5571f813ffb936bcf4ac6b7d9e2506966f55db5fa0caca6585b2c
            )
            check_type(
                argname="argument effect",
                value=effect,
                expected_type=type_hints["effect"],
            )
            check_type(
                argname="argument key", value=key, expected_type=type_hints["key"]
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "effect": effect,
            "key": key,
            "value": value,
        }

    @builtins.property
    def effect(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_node_pool#effect KubernetesNodePool#effect}."""
        result = self._values.get("effect")
        assert result is not None, "Required property 'effect' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_node_pool#key KubernetesNodePool#key}."""
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_node_pool#value KubernetesNodePool#value}."""
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesNodePoolTaint(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KubernetesNodePoolTaintList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.kubernetesNodePool.KubernetesNodePoolTaintList",
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
                _typecheckingstub__77a5b1a8a6be333cd34642176b324ddaba40e85fd3575058cd8b6dedce463933
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
    def get(self, index: jsii.Number) -> "KubernetesNodePoolTaintOutputReference":
        """
        :param index: the index of the item to return.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__864e6f99106ad5a1487107e4efe0190726283fefccd0b0b6508c112c305f9164
            )
            check_type(
                argname="argument index", value=index, expected_type=type_hints["index"]
            )
        return typing.cast(
            "KubernetesNodePoolTaintOutputReference", jsii.invoke(self, "get", [index])
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
                _typecheckingstub__976178d330bae383fda6eae299f5b76c911c71a50e8a7a2d263c41a92b49ff71
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
                _typecheckingstub__512de989beb664dbad338d273fb5b8ba6b35fa3fb16efb69a97a334c2b12f335
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
                _typecheckingstub__237dd3841dc613ef8a8a58f0f54c1560177e622caa3328161626fea7b148c1b3
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
        typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesNodePoolTaint]]
    ]:
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.IResolvable, typing.List[KubernetesNodePoolTaint]
                ]
            ],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[
            typing.Union[
                _cdktf_9a9027ec.IResolvable, typing.List[KubernetesNodePoolTaint]
            ]
        ],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__9a358076ebf6a6aa5a00a9b7d8596052f9ca20aa724dc8c4dc9bee8cf895448d
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


class KubernetesNodePoolTaintOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.kubernetesNodePool.KubernetesNodePoolTaintOutputReference",
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
                _typecheckingstub__45ce757c07633d22e527e5a5a7141f04b37fa551d0a5237a2e9c0b3496d691ff
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
    @jsii.member(jsii_name="effectInput")
    def effect_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "effectInput"))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="effect")
    def effect(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "effect"))

    @effect.setter
    def effect(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__80b60cf34705ad16e95a145b89eb5c0ab503e4d3d9544035c7d4c595b8f7f885
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "effect", value)

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__758881d555afde16bb0140bc1f45d381296c1d699d83920d0ef863fd6305b6aa
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__7ac489706ed39638a971811c698103e802b87f2ba209bfad9bd27aa309d6a45b
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesNodePoolTaint]
    ]:
        return typing.cast(
            typing.Optional[
                typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesNodePoolTaint]
            ],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[
            typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesNodePoolTaint]
        ],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__0d7391f282cd5641c5119eb3277570398a81dacfdfc1372a2be7895c95d2d4cc
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="digitalocean.kubernetesNodePool.KubernetesNodePoolTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete"},
)
class KubernetesNodePoolTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param create: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_node_pool#create KubernetesNodePool#create}.
        :param delete: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_node_pool#delete KubernetesNodePool#delete}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__3c2a04e00a88ddb1de0bbe940d8d797dfaa5035e825b62a45ecf3358eebc4e02
            )
            check_type(
                argname="argument create",
                value=create,
                expected_type=type_hints["create"],
            )
            check_type(
                argname="argument delete",
                value=delete,
                expected_type=type_hints["delete"],
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_node_pool#create KubernetesNodePool#create}."""
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_node_pool#delete KubernetesNodePool#delete}."""
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesNodePoolTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KubernetesNodePoolTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.kubernetesNodePool.KubernetesNodePoolTimeoutsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        """
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__7b042f2b1f790e6616b0f0e3e7273a8fb1e44a374b3b1b9943d44bdd2b55d0ed
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
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__55983d3e1918006b298cbc0789f0ad3bfad5ff3556a23c0fca74512284a04afd
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__a0743e7924f42e612ed21cbc57f69fc04f29d165e70b43500426a86f5d3c5ec0
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesNodePoolTimeouts]
    ]:
        return typing.cast(
            typing.Optional[
                typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesNodePoolTimeouts]
            ],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[
            typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesNodePoolTimeouts]
        ],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__b6fc520e2ff48abcdc652d055f11abdca6f74de5dd070550356e1ff6de82ba79
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


__all__ = [
    "KubernetesNodePool",
    "KubernetesNodePoolConfig",
    "KubernetesNodePoolNodes",
    "KubernetesNodePoolNodesList",
    "KubernetesNodePoolNodesOutputReference",
    "KubernetesNodePoolTaint",
    "KubernetesNodePoolTaintList",
    "KubernetesNodePoolTaintOutputReference",
    "KubernetesNodePoolTimeouts",
    "KubernetesNodePoolTimeoutsOutputReference",
]

publication.publish()


def _typecheckingstub__b5c4aa0c51eae12b1f0df7d700d3335dedd76038ab785c6f17ede68aa2446998(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    cluster_id: builtins.str,
    name: builtins.str,
    size: builtins.str,
    auto_scale: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    id: typing.Optional[builtins.str] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    max_nodes: typing.Optional[jsii.Number] = None,
    min_nodes: typing.Optional[jsii.Number] = None,
    node_count: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    taint: typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.Sequence[
                typing.Union[
                    KubernetesNodePoolTaint, typing.Dict[builtins.str, typing.Any]
                ]
            ],
        ]
    ] = None,
    timeouts: typing.Optional[
        typing.Union[KubernetesNodePoolTimeouts, typing.Dict[builtins.str, typing.Any]]
    ] = None,
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


def _typecheckingstub__4a08cfb062c2e124ce09d1890934d2cbb1e702956e02e0dc8ee564f0d6081c12(
    value: typing.Union[
        _cdktf_9a9027ec.IResolvable,
        typing.Sequence[
            typing.Union[KubernetesNodePoolTaint, typing.Dict[builtins.str, typing.Any]]
        ],
    ],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__8ef248345de022da6678b40c9c3f413fe8e8e683a6739eb91b3b9e673f49b73c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__7625860cd2a39b0761dd97945b2f8db96295035ea1a9c45fffe6dc987325e365(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__ecbb9bc6281b65f7f0aaed71186508101618b0c44dfa3e06449d1fb2ed0f79c5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__6ab2cbd70ef974d65c1c5543b20cade0ecea764a7ddc38ff0801ddc34250f0f8(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__984e8000f7f88c47bccd2d502451a8d537e3a66a08c56cef6829df03f80ea444(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__9f3664b824e7a3e075da042c2c40a27e8787fa86890d22ff2a7b66431f1f324a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__2a21d9fa960648c86f33f88846e6b9b14dcc5e8c92b4ff490c15add137a6c850(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__9698bda0f347a5aa5b955513be3680c6baa6f808a9404251a58e0527898983f3(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__caaeacd0e52f756311e615dc8f93e0d5c0f0a32f18ae78593493e1d43bf508df(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__dddc46293d3bda332b4b9016e1757cc5b15dca4bd0910458d42fa984a32c1468(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__bdd53c4bb006d5535e30e1248bf10cd5876a0647b14470268503191afbad9e4b(
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
    cluster_id: builtins.str,
    name: builtins.str,
    size: builtins.str,
    auto_scale: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    id: typing.Optional[builtins.str] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    max_nodes: typing.Optional[jsii.Number] = None,
    min_nodes: typing.Optional[jsii.Number] = None,
    node_count: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    taint: typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.Sequence[
                typing.Union[
                    KubernetesNodePoolTaint, typing.Dict[builtins.str, typing.Any]
                ]
            ],
        ]
    ] = None,
    timeouts: typing.Optional[
        typing.Union[KubernetesNodePoolTimeouts, typing.Dict[builtins.str, typing.Any]]
    ] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__9b5bc966ec1e6e3d8f3fcf62bbb51b2035b4c8fec4097e81a0df3bd24023ebf2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__04423caeb0206a79d94771f84b3a73deb60be29558a3fbb5847ea369beee8a12(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__bb8379b64a8c03d5918a9d1a58dee10ac3ecbd0c2dee2c27d3295a60d15b9402(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__9d5920b6aa1553d56e49f9c298cb92e13ed75b96fa90e061fb1013ce1b116bd8(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__4aa065952e359a82153e665f79898076135e0894412c39047dd26d1dc8afc5ed(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__b3ca4989e0160f2dd1e766db6b4ba88c9418334b3a5152d37e8d5a51c773c032(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__ddc0c7e5c10dfc0728ad943d022601391bdbf599a1764503fda710d1fe247314(
    value: typing.Optional[KubernetesNodePoolNodes],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__6ca09b9351c5571f813ffb936bcf4ac6b7d9e2506966f55db5fa0caca6585b2c(
    *,
    effect: builtins.str,
    key: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__77a5b1a8a6be333cd34642176b324ddaba40e85fd3575058cd8b6dedce463933(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__864e6f99106ad5a1487107e4efe0190726283fefccd0b0b6508c112c305f9164(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__976178d330bae383fda6eae299f5b76c911c71a50e8a7a2d263c41a92b49ff71(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__512de989beb664dbad338d273fb5b8ba6b35fa3fb16efb69a97a334c2b12f335(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__237dd3841dc613ef8a8a58f0f54c1560177e622caa3328161626fea7b148c1b3(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__9a358076ebf6a6aa5a00a9b7d8596052f9ca20aa724dc8c4dc9bee8cf895448d(
    value: typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesNodePoolTaint]]
    ],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__45ce757c07633d22e527e5a5a7141f04b37fa551d0a5237a2e9c0b3496d691ff(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__80b60cf34705ad16e95a145b89eb5c0ab503e4d3d9544035c7d4c595b8f7f885(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__758881d555afde16bb0140bc1f45d381296c1d699d83920d0ef863fd6305b6aa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__7ac489706ed39638a971811c698103e802b87f2ba209bfad9bd27aa309d6a45b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__0d7391f282cd5641c5119eb3277570398a81dacfdfc1372a2be7895c95d2d4cc(
    value: typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesNodePoolTaint]
    ],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__3c2a04e00a88ddb1de0bbe940d8d797dfaa5035e825b62a45ecf3358eebc4e02(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__7b042f2b1f790e6616b0f0e3e7273a8fb1e44a374b3b1b9943d44bdd2b55d0ed(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__55983d3e1918006b298cbc0789f0ad3bfad5ff3556a23c0fca74512284a04afd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a0743e7924f42e612ed21cbc57f69fc04f29d165e70b43500426a86f5d3c5ec0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__b6fc520e2ff48abcdc652d055f11abdca6f74de5dd070550356e1ff6de82ba79(
    value: typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesNodePoolTimeouts]
    ],
) -> None:
    """Type checking stubs"""
    pass
