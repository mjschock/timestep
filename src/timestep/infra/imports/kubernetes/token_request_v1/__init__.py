'''
# `kubernetes_token_request_v1`

Refer to the Terraform Registory for docs: [`kubernetes_token_request_v1`](https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/token_request_v1).
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


class TokenRequestV1(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.tokenRequestV1.TokenRequestV1",
):
    '''Represents a {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/token_request_v1 kubernetes_token_request_v1}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        metadata: typing.Union["TokenRequestV1Metadata", typing.Dict[builtins.str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        spec: typing.Optional[typing.Union["TokenRequestV1Spec", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/token_request_v1 kubernetes_token_request_v1} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/token_request_v1#metadata TokenRequestV1#metadata}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/token_request_v1#id TokenRequestV1#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param spec: spec block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/token_request_v1#spec TokenRequestV1#spec}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f3c1f4d2cb8edf6d6ce7ef31ee935fb6cd591f5eccae4dc01ee2dc568cd9cfe)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = TokenRequestV1Config(
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
        generate_name: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param annotations: An unstructured key value map stored with the token request that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/token_request_v1#annotations TokenRequestV1#annotations}
        :param generate_name: Prefix, used by the server, to generate a unique name ONLY IF the ``name`` field has not been provided. This value will also be combined with a unique suffix. Read more: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#idempotency Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/token_request_v1#generate_name TokenRequestV1#generate_name}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the token request. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/token_request_v1#labels TokenRequestV1#labels}
        :param name: Name of the token request, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/token_request_v1#name TokenRequestV1#name}
        :param namespace: Namespace defines the space within which name of the token request must be unique. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/token_request_v1#namespace TokenRequestV1#namespace}
        '''
        value = TokenRequestV1Metadata(
            annotations=annotations,
            generate_name=generate_name,
            labels=labels,
            name=name,
            namespace=namespace,
        )

        return typing.cast(None, jsii.invoke(self, "putMetadata", [value]))

    @jsii.member(jsii_name="putSpec")
    def put_spec(
        self,
        *,
        audiences: typing.Optional[typing.Sequence[builtins.str]] = None,
        bound_object_ref: typing.Optional[typing.Union["TokenRequestV1SpecBoundObjectRef", typing.Dict[builtins.str, typing.Any]]] = None,
        expiration_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param audiences: Audiences are the intendend audiences of the token. A recipient of a token must identify themself with an identifier in the list of audiences of the token, and otherwise should reject the token. A token issued for multiple audiences may be used to authenticate against any of the audiences listed but implies a high degree of trust between the target audiences. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/token_request_v1#audiences TokenRequestV1#audiences}
        :param bound_object_ref: bound_object_ref block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/token_request_v1#bound_object_ref TokenRequestV1#bound_object_ref}
        :param expiration_seconds: expiration_seconds is the requested duration of validity of the request. The token issuer may return a token with a different validity duration so a client needs to check the 'expiration' field in a response. The expiration can't be less than 10 minutes. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/token_request_v1#expiration_seconds TokenRequestV1#expiration_seconds}
        '''
        value = TokenRequestV1Spec(
            audiences=audiences,
            bound_object_ref=bound_object_ref,
            expiration_seconds=expiration_seconds,
        )

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
    def metadata(self) -> "TokenRequestV1MetadataOutputReference":
        return typing.cast("TokenRequestV1MetadataOutputReference", jsii.get(self, "metadata"))

    @builtins.property
    @jsii.member(jsii_name="spec")
    def spec(self) -> "TokenRequestV1SpecOutputReference":
        return typing.cast("TokenRequestV1SpecOutputReference", jsii.get(self, "spec"))

    @builtins.property
    @jsii.member(jsii_name="token")
    def token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "token"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataInput")
    def metadata_input(self) -> typing.Optional["TokenRequestV1Metadata"]:
        return typing.cast(typing.Optional["TokenRequestV1Metadata"], jsii.get(self, "metadataInput"))

    @builtins.property
    @jsii.member(jsii_name="specInput")
    def spec_input(self) -> typing.Optional["TokenRequestV1Spec"]:
        return typing.cast(typing.Optional["TokenRequestV1Spec"], jsii.get(self, "specInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ec42d54a2fa7ac731f9608ff4c6808321f2a9cc7e7f77bbe44c7638028bc676)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="kubernetes.tokenRequestV1.TokenRequestV1Config",
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
class TokenRequestV1Config(_cdktf_9a9027ec.TerraformMetaArguments):
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
        metadata: typing.Union["TokenRequestV1Metadata", typing.Dict[builtins.str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        spec: typing.Optional[typing.Union["TokenRequestV1Spec", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/token_request_v1#metadata TokenRequestV1#metadata}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/token_request_v1#id TokenRequestV1#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param spec: spec block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/token_request_v1#spec TokenRequestV1#spec}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(metadata, dict):
            metadata = TokenRequestV1Metadata(**metadata)
        if isinstance(spec, dict):
            spec = TokenRequestV1Spec(**spec)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__406636b0397cd485a57c255b23ed1207ea87cc1562092f7e2e91c10711161cb5)
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
    def metadata(self) -> "TokenRequestV1Metadata":
        '''metadata block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/token_request_v1#metadata TokenRequestV1#metadata}
        '''
        result = self._values.get("metadata")
        assert result is not None, "Required property 'metadata' is missing"
        return typing.cast("TokenRequestV1Metadata", result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/token_request_v1#id TokenRequestV1#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def spec(self) -> typing.Optional["TokenRequestV1Spec"]:
        '''spec block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/token_request_v1#spec TokenRequestV1#spec}
        '''
        result = self._values.get("spec")
        return typing.cast(typing.Optional["TokenRequestV1Spec"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TokenRequestV1Config(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kubernetes.tokenRequestV1.TokenRequestV1Metadata",
    jsii_struct_bases=[],
    name_mapping={
        "annotations": "annotations",
        "generate_name": "generateName",
        "labels": "labels",
        "name": "name",
        "namespace": "namespace",
    },
)
class TokenRequestV1Metadata:
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
        :param annotations: An unstructured key value map stored with the token request that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/token_request_v1#annotations TokenRequestV1#annotations}
        :param generate_name: Prefix, used by the server, to generate a unique name ONLY IF the ``name`` field has not been provided. This value will also be combined with a unique suffix. Read more: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#idempotency Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/token_request_v1#generate_name TokenRequestV1#generate_name}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the token request. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/token_request_v1#labels TokenRequestV1#labels}
        :param name: Name of the token request, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/token_request_v1#name TokenRequestV1#name}
        :param namespace: Namespace defines the space within which name of the token request must be unique. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/token_request_v1#namespace TokenRequestV1#namespace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a3cd8b19a13a4d7396f73dcd174300e63f4e97236617b8822ddb00237b33d57)
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
        '''An unstructured key value map stored with the token request that may be used to store arbitrary metadata.

        More info: http://kubernetes.io/docs/user-guide/annotations

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/token_request_v1#annotations TokenRequestV1#annotations}
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def generate_name(self) -> typing.Optional[builtins.str]:
        '''Prefix, used by the server, to generate a unique name ONLY IF the ``name`` field has not been provided.

        This value will also be combined with a unique suffix. Read more: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#idempotency

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/token_request_v1#generate_name TokenRequestV1#generate_name}
        '''
        result = self._values.get("generate_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Map of string keys and values that can be used to organize and categorize (scope and select) the token request.

        May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/token_request_v1#labels TokenRequestV1#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the token request, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/token_request_v1#name TokenRequestV1#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Namespace defines the space within which name of the token request must be unique.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/token_request_v1#namespace TokenRequestV1#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TokenRequestV1Metadata(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TokenRequestV1MetadataOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.tokenRequestV1.TokenRequestV1MetadataOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__39f2fdb207a48ab73e96bcd223cf9bbc76e19ede8d8dda531b8a383895a4fe14)
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
            type_hints = typing.get_type_hints(_typecheckingstub__395df4cd2cd8cff489f232f0b7dddea1cfce7946a4951503245eebf853a1a3ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "annotations", value)

    @builtins.property
    @jsii.member(jsii_name="generateName")
    def generate_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "generateName"))

    @generate_name.setter
    def generate_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09fcfa15d0e03922e483c6e5b3284cafbeee10cde35c81d1817590bb189c3f82)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "generateName", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76a28e54957973aadbcab6f3c10fad9b85f1e61947a93b0e18a4ea3b54abf43c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30c62c20458da4716d620826104ae92e46c55d53d0549729c081820d766a9689)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37ccb6ba776c37b3c16c5ece0aad1e87322f1f4c71199a6f85bb07753172052b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[TokenRequestV1Metadata]:
        return typing.cast(typing.Optional[TokenRequestV1Metadata], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[TokenRequestV1Metadata]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ac02a34627e2554679013547c7b366846d8b867320554af483ede1051f5619c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.tokenRequestV1.TokenRequestV1Spec",
    jsii_struct_bases=[],
    name_mapping={
        "audiences": "audiences",
        "bound_object_ref": "boundObjectRef",
        "expiration_seconds": "expirationSeconds",
    },
)
class TokenRequestV1Spec:
    def __init__(
        self,
        *,
        audiences: typing.Optional[typing.Sequence[builtins.str]] = None,
        bound_object_ref: typing.Optional[typing.Union["TokenRequestV1SpecBoundObjectRef", typing.Dict[builtins.str, typing.Any]]] = None,
        expiration_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param audiences: Audiences are the intendend audiences of the token. A recipient of a token must identify themself with an identifier in the list of audiences of the token, and otherwise should reject the token. A token issued for multiple audiences may be used to authenticate against any of the audiences listed but implies a high degree of trust between the target audiences. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/token_request_v1#audiences TokenRequestV1#audiences}
        :param bound_object_ref: bound_object_ref block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/token_request_v1#bound_object_ref TokenRequestV1#bound_object_ref}
        :param expiration_seconds: expiration_seconds is the requested duration of validity of the request. The token issuer may return a token with a different validity duration so a client needs to check the 'expiration' field in a response. The expiration can't be less than 10 minutes. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/token_request_v1#expiration_seconds TokenRequestV1#expiration_seconds}
        '''
        if isinstance(bound_object_ref, dict):
            bound_object_ref = TokenRequestV1SpecBoundObjectRef(**bound_object_ref)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c230f8cbc500f782e687a21e225645e5a4734527b1d7e658223aff600e9a2edb)
            check_type(argname="argument audiences", value=audiences, expected_type=type_hints["audiences"])
            check_type(argname="argument bound_object_ref", value=bound_object_ref, expected_type=type_hints["bound_object_ref"])
            check_type(argname="argument expiration_seconds", value=expiration_seconds, expected_type=type_hints["expiration_seconds"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if audiences is not None:
            self._values["audiences"] = audiences
        if bound_object_ref is not None:
            self._values["bound_object_ref"] = bound_object_ref
        if expiration_seconds is not None:
            self._values["expiration_seconds"] = expiration_seconds

    @builtins.property
    def audiences(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Audiences are the intendend audiences of the token.

        A recipient of a token must identify themself with an identifier in the list of audiences of the token, and otherwise should reject the token. A token issued for multiple audiences may be used to authenticate against any of the audiences listed but implies a high degree of trust between the target audiences.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/token_request_v1#audiences TokenRequestV1#audiences}
        '''
        result = self._values.get("audiences")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def bound_object_ref(self) -> typing.Optional["TokenRequestV1SpecBoundObjectRef"]:
        '''bound_object_ref block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/token_request_v1#bound_object_ref TokenRequestV1#bound_object_ref}
        '''
        result = self._values.get("bound_object_ref")
        return typing.cast(typing.Optional["TokenRequestV1SpecBoundObjectRef"], result)

    @builtins.property
    def expiration_seconds(self) -> typing.Optional[jsii.Number]:
        '''expiration_seconds is the requested duration of validity of the request.

        The token issuer may return a token with a different validity duration so a client needs to check the 'expiration' field in a response. The expiration can't be less than 10 minutes.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/token_request_v1#expiration_seconds TokenRequestV1#expiration_seconds}
        '''
        result = self._values.get("expiration_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TokenRequestV1Spec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kubernetes.tokenRequestV1.TokenRequestV1SpecBoundObjectRef",
    jsii_struct_bases=[],
    name_mapping={
        "api_version": "apiVersion",
        "kind": "kind",
        "name": "name",
        "uid": "uid",
    },
)
class TokenRequestV1SpecBoundObjectRef:
    def __init__(
        self,
        *,
        api_version: typing.Optional[builtins.str] = None,
        kind: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        uid: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param api_version: API version of the referent. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/token_request_v1#api_version TokenRequestV1#api_version}
        :param kind: Kind of the referent. Valid kinds are 'Pod' and 'Secret'. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/token_request_v1#kind TokenRequestV1#kind}
        :param name: Name of the referent. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/token_request_v1#name TokenRequestV1#name}
        :param uid: UID of the referent. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/token_request_v1#uid TokenRequestV1#uid}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02229e1724d1732dde7cc31554f9247427d1764ecea3a2b14dd6a813c6fe45b7)
            check_type(argname="argument api_version", value=api_version, expected_type=type_hints["api_version"])
            check_type(argname="argument kind", value=kind, expected_type=type_hints["kind"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument uid", value=uid, expected_type=type_hints["uid"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if api_version is not None:
            self._values["api_version"] = api_version
        if kind is not None:
            self._values["kind"] = kind
        if name is not None:
            self._values["name"] = name
        if uid is not None:
            self._values["uid"] = uid

    @builtins.property
    def api_version(self) -> typing.Optional[builtins.str]:
        '''API version of the referent.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/token_request_v1#api_version TokenRequestV1#api_version}
        '''
        result = self._values.get("api_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kind(self) -> typing.Optional[builtins.str]:
        '''Kind of the referent. Valid kinds are 'Pod' and 'Secret'.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/token_request_v1#kind TokenRequestV1#kind}
        '''
        result = self._values.get("kind")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the referent.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/token_request_v1#name TokenRequestV1#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def uid(self) -> typing.Optional[builtins.str]:
        '''UID of the referent.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/token_request_v1#uid TokenRequestV1#uid}
        '''
        result = self._values.get("uid")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TokenRequestV1SpecBoundObjectRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TokenRequestV1SpecBoundObjectRefOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.tokenRequestV1.TokenRequestV1SpecBoundObjectRefOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__71eab7f3010620fba8e6e083a8cd5b8ba0c39932937ceee2cd1f97cc1fa0d6ef)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetApiVersion")
    def reset_api_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApiVersion", []))

    @jsii.member(jsii_name="resetKind")
    def reset_kind(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKind", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetUid")
    def reset_uid(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUid", []))

    @builtins.property
    @jsii.member(jsii_name="apiVersionInput")
    def api_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="kindInput")
    def kind_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kindInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="uidInput")
    def uid_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "uidInput"))

    @builtins.property
    @jsii.member(jsii_name="apiVersion")
    def api_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiVersion"))

    @api_version.setter
    def api_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2801251642ec567da91c8dd5bd4607213632c76723c3070a735f15a60808171a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiVersion", value)

    @builtins.property
    @jsii.member(jsii_name="kind")
    def kind(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kind"))

    @kind.setter
    def kind(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4a264491c7cb3cc61cac37632a6c3af0675e76b6fe22bd1ac7fcd66d02789a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kind", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a4bd2c0bb6de8bfd4e66ef827c0931f860905e15cfa5faf68a3e02676148f32)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="uid")
    def uid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uid"))

    @uid.setter
    def uid(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dbc1d20e06906187c3fa07aa21c4d160580b4d8ba6b7fce860d3946b1704c2b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uid", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[TokenRequestV1SpecBoundObjectRef]:
        return typing.cast(typing.Optional[TokenRequestV1SpecBoundObjectRef], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[TokenRequestV1SpecBoundObjectRef],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28ec00a294bdf111c727f4c3a926005993693b131504fbe832c6edd49c486b36)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class TokenRequestV1SpecOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.tokenRequestV1.TokenRequestV1SpecOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8f6c2be7f765c8337c807b85344ab19ed07aeb2a979d698e0c4fc55349ec9471)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putBoundObjectRef")
    def put_bound_object_ref(
        self,
        *,
        api_version: typing.Optional[builtins.str] = None,
        kind: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        uid: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param api_version: API version of the referent. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/token_request_v1#api_version TokenRequestV1#api_version}
        :param kind: Kind of the referent. Valid kinds are 'Pod' and 'Secret'. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/token_request_v1#kind TokenRequestV1#kind}
        :param name: Name of the referent. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/token_request_v1#name TokenRequestV1#name}
        :param uid: UID of the referent. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/kubernetes/2.22.0/docs/resources/token_request_v1#uid TokenRequestV1#uid}
        '''
        value = TokenRequestV1SpecBoundObjectRef(
            api_version=api_version, kind=kind, name=name, uid=uid
        )

        return typing.cast(None, jsii.invoke(self, "putBoundObjectRef", [value]))

    @jsii.member(jsii_name="resetAudiences")
    def reset_audiences(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAudiences", []))

    @jsii.member(jsii_name="resetBoundObjectRef")
    def reset_bound_object_ref(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBoundObjectRef", []))

    @jsii.member(jsii_name="resetExpirationSeconds")
    def reset_expiration_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpirationSeconds", []))

    @builtins.property
    @jsii.member(jsii_name="boundObjectRef")
    def bound_object_ref(self) -> TokenRequestV1SpecBoundObjectRefOutputReference:
        return typing.cast(TokenRequestV1SpecBoundObjectRefOutputReference, jsii.get(self, "boundObjectRef"))

    @builtins.property
    @jsii.member(jsii_name="audiencesInput")
    def audiences_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "audiencesInput"))

    @builtins.property
    @jsii.member(jsii_name="boundObjectRefInput")
    def bound_object_ref_input(
        self,
    ) -> typing.Optional[TokenRequestV1SpecBoundObjectRef]:
        return typing.cast(typing.Optional[TokenRequestV1SpecBoundObjectRef], jsii.get(self, "boundObjectRefInput"))

    @builtins.property
    @jsii.member(jsii_name="expirationSecondsInput")
    def expiration_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "expirationSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="audiences")
    def audiences(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "audiences"))

    @audiences.setter
    def audiences(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__419a25d9845c9dcd4662680ed73e17095479c5c4451508a152bce463eaafb21f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "audiences", value)

    @builtins.property
    @jsii.member(jsii_name="expirationSeconds")
    def expiration_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "expirationSeconds"))

    @expiration_seconds.setter
    def expiration_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4aeec044c8c0de36d541873b071aa35771bf2a68b19b11d33dfb7b47edb4b2e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expirationSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[TokenRequestV1Spec]:
        return typing.cast(typing.Optional[TokenRequestV1Spec], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[TokenRequestV1Spec]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e08b3fe5b3d92736711ecc2c89114ae61ccc279baafb5aaedce887951a465ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "TokenRequestV1",
    "TokenRequestV1Config",
    "TokenRequestV1Metadata",
    "TokenRequestV1MetadataOutputReference",
    "TokenRequestV1Spec",
    "TokenRequestV1SpecBoundObjectRef",
    "TokenRequestV1SpecBoundObjectRefOutputReference",
    "TokenRequestV1SpecOutputReference",
]

publication.publish()

def _typecheckingstub__5f3c1f4d2cb8edf6d6ce7ef31ee935fb6cd591f5eccae4dc01ee2dc568cd9cfe(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    metadata: typing.Union[TokenRequestV1Metadata, typing.Dict[builtins.str, typing.Any]],
    id: typing.Optional[builtins.str] = None,
    spec: typing.Optional[typing.Union[TokenRequestV1Spec, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__1ec42d54a2fa7ac731f9608ff4c6808321f2a9cc7e7f77bbe44c7638028bc676(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__406636b0397cd485a57c255b23ed1207ea87cc1562092f7e2e91c10711161cb5(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    metadata: typing.Union[TokenRequestV1Metadata, typing.Dict[builtins.str, typing.Any]],
    id: typing.Optional[builtins.str] = None,
    spec: typing.Optional[typing.Union[TokenRequestV1Spec, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a3cd8b19a13a4d7396f73dcd174300e63f4e97236617b8822ddb00237b33d57(
    *,
    annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    generate_name: typing.Optional[builtins.str] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    name: typing.Optional[builtins.str] = None,
    namespace: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39f2fdb207a48ab73e96bcd223cf9bbc76e19ede8d8dda531b8a383895a4fe14(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__395df4cd2cd8cff489f232f0b7dddea1cfce7946a4951503245eebf853a1a3ae(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09fcfa15d0e03922e483c6e5b3284cafbeee10cde35c81d1817590bb189c3f82(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76a28e54957973aadbcab6f3c10fad9b85f1e61947a93b0e18a4ea3b54abf43c(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30c62c20458da4716d620826104ae92e46c55d53d0549729c081820d766a9689(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37ccb6ba776c37b3c16c5ece0aad1e87322f1f4c71199a6f85bb07753172052b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ac02a34627e2554679013547c7b366846d8b867320554af483ede1051f5619c(
    value: typing.Optional[TokenRequestV1Metadata],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c230f8cbc500f782e687a21e225645e5a4734527b1d7e658223aff600e9a2edb(
    *,
    audiences: typing.Optional[typing.Sequence[builtins.str]] = None,
    bound_object_ref: typing.Optional[typing.Union[TokenRequestV1SpecBoundObjectRef, typing.Dict[builtins.str, typing.Any]]] = None,
    expiration_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02229e1724d1732dde7cc31554f9247427d1764ecea3a2b14dd6a813c6fe45b7(
    *,
    api_version: typing.Optional[builtins.str] = None,
    kind: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    uid: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71eab7f3010620fba8e6e083a8cd5b8ba0c39932937ceee2cd1f97cc1fa0d6ef(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2801251642ec567da91c8dd5bd4607213632c76723c3070a735f15a60808171a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4a264491c7cb3cc61cac37632a6c3af0675e76b6fe22bd1ac7fcd66d02789a0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a4bd2c0bb6de8bfd4e66ef827c0931f860905e15cfa5faf68a3e02676148f32(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbc1d20e06906187c3fa07aa21c4d160580b4d8ba6b7fce860d3946b1704c2b6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28ec00a294bdf111c727f4c3a926005993693b131504fbe832c6edd49c486b36(
    value: typing.Optional[TokenRequestV1SpecBoundObjectRef],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f6c2be7f765c8337c807b85344ab19ed07aeb2a979d698e0c4fc55349ec9471(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__419a25d9845c9dcd4662680ed73e17095479c5c4451508a152bce463eaafb21f(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4aeec044c8c0de36d541873b071aa35771bf2a68b19b11d33dfb7b47edb4b2e8(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e08b3fe5b3d92736711ecc2c89114ae61ccc279baafb5aaedce887951a465ae(
    value: typing.Optional[TokenRequestV1Spec],
) -> None:
    """Type checking stubs"""
    pass
