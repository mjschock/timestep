"""
# `data_digitalocean_kubernetes_cluster`

Refer to the Terraform Registory for docs: [`data_digitalocean_kubernetes_cluster`](https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/data-sources/kubernetes_cluster).
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


class DataDigitaloceanKubernetesCluster(
    _cdktf_9a9027ec.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.dataDigitaloceanKubernetesCluster.DataDigitaloceanKubernetesCluster",
):
    """Represents a {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/data-sources/kubernetes_cluster digitalocean_kubernetes_cluster}."""

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        id: typing.Optional[builtins.str] = None,
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
        """Create a new {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/data-sources/kubernetes_cluster digitalocean_kubernetes_cluster} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/data-sources/kubernetes_cluster#name DataDigitaloceanKubernetesCluster#name}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/data-sources/kubernetes_cluster#id DataDigitaloceanKubernetesCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/data-sources/kubernetes_cluster#tags DataDigitaloceanKubernetesCluster#tags}.
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
                _typecheckingstub__358cb1bbbe8631e79099580643fb3eee6eb904096d09dc34ecab6cc743f3543b
            )
            check_type(
                argname="argument scope", value=scope, expected_type=type_hints["scope"]
            )
            check_type(
                argname="argument id_", value=id_, expected_type=type_hints["id_"]
            )
        config = DataDigitaloceanKubernetesClusterConfig(
            name=name,
            id=id,
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

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

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
    @jsii.member(jsii_name="autoUpgrade")
    def auto_upgrade(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "autoUpgrade"))

    @builtins.property
    @jsii.member(jsii_name="clusterSubnet")
    def cluster_subnet(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterSubnet"))

    @builtins.property
    @jsii.member(jsii_name="createdAt")
    def created_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdAt"))

    @builtins.property
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpoint"))

    @builtins.property
    @jsii.member(jsii_name="ha")
    def ha(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "ha"))

    @builtins.property
    @jsii.member(jsii_name="ipv4Address")
    def ipv4_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipv4Address"))

    @builtins.property
    @jsii.member(jsii_name="kubeConfig")
    def kube_config(self) -> "DataDigitaloceanKubernetesClusterKubeConfigList":
        return typing.cast(
            "DataDigitaloceanKubernetesClusterKubeConfigList",
            jsii.get(self, "kubeConfig"),
        )

    @builtins.property
    @jsii.member(jsii_name="maintenancePolicy")
    def maintenance_policy(
        self,
    ) -> "DataDigitaloceanKubernetesClusterMaintenancePolicyList":
        return typing.cast(
            "DataDigitaloceanKubernetesClusterMaintenancePolicyList",
            jsii.get(self, "maintenancePolicy"),
        )

    @builtins.property
    @jsii.member(jsii_name="nodePool")
    def node_pool(self) -> "DataDigitaloceanKubernetesClusterNodePoolList":
        return typing.cast(
            "DataDigitaloceanKubernetesClusterNodePoolList", jsii.get(self, "nodePool")
        )

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @builtins.property
    @jsii.member(jsii_name="serviceSubnet")
    def service_subnet(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceSubnet"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="surgeUpgrade")
    def surge_upgrade(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "surgeUpgrade"))

    @builtins.property
    @jsii.member(jsii_name="updatedAt")
    def updated_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "updatedAt"))

    @builtins.property
    @jsii.member(jsii_name="urn")
    def urn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "urn"))

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @builtins.property
    @jsii.member(jsii_name="vpcUuid")
    def vpc_uuid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcUuid"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(
            typing.Optional[typing.List[builtins.str]], jsii.get(self, "tagsInput")
        )

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__744a505fd1ca62a263976d6d18ca78912db6bb50aa76cb01cb39fe40a8b32b7f
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
                _typecheckingstub__710d81f583b3b4fdcdd894752ea38f225f9a4bb5ed32b88e6ac509e95d1cc558
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
                _typecheckingstub__6416dbeaddd5563541e2e591e0c49a9106fb2121a7ce5252847230b0f49b65f2
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="digitalocean.dataDigitaloceanKubernetesCluster.DataDigitaloceanKubernetesClusterConfig",
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
        "id": "id",
        "tags": "tags",
    },
)
class DataDigitaloceanKubernetesClusterConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        id: typing.Optional[builtins.str] = None,
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
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/data-sources/kubernetes_cluster#name DataDigitaloceanKubernetesCluster#name}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/data-sources/kubernetes_cluster#id DataDigitaloceanKubernetesCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/data-sources/kubernetes_cluster#tags DataDigitaloceanKubernetesCluster#tags}.
        """
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__b5f6e5059e4e1ffe057be439dc0ef4788901886f63cc26a6afbbe8506067f3bb
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
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
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
        if id is not None:
            self._values["id"] = id
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
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/data-sources/kubernetes_cluster#name DataDigitaloceanKubernetesCluster#name}."""
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/data-sources/kubernetes_cluster#id DataDigitaloceanKubernetesCluster#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        """
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/data-sources/kubernetes_cluster#tags DataDigitaloceanKubernetesCluster#tags}."""
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDigitaloceanKubernetesClusterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="digitalocean.dataDigitaloceanKubernetesCluster.DataDigitaloceanKubernetesClusterKubeConfig",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataDigitaloceanKubernetesClusterKubeConfig:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDigitaloceanKubernetesClusterKubeConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataDigitaloceanKubernetesClusterKubeConfigList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.dataDigitaloceanKubernetesCluster.DataDigitaloceanKubernetesClusterKubeConfigList",
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
                _typecheckingstub__432b496671f1a869d2f887e2a30b052f2a4ad9a4652ebf6d588bd43ffabf3328
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
    def get(
        self,
        index: jsii.Number,
    ) -> "DataDigitaloceanKubernetesClusterKubeConfigOutputReference":
        """
        :param index: the index of the item to return.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__498b3050a1a39d5f5be1647f9d67506ba6e9f6287305169b65b12dd4741a2397
            )
            check_type(
                argname="argument index", value=index, expected_type=type_hints["index"]
            )
        return typing.cast(
            "DataDigitaloceanKubernetesClusterKubeConfigOutputReference",
            jsii.invoke(self, "get", [index]),
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
                _typecheckingstub__d2a21bea33185376c77c5f37399e619a2e199e881a8ca61a29af81342255480c
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
                _typecheckingstub__6087f6c8f9e7fce740e982dae844ea4b2f98386bd12722e66304b0df4288e887
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
                _typecheckingstub__c2a19486752223eac0212b1ed1c5fbeb8d9679e0adecd5b3cc925f69a4f6a7f5
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "wrapsSet", value)


class DataDigitaloceanKubernetesClusterKubeConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.dataDigitaloceanKubernetesCluster.DataDigitaloceanKubernetesClusterKubeConfigOutputReference",
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
                _typecheckingstub__552a3f1b0b3cd3513c5387faf28acdca5ac43e3c97726f367b8b5752af90e3d4
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
    @jsii.member(jsii_name="clientCertificate")
    def client_certificate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientCertificate"))

    @builtins.property
    @jsii.member(jsii_name="clientKey")
    def client_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientKey"))

    @builtins.property
    @jsii.member(jsii_name="clusterCaCertificate")
    def cluster_ca_certificate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterCaCertificate"))

    @builtins.property
    @jsii.member(jsii_name="expiresAt")
    def expires_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expiresAt"))

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "host"))

    @builtins.property
    @jsii.member(jsii_name="rawConfig")
    def raw_config(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rawConfig"))

    @builtins.property
    @jsii.member(jsii_name="token")
    def token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "token"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataDigitaloceanKubernetesClusterKubeConfig]:
        return typing.cast(
            typing.Optional[DataDigitaloceanKubernetesClusterKubeConfig],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataDigitaloceanKubernetesClusterKubeConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__a52cde72b3d4a7922514e65adc580def2d72be8dd9181259199914708ad6b5c8
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="digitalocean.dataDigitaloceanKubernetesCluster.DataDigitaloceanKubernetesClusterMaintenancePolicy",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataDigitaloceanKubernetesClusterMaintenancePolicy:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDigitaloceanKubernetesClusterMaintenancePolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataDigitaloceanKubernetesClusterMaintenancePolicyList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.dataDigitaloceanKubernetesCluster.DataDigitaloceanKubernetesClusterMaintenancePolicyList",
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
                _typecheckingstub__16fba8885f16378e5d52bfa489f03ccfd50861655eea8316e9c3c28342fd55a6
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
    def get(
        self,
        index: jsii.Number,
    ) -> "DataDigitaloceanKubernetesClusterMaintenancePolicyOutputReference":
        """
        :param index: the index of the item to return.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__adefb07721c42855b7c2ce4f45aafd01e5e0e782b188f7569060357ca9b2decd
            )
            check_type(
                argname="argument index", value=index, expected_type=type_hints["index"]
            )
        return typing.cast(
            "DataDigitaloceanKubernetesClusterMaintenancePolicyOutputReference",
            jsii.invoke(self, "get", [index]),
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
                _typecheckingstub__c401ea61298b7efddc5af5b698cbf4114330c6f538834f5d2d044b16c37d2bb5
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
                _typecheckingstub__bfdecdd98a2cac7d5126a1497eca183036c73e95e9e688291591f399256fd188
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
                _typecheckingstub__3920e120533f424c5b75d86af5687765c0417c1c274bfda7ee0a493e02be0b2e
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "wrapsSet", value)


class DataDigitaloceanKubernetesClusterMaintenancePolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.dataDigitaloceanKubernetesCluster.DataDigitaloceanKubernetesClusterMaintenancePolicyOutputReference",
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
                _typecheckingstub__440cfd46aa8a04815d46a78329887cb3f691c1c150f0f43a989e71fa61c6afaf
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
    @jsii.member(jsii_name="day")
    def day(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "day"))

    @builtins.property
    @jsii.member(jsii_name="duration")
    def duration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "duration"))

    @builtins.property
    @jsii.member(jsii_name="startTime")
    def start_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startTime"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataDigitaloceanKubernetesClusterMaintenancePolicy]:
        return typing.cast(
            typing.Optional[DataDigitaloceanKubernetesClusterMaintenancePolicy],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataDigitaloceanKubernetesClusterMaintenancePolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__dbf76cd55b748fa4bb34b409f2bc7d93619ceb5f2982c79c8dda52506fc39143
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="digitalocean.dataDigitaloceanKubernetesCluster.DataDigitaloceanKubernetesClusterNodePool",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataDigitaloceanKubernetesClusterNodePool:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDigitaloceanKubernetesClusterNodePool(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataDigitaloceanKubernetesClusterNodePoolList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.dataDigitaloceanKubernetesCluster.DataDigitaloceanKubernetesClusterNodePoolList",
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
                _typecheckingstub__c74c300b3773b20bd81531363735f2daef3d090df34221f2b904d4861d49aea9
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
    def get(
        self,
        index: jsii.Number,
    ) -> "DataDigitaloceanKubernetesClusterNodePoolOutputReference":
        """
        :param index: the index of the item to return.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__4dec71bbae593b635fd1288b9a64889deb4fd2b52319d373fbe01cf0184b746d
            )
            check_type(
                argname="argument index", value=index, expected_type=type_hints["index"]
            )
        return typing.cast(
            "DataDigitaloceanKubernetesClusterNodePoolOutputReference",
            jsii.invoke(self, "get", [index]),
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
                _typecheckingstub__accc9cf299d7ec48a8bd35b7cb19c0ff15954534d3f059fba70a816ac9d68c80
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
                _typecheckingstub__9f5d7f187dec1017c7a9a50446d12e683a2794b6e6d2d272b83fe0010b5eb551
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
                _typecheckingstub__9d49f01a220e8b71339626ab77e424460f5b327abbb81d1e770c5c3ee5a9feb7
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "wrapsSet", value)


@jsii.data_type(
    jsii_type="digitalocean.dataDigitaloceanKubernetesCluster.DataDigitaloceanKubernetesClusterNodePoolNodes",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataDigitaloceanKubernetesClusterNodePoolNodes:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDigitaloceanKubernetesClusterNodePoolNodes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataDigitaloceanKubernetesClusterNodePoolNodesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.dataDigitaloceanKubernetesCluster.DataDigitaloceanKubernetesClusterNodePoolNodesList",
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
                _typecheckingstub__5e5a83085b3d2f98bc4f408bc567bd6e3e26271d432372051621700a241c5397
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
    def get(
        self,
        index: jsii.Number,
    ) -> "DataDigitaloceanKubernetesClusterNodePoolNodesOutputReference":
        """
        :param index: the index of the item to return.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__eff35207dfd85af22a28561aadc75d3bfc00131d0b27c5b3f268011ff966a628
            )
            check_type(
                argname="argument index", value=index, expected_type=type_hints["index"]
            )
        return typing.cast(
            "DataDigitaloceanKubernetesClusterNodePoolNodesOutputReference",
            jsii.invoke(self, "get", [index]),
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
                _typecheckingstub__c3c357be10e23ba51a7969803a7762ac421acd6e4e0cc8d6cd9ad535f109d2e0
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
                _typecheckingstub__cb66e3416f384399ab37bcbb4a280728cb69df3cc924395cb2a4ea0781df1004
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
                _typecheckingstub__6595b6b070dda44e89f2c3cfab17d201a3174232b4d5b4168de57df1ea011d6c
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "wrapsSet", value)


class DataDigitaloceanKubernetesClusterNodePoolNodesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.dataDigitaloceanKubernetesCluster.DataDigitaloceanKubernetesClusterNodePoolNodesOutputReference",
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
                _typecheckingstub__3b03893d07b25a539a66c097f0cbfb7008af0efcee2ea99c5c9cfc6c3548814d
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
    def internal_value(
        self,
    ) -> typing.Optional[DataDigitaloceanKubernetesClusterNodePoolNodes]:
        return typing.cast(
            typing.Optional[DataDigitaloceanKubernetesClusterNodePoolNodes],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataDigitaloceanKubernetesClusterNodePoolNodes],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__9eb622e870cbb1a78e79d328a7f7f0061626c7867c7b115a3ff8ab7453737e49
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


class DataDigitaloceanKubernetesClusterNodePoolOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.dataDigitaloceanKubernetesCluster.DataDigitaloceanKubernetesClusterNodePoolOutputReference",
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
                _typecheckingstub__7a372808503acfed07e3ba0c39fede245a0eed9e6d86eb61cb1f550ecc82a3cb
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
    @jsii.member(jsii_name="actualNodeCount")
    def actual_node_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "actualNodeCount"))

    @builtins.property
    @jsii.member(jsii_name="autoScale")
    def auto_scale(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "autoScale"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> _cdktf_9a9027ec.StringMap:
        return typing.cast(_cdktf_9a9027ec.StringMap, jsii.get(self, "labels"))

    @builtins.property
    @jsii.member(jsii_name="maxNodes")
    def max_nodes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxNodes"))

    @builtins.property
    @jsii.member(jsii_name="minNodes")
    def min_nodes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minNodes"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="nodeCount")
    def node_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "nodeCount"))

    @builtins.property
    @jsii.member(jsii_name="nodes")
    def nodes(self) -> DataDigitaloceanKubernetesClusterNodePoolNodesList:
        return typing.cast(
            DataDigitaloceanKubernetesClusterNodePoolNodesList, jsii.get(self, "nodes")
        )

    @builtins.property
    @jsii.member(jsii_name="size")
    def size(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "size"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="taint")
    def taint(self) -> "DataDigitaloceanKubernetesClusterNodePoolTaintList":
        return typing.cast(
            "DataDigitaloceanKubernetesClusterNodePoolTaintList",
            jsii.get(self, "taint"),
        )

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataDigitaloceanKubernetesClusterNodePool]:
        return typing.cast(
            typing.Optional[DataDigitaloceanKubernetesClusterNodePool],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataDigitaloceanKubernetesClusterNodePool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__15ca8ecf0cf982414c066551cd3ab5a78caea626e1b1477cdcadb49d9eeb7026
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="digitalocean.dataDigitaloceanKubernetesCluster.DataDigitaloceanKubernetesClusterNodePoolTaint",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataDigitaloceanKubernetesClusterNodePoolTaint:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDigitaloceanKubernetesClusterNodePoolTaint(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataDigitaloceanKubernetesClusterNodePoolTaintList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.dataDigitaloceanKubernetesCluster.DataDigitaloceanKubernetesClusterNodePoolTaintList",
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
                _typecheckingstub__3ba57064690c282cb8183038e1263eb4ac9f5f9c316fe9c100b4028b0004548a
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
    def get(
        self,
        index: jsii.Number,
    ) -> "DataDigitaloceanKubernetesClusterNodePoolTaintOutputReference":
        """
        :param index: the index of the item to return.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__d666ebfadd55a49d5f7c6f351ff8b52b95498d9b516eefe532249e1ed4ad9402
            )
            check_type(
                argname="argument index", value=index, expected_type=type_hints["index"]
            )
        return typing.cast(
            "DataDigitaloceanKubernetesClusterNodePoolTaintOutputReference",
            jsii.invoke(self, "get", [index]),
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
                _typecheckingstub__e5e10b137430293f251077e9266a68299e88e71ac924d3d35223c64322a82aef
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
                _typecheckingstub__790041436a702942a011fd46a40b0eb468daad789d0785dbf72c5fef1c9d1bad
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
                _typecheckingstub__0be1dd13d95d1011e7267afe0016cdf911020894803af74d4011c3660bc4775a
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "wrapsSet", value)


class DataDigitaloceanKubernetesClusterNodePoolTaintOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.dataDigitaloceanKubernetesCluster.DataDigitaloceanKubernetesClusterNodePoolTaintOutputReference",
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
                _typecheckingstub__d2b4082bd9827924af5d665fd415059a0c84f792d6162647588f3fe10c2793cd
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
    @jsii.member(jsii_name="effect")
    def effect(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "effect"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataDigitaloceanKubernetesClusterNodePoolTaint]:
        return typing.cast(
            typing.Optional[DataDigitaloceanKubernetesClusterNodePoolTaint],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataDigitaloceanKubernetesClusterNodePoolTaint],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__30e9654f5bc2a2ed652eb7ec76ba42ad0270b59493758126096ee9c457e2c372
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataDigitaloceanKubernetesCluster",
    "DataDigitaloceanKubernetesClusterConfig",
    "DataDigitaloceanKubernetesClusterKubeConfig",
    "DataDigitaloceanKubernetesClusterKubeConfigList",
    "DataDigitaloceanKubernetesClusterKubeConfigOutputReference",
    "DataDigitaloceanKubernetesClusterMaintenancePolicy",
    "DataDigitaloceanKubernetesClusterMaintenancePolicyList",
    "DataDigitaloceanKubernetesClusterMaintenancePolicyOutputReference",
    "DataDigitaloceanKubernetesClusterNodePool",
    "DataDigitaloceanKubernetesClusterNodePoolList",
    "DataDigitaloceanKubernetesClusterNodePoolNodes",
    "DataDigitaloceanKubernetesClusterNodePoolNodesList",
    "DataDigitaloceanKubernetesClusterNodePoolNodesOutputReference",
    "DataDigitaloceanKubernetesClusterNodePoolOutputReference",
    "DataDigitaloceanKubernetesClusterNodePoolTaint",
    "DataDigitaloceanKubernetesClusterNodePoolTaintList",
    "DataDigitaloceanKubernetesClusterNodePoolTaintOutputReference",
]

publication.publish()


def _typecheckingstub__358cb1bbbe8631e79099580643fb3eee6eb904096d09dc34ecab6cc743f3543b(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    id: typing.Optional[builtins.str] = None,
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


def _typecheckingstub__744a505fd1ca62a263976d6d18ca78912db6bb50aa76cb01cb39fe40a8b32b7f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__710d81f583b3b4fdcdd894752ea38f225f9a4bb5ed32b88e6ac509e95d1cc558(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__6416dbeaddd5563541e2e591e0c49a9106fb2121a7ce5252847230b0f49b65f2(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__b5f6e5059e4e1ffe057be439dc0ef4788901886f63cc26a6afbbe8506067f3bb(
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
    id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__432b496671f1a869d2f887e2a30b052f2a4ad9a4652ebf6d588bd43ffabf3328(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__498b3050a1a39d5f5be1647f9d67506ba6e9f6287305169b65b12dd4741a2397(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d2a21bea33185376c77c5f37399e619a2e199e881a8ca61a29af81342255480c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__6087f6c8f9e7fce740e982dae844ea4b2f98386bd12722e66304b0df4288e887(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__c2a19486752223eac0212b1ed1c5fbeb8d9679e0adecd5b3cc925f69a4f6a7f5(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__552a3f1b0b3cd3513c5387faf28acdca5ac43e3c97726f367b8b5752af90e3d4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a52cde72b3d4a7922514e65adc580def2d72be8dd9181259199914708ad6b5c8(
    value: typing.Optional[DataDigitaloceanKubernetesClusterKubeConfig],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__16fba8885f16378e5d52bfa489f03ccfd50861655eea8316e9c3c28342fd55a6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__adefb07721c42855b7c2ce4f45aafd01e5e0e782b188f7569060357ca9b2decd(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__c401ea61298b7efddc5af5b698cbf4114330c6f538834f5d2d044b16c37d2bb5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__bfdecdd98a2cac7d5126a1497eca183036c73e95e9e688291591f399256fd188(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__3920e120533f424c5b75d86af5687765c0417c1c274bfda7ee0a493e02be0b2e(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__440cfd46aa8a04815d46a78329887cb3f691c1c150f0f43a989e71fa61c6afaf(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__dbf76cd55b748fa4bb34b409f2bc7d93619ceb5f2982c79c8dda52506fc39143(
    value: typing.Optional[DataDigitaloceanKubernetesClusterMaintenancePolicy],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__c74c300b3773b20bd81531363735f2daef3d090df34221f2b904d4861d49aea9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__4dec71bbae593b635fd1288b9a64889deb4fd2b52319d373fbe01cf0184b746d(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__accc9cf299d7ec48a8bd35b7cb19c0ff15954534d3f059fba70a816ac9d68c80(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__9f5d7f187dec1017c7a9a50446d12e683a2794b6e6d2d272b83fe0010b5eb551(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__9d49f01a220e8b71339626ab77e424460f5b327abbb81d1e770c5c3ee5a9feb7(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__5e5a83085b3d2f98bc4f408bc567bd6e3e26271d432372051621700a241c5397(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__eff35207dfd85af22a28561aadc75d3bfc00131d0b27c5b3f268011ff966a628(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__c3c357be10e23ba51a7969803a7762ac421acd6e4e0cc8d6cd9ad535f109d2e0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__cb66e3416f384399ab37bcbb4a280728cb69df3cc924395cb2a4ea0781df1004(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__6595b6b070dda44e89f2c3cfab17d201a3174232b4d5b4168de57df1ea011d6c(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__3b03893d07b25a539a66c097f0cbfb7008af0efcee2ea99c5c9cfc6c3548814d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__9eb622e870cbb1a78e79d328a7f7f0061626c7867c7b115a3ff8ab7453737e49(
    value: typing.Optional[DataDigitaloceanKubernetesClusterNodePoolNodes],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__7a372808503acfed07e3ba0c39fede245a0eed9e6d86eb61cb1f550ecc82a3cb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__15ca8ecf0cf982414c066551cd3ab5a78caea626e1b1477cdcadb49d9eeb7026(
    value: typing.Optional[DataDigitaloceanKubernetesClusterNodePool],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__3ba57064690c282cb8183038e1263eb4ac9f5f9c316fe9c100b4028b0004548a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d666ebfadd55a49d5f7c6f351ff8b52b95498d9b516eefe532249e1ed4ad9402(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__e5e10b137430293f251077e9266a68299e88e71ac924d3d35223c64322a82aef(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__790041436a702942a011fd46a40b0eb468daad789d0785dbf72c5fef1c9d1bad(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__0be1dd13d95d1011e7267afe0016cdf911020894803af74d4011c3660bc4775a(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d2b4082bd9827924af5d665fd415059a0c84f792d6162647588f3fe10c2793cd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__30e9654f5bc2a2ed652eb7ec76ba42ad0270b59493758126096ee9c457e2c372(
    value: typing.Optional[DataDigitaloceanKubernetesClusterNodePoolTaint],
) -> None:
    """Type checking stubs"""
    pass
