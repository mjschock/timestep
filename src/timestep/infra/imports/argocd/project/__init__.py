'''
# `argocd_project`

Refer to the Terraform Registory for docs: [`argocd_project`](https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project).
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


class Project(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.project.Project",
):
    '''Represents a {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project argocd_project}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        metadata: typing.Union["ProjectMetadata", typing.Dict[builtins.str, typing.Any]],
        spec: typing.Union["ProjectSpec", typing.Dict[builtins.str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project argocd_project} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#metadata Project#metadata}
        :param spec: spec block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#spec Project#spec}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#id Project#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3d3d12bf0919961ff0081d1f1b5ce17f68906ef58dcb6dcfb94af7b73ae1086)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ProjectConfig(
            metadata=metadata,
            spec=spec,
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

    @jsii.member(jsii_name="putMetadata")
    def put_metadata(
        self,
        *,
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param annotations: An unstructured key value map stored with the appprojects.argoproj.io that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#annotations Project#annotations}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the appprojects.argoproj.io. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#labels Project#labels}
        :param name: Name of the appprojects.argoproj.io, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#name Project#name}
        :param namespace: Namespace of the appprojects.argoproj.io, must be unique. Cannot be updated. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#namespace Project#namespace}
        '''
        value = ProjectMetadata(
            annotations=annotations, labels=labels, name=name, namespace=namespace
        )

        return typing.cast(None, jsii.invoke(self, "putMetadata", [value]))

    @jsii.member(jsii_name="putSpec")
    def put_spec(
        self,
        *,
        destination: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ProjectSpecDestination", typing.Dict[builtins.str, typing.Any]]]],
        source_repos: typing.Sequence[builtins.str],
        cluster_resource_blacklist: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ProjectSpecClusterResourceBlacklistStruct", typing.Dict[builtins.str, typing.Any]]]]] = None,
        cluster_resource_whitelist: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ProjectSpecClusterResourceWhitelistStruct", typing.Dict[builtins.str, typing.Any]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        namespace_resource_blacklist: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ProjectSpecNamespaceResourceBlacklistStruct", typing.Dict[builtins.str, typing.Any]]]]] = None,
        namespace_resource_whitelist: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ProjectSpecNamespaceResourceWhitelistStruct", typing.Dict[builtins.str, typing.Any]]]]] = None,
        orphaned_resources: typing.Optional[typing.Union["ProjectSpecOrphanedResources", typing.Dict[builtins.str, typing.Any]]] = None,
        role: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ProjectSpecRole", typing.Dict[builtins.str, typing.Any]]]]] = None,
        signature_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        source_namespaces: typing.Optional[typing.Sequence[builtins.str]] = None,
        sync_window: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ProjectSpecSyncWindow", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param destination: destination block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#destination Project#destination}
        :param source_repos: List of repository URLs which can be used for deployment. Can be set to ``["*"]`` to allow all configured repositories configured in ArgoCD. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#source_repos Project#source_repos}
        :param cluster_resource_blacklist: cluster_resource_blacklist block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#cluster_resource_blacklist Project#cluster_resource_blacklist}
        :param cluster_resource_whitelist: cluster_resource_whitelist block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#cluster_resource_whitelist Project#cluster_resource_whitelist}
        :param description: Project description. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#description Project#description}
        :param namespace_resource_blacklist: namespace_resource_blacklist block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#namespace_resource_blacklist Project#namespace_resource_blacklist}
        :param namespace_resource_whitelist: namespace_resource_whitelist block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#namespace_resource_whitelist Project#namespace_resource_whitelist}
        :param orphaned_resources: orphaned_resources block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#orphaned_resources Project#orphaned_resources}
        :param role: role block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#role Project#role}
        :param signature_keys: List of PGP key IDs that commits in Git must be signed with in order to be allowed for sync. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#signature_keys Project#signature_keys}
        :param source_namespaces: List of namespaces that application resources are allowed to be created in. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#source_namespaces Project#source_namespaces}
        :param sync_window: sync_window block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#sync_window Project#sync_window}
        '''
        value = ProjectSpec(
            destination=destination,
            source_repos=source_repos,
            cluster_resource_blacklist=cluster_resource_blacklist,
            cluster_resource_whitelist=cluster_resource_whitelist,
            description=description,
            namespace_resource_blacklist=namespace_resource_blacklist,
            namespace_resource_whitelist=namespace_resource_whitelist,
            orphaned_resources=orphaned_resources,
            role=role,
            signature_keys=signature_keys,
            source_namespaces=source_namespaces,
            sync_window=sync_window,
        )

        return typing.cast(None, jsii.invoke(self, "putSpec", [value]))

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
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> "ProjectMetadataOutputReference":
        return typing.cast("ProjectMetadataOutputReference", jsii.get(self, "metadata"))

    @builtins.property
    @jsii.member(jsii_name="spec")
    def spec(self) -> "ProjectSpecOutputReference":
        return typing.cast("ProjectSpecOutputReference", jsii.get(self, "spec"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataInput")
    def metadata_input(self) -> typing.Optional["ProjectMetadata"]:
        return typing.cast(typing.Optional["ProjectMetadata"], jsii.get(self, "metadataInput"))

    @builtins.property
    @jsii.member(jsii_name="specInput")
    def spec_input(self) -> typing.Optional["ProjectSpec"]:
        return typing.cast(typing.Optional["ProjectSpec"], jsii.get(self, "specInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95b4bf546f3b84e96dd9e865f7bc676cdaa215bd5a9b3cb63ea90985106656b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="argocd.project.ProjectConfig",
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
        "spec": "spec",
        "id": "id",
    },
)
class ProjectConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        metadata: typing.Union["ProjectMetadata", typing.Dict[builtins.str, typing.Any]],
        spec: typing.Union["ProjectSpec", typing.Dict[builtins.str, typing.Any]],
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
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#metadata Project#metadata}
        :param spec: spec block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#spec Project#spec}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#id Project#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(metadata, dict):
            metadata = ProjectMetadata(**metadata)
        if isinstance(spec, dict):
            spec = ProjectSpec(**spec)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9497154d335aa51fa1cc3c762b4b407ef098098a87e966d5ebc0b5b000f2816f)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument spec", value=spec, expected_type=type_hints["spec"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "metadata": metadata,
            "spec": spec,
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
    def metadata(self) -> "ProjectMetadata":
        '''metadata block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#metadata Project#metadata}
        '''
        result = self._values.get("metadata")
        assert result is not None, "Required property 'metadata' is missing"
        return typing.cast("ProjectMetadata", result)

    @builtins.property
    def spec(self) -> "ProjectSpec":
        '''spec block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#spec Project#spec}
        '''
        result = self._values.get("spec")
        assert result is not None, "Required property 'spec' is missing"
        return typing.cast("ProjectSpec", result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#id Project#id}.

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
        return "ProjectConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="argocd.project.ProjectMetadata",
    jsii_struct_bases=[],
    name_mapping={
        "annotations": "annotations",
        "labels": "labels",
        "name": "name",
        "namespace": "namespace",
    },
)
class ProjectMetadata:
    def __init__(
        self,
        *,
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param annotations: An unstructured key value map stored with the appprojects.argoproj.io that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#annotations Project#annotations}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the appprojects.argoproj.io. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#labels Project#labels}
        :param name: Name of the appprojects.argoproj.io, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#name Project#name}
        :param namespace: Namespace of the appprojects.argoproj.io, must be unique. Cannot be updated. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#namespace Project#namespace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0f47e9f8dd93f2f280b59d5162ae992ccb3136741c570e1b40063ea6fc59ccf)
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if annotations is not None:
            self._values["annotations"] = annotations
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
        '''An unstructured key value map stored with the appprojects.argoproj.io that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#annotations Project#annotations}
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Map of string keys and values that can be used to organize and categorize (scope and select) the appprojects.argoproj.io. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#labels Project#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the appprojects.argoproj.io, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#name Project#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Namespace of the appprojects.argoproj.io, must be unique. Cannot be updated. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#namespace Project#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProjectMetadata(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ProjectMetadataOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.project.ProjectMetadataOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3e0049732ed9943592a92ce1862076bae0fbd0e3ce057d22ab205203e3e296b2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c033bc30e6c4d3b6a49ef402f3ca2d361b62154178432d3fe96254767c6356df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "annotations", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d0a3429c9a9fe1a3f6558922ea469e77c0fc5264335d0a5d9dc9637251bae7a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f620e7ee8ef3af2885b74b56bad52ffac96184766d35f6669ea08ad16422bda9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b55326445ed8cf45566e74ca9651e905bbe5404bac0797f418a2628dc19b50e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ProjectMetadata]:
        return typing.cast(typing.Optional[ProjectMetadata], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ProjectMetadata]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31b3b6ebe794b8f1e9aee8d7575b966766616cf290a1faa9ae8d9bf8ea0c6a4e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="argocd.project.ProjectSpec",
    jsii_struct_bases=[],
    name_mapping={
        "destination": "destination",
        "source_repos": "sourceRepos",
        "cluster_resource_blacklist": "clusterResourceBlacklist",
        "cluster_resource_whitelist": "clusterResourceWhitelist",
        "description": "description",
        "namespace_resource_blacklist": "namespaceResourceBlacklist",
        "namespace_resource_whitelist": "namespaceResourceWhitelist",
        "orphaned_resources": "orphanedResources",
        "role": "role",
        "signature_keys": "signatureKeys",
        "source_namespaces": "sourceNamespaces",
        "sync_window": "syncWindow",
    },
)
class ProjectSpec:
    def __init__(
        self,
        *,
        destination: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ProjectSpecDestination", typing.Dict[builtins.str, typing.Any]]]],
        source_repos: typing.Sequence[builtins.str],
        cluster_resource_blacklist: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ProjectSpecClusterResourceBlacklistStruct", typing.Dict[builtins.str, typing.Any]]]]] = None,
        cluster_resource_whitelist: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ProjectSpecClusterResourceWhitelistStruct", typing.Dict[builtins.str, typing.Any]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        namespace_resource_blacklist: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ProjectSpecNamespaceResourceBlacklistStruct", typing.Dict[builtins.str, typing.Any]]]]] = None,
        namespace_resource_whitelist: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ProjectSpecNamespaceResourceWhitelistStruct", typing.Dict[builtins.str, typing.Any]]]]] = None,
        orphaned_resources: typing.Optional[typing.Union["ProjectSpecOrphanedResources", typing.Dict[builtins.str, typing.Any]]] = None,
        role: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ProjectSpecRole", typing.Dict[builtins.str, typing.Any]]]]] = None,
        signature_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        source_namespaces: typing.Optional[typing.Sequence[builtins.str]] = None,
        sync_window: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ProjectSpecSyncWindow", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param destination: destination block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#destination Project#destination}
        :param source_repos: List of repository URLs which can be used for deployment. Can be set to ``["*"]`` to allow all configured repositories configured in ArgoCD. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#source_repos Project#source_repos}
        :param cluster_resource_blacklist: cluster_resource_blacklist block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#cluster_resource_blacklist Project#cluster_resource_blacklist}
        :param cluster_resource_whitelist: cluster_resource_whitelist block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#cluster_resource_whitelist Project#cluster_resource_whitelist}
        :param description: Project description. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#description Project#description}
        :param namespace_resource_blacklist: namespace_resource_blacklist block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#namespace_resource_blacklist Project#namespace_resource_blacklist}
        :param namespace_resource_whitelist: namespace_resource_whitelist block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#namespace_resource_whitelist Project#namespace_resource_whitelist}
        :param orphaned_resources: orphaned_resources block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#orphaned_resources Project#orphaned_resources}
        :param role: role block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#role Project#role}
        :param signature_keys: List of PGP key IDs that commits in Git must be signed with in order to be allowed for sync. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#signature_keys Project#signature_keys}
        :param source_namespaces: List of namespaces that application resources are allowed to be created in. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#source_namespaces Project#source_namespaces}
        :param sync_window: sync_window block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#sync_window Project#sync_window}
        '''
        if isinstance(orphaned_resources, dict):
            orphaned_resources = ProjectSpecOrphanedResources(**orphaned_resources)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18398239103ff4388e1197523ab4342e8f584b621fcfa1bdfe5d0d120d677423)
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
            check_type(argname="argument source_repos", value=source_repos, expected_type=type_hints["source_repos"])
            check_type(argname="argument cluster_resource_blacklist", value=cluster_resource_blacklist, expected_type=type_hints["cluster_resource_blacklist"])
            check_type(argname="argument cluster_resource_whitelist", value=cluster_resource_whitelist, expected_type=type_hints["cluster_resource_whitelist"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument namespace_resource_blacklist", value=namespace_resource_blacklist, expected_type=type_hints["namespace_resource_blacklist"])
            check_type(argname="argument namespace_resource_whitelist", value=namespace_resource_whitelist, expected_type=type_hints["namespace_resource_whitelist"])
            check_type(argname="argument orphaned_resources", value=orphaned_resources, expected_type=type_hints["orphaned_resources"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument signature_keys", value=signature_keys, expected_type=type_hints["signature_keys"])
            check_type(argname="argument source_namespaces", value=source_namespaces, expected_type=type_hints["source_namespaces"])
            check_type(argname="argument sync_window", value=sync_window, expected_type=type_hints["sync_window"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination": destination,
            "source_repos": source_repos,
        }
        if cluster_resource_blacklist is not None:
            self._values["cluster_resource_blacklist"] = cluster_resource_blacklist
        if cluster_resource_whitelist is not None:
            self._values["cluster_resource_whitelist"] = cluster_resource_whitelist
        if description is not None:
            self._values["description"] = description
        if namespace_resource_blacklist is not None:
            self._values["namespace_resource_blacklist"] = namespace_resource_blacklist
        if namespace_resource_whitelist is not None:
            self._values["namespace_resource_whitelist"] = namespace_resource_whitelist
        if orphaned_resources is not None:
            self._values["orphaned_resources"] = orphaned_resources
        if role is not None:
            self._values["role"] = role
        if signature_keys is not None:
            self._values["signature_keys"] = signature_keys
        if source_namespaces is not None:
            self._values["source_namespaces"] = source_namespaces
        if sync_window is not None:
            self._values["sync_window"] = sync_window

    @builtins.property
    def destination(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ProjectSpecDestination"]]:
        '''destination block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#destination Project#destination}
        '''
        result = self._values.get("destination")
        assert result is not None, "Required property 'destination' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ProjectSpecDestination"]], result)

    @builtins.property
    def source_repos(self) -> typing.List[builtins.str]:
        '''List of repository URLs which can be used for deployment.

        Can be set to ``["*"]`` to allow all configured repositories configured in ArgoCD.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#source_repos Project#source_repos}
        '''
        result = self._values.get("source_repos")
        assert result is not None, "Required property 'source_repos' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def cluster_resource_blacklist(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ProjectSpecClusterResourceBlacklistStruct"]]]:
        '''cluster_resource_blacklist block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#cluster_resource_blacklist Project#cluster_resource_blacklist}
        '''
        result = self._values.get("cluster_resource_blacklist")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ProjectSpecClusterResourceBlacklistStruct"]]], result)

    @builtins.property
    def cluster_resource_whitelist(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ProjectSpecClusterResourceWhitelistStruct"]]]:
        '''cluster_resource_whitelist block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#cluster_resource_whitelist Project#cluster_resource_whitelist}
        '''
        result = self._values.get("cluster_resource_whitelist")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ProjectSpecClusterResourceWhitelistStruct"]]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Project description.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#description Project#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace_resource_blacklist(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ProjectSpecNamespaceResourceBlacklistStruct"]]]:
        '''namespace_resource_blacklist block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#namespace_resource_blacklist Project#namespace_resource_blacklist}
        '''
        result = self._values.get("namespace_resource_blacklist")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ProjectSpecNamespaceResourceBlacklistStruct"]]], result)

    @builtins.property
    def namespace_resource_whitelist(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ProjectSpecNamespaceResourceWhitelistStruct"]]]:
        '''namespace_resource_whitelist block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#namespace_resource_whitelist Project#namespace_resource_whitelist}
        '''
        result = self._values.get("namespace_resource_whitelist")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ProjectSpecNamespaceResourceWhitelistStruct"]]], result)

    @builtins.property
    def orphaned_resources(self) -> typing.Optional["ProjectSpecOrphanedResources"]:
        '''orphaned_resources block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#orphaned_resources Project#orphaned_resources}
        '''
        result = self._values.get("orphaned_resources")
        return typing.cast(typing.Optional["ProjectSpecOrphanedResources"], result)

    @builtins.property
    def role(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ProjectSpecRole"]]]:
        '''role block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#role Project#role}
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ProjectSpecRole"]]], result)

    @builtins.property
    def signature_keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of PGP key IDs that commits in Git must be signed with in order to be allowed for sync.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#signature_keys Project#signature_keys}
        '''
        result = self._values.get("signature_keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def source_namespaces(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of namespaces that application resources are allowed to be created in.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#source_namespaces Project#source_namespaces}
        '''
        result = self._values.get("source_namespaces")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def sync_window(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ProjectSpecSyncWindow"]]]:
        '''sync_window block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#sync_window Project#sync_window}
        '''
        result = self._values.get("sync_window")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ProjectSpecSyncWindow"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProjectSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="argocd.project.ProjectSpecClusterResourceBlacklistStruct",
    jsii_struct_bases=[],
    name_mapping={"group": "group", "kind": "kind"},
)
class ProjectSpecClusterResourceBlacklistStruct:
    def __init__(
        self,
        *,
        group: typing.Optional[builtins.str] = None,
        kind: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param group: The Kubernetes resource Group to match for. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#group Project#group}
        :param kind: The Kubernetes resource Kind to match for. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#kind Project#kind}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa743e36d7fdd14d3c1131afce7270004ad566eadc3ffdb1aabf32953e97607f)
            check_type(argname="argument group", value=group, expected_type=type_hints["group"])
            check_type(argname="argument kind", value=kind, expected_type=type_hints["kind"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if group is not None:
            self._values["group"] = group
        if kind is not None:
            self._values["kind"] = kind

    @builtins.property
    def group(self) -> typing.Optional[builtins.str]:
        '''The Kubernetes resource Group to match for.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#group Project#group}
        '''
        result = self._values.get("group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kind(self) -> typing.Optional[builtins.str]:
        '''The Kubernetes resource Kind to match for.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#kind Project#kind}
        '''
        result = self._values.get("kind")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProjectSpecClusterResourceBlacklistStruct(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ProjectSpecClusterResourceBlacklistStructList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.project.ProjectSpecClusterResourceBlacklistStructList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__94b4d952d0273fe08b23548315d3d17ca2e751fcff16d08f8615c177dbfb36bf)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ProjectSpecClusterResourceBlacklistStructOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f81f5c643730dd7e88e02278ef088ae67194a14d2e2a93700737c4c8ef596d3c)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ProjectSpecClusterResourceBlacklistStructOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a91399d45f01f608e4a2e8460f4f412bdf3df0bbbc2bc4e25abe6b3f7211aafb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5195bc662586ae7f164d532db8ca8d5c5e1eeec2c668caa7778607e5eab2b74e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1c67ebe055152d204f4b8dd339d720fc94bf9269cfab4f6f9716e57f84fb5163)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectSpecClusterResourceBlacklistStruct]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectSpecClusterResourceBlacklistStruct]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectSpecClusterResourceBlacklistStruct]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ed8c66cd4c12189ede0f4b4556ac2ff15a6be48cb659ce87c0d714c814bdf25)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ProjectSpecClusterResourceBlacklistStructOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.project.ProjectSpecClusterResourceBlacklistStructOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cb47f92b6cbc57ce872c6a15347515ebbed803b80009000d69c3b42f2ed746c6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetGroup")
    def reset_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroup", []))

    @jsii.member(jsii_name="resetKind")
    def reset_kind(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKind", []))

    @builtins.property
    @jsii.member(jsii_name="groupInput")
    def group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupInput"))

    @builtins.property
    @jsii.member(jsii_name="kindInput")
    def kind_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kindInput"))

    @builtins.property
    @jsii.member(jsii_name="group")
    def group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "group"))

    @group.setter
    def group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__026968de30b0919ac9f816abd44ec43a72541adc0343e8ce177d9ae978f0a6a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "group", value)

    @builtins.property
    @jsii.member(jsii_name="kind")
    def kind(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kind"))

    @kind.setter
    def kind(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee69af0d85800cca57cfecec7f97143067247795a9aa675057bcf4132cb39d45)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kind", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectSpecClusterResourceBlacklistStruct]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectSpecClusterResourceBlacklistStruct]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectSpecClusterResourceBlacklistStruct]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__341251d2c89972a060d013a4aba0678fb262e5f753a8ae0c9fb5a908a4d7ced3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="argocd.project.ProjectSpecClusterResourceWhitelistStruct",
    jsii_struct_bases=[],
    name_mapping={"group": "group", "kind": "kind"},
)
class ProjectSpecClusterResourceWhitelistStruct:
    def __init__(
        self,
        *,
        group: typing.Optional[builtins.str] = None,
        kind: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param group: The Kubernetes resource Group to match for. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#group Project#group}
        :param kind: The Kubernetes resource Kind to match for. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#kind Project#kind}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef252e43a4079517d42e2a988d0ec61d23adf4c71077b0f49cc830c5c2a3d337)
            check_type(argname="argument group", value=group, expected_type=type_hints["group"])
            check_type(argname="argument kind", value=kind, expected_type=type_hints["kind"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if group is not None:
            self._values["group"] = group
        if kind is not None:
            self._values["kind"] = kind

    @builtins.property
    def group(self) -> typing.Optional[builtins.str]:
        '''The Kubernetes resource Group to match for.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#group Project#group}
        '''
        result = self._values.get("group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kind(self) -> typing.Optional[builtins.str]:
        '''The Kubernetes resource Kind to match for.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#kind Project#kind}
        '''
        result = self._values.get("kind")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProjectSpecClusterResourceWhitelistStruct(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ProjectSpecClusterResourceWhitelistStructList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.project.ProjectSpecClusterResourceWhitelistStructList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4a0349f68bb22e03d446c8ab8c4638474196b7c54704e4b789bfb619d3ccca08)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ProjectSpecClusterResourceWhitelistStructOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cad1675d8d945158d3b5b4d2ad4c99215c7fbb21efe3e2877487a4ec5bf0c39a)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ProjectSpecClusterResourceWhitelistStructOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2236a9d3cdf7d2524ebaeafd89b6a2c78e5ac58104892b64bf42abc0c063f618)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1e04d890c78d5e8327b733a338fdaae1459c1517b59ebdba4099e30550f0d0fe)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5d2ae583767993e5aa1cfca6939e976806af2136545bdd2ed31b992e45cd9862)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectSpecClusterResourceWhitelistStruct]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectSpecClusterResourceWhitelistStruct]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectSpecClusterResourceWhitelistStruct]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06f760453338533d3149780f7b5c6e0bdf9a47784332986835fa6e9263298185)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ProjectSpecClusterResourceWhitelistStructOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.project.ProjectSpecClusterResourceWhitelistStructOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__15c24dbe075f1e94e8ee8225aca51e2525b812414eaf1086c0684d219ff47e2e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetGroup")
    def reset_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroup", []))

    @jsii.member(jsii_name="resetKind")
    def reset_kind(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKind", []))

    @builtins.property
    @jsii.member(jsii_name="groupInput")
    def group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupInput"))

    @builtins.property
    @jsii.member(jsii_name="kindInput")
    def kind_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kindInput"))

    @builtins.property
    @jsii.member(jsii_name="group")
    def group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "group"))

    @group.setter
    def group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58aaece878a6e6e9fe181289efbdc3053e20fbdd4dc6621f9fb5f66555a50a5d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "group", value)

    @builtins.property
    @jsii.member(jsii_name="kind")
    def kind(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kind"))

    @kind.setter
    def kind(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f64bda654841f57b941e1705b1527d649c77c9611db196d3b6230af7190fad49)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kind", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectSpecClusterResourceWhitelistStruct]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectSpecClusterResourceWhitelistStruct]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectSpecClusterResourceWhitelistStruct]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70e598907ebeabef68881ef68bcc292433270f798d0a3f09b75adc61fc5b628b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="argocd.project.ProjectSpecDestination",
    jsii_struct_bases=[],
    name_mapping={"namespace": "namespace", "name": "name", "server": "server"},
)
class ProjectSpecDestination:
    def __init__(
        self,
        *,
        namespace: builtins.str,
        name: typing.Optional[builtins.str] = None,
        server: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param namespace: Target namespace for applications' resources. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#namespace Project#namespace}
        :param name: Name of the destination cluster which can be used instead of server. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#name Project#name}
        :param server: URL of the target cluster and must be set to the Kubernetes control plane API. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#server Project#server}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2fbd1a96bbe6ead42fbb3685ccdeef683ef37b1556d03eb58a4c566a6dd18e9d)
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument server", value=server, expected_type=type_hints["server"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "namespace": namespace,
        }
        if name is not None:
            self._values["name"] = name
        if server is not None:
            self._values["server"] = server

    @builtins.property
    def namespace(self) -> builtins.str:
        '''Target namespace for applications' resources.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#namespace Project#namespace}
        '''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the destination cluster which can be used instead of server.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#name Project#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def server(self) -> typing.Optional[builtins.str]:
        '''URL of the target cluster and must be set to the Kubernetes control plane API.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#server Project#server}
        '''
        result = self._values.get("server")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProjectSpecDestination(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ProjectSpecDestinationList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.project.ProjectSpecDestinationList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__43f93fdc162a287ffd2ce003fadfd1bdd41c2d8f98be3a94b3ae86158874dc24)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ProjectSpecDestinationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43a7fe3af317c77abf696f89fd2aa71fae825758c3aa7c820c46a949445fc63c)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ProjectSpecDestinationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a778a21972d579da1856a96ebe1bb7d46437ea0dbdffb31464c0ef2867f02a5e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ceee3c4b3a2683f9180a93236e55c92dda796a050bbf968ea340ef713a6383cd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a4234d40579284e6ee6a964bc3649912574e53dad95be46454d2ccebd69752ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectSpecDestination]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectSpecDestination]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectSpecDestination]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e1b55d39f09b8555131c9883a7332c96dcdf46c25e5634ab0a557cd228eb030)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ProjectSpecDestinationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.project.ProjectSpecDestinationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9737ca02cdeab70a5b4de85c1e5142b62d9c83cf7b53879d9986c6140eff1116)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetServer")
    def reset_server(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServer", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="serverInput")
    def server_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef783d2bdeb94d06028a33bcedd36bcc73d1541b4b735adbb75f3e44cd80ee4c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5253b4e24acef297cb6903d051de8d13a43c74be947f1ea0e3fb30706df44b17)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="server")
    def server(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "server"))

    @server.setter
    def server(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cdf4c61e0787daa6d247c49368a30ee7d14045c2d721fa11caf2c31495a2ddcc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "server", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectSpecDestination]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectSpecDestination]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectSpecDestination]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b43a6b3c5de3715758f5ae362f38bb77fc2379b2a610d4dc453194392db9434)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="argocd.project.ProjectSpecNamespaceResourceBlacklistStruct",
    jsii_struct_bases=[],
    name_mapping={"group": "group", "kind": "kind"},
)
class ProjectSpecNamespaceResourceBlacklistStruct:
    def __init__(
        self,
        *,
        group: typing.Optional[builtins.str] = None,
        kind: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param group: The Kubernetes resource Group to match for. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#group Project#group}
        :param kind: The Kubernetes resource Kind to match for. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#kind Project#kind}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f33da4f66ff4ff0a4b34fc9450a3eb4daf7ac95d9bb8668de286331f5d8d6126)
            check_type(argname="argument group", value=group, expected_type=type_hints["group"])
            check_type(argname="argument kind", value=kind, expected_type=type_hints["kind"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if group is not None:
            self._values["group"] = group
        if kind is not None:
            self._values["kind"] = kind

    @builtins.property
    def group(self) -> typing.Optional[builtins.str]:
        '''The Kubernetes resource Group to match for.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#group Project#group}
        '''
        result = self._values.get("group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kind(self) -> typing.Optional[builtins.str]:
        '''The Kubernetes resource Kind to match for.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#kind Project#kind}
        '''
        result = self._values.get("kind")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProjectSpecNamespaceResourceBlacklistStruct(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ProjectSpecNamespaceResourceBlacklistStructList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.project.ProjectSpecNamespaceResourceBlacklistStructList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__07fb8f98872fbc3b176b9d614d605ffdcd361bc567877c1cfbc4dffb09ec09e3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ProjectSpecNamespaceResourceBlacklistStructOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5dc4de655fa3d686cfc7a6b9f3bd7f33800300755519f41a6c9f98f309539edf)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ProjectSpecNamespaceResourceBlacklistStructOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae4cbafd34b663d50bee961805ac809ced3493e826a43994fd938be08256cb76)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a2349a30a8bb6712ba191362741dc4986458551eb953b7302d8510b8c36ae61c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a46066be1469053c958a1dce7d12205087b8a013c525a358f69b5dae2619307d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectSpecNamespaceResourceBlacklistStruct]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectSpecNamespaceResourceBlacklistStruct]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectSpecNamespaceResourceBlacklistStruct]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__088c3618c4dacc4c233eba6082d0fed8a1ab8960a57548e9a32d3537b1ac8869)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ProjectSpecNamespaceResourceBlacklistStructOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.project.ProjectSpecNamespaceResourceBlacklistStructOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__453a6786749b3ec45620c9492340985e11d21c28839895d39478c108d679c439)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetGroup")
    def reset_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroup", []))

    @jsii.member(jsii_name="resetKind")
    def reset_kind(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKind", []))

    @builtins.property
    @jsii.member(jsii_name="groupInput")
    def group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupInput"))

    @builtins.property
    @jsii.member(jsii_name="kindInput")
    def kind_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kindInput"))

    @builtins.property
    @jsii.member(jsii_name="group")
    def group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "group"))

    @group.setter
    def group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__490eff9cee13c66c8da572c14785579eb216cafce218b78342deb59c3dea0c8d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "group", value)

    @builtins.property
    @jsii.member(jsii_name="kind")
    def kind(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kind"))

    @kind.setter
    def kind(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e746ff5c4c2d5157a3679a1a21a425522368bcdba0e906cac57d71b4d499c066)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kind", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectSpecNamespaceResourceBlacklistStruct]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectSpecNamespaceResourceBlacklistStruct]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectSpecNamespaceResourceBlacklistStruct]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1f76eb60c6f233ebeaa199981fa93fb04e2c4edf9bd9dbdef74d0a9224db036)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="argocd.project.ProjectSpecNamespaceResourceWhitelistStruct",
    jsii_struct_bases=[],
    name_mapping={"group": "group", "kind": "kind"},
)
class ProjectSpecNamespaceResourceWhitelistStruct:
    def __init__(
        self,
        *,
        group: typing.Optional[builtins.str] = None,
        kind: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param group: The Kubernetes resource Group to match for. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#group Project#group}
        :param kind: The Kubernetes resource Kind to match for. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#kind Project#kind}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7de83e18d50f9e79e68b5de9527a0df9cce16c228f2a10081cad1bf3c6fd5357)
            check_type(argname="argument group", value=group, expected_type=type_hints["group"])
            check_type(argname="argument kind", value=kind, expected_type=type_hints["kind"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if group is not None:
            self._values["group"] = group
        if kind is not None:
            self._values["kind"] = kind

    @builtins.property
    def group(self) -> typing.Optional[builtins.str]:
        '''The Kubernetes resource Group to match for.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#group Project#group}
        '''
        result = self._values.get("group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kind(self) -> typing.Optional[builtins.str]:
        '''The Kubernetes resource Kind to match for.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#kind Project#kind}
        '''
        result = self._values.get("kind")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProjectSpecNamespaceResourceWhitelistStruct(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ProjectSpecNamespaceResourceWhitelistStructList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.project.ProjectSpecNamespaceResourceWhitelistStructList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__55231f04db8137cea3aede819a29d07f39f36cfd08d88c75aaeffdfd46866b04)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ProjectSpecNamespaceResourceWhitelistStructOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8039888d88c30f3f4eefbef969a256204194f20657a60a541e0bbb63bfbe0666)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ProjectSpecNamespaceResourceWhitelistStructOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c9b64c42de461d6df1c26434e09dbcf1d61de9bfa67a23e83e993057db77a66)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0bc82a896e2599331f7aa4ef7ab14dbf17b43347274311a69993b791fcc1ba00)
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
            type_hints = typing.get_type_hints(_typecheckingstub__70f096833f4212fd747bc569d47e93f52ee951bbaf63dc2f4a37fb95a9970e35)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectSpecNamespaceResourceWhitelistStruct]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectSpecNamespaceResourceWhitelistStruct]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectSpecNamespaceResourceWhitelistStruct]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf512c9ce22d17c9a930edd72714a01372234d45a191dcaa0e111da010a00140)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ProjectSpecNamespaceResourceWhitelistStructOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.project.ProjectSpecNamespaceResourceWhitelistStructOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__24157ce6dd1b34da5dad9943a7c67fd51dd7543b841b02baf1c67c9b499ddf71)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetGroup")
    def reset_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroup", []))

    @jsii.member(jsii_name="resetKind")
    def reset_kind(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKind", []))

    @builtins.property
    @jsii.member(jsii_name="groupInput")
    def group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupInput"))

    @builtins.property
    @jsii.member(jsii_name="kindInput")
    def kind_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kindInput"))

    @builtins.property
    @jsii.member(jsii_name="group")
    def group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "group"))

    @group.setter
    def group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e82293c81f4a6a7a0ab545e5164284805f579eed03dd4a850bd96fa32d5e6790)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "group", value)

    @builtins.property
    @jsii.member(jsii_name="kind")
    def kind(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kind"))

    @kind.setter
    def kind(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21d71a0aec939ca29aa69f45c6412557d50fb6acd2cecd00ca3f9f2d9ff4d48e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kind", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectSpecNamespaceResourceWhitelistStruct]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectSpecNamespaceResourceWhitelistStruct]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectSpecNamespaceResourceWhitelistStruct]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae1bc624f42c3e6c535a22ec7a5a693b6f788f08344523b843b398857e7a7186)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="argocd.project.ProjectSpecOrphanedResources",
    jsii_struct_bases=[],
    name_mapping={"ignore": "ignore", "warn": "warn"},
)
class ProjectSpecOrphanedResources:
    def __init__(
        self,
        *,
        ignore: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ProjectSpecOrphanedResourcesIgnore", typing.Dict[builtins.str, typing.Any]]]]] = None,
        warn: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param ignore: ignore block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#ignore Project#ignore}
        :param warn: Whether a warning condition should be created for apps which have orphaned resources. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#warn Project#warn}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9a5612b341433faf571ee5f513d30808d28ac3c135a58aae6690a17cc5302e0)
            check_type(argname="argument ignore", value=ignore, expected_type=type_hints["ignore"])
            check_type(argname="argument warn", value=warn, expected_type=type_hints["warn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if ignore is not None:
            self._values["ignore"] = ignore
        if warn is not None:
            self._values["warn"] = warn

    @builtins.property
    def ignore(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ProjectSpecOrphanedResourcesIgnore"]]]:
        '''ignore block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#ignore Project#ignore}
        '''
        result = self._values.get("ignore")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ProjectSpecOrphanedResourcesIgnore"]]], result)

    @builtins.property
    def warn(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether a warning condition should be created for apps which have orphaned resources.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#warn Project#warn}
        '''
        result = self._values.get("warn")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProjectSpecOrphanedResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="argocd.project.ProjectSpecOrphanedResourcesIgnore",
    jsii_struct_bases=[],
    name_mapping={"group": "group", "kind": "kind", "name": "name"},
)
class ProjectSpecOrphanedResourcesIgnore:
    def __init__(
        self,
        *,
        group: typing.Optional[builtins.str] = None,
        kind: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param group: The Kubernetes resource Group to match for. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#group Project#group}
        :param kind: The Kubernetes resource Kind to match for. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#kind Project#kind}
        :param name: The Kubernetes resource name to match for. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#name Project#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f80bfe15be73778a34951b232a196b60101eb7624f461b369bd28ce309e4aaf)
            check_type(argname="argument group", value=group, expected_type=type_hints["group"])
            check_type(argname="argument kind", value=kind, expected_type=type_hints["kind"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if group is not None:
            self._values["group"] = group
        if kind is not None:
            self._values["kind"] = kind
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def group(self) -> typing.Optional[builtins.str]:
        '''The Kubernetes resource Group to match for.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#group Project#group}
        '''
        result = self._values.get("group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kind(self) -> typing.Optional[builtins.str]:
        '''The Kubernetes resource Kind to match for.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#kind Project#kind}
        '''
        result = self._values.get("kind")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The Kubernetes resource name to match for.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#name Project#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProjectSpecOrphanedResourcesIgnore(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ProjectSpecOrphanedResourcesIgnoreList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.project.ProjectSpecOrphanedResourcesIgnoreList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__88fe479c35807d24d494ab8905304ce74c45e1c9b3bdd8745b69f729cfcce855)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ProjectSpecOrphanedResourcesIgnoreOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5fa8d5b0fb5797d967a203b6ecab14db3030d0d2f29abd48f64c47a30c874afe)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ProjectSpecOrphanedResourcesIgnoreOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8bd1360d3951dad86015d10b113d61f2e788bf941a806fa40f37421cce473217)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0bd71d68600029f631df91ea62f9f4f6647a2a6f79cba3f885c5ae86d669265b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6cde354d554fbf1ebae9ec3be4284ee78728ca624a6c7f22f66b47d96046dc88)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectSpecOrphanedResourcesIgnore]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectSpecOrphanedResourcesIgnore]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectSpecOrphanedResourcesIgnore]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b9e38ff118aea492c9e798c8743dd72c823c33063575458e874e632061b1bfe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ProjectSpecOrphanedResourcesIgnoreOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.project.ProjectSpecOrphanedResourcesIgnoreOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__785645f2fd49f760b5397d81b0e418ac98fcbc138df7a83028070555d40ba6d1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetGroup")
    def reset_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroup", []))

    @jsii.member(jsii_name="resetKind")
    def reset_kind(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKind", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="groupInput")
    def group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupInput"))

    @builtins.property
    @jsii.member(jsii_name="kindInput")
    def kind_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kindInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="group")
    def group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "group"))

    @group.setter
    def group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a54a95130871b369bb36f184256dc4b94787f25f637799b850b3277760b1209e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "group", value)

    @builtins.property
    @jsii.member(jsii_name="kind")
    def kind(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kind"))

    @kind.setter
    def kind(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a557e22b3e13c2acd07a530646ab608dd49aa15c29ae14ecd6763578ef59a283)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kind", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32b1b5821fba280449c296586f5ba825eafd3428a67d26ba718f4a05757fb037)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectSpecOrphanedResourcesIgnore]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectSpecOrphanedResourcesIgnore]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectSpecOrphanedResourcesIgnore]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec6769006d86c6624d5a5dfe1ceb8804d3591f57dc8a92e525eec2ddf38f66e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ProjectSpecOrphanedResourcesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.project.ProjectSpecOrphanedResourcesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7c56583078b5929e6f1a7fe3319b863f93cf4b75e101caae3fa85fec5fa98a79)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putIgnore")
    def put_ignore(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ProjectSpecOrphanedResourcesIgnore, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0dcd94aa32ba6b86e06b6682b8413ab4a7e076dbb1d96ddc62e64f08942f70f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putIgnore", [value]))

    @jsii.member(jsii_name="resetIgnore")
    def reset_ignore(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnore", []))

    @jsii.member(jsii_name="resetWarn")
    def reset_warn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWarn", []))

    @builtins.property
    @jsii.member(jsii_name="ignore")
    def ignore(self) -> ProjectSpecOrphanedResourcesIgnoreList:
        return typing.cast(ProjectSpecOrphanedResourcesIgnoreList, jsii.get(self, "ignore"))

    @builtins.property
    @jsii.member(jsii_name="ignoreInput")
    def ignore_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectSpecOrphanedResourcesIgnore]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectSpecOrphanedResourcesIgnore]]], jsii.get(self, "ignoreInput"))

    @builtins.property
    @jsii.member(jsii_name="warnInput")
    def warn_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "warnInput"))

    @builtins.property
    @jsii.member(jsii_name="warn")
    def warn(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "warn"))

    @warn.setter
    def warn(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00094d96eb7a781d639552b3461b1ae6cacb97e9c300e0e45aed6ae9a72e1646)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "warn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ProjectSpecOrphanedResources]:
        return typing.cast(typing.Optional[ProjectSpecOrphanedResources], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ProjectSpecOrphanedResources],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f8dbc5c8d0fb25610b68dc6dbf92894aadd4f1ed436c1d96425917f977d7b86)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ProjectSpecOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.project.ProjectSpecOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5c5fdabde7b24eb2747204cd9b39e33c0105501c3310a697f8a004a6a0d676d0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putClusterResourceBlacklist")
    def put_cluster_resource_blacklist(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ProjectSpecClusterResourceBlacklistStruct, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8efd4e2a2a486b8d83ebfd1c395799fb1a1a4b826b93532eca1350ab653ecbf4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putClusterResourceBlacklist", [value]))

    @jsii.member(jsii_name="putClusterResourceWhitelist")
    def put_cluster_resource_whitelist(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ProjectSpecClusterResourceWhitelistStruct, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d657ff5f377e3142d89b54d9ab7aa2f2466d9be267853ac85ecf00cc3ef998f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putClusterResourceWhitelist", [value]))

    @jsii.member(jsii_name="putDestination")
    def put_destination(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ProjectSpecDestination, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08ba263c11fbb7dd2214aef8272f2a50e78b1ded3e8e62928cdddbb433804286)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDestination", [value]))

    @jsii.member(jsii_name="putNamespaceResourceBlacklist")
    def put_namespace_resource_blacklist(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ProjectSpecNamespaceResourceBlacklistStruct, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0b92722a8ed9f127d6479488615e419a7ed9ca8c96b68ab5bc23c10be1b85b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNamespaceResourceBlacklist", [value]))

    @jsii.member(jsii_name="putNamespaceResourceWhitelist")
    def put_namespace_resource_whitelist(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ProjectSpecNamespaceResourceWhitelistStruct, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7817b0a257f6f23aabecbbf5a0f35918afccbedb3f7d86f20dd61a810f75090)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNamespaceResourceWhitelist", [value]))

    @jsii.member(jsii_name="putOrphanedResources")
    def put_orphaned_resources(
        self,
        *,
        ignore: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ProjectSpecOrphanedResourcesIgnore, typing.Dict[builtins.str, typing.Any]]]]] = None,
        warn: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param ignore: ignore block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#ignore Project#ignore}
        :param warn: Whether a warning condition should be created for apps which have orphaned resources. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#warn Project#warn}
        '''
        value = ProjectSpecOrphanedResources(ignore=ignore, warn=warn)

        return typing.cast(None, jsii.invoke(self, "putOrphanedResources", [value]))

    @jsii.member(jsii_name="putRole")
    def put_role(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ProjectSpecRole", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6bee040e6b4a476b1ff49dde1fef5384cf20077b677386693434623669ffb205)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRole", [value]))

    @jsii.member(jsii_name="putSyncWindow")
    def put_sync_window(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ProjectSpecSyncWindow", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__582fef51e2aed7c62890a1dea182e0eea6750c416b9d54f95ff3ad76cc32434c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSyncWindow", [value]))

    @jsii.member(jsii_name="resetClusterResourceBlacklist")
    def reset_cluster_resource_blacklist(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterResourceBlacklist", []))

    @jsii.member(jsii_name="resetClusterResourceWhitelist")
    def reset_cluster_resource_whitelist(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterResourceWhitelist", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetNamespaceResourceBlacklist")
    def reset_namespace_resource_blacklist(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespaceResourceBlacklist", []))

    @jsii.member(jsii_name="resetNamespaceResourceWhitelist")
    def reset_namespace_resource_whitelist(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespaceResourceWhitelist", []))

    @jsii.member(jsii_name="resetOrphanedResources")
    def reset_orphaned_resources(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrphanedResources", []))

    @jsii.member(jsii_name="resetRole")
    def reset_role(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRole", []))

    @jsii.member(jsii_name="resetSignatureKeys")
    def reset_signature_keys(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSignatureKeys", []))

    @jsii.member(jsii_name="resetSourceNamespaces")
    def reset_source_namespaces(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceNamespaces", []))

    @jsii.member(jsii_name="resetSyncWindow")
    def reset_sync_window(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSyncWindow", []))

    @builtins.property
    @jsii.member(jsii_name="clusterResourceBlacklist")
    def cluster_resource_blacklist(
        self,
    ) -> ProjectSpecClusterResourceBlacklistStructList:
        return typing.cast(ProjectSpecClusterResourceBlacklistStructList, jsii.get(self, "clusterResourceBlacklist"))

    @builtins.property
    @jsii.member(jsii_name="clusterResourceWhitelist")
    def cluster_resource_whitelist(
        self,
    ) -> ProjectSpecClusterResourceWhitelistStructList:
        return typing.cast(ProjectSpecClusterResourceWhitelistStructList, jsii.get(self, "clusterResourceWhitelist"))

    @builtins.property
    @jsii.member(jsii_name="destination")
    def destination(self) -> ProjectSpecDestinationList:
        return typing.cast(ProjectSpecDestinationList, jsii.get(self, "destination"))

    @builtins.property
    @jsii.member(jsii_name="namespaceResourceBlacklist")
    def namespace_resource_blacklist(
        self,
    ) -> ProjectSpecNamespaceResourceBlacklistStructList:
        return typing.cast(ProjectSpecNamespaceResourceBlacklistStructList, jsii.get(self, "namespaceResourceBlacklist"))

    @builtins.property
    @jsii.member(jsii_name="namespaceResourceWhitelist")
    def namespace_resource_whitelist(
        self,
    ) -> ProjectSpecNamespaceResourceWhitelistStructList:
        return typing.cast(ProjectSpecNamespaceResourceWhitelistStructList, jsii.get(self, "namespaceResourceWhitelist"))

    @builtins.property
    @jsii.member(jsii_name="orphanedResources")
    def orphaned_resources(self) -> ProjectSpecOrphanedResourcesOutputReference:
        return typing.cast(ProjectSpecOrphanedResourcesOutputReference, jsii.get(self, "orphanedResources"))

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> "ProjectSpecRoleList":
        return typing.cast("ProjectSpecRoleList", jsii.get(self, "role"))

    @builtins.property
    @jsii.member(jsii_name="syncWindow")
    def sync_window(self) -> "ProjectSpecSyncWindowList":
        return typing.cast("ProjectSpecSyncWindowList", jsii.get(self, "syncWindow"))

    @builtins.property
    @jsii.member(jsii_name="clusterResourceBlacklistInput")
    def cluster_resource_blacklist_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectSpecClusterResourceBlacklistStruct]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectSpecClusterResourceBlacklistStruct]]], jsii.get(self, "clusterResourceBlacklistInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterResourceWhitelistInput")
    def cluster_resource_whitelist_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectSpecClusterResourceWhitelistStruct]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectSpecClusterResourceWhitelistStruct]]], jsii.get(self, "clusterResourceWhitelistInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationInput")
    def destination_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectSpecDestination]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectSpecDestination]]], jsii.get(self, "destinationInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceResourceBlacklistInput")
    def namespace_resource_blacklist_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectSpecNamespaceResourceBlacklistStruct]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectSpecNamespaceResourceBlacklistStruct]]], jsii.get(self, "namespaceResourceBlacklistInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceResourceWhitelistInput")
    def namespace_resource_whitelist_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectSpecNamespaceResourceWhitelistStruct]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectSpecNamespaceResourceWhitelistStruct]]], jsii.get(self, "namespaceResourceWhitelistInput"))

    @builtins.property
    @jsii.member(jsii_name="orphanedResourcesInput")
    def orphaned_resources_input(self) -> typing.Optional[ProjectSpecOrphanedResources]:
        return typing.cast(typing.Optional[ProjectSpecOrphanedResources], jsii.get(self, "orphanedResourcesInput"))

    @builtins.property
    @jsii.member(jsii_name="roleInput")
    def role_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ProjectSpecRole"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ProjectSpecRole"]]], jsii.get(self, "roleInput"))

    @builtins.property
    @jsii.member(jsii_name="signatureKeysInput")
    def signature_keys_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "signatureKeysInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceNamespacesInput")
    def source_namespaces_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sourceNamespacesInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceReposInput")
    def source_repos_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sourceReposInput"))

    @builtins.property
    @jsii.member(jsii_name="syncWindowInput")
    def sync_window_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ProjectSpecSyncWindow"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ProjectSpecSyncWindow"]]], jsii.get(self, "syncWindowInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__473267226b1a6c04160114fe73d387c296d7543b97a095878d6a445b693bfce6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="signatureKeys")
    def signature_keys(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "signatureKeys"))

    @signature_keys.setter
    def signature_keys(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70f507bda8e4d9c3ca6eadf22ad6d8a15a25f31bd34b60d27fa276d002e3a0bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "signatureKeys", value)

    @builtins.property
    @jsii.member(jsii_name="sourceNamespaces")
    def source_namespaces(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sourceNamespaces"))

    @source_namespaces.setter
    def source_namespaces(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29bbf81d1f5a31aa0be3a31ec70f84f7417100b10bd13c8050c67b94dcb3fa42)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceNamespaces", value)

    @builtins.property
    @jsii.member(jsii_name="sourceRepos")
    def source_repos(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sourceRepos"))

    @source_repos.setter
    def source_repos(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c67fd744cc8e0f8a75ce41a9a0bdc0a17ccd1208983309824e8496048d8899f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceRepos", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ProjectSpec]:
        return typing.cast(typing.Optional[ProjectSpec], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ProjectSpec]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__133615b023d07209aa7f8972178058488f8c369b0bfd2654b60a646e20ee3a39)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="argocd.project.ProjectSpecRole",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "policies": "policies",
        "description": "description",
        "groups": "groups",
    },
)
class ProjectSpecRole:
    def __init__(
        self,
        *,
        name: builtins.str,
        policies: typing.Sequence[builtins.str],
        description: typing.Optional[builtins.str] = None,
        groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param name: Name of the role. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#name Project#name}
        :param policies: List of casbin formatted strings that define access policies for the role in the project. For more information, see the `ArgoCD RBAC reference <https://argoproj.github.io/argo-cd/operator-manual/rbac/#rbac-permission-structure>`_. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#policies Project#policies}
        :param description: Description of the role. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#description Project#description}
        :param groups: List of OIDC group claims bound to this role. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#groups Project#groups}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c91da7b81eb4485459948d146a86860ceaa56d7b2fd4d9297dddeb413d864e73)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument policies", value=policies, expected_type=type_hints["policies"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument groups", value=groups, expected_type=type_hints["groups"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "policies": policies,
        }
        if description is not None:
            self._values["description"] = description
        if groups is not None:
            self._values["groups"] = groups

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the role.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#name Project#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policies(self) -> typing.List[builtins.str]:
        '''List of casbin formatted strings that define access policies for the role in the project.

        For more information, see the `ArgoCD RBAC reference <https://argoproj.github.io/argo-cd/operator-manual/rbac/#rbac-permission-structure>`_.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#policies Project#policies}
        '''
        result = self._values.get("policies")
        assert result is not None, "Required property 'policies' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Description of the role.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#description Project#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of OIDC group claims bound to this role.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#groups Project#groups}
        '''
        result = self._values.get("groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProjectSpecRole(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ProjectSpecRoleList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.project.ProjectSpecRoleList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b485816c7d74e81d9cb11991e2e142f30efb9ce47651d248e679884d9f58d7da)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ProjectSpecRoleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c2bbd4393428d11b937aa8311116decd5cdd432e55feabfd23b40d3ec008933)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ProjectSpecRoleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e05f56377ad02948513f76f3e8df87a6c9e34fc9eeaf1b8c2d0568b0a7cad03)
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
            type_hints = typing.get_type_hints(_typecheckingstub__cac5ae281a69eb38aa72d693f24f7e8417a74c3df0d5cb321c11f18a0033807c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__febf0e39b548632c2ed818e243f52318bf798fd7af8b3fc2bc695217cbfb08ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectSpecRole]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectSpecRole]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectSpecRole]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f724d5285e9df4fa566e636893416b41cb68c0aed21cc9ec6b760de3ffe835be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ProjectSpecRoleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.project.ProjectSpecRoleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__284602c9d41eee7f88058886fec94c27fcb93124f3aa825ed6feb96b0892a0e5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetGroups")
    def reset_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroups", []))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="groupsInput")
    def groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "groupsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="policiesInput")
    def policies_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "policiesInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ead9835b211c5dc5cb8ce4ab8d06e356184042cfd4a705557219215b718961c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="groups")
    def groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "groups"))

    @groups.setter
    def groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc113df7c6a529786fd4371f9e38e1cac3cf45cbb0cd3e8e34ed8de7ce45e06c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groups", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3400cc219c1db1794d497348b028a1acd0f6d0670d2d0c45c289ce92ed2c207)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="policies")
    def policies(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "policies"))

    @policies.setter
    def policies(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a65f728259fb08b3118674bf168379c4f535377940641abdcd93a248f71c0933)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policies", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectSpecRole]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectSpecRole]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectSpecRole]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6ff2ed4b0d6df4ae91151453bf7eafacaf45923368cc20d5a9ea4171176e389)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="argocd.project.ProjectSpecSyncWindow",
    jsii_struct_bases=[],
    name_mapping={
        "applications": "applications",
        "clusters": "clusters",
        "duration": "duration",
        "kind": "kind",
        "manual_sync": "manualSync",
        "namespaces": "namespaces",
        "schedule": "schedule",
        "timezone": "timezone",
    },
)
class ProjectSpecSyncWindow:
    def __init__(
        self,
        *,
        applications: typing.Optional[typing.Sequence[builtins.str]] = None,
        clusters: typing.Optional[typing.Sequence[builtins.str]] = None,
        duration: typing.Optional[builtins.str] = None,
        kind: typing.Optional[builtins.str] = None,
        manual_sync: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        namespaces: typing.Optional[typing.Sequence[builtins.str]] = None,
        schedule: typing.Optional[builtins.str] = None,
        timezone: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param applications: List of applications that the window will apply to. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#applications Project#applications}
        :param clusters: List of clusters that the window will apply to. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#clusters Project#clusters}
        :param duration: Amount of time the sync window will be open. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#duration Project#duration}
        :param kind: Defines if the window allows or blocks syncs, allowed values are ``allow`` or ``deny``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#kind Project#kind}
        :param manual_sync: Enables manual syncs when they would otherwise be blocked. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#manual_sync Project#manual_sync}
        :param namespaces: List of namespaces that the window will apply to. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#namespaces Project#namespaces}
        :param schedule: Time the window will begin, specified in cron format. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#schedule Project#schedule}
        :param timezone: Timezone that the schedule will be evaluated in. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#timezone Project#timezone}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8af0dcd70700108581ca7659a1e00640e3674fd72971dfd6e8a85ff028e11e73)
            check_type(argname="argument applications", value=applications, expected_type=type_hints["applications"])
            check_type(argname="argument clusters", value=clusters, expected_type=type_hints["clusters"])
            check_type(argname="argument duration", value=duration, expected_type=type_hints["duration"])
            check_type(argname="argument kind", value=kind, expected_type=type_hints["kind"])
            check_type(argname="argument manual_sync", value=manual_sync, expected_type=type_hints["manual_sync"])
            check_type(argname="argument namespaces", value=namespaces, expected_type=type_hints["namespaces"])
            check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
            check_type(argname="argument timezone", value=timezone, expected_type=type_hints["timezone"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if applications is not None:
            self._values["applications"] = applications
        if clusters is not None:
            self._values["clusters"] = clusters
        if duration is not None:
            self._values["duration"] = duration
        if kind is not None:
            self._values["kind"] = kind
        if manual_sync is not None:
            self._values["manual_sync"] = manual_sync
        if namespaces is not None:
            self._values["namespaces"] = namespaces
        if schedule is not None:
            self._values["schedule"] = schedule
        if timezone is not None:
            self._values["timezone"] = timezone

    @builtins.property
    def applications(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of applications that the window will apply to.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#applications Project#applications}
        '''
        result = self._values.get("applications")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def clusters(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of clusters that the window will apply to.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#clusters Project#clusters}
        '''
        result = self._values.get("clusters")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def duration(self) -> typing.Optional[builtins.str]:
        '''Amount of time the sync window will be open.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#duration Project#duration}
        '''
        result = self._values.get("duration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kind(self) -> typing.Optional[builtins.str]:
        '''Defines if the window allows or blocks syncs, allowed values are ``allow`` or ``deny``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#kind Project#kind}
        '''
        result = self._values.get("kind")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def manual_sync(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Enables manual syncs when they would otherwise be blocked.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#manual_sync Project#manual_sync}
        '''
        result = self._values.get("manual_sync")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def namespaces(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of namespaces that the window will apply to.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#namespaces Project#namespaces}
        '''
        result = self._values.get("namespaces")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def schedule(self) -> typing.Optional[builtins.str]:
        '''Time the window will begin, specified in cron format.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#schedule Project#schedule}
        '''
        result = self._values.get("schedule")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timezone(self) -> typing.Optional[builtins.str]:
        '''Timezone that the schedule will be evaluated in.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/project#timezone Project#timezone}
        '''
        result = self._values.get("timezone")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProjectSpecSyncWindow(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ProjectSpecSyncWindowList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.project.ProjectSpecSyncWindowList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__04d05205c4280e3b1d109824d9edb7fed83b2a16f926720974c2d6dacc79743b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ProjectSpecSyncWindowOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dbfaecfd1a62ad9cbc484a09acc8cfec0c8fe33306706ca5f290886d9b029b14)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ProjectSpecSyncWindowOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c0427cd85fbc56f18090df4ea5b6d4dbc4e48366d4e51b8de78fa2d4c2181c5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9a250e6cf970909b2759372e5b930ce77c7ce58af71eee71a25aaf5b0d21ff19)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9d277696242e99a0161e4c45635558aa71a7a6c5b7dea1b192f535993de6adee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectSpecSyncWindow]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectSpecSyncWindow]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectSpecSyncWindow]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b54e4ccf60b5327d5764a9f4fe6b84813b3fd1f2e64191abd01b2a53460dbc73)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ProjectSpecSyncWindowOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.project.ProjectSpecSyncWindowOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__036f1c4b16c673bcbda99bc20650480fd42d59011d929e096fea98f02bfb6f28)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetApplications")
    def reset_applications(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApplications", []))

    @jsii.member(jsii_name="resetClusters")
    def reset_clusters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusters", []))

    @jsii.member(jsii_name="resetDuration")
    def reset_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDuration", []))

    @jsii.member(jsii_name="resetKind")
    def reset_kind(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKind", []))

    @jsii.member(jsii_name="resetManualSync")
    def reset_manual_sync(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManualSync", []))

    @jsii.member(jsii_name="resetNamespaces")
    def reset_namespaces(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespaces", []))

    @jsii.member(jsii_name="resetSchedule")
    def reset_schedule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchedule", []))

    @jsii.member(jsii_name="resetTimezone")
    def reset_timezone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimezone", []))

    @builtins.property
    @jsii.member(jsii_name="applicationsInput")
    def applications_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "applicationsInput"))

    @builtins.property
    @jsii.member(jsii_name="clustersInput")
    def clusters_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "clustersInput"))

    @builtins.property
    @jsii.member(jsii_name="durationInput")
    def duration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "durationInput"))

    @builtins.property
    @jsii.member(jsii_name="kindInput")
    def kind_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kindInput"))

    @builtins.property
    @jsii.member(jsii_name="manualSyncInput")
    def manual_sync_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "manualSyncInput"))

    @builtins.property
    @jsii.member(jsii_name="namespacesInput")
    def namespaces_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "namespacesInput"))

    @builtins.property
    @jsii.member(jsii_name="scheduleInput")
    def schedule_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scheduleInput"))

    @builtins.property
    @jsii.member(jsii_name="timezoneInput")
    def timezone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timezoneInput"))

    @builtins.property
    @jsii.member(jsii_name="applications")
    def applications(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "applications"))

    @applications.setter
    def applications(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66f46fcd4cae9e4c7ed91e84d390b77b1502b5d0ad71f3d2aa2915128e2e8015)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applications", value)

    @builtins.property
    @jsii.member(jsii_name="clusters")
    def clusters(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "clusters"))

    @clusters.setter
    def clusters(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e4877a6c5df0a2a782b3713ea82682869f6d668b107891f0fe7da5f18a22e58)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusters", value)

    @builtins.property
    @jsii.member(jsii_name="duration")
    def duration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "duration"))

    @duration.setter
    def duration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed93b4a976d30a7c89752b1158505a55d35660cfbd3b32a027d023e21c09c536)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "duration", value)

    @builtins.property
    @jsii.member(jsii_name="kind")
    def kind(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kind"))

    @kind.setter
    def kind(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__821d3e4eb56040954d3ddcee53f4cd4c55f016e19747c116243392097c57b1da)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kind", value)

    @builtins.property
    @jsii.member(jsii_name="manualSync")
    def manual_sync(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "manualSync"))

    @manual_sync.setter
    def manual_sync(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b16aef0648736f18d9000f942bd91f521b836bd54d41d915167301d9bbadfa0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "manualSync", value)

    @builtins.property
    @jsii.member(jsii_name="namespaces")
    def namespaces(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "namespaces"))

    @namespaces.setter
    def namespaces(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2188b2c66a45121a99fa86cc930b3ebc76800d185849fbea9f86250a9c3f51c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespaces", value)

    @builtins.property
    @jsii.member(jsii_name="schedule")
    def schedule(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schedule"))

    @schedule.setter
    def schedule(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43775029a82762fe0d205d8c8734f76132714ad3d0f13beb3c7dc111d9ce03b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schedule", value)

    @builtins.property
    @jsii.member(jsii_name="timezone")
    def timezone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timezone"))

    @timezone.setter
    def timezone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__975fa9600d48cf20980b6f68255cdce3e71352a888aae54141cf8de68db44e6e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timezone", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectSpecSyncWindow]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectSpecSyncWindow]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectSpecSyncWindow]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f85b52639c5b41aca4ac074ca9637bce17dcb406b20c4b0f8368b3437ca121f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Project",
    "ProjectConfig",
    "ProjectMetadata",
    "ProjectMetadataOutputReference",
    "ProjectSpec",
    "ProjectSpecClusterResourceBlacklistStruct",
    "ProjectSpecClusterResourceBlacklistStructList",
    "ProjectSpecClusterResourceBlacklistStructOutputReference",
    "ProjectSpecClusterResourceWhitelistStruct",
    "ProjectSpecClusterResourceWhitelistStructList",
    "ProjectSpecClusterResourceWhitelistStructOutputReference",
    "ProjectSpecDestination",
    "ProjectSpecDestinationList",
    "ProjectSpecDestinationOutputReference",
    "ProjectSpecNamespaceResourceBlacklistStruct",
    "ProjectSpecNamespaceResourceBlacklistStructList",
    "ProjectSpecNamespaceResourceBlacklistStructOutputReference",
    "ProjectSpecNamespaceResourceWhitelistStruct",
    "ProjectSpecNamespaceResourceWhitelistStructList",
    "ProjectSpecNamespaceResourceWhitelistStructOutputReference",
    "ProjectSpecOrphanedResources",
    "ProjectSpecOrphanedResourcesIgnore",
    "ProjectSpecOrphanedResourcesIgnoreList",
    "ProjectSpecOrphanedResourcesIgnoreOutputReference",
    "ProjectSpecOrphanedResourcesOutputReference",
    "ProjectSpecOutputReference",
    "ProjectSpecRole",
    "ProjectSpecRoleList",
    "ProjectSpecRoleOutputReference",
    "ProjectSpecSyncWindow",
    "ProjectSpecSyncWindowList",
    "ProjectSpecSyncWindowOutputReference",
]

publication.publish()

def _typecheckingstub__e3d3d12bf0919961ff0081d1f1b5ce17f68906ef58dcb6dcfb94af7b73ae1086(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    metadata: typing.Union[ProjectMetadata, typing.Dict[builtins.str, typing.Any]],
    spec: typing.Union[ProjectSpec, typing.Dict[builtins.str, typing.Any]],
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

def _typecheckingstub__95b4bf546f3b84e96dd9e865f7bc676cdaa215bd5a9b3cb63ea90985106656b0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9497154d335aa51fa1cc3c762b4b407ef098098a87e966d5ebc0b5b000f2816f(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    metadata: typing.Union[ProjectMetadata, typing.Dict[builtins.str, typing.Any]],
    spec: typing.Union[ProjectSpec, typing.Dict[builtins.str, typing.Any]],
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0f47e9f8dd93f2f280b59d5162ae992ccb3136741c570e1b40063ea6fc59ccf(
    *,
    annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    name: typing.Optional[builtins.str] = None,
    namespace: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e0049732ed9943592a92ce1862076bae0fbd0e3ce057d22ab205203e3e296b2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c033bc30e6c4d3b6a49ef402f3ca2d361b62154178432d3fe96254767c6356df(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d0a3429c9a9fe1a3f6558922ea469e77c0fc5264335d0a5d9dc9637251bae7a(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f620e7ee8ef3af2885b74b56bad52ffac96184766d35f6669ea08ad16422bda9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b55326445ed8cf45566e74ca9651e905bbe5404bac0797f418a2628dc19b50e6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31b3b6ebe794b8f1e9aee8d7575b966766616cf290a1faa9ae8d9bf8ea0c6a4e(
    value: typing.Optional[ProjectMetadata],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18398239103ff4388e1197523ab4342e8f584b621fcfa1bdfe5d0d120d677423(
    *,
    destination: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ProjectSpecDestination, typing.Dict[builtins.str, typing.Any]]]],
    source_repos: typing.Sequence[builtins.str],
    cluster_resource_blacklist: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ProjectSpecClusterResourceBlacklistStruct, typing.Dict[builtins.str, typing.Any]]]]] = None,
    cluster_resource_whitelist: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ProjectSpecClusterResourceWhitelistStruct, typing.Dict[builtins.str, typing.Any]]]]] = None,
    description: typing.Optional[builtins.str] = None,
    namespace_resource_blacklist: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ProjectSpecNamespaceResourceBlacklistStruct, typing.Dict[builtins.str, typing.Any]]]]] = None,
    namespace_resource_whitelist: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ProjectSpecNamespaceResourceWhitelistStruct, typing.Dict[builtins.str, typing.Any]]]]] = None,
    orphaned_resources: typing.Optional[typing.Union[ProjectSpecOrphanedResources, typing.Dict[builtins.str, typing.Any]]] = None,
    role: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ProjectSpecRole, typing.Dict[builtins.str, typing.Any]]]]] = None,
    signature_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
    source_namespaces: typing.Optional[typing.Sequence[builtins.str]] = None,
    sync_window: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ProjectSpecSyncWindow, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa743e36d7fdd14d3c1131afce7270004ad566eadc3ffdb1aabf32953e97607f(
    *,
    group: typing.Optional[builtins.str] = None,
    kind: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94b4d952d0273fe08b23548315d3d17ca2e751fcff16d08f8615c177dbfb36bf(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f81f5c643730dd7e88e02278ef088ae67194a14d2e2a93700737c4c8ef596d3c(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a91399d45f01f608e4a2e8460f4f412bdf3df0bbbc2bc4e25abe6b3f7211aafb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5195bc662586ae7f164d532db8ca8d5c5e1eeec2c668caa7778607e5eab2b74e(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c67ebe055152d204f4b8dd339d720fc94bf9269cfab4f6f9716e57f84fb5163(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ed8c66cd4c12189ede0f4b4556ac2ff15a6be48cb659ce87c0d714c814bdf25(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectSpecClusterResourceBlacklistStruct]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb47f92b6cbc57ce872c6a15347515ebbed803b80009000d69c3b42f2ed746c6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__026968de30b0919ac9f816abd44ec43a72541adc0343e8ce177d9ae978f0a6a4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee69af0d85800cca57cfecec7f97143067247795a9aa675057bcf4132cb39d45(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__341251d2c89972a060d013a4aba0678fb262e5f753a8ae0c9fb5a908a4d7ced3(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectSpecClusterResourceBlacklistStruct]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef252e43a4079517d42e2a988d0ec61d23adf4c71077b0f49cc830c5c2a3d337(
    *,
    group: typing.Optional[builtins.str] = None,
    kind: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a0349f68bb22e03d446c8ab8c4638474196b7c54704e4b789bfb619d3ccca08(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cad1675d8d945158d3b5b4d2ad4c99215c7fbb21efe3e2877487a4ec5bf0c39a(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2236a9d3cdf7d2524ebaeafd89b6a2c78e5ac58104892b64bf42abc0c063f618(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e04d890c78d5e8327b733a338fdaae1459c1517b59ebdba4099e30550f0d0fe(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d2ae583767993e5aa1cfca6939e976806af2136545bdd2ed31b992e45cd9862(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06f760453338533d3149780f7b5c6e0bdf9a47784332986835fa6e9263298185(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectSpecClusterResourceWhitelistStruct]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15c24dbe075f1e94e8ee8225aca51e2525b812414eaf1086c0684d219ff47e2e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58aaece878a6e6e9fe181289efbdc3053e20fbdd4dc6621f9fb5f66555a50a5d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f64bda654841f57b941e1705b1527d649c77c9611db196d3b6230af7190fad49(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70e598907ebeabef68881ef68bcc292433270f798d0a3f09b75adc61fc5b628b(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectSpecClusterResourceWhitelistStruct]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fbd1a96bbe6ead42fbb3685ccdeef683ef37b1556d03eb58a4c566a6dd18e9d(
    *,
    namespace: builtins.str,
    name: typing.Optional[builtins.str] = None,
    server: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43f93fdc162a287ffd2ce003fadfd1bdd41c2d8f98be3a94b3ae86158874dc24(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43a7fe3af317c77abf696f89fd2aa71fae825758c3aa7c820c46a949445fc63c(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a778a21972d579da1856a96ebe1bb7d46437ea0dbdffb31464c0ef2867f02a5e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ceee3c4b3a2683f9180a93236e55c92dda796a050bbf968ea340ef713a6383cd(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4234d40579284e6ee6a964bc3649912574e53dad95be46454d2ccebd69752ba(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e1b55d39f09b8555131c9883a7332c96dcdf46c25e5634ab0a557cd228eb030(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectSpecDestination]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9737ca02cdeab70a5b4de85c1e5142b62d9c83cf7b53879d9986c6140eff1116(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef783d2bdeb94d06028a33bcedd36bcc73d1541b4b735adbb75f3e44cd80ee4c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5253b4e24acef297cb6903d051de8d13a43c74be947f1ea0e3fb30706df44b17(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdf4c61e0787daa6d247c49368a30ee7d14045c2d721fa11caf2c31495a2ddcc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b43a6b3c5de3715758f5ae362f38bb77fc2379b2a610d4dc453194392db9434(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectSpecDestination]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f33da4f66ff4ff0a4b34fc9450a3eb4daf7ac95d9bb8668de286331f5d8d6126(
    *,
    group: typing.Optional[builtins.str] = None,
    kind: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07fb8f98872fbc3b176b9d614d605ffdcd361bc567877c1cfbc4dffb09ec09e3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5dc4de655fa3d686cfc7a6b9f3bd7f33800300755519f41a6c9f98f309539edf(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae4cbafd34b663d50bee961805ac809ced3493e826a43994fd938be08256cb76(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2349a30a8bb6712ba191362741dc4986458551eb953b7302d8510b8c36ae61c(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a46066be1469053c958a1dce7d12205087b8a013c525a358f69b5dae2619307d(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__088c3618c4dacc4c233eba6082d0fed8a1ab8960a57548e9a32d3537b1ac8869(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectSpecNamespaceResourceBlacklistStruct]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__453a6786749b3ec45620c9492340985e11d21c28839895d39478c108d679c439(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__490eff9cee13c66c8da572c14785579eb216cafce218b78342deb59c3dea0c8d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e746ff5c4c2d5157a3679a1a21a425522368bcdba0e906cac57d71b4d499c066(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1f76eb60c6f233ebeaa199981fa93fb04e2c4edf9bd9dbdef74d0a9224db036(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectSpecNamespaceResourceBlacklistStruct]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7de83e18d50f9e79e68b5de9527a0df9cce16c228f2a10081cad1bf3c6fd5357(
    *,
    group: typing.Optional[builtins.str] = None,
    kind: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55231f04db8137cea3aede819a29d07f39f36cfd08d88c75aaeffdfd46866b04(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8039888d88c30f3f4eefbef969a256204194f20657a60a541e0bbb63bfbe0666(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c9b64c42de461d6df1c26434e09dbcf1d61de9bfa67a23e83e993057db77a66(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0bc82a896e2599331f7aa4ef7ab14dbf17b43347274311a69993b791fcc1ba00(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70f096833f4212fd747bc569d47e93f52ee951bbaf63dc2f4a37fb95a9970e35(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf512c9ce22d17c9a930edd72714a01372234d45a191dcaa0e111da010a00140(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectSpecNamespaceResourceWhitelistStruct]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24157ce6dd1b34da5dad9943a7c67fd51dd7543b841b02baf1c67c9b499ddf71(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e82293c81f4a6a7a0ab545e5164284805f579eed03dd4a850bd96fa32d5e6790(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21d71a0aec939ca29aa69f45c6412557d50fb6acd2cecd00ca3f9f2d9ff4d48e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae1bc624f42c3e6c535a22ec7a5a693b6f788f08344523b843b398857e7a7186(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectSpecNamespaceResourceWhitelistStruct]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9a5612b341433faf571ee5f513d30808d28ac3c135a58aae6690a17cc5302e0(
    *,
    ignore: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ProjectSpecOrphanedResourcesIgnore, typing.Dict[builtins.str, typing.Any]]]]] = None,
    warn: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f80bfe15be73778a34951b232a196b60101eb7624f461b369bd28ce309e4aaf(
    *,
    group: typing.Optional[builtins.str] = None,
    kind: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88fe479c35807d24d494ab8905304ce74c45e1c9b3bdd8745b69f729cfcce855(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fa8d5b0fb5797d967a203b6ecab14db3030d0d2f29abd48f64c47a30c874afe(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8bd1360d3951dad86015d10b113d61f2e788bf941a806fa40f37421cce473217(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0bd71d68600029f631df91ea62f9f4f6647a2a6f79cba3f885c5ae86d669265b(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6cde354d554fbf1ebae9ec3be4284ee78728ca624a6c7f22f66b47d96046dc88(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b9e38ff118aea492c9e798c8743dd72c823c33063575458e874e632061b1bfe(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectSpecOrphanedResourcesIgnore]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__785645f2fd49f760b5397d81b0e418ac98fcbc138df7a83028070555d40ba6d1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a54a95130871b369bb36f184256dc4b94787f25f637799b850b3277760b1209e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a557e22b3e13c2acd07a530646ab608dd49aa15c29ae14ecd6763578ef59a283(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32b1b5821fba280449c296586f5ba825eafd3428a67d26ba718f4a05757fb037(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec6769006d86c6624d5a5dfe1ceb8804d3591f57dc8a92e525eec2ddf38f66e2(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectSpecOrphanedResourcesIgnore]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c56583078b5929e6f1a7fe3319b863f93cf4b75e101caae3fa85fec5fa98a79(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0dcd94aa32ba6b86e06b6682b8413ab4a7e076dbb1d96ddc62e64f08942f70f3(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ProjectSpecOrphanedResourcesIgnore, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00094d96eb7a781d639552b3461b1ae6cacb97e9c300e0e45aed6ae9a72e1646(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f8dbc5c8d0fb25610b68dc6dbf92894aadd4f1ed436c1d96425917f977d7b86(
    value: typing.Optional[ProjectSpecOrphanedResources],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c5fdabde7b24eb2747204cd9b39e33c0105501c3310a697f8a004a6a0d676d0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8efd4e2a2a486b8d83ebfd1c395799fb1a1a4b826b93532eca1350ab653ecbf4(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ProjectSpecClusterResourceBlacklistStruct, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d657ff5f377e3142d89b54d9ab7aa2f2466d9be267853ac85ecf00cc3ef998f8(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ProjectSpecClusterResourceWhitelistStruct, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08ba263c11fbb7dd2214aef8272f2a50e78b1ded3e8e62928cdddbb433804286(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ProjectSpecDestination, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0b92722a8ed9f127d6479488615e419a7ed9ca8c96b68ab5bc23c10be1b85b6(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ProjectSpecNamespaceResourceBlacklistStruct, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7817b0a257f6f23aabecbbf5a0f35918afccbedb3f7d86f20dd61a810f75090(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ProjectSpecNamespaceResourceWhitelistStruct, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bee040e6b4a476b1ff49dde1fef5384cf20077b677386693434623669ffb205(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ProjectSpecRole, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__582fef51e2aed7c62890a1dea182e0eea6750c416b9d54f95ff3ad76cc32434c(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ProjectSpecSyncWindow, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__473267226b1a6c04160114fe73d387c296d7543b97a095878d6a445b693bfce6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70f507bda8e4d9c3ca6eadf22ad6d8a15a25f31bd34b60d27fa276d002e3a0bc(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29bbf81d1f5a31aa0be3a31ec70f84f7417100b10bd13c8050c67b94dcb3fa42(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c67fd744cc8e0f8a75ce41a9a0bdc0a17ccd1208983309824e8496048d8899f7(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__133615b023d07209aa7f8972178058488f8c369b0bfd2654b60a646e20ee3a39(
    value: typing.Optional[ProjectSpec],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c91da7b81eb4485459948d146a86860ceaa56d7b2fd4d9297dddeb413d864e73(
    *,
    name: builtins.str,
    policies: typing.Sequence[builtins.str],
    description: typing.Optional[builtins.str] = None,
    groups: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b485816c7d74e81d9cb11991e2e142f30efb9ce47651d248e679884d9f58d7da(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c2bbd4393428d11b937aa8311116decd5cdd432e55feabfd23b40d3ec008933(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e05f56377ad02948513f76f3e8df87a6c9e34fc9eeaf1b8c2d0568b0a7cad03(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cac5ae281a69eb38aa72d693f24f7e8417a74c3df0d5cb321c11f18a0033807c(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__febf0e39b548632c2ed818e243f52318bf798fd7af8b3fc2bc695217cbfb08ec(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f724d5285e9df4fa566e636893416b41cb68c0aed21cc9ec6b760de3ffe835be(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectSpecRole]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__284602c9d41eee7f88058886fec94c27fcb93124f3aa825ed6feb96b0892a0e5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ead9835b211c5dc5cb8ce4ab8d06e356184042cfd4a705557219215b718961c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc113df7c6a529786fd4371f9e38e1cac3cf45cbb0cd3e8e34ed8de7ce45e06c(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3400cc219c1db1794d497348b028a1acd0f6d0670d2d0c45c289ce92ed2c207(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a65f728259fb08b3118674bf168379c4f535377940641abdcd93a248f71c0933(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6ff2ed4b0d6df4ae91151453bf7eafacaf45923368cc20d5a9ea4171176e389(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectSpecRole]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8af0dcd70700108581ca7659a1e00640e3674fd72971dfd6e8a85ff028e11e73(
    *,
    applications: typing.Optional[typing.Sequence[builtins.str]] = None,
    clusters: typing.Optional[typing.Sequence[builtins.str]] = None,
    duration: typing.Optional[builtins.str] = None,
    kind: typing.Optional[builtins.str] = None,
    manual_sync: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    namespaces: typing.Optional[typing.Sequence[builtins.str]] = None,
    schedule: typing.Optional[builtins.str] = None,
    timezone: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04d05205c4280e3b1d109824d9edb7fed83b2a16f926720974c2d6dacc79743b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbfaecfd1a62ad9cbc484a09acc8cfec0c8fe33306706ca5f290886d9b029b14(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c0427cd85fbc56f18090df4ea5b6d4dbc4e48366d4e51b8de78fa2d4c2181c5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a250e6cf970909b2759372e5b930ce77c7ce58af71eee71a25aaf5b0d21ff19(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d277696242e99a0161e4c45635558aa71a7a6c5b7dea1b192f535993de6adee(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b54e4ccf60b5327d5764a9f4fe6b84813b3fd1f2e64191abd01b2a53460dbc73(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectSpecSyncWindow]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__036f1c4b16c673bcbda99bc20650480fd42d59011d929e096fea98f02bfb6f28(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66f46fcd4cae9e4c7ed91e84d390b77b1502b5d0ad71f3d2aa2915128e2e8015(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e4877a6c5df0a2a782b3713ea82682869f6d668b107891f0fe7da5f18a22e58(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed93b4a976d30a7c89752b1158505a55d35660cfbd3b32a027d023e21c09c536(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__821d3e4eb56040954d3ddcee53f4cd4c55f016e19747c116243392097c57b1da(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b16aef0648736f18d9000f942bd91f521b836bd54d41d915167301d9bbadfa0(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2188b2c66a45121a99fa86cc930b3ebc76800d185849fbea9f86250a9c3f51c3(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43775029a82762fe0d205d8c8734f76132714ad3d0f13beb3c7dc111d9ce03b4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__975fa9600d48cf20980b6f68255cdce3e71352a888aae54141cf8de68db44e6e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f85b52639c5b41aca4ac074ca9637bce17dcb406b20c4b0f8368b3437ca121f3(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectSpecSyncWindow]],
) -> None:
    """Type checking stubs"""
    pass
