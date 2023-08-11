'''
# `kubernetes_endpoint_slice_v1`

Refer to the Terraform Registory for docs: [`kubernetes_endpoint_slice_v1`](https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1).
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


class EndpointSliceV1(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.endpointSliceV1.EndpointSliceV1",
):
    '''Represents a {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1 kubernetes_endpoint_slice_v1}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        address_type: builtins.str,
        endpoint: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EndpointSliceV1Endpoint", typing.Dict[builtins.str, typing.Any]]]],
        metadata: typing.Union["EndpointSliceV1Metadata", typing.Dict[builtins.str, typing.Any]],
        port: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EndpointSliceV1Port", typing.Dict[builtins.str, typing.Any]]]],
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1 kubernetes_endpoint_slice_v1} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param address_type: address_type specifies the type of address carried by this EndpointSlice. All addresses in this slice must be the same type. This field is immutable after creation. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#address_type EndpointSliceV1#address_type}
        :param endpoint: endpoint block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#endpoint EndpointSliceV1#endpoint}
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#metadata EndpointSliceV1#metadata}
        :param port: port block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#port EndpointSliceV1#port}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#id EndpointSliceV1#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4e3c865e2d78f1c436f565d8037fe2691fbeeaf5eddc7d664948e5c060744ef)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = EndpointSliceV1Config(
            address_type=address_type,
            endpoint=endpoint,
            metadata=metadata,
            port=port,
            id=id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putEndpoint")
    def put_endpoint(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EndpointSliceV1Endpoint", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49029da97b9a11e53ababb5cfa6e0a06d2773cbfd64fc915f25c3a6a9f192bad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEndpoint", [value]))

    @jsii.member(jsii_name="putMetadata")
    def put_metadata(
        self,
        *,
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        generate_name: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param annotations: An unstructured key value map stored with the endpoint_slice that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#annotations EndpointSliceV1#annotations}
        :param generate_name: Prefix, used by the server, to generate a unique name ONLY IF the ``name`` field has not been provided. This value will also be combined with a unique suffix. Read more: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#idempotency Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#generate_name EndpointSliceV1#generate_name}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the endpoint_slice. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#labels EndpointSliceV1#labels}
        :param name: Name of the endpoint_slice, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#name EndpointSliceV1#name}
        :param namespace: Namespace defines the space within which name of the endpoint_slice must be unique. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#namespace EndpointSliceV1#namespace}
        '''
        value = EndpointSliceV1Metadata(
            annotations=annotations,
            generate_name=generate_name,
            labels=labels,
            name=name,
            namespace=namespace,
        )

        return typing.cast(None, jsii.invoke(self, "putMetadata", [value]))

    @jsii.member(jsii_name="putPort")
    def put_port(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EndpointSliceV1Port", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98e946a37e23b9f882f5e190d57b19f9b417aac7a424889ddab08128b6ddfcfe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPort", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> "EndpointSliceV1EndpointList":
        return typing.cast("EndpointSliceV1EndpointList", jsii.get(self, "endpoint"))

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> "EndpointSliceV1MetadataOutputReference":
        return typing.cast("EndpointSliceV1MetadataOutputReference", jsii.get(self, "metadata"))

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> "EndpointSliceV1PortList":
        return typing.cast("EndpointSliceV1PortList", jsii.get(self, "port"))

    @builtins.property
    @jsii.member(jsii_name="addressTypeInput")
    def address_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "addressTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointInput")
    def endpoint_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EndpointSliceV1Endpoint"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EndpointSliceV1Endpoint"]]], jsii.get(self, "endpointInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataInput")
    def metadata_input(self) -> typing.Optional["EndpointSliceV1Metadata"]:
        return typing.cast(typing.Optional["EndpointSliceV1Metadata"], jsii.get(self, "metadataInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EndpointSliceV1Port"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EndpointSliceV1Port"]]], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="addressType")
    def address_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "addressType"))

    @address_type.setter
    def address_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e29385243555acd53e3030f2aaa212f36dc5673cb22d304c10910396b07a95b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "addressType", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__053d1adb6e12ded372d8f90de85c911a9e73091124377670437c6b49b9613bc7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="kubernetes.endpointSliceV1.EndpointSliceV1Config",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "address_type": "addressType",
        "endpoint": "endpoint",
        "metadata": "metadata",
        "port": "port",
        "id": "id",
    },
)
class EndpointSliceV1Config(_cdktf_9a9027ec.TerraformMetaArguments):
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
        address_type: builtins.str,
        endpoint: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EndpointSliceV1Endpoint", typing.Dict[builtins.str, typing.Any]]]],
        metadata: typing.Union["EndpointSliceV1Metadata", typing.Dict[builtins.str, typing.Any]],
        port: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EndpointSliceV1Port", typing.Dict[builtins.str, typing.Any]]]],
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param address_type: address_type specifies the type of address carried by this EndpointSlice. All addresses in this slice must be the same type. This field is immutable after creation. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#address_type EndpointSliceV1#address_type}
        :param endpoint: endpoint block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#endpoint EndpointSliceV1#endpoint}
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#metadata EndpointSliceV1#metadata}
        :param port: port block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#port EndpointSliceV1#port}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#id EndpointSliceV1#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(metadata, dict):
            metadata = EndpointSliceV1Metadata(**metadata)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ffa6fa15b18acf452017e0ec92e261fd1feb81bf692f304c8d54224ce410820)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument address_type", value=address_type, expected_type=type_hints["address_type"])
            check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "address_type": address_type,
            "endpoint": endpoint,
            "metadata": metadata,
            "port": port,
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
    def address_type(self) -> builtins.str:
        '''address_type specifies the type of address carried by this EndpointSlice.

        All addresses in this slice must be the same type. This field is immutable after creation.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#address_type EndpointSliceV1#address_type}
        '''
        result = self._values.get("address_type")
        assert result is not None, "Required property 'address_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def endpoint(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EndpointSliceV1Endpoint"]]:
        '''endpoint block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#endpoint EndpointSliceV1#endpoint}
        '''
        result = self._values.get("endpoint")
        assert result is not None, "Required property 'endpoint' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EndpointSliceV1Endpoint"]], result)

    @builtins.property
    def metadata(self) -> "EndpointSliceV1Metadata":
        '''metadata block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#metadata EndpointSliceV1#metadata}
        '''
        result = self._values.get("metadata")
        assert result is not None, "Required property 'metadata' is missing"
        return typing.cast("EndpointSliceV1Metadata", result)

    @builtins.property
    def port(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EndpointSliceV1Port"]]:
        '''port block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#port EndpointSliceV1#port}
        '''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EndpointSliceV1Port"]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#id EndpointSliceV1#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EndpointSliceV1Config(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kubernetes.endpointSliceV1.EndpointSliceV1Endpoint",
    jsii_struct_bases=[],
    name_mapping={
        "addresses": "addresses",
        "condition": "condition",
        "hostname": "hostname",
        "node_name": "nodeName",
        "target_ref": "targetRef",
        "zone": "zone",
    },
)
class EndpointSliceV1Endpoint:
    def __init__(
        self,
        *,
        addresses: typing.Sequence[builtins.str],
        condition: typing.Union["EndpointSliceV1EndpointCondition", typing.Dict[builtins.str, typing.Any]],
        hostname: typing.Optional[builtins.str] = None,
        node_name: typing.Optional[builtins.str] = None,
        target_ref: typing.Optional[typing.Union["EndpointSliceV1EndpointTargetRef", typing.Dict[builtins.str, typing.Any]]] = None,
        zone: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param addresses: addresses of this endpoint. The contents of this field are interpreted according to the corresponding EndpointSlice addressType field. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#addresses EndpointSliceV1#addresses}
        :param condition: condition block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#condition EndpointSliceV1#condition}
        :param hostname: hostname of this endpoint. This field may be used by consumers of endpoints to distinguish endpoints from each other. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#hostname EndpointSliceV1#hostname}
        :param node_name: nodeName represents the name of the Node hosting this endpoint. This can be used to determine endpoints local to a Node. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#node_name EndpointSliceV1#node_name}
        :param target_ref: target_ref block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#target_ref EndpointSliceV1#target_ref}
        :param zone: zone is the name of the Zone this endpoint exists in. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#zone EndpointSliceV1#zone}
        '''
        if isinstance(condition, dict):
            condition = EndpointSliceV1EndpointCondition(**condition)
        if isinstance(target_ref, dict):
            target_ref = EndpointSliceV1EndpointTargetRef(**target_ref)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ffe0771a4a6e6b84b676cd0a506d3e9056e785ad7597adde8126601b57e49521)
            check_type(argname="argument addresses", value=addresses, expected_type=type_hints["addresses"])
            check_type(argname="argument condition", value=condition, expected_type=type_hints["condition"])
            check_type(argname="argument hostname", value=hostname, expected_type=type_hints["hostname"])
            check_type(argname="argument node_name", value=node_name, expected_type=type_hints["node_name"])
            check_type(argname="argument target_ref", value=target_ref, expected_type=type_hints["target_ref"])
            check_type(argname="argument zone", value=zone, expected_type=type_hints["zone"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "addresses": addresses,
            "condition": condition,
        }
        if hostname is not None:
            self._values["hostname"] = hostname
        if node_name is not None:
            self._values["node_name"] = node_name
        if target_ref is not None:
            self._values["target_ref"] = target_ref
        if zone is not None:
            self._values["zone"] = zone

    @builtins.property
    def addresses(self) -> typing.List[builtins.str]:
        '''addresses of this endpoint. The contents of this field are interpreted according to the corresponding EndpointSlice addressType field.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#addresses EndpointSliceV1#addresses}
        '''
        result = self._values.get("addresses")
        assert result is not None, "Required property 'addresses' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def condition(self) -> "EndpointSliceV1EndpointCondition":
        '''condition block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#condition EndpointSliceV1#condition}
        '''
        result = self._values.get("condition")
        assert result is not None, "Required property 'condition' is missing"
        return typing.cast("EndpointSliceV1EndpointCondition", result)

    @builtins.property
    def hostname(self) -> typing.Optional[builtins.str]:
        '''hostname of this endpoint. This field may be used by consumers of endpoints to distinguish endpoints from each other.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#hostname EndpointSliceV1#hostname}
        '''
        result = self._values.get("hostname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def node_name(self) -> typing.Optional[builtins.str]:
        '''nodeName represents the name of the Node hosting this endpoint.

        This can be used to determine endpoints local to a Node.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#node_name EndpointSliceV1#node_name}
        '''
        result = self._values.get("node_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_ref(self) -> typing.Optional["EndpointSliceV1EndpointTargetRef"]:
        '''target_ref block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#target_ref EndpointSliceV1#target_ref}
        '''
        result = self._values.get("target_ref")
        return typing.cast(typing.Optional["EndpointSliceV1EndpointTargetRef"], result)

    @builtins.property
    def zone(self) -> typing.Optional[builtins.str]:
        '''zone is the name of the Zone this endpoint exists in.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#zone EndpointSliceV1#zone}
        '''
        result = self._values.get("zone")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EndpointSliceV1Endpoint(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kubernetes.endpointSliceV1.EndpointSliceV1EndpointCondition",
    jsii_struct_bases=[],
    name_mapping={
        "ready": "ready",
        "serving": "serving",
        "terminating": "terminating",
    },
)
class EndpointSliceV1EndpointCondition:
    def __init__(
        self,
        *,
        ready: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        serving: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        terminating: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param ready: ready indicates that this endpoint is prepared to receive traffic, according to whatever system is managing the endpoint. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#ready EndpointSliceV1#ready}
        :param serving: serving is identical to ready except that it is set regardless of the terminating state of endpoints. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#serving EndpointSliceV1#serving}
        :param terminating: terminating indicates that this endpoint is terminating. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#terminating EndpointSliceV1#terminating}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6ec654f7c8ef61ff806dd9f4bf703bb374268e6f482b218b80e524da41a27e5)
            check_type(argname="argument ready", value=ready, expected_type=type_hints["ready"])
            check_type(argname="argument serving", value=serving, expected_type=type_hints["serving"])
            check_type(argname="argument terminating", value=terminating, expected_type=type_hints["terminating"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if ready is not None:
            self._values["ready"] = ready
        if serving is not None:
            self._values["serving"] = serving
        if terminating is not None:
            self._values["terminating"] = terminating

    @builtins.property
    def ready(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''ready indicates that this endpoint is prepared to receive traffic, according to whatever system is managing the endpoint.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#ready EndpointSliceV1#ready}
        '''
        result = self._values.get("ready")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def serving(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''serving is identical to ready except that it is set regardless of the terminating state of endpoints.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#serving EndpointSliceV1#serving}
        '''
        result = self._values.get("serving")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def terminating(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''terminating indicates that this endpoint is terminating.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#terminating EndpointSliceV1#terminating}
        '''
        result = self._values.get("terminating")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EndpointSliceV1EndpointCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EndpointSliceV1EndpointConditionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.endpointSliceV1.EndpointSliceV1EndpointConditionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5557dfd1a43c0d7083071328cbc11a251ad753f061cabcefd49404dab3bc7f13)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetReady")
    def reset_ready(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReady", []))

    @jsii.member(jsii_name="resetServing")
    def reset_serving(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServing", []))

    @jsii.member(jsii_name="resetTerminating")
    def reset_terminating(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTerminating", []))

    @builtins.property
    @jsii.member(jsii_name="readyInput")
    def ready_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "readyInput"))

    @builtins.property
    @jsii.member(jsii_name="servingInput")
    def serving_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "servingInput"))

    @builtins.property
    @jsii.member(jsii_name="terminatingInput")
    def terminating_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "terminatingInput"))

    @builtins.property
    @jsii.member(jsii_name="ready")
    def ready(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "ready"))

    @ready.setter
    def ready(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__713290705d65dd44d04ccf00d3845037e62a30dbfd290cafc7da2ebf100a3349)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ready", value)

    @builtins.property
    @jsii.member(jsii_name="serving")
    def serving(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "serving"))

    @serving.setter
    def serving(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__277db840f77d76a713c026fa1fa0819e32b02dcf022624e44cbfa125fb5f2b01)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serving", value)

    @builtins.property
    @jsii.member(jsii_name="terminating")
    def terminating(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "terminating"))

    @terminating.setter
    def terminating(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__286917a644569c597c801dd958479a5077120eb7dab4d5dee4721d4a48121af3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terminating", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EndpointSliceV1EndpointCondition]:
        return typing.cast(typing.Optional[EndpointSliceV1EndpointCondition], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EndpointSliceV1EndpointCondition],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a741e8acb6980ac39760c14a629b374ab85d536df77bd8fdf8b5e0b4b5546ef0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EndpointSliceV1EndpointList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.endpointSliceV1.EndpointSliceV1EndpointList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__342fcfc38dce3ce8b5fe21ddcce00f05e9d84e3cc155c7f9051f3b73e20f6ca4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "EndpointSliceV1EndpointOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97b4e90e2ca262b6da60aad521179c94c5cc2f22dd3d9d1d85130838675a2afb)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EndpointSliceV1EndpointOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3dd534f26291aef18e564f8e3378c22d924dddab8ab6e05d2754f3194ff1efa)
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
            type_hints = typing.get_type_hints(_typecheckingstub__95db39342b4cb25b01930c17e68fab5f0ff42b4b6a57500ea34153ed61f0ed67)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7ce8ff7fbd9c7c93a8b67e951375ed36ef3763d03743ad6a5a1a4ca2e21f0671)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EndpointSliceV1Endpoint]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EndpointSliceV1Endpoint]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EndpointSliceV1Endpoint]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f39e44036c2c7d4284232d0b7ad96effbddb1818b14bb8f4b25de0ce86ff6fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EndpointSliceV1EndpointOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.endpointSliceV1.EndpointSliceV1EndpointOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c44bc40e095c86bb6020bc214c4a3820a1beb789fe27538891500a5388fd7e1d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putCondition")
    def put_condition(
        self,
        *,
        ready: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        serving: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        terminating: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param ready: ready indicates that this endpoint is prepared to receive traffic, according to whatever system is managing the endpoint. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#ready EndpointSliceV1#ready}
        :param serving: serving is identical to ready except that it is set regardless of the terminating state of endpoints. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#serving EndpointSliceV1#serving}
        :param terminating: terminating indicates that this endpoint is terminating. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#terminating EndpointSliceV1#terminating}
        '''
        value = EndpointSliceV1EndpointCondition(
            ready=ready, serving=serving, terminating=terminating
        )

        return typing.cast(None, jsii.invoke(self, "putCondition", [value]))

    @jsii.member(jsii_name="putTargetRef")
    def put_target_ref(
        self,
        *,
        name: builtins.str,
        field_path: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        resource_version: typing.Optional[builtins.str] = None,
        uid: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the referent. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#name EndpointSliceV1#name}
        :param field_path: If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#field_path EndpointSliceV1#field_path}
        :param namespace: Namespace of the referent. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#namespace EndpointSliceV1#namespace}
        :param resource_version: Specific resourceVersion to which this reference is made, if any. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#resource_version EndpointSliceV1#resource_version}
        :param uid: If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#uid EndpointSliceV1#uid}
        '''
        value = EndpointSliceV1EndpointTargetRef(
            name=name,
            field_path=field_path,
            namespace=namespace,
            resource_version=resource_version,
            uid=uid,
        )

        return typing.cast(None, jsii.invoke(self, "putTargetRef", [value]))

    @jsii.member(jsii_name="resetHostname")
    def reset_hostname(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostname", []))

    @jsii.member(jsii_name="resetNodeName")
    def reset_node_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodeName", []))

    @jsii.member(jsii_name="resetTargetRef")
    def reset_target_ref(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetRef", []))

    @jsii.member(jsii_name="resetZone")
    def reset_zone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZone", []))

    @builtins.property
    @jsii.member(jsii_name="condition")
    def condition(self) -> EndpointSliceV1EndpointConditionOutputReference:
        return typing.cast(EndpointSliceV1EndpointConditionOutputReference, jsii.get(self, "condition"))

    @builtins.property
    @jsii.member(jsii_name="targetRef")
    def target_ref(self) -> "EndpointSliceV1EndpointTargetRefOutputReference":
        return typing.cast("EndpointSliceV1EndpointTargetRefOutputReference", jsii.get(self, "targetRef"))

    @builtins.property
    @jsii.member(jsii_name="addressesInput")
    def addresses_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "addressesInput"))

    @builtins.property
    @jsii.member(jsii_name="conditionInput")
    def condition_input(self) -> typing.Optional[EndpointSliceV1EndpointCondition]:
        return typing.cast(typing.Optional[EndpointSliceV1EndpointCondition], jsii.get(self, "conditionInput"))

    @builtins.property
    @jsii.member(jsii_name="hostnameInput")
    def hostname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostnameInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeNameInput")
    def node_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nodeNameInput"))

    @builtins.property
    @jsii.member(jsii_name="targetRefInput")
    def target_ref_input(self) -> typing.Optional["EndpointSliceV1EndpointTargetRef"]:
        return typing.cast(typing.Optional["EndpointSliceV1EndpointTargetRef"], jsii.get(self, "targetRefInput"))

    @builtins.property
    @jsii.member(jsii_name="zoneInput")
    def zone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "zoneInput"))

    @builtins.property
    @jsii.member(jsii_name="addresses")
    def addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "addresses"))

    @addresses.setter
    def addresses(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91d2651e0f1726f6f0b41aa48818dc00caa93b37456b479155eb5fb1a84ee25a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "addresses", value)

    @builtins.property
    @jsii.member(jsii_name="hostname")
    def hostname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostname"))

    @hostname.setter
    def hostname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c8d2997435ea3212a831977d7fd0168635cccf40d45325cc3a875dfb3afb1e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostname", value)

    @builtins.property
    @jsii.member(jsii_name="nodeName")
    def node_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nodeName"))

    @node_name.setter
    def node_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08aff435c08532e83d425c6c0d4ca4a4c25f601eb21f0791a55097c0780b7062)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodeName", value)

    @builtins.property
    @jsii.member(jsii_name="zone")
    def zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zone"))

    @zone.setter
    def zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8dfad928b7e1e9c0716fd45d04d4d72fc80184f07a1b57c6c36ee3ecd0baf076)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zone", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, EndpointSliceV1Endpoint]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, EndpointSliceV1Endpoint]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, EndpointSliceV1Endpoint]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed3fdd97746ec038fe4f2b1a0bd9ece2a6c965974846441ef75c11dcd0ce6320)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.endpointSliceV1.EndpointSliceV1EndpointTargetRef",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "field_path": "fieldPath",
        "namespace": "namespace",
        "resource_version": "resourceVersion",
        "uid": "uid",
    },
)
class EndpointSliceV1EndpointTargetRef:
    def __init__(
        self,
        *,
        name: builtins.str,
        field_path: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        resource_version: typing.Optional[builtins.str] = None,
        uid: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the referent. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#name EndpointSliceV1#name}
        :param field_path: If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#field_path EndpointSliceV1#field_path}
        :param namespace: Namespace of the referent. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#namespace EndpointSliceV1#namespace}
        :param resource_version: Specific resourceVersion to which this reference is made, if any. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#resource_version EndpointSliceV1#resource_version}
        :param uid: If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#uid EndpointSliceV1#uid}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be1c80ceca4070e40b53a689f61a04eff69a8a2604a8e06f40bea27016ce0d42)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument field_path", value=field_path, expected_type=type_hints["field_path"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument resource_version", value=resource_version, expected_type=type_hints["resource_version"])
            check_type(argname="argument uid", value=uid, expected_type=type_hints["uid"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if field_path is not None:
            self._values["field_path"] = field_path
        if namespace is not None:
            self._values["namespace"] = namespace
        if resource_version is not None:
            self._values["resource_version"] = resource_version
        if uid is not None:
            self._values["uid"] = uid

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the referent.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#name EndpointSliceV1#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def field_path(self) -> typing.Optional[builtins.str]:
        '''If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2].

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#field_path EndpointSliceV1#field_path}
        '''
        result = self._values.get("field_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Namespace of the referent.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#namespace EndpointSliceV1#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resource_version(self) -> typing.Optional[builtins.str]:
        '''Specific resourceVersion to which this reference is made, if any.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#resource_version EndpointSliceV1#resource_version}
        '''
        result = self._values.get("resource_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def uid(self) -> typing.Optional[builtins.str]:
        '''If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2].

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#uid EndpointSliceV1#uid}
        '''
        result = self._values.get("uid")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EndpointSliceV1EndpointTargetRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EndpointSliceV1EndpointTargetRefOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.endpointSliceV1.EndpointSliceV1EndpointTargetRefOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a026cd0fd487a05c62d8f4e2470cd3b069f599895a3ebffe33a3dbddc871f466)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFieldPath")
    def reset_field_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFieldPath", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @jsii.member(jsii_name="resetResourceVersion")
    def reset_resource_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceVersion", []))

    @jsii.member(jsii_name="resetUid")
    def reset_uid(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUid", []))

    @builtins.property
    @jsii.member(jsii_name="fieldPathInput")
    def field_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fieldPathInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceVersionInput")
    def resource_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="uidInput")
    def uid_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "uidInput"))

    @builtins.property
    @jsii.member(jsii_name="fieldPath")
    def field_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fieldPath"))

    @field_path.setter
    def field_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48a07660ba8f4737a705c379c8f74431247543c9324e521e68af78fb0730f137)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fieldPath", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07de59c993971ae966487c8133d1079ce69739d0daa957421b17aadd045e4b25)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9fd925e186f63a7f3253b8a25b503c022be24cad6fb85a25b2b5e521e463243b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="resourceVersion")
    def resource_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceVersion"))

    @resource_version.setter
    def resource_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bba2f8ccd1a213b327b5167aa7e421a2c206dfe9f5cc60de57e2909ff5ca3a8a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceVersion", value)

    @builtins.property
    @jsii.member(jsii_name="uid")
    def uid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uid"))

    @uid.setter
    def uid(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c3f35457096822e824c5beb06b4ac4ab2d3c734fa525a8f859173f18c4411d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uid", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EndpointSliceV1EndpointTargetRef]:
        return typing.cast(typing.Optional[EndpointSliceV1EndpointTargetRef], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EndpointSliceV1EndpointTargetRef],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9b0330d7cabdb343a6f1fdf157d46f49d7781659ac07d77b0f3c92170f4d205)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.endpointSliceV1.EndpointSliceV1Metadata",
    jsii_struct_bases=[],
    name_mapping={
        "annotations": "annotations",
        "generate_name": "generateName",
        "labels": "labels",
        "name": "name",
        "namespace": "namespace",
    },
)
class EndpointSliceV1Metadata:
    def __init__(
        self,
        *,
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        generate_name: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param annotations: An unstructured key value map stored with the endpoint_slice that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#annotations EndpointSliceV1#annotations}
        :param generate_name: Prefix, used by the server, to generate a unique name ONLY IF the ``name`` field has not been provided. This value will also be combined with a unique suffix. Read more: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#idempotency Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#generate_name EndpointSliceV1#generate_name}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the endpoint_slice. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#labels EndpointSliceV1#labels}
        :param name: Name of the endpoint_slice, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#name EndpointSliceV1#name}
        :param namespace: Namespace defines the space within which name of the endpoint_slice must be unique. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#namespace EndpointSliceV1#namespace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__994d1cf6c6735eb8d39ffebbd297f2b88e458388395edf368f47134852024772)
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument generate_name", value=generate_name, expected_type=type_hints["generate_name"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if annotations is not None:
            self._values["annotations"] = annotations
        if generate_name is not None:
            self._values["generate_name"] = generate_name
        if labels is not None:
            self._values["labels"] = labels
        if name is not None:
            self._values["name"] = name
        if namespace is not None:
            self._values["namespace"] = namespace

    @builtins.property
    def annotations(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''An unstructured key value map stored with the endpoint_slice that may be used to store arbitrary metadata.

        More info: http://kubernetes.io/docs/user-guide/annotations

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#annotations EndpointSliceV1#annotations}
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def generate_name(self) -> typing.Optional[builtins.str]:
        '''Prefix, used by the server, to generate a unique name ONLY IF the ``name`` field has not been provided.

        This value will also be combined with a unique suffix. Read more: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#idempotency

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#generate_name EndpointSliceV1#generate_name}
        '''
        result = self._values.get("generate_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Map of string keys and values that can be used to organize and categorize (scope and select) the endpoint_slice.

        May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#labels EndpointSliceV1#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the endpoint_slice, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#name EndpointSliceV1#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Namespace defines the space within which name of the endpoint_slice must be unique.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#namespace EndpointSliceV1#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EndpointSliceV1Metadata(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EndpointSliceV1MetadataOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.endpointSliceV1.EndpointSliceV1MetadataOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__38e51924c42ca833958c930c677be200b2b1ba41b402e3baaa9a22ff28b03723)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAnnotations")
    def reset_annotations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnnotations", []))

    @jsii.member(jsii_name="resetGenerateName")
    def reset_generate_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGenerateName", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

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
    @jsii.member(jsii_name="generateNameInput")
    def generate_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "generateNameInput"))

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
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="annotations")
    def annotations(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "annotations"))

    @annotations.setter
    def annotations(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac6f034a6bd567476b0781686568b5387aea7a558f9fe9a498b4d1befe62c226)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "annotations", value)

    @builtins.property
    @jsii.member(jsii_name="generateName")
    def generate_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "generateName"))

    @generate_name.setter
    def generate_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6eac8d655ad4efbe0e32509893897ef53aed2ae41551f783789610b1e76978ca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "generateName", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c582c4666cdc9806437a956a3da228365887c8abeef7b1cda1aa4813a6b6a711)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb8aa6fb1083682f8c031645d8be633dfb459f8f7aff5eaed7f14db2aeb3f2c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ba3b31a1eca3c821e8420cc4602bc5db3888913325a455664b78718a5e7d3c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EndpointSliceV1Metadata]:
        return typing.cast(typing.Optional[EndpointSliceV1Metadata], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[EndpointSliceV1Metadata]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db9f5c5cdb1fae491d78a8478896dbe5fec632029139665c87eefbe1611a91d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.endpointSliceV1.EndpointSliceV1Port",
    jsii_struct_bases=[],
    name_mapping={
        "app_protocol": "appProtocol",
        "port": "port",
        "name": "name",
        "protocol": "protocol",
    },
)
class EndpointSliceV1Port:
    def __init__(
        self,
        *,
        app_protocol: builtins.str,
        port: builtins.str,
        name: typing.Optional[builtins.str] = None,
        protocol: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param app_protocol: The application protocol for this port. This is used as a hint for implementations to offer richer behavior for protocols that they understand. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#app_protocol EndpointSliceV1#app_protocol}
        :param port: port represents the port number of the endpoint. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#port EndpointSliceV1#port}
        :param name: name represents the name of this port. All ports in an EndpointSlice must have a unique name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#name EndpointSliceV1#name}
        :param protocol: protocol represents the IP protocol for this port. Must be UDP, TCP, or SCTP. Default is TCP. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#protocol EndpointSliceV1#protocol}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80d1534447a30d995294c0a7cca29a1fce1beeb855fbb76ae15b44ceb7a797e4)
            check_type(argname="argument app_protocol", value=app_protocol, expected_type=type_hints["app_protocol"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "app_protocol": app_protocol,
            "port": port,
        }
        if name is not None:
            self._values["name"] = name
        if protocol is not None:
            self._values["protocol"] = protocol

    @builtins.property
    def app_protocol(self) -> builtins.str:
        '''The application protocol for this port.

        This is used as a hint for implementations to offer richer behavior for protocols that they understand.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#app_protocol EndpointSliceV1#app_protocol}
        '''
        result = self._values.get("app_protocol")
        assert result is not None, "Required property 'app_protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port(self) -> builtins.str:
        '''port represents the port number of the endpoint.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#port EndpointSliceV1#port}
        '''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''name represents the name of this port. All ports in an EndpointSlice must have a unique name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#name EndpointSliceV1#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def protocol(self) -> typing.Optional[builtins.str]:
        '''protocol represents the IP protocol for this port. Must be UDP, TCP, or SCTP. Default is TCP.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/endpoint_slice_v1#protocol EndpointSliceV1#protocol}
        '''
        result = self._values.get("protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EndpointSliceV1Port(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EndpointSliceV1PortList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.endpointSliceV1.EndpointSliceV1PortList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8d43d550914ba607319f94c2a7b07b251e235c57da8e0fa6e098631859a452c2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "EndpointSliceV1PortOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c68e044de4e4d83f12c706dc40b063a5784396c6b7cfd17278d08bfe418e6efd)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EndpointSliceV1PortOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ddbe3447d4dafbfa9b9aa32f8a5146f795911c089bd46e5b5453aba207c0127)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3e52898a9ae36e781b9b603f7abf06e74a2247deeaac2917559427585fbde9bc)
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
            type_hints = typing.get_type_hints(_typecheckingstub__cc4f2e7807b7364429582e29b574c99eee31fd3252dd5e514e4bc9db17adbf94)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EndpointSliceV1Port]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EndpointSliceV1Port]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EndpointSliceV1Port]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e4854593275ace3862640f39a5b44c93bc700144c2eb6010b7bef2e0faa8294)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EndpointSliceV1PortOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.endpointSliceV1.EndpointSliceV1PortOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__bd2969a08d6eeeb59da7dcca5decf4f1838ad6aff9e160a0e4b12678343ebf78)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetProtocol")
    def reset_protocol(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProtocol", []))

    @builtins.property
    @jsii.member(jsii_name="appProtocolInput")
    def app_protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "appProtocolInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="appProtocol")
    def app_protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "appProtocol"))

    @app_protocol.setter
    def app_protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3401361450021cf3fbaa64d844952a7e805f4ff2fe044c9944e4f101f58c48df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appProtocol", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__088883997d0df4de80a452bb705d26dc1a17bde4d215656ce05d9ed216413a60)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "port"))

    @port.setter
    def port(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89610e5795384ada18f47ba1e0dc71ce2070ee6baf50445d26913b92b1e77b57)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73ad6bb78ac4c17b7bd94787dfe1a3cbda3af61227c6e73d01ade453be780df9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, EndpointSliceV1Port]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, EndpointSliceV1Port]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, EndpointSliceV1Port]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85055bf04bbf90bec88cbd785295bdc2842d4abe24b40cff20c7cf9cb1906800)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "EndpointSliceV1",
    "EndpointSliceV1Config",
    "EndpointSliceV1Endpoint",
    "EndpointSliceV1EndpointCondition",
    "EndpointSliceV1EndpointConditionOutputReference",
    "EndpointSliceV1EndpointList",
    "EndpointSliceV1EndpointOutputReference",
    "EndpointSliceV1EndpointTargetRef",
    "EndpointSliceV1EndpointTargetRefOutputReference",
    "EndpointSliceV1Metadata",
    "EndpointSliceV1MetadataOutputReference",
    "EndpointSliceV1Port",
    "EndpointSliceV1PortList",
    "EndpointSliceV1PortOutputReference",
]

publication.publish()

def _typecheckingstub__b4e3c865e2d78f1c436f565d8037fe2691fbeeaf5eddc7d664948e5c060744ef(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    address_type: builtins.str,
    endpoint: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EndpointSliceV1Endpoint, typing.Dict[builtins.str, typing.Any]]]],
    metadata: typing.Union[EndpointSliceV1Metadata, typing.Dict[builtins.str, typing.Any]],
    port: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EndpointSliceV1Port, typing.Dict[builtins.str, typing.Any]]]],
    id: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__49029da97b9a11e53ababb5cfa6e0a06d2773cbfd64fc915f25c3a6a9f192bad(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EndpointSliceV1Endpoint, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98e946a37e23b9f882f5e190d57b19f9b417aac7a424889ddab08128b6ddfcfe(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EndpointSliceV1Port, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e29385243555acd53e3030f2aaa212f36dc5673cb22d304c10910396b07a95b2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__053d1adb6e12ded372d8f90de85c911a9e73091124377670437c6b49b9613bc7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ffa6fa15b18acf452017e0ec92e261fd1feb81bf692f304c8d54224ce410820(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    address_type: builtins.str,
    endpoint: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EndpointSliceV1Endpoint, typing.Dict[builtins.str, typing.Any]]]],
    metadata: typing.Union[EndpointSliceV1Metadata, typing.Dict[builtins.str, typing.Any]],
    port: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EndpointSliceV1Port, typing.Dict[builtins.str, typing.Any]]]],
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffe0771a4a6e6b84b676cd0a506d3e9056e785ad7597adde8126601b57e49521(
    *,
    addresses: typing.Sequence[builtins.str],
    condition: typing.Union[EndpointSliceV1EndpointCondition, typing.Dict[builtins.str, typing.Any]],
    hostname: typing.Optional[builtins.str] = None,
    node_name: typing.Optional[builtins.str] = None,
    target_ref: typing.Optional[typing.Union[EndpointSliceV1EndpointTargetRef, typing.Dict[builtins.str, typing.Any]]] = None,
    zone: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6ec654f7c8ef61ff806dd9f4bf703bb374268e6f482b218b80e524da41a27e5(
    *,
    ready: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    serving: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    terminating: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5557dfd1a43c0d7083071328cbc11a251ad753f061cabcefd49404dab3bc7f13(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__713290705d65dd44d04ccf00d3845037e62a30dbfd290cafc7da2ebf100a3349(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__277db840f77d76a713c026fa1fa0819e32b02dcf022624e44cbfa125fb5f2b01(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__286917a644569c597c801dd958479a5077120eb7dab4d5dee4721d4a48121af3(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a741e8acb6980ac39760c14a629b374ab85d536df77bd8fdf8b5e0b4b5546ef0(
    value: typing.Optional[EndpointSliceV1EndpointCondition],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__342fcfc38dce3ce8b5fe21ddcce00f05e9d84e3cc155c7f9051f3b73e20f6ca4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97b4e90e2ca262b6da60aad521179c94c5cc2f22dd3d9d1d85130838675a2afb(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3dd534f26291aef18e564f8e3378c22d924dddab8ab6e05d2754f3194ff1efa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95db39342b4cb25b01930c17e68fab5f0ff42b4b6a57500ea34153ed61f0ed67(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ce8ff7fbd9c7c93a8b67e951375ed36ef3763d03743ad6a5a1a4ca2e21f0671(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f39e44036c2c7d4284232d0b7ad96effbddb1818b14bb8f4b25de0ce86ff6fe(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EndpointSliceV1Endpoint]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c44bc40e095c86bb6020bc214c4a3820a1beb789fe27538891500a5388fd7e1d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91d2651e0f1726f6f0b41aa48818dc00caa93b37456b479155eb5fb1a84ee25a(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c8d2997435ea3212a831977d7fd0168635cccf40d45325cc3a875dfb3afb1e0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08aff435c08532e83d425c6c0d4ca4a4c25f601eb21f0791a55097c0780b7062(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8dfad928b7e1e9c0716fd45d04d4d72fc80184f07a1b57c6c36ee3ecd0baf076(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed3fdd97746ec038fe4f2b1a0bd9ece2a6c965974846441ef75c11dcd0ce6320(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, EndpointSliceV1Endpoint]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be1c80ceca4070e40b53a689f61a04eff69a8a2604a8e06f40bea27016ce0d42(
    *,
    name: builtins.str,
    field_path: typing.Optional[builtins.str] = None,
    namespace: typing.Optional[builtins.str] = None,
    resource_version: typing.Optional[builtins.str] = None,
    uid: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a026cd0fd487a05c62d8f4e2470cd3b069f599895a3ebffe33a3dbddc871f466(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48a07660ba8f4737a705c379c8f74431247543c9324e521e68af78fb0730f137(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07de59c993971ae966487c8133d1079ce69739d0daa957421b17aadd045e4b25(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fd925e186f63a7f3253b8a25b503c022be24cad6fb85a25b2b5e521e463243b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bba2f8ccd1a213b327b5167aa7e421a2c206dfe9f5cc60de57e2909ff5ca3a8a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c3f35457096822e824c5beb06b4ac4ab2d3c734fa525a8f859173f18c4411d2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9b0330d7cabdb343a6f1fdf157d46f49d7781659ac07d77b0f3c92170f4d205(
    value: typing.Optional[EndpointSliceV1EndpointTargetRef],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__994d1cf6c6735eb8d39ffebbd297f2b88e458388395edf368f47134852024772(
    *,
    annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    generate_name: typing.Optional[builtins.str] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    name: typing.Optional[builtins.str] = None,
    namespace: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38e51924c42ca833958c930c677be200b2b1ba41b402e3baaa9a22ff28b03723(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac6f034a6bd567476b0781686568b5387aea7a558f9fe9a498b4d1befe62c226(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6eac8d655ad4efbe0e32509893897ef53aed2ae41551f783789610b1e76978ca(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c582c4666cdc9806437a956a3da228365887c8abeef7b1cda1aa4813a6b6a711(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb8aa6fb1083682f8c031645d8be633dfb459f8f7aff5eaed7f14db2aeb3f2c6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ba3b31a1eca3c821e8420cc4602bc5db3888913325a455664b78718a5e7d3c9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db9f5c5cdb1fae491d78a8478896dbe5fec632029139665c87eefbe1611a91d4(
    value: typing.Optional[EndpointSliceV1Metadata],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80d1534447a30d995294c0a7cca29a1fce1beeb855fbb76ae15b44ceb7a797e4(
    *,
    app_protocol: builtins.str,
    port: builtins.str,
    name: typing.Optional[builtins.str] = None,
    protocol: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d43d550914ba607319f94c2a7b07b251e235c57da8e0fa6e098631859a452c2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c68e044de4e4d83f12c706dc40b063a5784396c6b7cfd17278d08bfe418e6efd(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ddbe3447d4dafbfa9b9aa32f8a5146f795911c089bd46e5b5453aba207c0127(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e52898a9ae36e781b9b603f7abf06e74a2247deeaac2917559427585fbde9bc(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc4f2e7807b7364429582e29b574c99eee31fd3252dd5e514e4bc9db17adbf94(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e4854593275ace3862640f39a5b44c93bc700144c2eb6010b7bef2e0faa8294(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EndpointSliceV1Port]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd2969a08d6eeeb59da7dcca5decf4f1838ad6aff9e160a0e4b12678343ebf78(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3401361450021cf3fbaa64d844952a7e805f4ff2fe044c9944e4f101f58c48df(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__088883997d0df4de80a452bb705d26dc1a17bde4d215656ce05d9ed216413a60(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89610e5795384ada18f47ba1e0dc71ce2070ee6baf50445d26913b92b1e77b57(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73ad6bb78ac4c17b7bd94787dfe1a3cbda3af61227c6e73d01ade453be780df9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85055bf04bbf90bec88cbd785295bdc2842d4abe24b40cff20c7cf9cb1906800(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, EndpointSliceV1Port]],
) -> None:
    """Type checking stubs"""
    pass
