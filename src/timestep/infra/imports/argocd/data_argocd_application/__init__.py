'''
# `data_argocd_application`

Refer to the Terraform Registory for docs: [`data_argocd_application`](https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/data-sources/application).
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


class DataArgocdApplication(
    _cdktf_9a9027ec.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplication",
):
    '''Represents a {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/data-sources/application argocd_application}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        metadata: typing.Union["DataArgocdApplicationMetadata", typing.Dict[builtins.str, typing.Any]],
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/data-sources/application argocd_application} Data Source.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param metadata: Standard Kubernetes object metadata. For more info see the `Kubernetes reference <https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#metadata>`_. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/data-sources/application#metadata DataArgocdApplication#metadata}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da849c2c6b276983e97bec475e59b26dbd0f0d674064579bf325fd5fac97b54d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = DataArgocdApplicationConfig(
            metadata=metadata,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="putMetadata")
    def put_metadata(
        self,
        *,
        name: builtins.str,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the applications.argoproj.io, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/data-sources/application#name DataArgocdApplication#name}
        :param namespace: Namespace of the applications.argoproj.io, must be unique. Cannot be updated. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/data-sources/application#namespace DataArgocdApplication#namespace}
        '''
        value = DataArgocdApplicationMetadata(name=name, namespace=namespace)

        return typing.cast(None, jsii.invoke(self, "putMetadata", [value]))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> "DataArgocdApplicationMetadataOutputReference":
        return typing.cast("DataArgocdApplicationMetadataOutputReference", jsii.get(self, "metadata"))

    @builtins.property
    @jsii.member(jsii_name="spec")
    def spec(self) -> "DataArgocdApplicationSpecOutputReference":
        return typing.cast("DataArgocdApplicationSpecOutputReference", jsii.get(self, "spec"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> "DataArgocdApplicationStatusOutputReference":
        return typing.cast("DataArgocdApplicationStatusOutputReference", jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="metadataInput")
    def metadata_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, "DataArgocdApplicationMetadata"]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, "DataArgocdApplicationMetadata"]], jsii.get(self, "metadataInput"))


@jsii.data_type(
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "metadata": "metadata",
    },
)
class DataArgocdApplicationConfig(_cdktf_9a9027ec.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
        metadata: typing.Union["DataArgocdApplicationMetadata", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param metadata: Standard Kubernetes object metadata. For more info see the `Kubernetes reference <https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#metadata>`_. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/data-sources/application#metadata DataArgocdApplication#metadata}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(metadata, dict):
            metadata = DataArgocdApplicationMetadata(**metadata)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c144b90ddf6218190b622fd3166f3ee2bd352208703df251ab5ead6ccaca89aa)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "metadata": metadata,
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

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(
        self,
    ) -> typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]], result)

    @builtins.property
    def depends_on(
        self,
    ) -> typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[_cdktf_9a9027ec.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[_cdktf_9a9027ec.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]], result)

    @builtins.property
    def metadata(self) -> "DataArgocdApplicationMetadata":
        '''Standard Kubernetes object metadata. For more info see the `Kubernetes reference <https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#metadata>`_.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/data-sources/application#metadata DataArgocdApplication#metadata}
        '''
        result = self._values.get("metadata")
        assert result is not None, "Required property 'metadata' is missing"
        return typing.cast("DataArgocdApplicationMetadata", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataArgocdApplicationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationMetadata",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "namespace": "namespace"},
)
class DataArgocdApplicationMetadata:
    def __init__(
        self,
        *,
        name: builtins.str,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the applications.argoproj.io, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/data-sources/application#name DataArgocdApplication#name}
        :param namespace: Namespace of the applications.argoproj.io, must be unique. Cannot be updated. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/data-sources/application#namespace DataArgocdApplication#namespace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b9648322304ff60289eadea25472bb10532ad33912e9961dbf9a162e33a74a3)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if namespace is not None:
            self._values["namespace"] = namespace

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the applications.argoproj.io, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/data-sources/application#name DataArgocdApplication#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Namespace of the applications.argoproj.io, must be unique. Cannot be updated. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/data-sources/application#namespace DataArgocdApplication#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataArgocdApplicationMetadata(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataArgocdApplicationMetadataOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationMetadataOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e336e13820d322f98624e9ae323dc4730fb4ad17700a01fffdd81f508ed11ab)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @builtins.property
    @jsii.member(jsii_name="annotations")
    def annotations(self) -> _cdktf_9a9027ec.StringMap:
        return typing.cast(_cdktf_9a9027ec.StringMap, jsii.get(self, "annotations"))

    @builtins.property
    @jsii.member(jsii_name="generation")
    def generation(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "generation"))

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> _cdktf_9a9027ec.StringMap:
        return typing.cast(_cdktf_9a9027ec.StringMap, jsii.get(self, "labels"))

    @builtins.property
    @jsii.member(jsii_name="resourceVersion")
    def resource_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceVersion"))

    @builtins.property
    @jsii.member(jsii_name="uid")
    def uid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uid"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd373ce4b3bf791ed78f97ef6e6ef51cb64e09770e40e7623833d9f1ca7f5b6a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13a8e169aacfd9a3be4f390224d99519c93d1334affbc416f1a8326651ad662d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataArgocdApplicationMetadata]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataArgocdApplicationMetadata]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataArgocdApplicationMetadata]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd3beaa29f4a6a7de0c804fbbf80b237931cc1bda35ea89b09ca37bba12646f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationSpec",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataArgocdApplicationSpec:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataArgocdApplicationSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationSpecDestination",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataArgocdApplicationSpecDestination:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataArgocdApplicationSpecDestination(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataArgocdApplicationSpecDestinationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationSpecDestinationOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__edfeb2ea71abecb0b52c3bd94c480d88615acbfdb00f806b22687da9021e073d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @builtins.property
    @jsii.member(jsii_name="server")
    def server(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "server"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataArgocdApplicationSpecDestination]:
        return typing.cast(typing.Optional[DataArgocdApplicationSpecDestination], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataArgocdApplicationSpecDestination],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c260fd3749cda32d3ed3bd2eaedfb1726459eedf5e46bbc640ee9a6d967bb919)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationSpecIgnoreDifferences",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataArgocdApplicationSpecIgnoreDifferences:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataArgocdApplicationSpecIgnoreDifferences(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataArgocdApplicationSpecIgnoreDifferencesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationSpecIgnoreDifferencesList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c70a4b17ba3a31f80ab45b46d85185aaca664e909819b76c78c20242b8f8fcaf)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataArgocdApplicationSpecIgnoreDifferencesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e0408f837d1edf586afb0c04b67c6d3c47f74791cb82adb36ea353095c38a70)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataArgocdApplicationSpecIgnoreDifferencesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63cd19d18bcc136b5406bf303d6e7964d91eba558b1eaa1ea3dea625fd75b12e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5688cebab771b24ffb80a59a83f48e3c03fa0fb00694d116707b76651ddde06a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec4fc52d8e2d0cd207adcaa36c0269d5070d5935e593809ca46132ca77aeb2ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataArgocdApplicationSpecIgnoreDifferencesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationSpecIgnoreDifferencesOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9649e0a1ee65a53c25f6bfe9d89141750dfd387fe2a808d19505d948ef9b16c1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="group")
    def group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "group"))

    @builtins.property
    @jsii.member(jsii_name="jqPathExpressions")
    def jq_path_expressions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "jqPathExpressions"))

    @builtins.property
    @jsii.member(jsii_name="jsonPointers")
    def json_pointers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "jsonPointers"))

    @builtins.property
    @jsii.member(jsii_name="kind")
    def kind(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kind"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataArgocdApplicationSpecIgnoreDifferences]:
        return typing.cast(typing.Optional[DataArgocdApplicationSpecIgnoreDifferences], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataArgocdApplicationSpecIgnoreDifferences],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec937194a19679263f83127f66f06b1bffe5dfbe58f456ea7223c03b1ca2bf20)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationSpecInfos",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataArgocdApplicationSpecInfos:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataArgocdApplicationSpecInfos(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataArgocdApplicationSpecInfosList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationSpecInfosList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13251577fa2b4cefe9dd03f0ce1e5805df6efb1842867650d178faa1f5dd7292)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataArgocdApplicationSpecInfosOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d6cb04d6797cabf52d1b1388b73f9675e21624d2f55025c4e2dd0a426998ac3)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataArgocdApplicationSpecInfosOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eea48a36fa7a1981ab5993296c7f34e8f94878967c8e865545ec19a953dbe9e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0699889ee9c46b2505150ab44804f3beeeabd2714994e58006873dba8ed720d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4796c0cf2b119696081b60f10e437219bbf6d5f55d937367ab0a5341403961d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataArgocdApplicationSpecInfosOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationSpecInfosOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49d438ff81906f13731803f02764da8efc7900446809ab0d264464c6fa78c923)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataArgocdApplicationSpecInfos]:
        return typing.cast(typing.Optional[DataArgocdApplicationSpecInfos], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataArgocdApplicationSpecInfos],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1652296e474e7617d323a7334366da4ddeb013175e9b2b47d878457bccaea386)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataArgocdApplicationSpecOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationSpecOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c51e0deb546989a854d90e52203592180c400eff3d6feb0710287bfdfb12e17)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="destination")
    def destination(self) -> DataArgocdApplicationSpecDestinationOutputReference:
        return typing.cast(DataArgocdApplicationSpecDestinationOutputReference, jsii.get(self, "destination"))

    @builtins.property
    @jsii.member(jsii_name="ignoreDifferences")
    def ignore_differences(self) -> DataArgocdApplicationSpecIgnoreDifferencesList:
        return typing.cast(DataArgocdApplicationSpecIgnoreDifferencesList, jsii.get(self, "ignoreDifferences"))

    @builtins.property
    @jsii.member(jsii_name="infos")
    def infos(self) -> DataArgocdApplicationSpecInfosList:
        return typing.cast(DataArgocdApplicationSpecInfosList, jsii.get(self, "infos"))

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @builtins.property
    @jsii.member(jsii_name="revisionHistoryLimit")
    def revision_history_limit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "revisionHistoryLimit"))

    @builtins.property
    @jsii.member(jsii_name="sources")
    def sources(self) -> "DataArgocdApplicationSpecSourcesList":
        return typing.cast("DataArgocdApplicationSpecSourcesList", jsii.get(self, "sources"))

    @builtins.property
    @jsii.member(jsii_name="syncPolicy")
    def sync_policy(self) -> "DataArgocdApplicationSpecSyncPolicyOutputReference":
        return typing.cast("DataArgocdApplicationSpecSyncPolicyOutputReference", jsii.get(self, "syncPolicy"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataArgocdApplicationSpec]:
        return typing.cast(typing.Optional[DataArgocdApplicationSpec], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[DataArgocdApplicationSpec]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05b0b3599fd7a02a46f6b2b239819d84dc125361fdca2a0918d8fd83b0e47ed8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationSpecSources",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataArgocdApplicationSpecSources:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataArgocdApplicationSpecSources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationSpecSourcesDirectory",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataArgocdApplicationSpecSourcesDirectory:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataArgocdApplicationSpecSourcesDirectory(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationSpecSourcesDirectoryJsonnet",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataArgocdApplicationSpecSourcesDirectoryJsonnet:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataArgocdApplicationSpecSourcesDirectoryJsonnet(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationSpecSourcesDirectoryJsonnetExtVars",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataArgocdApplicationSpecSourcesDirectoryJsonnetExtVars:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataArgocdApplicationSpecSourcesDirectoryJsonnetExtVars(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataArgocdApplicationSpecSourcesDirectoryJsonnetExtVarsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationSpecSourcesDirectoryJsonnetExtVarsList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bdc0b535350f84c32888e9dae7088029cec99f0ace5f149cee3a343538b5a5c5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataArgocdApplicationSpecSourcesDirectoryJsonnetExtVarsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5bf037e915a4d69c77adff9172efb4cb013aec2453f2a84a0537cb66379a29b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataArgocdApplicationSpecSourcesDirectoryJsonnetExtVarsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c791d0ffd5d953e7f9244ed8b4643824903ca115bdf6502d23e11a6fc01bfe8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__873a89aa38c0050856d37f2eb67a8ebfe5277a25df8f04d00d160afc0f108c98)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b2fcbe2e1db54943119f090fe30b5272a5b60cef7a72a877e188415d2ee7776)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataArgocdApplicationSpecSourcesDirectoryJsonnetExtVarsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationSpecSourcesDirectoryJsonnetExtVarsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c28ed630d6ef1d4208c446bb896d72195fd56d3cf79b682f0f87cf1a7fd627b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="code")
    def code(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "code"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataArgocdApplicationSpecSourcesDirectoryJsonnetExtVars]:
        return typing.cast(typing.Optional[DataArgocdApplicationSpecSourcesDirectoryJsonnetExtVars], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataArgocdApplicationSpecSourcesDirectoryJsonnetExtVars],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53f8a6c8bbef2d592e12e02c36d7cab1706d0a6272c220ac816e8424c68fd2e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataArgocdApplicationSpecSourcesDirectoryJsonnetOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationSpecSourcesDirectoryJsonnetOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c25900dcd184ce1f484b868281ebd3bf23c6e17591b5edaec253441f5dbc037c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="extVars")
    def ext_vars(self) -> DataArgocdApplicationSpecSourcesDirectoryJsonnetExtVarsList:
        return typing.cast(DataArgocdApplicationSpecSourcesDirectoryJsonnetExtVarsList, jsii.get(self, "extVars"))

    @builtins.property
    @jsii.member(jsii_name="libs")
    def libs(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "libs"))

    @builtins.property
    @jsii.member(jsii_name="tlas")
    def tlas(self) -> "DataArgocdApplicationSpecSourcesDirectoryJsonnetTlasList":
        return typing.cast("DataArgocdApplicationSpecSourcesDirectoryJsonnetTlasList", jsii.get(self, "tlas"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataArgocdApplicationSpecSourcesDirectoryJsonnet]:
        return typing.cast(typing.Optional[DataArgocdApplicationSpecSourcesDirectoryJsonnet], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataArgocdApplicationSpecSourcesDirectoryJsonnet],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51ddc90960f0dbda7694f5643520467cbd78f80d241244e7e77c88ddec056fb2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationSpecSourcesDirectoryJsonnetTlas",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataArgocdApplicationSpecSourcesDirectoryJsonnetTlas:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataArgocdApplicationSpecSourcesDirectoryJsonnetTlas(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataArgocdApplicationSpecSourcesDirectoryJsonnetTlasList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationSpecSourcesDirectoryJsonnetTlasList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e00842e186de4c0f62342733589c55cb198a2564ad0ac1c08d28e2f7494b77a3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataArgocdApplicationSpecSourcesDirectoryJsonnetTlasOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa5c40ddb1a9878813818c6f399a74021e784f58ec899acbf09ccda475ad3369)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataArgocdApplicationSpecSourcesDirectoryJsonnetTlasOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c10ffdd37296dafdbef50b481b70fcf3731c1b239e074920b4ded852169c015d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5963612f868dd93c095dbe0e75e0a8d76e06631e28747ae4af665c58850e7ecf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ecd7bac057f8b91b135ed9c2ab94e000f36ac0165acf2a08638c59a309819259)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataArgocdApplicationSpecSourcesDirectoryJsonnetTlasOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationSpecSourcesDirectoryJsonnetTlasOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e97c858008ae8e752b1b38a70b85c28f935ed7d43ba1a091cc672881b623430)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="code")
    def code(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "code"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataArgocdApplicationSpecSourcesDirectoryJsonnetTlas]:
        return typing.cast(typing.Optional[DataArgocdApplicationSpecSourcesDirectoryJsonnetTlas], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataArgocdApplicationSpecSourcesDirectoryJsonnetTlas],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c897e53013cefd0d43b3d4a3ad8619e311d905cdee6bf108caa31d589727f2b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataArgocdApplicationSpecSourcesDirectoryOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationSpecSourcesDirectoryOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b38d5c432957fb29bc66544c4c4cc6adb3b9b85c765cadff3e2be3f7f7dc0fa9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="exclude")
    def exclude(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "exclude"))

    @builtins.property
    @jsii.member(jsii_name="include")
    def include(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "include"))

    @builtins.property
    @jsii.member(jsii_name="jsonnet")
    def jsonnet(
        self,
    ) -> DataArgocdApplicationSpecSourcesDirectoryJsonnetOutputReference:
        return typing.cast(DataArgocdApplicationSpecSourcesDirectoryJsonnetOutputReference, jsii.get(self, "jsonnet"))

    @builtins.property
    @jsii.member(jsii_name="recurse")
    def recurse(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "recurse"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataArgocdApplicationSpecSourcesDirectory]:
        return typing.cast(typing.Optional[DataArgocdApplicationSpecSourcesDirectory], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataArgocdApplicationSpecSourcesDirectory],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd334a0a0a964116837dd1989137c59d07709e5327b613e0ec6e38b8c4a067d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationSpecSourcesHelm",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataArgocdApplicationSpecSourcesHelm:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataArgocdApplicationSpecSourcesHelm(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationSpecSourcesHelmFileParameters",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataArgocdApplicationSpecSourcesHelmFileParameters:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataArgocdApplicationSpecSourcesHelmFileParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataArgocdApplicationSpecSourcesHelmFileParametersList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationSpecSourcesHelmFileParametersList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d2e3b5805b9acd796aae35d19e1c0f9b6c4984e00af7394b42e665f83679466)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataArgocdApplicationSpecSourcesHelmFileParametersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c375a80fe6f031d172c4a1b012d60159f7d4f591c0b17184f34aea0a6f48dc2)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataArgocdApplicationSpecSourcesHelmFileParametersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88a002f89b8653414c27424f097afb55636841bf05bfe5a8747e72cedc411962)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd162b2d5bd8c60f6cc393cba4ad8dd172861113df3d9cdcd0d814c32d3c87b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d5b3aef52ec52dce12b14fb3ff15fc3bf04c661cb335756be786855efaf42ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataArgocdApplicationSpecSourcesHelmFileParametersOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationSpecSourcesHelmFileParametersOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c84c2d4d5368bf60d16468eec780a9405d9f711cea680b2652c5b909fd99cbe)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataArgocdApplicationSpecSourcesHelmFileParameters]:
        return typing.cast(typing.Optional[DataArgocdApplicationSpecSourcesHelmFileParameters], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataArgocdApplicationSpecSourcesHelmFileParameters],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9647996d80fb7a77ec42d72387315f3aec004a537032fb3c64c38fe90db3b4f6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataArgocdApplicationSpecSourcesHelmOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationSpecSourcesHelmOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f499af335d8c5611d051c4d3a0053f0661f546c3df398d72770ad40a3b1a020b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="fileParameters")
    def file_parameters(self) -> DataArgocdApplicationSpecSourcesHelmFileParametersList:
        return typing.cast(DataArgocdApplicationSpecSourcesHelmFileParametersList, jsii.get(self, "fileParameters"))

    @builtins.property
    @jsii.member(jsii_name="ignoreMissingValueFiles")
    def ignore_missing_value_files(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "ignoreMissingValueFiles"))

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> "DataArgocdApplicationSpecSourcesHelmParametersList":
        return typing.cast("DataArgocdApplicationSpecSourcesHelmParametersList", jsii.get(self, "parameters"))

    @builtins.property
    @jsii.member(jsii_name="passCredentials")
    def pass_credentials(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "passCredentials"))

    @builtins.property
    @jsii.member(jsii_name="releaseName")
    def release_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "releaseName"))

    @builtins.property
    @jsii.member(jsii_name="skipCrds")
    def skip_crds(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "skipCrds"))

    @builtins.property
    @jsii.member(jsii_name="valueFiles")
    def value_files(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "valueFiles"))

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "values"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataArgocdApplicationSpecSourcesHelm]:
        return typing.cast(typing.Optional[DataArgocdApplicationSpecSourcesHelm], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataArgocdApplicationSpecSourcesHelm],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b98c6becba2277e2744126afb0f72ce615609311db919f677ddb86cbe3551412)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationSpecSourcesHelmParameters",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataArgocdApplicationSpecSourcesHelmParameters:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataArgocdApplicationSpecSourcesHelmParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataArgocdApplicationSpecSourcesHelmParametersList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationSpecSourcesHelmParametersList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2763acc6405bf714601ff3e5e21cfcf59da85d74141aa02d7eb637f5dd60fe88)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataArgocdApplicationSpecSourcesHelmParametersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01f5a457549c7f9abdd1dedf0a7e9ff4a70e7b77ce1bbec3ec9f2af6282f992b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataArgocdApplicationSpecSourcesHelmParametersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e54ebab58c7c9c690cdd60a52ca46fa94bb304c94c0802d4659b3c7212a505e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4add129435e85befc0ab5cfa7a9472ce800eee8ed3856e4acf34e27144ccceb4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c150f2126fad87205c1ce8a908a3dba4d728eb63887265b6293a466c8c16cd0c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataArgocdApplicationSpecSourcesHelmParametersOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationSpecSourcesHelmParametersOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb7035a0498ec3ab55d97896a56ed8e7fadbcacd3d5a51429ac9f241e4d2d138)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="forceString")
    def force_string(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "forceString"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataArgocdApplicationSpecSourcesHelmParameters]:
        return typing.cast(typing.Optional[DataArgocdApplicationSpecSourcesHelmParameters], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataArgocdApplicationSpecSourcesHelmParameters],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2aea9c59c1396a2ab3584202ed24cbb0c7b2ae0d10bd70d65f449aa12c31cb6a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationSpecSourcesKustomize",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataArgocdApplicationSpecSourcesKustomize:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataArgocdApplicationSpecSourcesKustomize(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataArgocdApplicationSpecSourcesKustomizeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationSpecSourcesKustomizeOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f8d4b88a253ecdded80c87937616bbe4a1e2dd634fffd7d8df487de91894539)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="commonAnnotations")
    def common_annotations(self) -> _cdktf_9a9027ec.StringMap:
        return typing.cast(_cdktf_9a9027ec.StringMap, jsii.get(self, "commonAnnotations"))

    @builtins.property
    @jsii.member(jsii_name="commonLabels")
    def common_labels(self) -> _cdktf_9a9027ec.StringMap:
        return typing.cast(_cdktf_9a9027ec.StringMap, jsii.get(self, "commonLabels"))

    @builtins.property
    @jsii.member(jsii_name="images")
    def images(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "images"))

    @builtins.property
    @jsii.member(jsii_name="namePrefix")
    def name_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namePrefix"))

    @builtins.property
    @jsii.member(jsii_name="nameSuffix")
    def name_suffix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nameSuffix"))

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataArgocdApplicationSpecSourcesKustomize]:
        return typing.cast(typing.Optional[DataArgocdApplicationSpecSourcesKustomize], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataArgocdApplicationSpecSourcesKustomize],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__033e4e1a41eae9e323f5eb5da97441c627da20b8d110c7f97ae20205252a781f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataArgocdApplicationSpecSourcesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationSpecSourcesList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e4bb5aebf8bf26574a99df68ca6e173d958910a71e6af231236f91b2bb8f5eb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataArgocdApplicationSpecSourcesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e24131c903aea3e9c82a6776c589e9ad775451a8952c1f2c0c0e1070adb5f9f6)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataArgocdApplicationSpecSourcesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__766ba84a7b31b96186c482b535725cc6ffc3249662869e0f473b07110d155957)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d54099aa0d8e1909344a4a0c70bfb5a98f50fffa2c3978a2d07fa2ee164921b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ea73f819d90cc7926353d0ecdd9e686f840f18d7d2ab4ed88347b0b6e894a3f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataArgocdApplicationSpecSourcesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationSpecSourcesOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d1acdab45a105c76bf76e3f0f00f31ddeb1ccff217fbe6338a7a93d0a44fa0f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="chart")
    def chart(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "chart"))

    @builtins.property
    @jsii.member(jsii_name="directory")
    def directory(self) -> DataArgocdApplicationSpecSourcesDirectoryOutputReference:
        return typing.cast(DataArgocdApplicationSpecSourcesDirectoryOutputReference, jsii.get(self, "directory"))

    @builtins.property
    @jsii.member(jsii_name="helm")
    def helm(self) -> DataArgocdApplicationSpecSourcesHelmOutputReference:
        return typing.cast(DataArgocdApplicationSpecSourcesHelmOutputReference, jsii.get(self, "helm"))

    @builtins.property
    @jsii.member(jsii_name="kustomize")
    def kustomize(self) -> DataArgocdApplicationSpecSourcesKustomizeOutputReference:
        return typing.cast(DataArgocdApplicationSpecSourcesKustomizeOutputReference, jsii.get(self, "kustomize"))

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @builtins.property
    @jsii.member(jsii_name="plugin")
    def plugin(self) -> "DataArgocdApplicationSpecSourcesPluginOutputReference":
        return typing.cast("DataArgocdApplicationSpecSourcesPluginOutputReference", jsii.get(self, "plugin"))

    @builtins.property
    @jsii.member(jsii_name="ref")
    def ref(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ref"))

    @builtins.property
    @jsii.member(jsii_name="repoUrl")
    def repo_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repoUrl"))

    @builtins.property
    @jsii.member(jsii_name="targetRevision")
    def target_revision(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetRevision"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataArgocdApplicationSpecSources]:
        return typing.cast(typing.Optional[DataArgocdApplicationSpecSources], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataArgocdApplicationSpecSources],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e6734a91c0a01e0e3bdc3e7cf40128db598f23ae17da30804e69d375913fcca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationSpecSourcesPlugin",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataArgocdApplicationSpecSourcesPlugin:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataArgocdApplicationSpecSourcesPlugin(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationSpecSourcesPluginEnv",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataArgocdApplicationSpecSourcesPluginEnv:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataArgocdApplicationSpecSourcesPluginEnv(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataArgocdApplicationSpecSourcesPluginEnvList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationSpecSourcesPluginEnvList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__764ee72bd9c40e229e072bd4d55efcb0160263014fca123ece15a87ce8b95924)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataArgocdApplicationSpecSourcesPluginEnvOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f5a0b28d0695894486ff83ea8855a6c9141811bf310384cd64a7ebe48970d8e)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataArgocdApplicationSpecSourcesPluginEnvOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aec2affbf5010ee5796922b711ac09d91bd3a831b659cea5f4a6e9a0b92067b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a7649813575f87df44134c949a736d8516158732cdfa7b6726c1f8e96642b39)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6bbec39ca7cdd6d594d97c4cfe86b3f20075a599ca0bce8835ec4c8dd59cf709)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataArgocdApplicationSpecSourcesPluginEnvOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationSpecSourcesPluginEnvOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d222476e5236d9eb0502cf17a3d31e81dd1239fbe340286b641bd830d5d135d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataArgocdApplicationSpecSourcesPluginEnv]:
        return typing.cast(typing.Optional[DataArgocdApplicationSpecSourcesPluginEnv], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataArgocdApplicationSpecSourcesPluginEnv],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5bb813ae4b04af8e3abbc1d653fd78da1dc6d3e4745d7fd9c338064b8ad7cdf1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataArgocdApplicationSpecSourcesPluginOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationSpecSourcesPluginOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd653fdc6aebad68008365e96f7a0d2e1e87af33b95103b4c78f136bbc5150bc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="env")
    def env(self) -> DataArgocdApplicationSpecSourcesPluginEnvList:
        return typing.cast(DataArgocdApplicationSpecSourcesPluginEnvList, jsii.get(self, "env"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> "DataArgocdApplicationSpecSourcesPluginParametersList":
        return typing.cast("DataArgocdApplicationSpecSourcesPluginParametersList", jsii.get(self, "parameters"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataArgocdApplicationSpecSourcesPlugin]:
        return typing.cast(typing.Optional[DataArgocdApplicationSpecSourcesPlugin], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataArgocdApplicationSpecSourcesPlugin],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d18fb1c3d3db91aafdd38900e5ebb147e76ec018f5384ff7204f8525715c6477)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationSpecSourcesPluginParameters",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataArgocdApplicationSpecSourcesPluginParameters:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataArgocdApplicationSpecSourcesPluginParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataArgocdApplicationSpecSourcesPluginParametersList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationSpecSourcesPluginParametersList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cdad7e86bd1d8c14268b1a6fa313a8992e0129592cc4c2ebf40cdb4ee18cfdb7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataArgocdApplicationSpecSourcesPluginParametersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c3e2bfdf9ae291a37fa4c4d2a182a9dcd39828d4bd4105f6aa18571e0eded80)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataArgocdApplicationSpecSourcesPluginParametersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f312edf6d3eab87c5eb2f070176360dcd633895d8ee348d53ed647a2d35379b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__639b47616ec7c26f4aac4dc5411a7389c80863b555ee54fb67a35c18a647009b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad73b22d25720467dbb152835e6deb1b0bad32b663553bdd85955d172d897023)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataArgocdApplicationSpecSourcesPluginParametersOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationSpecSourcesPluginParametersOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c08f1fffaafae3e564eb1891ec05fb80cae877fc0e849e8ed0472165f8ce895d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="array")
    def array(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "array"))

    @builtins.property
    @jsii.member(jsii_name="map")
    def map(self) -> _cdktf_9a9027ec.StringMap:
        return typing.cast(_cdktf_9a9027ec.StringMap, jsii.get(self, "map"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="string")
    def string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "string"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataArgocdApplicationSpecSourcesPluginParameters]:
        return typing.cast(typing.Optional[DataArgocdApplicationSpecSourcesPluginParameters], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataArgocdApplicationSpecSourcesPluginParameters],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df125d31de3d061fc1b2ff72d9c6069e248b34388c200438573d716c4d1f09e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationSpecSyncPolicy",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataArgocdApplicationSpecSyncPolicy:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataArgocdApplicationSpecSyncPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationSpecSyncPolicyAutomated",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataArgocdApplicationSpecSyncPolicyAutomated:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataArgocdApplicationSpecSyncPolicyAutomated(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataArgocdApplicationSpecSyncPolicyAutomatedOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationSpecSyncPolicyAutomatedOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5f7fbbcb0ccc5ab1bd80e11d4d4af7ce11422d7141f6b47a0d2ddcd6f8ffe6e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="allowEmpty")
    def allow_empty(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "allowEmpty"))

    @builtins.property
    @jsii.member(jsii_name="prune")
    def prune(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "prune"))

    @builtins.property
    @jsii.member(jsii_name="selfHeal")
    def self_heal(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "selfHeal"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataArgocdApplicationSpecSyncPolicyAutomated]:
        return typing.cast(typing.Optional[DataArgocdApplicationSpecSyncPolicyAutomated], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataArgocdApplicationSpecSyncPolicyAutomated],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1df3d0b5e7ede38b330737190f5656118c6b21b1f3107ee0cb44987eddab13b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataArgocdApplicationSpecSyncPolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationSpecSyncPolicyOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2a7f133d80b9e9ab2cde5730b5193e90b64933a22aa5ad4712d01b7664270fb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="automated")
    def automated(self) -> DataArgocdApplicationSpecSyncPolicyAutomatedOutputReference:
        return typing.cast(DataArgocdApplicationSpecSyncPolicyAutomatedOutputReference, jsii.get(self, "automated"))

    @builtins.property
    @jsii.member(jsii_name="retry")
    def retry(self) -> "DataArgocdApplicationSpecSyncPolicyRetryOutputReference":
        return typing.cast("DataArgocdApplicationSpecSyncPolicyRetryOutputReference", jsii.get(self, "retry"))

    @builtins.property
    @jsii.member(jsii_name="syncOptions")
    def sync_options(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "syncOptions"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataArgocdApplicationSpecSyncPolicy]:
        return typing.cast(typing.Optional[DataArgocdApplicationSpecSyncPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataArgocdApplicationSpecSyncPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b51cdc650400feedc8325a3d97bb7bec6c9e16de3b5f18a46b906a60c7beabc5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationSpecSyncPolicyRetry",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataArgocdApplicationSpecSyncPolicyRetry:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataArgocdApplicationSpecSyncPolicyRetry(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationSpecSyncPolicyRetryBackoff",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataArgocdApplicationSpecSyncPolicyRetryBackoff:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataArgocdApplicationSpecSyncPolicyRetryBackoff(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataArgocdApplicationSpecSyncPolicyRetryBackoffOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationSpecSyncPolicyRetryBackoffOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4327f06bdd27faa68b3259e1e05689266c22cc893b43bdedaf3fb488cae3b48d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="duration")
    def duration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "duration"))

    @builtins.property
    @jsii.member(jsii_name="factor")
    def factor(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "factor"))

    @builtins.property
    @jsii.member(jsii_name="maxDuration")
    def max_duration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxDuration"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataArgocdApplicationSpecSyncPolicyRetryBackoff]:
        return typing.cast(typing.Optional[DataArgocdApplicationSpecSyncPolicyRetryBackoff], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataArgocdApplicationSpecSyncPolicyRetryBackoff],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa5c1020d30ba5575af7cd622836ada71c99dd9a895628dfc97bb98149cf92dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataArgocdApplicationSpecSyncPolicyRetryOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationSpecSyncPolicyRetryOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9ad2e8aa10c4c7adc59ba2e5f94c509316eb08d85ad093df8562aec3b089c89)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="backoff")
    def backoff(self) -> DataArgocdApplicationSpecSyncPolicyRetryBackoffOutputReference:
        return typing.cast(DataArgocdApplicationSpecSyncPolicyRetryBackoffOutputReference, jsii.get(self, "backoff"))

    @builtins.property
    @jsii.member(jsii_name="limit")
    def limit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "limit"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataArgocdApplicationSpecSyncPolicyRetry]:
        return typing.cast(typing.Optional[DataArgocdApplicationSpecSyncPolicyRetry], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataArgocdApplicationSpecSyncPolicyRetry],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94f54d82f3718e3d8ea806f434504cbec608211ec983c91a20013a375ff83be9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationStatus",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataArgocdApplicationStatus:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataArgocdApplicationStatus(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationStatusConditions",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataArgocdApplicationStatusConditions:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataArgocdApplicationStatusConditions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataArgocdApplicationStatusConditionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationStatusConditionsList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e327a866960515c76b6f7a26520618084ea56464a4786a98d7d07b8874c6d3b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataArgocdApplicationStatusConditionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ae8eb9c9f1360732fead94c40eb7a0166991ef815565cdfea6e01fac1a7e24b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataArgocdApplicationStatusConditionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9be49da50766d90a90a80183d1d7d537bb7ba1ed13992a9a881be16d3e83264)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__382a2e677dcb54fc989e86e6865198b931851b3dcd4080561302a062e3d1f0ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78512262cb756ca2e1f81bc5064b73aa53e313383b3e5a25e097618a9e532fcc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataArgocdApplicationStatusConditionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationStatusConditionsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c44824ebd74b0d41bd369e41fc8cebadb2a9095b5f4355413c51bcb2bd6968b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="lastTransitionTime")
    def last_transition_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastTransitionTime"))

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "message"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataArgocdApplicationStatusConditions]:
        return typing.cast(typing.Optional[DataArgocdApplicationStatusConditions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataArgocdApplicationStatusConditions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f72bee223f96dd86716c0da06f6ea4539dd4e575cad9a02438438d4454ae673)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationStatusHealth",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataArgocdApplicationStatusHealth:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataArgocdApplicationStatusHealth(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataArgocdApplicationStatusHealthOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationStatusHealthOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a70642459330848df48f1733af2ab15bf8ed560701889071c16f7f637ea4e98)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "message"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataArgocdApplicationStatusHealth]:
        return typing.cast(typing.Optional[DataArgocdApplicationStatusHealth], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataArgocdApplicationStatusHealth],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__963e46b71cd89eda559bda31effd9dd2adef057cead56d6863e3c4decf88d535)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationStatusOperationState",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataArgocdApplicationStatusOperationState:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataArgocdApplicationStatusOperationState(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataArgocdApplicationStatusOperationStateOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationStatusOperationStateOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f383318b9c648a1582e6d302a825fd33bce10e04abb76c151d8ffab2e02bc211)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="finishedAt")
    def finished_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "finishedAt"))

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "message"))

    @builtins.property
    @jsii.member(jsii_name="phase")
    def phase(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "phase"))

    @builtins.property
    @jsii.member(jsii_name="retryCount")
    def retry_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retryCount"))

    @builtins.property
    @jsii.member(jsii_name="startedAt")
    def started_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startedAt"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataArgocdApplicationStatusOperationState]:
        return typing.cast(typing.Optional[DataArgocdApplicationStatusOperationState], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataArgocdApplicationStatusOperationState],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c31ef5edc7aea6b522ba83efba7c2c4fa37ab11f75901ccf10c04ea1bda31615)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataArgocdApplicationStatusOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationStatusOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11517ff603e5a51f0e16126c28bf8b67c784fdc60f91a69072dd05c197c62320)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="conditions")
    def conditions(self) -> DataArgocdApplicationStatusConditionsList:
        return typing.cast(DataArgocdApplicationStatusConditionsList, jsii.get(self, "conditions"))

    @builtins.property
    @jsii.member(jsii_name="health")
    def health(self) -> DataArgocdApplicationStatusHealthOutputReference:
        return typing.cast(DataArgocdApplicationStatusHealthOutputReference, jsii.get(self, "health"))

    @builtins.property
    @jsii.member(jsii_name="operationState")
    def operation_state(
        self,
    ) -> DataArgocdApplicationStatusOperationStateOutputReference:
        return typing.cast(DataArgocdApplicationStatusOperationStateOutputReference, jsii.get(self, "operationState"))

    @builtins.property
    @jsii.member(jsii_name="reconciledAt")
    def reconciled_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "reconciledAt"))

    @builtins.property
    @jsii.member(jsii_name="resources")
    def resources(self) -> "DataArgocdApplicationStatusResourcesList":
        return typing.cast("DataArgocdApplicationStatusResourcesList", jsii.get(self, "resources"))

    @builtins.property
    @jsii.member(jsii_name="summary")
    def summary(self) -> "DataArgocdApplicationStatusSummaryOutputReference":
        return typing.cast("DataArgocdApplicationStatusSummaryOutputReference", jsii.get(self, "summary"))

    @builtins.property
    @jsii.member(jsii_name="sync")
    def sync(self) -> "DataArgocdApplicationStatusSyncOutputReference":
        return typing.cast("DataArgocdApplicationStatusSyncOutputReference", jsii.get(self, "sync"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataArgocdApplicationStatus]:
        return typing.cast(typing.Optional[DataArgocdApplicationStatus], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataArgocdApplicationStatus],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b81f01f85f774d977b2091f13ec6773b6597b677251ed194bd234b8b340ad75)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationStatusResources",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataArgocdApplicationStatusResources:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataArgocdApplicationStatusResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationStatusResourcesHealth",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataArgocdApplicationStatusResourcesHealth:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataArgocdApplicationStatusResourcesHealth(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataArgocdApplicationStatusResourcesHealthOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationStatusResourcesHealthOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96c8070621b47e3ff7661e31e73651421708529b60d7a0b5cf28c634b84c8dba)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "message"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataArgocdApplicationStatusResourcesHealth]:
        return typing.cast(typing.Optional[DataArgocdApplicationStatusResourcesHealth], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataArgocdApplicationStatusResourcesHealth],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1812c0899dc731d7c6e958ecda88b0ca2e9c3f8fd5880d9dc6f14b6ee5797a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataArgocdApplicationStatusResourcesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationStatusResourcesList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97a098415cf050109d69fdf9251cf92e0a3945b4007e0b98900e5704f0f7c5e6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataArgocdApplicationStatusResourcesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15ff382853dc4515e8135306d2dc6fd463d0272a4728a3298a899070806921fe)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataArgocdApplicationStatusResourcesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfebc843cac9d1d44aca1dd18238e681a852d86f5d081ec02aca362cdab707d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb1c2983a88b0e13b3a7e084d024237bae827f8b20b1cd59ae87c321bbd38d3f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44c082dd57d4aa7bf60b3055bcd5da00d5dcaf7ec008eecaafb177a272718e2e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataArgocdApplicationStatusResourcesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationStatusResourcesOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb1639959707d964308d941109e74dc66fe84e43093b7902ee0be3ca251e9959)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="group")
    def group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "group"))

    @builtins.property
    @jsii.member(jsii_name="health")
    def health(self) -> DataArgocdApplicationStatusResourcesHealthOutputReference:
        return typing.cast(DataArgocdApplicationStatusResourcesHealthOutputReference, jsii.get(self, "health"))

    @builtins.property
    @jsii.member(jsii_name="hook")
    def hook(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "hook"))

    @builtins.property
    @jsii.member(jsii_name="kind")
    def kind(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kind"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @builtins.property
    @jsii.member(jsii_name="requiresPruning")
    def requires_pruning(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "requiresPruning"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="syncWave")
    def sync_wave(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "syncWave"))

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataArgocdApplicationStatusResources]:
        return typing.cast(typing.Optional[DataArgocdApplicationStatusResources], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataArgocdApplicationStatusResources],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9285bca1d9df517eb7530cbe7a0934d50f6dbaadfbc443335bf0d69953a3330)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationStatusSummary",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataArgocdApplicationStatusSummary:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataArgocdApplicationStatusSummary(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataArgocdApplicationStatusSummaryOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationStatusSummaryOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ce6d0d6606e451f8129933ac618b1f432a4add59ec92ffccbaf512372b6341b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="externalUrls")
    def external_urls(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "externalUrls"))

    @builtins.property
    @jsii.member(jsii_name="images")
    def images(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "images"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataArgocdApplicationStatusSummary]:
        return typing.cast(typing.Optional[DataArgocdApplicationStatusSummary], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataArgocdApplicationStatusSummary],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85919e7233c6f07ea3535485fec71c07ab172e0f0c08ce1f805f51bd7474f81c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationStatusSync",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataArgocdApplicationStatusSync:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataArgocdApplicationStatusSync(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataArgocdApplicationStatusSyncOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.dataArgocdApplication.DataArgocdApplicationStatusSyncOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__373e19753f2ebae5d4ba9ed82bff9be4939c4bc143a49f27f99051f52ab5d5ce)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="revisions")
    def revisions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "revisions"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataArgocdApplicationStatusSync]:
        return typing.cast(typing.Optional[DataArgocdApplicationStatusSync], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataArgocdApplicationStatusSync],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__307a82a7147d4ecd8be89e345f58add124c92d698bba288a3f9895d1f17dab9a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataArgocdApplication",
    "DataArgocdApplicationConfig",
    "DataArgocdApplicationMetadata",
    "DataArgocdApplicationMetadataOutputReference",
    "DataArgocdApplicationSpec",
    "DataArgocdApplicationSpecDestination",
    "DataArgocdApplicationSpecDestinationOutputReference",
    "DataArgocdApplicationSpecIgnoreDifferences",
    "DataArgocdApplicationSpecIgnoreDifferencesList",
    "DataArgocdApplicationSpecIgnoreDifferencesOutputReference",
    "DataArgocdApplicationSpecInfos",
    "DataArgocdApplicationSpecInfosList",
    "DataArgocdApplicationSpecInfosOutputReference",
    "DataArgocdApplicationSpecOutputReference",
    "DataArgocdApplicationSpecSources",
    "DataArgocdApplicationSpecSourcesDirectory",
    "DataArgocdApplicationSpecSourcesDirectoryJsonnet",
    "DataArgocdApplicationSpecSourcesDirectoryJsonnetExtVars",
    "DataArgocdApplicationSpecSourcesDirectoryJsonnetExtVarsList",
    "DataArgocdApplicationSpecSourcesDirectoryJsonnetExtVarsOutputReference",
    "DataArgocdApplicationSpecSourcesDirectoryJsonnetOutputReference",
    "DataArgocdApplicationSpecSourcesDirectoryJsonnetTlas",
    "DataArgocdApplicationSpecSourcesDirectoryJsonnetTlasList",
    "DataArgocdApplicationSpecSourcesDirectoryJsonnetTlasOutputReference",
    "DataArgocdApplicationSpecSourcesDirectoryOutputReference",
    "DataArgocdApplicationSpecSourcesHelm",
    "DataArgocdApplicationSpecSourcesHelmFileParameters",
    "DataArgocdApplicationSpecSourcesHelmFileParametersList",
    "DataArgocdApplicationSpecSourcesHelmFileParametersOutputReference",
    "DataArgocdApplicationSpecSourcesHelmOutputReference",
    "DataArgocdApplicationSpecSourcesHelmParameters",
    "DataArgocdApplicationSpecSourcesHelmParametersList",
    "DataArgocdApplicationSpecSourcesHelmParametersOutputReference",
    "DataArgocdApplicationSpecSourcesKustomize",
    "DataArgocdApplicationSpecSourcesKustomizeOutputReference",
    "DataArgocdApplicationSpecSourcesList",
    "DataArgocdApplicationSpecSourcesOutputReference",
    "DataArgocdApplicationSpecSourcesPlugin",
    "DataArgocdApplicationSpecSourcesPluginEnv",
    "DataArgocdApplicationSpecSourcesPluginEnvList",
    "DataArgocdApplicationSpecSourcesPluginEnvOutputReference",
    "DataArgocdApplicationSpecSourcesPluginOutputReference",
    "DataArgocdApplicationSpecSourcesPluginParameters",
    "DataArgocdApplicationSpecSourcesPluginParametersList",
    "DataArgocdApplicationSpecSourcesPluginParametersOutputReference",
    "DataArgocdApplicationSpecSyncPolicy",
    "DataArgocdApplicationSpecSyncPolicyAutomated",
    "DataArgocdApplicationSpecSyncPolicyAutomatedOutputReference",
    "DataArgocdApplicationSpecSyncPolicyOutputReference",
    "DataArgocdApplicationSpecSyncPolicyRetry",
    "DataArgocdApplicationSpecSyncPolicyRetryBackoff",
    "DataArgocdApplicationSpecSyncPolicyRetryBackoffOutputReference",
    "DataArgocdApplicationSpecSyncPolicyRetryOutputReference",
    "DataArgocdApplicationStatus",
    "DataArgocdApplicationStatusConditions",
    "DataArgocdApplicationStatusConditionsList",
    "DataArgocdApplicationStatusConditionsOutputReference",
    "DataArgocdApplicationStatusHealth",
    "DataArgocdApplicationStatusHealthOutputReference",
    "DataArgocdApplicationStatusOperationState",
    "DataArgocdApplicationStatusOperationStateOutputReference",
    "DataArgocdApplicationStatusOutputReference",
    "DataArgocdApplicationStatusResources",
    "DataArgocdApplicationStatusResourcesHealth",
    "DataArgocdApplicationStatusResourcesHealthOutputReference",
    "DataArgocdApplicationStatusResourcesList",
    "DataArgocdApplicationStatusResourcesOutputReference",
    "DataArgocdApplicationStatusSummary",
    "DataArgocdApplicationStatusSummaryOutputReference",
    "DataArgocdApplicationStatusSync",
    "DataArgocdApplicationStatusSyncOutputReference",
]

publication.publish()

def _typecheckingstub__da849c2c6b276983e97bec475e59b26dbd0f0d674064579bf325fd5fac97b54d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    metadata: typing.Union[DataArgocdApplicationMetadata, typing.Dict[builtins.str, typing.Any]],
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c144b90ddf6218190b622fd3166f3ee2bd352208703df251ab5ead6ccaca89aa(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    metadata: typing.Union[DataArgocdApplicationMetadata, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b9648322304ff60289eadea25472bb10532ad33912e9961dbf9a162e33a74a3(
    *,
    name: builtins.str,
    namespace: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e336e13820d322f98624e9ae323dc4730fb4ad17700a01fffdd81f508ed11ab(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd373ce4b3bf791ed78f97ef6e6ef51cb64e09770e40e7623833d9f1ca7f5b6a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13a8e169aacfd9a3be4f390224d99519c93d1334affbc416f1a8326651ad662d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd3beaa29f4a6a7de0c804fbbf80b237931cc1bda35ea89b09ca37bba12646f0(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataArgocdApplicationMetadata]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__edfeb2ea71abecb0b52c3bd94c480d88615acbfdb00f806b22687da9021e073d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c260fd3749cda32d3ed3bd2eaedfb1726459eedf5e46bbc640ee9a6d967bb919(
    value: typing.Optional[DataArgocdApplicationSpecDestination],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c70a4b17ba3a31f80ab45b46d85185aaca664e909819b76c78c20242b8f8fcaf(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e0408f837d1edf586afb0c04b67c6d3c47f74791cb82adb36ea353095c38a70(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63cd19d18bcc136b5406bf303d6e7964d91eba558b1eaa1ea3dea625fd75b12e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5688cebab771b24ffb80a59a83f48e3c03fa0fb00694d116707b76651ddde06a(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec4fc52d8e2d0cd207adcaa36c0269d5070d5935e593809ca46132ca77aeb2ff(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9649e0a1ee65a53c25f6bfe9d89141750dfd387fe2a808d19505d948ef9b16c1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec937194a19679263f83127f66f06b1bffe5dfbe58f456ea7223c03b1ca2bf20(
    value: typing.Optional[DataArgocdApplicationSpecIgnoreDifferences],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13251577fa2b4cefe9dd03f0ce1e5805df6efb1842867650d178faa1f5dd7292(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d6cb04d6797cabf52d1b1388b73f9675e21624d2f55025c4e2dd0a426998ac3(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eea48a36fa7a1981ab5993296c7f34e8f94878967c8e865545ec19a953dbe9e5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0699889ee9c46b2505150ab44804f3beeeabd2714994e58006873dba8ed720d(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4796c0cf2b119696081b60f10e437219bbf6d5f55d937367ab0a5341403961d3(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49d438ff81906f13731803f02764da8efc7900446809ab0d264464c6fa78c923(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1652296e474e7617d323a7334366da4ddeb013175e9b2b47d878457bccaea386(
    value: typing.Optional[DataArgocdApplicationSpecInfos],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c51e0deb546989a854d90e52203592180c400eff3d6feb0710287bfdfb12e17(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05b0b3599fd7a02a46f6b2b239819d84dc125361fdca2a0918d8fd83b0e47ed8(
    value: typing.Optional[DataArgocdApplicationSpec],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bdc0b535350f84c32888e9dae7088029cec99f0ace5f149cee3a343538b5a5c5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5bf037e915a4d69c77adff9172efb4cb013aec2453f2a84a0537cb66379a29b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c791d0ffd5d953e7f9244ed8b4643824903ca115bdf6502d23e11a6fc01bfe8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__873a89aa38c0050856d37f2eb67a8ebfe5277a25df8f04d00d160afc0f108c98(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b2fcbe2e1db54943119f090fe30b5272a5b60cef7a72a877e188415d2ee7776(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c28ed630d6ef1d4208c446bb896d72195fd56d3cf79b682f0f87cf1a7fd627b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53f8a6c8bbef2d592e12e02c36d7cab1706d0a6272c220ac816e8424c68fd2e7(
    value: typing.Optional[DataArgocdApplicationSpecSourcesDirectoryJsonnetExtVars],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c25900dcd184ce1f484b868281ebd3bf23c6e17591b5edaec253441f5dbc037c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51ddc90960f0dbda7694f5643520467cbd78f80d241244e7e77c88ddec056fb2(
    value: typing.Optional[DataArgocdApplicationSpecSourcesDirectoryJsonnet],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e00842e186de4c0f62342733589c55cb198a2564ad0ac1c08d28e2f7494b77a3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa5c40ddb1a9878813818c6f399a74021e784f58ec899acbf09ccda475ad3369(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c10ffdd37296dafdbef50b481b70fcf3731c1b239e074920b4ded852169c015d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5963612f868dd93c095dbe0e75e0a8d76e06631e28747ae4af665c58850e7ecf(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecd7bac057f8b91b135ed9c2ab94e000f36ac0165acf2a08638c59a309819259(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e97c858008ae8e752b1b38a70b85c28f935ed7d43ba1a091cc672881b623430(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c897e53013cefd0d43b3d4a3ad8619e311d905cdee6bf108caa31d589727f2b1(
    value: typing.Optional[DataArgocdApplicationSpecSourcesDirectoryJsonnetTlas],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b38d5c432957fb29bc66544c4c4cc6adb3b9b85c765cadff3e2be3f7f7dc0fa9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd334a0a0a964116837dd1989137c59d07709e5327b613e0ec6e38b8c4a067d4(
    value: typing.Optional[DataArgocdApplicationSpecSourcesDirectory],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d2e3b5805b9acd796aae35d19e1c0f9b6c4984e00af7394b42e665f83679466(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c375a80fe6f031d172c4a1b012d60159f7d4f591c0b17184f34aea0a6f48dc2(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88a002f89b8653414c27424f097afb55636841bf05bfe5a8747e72cedc411962(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd162b2d5bd8c60f6cc393cba4ad8dd172861113df3d9cdcd0d814c32d3c87b5(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d5b3aef52ec52dce12b14fb3ff15fc3bf04c661cb335756be786855efaf42ac(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c84c2d4d5368bf60d16468eec780a9405d9f711cea680b2652c5b909fd99cbe(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9647996d80fb7a77ec42d72387315f3aec004a537032fb3c64c38fe90db3b4f6(
    value: typing.Optional[DataArgocdApplicationSpecSourcesHelmFileParameters],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f499af335d8c5611d051c4d3a0053f0661f546c3df398d72770ad40a3b1a020b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b98c6becba2277e2744126afb0f72ce615609311db919f677ddb86cbe3551412(
    value: typing.Optional[DataArgocdApplicationSpecSourcesHelm],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2763acc6405bf714601ff3e5e21cfcf59da85d74141aa02d7eb637f5dd60fe88(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01f5a457549c7f9abdd1dedf0a7e9ff4a70e7b77ce1bbec3ec9f2af6282f992b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e54ebab58c7c9c690cdd60a52ca46fa94bb304c94c0802d4659b3c7212a505e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4add129435e85befc0ab5cfa7a9472ce800eee8ed3856e4acf34e27144ccceb4(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c150f2126fad87205c1ce8a908a3dba4d728eb63887265b6293a466c8c16cd0c(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb7035a0498ec3ab55d97896a56ed8e7fadbcacd3d5a51429ac9f241e4d2d138(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2aea9c59c1396a2ab3584202ed24cbb0c7b2ae0d10bd70d65f449aa12c31cb6a(
    value: typing.Optional[DataArgocdApplicationSpecSourcesHelmParameters],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f8d4b88a253ecdded80c87937616bbe4a1e2dd634fffd7d8df487de91894539(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__033e4e1a41eae9e323f5eb5da97441c627da20b8d110c7f97ae20205252a781f(
    value: typing.Optional[DataArgocdApplicationSpecSourcesKustomize],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e4bb5aebf8bf26574a99df68ca6e173d958910a71e6af231236f91b2bb8f5eb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e24131c903aea3e9c82a6776c589e9ad775451a8952c1f2c0c0e1070adb5f9f6(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__766ba84a7b31b96186c482b535725cc6ffc3249662869e0f473b07110d155957(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d54099aa0d8e1909344a4a0c70bfb5a98f50fffa2c3978a2d07fa2ee164921b(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ea73f819d90cc7926353d0ecdd9e686f840f18d7d2ab4ed88347b0b6e894a3f(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d1acdab45a105c76bf76e3f0f00f31ddeb1ccff217fbe6338a7a93d0a44fa0f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e6734a91c0a01e0e3bdc3e7cf40128db598f23ae17da30804e69d375913fcca(
    value: typing.Optional[DataArgocdApplicationSpecSources],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__764ee72bd9c40e229e072bd4d55efcb0160263014fca123ece15a87ce8b95924(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f5a0b28d0695894486ff83ea8855a6c9141811bf310384cd64a7ebe48970d8e(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aec2affbf5010ee5796922b711ac09d91bd3a831b659cea5f4a6e9a0b92067b6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a7649813575f87df44134c949a736d8516158732cdfa7b6726c1f8e96642b39(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bbec39ca7cdd6d594d97c4cfe86b3f20075a599ca0bce8835ec4c8dd59cf709(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d222476e5236d9eb0502cf17a3d31e81dd1239fbe340286b641bd830d5d135d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bb813ae4b04af8e3abbc1d653fd78da1dc6d3e4745d7fd9c338064b8ad7cdf1(
    value: typing.Optional[DataArgocdApplicationSpecSourcesPluginEnv],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd653fdc6aebad68008365e96f7a0d2e1e87af33b95103b4c78f136bbc5150bc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d18fb1c3d3db91aafdd38900e5ebb147e76ec018f5384ff7204f8525715c6477(
    value: typing.Optional[DataArgocdApplicationSpecSourcesPlugin],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdad7e86bd1d8c14268b1a6fa313a8992e0129592cc4c2ebf40cdb4ee18cfdb7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c3e2bfdf9ae291a37fa4c4d2a182a9dcd39828d4bd4105f6aa18571e0eded80(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f312edf6d3eab87c5eb2f070176360dcd633895d8ee348d53ed647a2d35379b6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__639b47616ec7c26f4aac4dc5411a7389c80863b555ee54fb67a35c18a647009b(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad73b22d25720467dbb152835e6deb1b0bad32b663553bdd85955d172d897023(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c08f1fffaafae3e564eb1891ec05fb80cae877fc0e849e8ed0472165f8ce895d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df125d31de3d061fc1b2ff72d9c6069e248b34388c200438573d716c4d1f09e9(
    value: typing.Optional[DataArgocdApplicationSpecSourcesPluginParameters],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5f7fbbcb0ccc5ab1bd80e11d4d4af7ce11422d7141f6b47a0d2ddcd6f8ffe6e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1df3d0b5e7ede38b330737190f5656118c6b21b1f3107ee0cb44987eddab13b(
    value: typing.Optional[DataArgocdApplicationSpecSyncPolicyAutomated],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2a7f133d80b9e9ab2cde5730b5193e90b64933a22aa5ad4712d01b7664270fb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b51cdc650400feedc8325a3d97bb7bec6c9e16de3b5f18a46b906a60c7beabc5(
    value: typing.Optional[DataArgocdApplicationSpecSyncPolicy],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4327f06bdd27faa68b3259e1e05689266c22cc893b43bdedaf3fb488cae3b48d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa5c1020d30ba5575af7cd622836ada71c99dd9a895628dfc97bb98149cf92dc(
    value: typing.Optional[DataArgocdApplicationSpecSyncPolicyRetryBackoff],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9ad2e8aa10c4c7adc59ba2e5f94c509316eb08d85ad093df8562aec3b089c89(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94f54d82f3718e3d8ea806f434504cbec608211ec983c91a20013a375ff83be9(
    value: typing.Optional[DataArgocdApplicationSpecSyncPolicyRetry],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e327a866960515c76b6f7a26520618084ea56464a4786a98d7d07b8874c6d3b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ae8eb9c9f1360732fead94c40eb7a0166991ef815565cdfea6e01fac1a7e24b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9be49da50766d90a90a80183d1d7d537bb7ba1ed13992a9a881be16d3e83264(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__382a2e677dcb54fc989e86e6865198b931851b3dcd4080561302a062e3d1f0ec(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78512262cb756ca2e1f81bc5064b73aa53e313383b3e5a25e097618a9e532fcc(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c44824ebd74b0d41bd369e41fc8cebadb2a9095b5f4355413c51bcb2bd6968b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f72bee223f96dd86716c0da06f6ea4539dd4e575cad9a02438438d4454ae673(
    value: typing.Optional[DataArgocdApplicationStatusConditions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a70642459330848df48f1733af2ab15bf8ed560701889071c16f7f637ea4e98(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__963e46b71cd89eda559bda31effd9dd2adef057cead56d6863e3c4decf88d535(
    value: typing.Optional[DataArgocdApplicationStatusHealth],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f383318b9c648a1582e6d302a825fd33bce10e04abb76c151d8ffab2e02bc211(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c31ef5edc7aea6b522ba83efba7c2c4fa37ab11f75901ccf10c04ea1bda31615(
    value: typing.Optional[DataArgocdApplicationStatusOperationState],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11517ff603e5a51f0e16126c28bf8b67c784fdc60f91a69072dd05c197c62320(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b81f01f85f774d977b2091f13ec6773b6597b677251ed194bd234b8b340ad75(
    value: typing.Optional[DataArgocdApplicationStatus],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96c8070621b47e3ff7661e31e73651421708529b60d7a0b5cf28c634b84c8dba(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1812c0899dc731d7c6e958ecda88b0ca2e9c3f8fd5880d9dc6f14b6ee5797a9(
    value: typing.Optional[DataArgocdApplicationStatusResourcesHealth],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97a098415cf050109d69fdf9251cf92e0a3945b4007e0b98900e5704f0f7c5e6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15ff382853dc4515e8135306d2dc6fd463d0272a4728a3298a899070806921fe(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfebc843cac9d1d44aca1dd18238e681a852d86f5d081ec02aca362cdab707d6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb1c2983a88b0e13b3a7e084d024237bae827f8b20b1cd59ae87c321bbd38d3f(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44c082dd57d4aa7bf60b3055bcd5da00d5dcaf7ec008eecaafb177a272718e2e(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb1639959707d964308d941109e74dc66fe84e43093b7902ee0be3ca251e9959(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9285bca1d9df517eb7530cbe7a0934d50f6dbaadfbc443335bf0d69953a3330(
    value: typing.Optional[DataArgocdApplicationStatusResources],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ce6d0d6606e451f8129933ac618b1f432a4add59ec92ffccbaf512372b6341b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85919e7233c6f07ea3535485fec71c07ab172e0f0c08ce1f805f51bd7474f81c(
    value: typing.Optional[DataArgocdApplicationStatusSummary],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__373e19753f2ebae5d4ba9ed82bff9be4939c4bc143a49f27f99051f52ab5d5ce(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__307a82a7147d4ecd8be89e345f58add124c92d698bba288a3f9895d1f17dab9a(
    value: typing.Optional[DataArgocdApplicationStatusSync],
) -> None:
    """Type checking stubs"""
    pass
