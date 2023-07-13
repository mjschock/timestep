'''
# `data_kubernetes_persistent_volume_v1`

Refer to the Terraform Registory for docs: [`data_kubernetes_persistent_volume_v1`](https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1).
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


class DataKubernetesPersistentVolumeV1(
    _cdktf_9a9027ec.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1",
):
    '''Represents a {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1 kubernetes_persistent_volume_v1}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        metadata: typing.Union["DataKubernetesPersistentVolumeV1Metadata", typing.Dict[builtins.str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        spec: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataKubernetesPersistentVolumeV1Spec", typing.Dict[builtins.str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1 kubernetes_persistent_volume_v1} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#metadata DataKubernetesPersistentVolumeV1#metadata}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#id DataKubernetesPersistentVolumeV1#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param spec: spec block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#spec DataKubernetesPersistentVolumeV1#spec}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a36d09ce346420033ae9deb890db42338e8cd3fdfb77f97ee8d34f7df8e55adb)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataKubernetesPersistentVolumeV1Config(
            metadata=metadata,
            id=id,
            spec=spec,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putMetadata")
    def put_metadata(
        self,
        *,
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param annotations: An unstructured key value map stored with the persistent volume that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#annotations DataKubernetesPersistentVolumeV1#annotations}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the persistent volume. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#labels DataKubernetesPersistentVolumeV1#labels}
        :param name: Name of the persistent volume, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#name DataKubernetesPersistentVolumeV1#name}
        '''
        value = DataKubernetesPersistentVolumeV1Metadata(
            annotations=annotations, labels=labels, name=name
        )

        return typing.cast(None, jsii.invoke(self, "putMetadata", [value]))

    @jsii.member(jsii_name="putSpec")
    def put_spec(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataKubernetesPersistentVolumeV1Spec", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe8b958ab25ba340e360c55811ab17a68e0a13f77110440dcd12016ab03cf35d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSpec", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetSpec")
    def reset_spec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSpec", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> "DataKubernetesPersistentVolumeV1MetadataOutputReference":
        return typing.cast("DataKubernetesPersistentVolumeV1MetadataOutputReference", jsii.get(self, "metadata"))

    @builtins.property
    @jsii.member(jsii_name="spec")
    def spec(self) -> "DataKubernetesPersistentVolumeV1SpecList":
        return typing.cast("DataKubernetesPersistentVolumeV1SpecList", jsii.get(self, "spec"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataInput")
    def metadata_input(
        self,
    ) -> typing.Optional["DataKubernetesPersistentVolumeV1Metadata"]:
        return typing.cast(typing.Optional["DataKubernetesPersistentVolumeV1Metadata"], jsii.get(self, "metadataInput"))

    @builtins.property
    @jsii.member(jsii_name="specInput")
    def spec_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataKubernetesPersistentVolumeV1Spec"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataKubernetesPersistentVolumeV1Spec"]]], jsii.get(self, "specInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a005e69c6b3ce2245190f84fcea4b151f069cd2b7193a19475735b62fd9e5af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1Config",
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
        "id": "id",
        "spec": "spec",
    },
)
class DataKubernetesPersistentVolumeV1Config(_cdktf_9a9027ec.TerraformMetaArguments):
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
        metadata: typing.Union["DataKubernetesPersistentVolumeV1Metadata", typing.Dict[builtins.str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        spec: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataKubernetesPersistentVolumeV1Spec", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#metadata DataKubernetesPersistentVolumeV1#metadata}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#id DataKubernetesPersistentVolumeV1#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param spec: spec block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#spec DataKubernetesPersistentVolumeV1#spec}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(metadata, dict):
            metadata = DataKubernetesPersistentVolumeV1Metadata(**metadata)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05fe15da96f9541a8d08f3af321d7affa73cf8250962949c04ce852a8e679674)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument spec", value=spec, expected_type=type_hints["spec"])
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
        if id is not None:
            self._values["id"] = id
        if spec is not None:
            self._values["spec"] = spec

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
    def metadata(self) -> "DataKubernetesPersistentVolumeV1Metadata":
        '''metadata block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#metadata DataKubernetesPersistentVolumeV1#metadata}
        '''
        result = self._values.get("metadata")
        assert result is not None, "Required property 'metadata' is missing"
        return typing.cast("DataKubernetesPersistentVolumeV1Metadata", result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#id DataKubernetesPersistentVolumeV1#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def spec(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataKubernetesPersistentVolumeV1Spec"]]]:
        '''spec block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#spec DataKubernetesPersistentVolumeV1#spec}
        '''
        result = self._values.get("spec")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataKubernetesPersistentVolumeV1Spec"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataKubernetesPersistentVolumeV1Config(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1Metadata",
    jsii_struct_bases=[],
    name_mapping={"annotations": "annotations", "labels": "labels", "name": "name"},
)
class DataKubernetesPersistentVolumeV1Metadata:
    def __init__(
        self,
        *,
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param annotations: An unstructured key value map stored with the persistent volume that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#annotations DataKubernetesPersistentVolumeV1#annotations}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the persistent volume. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#labels DataKubernetesPersistentVolumeV1#labels}
        :param name: Name of the persistent volume, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#name DataKubernetesPersistentVolumeV1#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__217167e19339c8a03bab5a82157f2f943cf9acf577295a422d5969dd5aae7197)
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if annotations is not None:
            self._values["annotations"] = annotations
        if labels is not None:
            self._values["labels"] = labels
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def annotations(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''An unstructured key value map stored with the persistent volume that may be used to store arbitrary metadata.

        More info: http://kubernetes.io/docs/user-guide/annotations

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#annotations DataKubernetesPersistentVolumeV1#annotations}
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Map of string keys and values that can be used to organize and categorize (scope and select) the persistent volume.

        May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#labels DataKubernetesPersistentVolumeV1#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the persistent volume, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#name DataKubernetesPersistentVolumeV1#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataKubernetesPersistentVolumeV1Metadata(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataKubernetesPersistentVolumeV1MetadataOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1MetadataOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8de94df421b903310c1b923b19e43c6110c7a91923b370a74c8549af417ec0a1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAnnotations")
    def reset_annotations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnnotations", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="generation")
    def generation(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "generation"))

    @builtins.property
    @jsii.member(jsii_name="resourceVersion")
    def resource_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceVersion"))

    @builtins.property
    @jsii.member(jsii_name="uid")
    def uid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uid"))

    @builtins.property
    @jsii.member(jsii_name="annotationsInput")
    def annotations_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "annotationsInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="annotations")
    def annotations(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "annotations"))

    @annotations.setter
    def annotations(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d12c5093b23351f47b24890591a6db73828abb783aa2bcf968bba9b1e315a1f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "annotations", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cdf00026c6deb97c4aaaa9536454cb9676dfd3f7ccb21d47a7781c14dfebbc45)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30d332e580c281d56888ebf6eebd7798126870e100e0963099dda9b87fe7d73f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataKubernetesPersistentVolumeV1Metadata]:
        return typing.cast(typing.Optional[DataKubernetesPersistentVolumeV1Metadata], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataKubernetesPersistentVolumeV1Metadata],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c89cf5f499a85901caa03b7e191b31889d58a66126c5fdb28be850563c84a04c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1Spec",
    jsii_struct_bases=[],
    name_mapping={
        "access_modes": "accessModes",
        "capacity": "capacity",
        "persistent_volume_source": "persistentVolumeSource",
        "claim_ref": "claimRef",
        "mount_options": "mountOptions",
        "node_affinity": "nodeAffinity",
        "persistent_volume_reclaim_policy": "persistentVolumeReclaimPolicy",
        "storage_class_name": "storageClassName",
        "volume_mode": "volumeMode",
    },
)
class DataKubernetesPersistentVolumeV1Spec:
    def __init__(
        self,
        *,
        access_modes: typing.Sequence[builtins.str],
        capacity: typing.Mapping[builtins.str, builtins.str],
        persistent_volume_source: typing.Union["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSource", typing.Dict[builtins.str, typing.Any]],
        claim_ref: typing.Optional[typing.Union["DataKubernetesPersistentVolumeV1SpecClaimRef", typing.Dict[builtins.str, typing.Any]]] = None,
        mount_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        node_affinity: typing.Optional[typing.Union["DataKubernetesPersistentVolumeV1SpecNodeAffinity", typing.Dict[builtins.str, typing.Any]]] = None,
        persistent_volume_reclaim_policy: typing.Optional[builtins.str] = None,
        storage_class_name: typing.Optional[builtins.str] = None,
        volume_mode: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param access_modes: Contains all ways the volume can be mounted. More info: http://kubernetes.io/docs/user-guide/persistent-volumes#access-modes. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#access_modes DataKubernetesPersistentVolumeV1#access_modes}
        :param capacity: A description of the persistent volume's resources and capacity. More info: http://kubernetes.io/docs/user-guide/persistent-volumes#capacity. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#capacity DataKubernetesPersistentVolumeV1#capacity}
        :param persistent_volume_source: persistent_volume_source block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#persistent_volume_source DataKubernetesPersistentVolumeV1#persistent_volume_source}
        :param claim_ref: claim_ref block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#claim_ref DataKubernetesPersistentVolumeV1#claim_ref}
        :param mount_options: A list of mount options, e.g. ["ro", "soft"]. Not validated - mount will simply fail if one is invalid. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#mount_options DataKubernetesPersistentVolumeV1#mount_options}
        :param node_affinity: node_affinity block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#node_affinity DataKubernetesPersistentVolumeV1#node_affinity}
        :param persistent_volume_reclaim_policy: What happens to a persistent volume when released from its claim. Valid options are Retain (default) and Recycle. Recycling must be supported by the volume plugin underlying this persistent volume. More info: http://kubernetes.io/docs/user-guide/persistent-volumes#recycling-policy Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#persistent_volume_reclaim_policy DataKubernetesPersistentVolumeV1#persistent_volume_reclaim_policy}
        :param storage_class_name: A description of the persistent volume's class. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes/#class. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#storage_class_name DataKubernetesPersistentVolumeV1#storage_class_name}
        :param volume_mode: Defines if a volume is intended to be used with a formatted filesystem. or to remain in raw block state. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#volume_mode DataKubernetesPersistentVolumeV1#volume_mode}
        '''
        if isinstance(persistent_volume_source, dict):
            persistent_volume_source = DataKubernetesPersistentVolumeV1SpecPersistentVolumeSource(**persistent_volume_source)
        if isinstance(claim_ref, dict):
            claim_ref = DataKubernetesPersistentVolumeV1SpecClaimRef(**claim_ref)
        if isinstance(node_affinity, dict):
            node_affinity = DataKubernetesPersistentVolumeV1SpecNodeAffinity(**node_affinity)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3d29fddb4061926d6ce6652ceba01c9079def1e16e5b815f5d775895197c9b4)
            check_type(argname="argument access_modes", value=access_modes, expected_type=type_hints["access_modes"])
            check_type(argname="argument capacity", value=capacity, expected_type=type_hints["capacity"])
            check_type(argname="argument persistent_volume_source", value=persistent_volume_source, expected_type=type_hints["persistent_volume_source"])
            check_type(argname="argument claim_ref", value=claim_ref, expected_type=type_hints["claim_ref"])
            check_type(argname="argument mount_options", value=mount_options, expected_type=type_hints["mount_options"])
            check_type(argname="argument node_affinity", value=node_affinity, expected_type=type_hints["node_affinity"])
            check_type(argname="argument persistent_volume_reclaim_policy", value=persistent_volume_reclaim_policy, expected_type=type_hints["persistent_volume_reclaim_policy"])
            check_type(argname="argument storage_class_name", value=storage_class_name, expected_type=type_hints["storage_class_name"])
            check_type(argname="argument volume_mode", value=volume_mode, expected_type=type_hints["volume_mode"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "access_modes": access_modes,
            "capacity": capacity,
            "persistent_volume_source": persistent_volume_source,
        }
        if claim_ref is not None:
            self._values["claim_ref"] = claim_ref
        if mount_options is not None:
            self._values["mount_options"] = mount_options
        if node_affinity is not None:
            self._values["node_affinity"] = node_affinity
        if persistent_volume_reclaim_policy is not None:
            self._values["persistent_volume_reclaim_policy"] = persistent_volume_reclaim_policy
        if storage_class_name is not None:
            self._values["storage_class_name"] = storage_class_name
        if volume_mode is not None:
            self._values["volume_mode"] = volume_mode

    @builtins.property
    def access_modes(self) -> typing.List[builtins.str]:
        '''Contains all ways the volume can be mounted. More info: http://kubernetes.io/docs/user-guide/persistent-volumes#access-modes.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#access_modes DataKubernetesPersistentVolumeV1#access_modes}
        '''
        result = self._values.get("access_modes")
        assert result is not None, "Required property 'access_modes' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def capacity(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''A description of the persistent volume's resources and capacity. More info: http://kubernetes.io/docs/user-guide/persistent-volumes#capacity.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#capacity DataKubernetesPersistentVolumeV1#capacity}
        '''
        result = self._values.get("capacity")
        assert result is not None, "Required property 'capacity' is missing"
        return typing.cast(typing.Mapping[builtins.str, builtins.str], result)

    @builtins.property
    def persistent_volume_source(
        self,
    ) -> "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSource":
        '''persistent_volume_source block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#persistent_volume_source DataKubernetesPersistentVolumeV1#persistent_volume_source}
        '''
        result = self._values.get("persistent_volume_source")
        assert result is not None, "Required property 'persistent_volume_source' is missing"
        return typing.cast("DataKubernetesPersistentVolumeV1SpecPersistentVolumeSource", result)

    @builtins.property
    def claim_ref(
        self,
    ) -> typing.Optional["DataKubernetesPersistentVolumeV1SpecClaimRef"]:
        '''claim_ref block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#claim_ref DataKubernetesPersistentVolumeV1#claim_ref}
        '''
        result = self._values.get("claim_ref")
        return typing.cast(typing.Optional["DataKubernetesPersistentVolumeV1SpecClaimRef"], result)

    @builtins.property
    def mount_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of mount options, e.g. ["ro", "soft"]. Not validated - mount will simply fail if one is invalid.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#mount_options DataKubernetesPersistentVolumeV1#mount_options}
        '''
        result = self._values.get("mount_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def node_affinity(
        self,
    ) -> typing.Optional["DataKubernetesPersistentVolumeV1SpecNodeAffinity"]:
        '''node_affinity block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#node_affinity DataKubernetesPersistentVolumeV1#node_affinity}
        '''
        result = self._values.get("node_affinity")
        return typing.cast(typing.Optional["DataKubernetesPersistentVolumeV1SpecNodeAffinity"], result)

    @builtins.property
    def persistent_volume_reclaim_policy(self) -> typing.Optional[builtins.str]:
        '''What happens to a persistent volume when released from its claim.

        Valid options are Retain (default) and Recycle. Recycling must be supported by the volume plugin underlying this persistent volume. More info: http://kubernetes.io/docs/user-guide/persistent-volumes#recycling-policy

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#persistent_volume_reclaim_policy DataKubernetesPersistentVolumeV1#persistent_volume_reclaim_policy}
        '''
        result = self._values.get("persistent_volume_reclaim_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_class_name(self) -> typing.Optional[builtins.str]:
        '''A description of the persistent volume's class. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes/#class.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#storage_class_name DataKubernetesPersistentVolumeV1#storage_class_name}
        '''
        result = self._values.get("storage_class_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def volume_mode(self) -> typing.Optional[builtins.str]:
        '''Defines if a volume is intended to be used with a formatted filesystem.

        or to remain in raw block state.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#volume_mode DataKubernetesPersistentVolumeV1#volume_mode}
        '''
        result = self._values.get("volume_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataKubernetesPersistentVolumeV1Spec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecClaimRef",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "namespace": "namespace"},
)
class DataKubernetesPersistentVolumeV1SpecClaimRef:
    def __init__(
        self,
        *,
        name: builtins.str,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: The name of the PersistentVolumeClaim. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#name DataKubernetesPersistentVolumeV1#name}
        :param namespace: The namespace of the PersistentVolumeClaim. Uses 'default' namespace if none is specified. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#namespace DataKubernetesPersistentVolumeV1#namespace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__027983f95dc76c9510fe3e31a5b722d1cd0086682fa9a206f98cf377f4e92030)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if namespace is not None:
            self._values["namespace"] = namespace

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the PersistentVolumeClaim.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#name DataKubernetesPersistentVolumeV1#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''The namespace of the PersistentVolumeClaim. Uses 'default' namespace if none is specified.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#namespace DataKubernetesPersistentVolumeV1#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataKubernetesPersistentVolumeV1SpecClaimRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataKubernetesPersistentVolumeV1SpecClaimRefOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecClaimRefOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__91e7c36065f2342ea56f0dbff7a3a3f30b879a41a2ccfd83dd21e35d1465a620)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

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
            type_hints = typing.get_type_hints(_typecheckingstub__d70eafb5b634510081e933f70aa62457d10064b590b77af379cf2b8a0c3630fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10c958bae7ff95ba26b7e7e6d70328be20b6c04008a411d91b915fc932038ff6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataKubernetesPersistentVolumeV1SpecClaimRef]:
        return typing.cast(typing.Optional[DataKubernetesPersistentVolumeV1SpecClaimRef], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataKubernetesPersistentVolumeV1SpecClaimRef],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94650a6b062c678e5c975ab7d8415a3d06737fabc51913c3a20532db632b2b3e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataKubernetesPersistentVolumeV1SpecList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e271a8a3b265b2902114f6aef1f2fa9c863006f84ba7a32fd8edc9526f24b753)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataKubernetesPersistentVolumeV1SpecOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbfdec2eb8ed460945570dff9c8ee3d259d740e262ff6bfd4a05f188507213e3)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataKubernetesPersistentVolumeV1SpecOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd85b3fa65ba0dd05076c19d141ff20e0a5ea05376abbbbfe064ea2e11e369a4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__cd611b1cbae3c77190d4f590e3f98ecb637d735c12d0f84fdf98d0a3566c6518)
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
            type_hints = typing.get_type_hints(_typecheckingstub__93261a71bc8d48a2b8e03e4ed3387038c38006343ec04771dd7de718c572a5e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataKubernetesPersistentVolumeV1Spec]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataKubernetesPersistentVolumeV1Spec]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataKubernetesPersistentVolumeV1Spec]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb779ea692e2d39c3537cb52a9c1060b45ae3c0a77c099411b9428c3cf2da684)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecNodeAffinity",
    jsii_struct_bases=[],
    name_mapping={"required": "required"},
)
class DataKubernetesPersistentVolumeV1SpecNodeAffinity:
    def __init__(
        self,
        *,
        required: typing.Optional[typing.Union["DataKubernetesPersistentVolumeV1SpecNodeAffinityRequired", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param required: required block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#required DataKubernetesPersistentVolumeV1#required}
        '''
        if isinstance(required, dict):
            required = DataKubernetesPersistentVolumeV1SpecNodeAffinityRequired(**required)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__583b6906e6d7d4a3d02715c43c77caad8fe10aa1b3573a1fb137b7df3b784adb)
            check_type(argname="argument required", value=required, expected_type=type_hints["required"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if required is not None:
            self._values["required"] = required

    @builtins.property
    def required(
        self,
    ) -> typing.Optional["DataKubernetesPersistentVolumeV1SpecNodeAffinityRequired"]:
        '''required block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#required DataKubernetesPersistentVolumeV1#required}
        '''
        result = self._values.get("required")
        return typing.cast(typing.Optional["DataKubernetesPersistentVolumeV1SpecNodeAffinityRequired"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataKubernetesPersistentVolumeV1SpecNodeAffinity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataKubernetesPersistentVolumeV1SpecNodeAffinityOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecNodeAffinityOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0fdc59341c09dc4bef49883a0dd6f9251a11f6cbea87992049912b3b3d5f659d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRequired")
    def put_required(
        self,
        *,
        node_selector_term: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTerm", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param node_selector_term: node_selector_term block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#node_selector_term DataKubernetesPersistentVolumeV1#node_selector_term}
        '''
        value = DataKubernetesPersistentVolumeV1SpecNodeAffinityRequired(
            node_selector_term=node_selector_term
        )

        return typing.cast(None, jsii.invoke(self, "putRequired", [value]))

    @jsii.member(jsii_name="resetRequired")
    def reset_required(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequired", []))

    @builtins.property
    @jsii.member(jsii_name="required")
    def required(
        self,
    ) -> "DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredOutputReference":
        return typing.cast("DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredOutputReference", jsii.get(self, "required"))

    @builtins.property
    @jsii.member(jsii_name="requiredInput")
    def required_input(
        self,
    ) -> typing.Optional["DataKubernetesPersistentVolumeV1SpecNodeAffinityRequired"]:
        return typing.cast(typing.Optional["DataKubernetesPersistentVolumeV1SpecNodeAffinityRequired"], jsii.get(self, "requiredInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataKubernetesPersistentVolumeV1SpecNodeAffinity]:
        return typing.cast(typing.Optional[DataKubernetesPersistentVolumeV1SpecNodeAffinity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataKubernetesPersistentVolumeV1SpecNodeAffinity],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84bbfe16ccaf2026eaab95e885983e4bdd2901ff65f4c757bd58998a02247a03)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecNodeAffinityRequired",
    jsii_struct_bases=[],
    name_mapping={"node_selector_term": "nodeSelectorTerm"},
)
class DataKubernetesPersistentVolumeV1SpecNodeAffinityRequired:
    def __init__(
        self,
        *,
        node_selector_term: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTerm", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param node_selector_term: node_selector_term block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#node_selector_term DataKubernetesPersistentVolumeV1#node_selector_term}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf27749cc8de2c7062b320655d859b37766069c10e5fb0325a3b60c223851904)
            check_type(argname="argument node_selector_term", value=node_selector_term, expected_type=type_hints["node_selector_term"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "node_selector_term": node_selector_term,
        }

    @builtins.property
    def node_selector_term(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTerm"]]:
        '''node_selector_term block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#node_selector_term DataKubernetesPersistentVolumeV1#node_selector_term}
        '''
        result = self._values.get("node_selector_term")
        assert result is not None, "Required property 'node_selector_term' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTerm"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataKubernetesPersistentVolumeV1SpecNodeAffinityRequired(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTerm",
    jsii_struct_bases=[],
    name_mapping={
        "match_expressions": "matchExpressions",
        "match_fields": "matchFields",
    },
)
class DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTerm:
    def __init__(
        self,
        *,
        match_expressions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        match_fields: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFields", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param match_expressions: match_expressions block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#match_expressions DataKubernetesPersistentVolumeV1#match_expressions}
        :param match_fields: match_fields block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#match_fields DataKubernetesPersistentVolumeV1#match_fields}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34c95e657646ee840f1e8ed2e9ab458aeebfe5d37234eb97982b7cb7e03602df)
            check_type(argname="argument match_expressions", value=match_expressions, expected_type=type_hints["match_expressions"])
            check_type(argname="argument match_fields", value=match_fields, expected_type=type_hints["match_fields"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if match_expressions is not None:
            self._values["match_expressions"] = match_expressions
        if match_fields is not None:
            self._values["match_fields"] = match_fields

    @builtins.property
    def match_expressions(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressions"]]]:
        '''match_expressions block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#match_expressions DataKubernetesPersistentVolumeV1#match_expressions}
        '''
        result = self._values.get("match_expressions")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressions"]]], result)

    @builtins.property
    def match_fields(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFields"]]]:
        '''match_fields block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#match_fields DataKubernetesPersistentVolumeV1#match_fields}
        '''
        result = self._values.get("match_fields")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFields"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTerm(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c061554b8565473c3d47e02e93a580f42e57efc6e59058478562e4de120a84a9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d2f37fe5e1308c8ce58c06afe61512d219a755d933f26b88185f7752f635138)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28d8e173ed0fff36eb418a048a4a7124f4ec1e3c4299970f7574ad9d28ab3839)
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
            type_hints = typing.get_type_hints(_typecheckingstub__193b120a127bd93617fc9556762e0b1bfbb3ec3240d1d562331ab2fd8b2dfcb9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__182a1225d02192cc7d26b565798bfb03548483bd0c2ecf063b73ea1a9e355849)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTerm]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTerm]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTerm]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d86a895493c1f7859ea0b3e2f1729102ffe086cd2912ce9cd4b1cb23f2024edd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressions",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "operator": "operator", "values": "values"},
)
class DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressions:
    def __init__(
        self,
        *,
        key: builtins.str,
        operator: builtins.str,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: The label key that the selector applies to. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#key DataKubernetesPersistentVolumeV1#key}
        :param operator: A key's relationship to a set of values. Valid operators ard ``In``, ``NotIn``, ``Exists``, ``DoesNotExist``, ``Gt``, and ``Lt``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#operator DataKubernetesPersistentVolumeV1#operator}
        :param values: An array of string values. If the operator is ``In`` or ``NotIn``, the values array must be non-empty. If the operator is ``Exists`` or ``DoesNotExist``, the values array must be empty. This array is replaced during a strategic merge patch. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#values DataKubernetesPersistentVolumeV1#values}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__374e78f34d6c6f928bdce612757ab586b766f6f33422bef388ad1ff2cb3aa5f8)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "operator": operator,
        }
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> builtins.str:
        '''The label key that the selector applies to.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#key DataKubernetesPersistentVolumeV1#key}
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''A key's relationship to a set of values. Valid operators ard ``In``, ``NotIn``, ``Exists``, ``DoesNotExist``, ``Gt``, and ``Lt``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#operator DataKubernetesPersistentVolumeV1#operator}
        '''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of string values.

        If the operator is ``In`` or ``NotIn``, the values array must be non-empty. If the operator is ``Exists`` or ``DoesNotExist``, the values array must be empty. This array is replaced during a strategic merge patch.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#values DataKubernetesPersistentVolumeV1#values}
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressionsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c66801121a2cf4884f57fa3554f3dd44e4ec6e25b1e5ed444df89b6f4cbcbaae)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9787c6a11314e6c0bb573ee0c9437ad22113a96f93ac32f55f16c896df2e79ca)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa312b9f423a40d58a41ba08444fff19556d56ffae013bc0256a605d9006ea29)
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
            type_hints = typing.get_type_hints(_typecheckingstub__218e90cb21541c7d67e015aaec6032d4e80bda61fa2ddb0dec4d2cd5403bd09e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ca6752a1fbad6c2202ffcb03fbf5c5243c1f8c3d86d14375d479ed85e28de5f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b51a08503bfd4ec260538d5ffb5fd18d6a6fb8c5d75dbc23ec39e2c4f9a9d41)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3ee52fc2dc060742142ef4ac96ac220ba279f791162b3f30a1e67f92e279fdde)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__daa1131014585873eb6b44dd338ca98fc2968da4dfbe883ce94f4f74c0c35074)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b743aec58d4631c925b06bb56f6661c5568181514b7000ff87fcc0a37e304903)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ac56be3fab2c4c8808311d70a7484fbffb5c5abd47d371532456dbae833e104)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressions]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressions]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressions]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd3b8cf2aa4a50da9bcda8bac4e2c09a2bc6fd2fbbc51c80b2f43951f94980fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFields",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "operator": "operator", "values": "values"},
)
class DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFields:
    def __init__(
        self,
        *,
        key: builtins.str,
        operator: builtins.str,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: The label key that the selector applies to. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#key DataKubernetesPersistentVolumeV1#key}
        :param operator: A key's relationship to a set of values. Valid operators ard ``In``, ``NotIn``, ``Exists``, ``DoesNotExist``, ``Gt``, and ``Lt``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#operator DataKubernetesPersistentVolumeV1#operator}
        :param values: An array of string values. If the operator is ``In`` or ``NotIn``, the values array must be non-empty. If the operator is ``Exists`` or ``DoesNotExist``, the values array must be empty. This array is replaced during a strategic merge patch. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#values DataKubernetesPersistentVolumeV1#values}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04145c6e7d60b514f6a429abdcede7ba651a943b2032adf07d795cebbafd6172)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "operator": operator,
        }
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> builtins.str:
        '''The label key that the selector applies to.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#key DataKubernetesPersistentVolumeV1#key}
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''A key's relationship to a set of values. Valid operators ard ``In``, ``NotIn``, ``Exists``, ``DoesNotExist``, ``Gt``, and ``Lt``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#operator DataKubernetesPersistentVolumeV1#operator}
        '''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of string values.

        If the operator is ``In`` or ``NotIn``, the values array must be non-empty. If the operator is ``Exists`` or ``DoesNotExist``, the values array must be empty. This array is replaced during a strategic merge patch.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#values DataKubernetesPersistentVolumeV1#values}
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFields(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFieldsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFieldsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a36d9fec6c370e1511be7ccb88d5446c175e65bebc19105c2e0770b88d16dda1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFieldsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd02ed3f0c4385fa060e2684610d1dd3aeddee76e8b49aa082231907eefa9c59)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFieldsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0d1a9bd299e1de5ec566d16b9522ceff79df3155644c59a99c3996d753ec910)
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
            type_hints = typing.get_type_hints(_typecheckingstub__42e6afdcb3d08ce245d1ff0d18fedcbbb942d2f7bbc108eae0ff7e867810cf28)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b0e0a9c9e2cf05cc606e2b9d30cff50327d2b1f0dfc6c989c127943b868d7675)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFields]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFields]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFields]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09e94b9c1725734b75b288a4d4139c709b11eb3c680dc45f8cde04771a5ed85f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFieldsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFieldsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ca95ab35e4798f1212688b58ab72dd1314afb9a6eac735335ca5b7a5c188c644)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d02d9fad8803560d1571a906d3b18bab30d767e7111a9dcbd50aba6c508dbe5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b79f86a70dd0ab2233ab08a4436a226d0a19ada0164cf09c3268e6dda56b27ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__974ad5dc27f718f31f61137a7afae518c8f7a3e0ea9775c984422d2faa3fd033)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFields]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFields]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFields]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a89812919a9dce35e22d2a67af2949b5175b39076581d589245dd8ab2682146)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__534a4a19024f06f137c43f6dc3c1bc7511066baf8a43f3ddb8dbb2bbdb313394)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putMatchExpressions")
    def put_match_expressions(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressions, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44da079d93802d45fe935b6e4b9a7add45264ec6c7ba047078229d55cf134a78)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMatchExpressions", [value]))

    @jsii.member(jsii_name="putMatchFields")
    def put_match_fields(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFields, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d03bd88817b161a45d783bfc20fb108712a5eea4494fec53ae81ef4f9dea26d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMatchFields", [value]))

    @jsii.member(jsii_name="resetMatchExpressions")
    def reset_match_expressions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchExpressions", []))

    @jsii.member(jsii_name="resetMatchFields")
    def reset_match_fields(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchFields", []))

    @builtins.property
    @jsii.member(jsii_name="matchExpressions")
    def match_expressions(
        self,
    ) -> DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressionsList:
        return typing.cast(DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressionsList, jsii.get(self, "matchExpressions"))

    @builtins.property
    @jsii.member(jsii_name="matchFields")
    def match_fields(
        self,
    ) -> DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFieldsList:
        return typing.cast(DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFieldsList, jsii.get(self, "matchFields"))

    @builtins.property
    @jsii.member(jsii_name="matchExpressionsInput")
    def match_expressions_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressions]]], jsii.get(self, "matchExpressionsInput"))

    @builtins.property
    @jsii.member(jsii_name="matchFieldsInput")
    def match_fields_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFields]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFields]]], jsii.get(self, "matchFieldsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTerm]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTerm]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTerm]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf2c6168c78f678dc6f21218f4f3032829e3924fd91b783165ce695c23e88c3f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2f2a889d907d6aeb6958988571eacc1f09c735e149e2f13d1cc45072d92c84b9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putNodeSelectorTerm")
    def put_node_selector_term(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTerm, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf1a702f78d5e2c50077c43464491188eccf03b0f8e69cbb63cfb7eade803e88)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNodeSelectorTerm", [value]))

    @builtins.property
    @jsii.member(jsii_name="nodeSelectorTerm")
    def node_selector_term(
        self,
    ) -> DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermList:
        return typing.cast(DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermList, jsii.get(self, "nodeSelectorTerm"))

    @builtins.property
    @jsii.member(jsii_name="nodeSelectorTermInput")
    def node_selector_term_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTerm]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTerm]]], jsii.get(self, "nodeSelectorTermInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataKubernetesPersistentVolumeV1SpecNodeAffinityRequired]:
        return typing.cast(typing.Optional[DataKubernetesPersistentVolumeV1SpecNodeAffinityRequired], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataKubernetesPersistentVolumeV1SpecNodeAffinityRequired],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19552da9d2d4099620d4931679288c6fc52850d5801bfd105274ee3fb6423814)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataKubernetesPersistentVolumeV1SpecOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b794878e6bd39bdc6e0d62cb339b6b32093d7aefb6998aa3737858a4f8a284e2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putClaimRef")
    def put_claim_ref(
        self,
        *,
        name: builtins.str,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: The name of the PersistentVolumeClaim. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#name DataKubernetesPersistentVolumeV1#name}
        :param namespace: The namespace of the PersistentVolumeClaim. Uses 'default' namespace if none is specified. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#namespace DataKubernetesPersistentVolumeV1#namespace}
        '''
        value = DataKubernetesPersistentVolumeV1SpecClaimRef(
            name=name, namespace=namespace
        )

        return typing.cast(None, jsii.invoke(self, "putClaimRef", [value]))

    @jsii.member(jsii_name="putNodeAffinity")
    def put_node_affinity(
        self,
        *,
        required: typing.Optional[typing.Union[DataKubernetesPersistentVolumeV1SpecNodeAffinityRequired, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param required: required block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#required DataKubernetesPersistentVolumeV1#required}
        '''
        value = DataKubernetesPersistentVolumeV1SpecNodeAffinity(required=required)

        return typing.cast(None, jsii.invoke(self, "putNodeAffinity", [value]))

    @jsii.member(jsii_name="putPersistentVolumeSource")
    def put_persistent_volume_source(
        self,
        *,
        aws_elastic_block_store: typing.Optional[typing.Union["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAwsElasticBlockStore", typing.Dict[builtins.str, typing.Any]]] = None,
        azure_disk: typing.Optional[typing.Union["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAzureDisk", typing.Dict[builtins.str, typing.Any]]] = None,
        azure_file: typing.Optional[typing.Union["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAzureFile", typing.Dict[builtins.str, typing.Any]]] = None,
        ceph_fs: typing.Optional[typing.Union["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCephFs", typing.Dict[builtins.str, typing.Any]]] = None,
        cinder: typing.Optional[typing.Union["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCinder", typing.Dict[builtins.str, typing.Any]]] = None,
        csi: typing.Optional[typing.Union["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsi", typing.Dict[builtins.str, typing.Any]]] = None,
        fc: typing.Optional[typing.Union["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFc", typing.Dict[builtins.str, typing.Any]]] = None,
        flex_volume: typing.Optional[typing.Union["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlexVolume", typing.Dict[builtins.str, typing.Any]]] = None,
        flocker: typing.Optional[typing.Union["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlocker", typing.Dict[builtins.str, typing.Any]]] = None,
        gce_persistent_disk: typing.Optional[typing.Union["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceGcePersistentDisk", typing.Dict[builtins.str, typing.Any]]] = None,
        glusterfs: typing.Optional[typing.Union["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceGlusterfs", typing.Dict[builtins.str, typing.Any]]] = None,
        host_path: typing.Optional[typing.Union["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceHostPath", typing.Dict[builtins.str, typing.Any]]] = None,
        iscsi: typing.Optional[typing.Union["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceIscsi", typing.Dict[builtins.str, typing.Any]]] = None,
        local: typing.Optional[typing.Union["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceLocal", typing.Dict[builtins.str, typing.Any]]] = None,
        nfs: typing.Optional[typing.Union["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceNfs", typing.Dict[builtins.str, typing.Any]]] = None,
        photon_persistent_disk: typing.Optional[typing.Union["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourcePhotonPersistentDisk", typing.Dict[builtins.str, typing.Any]]] = None,
        quobyte: typing.Optional[typing.Union["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceQuobyte", typing.Dict[builtins.str, typing.Any]]] = None,
        rbd: typing.Optional[typing.Union["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceRbd", typing.Dict[builtins.str, typing.Any]]] = None,
        vsphere_volume: typing.Optional[typing.Union["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceVsphereVolume", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param aws_elastic_block_store: aws_elastic_block_store block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#aws_elastic_block_store DataKubernetesPersistentVolumeV1#aws_elastic_block_store}
        :param azure_disk: azure_disk block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#azure_disk DataKubernetesPersistentVolumeV1#azure_disk}
        :param azure_file: azure_file block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#azure_file DataKubernetesPersistentVolumeV1#azure_file}
        :param ceph_fs: ceph_fs block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#ceph_fs DataKubernetesPersistentVolumeV1#ceph_fs}
        :param cinder: cinder block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#cinder DataKubernetesPersistentVolumeV1#cinder}
        :param csi: csi block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#csi DataKubernetesPersistentVolumeV1#csi}
        :param fc: fc block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#fc DataKubernetesPersistentVolumeV1#fc}
        :param flex_volume: flex_volume block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#flex_volume DataKubernetesPersistentVolumeV1#flex_volume}
        :param flocker: flocker block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#flocker DataKubernetesPersistentVolumeV1#flocker}
        :param gce_persistent_disk: gce_persistent_disk block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#gce_persistent_disk DataKubernetesPersistentVolumeV1#gce_persistent_disk}
        :param glusterfs: glusterfs block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#glusterfs DataKubernetesPersistentVolumeV1#glusterfs}
        :param host_path: host_path block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#host_path DataKubernetesPersistentVolumeV1#host_path}
        :param iscsi: iscsi block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#iscsi DataKubernetesPersistentVolumeV1#iscsi}
        :param local: local block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#local DataKubernetesPersistentVolumeV1#local}
        :param nfs: nfs block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#nfs DataKubernetesPersistentVolumeV1#nfs}
        :param photon_persistent_disk: photon_persistent_disk block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#photon_persistent_disk DataKubernetesPersistentVolumeV1#photon_persistent_disk}
        :param quobyte: quobyte block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#quobyte DataKubernetesPersistentVolumeV1#quobyte}
        :param rbd: rbd block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#rbd DataKubernetesPersistentVolumeV1#rbd}
        :param vsphere_volume: vsphere_volume block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#vsphere_volume DataKubernetesPersistentVolumeV1#vsphere_volume}
        '''
        value = DataKubernetesPersistentVolumeV1SpecPersistentVolumeSource(
            aws_elastic_block_store=aws_elastic_block_store,
            azure_disk=azure_disk,
            azure_file=azure_file,
            ceph_fs=ceph_fs,
            cinder=cinder,
            csi=csi,
            fc=fc,
            flex_volume=flex_volume,
            flocker=flocker,
            gce_persistent_disk=gce_persistent_disk,
            glusterfs=glusterfs,
            host_path=host_path,
            iscsi=iscsi,
            local=local,
            nfs=nfs,
            photon_persistent_disk=photon_persistent_disk,
            quobyte=quobyte,
            rbd=rbd,
            vsphere_volume=vsphere_volume,
        )

        return typing.cast(None, jsii.invoke(self, "putPersistentVolumeSource", [value]))

    @jsii.member(jsii_name="resetClaimRef")
    def reset_claim_ref(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClaimRef", []))

    @jsii.member(jsii_name="resetMountOptions")
    def reset_mount_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMountOptions", []))

    @jsii.member(jsii_name="resetNodeAffinity")
    def reset_node_affinity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodeAffinity", []))

    @jsii.member(jsii_name="resetPersistentVolumeReclaimPolicy")
    def reset_persistent_volume_reclaim_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPersistentVolumeReclaimPolicy", []))

    @jsii.member(jsii_name="resetStorageClassName")
    def reset_storage_class_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageClassName", []))

    @jsii.member(jsii_name="resetVolumeMode")
    def reset_volume_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolumeMode", []))

    @builtins.property
    @jsii.member(jsii_name="claimRef")
    def claim_ref(self) -> DataKubernetesPersistentVolumeV1SpecClaimRefOutputReference:
        return typing.cast(DataKubernetesPersistentVolumeV1SpecClaimRefOutputReference, jsii.get(self, "claimRef"))

    @builtins.property
    @jsii.member(jsii_name="nodeAffinity")
    def node_affinity(
        self,
    ) -> DataKubernetesPersistentVolumeV1SpecNodeAffinityOutputReference:
        return typing.cast(DataKubernetesPersistentVolumeV1SpecNodeAffinityOutputReference, jsii.get(self, "nodeAffinity"))

    @builtins.property
    @jsii.member(jsii_name="persistentVolumeSource")
    def persistent_volume_source(
        self,
    ) -> "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceOutputReference":
        return typing.cast("DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceOutputReference", jsii.get(self, "persistentVolumeSource"))

    @builtins.property
    @jsii.member(jsii_name="accessModesInput")
    def access_modes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "accessModesInput"))

    @builtins.property
    @jsii.member(jsii_name="capacityInput")
    def capacity_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "capacityInput"))

    @builtins.property
    @jsii.member(jsii_name="claimRefInput")
    def claim_ref_input(
        self,
    ) -> typing.Optional[DataKubernetesPersistentVolumeV1SpecClaimRef]:
        return typing.cast(typing.Optional[DataKubernetesPersistentVolumeV1SpecClaimRef], jsii.get(self, "claimRefInput"))

    @builtins.property
    @jsii.member(jsii_name="mountOptionsInput")
    def mount_options_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "mountOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeAffinityInput")
    def node_affinity_input(
        self,
    ) -> typing.Optional[DataKubernetesPersistentVolumeV1SpecNodeAffinity]:
        return typing.cast(typing.Optional[DataKubernetesPersistentVolumeV1SpecNodeAffinity], jsii.get(self, "nodeAffinityInput"))

    @builtins.property
    @jsii.member(jsii_name="persistentVolumeReclaimPolicyInput")
    def persistent_volume_reclaim_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "persistentVolumeReclaimPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="persistentVolumeSourceInput")
    def persistent_volume_source_input(
        self,
    ) -> typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSource"]:
        return typing.cast(typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSource"], jsii.get(self, "persistentVolumeSourceInput"))

    @builtins.property
    @jsii.member(jsii_name="storageClassNameInput")
    def storage_class_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageClassNameInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeModeInput")
    def volume_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "volumeModeInput"))

    @builtins.property
    @jsii.member(jsii_name="accessModes")
    def access_modes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "accessModes"))

    @access_modes.setter
    def access_modes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7061a88c1d438721992f3767ba16e704c61517680fef60e1d65797af780523e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessModes", value)

    @builtins.property
    @jsii.member(jsii_name="capacity")
    def capacity(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "capacity"))

    @capacity.setter
    def capacity(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88a321ff067dfef1bf5c0214522ed4c018402ce6bada2d646626ee517ed27983)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "capacity", value)

    @builtins.property
    @jsii.member(jsii_name="mountOptions")
    def mount_options(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "mountOptions"))

    @mount_options.setter
    def mount_options(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a1accdd341d97c5cbf156d651f36e62e077ce8dc23df86af856f5124a7708c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mountOptions", value)

    @builtins.property
    @jsii.member(jsii_name="persistentVolumeReclaimPolicy")
    def persistent_volume_reclaim_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "persistentVolumeReclaimPolicy"))

    @persistent_volume_reclaim_policy.setter
    def persistent_volume_reclaim_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dda1c61a79ab0f19aeb1f2896406b57811ee25ff1edf3e788e31a8e94b620506)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "persistentVolumeReclaimPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="storageClassName")
    def storage_class_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageClassName"))

    @storage_class_name.setter
    def storage_class_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__971f97406976b08fd006d872b12222662ffa5571c28be6e07dc24ea5a35d01de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageClassName", value)

    @builtins.property
    @jsii.member(jsii_name="volumeMode")
    def volume_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volumeMode"))

    @volume_mode.setter
    def volume_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c10d6afee1ce3aa3e1bb850b43b057029395f3a61eb79e165d7a34e23d321972)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeMode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataKubernetesPersistentVolumeV1Spec]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataKubernetesPersistentVolumeV1Spec]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataKubernetesPersistentVolumeV1Spec]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe84db2d068e0cb2368bfd390812a8cf3a027e90a51c79667c5c3b74d5dc5e5c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecPersistentVolumeSource",
    jsii_struct_bases=[],
    name_mapping={
        "aws_elastic_block_store": "awsElasticBlockStore",
        "azure_disk": "azureDisk",
        "azure_file": "azureFile",
        "ceph_fs": "cephFs",
        "cinder": "cinder",
        "csi": "csi",
        "fc": "fc",
        "flex_volume": "flexVolume",
        "flocker": "flocker",
        "gce_persistent_disk": "gcePersistentDisk",
        "glusterfs": "glusterfs",
        "host_path": "hostPath",
        "iscsi": "iscsi",
        "local": "local",
        "nfs": "nfs",
        "photon_persistent_disk": "photonPersistentDisk",
        "quobyte": "quobyte",
        "rbd": "rbd",
        "vsphere_volume": "vsphereVolume",
    },
)
class DataKubernetesPersistentVolumeV1SpecPersistentVolumeSource:
    def __init__(
        self,
        *,
        aws_elastic_block_store: typing.Optional[typing.Union["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAwsElasticBlockStore", typing.Dict[builtins.str, typing.Any]]] = None,
        azure_disk: typing.Optional[typing.Union["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAzureDisk", typing.Dict[builtins.str, typing.Any]]] = None,
        azure_file: typing.Optional[typing.Union["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAzureFile", typing.Dict[builtins.str, typing.Any]]] = None,
        ceph_fs: typing.Optional[typing.Union["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCephFs", typing.Dict[builtins.str, typing.Any]]] = None,
        cinder: typing.Optional[typing.Union["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCinder", typing.Dict[builtins.str, typing.Any]]] = None,
        csi: typing.Optional[typing.Union["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsi", typing.Dict[builtins.str, typing.Any]]] = None,
        fc: typing.Optional[typing.Union["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFc", typing.Dict[builtins.str, typing.Any]]] = None,
        flex_volume: typing.Optional[typing.Union["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlexVolume", typing.Dict[builtins.str, typing.Any]]] = None,
        flocker: typing.Optional[typing.Union["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlocker", typing.Dict[builtins.str, typing.Any]]] = None,
        gce_persistent_disk: typing.Optional[typing.Union["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceGcePersistentDisk", typing.Dict[builtins.str, typing.Any]]] = None,
        glusterfs: typing.Optional[typing.Union["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceGlusterfs", typing.Dict[builtins.str, typing.Any]]] = None,
        host_path: typing.Optional[typing.Union["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceHostPath", typing.Dict[builtins.str, typing.Any]]] = None,
        iscsi: typing.Optional[typing.Union["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceIscsi", typing.Dict[builtins.str, typing.Any]]] = None,
        local: typing.Optional[typing.Union["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceLocal", typing.Dict[builtins.str, typing.Any]]] = None,
        nfs: typing.Optional[typing.Union["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceNfs", typing.Dict[builtins.str, typing.Any]]] = None,
        photon_persistent_disk: typing.Optional[typing.Union["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourcePhotonPersistentDisk", typing.Dict[builtins.str, typing.Any]]] = None,
        quobyte: typing.Optional[typing.Union["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceQuobyte", typing.Dict[builtins.str, typing.Any]]] = None,
        rbd: typing.Optional[typing.Union["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceRbd", typing.Dict[builtins.str, typing.Any]]] = None,
        vsphere_volume: typing.Optional[typing.Union["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceVsphereVolume", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param aws_elastic_block_store: aws_elastic_block_store block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#aws_elastic_block_store DataKubernetesPersistentVolumeV1#aws_elastic_block_store}
        :param azure_disk: azure_disk block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#azure_disk DataKubernetesPersistentVolumeV1#azure_disk}
        :param azure_file: azure_file block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#azure_file DataKubernetesPersistentVolumeV1#azure_file}
        :param ceph_fs: ceph_fs block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#ceph_fs DataKubernetesPersistentVolumeV1#ceph_fs}
        :param cinder: cinder block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#cinder DataKubernetesPersistentVolumeV1#cinder}
        :param csi: csi block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#csi DataKubernetesPersistentVolumeV1#csi}
        :param fc: fc block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#fc DataKubernetesPersistentVolumeV1#fc}
        :param flex_volume: flex_volume block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#flex_volume DataKubernetesPersistentVolumeV1#flex_volume}
        :param flocker: flocker block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#flocker DataKubernetesPersistentVolumeV1#flocker}
        :param gce_persistent_disk: gce_persistent_disk block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#gce_persistent_disk DataKubernetesPersistentVolumeV1#gce_persistent_disk}
        :param glusterfs: glusterfs block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#glusterfs DataKubernetesPersistentVolumeV1#glusterfs}
        :param host_path: host_path block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#host_path DataKubernetesPersistentVolumeV1#host_path}
        :param iscsi: iscsi block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#iscsi DataKubernetesPersistentVolumeV1#iscsi}
        :param local: local block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#local DataKubernetesPersistentVolumeV1#local}
        :param nfs: nfs block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#nfs DataKubernetesPersistentVolumeV1#nfs}
        :param photon_persistent_disk: photon_persistent_disk block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#photon_persistent_disk DataKubernetesPersistentVolumeV1#photon_persistent_disk}
        :param quobyte: quobyte block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#quobyte DataKubernetesPersistentVolumeV1#quobyte}
        :param rbd: rbd block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#rbd DataKubernetesPersistentVolumeV1#rbd}
        :param vsphere_volume: vsphere_volume block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#vsphere_volume DataKubernetesPersistentVolumeV1#vsphere_volume}
        '''
        if isinstance(aws_elastic_block_store, dict):
            aws_elastic_block_store = DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAwsElasticBlockStore(**aws_elastic_block_store)
        if isinstance(azure_disk, dict):
            azure_disk = DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAzureDisk(**azure_disk)
        if isinstance(azure_file, dict):
            azure_file = DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAzureFile(**azure_file)
        if isinstance(ceph_fs, dict):
            ceph_fs = DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCephFs(**ceph_fs)
        if isinstance(cinder, dict):
            cinder = DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCinder(**cinder)
        if isinstance(csi, dict):
            csi = DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsi(**csi)
        if isinstance(fc, dict):
            fc = DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFc(**fc)
        if isinstance(flex_volume, dict):
            flex_volume = DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlexVolume(**flex_volume)
        if isinstance(flocker, dict):
            flocker = DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlocker(**flocker)
        if isinstance(gce_persistent_disk, dict):
            gce_persistent_disk = DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceGcePersistentDisk(**gce_persistent_disk)
        if isinstance(glusterfs, dict):
            glusterfs = DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceGlusterfs(**glusterfs)
        if isinstance(host_path, dict):
            host_path = DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceHostPath(**host_path)
        if isinstance(iscsi, dict):
            iscsi = DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceIscsi(**iscsi)
        if isinstance(local, dict):
            local = DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceLocal(**local)
        if isinstance(nfs, dict):
            nfs = DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceNfs(**nfs)
        if isinstance(photon_persistent_disk, dict):
            photon_persistent_disk = DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourcePhotonPersistentDisk(**photon_persistent_disk)
        if isinstance(quobyte, dict):
            quobyte = DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceQuobyte(**quobyte)
        if isinstance(rbd, dict):
            rbd = DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceRbd(**rbd)
        if isinstance(vsphere_volume, dict):
            vsphere_volume = DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceVsphereVolume(**vsphere_volume)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6296fac964270b113bd0b52cc34701e4ae767965f1a6b9c67953fff4ccb92eb6)
            check_type(argname="argument aws_elastic_block_store", value=aws_elastic_block_store, expected_type=type_hints["aws_elastic_block_store"])
            check_type(argname="argument azure_disk", value=azure_disk, expected_type=type_hints["azure_disk"])
            check_type(argname="argument azure_file", value=azure_file, expected_type=type_hints["azure_file"])
            check_type(argname="argument ceph_fs", value=ceph_fs, expected_type=type_hints["ceph_fs"])
            check_type(argname="argument cinder", value=cinder, expected_type=type_hints["cinder"])
            check_type(argname="argument csi", value=csi, expected_type=type_hints["csi"])
            check_type(argname="argument fc", value=fc, expected_type=type_hints["fc"])
            check_type(argname="argument flex_volume", value=flex_volume, expected_type=type_hints["flex_volume"])
            check_type(argname="argument flocker", value=flocker, expected_type=type_hints["flocker"])
            check_type(argname="argument gce_persistent_disk", value=gce_persistent_disk, expected_type=type_hints["gce_persistent_disk"])
            check_type(argname="argument glusterfs", value=glusterfs, expected_type=type_hints["glusterfs"])
            check_type(argname="argument host_path", value=host_path, expected_type=type_hints["host_path"])
            check_type(argname="argument iscsi", value=iscsi, expected_type=type_hints["iscsi"])
            check_type(argname="argument local", value=local, expected_type=type_hints["local"])
            check_type(argname="argument nfs", value=nfs, expected_type=type_hints["nfs"])
            check_type(argname="argument photon_persistent_disk", value=photon_persistent_disk, expected_type=type_hints["photon_persistent_disk"])
            check_type(argname="argument quobyte", value=quobyte, expected_type=type_hints["quobyte"])
            check_type(argname="argument rbd", value=rbd, expected_type=type_hints["rbd"])
            check_type(argname="argument vsphere_volume", value=vsphere_volume, expected_type=type_hints["vsphere_volume"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if aws_elastic_block_store is not None:
            self._values["aws_elastic_block_store"] = aws_elastic_block_store
        if azure_disk is not None:
            self._values["azure_disk"] = azure_disk
        if azure_file is not None:
            self._values["azure_file"] = azure_file
        if ceph_fs is not None:
            self._values["ceph_fs"] = ceph_fs
        if cinder is not None:
            self._values["cinder"] = cinder
        if csi is not None:
            self._values["csi"] = csi
        if fc is not None:
            self._values["fc"] = fc
        if flex_volume is not None:
            self._values["flex_volume"] = flex_volume
        if flocker is not None:
            self._values["flocker"] = flocker
        if gce_persistent_disk is not None:
            self._values["gce_persistent_disk"] = gce_persistent_disk
        if glusterfs is not None:
            self._values["glusterfs"] = glusterfs
        if host_path is not None:
            self._values["host_path"] = host_path
        if iscsi is not None:
            self._values["iscsi"] = iscsi
        if local is not None:
            self._values["local"] = local
        if nfs is not None:
            self._values["nfs"] = nfs
        if photon_persistent_disk is not None:
            self._values["photon_persistent_disk"] = photon_persistent_disk
        if quobyte is not None:
            self._values["quobyte"] = quobyte
        if rbd is not None:
            self._values["rbd"] = rbd
        if vsphere_volume is not None:
            self._values["vsphere_volume"] = vsphere_volume

    @builtins.property
    def aws_elastic_block_store(
        self,
    ) -> typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAwsElasticBlockStore"]:
        '''aws_elastic_block_store block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#aws_elastic_block_store DataKubernetesPersistentVolumeV1#aws_elastic_block_store}
        '''
        result = self._values.get("aws_elastic_block_store")
        return typing.cast(typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAwsElasticBlockStore"], result)

    @builtins.property
    def azure_disk(
        self,
    ) -> typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAzureDisk"]:
        '''azure_disk block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#azure_disk DataKubernetesPersistentVolumeV1#azure_disk}
        '''
        result = self._values.get("azure_disk")
        return typing.cast(typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAzureDisk"], result)

    @builtins.property
    def azure_file(
        self,
    ) -> typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAzureFile"]:
        '''azure_file block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#azure_file DataKubernetesPersistentVolumeV1#azure_file}
        '''
        result = self._values.get("azure_file")
        return typing.cast(typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAzureFile"], result)

    @builtins.property
    def ceph_fs(
        self,
    ) -> typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCephFs"]:
        '''ceph_fs block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#ceph_fs DataKubernetesPersistentVolumeV1#ceph_fs}
        '''
        result = self._values.get("ceph_fs")
        return typing.cast(typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCephFs"], result)

    @builtins.property
    def cinder(
        self,
    ) -> typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCinder"]:
        '''cinder block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#cinder DataKubernetesPersistentVolumeV1#cinder}
        '''
        result = self._values.get("cinder")
        return typing.cast(typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCinder"], result)

    @builtins.property
    def csi(
        self,
    ) -> typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsi"]:
        '''csi block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#csi DataKubernetesPersistentVolumeV1#csi}
        '''
        result = self._values.get("csi")
        return typing.cast(typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsi"], result)

    @builtins.property
    def fc(
        self,
    ) -> typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFc"]:
        '''fc block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#fc DataKubernetesPersistentVolumeV1#fc}
        '''
        result = self._values.get("fc")
        return typing.cast(typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFc"], result)

    @builtins.property
    def flex_volume(
        self,
    ) -> typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlexVolume"]:
        '''flex_volume block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#flex_volume DataKubernetesPersistentVolumeV1#flex_volume}
        '''
        result = self._values.get("flex_volume")
        return typing.cast(typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlexVolume"], result)

    @builtins.property
    def flocker(
        self,
    ) -> typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlocker"]:
        '''flocker block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#flocker DataKubernetesPersistentVolumeV1#flocker}
        '''
        result = self._values.get("flocker")
        return typing.cast(typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlocker"], result)

    @builtins.property
    def gce_persistent_disk(
        self,
    ) -> typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceGcePersistentDisk"]:
        '''gce_persistent_disk block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#gce_persistent_disk DataKubernetesPersistentVolumeV1#gce_persistent_disk}
        '''
        result = self._values.get("gce_persistent_disk")
        return typing.cast(typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceGcePersistentDisk"], result)

    @builtins.property
    def glusterfs(
        self,
    ) -> typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceGlusterfs"]:
        '''glusterfs block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#glusterfs DataKubernetesPersistentVolumeV1#glusterfs}
        '''
        result = self._values.get("glusterfs")
        return typing.cast(typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceGlusterfs"], result)

    @builtins.property
    def host_path(
        self,
    ) -> typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceHostPath"]:
        '''host_path block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#host_path DataKubernetesPersistentVolumeV1#host_path}
        '''
        result = self._values.get("host_path")
        return typing.cast(typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceHostPath"], result)

    @builtins.property
    def iscsi(
        self,
    ) -> typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceIscsi"]:
        '''iscsi block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#iscsi DataKubernetesPersistentVolumeV1#iscsi}
        '''
        result = self._values.get("iscsi")
        return typing.cast(typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceIscsi"], result)

    @builtins.property
    def local(
        self,
    ) -> typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceLocal"]:
        '''local block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#local DataKubernetesPersistentVolumeV1#local}
        '''
        result = self._values.get("local")
        return typing.cast(typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceLocal"], result)

    @builtins.property
    def nfs(
        self,
    ) -> typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceNfs"]:
        '''nfs block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#nfs DataKubernetesPersistentVolumeV1#nfs}
        '''
        result = self._values.get("nfs")
        return typing.cast(typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceNfs"], result)

    @builtins.property
    def photon_persistent_disk(
        self,
    ) -> typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourcePhotonPersistentDisk"]:
        '''photon_persistent_disk block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#photon_persistent_disk DataKubernetesPersistentVolumeV1#photon_persistent_disk}
        '''
        result = self._values.get("photon_persistent_disk")
        return typing.cast(typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourcePhotonPersistentDisk"], result)

    @builtins.property
    def quobyte(
        self,
    ) -> typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceQuobyte"]:
        '''quobyte block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#quobyte DataKubernetesPersistentVolumeV1#quobyte}
        '''
        result = self._values.get("quobyte")
        return typing.cast(typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceQuobyte"], result)

    @builtins.property
    def rbd(
        self,
    ) -> typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceRbd"]:
        '''rbd block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#rbd DataKubernetesPersistentVolumeV1#rbd}
        '''
        result = self._values.get("rbd")
        return typing.cast(typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceRbd"], result)

    @builtins.property
    def vsphere_volume(
        self,
    ) -> typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceVsphereVolume"]:
        '''vsphere_volume block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#vsphere_volume DataKubernetesPersistentVolumeV1#vsphere_volume}
        '''
        result = self._values.get("vsphere_volume")
        return typing.cast(typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceVsphereVolume"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAwsElasticBlockStore",
    jsii_struct_bases=[],
    name_mapping={
        "volume_id": "volumeId",
        "fs_type": "fsType",
        "partition": "partition",
        "read_only": "readOnly",
    },
)
class DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAwsElasticBlockStore:
    def __init__(
        self,
        *,
        volume_id: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        partition: typing.Optional[jsii.Number] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param volume_id: Unique ID of the persistent disk resource in AWS (Amazon EBS volume). More info: http://kubernetes.io/docs/user-guide/volumes#awselasticblockstore. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#volume_id DataKubernetesPersistentVolumeV1#volume_id}
        :param fs_type: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: http://kubernetes.io/docs/user-guide/volumes#awselasticblockstore Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#fs_type DataKubernetesPersistentVolumeV1#fs_type}
        :param partition: The partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#partition DataKubernetesPersistentVolumeV1#partition}
        :param read_only: Whether to set the read-only property in VolumeMounts to "true". If omitted, the default is "false". More info: http://kubernetes.io/docs/user-guide/volumes#awselasticblockstore. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#read_only DataKubernetesPersistentVolumeV1#read_only}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95838069dc361c6b1d0bb25c94bda6ee6181da8df259d5cd73163bd2e1dd96af)
            check_type(argname="argument volume_id", value=volume_id, expected_type=type_hints["volume_id"])
            check_type(argname="argument fs_type", value=fs_type, expected_type=type_hints["fs_type"])
            check_type(argname="argument partition", value=partition, expected_type=type_hints["partition"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "volume_id": volume_id,
        }
        if fs_type is not None:
            self._values["fs_type"] = fs_type
        if partition is not None:
            self._values["partition"] = partition
        if read_only is not None:
            self._values["read_only"] = read_only

    @builtins.property
    def volume_id(self) -> builtins.str:
        '''Unique ID of the persistent disk resource in AWS (Amazon EBS volume). More info: http://kubernetes.io/docs/user-guide/volumes#awselasticblockstore.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#volume_id DataKubernetesPersistentVolumeV1#volume_id}
        '''
        result = self._values.get("volume_id")
        assert result is not None, "Required property 'volume_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def fs_type(self) -> typing.Optional[builtins.str]:
        '''Filesystem type of the volume that you want to mount.

        Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: http://kubernetes.io/docs/user-guide/volumes#awselasticblockstore

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#fs_type DataKubernetesPersistentVolumeV1#fs_type}
        '''
        result = self._values.get("fs_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def partition(self) -> typing.Optional[jsii.Number]:
        '''The partition in the volume that you want to mount.

        If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#partition DataKubernetesPersistentVolumeV1#partition}
        '''
        result = self._values.get("partition")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to set the read-only property in VolumeMounts to "true". If omitted, the default is "false". More info: http://kubernetes.io/docs/user-guide/volumes#awselasticblockstore.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#read_only DataKubernetesPersistentVolumeV1#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAwsElasticBlockStore(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAwsElasticBlockStoreOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAwsElasticBlockStoreOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c39473f1592c11be2eda4239469558a0c0dff273b0d6eecfc0d4d409efba0202)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFsType")
    def reset_fs_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFsType", []))

    @jsii.member(jsii_name="resetPartition")
    def reset_partition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPartition", []))

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @builtins.property
    @jsii.member(jsii_name="fsTypeInput")
    def fs_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fsTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="partitionInput")
    def partition_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "partitionInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeIdInput")
    def volume_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "volumeIdInput"))

    @builtins.property
    @jsii.member(jsii_name="fsType")
    def fs_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fsType"))

    @fs_type.setter
    def fs_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d32141dea011167aa5799235c7cd0942280f608ae7afe2f2203f2bcf328e0b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fsType", value)

    @builtins.property
    @jsii.member(jsii_name="partition")
    def partition(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "partition"))

    @partition.setter
    def partition(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__765b098fd1aca3b946e0c21ca74b27d3dac6bf5a41133095a7b768c03cb481e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "partition", value)

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "readOnly"))

    @read_only.setter
    def read_only(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1b787bf7b7f97f5c7f7478161c262220b2a8d4fbd0b5c771c36816c469bd7cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="volumeId")
    def volume_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volumeId"))

    @volume_id.setter
    def volume_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b8ab041b82b3f21e2266c7b4acb8aa86e3dba09a1bb81472d4b11653cbe93f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAwsElasticBlockStore]:
        return typing.cast(typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAwsElasticBlockStore], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAwsElasticBlockStore],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19b69fccdeb0617f14ca28f634686c2dcb9880daa6337f5a2e13670df4127ef2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAzureDisk",
    jsii_struct_bases=[],
    name_mapping={
        "caching_mode": "cachingMode",
        "data_disk_uri": "dataDiskUri",
        "disk_name": "diskName",
        "fs_type": "fsType",
        "kind": "kind",
        "read_only": "readOnly",
    },
)
class DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAzureDisk:
    def __init__(
        self,
        *,
        caching_mode: builtins.str,
        data_disk_uri: builtins.str,
        disk_name: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        kind: typing.Optional[builtins.str] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param caching_mode: Host Caching mode: None, Read Only, Read Write. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#caching_mode DataKubernetesPersistentVolumeV1#caching_mode}
        :param data_disk_uri: The URI the data disk in the blob storage. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#data_disk_uri DataKubernetesPersistentVolumeV1#data_disk_uri}
        :param disk_name: The Name of the data disk in the blob storage. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#disk_name DataKubernetesPersistentVolumeV1#disk_name}
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#fs_type DataKubernetesPersistentVolumeV1#fs_type}
        :param kind: The type for the data disk. Expected values: Shared, Dedicated, Managed. Defaults to Shared. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#kind DataKubernetesPersistentVolumeV1#kind}
        :param read_only: Whether to force the read-only setting in VolumeMounts. Defaults to false (read/write). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#read_only DataKubernetesPersistentVolumeV1#read_only}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e483acc85a6ebf6dcea526cbf0d69e5763132e2960040c84fe96ee6a0a550c06)
            check_type(argname="argument caching_mode", value=caching_mode, expected_type=type_hints["caching_mode"])
            check_type(argname="argument data_disk_uri", value=data_disk_uri, expected_type=type_hints["data_disk_uri"])
            check_type(argname="argument disk_name", value=disk_name, expected_type=type_hints["disk_name"])
            check_type(argname="argument fs_type", value=fs_type, expected_type=type_hints["fs_type"])
            check_type(argname="argument kind", value=kind, expected_type=type_hints["kind"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "caching_mode": caching_mode,
            "data_disk_uri": data_disk_uri,
            "disk_name": disk_name,
        }
        if fs_type is not None:
            self._values["fs_type"] = fs_type
        if kind is not None:
            self._values["kind"] = kind
        if read_only is not None:
            self._values["read_only"] = read_only

    @builtins.property
    def caching_mode(self) -> builtins.str:
        '''Host Caching mode: None, Read Only, Read Write.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#caching_mode DataKubernetesPersistentVolumeV1#caching_mode}
        '''
        result = self._values.get("caching_mode")
        assert result is not None, "Required property 'caching_mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_disk_uri(self) -> builtins.str:
        '''The URI the data disk in the blob storage.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#data_disk_uri DataKubernetesPersistentVolumeV1#data_disk_uri}
        '''
        result = self._values.get("data_disk_uri")
        assert result is not None, "Required property 'data_disk_uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def disk_name(self) -> builtins.str:
        '''The Name of the data disk in the blob storage.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#disk_name DataKubernetesPersistentVolumeV1#disk_name}
        '''
        result = self._values.get("disk_name")
        assert result is not None, "Required property 'disk_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def fs_type(self) -> typing.Optional[builtins.str]:
        '''Filesystem type to mount.

        Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#fs_type DataKubernetesPersistentVolumeV1#fs_type}
        '''
        result = self._values.get("fs_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kind(self) -> typing.Optional[builtins.str]:
        '''The type for the data disk. Expected values: Shared, Dedicated, Managed. Defaults to Shared.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#kind DataKubernetesPersistentVolumeV1#kind}
        '''
        result = self._values.get("kind")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to force the read-only setting in VolumeMounts. Defaults to false (read/write).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#read_only DataKubernetesPersistentVolumeV1#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAzureDisk(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAzureDiskOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAzureDiskOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a3308fb8fb294a1f1fd7209b9a721b9f31d105b7bd0412caf61f624601f40487)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFsType")
    def reset_fs_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFsType", []))

    @jsii.member(jsii_name="resetKind")
    def reset_kind(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKind", []))

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @builtins.property
    @jsii.member(jsii_name="cachingModeInput")
    def caching_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cachingModeInput"))

    @builtins.property
    @jsii.member(jsii_name="dataDiskUriInput")
    def data_disk_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataDiskUriInput"))

    @builtins.property
    @jsii.member(jsii_name="diskNameInput")
    def disk_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "diskNameInput"))

    @builtins.property
    @jsii.member(jsii_name="fsTypeInput")
    def fs_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fsTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="kindInput")
    def kind_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kindInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="cachingMode")
    def caching_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cachingMode"))

    @caching_mode.setter
    def caching_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58d871700904b6ad5cd927126bac6e015035775ebcb58174bd1a712f926a02a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cachingMode", value)

    @builtins.property
    @jsii.member(jsii_name="dataDiskUri")
    def data_disk_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataDiskUri"))

    @data_disk_uri.setter
    def data_disk_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa56a080b16556e780cf25e9f7f8e83eb971b0fb00b129854da6055df2215a33)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataDiskUri", value)

    @builtins.property
    @jsii.member(jsii_name="diskName")
    def disk_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "diskName"))

    @disk_name.setter
    def disk_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__311faa50e75a507ea03c2abd5bd988f5c72d99cfaefa2e86e5e251f9899602d9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskName", value)

    @builtins.property
    @jsii.member(jsii_name="fsType")
    def fs_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fsType"))

    @fs_type.setter
    def fs_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5cd4df574e763901374c8caf0547d7f887b99d85217082cce9286f37fedcdfa1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fsType", value)

    @builtins.property
    @jsii.member(jsii_name="kind")
    def kind(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kind"))

    @kind.setter
    def kind(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ad867a959e9d99af0bb88fc76ea31ed3df6aa5fc84c8d7cda623a2396d7de17)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kind", value)

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "readOnly"))

    @read_only.setter
    def read_only(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f89ad155f332c3b84a198bb2577f5177af1048f2350173c9d61ba13d9f325b09)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAzureDisk]:
        return typing.cast(typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAzureDisk], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAzureDisk],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95d03ab14a494e1e7ed359e0d72fa823ae311bf72b20b0f903a3fefb1249114a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAzureFile",
    jsii_struct_bases=[],
    name_mapping={
        "secret_name": "secretName",
        "share_name": "shareName",
        "read_only": "readOnly",
        "secret_namespace": "secretNamespace",
    },
)
class DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAzureFile:
    def __init__(
        self,
        *,
        secret_name: builtins.str,
        share_name: builtins.str,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        secret_namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param secret_name: The name of secret that contains Azure Storage Account Name and Key. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#secret_name DataKubernetesPersistentVolumeV1#secret_name}
        :param share_name: Share Name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#share_name DataKubernetesPersistentVolumeV1#share_name}
        :param read_only: Whether to force the read-only setting in VolumeMounts. Defaults to false (read/write). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#read_only DataKubernetesPersistentVolumeV1#read_only}
        :param secret_namespace: The namespace of the secret that contains Azure Storage Account Name and Key. For Kubernetes up to 1.18.x the default is the same as the Pod. For Kubernetes 1.19.x and later the default is "default" namespace. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#secret_namespace DataKubernetesPersistentVolumeV1#secret_namespace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ac3ece09a4d6ec3ba1829cb4357a9b4465b6570d653ca27120ebd40fde1e7f8)
            check_type(argname="argument secret_name", value=secret_name, expected_type=type_hints["secret_name"])
            check_type(argname="argument share_name", value=share_name, expected_type=type_hints["share_name"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
            check_type(argname="argument secret_namespace", value=secret_namespace, expected_type=type_hints["secret_namespace"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "secret_name": secret_name,
            "share_name": share_name,
        }
        if read_only is not None:
            self._values["read_only"] = read_only
        if secret_namespace is not None:
            self._values["secret_namespace"] = secret_namespace

    @builtins.property
    def secret_name(self) -> builtins.str:
        '''The name of secret that contains Azure Storage Account Name and Key.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#secret_name DataKubernetesPersistentVolumeV1#secret_name}
        '''
        result = self._values.get("secret_name")
        assert result is not None, "Required property 'secret_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def share_name(self) -> builtins.str:
        '''Share Name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#share_name DataKubernetesPersistentVolumeV1#share_name}
        '''
        result = self._values.get("share_name")
        assert result is not None, "Required property 'share_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to force the read-only setting in VolumeMounts. Defaults to false (read/write).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#read_only DataKubernetesPersistentVolumeV1#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def secret_namespace(self) -> typing.Optional[builtins.str]:
        '''The namespace of the secret that contains Azure Storage Account Name and Key.

        For Kubernetes up to 1.18.x the default is the same as the Pod. For Kubernetes 1.19.x and later the default is "default" namespace.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#secret_namespace DataKubernetesPersistentVolumeV1#secret_namespace}
        '''
        result = self._values.get("secret_namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAzureFile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAzureFileOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAzureFileOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__28edb90ed8ae7f47d594a85d6fb624467755dbc7c92fbc7d4d040d266a759652)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @jsii.member(jsii_name="resetSecretNamespace")
    def reset_secret_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretNamespace", []))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="secretNameInput")
    def secret_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretNameInput"))

    @builtins.property
    @jsii.member(jsii_name="secretNamespaceInput")
    def secret_namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretNamespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="shareNameInput")
    def share_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "shareNameInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "readOnly"))

    @read_only.setter
    def read_only(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5c5cd63a76bb3c039f3e15c22b81e044fc0c598da9a24b17aefb8bcddc0cf89)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="secretName")
    def secret_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretName"))

    @secret_name.setter
    def secret_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d9ed3dbe864f607be7cbc0089eb4d9612fdf3155f8f27bdb0bf735de50e66e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretName", value)

    @builtins.property
    @jsii.member(jsii_name="secretNamespace")
    def secret_namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretNamespace"))

    @secret_namespace.setter
    def secret_namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2538fc6416227a3a30108812bfd1a48965984b2cadeac63007c4ee0257c463f6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretNamespace", value)

    @builtins.property
    @jsii.member(jsii_name="shareName")
    def share_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "shareName"))

    @share_name.setter
    def share_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8bd55424b9a283c5d40f202ab53428eafc4ff7b873a1e5064000c09e0f4b103)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shareName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAzureFile]:
        return typing.cast(typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAzureFile], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAzureFile],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__738f901648a3d0b3990c51ef2ef9670b99dba39b570edf1fb7f26d9cf8ec0a94)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCephFs",
    jsii_struct_bases=[],
    name_mapping={
        "monitors": "monitors",
        "path": "path",
        "read_only": "readOnly",
        "secret_file": "secretFile",
        "secret_ref": "secretRef",
        "user": "user",
    },
)
class DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCephFs:
    def __init__(
        self,
        *,
        monitors: typing.Sequence[builtins.str],
        path: typing.Optional[builtins.str] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        secret_file: typing.Optional[builtins.str] = None,
        secret_ref: typing.Optional[typing.Union["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCephFsSecretRef", typing.Dict[builtins.str, typing.Any]]] = None,
        user: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param monitors: Monitors is a collection of Ceph monitors More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#monitors DataKubernetesPersistentVolumeV1#monitors}
        :param path: Used as the mounted root, rather than the full Ceph tree, default is /. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#path DataKubernetesPersistentVolumeV1#path}
        :param read_only: Whether to force the read-only setting in VolumeMounts. Defaults to ``false`` (read/write). More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#read_only DataKubernetesPersistentVolumeV1#read_only}
        :param secret_file: The path to key ring for User, default is /etc/ceph/user.secret More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#secret_file DataKubernetesPersistentVolumeV1#secret_file}
        :param secret_ref: secret_ref block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#secret_ref DataKubernetesPersistentVolumeV1#secret_ref}
        :param user: User is the rados user name, default is admin. More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#user DataKubernetesPersistentVolumeV1#user}
        '''
        if isinstance(secret_ref, dict):
            secret_ref = DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCephFsSecretRef(**secret_ref)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cdcdc45d073fdaa2c763184b851d302bc46199909ca5ea212a22e99e587fb1e2)
            check_type(argname="argument monitors", value=monitors, expected_type=type_hints["monitors"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
            check_type(argname="argument secret_file", value=secret_file, expected_type=type_hints["secret_file"])
            check_type(argname="argument secret_ref", value=secret_ref, expected_type=type_hints["secret_ref"])
            check_type(argname="argument user", value=user, expected_type=type_hints["user"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "monitors": monitors,
        }
        if path is not None:
            self._values["path"] = path
        if read_only is not None:
            self._values["read_only"] = read_only
        if secret_file is not None:
            self._values["secret_file"] = secret_file
        if secret_ref is not None:
            self._values["secret_ref"] = secret_ref
        if user is not None:
            self._values["user"] = user

    @builtins.property
    def monitors(self) -> typing.List[builtins.str]:
        '''Monitors is a collection of Ceph monitors More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#monitors DataKubernetesPersistentVolumeV1#monitors}
        '''
        result = self._values.get("monitors")
        assert result is not None, "Required property 'monitors' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Used as the mounted root, rather than the full Ceph tree, default is /.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#path DataKubernetesPersistentVolumeV1#path}
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to force the read-only setting in VolumeMounts. Defaults to ``false`` (read/write). More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#read_only DataKubernetesPersistentVolumeV1#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def secret_file(self) -> typing.Optional[builtins.str]:
        '''The path to key ring for User, default is /etc/ceph/user.secret More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#secret_file DataKubernetesPersistentVolumeV1#secret_file}
        '''
        result = self._values.get("secret_file")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secret_ref(
        self,
    ) -> typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCephFsSecretRef"]:
        '''secret_ref block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#secret_ref DataKubernetesPersistentVolumeV1#secret_ref}
        '''
        result = self._values.get("secret_ref")
        return typing.cast(typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCephFsSecretRef"], result)

    @builtins.property
    def user(self) -> typing.Optional[builtins.str]:
        '''User is the rados user name, default is admin. More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#user DataKubernetesPersistentVolumeV1#user}
        '''
        result = self._values.get("user")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCephFs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCephFsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCephFsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3488d295f60f308cb06f30741be492c84fa722255824b30665a448e3ca3fba16)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSecretRef")
    def put_secret_ref(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#name DataKubernetesPersistentVolumeV1#name}
        :param namespace: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#namespace DataKubernetesPersistentVolumeV1#namespace}
        '''
        value = DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCephFsSecretRef(
            name=name, namespace=namespace
        )

        return typing.cast(None, jsii.invoke(self, "putSecretRef", [value]))

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @jsii.member(jsii_name="resetSecretFile")
    def reset_secret_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretFile", []))

    @jsii.member(jsii_name="resetSecretRef")
    def reset_secret_ref(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretRef", []))

    @jsii.member(jsii_name="resetUser")
    def reset_user(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUser", []))

    @builtins.property
    @jsii.member(jsii_name="secretRef")
    def secret_ref(
        self,
    ) -> "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCephFsSecretRefOutputReference":
        return typing.cast("DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCephFsSecretRefOutputReference", jsii.get(self, "secretRef"))

    @builtins.property
    @jsii.member(jsii_name="monitorsInput")
    def monitors_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "monitorsInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="secretFileInput")
    def secret_file_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretFileInput"))

    @builtins.property
    @jsii.member(jsii_name="secretRefInput")
    def secret_ref_input(
        self,
    ) -> typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCephFsSecretRef"]:
        return typing.cast(typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCephFsSecretRef"], jsii.get(self, "secretRefInput"))

    @builtins.property
    @jsii.member(jsii_name="userInput")
    def user_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userInput"))

    @builtins.property
    @jsii.member(jsii_name="monitors")
    def monitors(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "monitors"))

    @monitors.setter
    def monitors(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16baf5430605724bfab8071e8ca724db5bb9e4f183a9f05f87e07f799d8b060d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "monitors", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd37e16588ff102132af10def9115ea63cec1487341f4cd20e84b82dfcd9f308)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "readOnly"))

    @read_only.setter
    def read_only(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d19023a785f6165e7853c064ad2ce3924e1d0310cae21299bb8dff675b67bd23)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="secretFile")
    def secret_file(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretFile"))

    @secret_file.setter
    def secret_file(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1dd384b118df4bb807f6a04d5c0893ad2205a0105b561dc67f7315370ab69eb5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretFile", value)

    @builtins.property
    @jsii.member(jsii_name="user")
    def user(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "user"))

    @user.setter
    def user(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c69958dc6ab56e68c1dd46ac717ae3efa4ab1936358a8050fe2dbb1c124ce2a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "user", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCephFs]:
        return typing.cast(typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCephFs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCephFs],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3337c44b732676a63cfcd61ba80557009a02fe34cdfe0eadb6640a8a8a2681fc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCephFsSecretRef",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "namespace": "namespace"},
)
class DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCephFsSecretRef:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#name DataKubernetesPersistentVolumeV1#name}
        :param namespace: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#namespace DataKubernetesPersistentVolumeV1#namespace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e0cd02aea472dc4ed36725d72d2508ce37ff8415ecc7b83313df72e218ee31a)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if namespace is not None:
            self._values["namespace"] = namespace

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#name DataKubernetesPersistentVolumeV1#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#namespace DataKubernetesPersistentVolumeV1#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCephFsSecretRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCephFsSecretRefOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCephFsSecretRefOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2069edbfbb364d4f034f8afbd0b794aa6db0885272534f8b6042884cb8fad175)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

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
            type_hints = typing.get_type_hints(_typecheckingstub__bc6dcd3eb7d36809dd8061bf18ae4f666b385950e4b8e7064105ef59f1c3d1c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__120cdb9c74f187861bca77086c6170eb837dc0916cf179c8701bf5eec9207811)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCephFsSecretRef]:
        return typing.cast(typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCephFsSecretRef], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCephFsSecretRef],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93a92d18b7341525fc16258b86730d126b99a83215b85a4800f47efd6452871f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCinder",
    jsii_struct_bases=[],
    name_mapping={
        "volume_id": "volumeId",
        "fs_type": "fsType",
        "read_only": "readOnly",
    },
)
class DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCinder:
    def __init__(
        self,
        *,
        volume_id: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param volume_id: Volume ID used to identify the volume in Cinder. More info: http://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#volume_id DataKubernetesPersistentVolumeV1#volume_id}
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: http://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#fs_type DataKubernetesPersistentVolumeV1#fs_type}
        :param read_only: Whether to force the read-only setting in VolumeMounts. Defaults to false (read/write). More info: http://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#read_only DataKubernetesPersistentVolumeV1#read_only}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec56642d8343576e0754786703d9e36f153d4782718b1ac5668912a9835bd6a3)
            check_type(argname="argument volume_id", value=volume_id, expected_type=type_hints["volume_id"])
            check_type(argname="argument fs_type", value=fs_type, expected_type=type_hints["fs_type"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "volume_id": volume_id,
        }
        if fs_type is not None:
            self._values["fs_type"] = fs_type
        if read_only is not None:
            self._values["read_only"] = read_only

    @builtins.property
    def volume_id(self) -> builtins.str:
        '''Volume ID used to identify the volume in Cinder. More info: http://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#volume_id DataKubernetesPersistentVolumeV1#volume_id}
        '''
        result = self._values.get("volume_id")
        assert result is not None, "Required property 'volume_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def fs_type(self) -> typing.Optional[builtins.str]:
        '''Filesystem type to mount.

        Must be a filesystem type supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: http://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#fs_type DataKubernetesPersistentVolumeV1#fs_type}
        '''
        result = self._values.get("fs_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to force the read-only setting in VolumeMounts. Defaults to false (read/write). More info: http://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#read_only DataKubernetesPersistentVolumeV1#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCinder(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCinderOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCinderOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0ba1243103601444549492729b8737027309b2d50b745a54177edef31418b77e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFsType")
    def reset_fs_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFsType", []))

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @builtins.property
    @jsii.member(jsii_name="fsTypeInput")
    def fs_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fsTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeIdInput")
    def volume_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "volumeIdInput"))

    @builtins.property
    @jsii.member(jsii_name="fsType")
    def fs_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fsType"))

    @fs_type.setter
    def fs_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f08c07db653f737e53340bd7262fb20255cf72e1b8143932f4ac2787c4c702b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fsType", value)

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "readOnly"))

    @read_only.setter
    def read_only(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__385812c0b9ae3e30529c506c27f9c162a13d66a41eaeb613e2d48da1cd6f96a6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="volumeId")
    def volume_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volumeId"))

    @volume_id.setter
    def volume_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ecfd7da1842b45f8da798f2cb1ae6cbb289ad5ed6a2fa1fd19fd23cb31addd1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCinder]:
        return typing.cast(typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCinder], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCinder],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff7d064fec3e65f439f523bf2b0a19ee13b516b104d8308803e4c2c4f278f40d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsi",
    jsii_struct_bases=[],
    name_mapping={
        "driver": "driver",
        "volume_handle": "volumeHandle",
        "controller_expand_secret_ref": "controllerExpandSecretRef",
        "controller_publish_secret_ref": "controllerPublishSecretRef",
        "fs_type": "fsType",
        "node_publish_secret_ref": "nodePublishSecretRef",
        "node_stage_secret_ref": "nodeStageSecretRef",
        "read_only": "readOnly",
        "volume_attributes": "volumeAttributes",
    },
)
class DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsi:
    def __init__(
        self,
        *,
        driver: builtins.str,
        volume_handle: builtins.str,
        controller_expand_secret_ref: typing.Optional[typing.Union["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiControllerExpandSecretRef", typing.Dict[builtins.str, typing.Any]]] = None,
        controller_publish_secret_ref: typing.Optional[typing.Union["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiControllerPublishSecretRef", typing.Dict[builtins.str, typing.Any]]] = None,
        fs_type: typing.Optional[builtins.str] = None,
        node_publish_secret_ref: typing.Optional[typing.Union["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiNodePublishSecretRef", typing.Dict[builtins.str, typing.Any]]] = None,
        node_stage_secret_ref: typing.Optional[typing.Union["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiNodeStageSecretRef", typing.Dict[builtins.str, typing.Any]]] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        volume_attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param driver: the name of the volume driver to use. More info: https://kubernetes.io/docs/concepts/storage/volumes/#csi. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#driver DataKubernetesPersistentVolumeV1#driver}
        :param volume_handle: A string value that uniquely identifies the volume. More info: https://kubernetes.io/docs/concepts/storage/volumes/#csi. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#volume_handle DataKubernetesPersistentVolumeV1#volume_handle}
        :param controller_expand_secret_ref: controller_expand_secret_ref block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#controller_expand_secret_ref DataKubernetesPersistentVolumeV1#controller_expand_secret_ref}
        :param controller_publish_secret_ref: controller_publish_secret_ref block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#controller_publish_secret_ref DataKubernetesPersistentVolumeV1#controller_publish_secret_ref}
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#fs_type DataKubernetesPersistentVolumeV1#fs_type}
        :param node_publish_secret_ref: node_publish_secret_ref block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#node_publish_secret_ref DataKubernetesPersistentVolumeV1#node_publish_secret_ref}
        :param node_stage_secret_ref: node_stage_secret_ref block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#node_stage_secret_ref DataKubernetesPersistentVolumeV1#node_stage_secret_ref}
        :param read_only: Whether to set the read-only property in VolumeMounts to "true". If omitted, the default is "false". More info: http://kubernetes.io/docs/user-guide/volumes#csi. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#read_only DataKubernetesPersistentVolumeV1#read_only}
        :param volume_attributes: Attributes of the volume to publish. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#volume_attributes DataKubernetesPersistentVolumeV1#volume_attributes}
        '''
        if isinstance(controller_expand_secret_ref, dict):
            controller_expand_secret_ref = DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiControllerExpandSecretRef(**controller_expand_secret_ref)
        if isinstance(controller_publish_secret_ref, dict):
            controller_publish_secret_ref = DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiControllerPublishSecretRef(**controller_publish_secret_ref)
        if isinstance(node_publish_secret_ref, dict):
            node_publish_secret_ref = DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiNodePublishSecretRef(**node_publish_secret_ref)
        if isinstance(node_stage_secret_ref, dict):
            node_stage_secret_ref = DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiNodeStageSecretRef(**node_stage_secret_ref)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9961d99ede4f46ceeaf0465e2ce999eac04cf6ba23ba45b21d0a55d5bd068ba0)
            check_type(argname="argument driver", value=driver, expected_type=type_hints["driver"])
            check_type(argname="argument volume_handle", value=volume_handle, expected_type=type_hints["volume_handle"])
            check_type(argname="argument controller_expand_secret_ref", value=controller_expand_secret_ref, expected_type=type_hints["controller_expand_secret_ref"])
            check_type(argname="argument controller_publish_secret_ref", value=controller_publish_secret_ref, expected_type=type_hints["controller_publish_secret_ref"])
            check_type(argname="argument fs_type", value=fs_type, expected_type=type_hints["fs_type"])
            check_type(argname="argument node_publish_secret_ref", value=node_publish_secret_ref, expected_type=type_hints["node_publish_secret_ref"])
            check_type(argname="argument node_stage_secret_ref", value=node_stage_secret_ref, expected_type=type_hints["node_stage_secret_ref"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
            check_type(argname="argument volume_attributes", value=volume_attributes, expected_type=type_hints["volume_attributes"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "driver": driver,
            "volume_handle": volume_handle,
        }
        if controller_expand_secret_ref is not None:
            self._values["controller_expand_secret_ref"] = controller_expand_secret_ref
        if controller_publish_secret_ref is not None:
            self._values["controller_publish_secret_ref"] = controller_publish_secret_ref
        if fs_type is not None:
            self._values["fs_type"] = fs_type
        if node_publish_secret_ref is not None:
            self._values["node_publish_secret_ref"] = node_publish_secret_ref
        if node_stage_secret_ref is not None:
            self._values["node_stage_secret_ref"] = node_stage_secret_ref
        if read_only is not None:
            self._values["read_only"] = read_only
        if volume_attributes is not None:
            self._values["volume_attributes"] = volume_attributes

    @builtins.property
    def driver(self) -> builtins.str:
        '''the name of the volume driver to use. More info: https://kubernetes.io/docs/concepts/storage/volumes/#csi.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#driver DataKubernetesPersistentVolumeV1#driver}
        '''
        result = self._values.get("driver")
        assert result is not None, "Required property 'driver' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def volume_handle(self) -> builtins.str:
        '''A string value that uniquely identifies the volume. More info: https://kubernetes.io/docs/concepts/storage/volumes/#csi.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#volume_handle DataKubernetesPersistentVolumeV1#volume_handle}
        '''
        result = self._values.get("volume_handle")
        assert result is not None, "Required property 'volume_handle' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def controller_expand_secret_ref(
        self,
    ) -> typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiControllerExpandSecretRef"]:
        '''controller_expand_secret_ref block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#controller_expand_secret_ref DataKubernetesPersistentVolumeV1#controller_expand_secret_ref}
        '''
        result = self._values.get("controller_expand_secret_ref")
        return typing.cast(typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiControllerExpandSecretRef"], result)

    @builtins.property
    def controller_publish_secret_ref(
        self,
    ) -> typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiControllerPublishSecretRef"]:
        '''controller_publish_secret_ref block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#controller_publish_secret_ref DataKubernetesPersistentVolumeV1#controller_publish_secret_ref}
        '''
        result = self._values.get("controller_publish_secret_ref")
        return typing.cast(typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiControllerPublishSecretRef"], result)

    @builtins.property
    def fs_type(self) -> typing.Optional[builtins.str]:
        '''Filesystem type to mount.

        Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#fs_type DataKubernetesPersistentVolumeV1#fs_type}
        '''
        result = self._values.get("fs_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def node_publish_secret_ref(
        self,
    ) -> typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiNodePublishSecretRef"]:
        '''node_publish_secret_ref block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#node_publish_secret_ref DataKubernetesPersistentVolumeV1#node_publish_secret_ref}
        '''
        result = self._values.get("node_publish_secret_ref")
        return typing.cast(typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiNodePublishSecretRef"], result)

    @builtins.property
    def node_stage_secret_ref(
        self,
    ) -> typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiNodeStageSecretRef"]:
        '''node_stage_secret_ref block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#node_stage_secret_ref DataKubernetesPersistentVolumeV1#node_stage_secret_ref}
        '''
        result = self._values.get("node_stage_secret_ref")
        return typing.cast(typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiNodeStageSecretRef"], result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to set the read-only property in VolumeMounts to "true". If omitted, the default is "false". More info: http://kubernetes.io/docs/user-guide/volumes#csi.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#read_only DataKubernetesPersistentVolumeV1#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def volume_attributes(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Attributes of the volume to publish.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#volume_attributes DataKubernetesPersistentVolumeV1#volume_attributes}
        '''
        result = self._values.get("volume_attributes")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsi(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiControllerExpandSecretRef",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "namespace": "namespace"},
)
class DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiControllerExpandSecretRef:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#name DataKubernetesPersistentVolumeV1#name}
        :param namespace: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#namespace DataKubernetesPersistentVolumeV1#namespace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8110c2f55bdc756acaafa38cfbd0419213946ab715c89524edace0c0e40203a)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if namespace is not None:
            self._values["namespace"] = namespace

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#name DataKubernetesPersistentVolumeV1#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#namespace DataKubernetesPersistentVolumeV1#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiControllerExpandSecretRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiControllerExpandSecretRefOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiControllerExpandSecretRefOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2e36acb8095eb6533df9d5e5e4bfb8d7c1341993a1447d856d01f53a95cf5622)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

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
            type_hints = typing.get_type_hints(_typecheckingstub__f3d775212ac1aa75a834044c3e9abc84b4e6a99dd5ccaca122887692ab4c38bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b72d8d4ccfd37a3e3554f1c8b52ef996c82125a36428168cac776397fe793b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiControllerExpandSecretRef]:
        return typing.cast(typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiControllerExpandSecretRef], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiControllerExpandSecretRef],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70b6791a51f4c4bcf7a8f2c42f66a6a768e25a1e414addfffb6d3ebe87a2411b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiControllerPublishSecretRef",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "namespace": "namespace"},
)
class DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiControllerPublishSecretRef:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#name DataKubernetesPersistentVolumeV1#name}
        :param namespace: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#namespace DataKubernetesPersistentVolumeV1#namespace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73a8fd04f1e794d0f935e7f6f05b31e0aba0434c7ab0d6623f069f21dc69ada5)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if namespace is not None:
            self._values["namespace"] = namespace

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#name DataKubernetesPersistentVolumeV1#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#namespace DataKubernetesPersistentVolumeV1#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiControllerPublishSecretRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiControllerPublishSecretRefOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiControllerPublishSecretRefOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cc0eda3cfd401fd512e8da681a3aedb7383c365227ad19707015cbee56905687)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

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
            type_hints = typing.get_type_hints(_typecheckingstub__2142e929bbff211778f768c6998b4ee06b8da3eb6527921f28104eaafe751dc4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7fc095ca30fc35863439f549c02b21481267203274fad6e18ade63c4c5c5c27)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiControllerPublishSecretRef]:
        return typing.cast(typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiControllerPublishSecretRef], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiControllerPublishSecretRef],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55de99e5dd46ccb51d4580c45c5f1c2d9187ea3febfeef86623908c93e81ac1a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiNodePublishSecretRef",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "namespace": "namespace"},
)
class DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiNodePublishSecretRef:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#name DataKubernetesPersistentVolumeV1#name}
        :param namespace: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#namespace DataKubernetesPersistentVolumeV1#namespace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__897c0c857d094f8880a83ce5adb4d36298193fcda25657f7fb7d4b9b76c193c0)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if namespace is not None:
            self._values["namespace"] = namespace

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#name DataKubernetesPersistentVolumeV1#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#namespace DataKubernetesPersistentVolumeV1#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiNodePublishSecretRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiNodePublishSecretRefOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiNodePublishSecretRefOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e7b8764111a43cb47897968f146502a46a7fe0cd760a3f5503fc77917683b71e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

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
            type_hints = typing.get_type_hints(_typecheckingstub__18fe40a15a0acbd9081a5681dfc16dfd2c276c8a968a936a1d66c3651b224853)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d6f45d20630173fa5b550b9d67e4636c9d887673827480c718934385a98271d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiNodePublishSecretRef]:
        return typing.cast(typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiNodePublishSecretRef], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiNodePublishSecretRef],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a8f9963d3cfa92e51f08d99e90e035b4b7b7dc37dfdedae6d0140a47a9da6d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiNodeStageSecretRef",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "namespace": "namespace"},
)
class DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiNodeStageSecretRef:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#name DataKubernetesPersistentVolumeV1#name}
        :param namespace: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#namespace DataKubernetesPersistentVolumeV1#namespace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc6390703e69fa3ab6fb1603e58fae3f28bd97349f1ada3a77446436164ff949)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if namespace is not None:
            self._values["namespace"] = namespace

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#name DataKubernetesPersistentVolumeV1#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#namespace DataKubernetesPersistentVolumeV1#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiNodeStageSecretRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiNodeStageSecretRefOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiNodeStageSecretRefOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__24ccd060a25833975aa81efc8553c92b12c4a385a6440842ea6adb1bc2e64132)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

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
            type_hints = typing.get_type_hints(_typecheckingstub__22dccc53583e5ba5cd82594d0be3e132b094a4ce88e5714516ebf3e55355051b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0aaa602794b6e248d0aeab18edaee7ff86219427a55ffeeb2a2fac32d646fa67)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiNodeStageSecretRef]:
        return typing.cast(typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiNodeStageSecretRef], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiNodeStageSecretRef],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12916cc1fc155c8e0776636f16833446bb0b0bdc209f1d1561f269aba47d0d20)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f78446d608cad5f526dc06bdddbd9f08232b7cc50d58f31058547530d569beeb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putControllerExpandSecretRef")
    def put_controller_expand_secret_ref(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#name DataKubernetesPersistentVolumeV1#name}
        :param namespace: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#namespace DataKubernetesPersistentVolumeV1#namespace}
        '''
        value = DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiControllerExpandSecretRef(
            name=name, namespace=namespace
        )

        return typing.cast(None, jsii.invoke(self, "putControllerExpandSecretRef", [value]))

    @jsii.member(jsii_name="putControllerPublishSecretRef")
    def put_controller_publish_secret_ref(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#name DataKubernetesPersistentVolumeV1#name}
        :param namespace: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#namespace DataKubernetesPersistentVolumeV1#namespace}
        '''
        value = DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiControllerPublishSecretRef(
            name=name, namespace=namespace
        )

        return typing.cast(None, jsii.invoke(self, "putControllerPublishSecretRef", [value]))

    @jsii.member(jsii_name="putNodePublishSecretRef")
    def put_node_publish_secret_ref(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#name DataKubernetesPersistentVolumeV1#name}
        :param namespace: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#namespace DataKubernetesPersistentVolumeV1#namespace}
        '''
        value = DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiNodePublishSecretRef(
            name=name, namespace=namespace
        )

        return typing.cast(None, jsii.invoke(self, "putNodePublishSecretRef", [value]))

    @jsii.member(jsii_name="putNodeStageSecretRef")
    def put_node_stage_secret_ref(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#name DataKubernetesPersistentVolumeV1#name}
        :param namespace: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#namespace DataKubernetesPersistentVolumeV1#namespace}
        '''
        value = DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiNodeStageSecretRef(
            name=name, namespace=namespace
        )

        return typing.cast(None, jsii.invoke(self, "putNodeStageSecretRef", [value]))

    @jsii.member(jsii_name="resetControllerExpandSecretRef")
    def reset_controller_expand_secret_ref(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetControllerExpandSecretRef", []))

    @jsii.member(jsii_name="resetControllerPublishSecretRef")
    def reset_controller_publish_secret_ref(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetControllerPublishSecretRef", []))

    @jsii.member(jsii_name="resetFsType")
    def reset_fs_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFsType", []))

    @jsii.member(jsii_name="resetNodePublishSecretRef")
    def reset_node_publish_secret_ref(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodePublishSecretRef", []))

    @jsii.member(jsii_name="resetNodeStageSecretRef")
    def reset_node_stage_secret_ref(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodeStageSecretRef", []))

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @jsii.member(jsii_name="resetVolumeAttributes")
    def reset_volume_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolumeAttributes", []))

    @builtins.property
    @jsii.member(jsii_name="controllerExpandSecretRef")
    def controller_expand_secret_ref(
        self,
    ) -> DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiControllerExpandSecretRefOutputReference:
        return typing.cast(DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiControllerExpandSecretRefOutputReference, jsii.get(self, "controllerExpandSecretRef"))

    @builtins.property
    @jsii.member(jsii_name="controllerPublishSecretRef")
    def controller_publish_secret_ref(
        self,
    ) -> DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiControllerPublishSecretRefOutputReference:
        return typing.cast(DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiControllerPublishSecretRefOutputReference, jsii.get(self, "controllerPublishSecretRef"))

    @builtins.property
    @jsii.member(jsii_name="nodePublishSecretRef")
    def node_publish_secret_ref(
        self,
    ) -> DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiNodePublishSecretRefOutputReference:
        return typing.cast(DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiNodePublishSecretRefOutputReference, jsii.get(self, "nodePublishSecretRef"))

    @builtins.property
    @jsii.member(jsii_name="nodeStageSecretRef")
    def node_stage_secret_ref(
        self,
    ) -> DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiNodeStageSecretRefOutputReference:
        return typing.cast(DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiNodeStageSecretRefOutputReference, jsii.get(self, "nodeStageSecretRef"))

    @builtins.property
    @jsii.member(jsii_name="controllerExpandSecretRefInput")
    def controller_expand_secret_ref_input(
        self,
    ) -> typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiControllerExpandSecretRef]:
        return typing.cast(typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiControllerExpandSecretRef], jsii.get(self, "controllerExpandSecretRefInput"))

    @builtins.property
    @jsii.member(jsii_name="controllerPublishSecretRefInput")
    def controller_publish_secret_ref_input(
        self,
    ) -> typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiControllerPublishSecretRef]:
        return typing.cast(typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiControllerPublishSecretRef], jsii.get(self, "controllerPublishSecretRefInput"))

    @builtins.property
    @jsii.member(jsii_name="driverInput")
    def driver_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "driverInput"))

    @builtins.property
    @jsii.member(jsii_name="fsTypeInput")
    def fs_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fsTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="nodePublishSecretRefInput")
    def node_publish_secret_ref_input(
        self,
    ) -> typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiNodePublishSecretRef]:
        return typing.cast(typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiNodePublishSecretRef], jsii.get(self, "nodePublishSecretRefInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeStageSecretRefInput")
    def node_stage_secret_ref_input(
        self,
    ) -> typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiNodeStageSecretRef]:
        return typing.cast(typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiNodeStageSecretRef], jsii.get(self, "nodeStageSecretRefInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeAttributesInput")
    def volume_attributes_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "volumeAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeHandleInput")
    def volume_handle_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "volumeHandleInput"))

    @builtins.property
    @jsii.member(jsii_name="driver")
    def driver(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "driver"))

    @driver.setter
    def driver(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__815ee8d3d1292e57bb3e0ae293c898c8f091d82c536ca8e1da304ab2862df521)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "driver", value)

    @builtins.property
    @jsii.member(jsii_name="fsType")
    def fs_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fsType"))

    @fs_type.setter
    def fs_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dcdb53e7bf80a00a0cdf1f054398157263e43a8046cf584822fbd5e2318bcb86)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fsType", value)

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "readOnly"))

    @read_only.setter
    def read_only(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e06b7b301dd961bf33061880079f0895563b338641ec04e3f0f3e47493699fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="volumeAttributes")
    def volume_attributes(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "volumeAttributes"))

    @volume_attributes.setter
    def volume_attributes(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab2e77e3fc9bfff66c1fb8faa7bd95f30c624ed3de30b54e05fa7e6d80e58356)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeAttributes", value)

    @builtins.property
    @jsii.member(jsii_name="volumeHandle")
    def volume_handle(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volumeHandle"))

    @volume_handle.setter
    def volume_handle(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75285012f40ff74d2f23ee6fddb27928f28e35b0492db32d8708871fc2764ee4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeHandle", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsi]:
        return typing.cast(typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsi], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsi],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5f5e2a4871a7ba63e88f67b25b67fe05f0fc2ec120bb637b6a055a495286b23)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFc",
    jsii_struct_bases=[],
    name_mapping={
        "lun": "lun",
        "target_ww_ns": "targetWwNs",
        "fs_type": "fsType",
        "read_only": "readOnly",
    },
)
class DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFc:
    def __init__(
        self,
        *,
        lun: jsii.Number,
        target_ww_ns: typing.Sequence[builtins.str],
        fs_type: typing.Optional[builtins.str] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param lun: FC target lun number. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#lun DataKubernetesPersistentVolumeV1#lun}
        :param target_ww_ns: FC target worldwide names (WWNs). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#target_ww_ns DataKubernetesPersistentVolumeV1#target_ww_ns}
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#fs_type DataKubernetesPersistentVolumeV1#fs_type}
        :param read_only: Whether to force the read-only setting in VolumeMounts. Defaults to false (read/write). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#read_only DataKubernetesPersistentVolumeV1#read_only}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__734a0ec675ed8aded439a1244b00a9b34799d5fd8c2f8da587fdcddca24c9bdf)
            check_type(argname="argument lun", value=lun, expected_type=type_hints["lun"])
            check_type(argname="argument target_ww_ns", value=target_ww_ns, expected_type=type_hints["target_ww_ns"])
            check_type(argname="argument fs_type", value=fs_type, expected_type=type_hints["fs_type"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "lun": lun,
            "target_ww_ns": target_ww_ns,
        }
        if fs_type is not None:
            self._values["fs_type"] = fs_type
        if read_only is not None:
            self._values["read_only"] = read_only

    @builtins.property
    def lun(self) -> jsii.Number:
        '''FC target lun number.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#lun DataKubernetesPersistentVolumeV1#lun}
        '''
        result = self._values.get("lun")
        assert result is not None, "Required property 'lun' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def target_ww_ns(self) -> typing.List[builtins.str]:
        '''FC target worldwide names (WWNs).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#target_ww_ns DataKubernetesPersistentVolumeV1#target_ww_ns}
        '''
        result = self._values.get("target_ww_ns")
        assert result is not None, "Required property 'target_ww_ns' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def fs_type(self) -> typing.Optional[builtins.str]:
        '''Filesystem type to mount.

        Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#fs_type DataKubernetesPersistentVolumeV1#fs_type}
        '''
        result = self._values.get("fs_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to force the read-only setting in VolumeMounts. Defaults to false (read/write).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#read_only DataKubernetesPersistentVolumeV1#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFc(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFcOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFcOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2af07bdbe4c4a26523a9ca8e942e3a0e5367798a227733ecbcd7165591e6a1c7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFsType")
    def reset_fs_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFsType", []))

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @builtins.property
    @jsii.member(jsii_name="fsTypeInput")
    def fs_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fsTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="lunInput")
    def lun_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "lunInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="targetWwNsInput")
    def target_ww_ns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "targetWwNsInput"))

    @builtins.property
    @jsii.member(jsii_name="fsType")
    def fs_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fsType"))

    @fs_type.setter
    def fs_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__244833c926e090c48cad82151e81f861aaca72a0eb13d3ef7480778bbd9589a3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fsType", value)

    @builtins.property
    @jsii.member(jsii_name="lun")
    def lun(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "lun"))

    @lun.setter
    def lun(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4fdda6dede5bd3443c941f9f4ef463bfb75ae6c7d36af354eb17e3b0b2267fb9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lun", value)

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "readOnly"))

    @read_only.setter
    def read_only(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efe316a2feaac1f539d881e8b7fccee1b4f321009d2ab589590aadc5657c8f0b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="targetWwNs")
    def target_ww_ns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "targetWwNs"))

    @target_ww_ns.setter
    def target_ww_ns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d813d87a633e6bc299c4c947a5a3ae11beb63e47c4481a2a08c99d210b6e3ea8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetWwNs", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFc]:
        return typing.cast(typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFc], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFc],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0edc8e65d3b2ccff8fa8dd5ecb432b32ed64c77caae1683604c286257de1f88)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlexVolume",
    jsii_struct_bases=[],
    name_mapping={
        "driver": "driver",
        "fs_type": "fsType",
        "options": "options",
        "read_only": "readOnly",
        "secret_ref": "secretRef",
    },
)
class DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlexVolume:
    def __init__(
        self,
        *,
        driver: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        secret_ref: typing.Optional[typing.Union["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeSecretRef", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param driver: Driver is the name of the driver to use for this volume. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#driver DataKubernetesPersistentVolumeV1#driver}
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The default filesystem depends on FlexVolume script. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#fs_type DataKubernetesPersistentVolumeV1#fs_type}
        :param options: Extra command options if any. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#options DataKubernetesPersistentVolumeV1#options}
        :param read_only: Whether to force the ReadOnly setting in VolumeMounts. Defaults to false (read/write). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#read_only DataKubernetesPersistentVolumeV1#read_only}
        :param secret_ref: secret_ref block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#secret_ref DataKubernetesPersistentVolumeV1#secret_ref}
        '''
        if isinstance(secret_ref, dict):
            secret_ref = DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeSecretRef(**secret_ref)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c64e3c574c49544d7b3e0ff9f906763ec9de9a632e1d98dca3240857ffd62a4b)
            check_type(argname="argument driver", value=driver, expected_type=type_hints["driver"])
            check_type(argname="argument fs_type", value=fs_type, expected_type=type_hints["fs_type"])
            check_type(argname="argument options", value=options, expected_type=type_hints["options"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
            check_type(argname="argument secret_ref", value=secret_ref, expected_type=type_hints["secret_ref"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "driver": driver,
        }
        if fs_type is not None:
            self._values["fs_type"] = fs_type
        if options is not None:
            self._values["options"] = options
        if read_only is not None:
            self._values["read_only"] = read_only
        if secret_ref is not None:
            self._values["secret_ref"] = secret_ref

    @builtins.property
    def driver(self) -> builtins.str:
        '''Driver is the name of the driver to use for this volume.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#driver DataKubernetesPersistentVolumeV1#driver}
        '''
        result = self._values.get("driver")
        assert result is not None, "Required property 'driver' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def fs_type(self) -> typing.Optional[builtins.str]:
        '''Filesystem type to mount.

        Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The default filesystem depends on FlexVolume script.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#fs_type DataKubernetesPersistentVolumeV1#fs_type}
        '''
        result = self._values.get("fs_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def options(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Extra command options if any.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#options DataKubernetesPersistentVolumeV1#options}
        '''
        result = self._values.get("options")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to force the ReadOnly setting in VolumeMounts. Defaults to false (read/write).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#read_only DataKubernetesPersistentVolumeV1#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def secret_ref(
        self,
    ) -> typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeSecretRef"]:
        '''secret_ref block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#secret_ref DataKubernetesPersistentVolumeV1#secret_ref}
        '''
        result = self._values.get("secret_ref")
        return typing.cast(typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeSecretRef"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlexVolume(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9f7499d35f2687f4cb85bb1ac62cbefe3a139b4bba5c7d92cd6b06ab747697dd)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSecretRef")
    def put_secret_ref(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#name DataKubernetesPersistentVolumeV1#name}
        :param namespace: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#namespace DataKubernetesPersistentVolumeV1#namespace}
        '''
        value = DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeSecretRef(
            name=name, namespace=namespace
        )

        return typing.cast(None, jsii.invoke(self, "putSecretRef", [value]))

    @jsii.member(jsii_name="resetFsType")
    def reset_fs_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFsType", []))

    @jsii.member(jsii_name="resetOptions")
    def reset_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOptions", []))

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @jsii.member(jsii_name="resetSecretRef")
    def reset_secret_ref(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretRef", []))

    @builtins.property
    @jsii.member(jsii_name="secretRef")
    def secret_ref(
        self,
    ) -> "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeSecretRefOutputReference":
        return typing.cast("DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeSecretRefOutputReference", jsii.get(self, "secretRef"))

    @builtins.property
    @jsii.member(jsii_name="driverInput")
    def driver_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "driverInput"))

    @builtins.property
    @jsii.member(jsii_name="fsTypeInput")
    def fs_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fsTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="optionsInput")
    def options_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "optionsInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="secretRefInput")
    def secret_ref_input(
        self,
    ) -> typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeSecretRef"]:
        return typing.cast(typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeSecretRef"], jsii.get(self, "secretRefInput"))

    @builtins.property
    @jsii.member(jsii_name="driver")
    def driver(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "driver"))

    @driver.setter
    def driver(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__307aa899a7fa60f8305d4d4c2faba291e625f0dc01b7a02979cf29259b99490f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "driver", value)

    @builtins.property
    @jsii.member(jsii_name="fsType")
    def fs_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fsType"))

    @fs_type.setter
    def fs_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__391e133bf69252f478056c44ddbeef2b2d765ed6992a106bf9380339c84d4ff9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fsType", value)

    @builtins.property
    @jsii.member(jsii_name="options")
    def options(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "options"))

    @options.setter
    def options(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d8c064f8e2177481f4a60078b13760a08c8d3d4cb5f7198ffceab3eb27f09cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "options", value)

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "readOnly"))

    @read_only.setter
    def read_only(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f589b3d740c0ef5097bf040f98994d314515ab9e371ac25c416f581fae070003)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlexVolume]:
        return typing.cast(typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlexVolume], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlexVolume],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea120be9558bb894319207528296aa750f920723db87c2d8cd7fd81a1a8f25b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeSecretRef",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "namespace": "namespace"},
)
class DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeSecretRef:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#name DataKubernetesPersistentVolumeV1#name}
        :param namespace: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#namespace DataKubernetesPersistentVolumeV1#namespace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf9bab4cddb22a51bbfc10d541d1a365f2ab5d36fcb3acdf693ea98baced07e5)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if namespace is not None:
            self._values["namespace"] = namespace

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#name DataKubernetesPersistentVolumeV1#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#namespace DataKubernetesPersistentVolumeV1#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeSecretRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeSecretRefOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeSecretRefOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__659612f6de6e28a6b469cb05aa7ddc1a2e4755004b8897cf446b8be1d9fc87c4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

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
            type_hints = typing.get_type_hints(_typecheckingstub__5f5529b453cba46b7fbcb55b6652018bd96aeb8412e4a837583d6ecc87579bc6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2bbf49b89908c88f441e712373b310a1aea8c62e0e29fb7c4bdede61162a497)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeSecretRef]:
        return typing.cast(typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeSecretRef], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeSecretRef],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4112d00099c8438eab5bdd54986db92a27a74d30ce06d5c859f3159bd4ebf13)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlocker",
    jsii_struct_bases=[],
    name_mapping={"dataset_name": "datasetName", "dataset_uuid": "datasetUuid"},
)
class DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlocker:
    def __init__(
        self,
        *,
        dataset_name: typing.Optional[builtins.str] = None,
        dataset_uuid: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param dataset_name: Name of the dataset stored as metadata -> name on the dataset for Flocker should be considered as deprecated. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#dataset_name DataKubernetesPersistentVolumeV1#dataset_name}
        :param dataset_uuid: UUID of the dataset. This is unique identifier of a Flocker dataset. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#dataset_uuid DataKubernetesPersistentVolumeV1#dataset_uuid}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__174a60ac62c2497a02b62c642c8b5b59bb614f8cf627c84caeee32c6c4ee5adf)
            check_type(argname="argument dataset_name", value=dataset_name, expected_type=type_hints["dataset_name"])
            check_type(argname="argument dataset_uuid", value=dataset_uuid, expected_type=type_hints["dataset_uuid"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if dataset_name is not None:
            self._values["dataset_name"] = dataset_name
        if dataset_uuid is not None:
            self._values["dataset_uuid"] = dataset_uuid

    @builtins.property
    def dataset_name(self) -> typing.Optional[builtins.str]:
        '''Name of the dataset stored as metadata -> name on the dataset for Flocker should be considered as deprecated.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#dataset_name DataKubernetesPersistentVolumeV1#dataset_name}
        '''
        result = self._values.get("dataset_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dataset_uuid(self) -> typing.Optional[builtins.str]:
        '''UUID of the dataset. This is unique identifier of a Flocker dataset.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#dataset_uuid DataKubernetesPersistentVolumeV1#dataset_uuid}
        '''
        result = self._values.get("dataset_uuid")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlocker(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlockerOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlockerOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__313792389b79b77ba18552e8665e5e0076e280f084e7ffed99095fa59a622acb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDatasetName")
    def reset_dataset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatasetName", []))

    @jsii.member(jsii_name="resetDatasetUuid")
    def reset_dataset_uuid(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatasetUuid", []))

    @builtins.property
    @jsii.member(jsii_name="datasetNameInput")
    def dataset_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datasetNameInput"))

    @builtins.property
    @jsii.member(jsii_name="datasetUuidInput")
    def dataset_uuid_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datasetUuidInput"))

    @builtins.property
    @jsii.member(jsii_name="datasetName")
    def dataset_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datasetName"))

    @dataset_name.setter
    def dataset_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3fd249d9393404e55d0ab5e0855fec1257a4bd672a9c022e712e42b385aa67ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasetName", value)

    @builtins.property
    @jsii.member(jsii_name="datasetUuid")
    def dataset_uuid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datasetUuid"))

    @dataset_uuid.setter
    def dataset_uuid(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8f25ea600663cf48db7aec27fd4a5f6d7970a5ce0cfadc8a131102eb407aabf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasetUuid", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlocker]:
        return typing.cast(typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlocker], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlocker],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__425f18743b5173c10cd31a6c840e26c7ff8d9cefc46f2d75ba2a8daadb1bf9a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceGcePersistentDisk",
    jsii_struct_bases=[],
    name_mapping={
        "pd_name": "pdName",
        "fs_type": "fsType",
        "partition": "partition",
        "read_only": "readOnly",
    },
)
class DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceGcePersistentDisk:
    def __init__(
        self,
        *,
        pd_name: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        partition: typing.Optional[jsii.Number] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param pd_name: Unique name of the PD resource in GCE. Used to identify the disk in GCE. More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#pd_name DataKubernetesPersistentVolumeV1#pd_name}
        :param fs_type: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#fs_type DataKubernetesPersistentVolumeV1#fs_type}
        :param partition: The partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#partition DataKubernetesPersistentVolumeV1#partition}
        :param read_only: Whether to force the ReadOnly setting in VolumeMounts. Defaults to false. More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#read_only DataKubernetesPersistentVolumeV1#read_only}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bceb8d8c32fac051598f31a10990762241ed709ee041c0b9a5c13e12504e3996)
            check_type(argname="argument pd_name", value=pd_name, expected_type=type_hints["pd_name"])
            check_type(argname="argument fs_type", value=fs_type, expected_type=type_hints["fs_type"])
            check_type(argname="argument partition", value=partition, expected_type=type_hints["partition"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "pd_name": pd_name,
        }
        if fs_type is not None:
            self._values["fs_type"] = fs_type
        if partition is not None:
            self._values["partition"] = partition
        if read_only is not None:
            self._values["read_only"] = read_only

    @builtins.property
    def pd_name(self) -> builtins.str:
        '''Unique name of the PD resource in GCE. Used to identify the disk in GCE. More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#pd_name DataKubernetesPersistentVolumeV1#pd_name}
        '''
        result = self._values.get("pd_name")
        assert result is not None, "Required property 'pd_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def fs_type(self) -> typing.Optional[builtins.str]:
        '''Filesystem type of the volume that you want to mount.

        Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#fs_type DataKubernetesPersistentVolumeV1#fs_type}
        '''
        result = self._values.get("fs_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def partition(self) -> typing.Optional[jsii.Number]:
        '''The partition in the volume that you want to mount.

        If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#partition DataKubernetesPersistentVolumeV1#partition}
        '''
        result = self._values.get("partition")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to force the ReadOnly setting in VolumeMounts. Defaults to false. More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#read_only DataKubernetesPersistentVolumeV1#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceGcePersistentDisk(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceGcePersistentDiskOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceGcePersistentDiskOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9c4cfd3f659728a12d77921736b2f931e200e0ae2d64c77f0effdaf0ce12e5c8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFsType")
    def reset_fs_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFsType", []))

    @jsii.member(jsii_name="resetPartition")
    def reset_partition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPartition", []))

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @builtins.property
    @jsii.member(jsii_name="fsTypeInput")
    def fs_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fsTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="partitionInput")
    def partition_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "partitionInput"))

    @builtins.property
    @jsii.member(jsii_name="pdNameInput")
    def pd_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pdNameInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="fsType")
    def fs_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fsType"))

    @fs_type.setter
    def fs_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8db1550f3fc2dfe8f98aa5e7d50294fd6abe166d61ac0566a9a4335b36b113ca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fsType", value)

    @builtins.property
    @jsii.member(jsii_name="partition")
    def partition(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "partition"))

    @partition.setter
    def partition(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af14d6391891659d266026fdb1861dabb5b81e609238b5c9d946238d57eab503)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "partition", value)

    @builtins.property
    @jsii.member(jsii_name="pdName")
    def pd_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pdName"))

    @pd_name.setter
    def pd_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09206653490521ba1ccaee088c42ad53d3bff2863c8b27f863e63ba27cce9b60)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pdName", value)

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "readOnly"))

    @read_only.setter
    def read_only(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0df4b0574d232374d06ecbb05a8442a6b0e175e344f144d4f4fc30589155b6b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceGcePersistentDisk]:
        return typing.cast(typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceGcePersistentDisk], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceGcePersistentDisk],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c652c8187906a5879b23334eaff956d00893957c334132a8c7798bf2be4045fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceGlusterfs",
    jsii_struct_bases=[],
    name_mapping={
        "endpoints_name": "endpointsName",
        "path": "path",
        "read_only": "readOnly",
    },
)
class DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceGlusterfs:
    def __init__(
        self,
        *,
        endpoints_name: builtins.str,
        path: builtins.str,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param endpoints_name: The endpoint name that details Glusterfs topology. More info: http://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md#create-a-pod. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#endpoints_name DataKubernetesPersistentVolumeV1#endpoints_name}
        :param path: The Glusterfs volume path. More info: http://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md#create-a-pod. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#path DataKubernetesPersistentVolumeV1#path}
        :param read_only: Whether to force the Glusterfs volume to be mounted with read-only permissions. Defaults to false. More info: http://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md#create-a-pod. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#read_only DataKubernetesPersistentVolumeV1#read_only}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__782d8ea383b004ce0275f91289514b69b3dbcf9554ccbacd2587a6c90ba31e59)
            check_type(argname="argument endpoints_name", value=endpoints_name, expected_type=type_hints["endpoints_name"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "endpoints_name": endpoints_name,
            "path": path,
        }
        if read_only is not None:
            self._values["read_only"] = read_only

    @builtins.property
    def endpoints_name(self) -> builtins.str:
        '''The endpoint name that details Glusterfs topology. More info: http://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md#create-a-pod.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#endpoints_name DataKubernetesPersistentVolumeV1#endpoints_name}
        '''
        result = self._values.get("endpoints_name")
        assert result is not None, "Required property 'endpoints_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> builtins.str:
        '''The Glusterfs volume path. More info: http://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md#create-a-pod.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#path DataKubernetesPersistentVolumeV1#path}
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to force the Glusterfs volume to be mounted with read-only permissions. Defaults to false. More info: http://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md#create-a-pod.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#read_only DataKubernetesPersistentVolumeV1#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceGlusterfs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceGlusterfsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceGlusterfsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fb76a3266bebec7cbfc9883a065e33317b16f03e858fc38bc01862f1bb72a1c0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @builtins.property
    @jsii.member(jsii_name="endpointsNameInput")
    def endpoints_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointsNameInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointsName")
    def endpoints_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpointsName"))

    @endpoints_name.setter
    def endpoints_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1c2922bd3a483abb2241b47f15e42694f9bc6c71739c5a5e65d068f0e7487eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpointsName", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea07f1fe51a145addc65cf5c881f25d982ab8b37218601647c1c1974445e3ecb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "readOnly"))

    @read_only.setter
    def read_only(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7a42fc9c4f24d6e77845d1625c37809fa4ac0b5976e0925c0505f3a8726a845)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceGlusterfs]:
        return typing.cast(typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceGlusterfs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceGlusterfs],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75ac70738dc84eb8e9e531f1f175ffcfb07f9380738f4502f4464f8d3b393165)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceHostPath",
    jsii_struct_bases=[],
    name_mapping={"path": "path", "type": "type"},
)
class DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceHostPath:
    def __init__(
        self,
        *,
        path: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param path: Path of the directory on the host. More info: http://kubernetes.io/docs/user-guide/volumes#hostpath. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#path DataKubernetesPersistentVolumeV1#path}
        :param type: Type for HostPath volume. Allowed values are "" (default), DirectoryOrCreate, Directory, FileOrCreate, File, Socket, CharDevice and BlockDevice. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#type DataKubernetesPersistentVolumeV1#type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cac55bdba17cef547f2dd204e83aa8d306a0be4e4ab2faa47dfd3687f610826e)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if path is not None:
            self._values["path"] = path
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Path of the directory on the host. More info: http://kubernetes.io/docs/user-guide/volumes#hostpath.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#path DataKubernetesPersistentVolumeV1#path}
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Type for HostPath volume. Allowed values are "" (default), DirectoryOrCreate, Directory, FileOrCreate, File, Socket, CharDevice and BlockDevice.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#type DataKubernetesPersistentVolumeV1#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceHostPath(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceHostPathOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceHostPathOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__44323cc6d7f21f65b0a158d4dc13aaae6b1fcdc9c058d91ec3dbfeaeae0e02bf)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6723916cc813d1878aaf30ab89a3428da685018d7a65fa63bd9699bd38eb7455)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ce2a71e4de54d36823594e9713349263b3bcbff16fa06ae66b5bc58eb01bdb7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceHostPath]:
        return typing.cast(typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceHostPath], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceHostPath],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c3bcae10bed0d653a8ef3a49e72191778dbcf050f8ad4b7b7e19801c57c7a3f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceIscsi",
    jsii_struct_bases=[],
    name_mapping={
        "iqn": "iqn",
        "target_portal": "targetPortal",
        "fs_type": "fsType",
        "iscsi_interface": "iscsiInterface",
        "lun": "lun",
        "read_only": "readOnly",
    },
)
class DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceIscsi:
    def __init__(
        self,
        *,
        iqn: builtins.str,
        target_portal: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        iscsi_interface: typing.Optional[builtins.str] = None,
        lun: typing.Optional[jsii.Number] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param iqn: Target iSCSI Qualified Name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#iqn DataKubernetesPersistentVolumeV1#iqn}
        :param target_portal: iSCSI target portal. The portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#target_portal DataKubernetesPersistentVolumeV1#target_portal}
        :param fs_type: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: http://kubernetes.io/docs/user-guide/volumes#iscsi Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#fs_type DataKubernetesPersistentVolumeV1#fs_type}
        :param iscsi_interface: iSCSI interface name that uses an iSCSI transport. Defaults to 'default' (tcp). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#iscsi_interface DataKubernetesPersistentVolumeV1#iscsi_interface}
        :param lun: iSCSI target lun number. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#lun DataKubernetesPersistentVolumeV1#lun}
        :param read_only: Whether to force the read-only setting in VolumeMounts. Defaults to false. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#read_only DataKubernetesPersistentVolumeV1#read_only}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc6889c860859f093cb665fb948824eb2e7075ddc1d44e252649bafa2293691e)
            check_type(argname="argument iqn", value=iqn, expected_type=type_hints["iqn"])
            check_type(argname="argument target_portal", value=target_portal, expected_type=type_hints["target_portal"])
            check_type(argname="argument fs_type", value=fs_type, expected_type=type_hints["fs_type"])
            check_type(argname="argument iscsi_interface", value=iscsi_interface, expected_type=type_hints["iscsi_interface"])
            check_type(argname="argument lun", value=lun, expected_type=type_hints["lun"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "iqn": iqn,
            "target_portal": target_portal,
        }
        if fs_type is not None:
            self._values["fs_type"] = fs_type
        if iscsi_interface is not None:
            self._values["iscsi_interface"] = iscsi_interface
        if lun is not None:
            self._values["lun"] = lun
        if read_only is not None:
            self._values["read_only"] = read_only

    @builtins.property
    def iqn(self) -> builtins.str:
        '''Target iSCSI Qualified Name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#iqn DataKubernetesPersistentVolumeV1#iqn}
        '''
        result = self._values.get("iqn")
        assert result is not None, "Required property 'iqn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_portal(self) -> builtins.str:
        '''iSCSI target portal.

        The portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#target_portal DataKubernetesPersistentVolumeV1#target_portal}
        '''
        result = self._values.get("target_portal")
        assert result is not None, "Required property 'target_portal' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def fs_type(self) -> typing.Optional[builtins.str]:
        '''Filesystem type of the volume that you want to mount.

        Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: http://kubernetes.io/docs/user-guide/volumes#iscsi

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#fs_type DataKubernetesPersistentVolumeV1#fs_type}
        '''
        result = self._values.get("fs_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iscsi_interface(self) -> typing.Optional[builtins.str]:
        '''iSCSI interface name that uses an iSCSI transport. Defaults to 'default' (tcp).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#iscsi_interface DataKubernetesPersistentVolumeV1#iscsi_interface}
        '''
        result = self._values.get("iscsi_interface")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lun(self) -> typing.Optional[jsii.Number]:
        '''iSCSI target lun number.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#lun DataKubernetesPersistentVolumeV1#lun}
        '''
        result = self._values.get("lun")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to force the read-only setting in VolumeMounts. Defaults to false.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#read_only DataKubernetesPersistentVolumeV1#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceIscsi(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceIscsiOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceIscsiOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1ba4ca622f989c50926546da7e784abd417ce086713248f7ece3c3d1f2163ea5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFsType")
    def reset_fs_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFsType", []))

    @jsii.member(jsii_name="resetIscsiInterface")
    def reset_iscsi_interface(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIscsiInterface", []))

    @jsii.member(jsii_name="resetLun")
    def reset_lun(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLun", []))

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @builtins.property
    @jsii.member(jsii_name="fsTypeInput")
    def fs_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fsTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="iqnInput")
    def iqn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "iqnInput"))

    @builtins.property
    @jsii.member(jsii_name="iscsiInterfaceInput")
    def iscsi_interface_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "iscsiInterfaceInput"))

    @builtins.property
    @jsii.member(jsii_name="lunInput")
    def lun_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "lunInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="targetPortalInput")
    def target_portal_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetPortalInput"))

    @builtins.property
    @jsii.member(jsii_name="fsType")
    def fs_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fsType"))

    @fs_type.setter
    def fs_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c06735dbfbf7aa17ac01b497d1e6ea80a5093ae573d5c65a1b1af196af5654e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fsType", value)

    @builtins.property
    @jsii.member(jsii_name="iqn")
    def iqn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "iqn"))

    @iqn.setter
    def iqn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac327e636947eeb194bc232ad0c24fe1330a79675579fec45e2b8b623625f6d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iqn", value)

    @builtins.property
    @jsii.member(jsii_name="iscsiInterface")
    def iscsi_interface(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "iscsiInterface"))

    @iscsi_interface.setter
    def iscsi_interface(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3204a1c55301427324f4903dacbdbe3d799c1d49c87980440c2ddd6b535740b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iscsiInterface", value)

    @builtins.property
    @jsii.member(jsii_name="lun")
    def lun(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "lun"))

    @lun.setter
    def lun(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e5943d9cd3efabece4b26a8b1d143e0ac7a819b7d02777976cb3b7d540e7d5e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lun", value)

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "readOnly"))

    @read_only.setter
    def read_only(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4bdad44adaacfa338806ebeed891f866e702eed535da11c73c1d583d8589cf8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="targetPortal")
    def target_portal(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetPortal"))

    @target_portal.setter
    def target_portal(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2e2f04d7f58ab6ed8de07fe9c103526f5ba3810cffe4cd38942c58f751ed2fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetPortal", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceIscsi]:
        return typing.cast(typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceIscsi], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceIscsi],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08c2d374e4c62ebdd19d71d171bfd4946b7b46529fbc2e16e7aaaf72f3fa9786)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceLocal",
    jsii_struct_bases=[],
    name_mapping={"path": "path"},
)
class DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceLocal:
    def __init__(self, *, path: typing.Optional[builtins.str] = None) -> None:
        '''
        :param path: Path of the directory on the host. More info: http://kubernetes.io/docs/user-guide/volumes#local. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#path DataKubernetesPersistentVolumeV1#path}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e409bed12e5554bf4d137e1031330785736c3c0902a66f3d09da1392e1ddbbc1)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if path is not None:
            self._values["path"] = path

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Path of the directory on the host. More info: http://kubernetes.io/docs/user-guide/volumes#local.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#path DataKubernetesPersistentVolumeV1#path}
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceLocal(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceLocalOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceLocalOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__157a24630a91bc14435bb8e806205db3d42ad77a20428e38ccadef759ceb097c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d1e2c398e980dafaa72397f4c5c6924c5fe2c97a4a328c7b55b708cfa8828a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceLocal]:
        return typing.cast(typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceLocal], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceLocal],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3cfc2f527519a8930aed66240e063abb14cd0eb2f4ea7d6a3ae3ea0b0e1b34b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceNfs",
    jsii_struct_bases=[],
    name_mapping={"path": "path", "server": "server", "read_only": "readOnly"},
)
class DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceNfs:
    def __init__(
        self,
        *,
        path: builtins.str,
        server: builtins.str,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param path: Path that is exported by the NFS server. More info: http://kubernetes.io/docs/user-guide/volumes#nfs. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#path DataKubernetesPersistentVolumeV1#path}
        :param server: Server is the hostname or IP address of the NFS server. More info: http://kubernetes.io/docs/user-guide/volumes#nfs. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#server DataKubernetesPersistentVolumeV1#server}
        :param read_only: Whether to force the NFS export to be mounted with read-only permissions. Defaults to false. More info: http://kubernetes.io/docs/user-guide/volumes#nfs. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#read_only DataKubernetesPersistentVolumeV1#read_only}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13498673ceae143fa31f6141f0699191b409c6f87b45b19a01ccad8ad20d3aa7)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument server", value=server, expected_type=type_hints["server"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "path": path,
            "server": server,
        }
        if read_only is not None:
            self._values["read_only"] = read_only

    @builtins.property
    def path(self) -> builtins.str:
        '''Path that is exported by the NFS server. More info: http://kubernetes.io/docs/user-guide/volumes#nfs.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#path DataKubernetesPersistentVolumeV1#path}
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def server(self) -> builtins.str:
        '''Server is the hostname or IP address of the NFS server. More info: http://kubernetes.io/docs/user-guide/volumes#nfs.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#server DataKubernetesPersistentVolumeV1#server}
        '''
        result = self._values.get("server")
        assert result is not None, "Required property 'server' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to force the NFS export to be mounted with read-only permissions. Defaults to false. More info: http://kubernetes.io/docs/user-guide/volumes#nfs.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#read_only DataKubernetesPersistentVolumeV1#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceNfs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceNfsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceNfsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__21167250b0e5ff3345fec53625853d0b44f66d4fa6dfe3cda5f0f8dcbc19ff43)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="serverInput")
    def server_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverInput"))

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac69ed966e39bd9fa5fc75587bc35e73c5ca6c19a5db14d270ccf5a553556dba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "readOnly"))

    @read_only.setter
    def read_only(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ccb149f7814dc012c1289282bcab5d69c4dcbc4867b6f68a5cbcce46695cfd8b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="server")
    def server(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "server"))

    @server.setter
    def server(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3dc99563e6bd902629222147e123624c707cdf1f5dc50c82a7ab2a58020190a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "server", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceNfs]:
        return typing.cast(typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceNfs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceNfs],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab2d1ee45272767e2b4dea846d4baf925a1174a9d24a6ea477cbfc2e7ec2b3f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6f0d918c7e23ad59464986451f7af63da4bc4f4c97dc58b31ed61b48be98f42b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAwsElasticBlockStore")
    def put_aws_elastic_block_store(
        self,
        *,
        volume_id: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        partition: typing.Optional[jsii.Number] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param volume_id: Unique ID of the persistent disk resource in AWS (Amazon EBS volume). More info: http://kubernetes.io/docs/user-guide/volumes#awselasticblockstore. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#volume_id DataKubernetesPersistentVolumeV1#volume_id}
        :param fs_type: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: http://kubernetes.io/docs/user-guide/volumes#awselasticblockstore Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#fs_type DataKubernetesPersistentVolumeV1#fs_type}
        :param partition: The partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#partition DataKubernetesPersistentVolumeV1#partition}
        :param read_only: Whether to set the read-only property in VolumeMounts to "true". If omitted, the default is "false". More info: http://kubernetes.io/docs/user-guide/volumes#awselasticblockstore. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#read_only DataKubernetesPersistentVolumeV1#read_only}
        '''
        value = DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAwsElasticBlockStore(
            volume_id=volume_id,
            fs_type=fs_type,
            partition=partition,
            read_only=read_only,
        )

        return typing.cast(None, jsii.invoke(self, "putAwsElasticBlockStore", [value]))

    @jsii.member(jsii_name="putAzureDisk")
    def put_azure_disk(
        self,
        *,
        caching_mode: builtins.str,
        data_disk_uri: builtins.str,
        disk_name: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        kind: typing.Optional[builtins.str] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param caching_mode: Host Caching mode: None, Read Only, Read Write. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#caching_mode DataKubernetesPersistentVolumeV1#caching_mode}
        :param data_disk_uri: The URI the data disk in the blob storage. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#data_disk_uri DataKubernetesPersistentVolumeV1#data_disk_uri}
        :param disk_name: The Name of the data disk in the blob storage. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#disk_name DataKubernetesPersistentVolumeV1#disk_name}
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#fs_type DataKubernetesPersistentVolumeV1#fs_type}
        :param kind: The type for the data disk. Expected values: Shared, Dedicated, Managed. Defaults to Shared. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#kind DataKubernetesPersistentVolumeV1#kind}
        :param read_only: Whether to force the read-only setting in VolumeMounts. Defaults to false (read/write). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#read_only DataKubernetesPersistentVolumeV1#read_only}
        '''
        value = DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAzureDisk(
            caching_mode=caching_mode,
            data_disk_uri=data_disk_uri,
            disk_name=disk_name,
            fs_type=fs_type,
            kind=kind,
            read_only=read_only,
        )

        return typing.cast(None, jsii.invoke(self, "putAzureDisk", [value]))

    @jsii.member(jsii_name="putAzureFile")
    def put_azure_file(
        self,
        *,
        secret_name: builtins.str,
        share_name: builtins.str,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        secret_namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param secret_name: The name of secret that contains Azure Storage Account Name and Key. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#secret_name DataKubernetesPersistentVolumeV1#secret_name}
        :param share_name: Share Name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#share_name DataKubernetesPersistentVolumeV1#share_name}
        :param read_only: Whether to force the read-only setting in VolumeMounts. Defaults to false (read/write). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#read_only DataKubernetesPersistentVolumeV1#read_only}
        :param secret_namespace: The namespace of the secret that contains Azure Storage Account Name and Key. For Kubernetes up to 1.18.x the default is the same as the Pod. For Kubernetes 1.19.x and later the default is "default" namespace. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#secret_namespace DataKubernetesPersistentVolumeV1#secret_namespace}
        '''
        value = DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAzureFile(
            secret_name=secret_name,
            share_name=share_name,
            read_only=read_only,
            secret_namespace=secret_namespace,
        )

        return typing.cast(None, jsii.invoke(self, "putAzureFile", [value]))

    @jsii.member(jsii_name="putCephFs")
    def put_ceph_fs(
        self,
        *,
        monitors: typing.Sequence[builtins.str],
        path: typing.Optional[builtins.str] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        secret_file: typing.Optional[builtins.str] = None,
        secret_ref: typing.Optional[typing.Union[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCephFsSecretRef, typing.Dict[builtins.str, typing.Any]]] = None,
        user: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param monitors: Monitors is a collection of Ceph monitors More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#monitors DataKubernetesPersistentVolumeV1#monitors}
        :param path: Used as the mounted root, rather than the full Ceph tree, default is /. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#path DataKubernetesPersistentVolumeV1#path}
        :param read_only: Whether to force the read-only setting in VolumeMounts. Defaults to ``false`` (read/write). More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#read_only DataKubernetesPersistentVolumeV1#read_only}
        :param secret_file: The path to key ring for User, default is /etc/ceph/user.secret More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#secret_file DataKubernetesPersistentVolumeV1#secret_file}
        :param secret_ref: secret_ref block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#secret_ref DataKubernetesPersistentVolumeV1#secret_ref}
        :param user: User is the rados user name, default is admin. More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#user DataKubernetesPersistentVolumeV1#user}
        '''
        value = DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCephFs(
            monitors=monitors,
            path=path,
            read_only=read_only,
            secret_file=secret_file,
            secret_ref=secret_ref,
            user=user,
        )

        return typing.cast(None, jsii.invoke(self, "putCephFs", [value]))

    @jsii.member(jsii_name="putCinder")
    def put_cinder(
        self,
        *,
        volume_id: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param volume_id: Volume ID used to identify the volume in Cinder. More info: http://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#volume_id DataKubernetesPersistentVolumeV1#volume_id}
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: http://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#fs_type DataKubernetesPersistentVolumeV1#fs_type}
        :param read_only: Whether to force the read-only setting in VolumeMounts. Defaults to false (read/write). More info: http://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#read_only DataKubernetesPersistentVolumeV1#read_only}
        '''
        value = DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCinder(
            volume_id=volume_id, fs_type=fs_type, read_only=read_only
        )

        return typing.cast(None, jsii.invoke(self, "putCinder", [value]))

    @jsii.member(jsii_name="putCsi")
    def put_csi(
        self,
        *,
        driver: builtins.str,
        volume_handle: builtins.str,
        controller_expand_secret_ref: typing.Optional[typing.Union[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiControllerExpandSecretRef, typing.Dict[builtins.str, typing.Any]]] = None,
        controller_publish_secret_ref: typing.Optional[typing.Union[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiControllerPublishSecretRef, typing.Dict[builtins.str, typing.Any]]] = None,
        fs_type: typing.Optional[builtins.str] = None,
        node_publish_secret_ref: typing.Optional[typing.Union[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiNodePublishSecretRef, typing.Dict[builtins.str, typing.Any]]] = None,
        node_stage_secret_ref: typing.Optional[typing.Union[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiNodeStageSecretRef, typing.Dict[builtins.str, typing.Any]]] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        volume_attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param driver: the name of the volume driver to use. More info: https://kubernetes.io/docs/concepts/storage/volumes/#csi. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#driver DataKubernetesPersistentVolumeV1#driver}
        :param volume_handle: A string value that uniquely identifies the volume. More info: https://kubernetes.io/docs/concepts/storage/volumes/#csi. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#volume_handle DataKubernetesPersistentVolumeV1#volume_handle}
        :param controller_expand_secret_ref: controller_expand_secret_ref block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#controller_expand_secret_ref DataKubernetesPersistentVolumeV1#controller_expand_secret_ref}
        :param controller_publish_secret_ref: controller_publish_secret_ref block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#controller_publish_secret_ref DataKubernetesPersistentVolumeV1#controller_publish_secret_ref}
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#fs_type DataKubernetesPersistentVolumeV1#fs_type}
        :param node_publish_secret_ref: node_publish_secret_ref block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#node_publish_secret_ref DataKubernetesPersistentVolumeV1#node_publish_secret_ref}
        :param node_stage_secret_ref: node_stage_secret_ref block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#node_stage_secret_ref DataKubernetesPersistentVolumeV1#node_stage_secret_ref}
        :param read_only: Whether to set the read-only property in VolumeMounts to "true". If omitted, the default is "false". More info: http://kubernetes.io/docs/user-guide/volumes#csi. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#read_only DataKubernetesPersistentVolumeV1#read_only}
        :param volume_attributes: Attributes of the volume to publish. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#volume_attributes DataKubernetesPersistentVolumeV1#volume_attributes}
        '''
        value = DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsi(
            driver=driver,
            volume_handle=volume_handle,
            controller_expand_secret_ref=controller_expand_secret_ref,
            controller_publish_secret_ref=controller_publish_secret_ref,
            fs_type=fs_type,
            node_publish_secret_ref=node_publish_secret_ref,
            node_stage_secret_ref=node_stage_secret_ref,
            read_only=read_only,
            volume_attributes=volume_attributes,
        )

        return typing.cast(None, jsii.invoke(self, "putCsi", [value]))

    @jsii.member(jsii_name="putFc")
    def put_fc(
        self,
        *,
        lun: jsii.Number,
        target_ww_ns: typing.Sequence[builtins.str],
        fs_type: typing.Optional[builtins.str] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param lun: FC target lun number. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#lun DataKubernetesPersistentVolumeV1#lun}
        :param target_ww_ns: FC target worldwide names (WWNs). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#target_ww_ns DataKubernetesPersistentVolumeV1#target_ww_ns}
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#fs_type DataKubernetesPersistentVolumeV1#fs_type}
        :param read_only: Whether to force the read-only setting in VolumeMounts. Defaults to false (read/write). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#read_only DataKubernetesPersistentVolumeV1#read_only}
        '''
        value = DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFc(
            lun=lun, target_ww_ns=target_ww_ns, fs_type=fs_type, read_only=read_only
        )

        return typing.cast(None, jsii.invoke(self, "putFc", [value]))

    @jsii.member(jsii_name="putFlexVolume")
    def put_flex_volume(
        self,
        *,
        driver: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        secret_ref: typing.Optional[typing.Union[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeSecretRef, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param driver: Driver is the name of the driver to use for this volume. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#driver DataKubernetesPersistentVolumeV1#driver}
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The default filesystem depends on FlexVolume script. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#fs_type DataKubernetesPersistentVolumeV1#fs_type}
        :param options: Extra command options if any. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#options DataKubernetesPersistentVolumeV1#options}
        :param read_only: Whether to force the ReadOnly setting in VolumeMounts. Defaults to false (read/write). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#read_only DataKubernetesPersistentVolumeV1#read_only}
        :param secret_ref: secret_ref block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#secret_ref DataKubernetesPersistentVolumeV1#secret_ref}
        '''
        value = DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlexVolume(
            driver=driver,
            fs_type=fs_type,
            options=options,
            read_only=read_only,
            secret_ref=secret_ref,
        )

        return typing.cast(None, jsii.invoke(self, "putFlexVolume", [value]))

    @jsii.member(jsii_name="putFlocker")
    def put_flocker(
        self,
        *,
        dataset_name: typing.Optional[builtins.str] = None,
        dataset_uuid: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param dataset_name: Name of the dataset stored as metadata -> name on the dataset for Flocker should be considered as deprecated. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#dataset_name DataKubernetesPersistentVolumeV1#dataset_name}
        :param dataset_uuid: UUID of the dataset. This is unique identifier of a Flocker dataset. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#dataset_uuid DataKubernetesPersistentVolumeV1#dataset_uuid}
        '''
        value = DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlocker(
            dataset_name=dataset_name, dataset_uuid=dataset_uuid
        )

        return typing.cast(None, jsii.invoke(self, "putFlocker", [value]))

    @jsii.member(jsii_name="putGcePersistentDisk")
    def put_gce_persistent_disk(
        self,
        *,
        pd_name: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        partition: typing.Optional[jsii.Number] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param pd_name: Unique name of the PD resource in GCE. Used to identify the disk in GCE. More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#pd_name DataKubernetesPersistentVolumeV1#pd_name}
        :param fs_type: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#fs_type DataKubernetesPersistentVolumeV1#fs_type}
        :param partition: The partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#partition DataKubernetesPersistentVolumeV1#partition}
        :param read_only: Whether to force the ReadOnly setting in VolumeMounts. Defaults to false. More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#read_only DataKubernetesPersistentVolumeV1#read_only}
        '''
        value = DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceGcePersistentDisk(
            pd_name=pd_name, fs_type=fs_type, partition=partition, read_only=read_only
        )

        return typing.cast(None, jsii.invoke(self, "putGcePersistentDisk", [value]))

    @jsii.member(jsii_name="putGlusterfs")
    def put_glusterfs(
        self,
        *,
        endpoints_name: builtins.str,
        path: builtins.str,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param endpoints_name: The endpoint name that details Glusterfs topology. More info: http://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md#create-a-pod. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#endpoints_name DataKubernetesPersistentVolumeV1#endpoints_name}
        :param path: The Glusterfs volume path. More info: http://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md#create-a-pod. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#path DataKubernetesPersistentVolumeV1#path}
        :param read_only: Whether to force the Glusterfs volume to be mounted with read-only permissions. Defaults to false. More info: http://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md#create-a-pod. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#read_only DataKubernetesPersistentVolumeV1#read_only}
        '''
        value = DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceGlusterfs(
            endpoints_name=endpoints_name, path=path, read_only=read_only
        )

        return typing.cast(None, jsii.invoke(self, "putGlusterfs", [value]))

    @jsii.member(jsii_name="putHostPath")
    def put_host_path(
        self,
        *,
        path: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param path: Path of the directory on the host. More info: http://kubernetes.io/docs/user-guide/volumes#hostpath. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#path DataKubernetesPersistentVolumeV1#path}
        :param type: Type for HostPath volume. Allowed values are "" (default), DirectoryOrCreate, Directory, FileOrCreate, File, Socket, CharDevice and BlockDevice. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#type DataKubernetesPersistentVolumeV1#type}
        '''
        value = DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceHostPath(
            path=path, type=type
        )

        return typing.cast(None, jsii.invoke(self, "putHostPath", [value]))

    @jsii.member(jsii_name="putIscsi")
    def put_iscsi(
        self,
        *,
        iqn: builtins.str,
        target_portal: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        iscsi_interface: typing.Optional[builtins.str] = None,
        lun: typing.Optional[jsii.Number] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param iqn: Target iSCSI Qualified Name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#iqn DataKubernetesPersistentVolumeV1#iqn}
        :param target_portal: iSCSI target portal. The portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#target_portal DataKubernetesPersistentVolumeV1#target_portal}
        :param fs_type: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: http://kubernetes.io/docs/user-guide/volumes#iscsi Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#fs_type DataKubernetesPersistentVolumeV1#fs_type}
        :param iscsi_interface: iSCSI interface name that uses an iSCSI transport. Defaults to 'default' (tcp). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#iscsi_interface DataKubernetesPersistentVolumeV1#iscsi_interface}
        :param lun: iSCSI target lun number. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#lun DataKubernetesPersistentVolumeV1#lun}
        :param read_only: Whether to force the read-only setting in VolumeMounts. Defaults to false. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#read_only DataKubernetesPersistentVolumeV1#read_only}
        '''
        value = DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceIscsi(
            iqn=iqn,
            target_portal=target_portal,
            fs_type=fs_type,
            iscsi_interface=iscsi_interface,
            lun=lun,
            read_only=read_only,
        )

        return typing.cast(None, jsii.invoke(self, "putIscsi", [value]))

    @jsii.member(jsii_name="putLocal")
    def put_local(self, *, path: typing.Optional[builtins.str] = None) -> None:
        '''
        :param path: Path of the directory on the host. More info: http://kubernetes.io/docs/user-guide/volumes#local. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#path DataKubernetesPersistentVolumeV1#path}
        '''
        value = DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceLocal(
            path=path
        )

        return typing.cast(None, jsii.invoke(self, "putLocal", [value]))

    @jsii.member(jsii_name="putNfs")
    def put_nfs(
        self,
        *,
        path: builtins.str,
        server: builtins.str,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param path: Path that is exported by the NFS server. More info: http://kubernetes.io/docs/user-guide/volumes#nfs. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#path DataKubernetesPersistentVolumeV1#path}
        :param server: Server is the hostname or IP address of the NFS server. More info: http://kubernetes.io/docs/user-guide/volumes#nfs. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#server DataKubernetesPersistentVolumeV1#server}
        :param read_only: Whether to force the NFS export to be mounted with read-only permissions. Defaults to false. More info: http://kubernetes.io/docs/user-guide/volumes#nfs. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#read_only DataKubernetesPersistentVolumeV1#read_only}
        '''
        value = DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceNfs(
            path=path, server=server, read_only=read_only
        )

        return typing.cast(None, jsii.invoke(self, "putNfs", [value]))

    @jsii.member(jsii_name="putPhotonPersistentDisk")
    def put_photon_persistent_disk(
        self,
        *,
        pd_id: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param pd_id: ID that identifies Photon Controller persistent disk. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#pd_id DataKubernetesPersistentVolumeV1#pd_id}
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#fs_type DataKubernetesPersistentVolumeV1#fs_type}
        '''
        value = DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourcePhotonPersistentDisk(
            pd_id=pd_id, fs_type=fs_type
        )

        return typing.cast(None, jsii.invoke(self, "putPhotonPersistentDisk", [value]))

    @jsii.member(jsii_name="putQuobyte")
    def put_quobyte(
        self,
        *,
        registry: builtins.str,
        volume: builtins.str,
        group: typing.Optional[builtins.str] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        user: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param registry: Registry represents a single or multiple Quobyte Registry services specified as a string as host:port pair (multiple entries are separated with commas) which acts as the central registry for volumes. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#registry DataKubernetesPersistentVolumeV1#registry}
        :param volume: Volume is a string that references an already created Quobyte volume by name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#volume DataKubernetesPersistentVolumeV1#volume}
        :param group: Group to map volume access to Default is no group. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#group DataKubernetesPersistentVolumeV1#group}
        :param read_only: Whether to force the Quobyte volume to be mounted with read-only permissions. Defaults to false. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#read_only DataKubernetesPersistentVolumeV1#read_only}
        :param user: User to map volume access to Defaults to serivceaccount user. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#user DataKubernetesPersistentVolumeV1#user}
        '''
        value = DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceQuobyte(
            registry=registry,
            volume=volume,
            group=group,
            read_only=read_only,
            user=user,
        )

        return typing.cast(None, jsii.invoke(self, "putQuobyte", [value]))

    @jsii.member(jsii_name="putRbd")
    def put_rbd(
        self,
        *,
        ceph_monitors: typing.Sequence[builtins.str],
        rbd_image: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        keyring: typing.Optional[builtins.str] = None,
        rados_user: typing.Optional[builtins.str] = None,
        rbd_pool: typing.Optional[builtins.str] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        secret_ref: typing.Optional[typing.Union["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceRbdSecretRef", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param ceph_monitors: A collection of Ceph monitors. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#ceph_monitors DataKubernetesPersistentVolumeV1#ceph_monitors}
        :param rbd_image: The rados image name. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#rbd_image DataKubernetesPersistentVolumeV1#rbd_image}
        :param fs_type: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: http://kubernetes.io/docs/user-guide/volumes#rbd Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#fs_type DataKubernetesPersistentVolumeV1#fs_type}
        :param keyring: Keyring is the path to key ring for RBDUser. Default is /etc/ceph/keyring. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#keyring DataKubernetesPersistentVolumeV1#keyring}
        :param rados_user: The rados user name. Default is admin. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#rados_user DataKubernetesPersistentVolumeV1#rados_user}
        :param rbd_pool: The rados pool name. Default is rbd. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#rbd_pool DataKubernetesPersistentVolumeV1#rbd_pool}
        :param read_only: Whether to force the read-only setting in VolumeMounts. Defaults to false. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#read_only DataKubernetesPersistentVolumeV1#read_only}
        :param secret_ref: secret_ref block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#secret_ref DataKubernetesPersistentVolumeV1#secret_ref}
        '''
        value = DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceRbd(
            ceph_monitors=ceph_monitors,
            rbd_image=rbd_image,
            fs_type=fs_type,
            keyring=keyring,
            rados_user=rados_user,
            rbd_pool=rbd_pool,
            read_only=read_only,
            secret_ref=secret_ref,
        )

        return typing.cast(None, jsii.invoke(self, "putRbd", [value]))

    @jsii.member(jsii_name="putVsphereVolume")
    def put_vsphere_volume(
        self,
        *,
        volume_path: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param volume_path: Path that identifies vSphere volume vmdk. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#volume_path DataKubernetesPersistentVolumeV1#volume_path}
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#fs_type DataKubernetesPersistentVolumeV1#fs_type}
        '''
        value = DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceVsphereVolume(
            volume_path=volume_path, fs_type=fs_type
        )

        return typing.cast(None, jsii.invoke(self, "putVsphereVolume", [value]))

    @jsii.member(jsii_name="resetAwsElasticBlockStore")
    def reset_aws_elastic_block_store(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsElasticBlockStore", []))

    @jsii.member(jsii_name="resetAzureDisk")
    def reset_azure_disk(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureDisk", []))

    @jsii.member(jsii_name="resetAzureFile")
    def reset_azure_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureFile", []))

    @jsii.member(jsii_name="resetCephFs")
    def reset_ceph_fs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCephFs", []))

    @jsii.member(jsii_name="resetCinder")
    def reset_cinder(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCinder", []))

    @jsii.member(jsii_name="resetCsi")
    def reset_csi(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCsi", []))

    @jsii.member(jsii_name="resetFc")
    def reset_fc(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFc", []))

    @jsii.member(jsii_name="resetFlexVolume")
    def reset_flex_volume(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFlexVolume", []))

    @jsii.member(jsii_name="resetFlocker")
    def reset_flocker(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFlocker", []))

    @jsii.member(jsii_name="resetGcePersistentDisk")
    def reset_gce_persistent_disk(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGcePersistentDisk", []))

    @jsii.member(jsii_name="resetGlusterfs")
    def reset_glusterfs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGlusterfs", []))

    @jsii.member(jsii_name="resetHostPath")
    def reset_host_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostPath", []))

    @jsii.member(jsii_name="resetIscsi")
    def reset_iscsi(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIscsi", []))

    @jsii.member(jsii_name="resetLocal")
    def reset_local(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocal", []))

    @jsii.member(jsii_name="resetNfs")
    def reset_nfs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNfs", []))

    @jsii.member(jsii_name="resetPhotonPersistentDisk")
    def reset_photon_persistent_disk(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPhotonPersistentDisk", []))

    @jsii.member(jsii_name="resetQuobyte")
    def reset_quobyte(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQuobyte", []))

    @jsii.member(jsii_name="resetRbd")
    def reset_rbd(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRbd", []))

    @jsii.member(jsii_name="resetVsphereVolume")
    def reset_vsphere_volume(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVsphereVolume", []))

    @builtins.property
    @jsii.member(jsii_name="awsElasticBlockStore")
    def aws_elastic_block_store(
        self,
    ) -> DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAwsElasticBlockStoreOutputReference:
        return typing.cast(DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAwsElasticBlockStoreOutputReference, jsii.get(self, "awsElasticBlockStore"))

    @builtins.property
    @jsii.member(jsii_name="azureDisk")
    def azure_disk(
        self,
    ) -> DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAzureDiskOutputReference:
        return typing.cast(DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAzureDiskOutputReference, jsii.get(self, "azureDisk"))

    @builtins.property
    @jsii.member(jsii_name="azureFile")
    def azure_file(
        self,
    ) -> DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAzureFileOutputReference:
        return typing.cast(DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAzureFileOutputReference, jsii.get(self, "azureFile"))

    @builtins.property
    @jsii.member(jsii_name="cephFs")
    def ceph_fs(
        self,
    ) -> DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCephFsOutputReference:
        return typing.cast(DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCephFsOutputReference, jsii.get(self, "cephFs"))

    @builtins.property
    @jsii.member(jsii_name="cinder")
    def cinder(
        self,
    ) -> DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCinderOutputReference:
        return typing.cast(DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCinderOutputReference, jsii.get(self, "cinder"))

    @builtins.property
    @jsii.member(jsii_name="csi")
    def csi(
        self,
    ) -> DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiOutputReference:
        return typing.cast(DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiOutputReference, jsii.get(self, "csi"))

    @builtins.property
    @jsii.member(jsii_name="fc")
    def fc(
        self,
    ) -> DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFcOutputReference:
        return typing.cast(DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFcOutputReference, jsii.get(self, "fc"))

    @builtins.property
    @jsii.member(jsii_name="flexVolume")
    def flex_volume(
        self,
    ) -> DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeOutputReference:
        return typing.cast(DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeOutputReference, jsii.get(self, "flexVolume"))

    @builtins.property
    @jsii.member(jsii_name="flocker")
    def flocker(
        self,
    ) -> DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlockerOutputReference:
        return typing.cast(DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlockerOutputReference, jsii.get(self, "flocker"))

    @builtins.property
    @jsii.member(jsii_name="gcePersistentDisk")
    def gce_persistent_disk(
        self,
    ) -> DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceGcePersistentDiskOutputReference:
        return typing.cast(DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceGcePersistentDiskOutputReference, jsii.get(self, "gcePersistentDisk"))

    @builtins.property
    @jsii.member(jsii_name="glusterfs")
    def glusterfs(
        self,
    ) -> DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceGlusterfsOutputReference:
        return typing.cast(DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceGlusterfsOutputReference, jsii.get(self, "glusterfs"))

    @builtins.property
    @jsii.member(jsii_name="hostPath")
    def host_path(
        self,
    ) -> DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceHostPathOutputReference:
        return typing.cast(DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceHostPathOutputReference, jsii.get(self, "hostPath"))

    @builtins.property
    @jsii.member(jsii_name="iscsi")
    def iscsi(
        self,
    ) -> DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceIscsiOutputReference:
        return typing.cast(DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceIscsiOutputReference, jsii.get(self, "iscsi"))

    @builtins.property
    @jsii.member(jsii_name="local")
    def local(
        self,
    ) -> DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceLocalOutputReference:
        return typing.cast(DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceLocalOutputReference, jsii.get(self, "local"))

    @builtins.property
    @jsii.member(jsii_name="nfs")
    def nfs(
        self,
    ) -> DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceNfsOutputReference:
        return typing.cast(DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceNfsOutputReference, jsii.get(self, "nfs"))

    @builtins.property
    @jsii.member(jsii_name="photonPersistentDisk")
    def photon_persistent_disk(
        self,
    ) -> "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourcePhotonPersistentDiskOutputReference":
        return typing.cast("DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourcePhotonPersistentDiskOutputReference", jsii.get(self, "photonPersistentDisk"))

    @builtins.property
    @jsii.member(jsii_name="quobyte")
    def quobyte(
        self,
    ) -> "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceQuobyteOutputReference":
        return typing.cast("DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceQuobyteOutputReference", jsii.get(self, "quobyte"))

    @builtins.property
    @jsii.member(jsii_name="rbd")
    def rbd(
        self,
    ) -> "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceRbdOutputReference":
        return typing.cast("DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceRbdOutputReference", jsii.get(self, "rbd"))

    @builtins.property
    @jsii.member(jsii_name="vsphereVolume")
    def vsphere_volume(
        self,
    ) -> "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceVsphereVolumeOutputReference":
        return typing.cast("DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceVsphereVolumeOutputReference", jsii.get(self, "vsphereVolume"))

    @builtins.property
    @jsii.member(jsii_name="awsElasticBlockStoreInput")
    def aws_elastic_block_store_input(
        self,
    ) -> typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAwsElasticBlockStore]:
        return typing.cast(typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAwsElasticBlockStore], jsii.get(self, "awsElasticBlockStoreInput"))

    @builtins.property
    @jsii.member(jsii_name="azureDiskInput")
    def azure_disk_input(
        self,
    ) -> typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAzureDisk]:
        return typing.cast(typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAzureDisk], jsii.get(self, "azureDiskInput"))

    @builtins.property
    @jsii.member(jsii_name="azureFileInput")
    def azure_file_input(
        self,
    ) -> typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAzureFile]:
        return typing.cast(typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAzureFile], jsii.get(self, "azureFileInput"))

    @builtins.property
    @jsii.member(jsii_name="cephFsInput")
    def ceph_fs_input(
        self,
    ) -> typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCephFs]:
        return typing.cast(typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCephFs], jsii.get(self, "cephFsInput"))

    @builtins.property
    @jsii.member(jsii_name="cinderInput")
    def cinder_input(
        self,
    ) -> typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCinder]:
        return typing.cast(typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCinder], jsii.get(self, "cinderInput"))

    @builtins.property
    @jsii.member(jsii_name="csiInput")
    def csi_input(
        self,
    ) -> typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsi]:
        return typing.cast(typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsi], jsii.get(self, "csiInput"))

    @builtins.property
    @jsii.member(jsii_name="fcInput")
    def fc_input(
        self,
    ) -> typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFc]:
        return typing.cast(typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFc], jsii.get(self, "fcInput"))

    @builtins.property
    @jsii.member(jsii_name="flexVolumeInput")
    def flex_volume_input(
        self,
    ) -> typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlexVolume]:
        return typing.cast(typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlexVolume], jsii.get(self, "flexVolumeInput"))

    @builtins.property
    @jsii.member(jsii_name="flockerInput")
    def flocker_input(
        self,
    ) -> typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlocker]:
        return typing.cast(typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlocker], jsii.get(self, "flockerInput"))

    @builtins.property
    @jsii.member(jsii_name="gcePersistentDiskInput")
    def gce_persistent_disk_input(
        self,
    ) -> typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceGcePersistentDisk]:
        return typing.cast(typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceGcePersistentDisk], jsii.get(self, "gcePersistentDiskInput"))

    @builtins.property
    @jsii.member(jsii_name="glusterfsInput")
    def glusterfs_input(
        self,
    ) -> typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceGlusterfs]:
        return typing.cast(typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceGlusterfs], jsii.get(self, "glusterfsInput"))

    @builtins.property
    @jsii.member(jsii_name="hostPathInput")
    def host_path_input(
        self,
    ) -> typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceHostPath]:
        return typing.cast(typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceHostPath], jsii.get(self, "hostPathInput"))

    @builtins.property
    @jsii.member(jsii_name="iscsiInput")
    def iscsi_input(
        self,
    ) -> typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceIscsi]:
        return typing.cast(typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceIscsi], jsii.get(self, "iscsiInput"))

    @builtins.property
    @jsii.member(jsii_name="localInput")
    def local_input(
        self,
    ) -> typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceLocal]:
        return typing.cast(typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceLocal], jsii.get(self, "localInput"))

    @builtins.property
    @jsii.member(jsii_name="nfsInput")
    def nfs_input(
        self,
    ) -> typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceNfs]:
        return typing.cast(typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceNfs], jsii.get(self, "nfsInput"))

    @builtins.property
    @jsii.member(jsii_name="photonPersistentDiskInput")
    def photon_persistent_disk_input(
        self,
    ) -> typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourcePhotonPersistentDisk"]:
        return typing.cast(typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourcePhotonPersistentDisk"], jsii.get(self, "photonPersistentDiskInput"))

    @builtins.property
    @jsii.member(jsii_name="quobyteInput")
    def quobyte_input(
        self,
    ) -> typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceQuobyte"]:
        return typing.cast(typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceQuobyte"], jsii.get(self, "quobyteInput"))

    @builtins.property
    @jsii.member(jsii_name="rbdInput")
    def rbd_input(
        self,
    ) -> typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceRbd"]:
        return typing.cast(typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceRbd"], jsii.get(self, "rbdInput"))

    @builtins.property
    @jsii.member(jsii_name="vsphereVolumeInput")
    def vsphere_volume_input(
        self,
    ) -> typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceVsphereVolume"]:
        return typing.cast(typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceVsphereVolume"], jsii.get(self, "vsphereVolumeInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSource]:
        return typing.cast(typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSource], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSource],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8bd5a34e5f2d6d050257cb981c1664272c357895346bd561c145b70416ef7ed3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourcePhotonPersistentDisk",
    jsii_struct_bases=[],
    name_mapping={"pd_id": "pdId", "fs_type": "fsType"},
)
class DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourcePhotonPersistentDisk:
    def __init__(
        self,
        *,
        pd_id: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param pd_id: ID that identifies Photon Controller persistent disk. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#pd_id DataKubernetesPersistentVolumeV1#pd_id}
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#fs_type DataKubernetesPersistentVolumeV1#fs_type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc64369077a4a86adc3688db338be21ad212d7ff8307f39fda46cf9339960011)
            check_type(argname="argument pd_id", value=pd_id, expected_type=type_hints["pd_id"])
            check_type(argname="argument fs_type", value=fs_type, expected_type=type_hints["fs_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "pd_id": pd_id,
        }
        if fs_type is not None:
            self._values["fs_type"] = fs_type

    @builtins.property
    def pd_id(self) -> builtins.str:
        '''ID that identifies Photon Controller persistent disk.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#pd_id DataKubernetesPersistentVolumeV1#pd_id}
        '''
        result = self._values.get("pd_id")
        assert result is not None, "Required property 'pd_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def fs_type(self) -> typing.Optional[builtins.str]:
        '''Filesystem type to mount.

        Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#fs_type DataKubernetesPersistentVolumeV1#fs_type}
        '''
        result = self._values.get("fs_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourcePhotonPersistentDisk(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourcePhotonPersistentDiskOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourcePhotonPersistentDiskOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a06f9d8484a2fa5f01e5ca77094cbafaae82ddfed6f716f8932a1b6dbf448288)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFsType")
    def reset_fs_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFsType", []))

    @builtins.property
    @jsii.member(jsii_name="fsTypeInput")
    def fs_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fsTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="pdIdInput")
    def pd_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pdIdInput"))

    @builtins.property
    @jsii.member(jsii_name="fsType")
    def fs_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fsType"))

    @fs_type.setter
    def fs_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58846d4492865a4270c4c4c924efdcbb6c0a2e116ed1b1a345a8b4d2c7ca046d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fsType", value)

    @builtins.property
    @jsii.member(jsii_name="pdId")
    def pd_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pdId"))

    @pd_id.setter
    def pd_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__700b591852fd1e8d77d28ef88e5eebf54705a5b24299dd3975f4b74e490e2f5f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pdId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourcePhotonPersistentDisk]:
        return typing.cast(typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourcePhotonPersistentDisk], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourcePhotonPersistentDisk],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aebad767e846ae6e914b42eaf81401d3939a1384eb0ef52595692127b906ec0d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceQuobyte",
    jsii_struct_bases=[],
    name_mapping={
        "registry": "registry",
        "volume": "volume",
        "group": "group",
        "read_only": "readOnly",
        "user": "user",
    },
)
class DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceQuobyte:
    def __init__(
        self,
        *,
        registry: builtins.str,
        volume: builtins.str,
        group: typing.Optional[builtins.str] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        user: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param registry: Registry represents a single or multiple Quobyte Registry services specified as a string as host:port pair (multiple entries are separated with commas) which acts as the central registry for volumes. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#registry DataKubernetesPersistentVolumeV1#registry}
        :param volume: Volume is a string that references an already created Quobyte volume by name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#volume DataKubernetesPersistentVolumeV1#volume}
        :param group: Group to map volume access to Default is no group. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#group DataKubernetesPersistentVolumeV1#group}
        :param read_only: Whether to force the Quobyte volume to be mounted with read-only permissions. Defaults to false. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#read_only DataKubernetesPersistentVolumeV1#read_only}
        :param user: User to map volume access to Defaults to serivceaccount user. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#user DataKubernetesPersistentVolumeV1#user}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa06c1f399486e1037074042d5de0708ca013c96a5881e1b63f09d60c88d9df9)
            check_type(argname="argument registry", value=registry, expected_type=type_hints["registry"])
            check_type(argname="argument volume", value=volume, expected_type=type_hints["volume"])
            check_type(argname="argument group", value=group, expected_type=type_hints["group"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
            check_type(argname="argument user", value=user, expected_type=type_hints["user"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "registry": registry,
            "volume": volume,
        }
        if group is not None:
            self._values["group"] = group
        if read_only is not None:
            self._values["read_only"] = read_only
        if user is not None:
            self._values["user"] = user

    @builtins.property
    def registry(self) -> builtins.str:
        '''Registry represents a single or multiple Quobyte Registry services specified as a string as host:port pair (multiple entries are separated with commas) which acts as the central registry for volumes.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#registry DataKubernetesPersistentVolumeV1#registry}
        '''
        result = self._values.get("registry")
        assert result is not None, "Required property 'registry' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def volume(self) -> builtins.str:
        '''Volume is a string that references an already created Quobyte volume by name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#volume DataKubernetesPersistentVolumeV1#volume}
        '''
        result = self._values.get("volume")
        assert result is not None, "Required property 'volume' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group(self) -> typing.Optional[builtins.str]:
        '''Group to map volume access to Default is no group.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#group DataKubernetesPersistentVolumeV1#group}
        '''
        result = self._values.get("group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to force the Quobyte volume to be mounted with read-only permissions. Defaults to false.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#read_only DataKubernetesPersistentVolumeV1#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def user(self) -> typing.Optional[builtins.str]:
        '''User to map volume access to Defaults to serivceaccount user.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#user DataKubernetesPersistentVolumeV1#user}
        '''
        result = self._values.get("user")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceQuobyte(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceQuobyteOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceQuobyteOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8579a3fc181e3efa3f0ef66111afc6055e0e3d3cb2a65fb2fbd71909c17f71e0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetGroup")
    def reset_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroup", []))

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @jsii.member(jsii_name="resetUser")
    def reset_user(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUser", []))

    @builtins.property
    @jsii.member(jsii_name="groupInput")
    def group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="registryInput")
    def registry_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "registryInput"))

    @builtins.property
    @jsii.member(jsii_name="userInput")
    def user_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeInput")
    def volume_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "volumeInput"))

    @builtins.property
    @jsii.member(jsii_name="group")
    def group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "group"))

    @group.setter
    def group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__744c6df6bba43e06002ef053afb271d2ee1f3316bfe2a9ac30ee90c7d3421a21)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "group", value)

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "readOnly"))

    @read_only.setter
    def read_only(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f12535a80f1d7fb827ce84f91b72da9437fe7928c77293a5b4d8bf0cba342b16)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="registry")
    def registry(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "registry"))

    @registry.setter
    def registry(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__481c3e8b78b255dc28c69b3701dbebdd397d9268b7440f0f15a29bd247c9f087)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "registry", value)

    @builtins.property
    @jsii.member(jsii_name="user")
    def user(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "user"))

    @user.setter
    def user(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa64b50e072742f60fc31aca9e9332edc0c968dc8c5640c13b7fb2271048da5a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "user", value)

    @builtins.property
    @jsii.member(jsii_name="volume")
    def volume(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volume"))

    @volume.setter
    def volume(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ddd86e5c35605fd100a178d123950f57903daeb5f9356a914b8ba1a85cbd7f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volume", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceQuobyte]:
        return typing.cast(typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceQuobyte], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceQuobyte],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ded2c7e5bc0a7120eba0290750e9bdff64c9459c1936addbcb7f632ee1cc4518)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceRbd",
    jsii_struct_bases=[],
    name_mapping={
        "ceph_monitors": "cephMonitors",
        "rbd_image": "rbdImage",
        "fs_type": "fsType",
        "keyring": "keyring",
        "rados_user": "radosUser",
        "rbd_pool": "rbdPool",
        "read_only": "readOnly",
        "secret_ref": "secretRef",
    },
)
class DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceRbd:
    def __init__(
        self,
        *,
        ceph_monitors: typing.Sequence[builtins.str],
        rbd_image: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        keyring: typing.Optional[builtins.str] = None,
        rados_user: typing.Optional[builtins.str] = None,
        rbd_pool: typing.Optional[builtins.str] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        secret_ref: typing.Optional[typing.Union["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceRbdSecretRef", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param ceph_monitors: A collection of Ceph monitors. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#ceph_monitors DataKubernetesPersistentVolumeV1#ceph_monitors}
        :param rbd_image: The rados image name. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#rbd_image DataKubernetesPersistentVolumeV1#rbd_image}
        :param fs_type: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: http://kubernetes.io/docs/user-guide/volumes#rbd Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#fs_type DataKubernetesPersistentVolumeV1#fs_type}
        :param keyring: Keyring is the path to key ring for RBDUser. Default is /etc/ceph/keyring. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#keyring DataKubernetesPersistentVolumeV1#keyring}
        :param rados_user: The rados user name. Default is admin. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#rados_user DataKubernetesPersistentVolumeV1#rados_user}
        :param rbd_pool: The rados pool name. Default is rbd. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#rbd_pool DataKubernetesPersistentVolumeV1#rbd_pool}
        :param read_only: Whether to force the read-only setting in VolumeMounts. Defaults to false. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#read_only DataKubernetesPersistentVolumeV1#read_only}
        :param secret_ref: secret_ref block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#secret_ref DataKubernetesPersistentVolumeV1#secret_ref}
        '''
        if isinstance(secret_ref, dict):
            secret_ref = DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceRbdSecretRef(**secret_ref)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f9ed4348c81630d621bb98ec511a9407f18af55d90b7db8af265e8586ce4186)
            check_type(argname="argument ceph_monitors", value=ceph_monitors, expected_type=type_hints["ceph_monitors"])
            check_type(argname="argument rbd_image", value=rbd_image, expected_type=type_hints["rbd_image"])
            check_type(argname="argument fs_type", value=fs_type, expected_type=type_hints["fs_type"])
            check_type(argname="argument keyring", value=keyring, expected_type=type_hints["keyring"])
            check_type(argname="argument rados_user", value=rados_user, expected_type=type_hints["rados_user"])
            check_type(argname="argument rbd_pool", value=rbd_pool, expected_type=type_hints["rbd_pool"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
            check_type(argname="argument secret_ref", value=secret_ref, expected_type=type_hints["secret_ref"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ceph_monitors": ceph_monitors,
            "rbd_image": rbd_image,
        }
        if fs_type is not None:
            self._values["fs_type"] = fs_type
        if keyring is not None:
            self._values["keyring"] = keyring
        if rados_user is not None:
            self._values["rados_user"] = rados_user
        if rbd_pool is not None:
            self._values["rbd_pool"] = rbd_pool
        if read_only is not None:
            self._values["read_only"] = read_only
        if secret_ref is not None:
            self._values["secret_ref"] = secret_ref

    @builtins.property
    def ceph_monitors(self) -> typing.List[builtins.str]:
        '''A collection of Ceph monitors. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#ceph_monitors DataKubernetesPersistentVolumeV1#ceph_monitors}
        '''
        result = self._values.get("ceph_monitors")
        assert result is not None, "Required property 'ceph_monitors' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def rbd_image(self) -> builtins.str:
        '''The rados image name. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#rbd_image DataKubernetesPersistentVolumeV1#rbd_image}
        '''
        result = self._values.get("rbd_image")
        assert result is not None, "Required property 'rbd_image' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def fs_type(self) -> typing.Optional[builtins.str]:
        '''Filesystem type of the volume that you want to mount.

        Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: http://kubernetes.io/docs/user-guide/volumes#rbd

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#fs_type DataKubernetesPersistentVolumeV1#fs_type}
        '''
        result = self._values.get("fs_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def keyring(self) -> typing.Optional[builtins.str]:
        '''Keyring is the path to key ring for RBDUser. Default is /etc/ceph/keyring. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#keyring DataKubernetesPersistentVolumeV1#keyring}
        '''
        result = self._values.get("keyring")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rados_user(self) -> typing.Optional[builtins.str]:
        '''The rados user name. Default is admin. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#rados_user DataKubernetesPersistentVolumeV1#rados_user}
        '''
        result = self._values.get("rados_user")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rbd_pool(self) -> typing.Optional[builtins.str]:
        '''The rados pool name. Default is rbd. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#rbd_pool DataKubernetesPersistentVolumeV1#rbd_pool}
        '''
        result = self._values.get("rbd_pool")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to force the read-only setting in VolumeMounts. Defaults to false. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#read_only DataKubernetesPersistentVolumeV1#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def secret_ref(
        self,
    ) -> typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceRbdSecretRef"]:
        '''secret_ref block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#secret_ref DataKubernetesPersistentVolumeV1#secret_ref}
        '''
        result = self._values.get("secret_ref")
        return typing.cast(typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceRbdSecretRef"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceRbd(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceRbdOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceRbdOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6a96c74a440429e9339d4f98a92e28cf08553ce8c1e79b9ed40cdbb20e8c1838)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSecretRef")
    def put_secret_ref(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#name DataKubernetesPersistentVolumeV1#name}
        :param namespace: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#namespace DataKubernetesPersistentVolumeV1#namespace}
        '''
        value = DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceRbdSecretRef(
            name=name, namespace=namespace
        )

        return typing.cast(None, jsii.invoke(self, "putSecretRef", [value]))

    @jsii.member(jsii_name="resetFsType")
    def reset_fs_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFsType", []))

    @jsii.member(jsii_name="resetKeyring")
    def reset_keyring(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyring", []))

    @jsii.member(jsii_name="resetRadosUser")
    def reset_rados_user(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRadosUser", []))

    @jsii.member(jsii_name="resetRbdPool")
    def reset_rbd_pool(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRbdPool", []))

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @jsii.member(jsii_name="resetSecretRef")
    def reset_secret_ref(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretRef", []))

    @builtins.property
    @jsii.member(jsii_name="secretRef")
    def secret_ref(
        self,
    ) -> "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceRbdSecretRefOutputReference":
        return typing.cast("DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceRbdSecretRefOutputReference", jsii.get(self, "secretRef"))

    @builtins.property
    @jsii.member(jsii_name="cephMonitorsInput")
    def ceph_monitors_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "cephMonitorsInput"))

    @builtins.property
    @jsii.member(jsii_name="fsTypeInput")
    def fs_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fsTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="keyringInput")
    def keyring_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyringInput"))

    @builtins.property
    @jsii.member(jsii_name="radosUserInput")
    def rados_user_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "radosUserInput"))

    @builtins.property
    @jsii.member(jsii_name="rbdImageInput")
    def rbd_image_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rbdImageInput"))

    @builtins.property
    @jsii.member(jsii_name="rbdPoolInput")
    def rbd_pool_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rbdPoolInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="secretRefInput")
    def secret_ref_input(
        self,
    ) -> typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceRbdSecretRef"]:
        return typing.cast(typing.Optional["DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceRbdSecretRef"], jsii.get(self, "secretRefInput"))

    @builtins.property
    @jsii.member(jsii_name="cephMonitors")
    def ceph_monitors(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "cephMonitors"))

    @ceph_monitors.setter
    def ceph_monitors(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__437060bca7b2a98444937e007d3d9f29d33ac019aa4ae424b4c81eb3a3c006df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cephMonitors", value)

    @builtins.property
    @jsii.member(jsii_name="fsType")
    def fs_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fsType"))

    @fs_type.setter
    def fs_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75eef44593b85fe6726236e59f2edc0242fe46971d384b2695e70c4b6efc059b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fsType", value)

    @builtins.property
    @jsii.member(jsii_name="keyring")
    def keyring(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyring"))

    @keyring.setter
    def keyring(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__456abd1cc8331f7f835bf779e8353e99ee41bb6cfd0cdcd2b7c0c9b4b013820c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyring", value)

    @builtins.property
    @jsii.member(jsii_name="radosUser")
    def rados_user(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "radosUser"))

    @rados_user.setter
    def rados_user(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f6d2e2f3f135f19cc32ae3e9163a98b919eb1222c1a4bf3f6dcb1a908acf90c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "radosUser", value)

    @builtins.property
    @jsii.member(jsii_name="rbdImage")
    def rbd_image(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rbdImage"))

    @rbd_image.setter
    def rbd_image(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06393f2b56a29ec2d33bcf4e08e04bae4b56572d2b48d504e3601fcd6c8a05e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rbdImage", value)

    @builtins.property
    @jsii.member(jsii_name="rbdPool")
    def rbd_pool(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rbdPool"))

    @rbd_pool.setter
    def rbd_pool(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b7e45e573340bb358705078de903d8f718e6afbc0d02cc780dd2f1489b9cd18)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rbdPool", value)

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "readOnly"))

    @read_only.setter
    def read_only(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a13a485667ecb7b43c9009bd7b8234bbed1b6aa0708b0899df31ce3888da7bc8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceRbd]:
        return typing.cast(typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceRbd], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceRbd],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__948532c00736e4090c4f9a74debccc7dfa196638ca7dd544fbf8aac651f806b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceRbdSecretRef",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "namespace": "namespace"},
)
class DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceRbdSecretRef:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#name DataKubernetesPersistentVolumeV1#name}
        :param namespace: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#namespace DataKubernetesPersistentVolumeV1#namespace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__294e7155d3f30dec618a99b7496ebcdf4e91169cf9ec9ad24e023ce845bfac21)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if namespace is not None:
            self._values["namespace"] = namespace

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#name DataKubernetesPersistentVolumeV1#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#namespace DataKubernetesPersistentVolumeV1#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceRbdSecretRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceRbdSecretRefOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceRbdSecretRefOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__630e9d4d89137a7fb975ca0bb7f199ea137ed91d98847eb0ebba8a0e12668467)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

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
            type_hints = typing.get_type_hints(_typecheckingstub__ec6c7a2b2b221921f50fede1f32d489e775a554856ce5cfb288da6ace6a10e94)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aad1747ab993f3a51e2e561da2eab1205b9103fb4d5bd4853926b734807624ee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceRbdSecretRef]:
        return typing.cast(typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceRbdSecretRef], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceRbdSecretRef],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73c5c9ace53f59cff8f6d1f4dea2f6a54903cb9cc1994330ebde1cda3a0ba024)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceVsphereVolume",
    jsii_struct_bases=[],
    name_mapping={"volume_path": "volumePath", "fs_type": "fsType"},
)
class DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceVsphereVolume:
    def __init__(
        self,
        *,
        volume_path: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param volume_path: Path that identifies vSphere volume vmdk. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#volume_path DataKubernetesPersistentVolumeV1#volume_path}
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#fs_type DataKubernetesPersistentVolumeV1#fs_type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39fd40c52e9a2b01f1f4a492ff9d43c367ee1d49e28bfcf4f0399f60eec2123f)
            check_type(argname="argument volume_path", value=volume_path, expected_type=type_hints["volume_path"])
            check_type(argname="argument fs_type", value=fs_type, expected_type=type_hints["fs_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "volume_path": volume_path,
        }
        if fs_type is not None:
            self._values["fs_type"] = fs_type

    @builtins.property
    def volume_path(self) -> builtins.str:
        '''Path that identifies vSphere volume vmdk.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#volume_path DataKubernetesPersistentVolumeV1#volume_path}
        '''
        result = self._values.get("volume_path")
        assert result is not None, "Required property 'volume_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def fs_type(self) -> typing.Optional[builtins.str]:
        '''Filesystem type to mount.

        Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/data-sources/persistent_volume_v1#fs_type DataKubernetesPersistentVolumeV1#fs_type}
        '''
        result = self._values.get("fs_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceVsphereVolume(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceVsphereVolumeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.dataKubernetesPersistentVolumeV1.DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceVsphereVolumeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__26792b7ca98774aa0fcd9013ec078f9168debf4301ba551965a25d7e9e819d6f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFsType")
    def reset_fs_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFsType", []))

    @builtins.property
    @jsii.member(jsii_name="fsTypeInput")
    def fs_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fsTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="volumePathInput")
    def volume_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "volumePathInput"))

    @builtins.property
    @jsii.member(jsii_name="fsType")
    def fs_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fsType"))

    @fs_type.setter
    def fs_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9211211713d8e673309da36caa80f7a9cc579a0d16782683985b4fb06f96a50)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fsType", value)

    @builtins.property
    @jsii.member(jsii_name="volumePath")
    def volume_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volumePath"))

    @volume_path.setter
    def volume_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b5c00b6ae273ac0181b7171f4b5c4b0f30ac1ffc9862240c4cb80dfcf1f37d80)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumePath", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceVsphereVolume]:
        return typing.cast(typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceVsphereVolume], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceVsphereVolume],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb0aa86f5e770916d4ca4116c6af0c2a05307304e778000184c3c67d887527d9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataKubernetesPersistentVolumeV1",
    "DataKubernetesPersistentVolumeV1Config",
    "DataKubernetesPersistentVolumeV1Metadata",
    "DataKubernetesPersistentVolumeV1MetadataOutputReference",
    "DataKubernetesPersistentVolumeV1Spec",
    "DataKubernetesPersistentVolumeV1SpecClaimRef",
    "DataKubernetesPersistentVolumeV1SpecClaimRefOutputReference",
    "DataKubernetesPersistentVolumeV1SpecList",
    "DataKubernetesPersistentVolumeV1SpecNodeAffinity",
    "DataKubernetesPersistentVolumeV1SpecNodeAffinityOutputReference",
    "DataKubernetesPersistentVolumeV1SpecNodeAffinityRequired",
    "DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTerm",
    "DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermList",
    "DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressions",
    "DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressionsList",
    "DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressionsOutputReference",
    "DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFields",
    "DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFieldsList",
    "DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFieldsOutputReference",
    "DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermOutputReference",
    "DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredOutputReference",
    "DataKubernetesPersistentVolumeV1SpecOutputReference",
    "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSource",
    "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAwsElasticBlockStore",
    "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAwsElasticBlockStoreOutputReference",
    "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAzureDisk",
    "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAzureDiskOutputReference",
    "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAzureFile",
    "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAzureFileOutputReference",
    "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCephFs",
    "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCephFsOutputReference",
    "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCephFsSecretRef",
    "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCephFsSecretRefOutputReference",
    "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCinder",
    "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCinderOutputReference",
    "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsi",
    "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiControllerExpandSecretRef",
    "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiControllerExpandSecretRefOutputReference",
    "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiControllerPublishSecretRef",
    "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiControllerPublishSecretRefOutputReference",
    "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiNodePublishSecretRef",
    "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiNodePublishSecretRefOutputReference",
    "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiNodeStageSecretRef",
    "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiNodeStageSecretRefOutputReference",
    "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiOutputReference",
    "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFc",
    "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFcOutputReference",
    "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlexVolume",
    "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeOutputReference",
    "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeSecretRef",
    "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeSecretRefOutputReference",
    "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlocker",
    "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlockerOutputReference",
    "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceGcePersistentDisk",
    "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceGcePersistentDiskOutputReference",
    "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceGlusterfs",
    "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceGlusterfsOutputReference",
    "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceHostPath",
    "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceHostPathOutputReference",
    "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceIscsi",
    "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceIscsiOutputReference",
    "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceLocal",
    "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceLocalOutputReference",
    "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceNfs",
    "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceNfsOutputReference",
    "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceOutputReference",
    "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourcePhotonPersistentDisk",
    "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourcePhotonPersistentDiskOutputReference",
    "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceQuobyte",
    "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceQuobyteOutputReference",
    "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceRbd",
    "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceRbdOutputReference",
    "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceRbdSecretRef",
    "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceRbdSecretRefOutputReference",
    "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceVsphereVolume",
    "DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceVsphereVolumeOutputReference",
]

publication.publish()

def _typecheckingstub__a36d09ce346420033ae9deb890db42338e8cd3fdfb77f97ee8d34f7df8e55adb(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    metadata: typing.Union[DataKubernetesPersistentVolumeV1Metadata, typing.Dict[builtins.str, typing.Any]],
    id: typing.Optional[builtins.str] = None,
    spec: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataKubernetesPersistentVolumeV1Spec, typing.Dict[builtins.str, typing.Any]]]]] = None,
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

def _typecheckingstub__fe8b958ab25ba340e360c55811ab17a68e0a13f77110440dcd12016ab03cf35d(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataKubernetesPersistentVolumeV1Spec, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a005e69c6b3ce2245190f84fcea4b151f069cd2b7193a19475735b62fd9e5af(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05fe15da96f9541a8d08f3af321d7affa73cf8250962949c04ce852a8e679674(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    metadata: typing.Union[DataKubernetesPersistentVolumeV1Metadata, typing.Dict[builtins.str, typing.Any]],
    id: typing.Optional[builtins.str] = None,
    spec: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataKubernetesPersistentVolumeV1Spec, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__217167e19339c8a03bab5a82157f2f943cf9acf577295a422d5969dd5aae7197(
    *,
    annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8de94df421b903310c1b923b19e43c6110c7a91923b370a74c8549af417ec0a1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d12c5093b23351f47b24890591a6db73828abb783aa2bcf968bba9b1e315a1f(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdf00026c6deb97c4aaaa9536454cb9676dfd3f7ccb21d47a7781c14dfebbc45(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30d332e580c281d56888ebf6eebd7798126870e100e0963099dda9b87fe7d73f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c89cf5f499a85901caa03b7e191b31889d58a66126c5fdb28be850563c84a04c(
    value: typing.Optional[DataKubernetesPersistentVolumeV1Metadata],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3d29fddb4061926d6ce6652ceba01c9079def1e16e5b815f5d775895197c9b4(
    *,
    access_modes: typing.Sequence[builtins.str],
    capacity: typing.Mapping[builtins.str, builtins.str],
    persistent_volume_source: typing.Union[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSource, typing.Dict[builtins.str, typing.Any]],
    claim_ref: typing.Optional[typing.Union[DataKubernetesPersistentVolumeV1SpecClaimRef, typing.Dict[builtins.str, typing.Any]]] = None,
    mount_options: typing.Optional[typing.Sequence[builtins.str]] = None,
    node_affinity: typing.Optional[typing.Union[DataKubernetesPersistentVolumeV1SpecNodeAffinity, typing.Dict[builtins.str, typing.Any]]] = None,
    persistent_volume_reclaim_policy: typing.Optional[builtins.str] = None,
    storage_class_name: typing.Optional[builtins.str] = None,
    volume_mode: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__027983f95dc76c9510fe3e31a5b722d1cd0086682fa9a206f98cf377f4e92030(
    *,
    name: builtins.str,
    namespace: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91e7c36065f2342ea56f0dbff7a3a3f30b879a41a2ccfd83dd21e35d1465a620(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d70eafb5b634510081e933f70aa62457d10064b590b77af379cf2b8a0c3630fa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10c958bae7ff95ba26b7e7e6d70328be20b6c04008a411d91b915fc932038ff6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94650a6b062c678e5c975ab7d8415a3d06737fabc51913c3a20532db632b2b3e(
    value: typing.Optional[DataKubernetesPersistentVolumeV1SpecClaimRef],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e271a8a3b265b2902114f6aef1f2fa9c863006f84ba7a32fd8edc9526f24b753(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbfdec2eb8ed460945570dff9c8ee3d259d740e262ff6bfd4a05f188507213e3(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd85b3fa65ba0dd05076c19d141ff20e0a5ea05376abbbbfe064ea2e11e369a4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd611b1cbae3c77190d4f590e3f98ecb637d735c12d0f84fdf98d0a3566c6518(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93261a71bc8d48a2b8e03e4ed3387038c38006343ec04771dd7de718c572a5e6(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb779ea692e2d39c3537cb52a9c1060b45ae3c0a77c099411b9428c3cf2da684(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataKubernetesPersistentVolumeV1Spec]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__583b6906e6d7d4a3d02715c43c77caad8fe10aa1b3573a1fb137b7df3b784adb(
    *,
    required: typing.Optional[typing.Union[DataKubernetesPersistentVolumeV1SpecNodeAffinityRequired, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fdc59341c09dc4bef49883a0dd6f9251a11f6cbea87992049912b3b3d5f659d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84bbfe16ccaf2026eaab95e885983e4bdd2901ff65f4c757bd58998a02247a03(
    value: typing.Optional[DataKubernetesPersistentVolumeV1SpecNodeAffinity],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf27749cc8de2c7062b320655d859b37766069c10e5fb0325a3b60c223851904(
    *,
    node_selector_term: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTerm, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34c95e657646ee840f1e8ed2e9ab458aeebfe5d37234eb97982b7cb7e03602df(
    *,
    match_expressions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressions, typing.Dict[builtins.str, typing.Any]]]]] = None,
    match_fields: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFields, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c061554b8565473c3d47e02e93a580f42e57efc6e59058478562e4de120a84a9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d2f37fe5e1308c8ce58c06afe61512d219a755d933f26b88185f7752f635138(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28d8e173ed0fff36eb418a048a4a7124f4ec1e3c4299970f7574ad9d28ab3839(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__193b120a127bd93617fc9556762e0b1bfbb3ec3240d1d562331ab2fd8b2dfcb9(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__182a1225d02192cc7d26b565798bfb03548483bd0c2ecf063b73ea1a9e355849(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d86a895493c1f7859ea0b3e2f1729102ffe086cd2912ce9cd4b1cb23f2024edd(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTerm]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__374e78f34d6c6f928bdce612757ab586b766f6f33422bef388ad1ff2cb3aa5f8(
    *,
    key: builtins.str,
    operator: builtins.str,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c66801121a2cf4884f57fa3554f3dd44e4ec6e25b1e5ed444df89b6f4cbcbaae(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9787c6a11314e6c0bb573ee0c9437ad22113a96f93ac32f55f16c896df2e79ca(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa312b9f423a40d58a41ba08444fff19556d56ffae013bc0256a605d9006ea29(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__218e90cb21541c7d67e015aaec6032d4e80bda61fa2ddb0dec4d2cd5403bd09e(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca6752a1fbad6c2202ffcb03fbf5c5243c1f8c3d86d14375d479ed85e28de5f3(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b51a08503bfd4ec260538d5ffb5fd18d6a6fb8c5d75dbc23ec39e2c4f9a9d41(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ee52fc2dc060742142ef4ac96ac220ba279f791162b3f30a1e67f92e279fdde(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__daa1131014585873eb6b44dd338ca98fc2968da4dfbe883ce94f4f74c0c35074(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b743aec58d4631c925b06bb56f6661c5568181514b7000ff87fcc0a37e304903(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ac56be3fab2c4c8808311d70a7484fbffb5c5abd47d371532456dbae833e104(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd3b8cf2aa4a50da9bcda8bac4e2c09a2bc6fd2fbbc51c80b2f43951f94980fd(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressions]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04145c6e7d60b514f6a429abdcede7ba651a943b2032adf07d795cebbafd6172(
    *,
    key: builtins.str,
    operator: builtins.str,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a36d9fec6c370e1511be7ccb88d5446c175e65bebc19105c2e0770b88d16dda1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd02ed3f0c4385fa060e2684610d1dd3aeddee76e8b49aa082231907eefa9c59(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0d1a9bd299e1de5ec566d16b9522ceff79df3155644c59a99c3996d753ec910(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42e6afdcb3d08ce245d1ff0d18fedcbbb942d2f7bbc108eae0ff7e867810cf28(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0e0a9c9e2cf05cc606e2b9d30cff50327d2b1f0dfc6c989c127943b868d7675(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09e94b9c1725734b75b288a4d4139c709b11eb3c680dc45f8cde04771a5ed85f(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFields]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca95ab35e4798f1212688b58ab72dd1314afb9a6eac735335ca5b7a5c188c644(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d02d9fad8803560d1571a906d3b18bab30d767e7111a9dcbd50aba6c508dbe5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b79f86a70dd0ab2233ab08a4436a226d0a19ada0164cf09c3268e6dda56b27ab(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__974ad5dc27f718f31f61137a7afae518c8f7a3e0ea9775c984422d2faa3fd033(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a89812919a9dce35e22d2a67af2949b5175b39076581d589245dd8ab2682146(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFields]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__534a4a19024f06f137c43f6dc3c1bc7511066baf8a43f3ddb8dbb2bbdb313394(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44da079d93802d45fe935b6e4b9a7add45264ec6c7ba047078229d55cf134a78(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d03bd88817b161a45d783bfc20fb108712a5eea4494fec53ae81ef4f9dea26d(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFields, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf2c6168c78f678dc6f21218f4f3032829e3924fd91b783165ce695c23e88c3f(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTerm]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f2a889d907d6aeb6958988571eacc1f09c735e149e2f13d1cc45072d92c84b9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf1a702f78d5e2c50077c43464491188eccf03b0f8e69cbb63cfb7eade803e88(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataKubernetesPersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTerm, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19552da9d2d4099620d4931679288c6fc52850d5801bfd105274ee3fb6423814(
    value: typing.Optional[DataKubernetesPersistentVolumeV1SpecNodeAffinityRequired],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b794878e6bd39bdc6e0d62cb339b6b32093d7aefb6998aa3737858a4f8a284e2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7061a88c1d438721992f3767ba16e704c61517680fef60e1d65797af780523e8(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88a321ff067dfef1bf5c0214522ed4c018402ce6bada2d646626ee517ed27983(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a1accdd341d97c5cbf156d651f36e62e077ce8dc23df86af856f5124a7708c4(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dda1c61a79ab0f19aeb1f2896406b57811ee25ff1edf3e788e31a8e94b620506(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__971f97406976b08fd006d872b12222662ffa5571c28be6e07dc24ea5a35d01de(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c10d6afee1ce3aa3e1bb850b43b057029395f3a61eb79e165d7a34e23d321972(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe84db2d068e0cb2368bfd390812a8cf3a027e90a51c79667c5c3b74d5dc5e5c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataKubernetesPersistentVolumeV1Spec]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6296fac964270b113bd0b52cc34701e4ae767965f1a6b9c67953fff4ccb92eb6(
    *,
    aws_elastic_block_store: typing.Optional[typing.Union[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAwsElasticBlockStore, typing.Dict[builtins.str, typing.Any]]] = None,
    azure_disk: typing.Optional[typing.Union[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAzureDisk, typing.Dict[builtins.str, typing.Any]]] = None,
    azure_file: typing.Optional[typing.Union[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAzureFile, typing.Dict[builtins.str, typing.Any]]] = None,
    ceph_fs: typing.Optional[typing.Union[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCephFs, typing.Dict[builtins.str, typing.Any]]] = None,
    cinder: typing.Optional[typing.Union[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCinder, typing.Dict[builtins.str, typing.Any]]] = None,
    csi: typing.Optional[typing.Union[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsi, typing.Dict[builtins.str, typing.Any]]] = None,
    fc: typing.Optional[typing.Union[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFc, typing.Dict[builtins.str, typing.Any]]] = None,
    flex_volume: typing.Optional[typing.Union[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlexVolume, typing.Dict[builtins.str, typing.Any]]] = None,
    flocker: typing.Optional[typing.Union[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlocker, typing.Dict[builtins.str, typing.Any]]] = None,
    gce_persistent_disk: typing.Optional[typing.Union[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceGcePersistentDisk, typing.Dict[builtins.str, typing.Any]]] = None,
    glusterfs: typing.Optional[typing.Union[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceGlusterfs, typing.Dict[builtins.str, typing.Any]]] = None,
    host_path: typing.Optional[typing.Union[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceHostPath, typing.Dict[builtins.str, typing.Any]]] = None,
    iscsi: typing.Optional[typing.Union[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceIscsi, typing.Dict[builtins.str, typing.Any]]] = None,
    local: typing.Optional[typing.Union[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceLocal, typing.Dict[builtins.str, typing.Any]]] = None,
    nfs: typing.Optional[typing.Union[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceNfs, typing.Dict[builtins.str, typing.Any]]] = None,
    photon_persistent_disk: typing.Optional[typing.Union[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourcePhotonPersistentDisk, typing.Dict[builtins.str, typing.Any]]] = None,
    quobyte: typing.Optional[typing.Union[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceQuobyte, typing.Dict[builtins.str, typing.Any]]] = None,
    rbd: typing.Optional[typing.Union[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceRbd, typing.Dict[builtins.str, typing.Any]]] = None,
    vsphere_volume: typing.Optional[typing.Union[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceVsphereVolume, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95838069dc361c6b1d0bb25c94bda6ee6181da8df259d5cd73163bd2e1dd96af(
    *,
    volume_id: builtins.str,
    fs_type: typing.Optional[builtins.str] = None,
    partition: typing.Optional[jsii.Number] = None,
    read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c39473f1592c11be2eda4239469558a0c0dff273b0d6eecfc0d4d409efba0202(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d32141dea011167aa5799235c7cd0942280f608ae7afe2f2203f2bcf328e0b9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__765b098fd1aca3b946e0c21ca74b27d3dac6bf5a41133095a7b768c03cb481e2(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1b787bf7b7f97f5c7f7478161c262220b2a8d4fbd0b5c771c36816c469bd7cf(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b8ab041b82b3f21e2266c7b4acb8aa86e3dba09a1bb81472d4b11653cbe93f8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19b69fccdeb0617f14ca28f634686c2dcb9880daa6337f5a2e13670df4127ef2(
    value: typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAwsElasticBlockStore],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e483acc85a6ebf6dcea526cbf0d69e5763132e2960040c84fe96ee6a0a550c06(
    *,
    caching_mode: builtins.str,
    data_disk_uri: builtins.str,
    disk_name: builtins.str,
    fs_type: typing.Optional[builtins.str] = None,
    kind: typing.Optional[builtins.str] = None,
    read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3308fb8fb294a1f1fd7209b9a721b9f31d105b7bd0412caf61f624601f40487(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58d871700904b6ad5cd927126bac6e015035775ebcb58174bd1a712f926a02a2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa56a080b16556e780cf25e9f7f8e83eb971b0fb00b129854da6055df2215a33(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__311faa50e75a507ea03c2abd5bd988f5c72d99cfaefa2e86e5e251f9899602d9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5cd4df574e763901374c8caf0547d7f887b99d85217082cce9286f37fedcdfa1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ad867a959e9d99af0bb88fc76ea31ed3df6aa5fc84c8d7cda623a2396d7de17(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f89ad155f332c3b84a198bb2577f5177af1048f2350173c9d61ba13d9f325b09(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95d03ab14a494e1e7ed359e0d72fa823ae311bf72b20b0f903a3fefb1249114a(
    value: typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAzureDisk],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ac3ece09a4d6ec3ba1829cb4357a9b4465b6570d653ca27120ebd40fde1e7f8(
    *,
    secret_name: builtins.str,
    share_name: builtins.str,
    read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    secret_namespace: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28edb90ed8ae7f47d594a85d6fb624467755dbc7c92fbc7d4d040d266a759652(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5c5cd63a76bb3c039f3e15c22b81e044fc0c598da9a24b17aefb8bcddc0cf89(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d9ed3dbe864f607be7cbc0089eb4d9612fdf3155f8f27bdb0bf735de50e66e6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2538fc6416227a3a30108812bfd1a48965984b2cadeac63007c4ee0257c463f6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8bd55424b9a283c5d40f202ab53428eafc4ff7b873a1e5064000c09e0f4b103(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__738f901648a3d0b3990c51ef2ef9670b99dba39b570edf1fb7f26d9cf8ec0a94(
    value: typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceAzureFile],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdcdc45d073fdaa2c763184b851d302bc46199909ca5ea212a22e99e587fb1e2(
    *,
    monitors: typing.Sequence[builtins.str],
    path: typing.Optional[builtins.str] = None,
    read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    secret_file: typing.Optional[builtins.str] = None,
    secret_ref: typing.Optional[typing.Union[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCephFsSecretRef, typing.Dict[builtins.str, typing.Any]]] = None,
    user: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3488d295f60f308cb06f30741be492c84fa722255824b30665a448e3ca3fba16(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16baf5430605724bfab8071e8ca724db5bb9e4f183a9f05f87e07f799d8b060d(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd37e16588ff102132af10def9115ea63cec1487341f4cd20e84b82dfcd9f308(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d19023a785f6165e7853c064ad2ce3924e1d0310cae21299bb8dff675b67bd23(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1dd384b118df4bb807f6a04d5c0893ad2205a0105b561dc67f7315370ab69eb5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c69958dc6ab56e68c1dd46ac717ae3efa4ab1936358a8050fe2dbb1c124ce2a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3337c44b732676a63cfcd61ba80557009a02fe34cdfe0eadb6640a8a8a2681fc(
    value: typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCephFs],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e0cd02aea472dc4ed36725d72d2508ce37ff8415ecc7b83313df72e218ee31a(
    *,
    name: typing.Optional[builtins.str] = None,
    namespace: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2069edbfbb364d4f034f8afbd0b794aa6db0885272534f8b6042884cb8fad175(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc6dcd3eb7d36809dd8061bf18ae4f666b385950e4b8e7064105ef59f1c3d1c2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__120cdb9c74f187861bca77086c6170eb837dc0916cf179c8701bf5eec9207811(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93a92d18b7341525fc16258b86730d126b99a83215b85a4800f47efd6452871f(
    value: typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCephFsSecretRef],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec56642d8343576e0754786703d9e36f153d4782718b1ac5668912a9835bd6a3(
    *,
    volume_id: builtins.str,
    fs_type: typing.Optional[builtins.str] = None,
    read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ba1243103601444549492729b8737027309b2d50b745a54177edef31418b77e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f08c07db653f737e53340bd7262fb20255cf72e1b8143932f4ac2787c4c702b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__385812c0b9ae3e30529c506c27f9c162a13d66a41eaeb613e2d48da1cd6f96a6(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ecfd7da1842b45f8da798f2cb1ae6cbb289ad5ed6a2fa1fd19fd23cb31addd1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff7d064fec3e65f439f523bf2b0a19ee13b516b104d8308803e4c2c4f278f40d(
    value: typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCinder],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9961d99ede4f46ceeaf0465e2ce999eac04cf6ba23ba45b21d0a55d5bd068ba0(
    *,
    driver: builtins.str,
    volume_handle: builtins.str,
    controller_expand_secret_ref: typing.Optional[typing.Union[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiControllerExpandSecretRef, typing.Dict[builtins.str, typing.Any]]] = None,
    controller_publish_secret_ref: typing.Optional[typing.Union[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiControllerPublishSecretRef, typing.Dict[builtins.str, typing.Any]]] = None,
    fs_type: typing.Optional[builtins.str] = None,
    node_publish_secret_ref: typing.Optional[typing.Union[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiNodePublishSecretRef, typing.Dict[builtins.str, typing.Any]]] = None,
    node_stage_secret_ref: typing.Optional[typing.Union[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiNodeStageSecretRef, typing.Dict[builtins.str, typing.Any]]] = None,
    read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    volume_attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8110c2f55bdc756acaafa38cfbd0419213946ab715c89524edace0c0e40203a(
    *,
    name: typing.Optional[builtins.str] = None,
    namespace: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e36acb8095eb6533df9d5e5e4bfb8d7c1341993a1447d856d01f53a95cf5622(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3d775212ac1aa75a834044c3e9abc84b4e6a99dd5ccaca122887692ab4c38bb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b72d8d4ccfd37a3e3554f1c8b52ef996c82125a36428168cac776397fe793b0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70b6791a51f4c4bcf7a8f2c42f66a6a768e25a1e414addfffb6d3ebe87a2411b(
    value: typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiControllerExpandSecretRef],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73a8fd04f1e794d0f935e7f6f05b31e0aba0434c7ab0d6623f069f21dc69ada5(
    *,
    name: typing.Optional[builtins.str] = None,
    namespace: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc0eda3cfd401fd512e8da681a3aedb7383c365227ad19707015cbee56905687(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2142e929bbff211778f768c6998b4ee06b8da3eb6527921f28104eaafe751dc4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7fc095ca30fc35863439f549c02b21481267203274fad6e18ade63c4c5c5c27(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55de99e5dd46ccb51d4580c45c5f1c2d9187ea3febfeef86623908c93e81ac1a(
    value: typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiControllerPublishSecretRef],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__897c0c857d094f8880a83ce5adb4d36298193fcda25657f7fb7d4b9b76c193c0(
    *,
    name: typing.Optional[builtins.str] = None,
    namespace: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7b8764111a43cb47897968f146502a46a7fe0cd760a3f5503fc77917683b71e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18fe40a15a0acbd9081a5681dfc16dfd2c276c8a968a936a1d66c3651b224853(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d6f45d20630173fa5b550b9d67e4636c9d887673827480c718934385a98271d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a8f9963d3cfa92e51f08d99e90e035b4b7b7dc37dfdedae6d0140a47a9da6d2(
    value: typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiNodePublishSecretRef],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc6390703e69fa3ab6fb1603e58fae3f28bd97349f1ada3a77446436164ff949(
    *,
    name: typing.Optional[builtins.str] = None,
    namespace: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24ccd060a25833975aa81efc8553c92b12c4a385a6440842ea6adb1bc2e64132(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22dccc53583e5ba5cd82594d0be3e132b094a4ce88e5714516ebf3e55355051b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0aaa602794b6e248d0aeab18edaee7ff86219427a55ffeeb2a2fac32d646fa67(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12916cc1fc155c8e0776636f16833446bb0b0bdc209f1d1561f269aba47d0d20(
    value: typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsiNodeStageSecretRef],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f78446d608cad5f526dc06bdddbd9f08232b7cc50d58f31058547530d569beeb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__815ee8d3d1292e57bb3e0ae293c898c8f091d82c536ca8e1da304ab2862df521(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dcdb53e7bf80a00a0cdf1f054398157263e43a8046cf584822fbd5e2318bcb86(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e06b7b301dd961bf33061880079f0895563b338641ec04e3f0f3e47493699fb(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab2e77e3fc9bfff66c1fb8faa7bd95f30c624ed3de30b54e05fa7e6d80e58356(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75285012f40ff74d2f23ee6fddb27928f28e35b0492db32d8708871fc2764ee4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5f5e2a4871a7ba63e88f67b25b67fe05f0fc2ec120bb637b6a055a495286b23(
    value: typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceCsi],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__734a0ec675ed8aded439a1244b00a9b34799d5fd8c2f8da587fdcddca24c9bdf(
    *,
    lun: jsii.Number,
    target_ww_ns: typing.Sequence[builtins.str],
    fs_type: typing.Optional[builtins.str] = None,
    read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2af07bdbe4c4a26523a9ca8e942e3a0e5367798a227733ecbcd7165591e6a1c7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__244833c926e090c48cad82151e81f861aaca72a0eb13d3ef7480778bbd9589a3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4fdda6dede5bd3443c941f9f4ef463bfb75ae6c7d36af354eb17e3b0b2267fb9(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efe316a2feaac1f539d881e8b7fccee1b4f321009d2ab589590aadc5657c8f0b(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d813d87a633e6bc299c4c947a5a3ae11beb63e47c4481a2a08c99d210b6e3ea8(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0edc8e65d3b2ccff8fa8dd5ecb432b32ed64c77caae1683604c286257de1f88(
    value: typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFc],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c64e3c574c49544d7b3e0ff9f906763ec9de9a632e1d98dca3240857ffd62a4b(
    *,
    driver: builtins.str,
    fs_type: typing.Optional[builtins.str] = None,
    options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    secret_ref: typing.Optional[typing.Union[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeSecretRef, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f7499d35f2687f4cb85bb1ac62cbefe3a139b4bba5c7d92cd6b06ab747697dd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__307aa899a7fa60f8305d4d4c2faba291e625f0dc01b7a02979cf29259b99490f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__391e133bf69252f478056c44ddbeef2b2d765ed6992a106bf9380339c84d4ff9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d8c064f8e2177481f4a60078b13760a08c8d3d4cb5f7198ffceab3eb27f09cf(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f589b3d740c0ef5097bf040f98994d314515ab9e371ac25c416f581fae070003(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea120be9558bb894319207528296aa750f920723db87c2d8cd7fd81a1a8f25b4(
    value: typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlexVolume],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf9bab4cddb22a51bbfc10d541d1a365f2ab5d36fcb3acdf693ea98baced07e5(
    *,
    name: typing.Optional[builtins.str] = None,
    namespace: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__659612f6de6e28a6b469cb05aa7ddc1a2e4755004b8897cf446b8be1d9fc87c4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f5529b453cba46b7fbcb55b6652018bd96aeb8412e4a837583d6ecc87579bc6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2bbf49b89908c88f441e712373b310a1aea8c62e0e29fb7c4bdede61162a497(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4112d00099c8438eab5bdd54986db92a27a74d30ce06d5c859f3159bd4ebf13(
    value: typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeSecretRef],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__174a60ac62c2497a02b62c642c8b5b59bb614f8cf627c84caeee32c6c4ee5adf(
    *,
    dataset_name: typing.Optional[builtins.str] = None,
    dataset_uuid: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__313792389b79b77ba18552e8665e5e0076e280f084e7ffed99095fa59a622acb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3fd249d9393404e55d0ab5e0855fec1257a4bd672a9c022e712e42b385aa67ef(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8f25ea600663cf48db7aec27fd4a5f6d7970a5ce0cfadc8a131102eb407aabf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__425f18743b5173c10cd31a6c840e26c7ff8d9cefc46f2d75ba2a8daadb1bf9a4(
    value: typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceFlocker],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bceb8d8c32fac051598f31a10990762241ed709ee041c0b9a5c13e12504e3996(
    *,
    pd_name: builtins.str,
    fs_type: typing.Optional[builtins.str] = None,
    partition: typing.Optional[jsii.Number] = None,
    read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c4cfd3f659728a12d77921736b2f931e200e0ae2d64c77f0effdaf0ce12e5c8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8db1550f3fc2dfe8f98aa5e7d50294fd6abe166d61ac0566a9a4335b36b113ca(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af14d6391891659d266026fdb1861dabb5b81e609238b5c9d946238d57eab503(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09206653490521ba1ccaee088c42ad53d3bff2863c8b27f863e63ba27cce9b60(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0df4b0574d232374d06ecbb05a8442a6b0e175e344f144d4f4fc30589155b6b2(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c652c8187906a5879b23334eaff956d00893957c334132a8c7798bf2be4045fd(
    value: typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceGcePersistentDisk],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__782d8ea383b004ce0275f91289514b69b3dbcf9554ccbacd2587a6c90ba31e59(
    *,
    endpoints_name: builtins.str,
    path: builtins.str,
    read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb76a3266bebec7cbfc9883a065e33317b16f03e858fc38bc01862f1bb72a1c0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1c2922bd3a483abb2241b47f15e42694f9bc6c71739c5a5e65d068f0e7487eb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea07f1fe51a145addc65cf5c881f25d982ab8b37218601647c1c1974445e3ecb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7a42fc9c4f24d6e77845d1625c37809fa4ac0b5976e0925c0505f3a8726a845(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75ac70738dc84eb8e9e531f1f175ffcfb07f9380738f4502f4464f8d3b393165(
    value: typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceGlusterfs],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cac55bdba17cef547f2dd204e83aa8d306a0be4e4ab2faa47dfd3687f610826e(
    *,
    path: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44323cc6d7f21f65b0a158d4dc13aaae6b1fcdc9c058d91ec3dbfeaeae0e02bf(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6723916cc813d1878aaf30ab89a3428da685018d7a65fa63bd9699bd38eb7455(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ce2a71e4de54d36823594e9713349263b3bcbff16fa06ae66b5bc58eb01bdb7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c3bcae10bed0d653a8ef3a49e72191778dbcf050f8ad4b7b7e19801c57c7a3f(
    value: typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceHostPath],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc6889c860859f093cb665fb948824eb2e7075ddc1d44e252649bafa2293691e(
    *,
    iqn: builtins.str,
    target_portal: builtins.str,
    fs_type: typing.Optional[builtins.str] = None,
    iscsi_interface: typing.Optional[builtins.str] = None,
    lun: typing.Optional[jsii.Number] = None,
    read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ba4ca622f989c50926546da7e784abd417ce086713248f7ece3c3d1f2163ea5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c06735dbfbf7aa17ac01b497d1e6ea80a5093ae573d5c65a1b1af196af5654e6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac327e636947eeb194bc232ad0c24fe1330a79675579fec45e2b8b623625f6d8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3204a1c55301427324f4903dacbdbe3d799c1d49c87980440c2ddd6b535740b1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e5943d9cd3efabece4b26a8b1d143e0ac7a819b7d02777976cb3b7d540e7d5e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4bdad44adaacfa338806ebeed891f866e702eed535da11c73c1d583d8589cf8(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2e2f04d7f58ab6ed8de07fe9c103526f5ba3810cffe4cd38942c58f751ed2fd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08c2d374e4c62ebdd19d71d171bfd4946b7b46529fbc2e16e7aaaf72f3fa9786(
    value: typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceIscsi],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e409bed12e5554bf4d137e1031330785736c3c0902a66f3d09da1392e1ddbbc1(
    *,
    path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__157a24630a91bc14435bb8e806205db3d42ad77a20428e38ccadef759ceb097c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d1e2c398e980dafaa72397f4c5c6924c5fe2c97a4a328c7b55b708cfa8828a9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3cfc2f527519a8930aed66240e063abb14cd0eb2f4ea7d6a3ae3ea0b0e1b34b6(
    value: typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceLocal],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13498673ceae143fa31f6141f0699191b409c6f87b45b19a01ccad8ad20d3aa7(
    *,
    path: builtins.str,
    server: builtins.str,
    read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21167250b0e5ff3345fec53625853d0b44f66d4fa6dfe3cda5f0f8dcbc19ff43(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac69ed966e39bd9fa5fc75587bc35e73c5ca6c19a5db14d270ccf5a553556dba(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccb149f7814dc012c1289282bcab5d69c4dcbc4867b6f68a5cbcce46695cfd8b(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3dc99563e6bd902629222147e123624c707cdf1f5dc50c82a7ab2a58020190a7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab2d1ee45272767e2b4dea846d4baf925a1174a9d24a6ea477cbfc2e7ec2b3f8(
    value: typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceNfs],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f0d918c7e23ad59464986451f7af63da4bc4f4c97dc58b31ed61b48be98f42b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8bd5a34e5f2d6d050257cb981c1664272c357895346bd561c145b70416ef7ed3(
    value: typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSource],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc64369077a4a86adc3688db338be21ad212d7ff8307f39fda46cf9339960011(
    *,
    pd_id: builtins.str,
    fs_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a06f9d8484a2fa5f01e5ca77094cbafaae82ddfed6f716f8932a1b6dbf448288(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58846d4492865a4270c4c4c924efdcbb6c0a2e116ed1b1a345a8b4d2c7ca046d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__700b591852fd1e8d77d28ef88e5eebf54705a5b24299dd3975f4b74e490e2f5f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aebad767e846ae6e914b42eaf81401d3939a1384eb0ef52595692127b906ec0d(
    value: typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourcePhotonPersistentDisk],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa06c1f399486e1037074042d5de0708ca013c96a5881e1b63f09d60c88d9df9(
    *,
    registry: builtins.str,
    volume: builtins.str,
    group: typing.Optional[builtins.str] = None,
    read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    user: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8579a3fc181e3efa3f0ef66111afc6055e0e3d3cb2a65fb2fbd71909c17f71e0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__744c6df6bba43e06002ef053afb271d2ee1f3316bfe2a9ac30ee90c7d3421a21(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f12535a80f1d7fb827ce84f91b72da9437fe7928c77293a5b4d8bf0cba342b16(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__481c3e8b78b255dc28c69b3701dbebdd397d9268b7440f0f15a29bd247c9f087(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa64b50e072742f60fc31aca9e9332edc0c968dc8c5640c13b7fb2271048da5a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ddd86e5c35605fd100a178d123950f57903daeb5f9356a914b8ba1a85cbd7f7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ded2c7e5bc0a7120eba0290750e9bdff64c9459c1936addbcb7f632ee1cc4518(
    value: typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceQuobyte],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f9ed4348c81630d621bb98ec511a9407f18af55d90b7db8af265e8586ce4186(
    *,
    ceph_monitors: typing.Sequence[builtins.str],
    rbd_image: builtins.str,
    fs_type: typing.Optional[builtins.str] = None,
    keyring: typing.Optional[builtins.str] = None,
    rados_user: typing.Optional[builtins.str] = None,
    rbd_pool: typing.Optional[builtins.str] = None,
    read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    secret_ref: typing.Optional[typing.Union[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceRbdSecretRef, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a96c74a440429e9339d4f98a92e28cf08553ce8c1e79b9ed40cdbb20e8c1838(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__437060bca7b2a98444937e007d3d9f29d33ac019aa4ae424b4c81eb3a3c006df(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75eef44593b85fe6726236e59f2edc0242fe46971d384b2695e70c4b6efc059b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__456abd1cc8331f7f835bf779e8353e99ee41bb6cfd0cdcd2b7c0c9b4b013820c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f6d2e2f3f135f19cc32ae3e9163a98b919eb1222c1a4bf3f6dcb1a908acf90c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06393f2b56a29ec2d33bcf4e08e04bae4b56572d2b48d504e3601fcd6c8a05e5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b7e45e573340bb358705078de903d8f718e6afbc0d02cc780dd2f1489b9cd18(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a13a485667ecb7b43c9009bd7b8234bbed1b6aa0708b0899df31ce3888da7bc8(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__948532c00736e4090c4f9a74debccc7dfa196638ca7dd544fbf8aac651f806b5(
    value: typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceRbd],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__294e7155d3f30dec618a99b7496ebcdf4e91169cf9ec9ad24e023ce845bfac21(
    *,
    name: typing.Optional[builtins.str] = None,
    namespace: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__630e9d4d89137a7fb975ca0bb7f199ea137ed91d98847eb0ebba8a0e12668467(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec6c7a2b2b221921f50fede1f32d489e775a554856ce5cfb288da6ace6a10e94(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aad1747ab993f3a51e2e561da2eab1205b9103fb4d5bd4853926b734807624ee(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73c5c9ace53f59cff8f6d1f4dea2f6a54903cb9cc1994330ebde1cda3a0ba024(
    value: typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceRbdSecretRef],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39fd40c52e9a2b01f1f4a492ff9d43c367ee1d49e28bfcf4f0399f60eec2123f(
    *,
    volume_path: builtins.str,
    fs_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26792b7ca98774aa0fcd9013ec078f9168debf4301ba551965a25d7e9e819d6f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9211211713d8e673309da36caa80f7a9cc579a0d16782683985b4fb06f96a50(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5c00b6ae273ac0181b7171f4b5c4b0f30ac1ffc9862240c4cb80dfcf1f37d80(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb0aa86f5e770916d4ca4116c6af0c2a05307304e778000184c3c67d887527d9(
    value: typing.Optional[DataKubernetesPersistentVolumeV1SpecPersistentVolumeSourceVsphereVolume],
) -> None:
    """Type checking stubs"""
    pass
