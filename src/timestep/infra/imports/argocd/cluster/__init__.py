'''
# `argocd_cluster`

Refer to the Terraform Registory for docs: [`argocd_cluster`](https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster).
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


class Cluster(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.cluster.Cluster",
):
    '''Represents a {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster argocd_cluster}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        config: typing.Union["ClusterConfigA", typing.Dict[builtins.str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        metadata: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ClusterMetadata", typing.Dict[builtins.str, typing.Any]]]]] = None,
        name: typing.Optional[builtins.str] = None,
        namespaces: typing.Optional[typing.Sequence[builtins.str]] = None,
        project: typing.Optional[builtins.str] = None,
        server: typing.Optional[builtins.str] = None,
        shard: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster argocd_cluster} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param config: config block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#config Cluster#config}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#id Cluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#metadata Cluster#metadata}
        :param name: Name of the cluster. If omitted, will use the server address. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#name Cluster#name}
        :param namespaces: List of namespaces which are accessible in that cluster. Cluster level resources would be ignored if namespace list is not empty. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#namespaces Cluster#namespaces}
        :param project: Reference between project and cluster that allow you automatically to be added as item inside Destinations project entity. More info: https://argo-cd.readthedocs.io/en/stable/user-guide/projects/#project-scoped-repositories-and-clusters. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#project Cluster#project}
        :param server: Server is the API server URL of the Kubernetes cluster. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#server Cluster#server}
        :param shard: Optional shard number. Calculated on the fly by the application controller if not specified. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#shard Cluster#shard}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b74ed58f16a119a0d0ed009671e35fdf6f16637eb3f70e2ea966e7cd29745e04)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config_ = ClusterConfig(
            config=config,
            id=id,
            metadata=metadata,
            name=name,
            namespaces=namespaces,
            project=project,
            server=server,
            shard=shard,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config_])

    @jsii.member(jsii_name="generateConfigForImport")
    @builtins.classmethod
    def generate_config_for_import(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        import_to_id: builtins.str,
        import_from_id: builtins.str,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    ) -> _cdktf_9a9027ec.ImportableResource:
        '''Generates CDKTF code for importing a Cluster resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the Cluster to import.
        :param import_from_id: The id of the existing Cluster that should be imported. Refer to the {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the Cluster to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b93237249ce4340de04ca4b9d6b448dea5e8647cc70144fc186e12c0295485c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putConfig")
    def put_config(
        self,
        *,
        aws_auth_config: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ClusterConfigAwsAuthConfig", typing.Dict[builtins.str, typing.Any]]]]] = None,
        bearer_token: typing.Optional[builtins.str] = None,
        exec_provider_config: typing.Optional[typing.Union["ClusterConfigExecProviderConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        password: typing.Optional[builtins.str] = None,
        tls_client_config: typing.Optional[typing.Union["ClusterConfigTlsClientConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_auth_config: aws_auth_config block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#aws_auth_config Cluster#aws_auth_config}
        :param bearer_token: Server requires Bearer authentication. The client will not attempt to use refresh tokens for an OAuth2 flow. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#bearer_token Cluster#bearer_token}
        :param exec_provider_config: exec_provider_config block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#exec_provider_config Cluster#exec_provider_config}
        :param password: Password for servers that require Basic authentication. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#password Cluster#password}
        :param tls_client_config: tls_client_config block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#tls_client_config Cluster#tls_client_config}
        :param username: Username for servers that require Basic authentication. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#username Cluster#username}
        '''
        value = ClusterConfigA(
            aws_auth_config=aws_auth_config,
            bearer_token=bearer_token,
            exec_provider_config=exec_provider_config,
            password=password,
            tls_client_config=tls_client_config,
            username=username,
        )

        return typing.cast(None, jsii.invoke(self, "putConfig", [value]))

    @jsii.member(jsii_name="putMetadata")
    def put_metadata(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ClusterMetadata", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4165cea0fb95ae8bf68cc5706f518f1efb249ca4a63fef5958f17fd24e0e8c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMetadata", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMetadata")
    def reset_metadata(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetadata", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNamespaces")
    def reset_namespaces(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespaces", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetServer")
    def reset_server(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServer", []))

    @jsii.member(jsii_name="resetShard")
    def reset_shard(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetShard", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="config")
    def config(self) -> "ClusterConfigAOutputReference":
        return typing.cast("ClusterConfigAOutputReference", jsii.get(self, "config"))

    @builtins.property
    @jsii.member(jsii_name="info")
    def info(self) -> "ClusterInfoList":
        return typing.cast("ClusterInfoList", jsii.get(self, "info"))

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> "ClusterMetadataList":
        return typing.cast("ClusterMetadataList", jsii.get(self, "metadata"))

    @builtins.property
    @jsii.member(jsii_name="configInput")
    def config_input(self) -> typing.Optional["ClusterConfigA"]:
        return typing.cast(typing.Optional["ClusterConfigA"], jsii.get(self, "configInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataInput")
    def metadata_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ClusterMetadata"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ClusterMetadata"]]], jsii.get(self, "metadataInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespacesInput")
    def namespaces_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "namespacesInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="serverInput")
    def server_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverInput"))

    @builtins.property
    @jsii.member(jsii_name="shardInput")
    def shard_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "shardInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a61f61e9752a2326164142d2ebc01f9e9fecb2d74af22e9131defefcbf19ea33)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc98af5cdf14c08b1fb3339f748f030f11c63376f69a8e709c987685dc0c4deb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespaces")
    def namespaces(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "namespaces"))

    @namespaces.setter
    def namespaces(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b031f05d00937342a563c12337ecb1e6ab4c9e6de838648389b38f55182a72df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespaces", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3cc273bc212f0456ea34720255d4dc0aa7474e3e67907b0a5c7e0fad568eb1fc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="server")
    def server(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "server"))

    @server.setter
    def server(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22cad3e145e520db51524e18c7836cee14faeeeeac0ba505dc4e1654e5044f39)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "server", value)

    @builtins.property
    @jsii.member(jsii_name="shard")
    def shard(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "shard"))

    @shard.setter
    def shard(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc63fe3dffbf3ede7259d394d2d6cfb4f57228bc1395fc4ca1a828574f559754)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shard", value)


@jsii.data_type(
    jsii_type="argocd.cluster.ClusterConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "config": "config",
        "id": "id",
        "metadata": "metadata",
        "name": "name",
        "namespaces": "namespaces",
        "project": "project",
        "server": "server",
        "shard": "shard",
    },
)
class ClusterConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        config: typing.Union["ClusterConfigA", typing.Dict[builtins.str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        metadata: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ClusterMetadata", typing.Dict[builtins.str, typing.Any]]]]] = None,
        name: typing.Optional[builtins.str] = None,
        namespaces: typing.Optional[typing.Sequence[builtins.str]] = None,
        project: typing.Optional[builtins.str] = None,
        server: typing.Optional[builtins.str] = None,
        shard: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param config: config block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#config Cluster#config}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#id Cluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#metadata Cluster#metadata}
        :param name: Name of the cluster. If omitted, will use the server address. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#name Cluster#name}
        :param namespaces: List of namespaces which are accessible in that cluster. Cluster level resources would be ignored if namespace list is not empty. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#namespaces Cluster#namespaces}
        :param project: Reference between project and cluster that allow you automatically to be added as item inside Destinations project entity. More info: https://argo-cd.readthedocs.io/en/stable/user-guide/projects/#project-scoped-repositories-and-clusters. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#project Cluster#project}
        :param server: Server is the API server URL of the Kubernetes cluster. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#server Cluster#server}
        :param shard: Optional shard number. Calculated on the fly by the application controller if not specified. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#shard Cluster#shard}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(config, dict):
            config = ClusterConfigA(**config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b7198b9273ab923c023f395b7f3004e7b062f65c92932d8f4482f6167ef446f)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument config", value=config, expected_type=type_hints["config"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespaces", value=namespaces, expected_type=type_hints["namespaces"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument server", value=server, expected_type=type_hints["server"])
            check_type(argname="argument shard", value=shard, expected_type=type_hints["shard"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "config": config,
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
        if metadata is not None:
            self._values["metadata"] = metadata
        if name is not None:
            self._values["name"] = name
        if namespaces is not None:
            self._values["namespaces"] = namespaces
        if project is not None:
            self._values["project"] = project
        if server is not None:
            self._values["server"] = server
        if shard is not None:
            self._values["shard"] = shard

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
    def config(self) -> "ClusterConfigA":
        '''config block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#config Cluster#config}
        '''
        result = self._values.get("config")
        assert result is not None, "Required property 'config' is missing"
        return typing.cast("ClusterConfigA", result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#id Cluster#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metadata(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ClusterMetadata"]]]:
        '''metadata block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#metadata Cluster#metadata}
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ClusterMetadata"]]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the cluster. If omitted, will use the server address.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#name Cluster#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespaces(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of namespaces which are accessible in that cluster.

        Cluster level resources would be ignored if namespace list is not empty.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#namespaces Cluster#namespaces}
        '''
        result = self._values.get("namespaces")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Reference between project and cluster that allow you automatically to be added as item inside Destinations project entity.

        More info: https://argo-cd.readthedocs.io/en/stable/user-guide/projects/#project-scoped-repositories-and-clusters.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#project Cluster#project}
        '''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def server(self) -> typing.Optional[builtins.str]:
        '''Server is the API server URL of the Kubernetes cluster.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#server Cluster#server}
        '''
        result = self._values.get("server")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def shard(self) -> typing.Optional[builtins.str]:
        '''Optional shard number. Calculated on the fly by the application controller if not specified.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#shard Cluster#shard}
        '''
        result = self._values.get("shard")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="argocd.cluster.ClusterConfigA",
    jsii_struct_bases=[],
    name_mapping={
        "aws_auth_config": "awsAuthConfig",
        "bearer_token": "bearerToken",
        "exec_provider_config": "execProviderConfig",
        "password": "password",
        "tls_client_config": "tlsClientConfig",
        "username": "username",
    },
)
class ClusterConfigA:
    def __init__(
        self,
        *,
        aws_auth_config: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ClusterConfigAwsAuthConfig", typing.Dict[builtins.str, typing.Any]]]]] = None,
        bearer_token: typing.Optional[builtins.str] = None,
        exec_provider_config: typing.Optional[typing.Union["ClusterConfigExecProviderConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        password: typing.Optional[builtins.str] = None,
        tls_client_config: typing.Optional[typing.Union["ClusterConfigTlsClientConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_auth_config: aws_auth_config block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#aws_auth_config Cluster#aws_auth_config}
        :param bearer_token: Server requires Bearer authentication. The client will not attempt to use refresh tokens for an OAuth2 flow. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#bearer_token Cluster#bearer_token}
        :param exec_provider_config: exec_provider_config block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#exec_provider_config Cluster#exec_provider_config}
        :param password: Password for servers that require Basic authentication. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#password Cluster#password}
        :param tls_client_config: tls_client_config block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#tls_client_config Cluster#tls_client_config}
        :param username: Username for servers that require Basic authentication. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#username Cluster#username}
        '''
        if isinstance(exec_provider_config, dict):
            exec_provider_config = ClusterConfigExecProviderConfig(**exec_provider_config)
        if isinstance(tls_client_config, dict):
            tls_client_config = ClusterConfigTlsClientConfig(**tls_client_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a5d269c60b9b05d98d508f90d124585cbe5e70615d3ff3472bb28e67b26f40e)
            check_type(argname="argument aws_auth_config", value=aws_auth_config, expected_type=type_hints["aws_auth_config"])
            check_type(argname="argument bearer_token", value=bearer_token, expected_type=type_hints["bearer_token"])
            check_type(argname="argument exec_provider_config", value=exec_provider_config, expected_type=type_hints["exec_provider_config"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument tls_client_config", value=tls_client_config, expected_type=type_hints["tls_client_config"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if aws_auth_config is not None:
            self._values["aws_auth_config"] = aws_auth_config
        if bearer_token is not None:
            self._values["bearer_token"] = bearer_token
        if exec_provider_config is not None:
            self._values["exec_provider_config"] = exec_provider_config
        if password is not None:
            self._values["password"] = password
        if tls_client_config is not None:
            self._values["tls_client_config"] = tls_client_config
        if username is not None:
            self._values["username"] = username

    @builtins.property
    def aws_auth_config(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ClusterConfigAwsAuthConfig"]]]:
        '''aws_auth_config block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#aws_auth_config Cluster#aws_auth_config}
        '''
        result = self._values.get("aws_auth_config")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ClusterConfigAwsAuthConfig"]]], result)

    @builtins.property
    def bearer_token(self) -> typing.Optional[builtins.str]:
        '''Server requires Bearer authentication. The client will not attempt to use refresh tokens for an OAuth2 flow.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#bearer_token Cluster#bearer_token}
        '''
        result = self._values.get("bearer_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def exec_provider_config(
        self,
    ) -> typing.Optional["ClusterConfigExecProviderConfig"]:
        '''exec_provider_config block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#exec_provider_config Cluster#exec_provider_config}
        '''
        result = self._values.get("exec_provider_config")
        return typing.cast(typing.Optional["ClusterConfigExecProviderConfig"], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''Password for servers that require Basic authentication.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#password Cluster#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tls_client_config(self) -> typing.Optional["ClusterConfigTlsClientConfig"]:
        '''tls_client_config block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#tls_client_config Cluster#tls_client_config}
        '''
        result = self._values.get("tls_client_config")
        return typing.cast(typing.Optional["ClusterConfigTlsClientConfig"], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''Username for servers that require Basic authentication.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#username Cluster#username}
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterConfigA(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ClusterConfigAOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.cluster.ClusterConfigAOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f1608149aac59463ab7cae8cd5e05420ee2b31f16514fde04ac917920dd6512b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAwsAuthConfig")
    def put_aws_auth_config(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ClusterConfigAwsAuthConfig", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6325eb30e2aed37b315cffbb80969a79ed0861e89cdbe2d55447f1bd77f380e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAwsAuthConfig", [value]))

    @jsii.member(jsii_name="putExecProviderConfig")
    def put_exec_provider_config(
        self,
        *,
        api_version: typing.Optional[builtins.str] = None,
        args: typing.Optional[typing.Sequence[builtins.str]] = None,
        command: typing.Optional[builtins.str] = None,
        env: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        install_hint: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param api_version: Preferred input version of the ExecInfo. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#api_version Cluster#api_version}
        :param args: Arguments to pass to the command when executing it. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#args Cluster#args}
        :param command: Command to execute. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#command Cluster#command}
        :param env: Env defines additional environment variables to expose to the process. Passed as a map of strings. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#env Cluster#env}
        :param install_hint: This text is shown to the user when the executable doesn't seem to be present. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#install_hint Cluster#install_hint}
        '''
        value = ClusterConfigExecProviderConfig(
            api_version=api_version,
            args=args,
            command=command,
            env=env,
            install_hint=install_hint,
        )

        return typing.cast(None, jsii.invoke(self, "putExecProviderConfig", [value]))

    @jsii.member(jsii_name="putTlsClientConfig")
    def put_tls_client_config(
        self,
        *,
        ca_data: typing.Optional[builtins.str] = None,
        cert_data: typing.Optional[builtins.str] = None,
        insecure: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        key_data: typing.Optional[builtins.str] = None,
        server_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param ca_data: PEM-encoded bytes (typically read from a root certificates bundle). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#ca_data Cluster#ca_data}
        :param cert_data: PEM-encoded bytes (typically read from a client certificate file). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#cert_data Cluster#cert_data}
        :param insecure: Whether server should be accessed without verifying the TLS certificate. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#insecure Cluster#insecure}
        :param key_data: PEM-encoded bytes (typically read from a client certificate key file). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#key_data Cluster#key_data}
        :param server_name: Name to pass to the server for SNI and used in the client to check server certificates against. If empty, the hostname used to contact the server is used. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#server_name Cluster#server_name}
        '''
        value = ClusterConfigTlsClientConfig(
            ca_data=ca_data,
            cert_data=cert_data,
            insecure=insecure,
            key_data=key_data,
            server_name=server_name,
        )

        return typing.cast(None, jsii.invoke(self, "putTlsClientConfig", [value]))

    @jsii.member(jsii_name="resetAwsAuthConfig")
    def reset_aws_auth_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsAuthConfig", []))

    @jsii.member(jsii_name="resetBearerToken")
    def reset_bearer_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBearerToken", []))

    @jsii.member(jsii_name="resetExecProviderConfig")
    def reset_exec_provider_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExecProviderConfig", []))

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetTlsClientConfig")
    def reset_tls_client_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTlsClientConfig", []))

    @jsii.member(jsii_name="resetUsername")
    def reset_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsername", []))

    @builtins.property
    @jsii.member(jsii_name="awsAuthConfig")
    def aws_auth_config(self) -> "ClusterConfigAwsAuthConfigList":
        return typing.cast("ClusterConfigAwsAuthConfigList", jsii.get(self, "awsAuthConfig"))

    @builtins.property
    @jsii.member(jsii_name="execProviderConfig")
    def exec_provider_config(self) -> "ClusterConfigExecProviderConfigOutputReference":
        return typing.cast("ClusterConfigExecProviderConfigOutputReference", jsii.get(self, "execProviderConfig"))

    @builtins.property
    @jsii.member(jsii_name="tlsClientConfig")
    def tls_client_config(self) -> "ClusterConfigTlsClientConfigOutputReference":
        return typing.cast("ClusterConfigTlsClientConfigOutputReference", jsii.get(self, "tlsClientConfig"))

    @builtins.property
    @jsii.member(jsii_name="awsAuthConfigInput")
    def aws_auth_config_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ClusterConfigAwsAuthConfig"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ClusterConfigAwsAuthConfig"]]], jsii.get(self, "awsAuthConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="bearerTokenInput")
    def bearer_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bearerTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="execProviderConfigInput")
    def exec_provider_config_input(
        self,
    ) -> typing.Optional["ClusterConfigExecProviderConfig"]:
        return typing.cast(typing.Optional["ClusterConfigExecProviderConfig"], jsii.get(self, "execProviderConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsClientConfigInput")
    def tls_client_config_input(
        self,
    ) -> typing.Optional["ClusterConfigTlsClientConfig"]:
        return typing.cast(typing.Optional["ClusterConfigTlsClientConfig"], jsii.get(self, "tlsClientConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="bearerToken")
    def bearer_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bearerToken"))

    @bearer_token.setter
    def bearer_token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74d39086f4463f5fc08f92a9ab534f05283c7792b701b368cd4d8ee5f9a74a1d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bearerToken", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb8ebe49e654e75ba4e397b8ae9c56547ea5734196ad39b4576e9fe0d9ef2c54)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d087a95e38c7611d49f84afe7f21e2850267c79ea5e1a4064d01cf5410df67a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ClusterConfigA]:
        return typing.cast(typing.Optional[ClusterConfigA], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ClusterConfigA]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab3ef0d52861137e9f3b9a1bc841445d174ae1b10c2c6622821e7251a89494e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="argocd.cluster.ClusterConfigAwsAuthConfig",
    jsii_struct_bases=[],
    name_mapping={"cluster_name": "clusterName", "role_arn": "roleArn"},
)
class ClusterConfigAwsAuthConfig:
    def __init__(
        self,
        *,
        cluster_name: typing.Optional[builtins.str] = None,
        role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cluster_name: AWS cluster name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#cluster_name Cluster#cluster_name}
        :param role_arn: IAM role ARN. If set then AWS IAM Authenticator assume a role to perform cluster operations instead of the default AWS credential provider chain. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#role_arn Cluster#role_arn}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__713cf43653054471c8e66b9391788a03b0f598aed33b3530541beb576c0af4a1)
            check_type(argname="argument cluster_name", value=cluster_name, expected_type=type_hints["cluster_name"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cluster_name is not None:
            self._values["cluster_name"] = cluster_name
        if role_arn is not None:
            self._values["role_arn"] = role_arn

    @builtins.property
    def cluster_name(self) -> typing.Optional[builtins.str]:
        '''AWS cluster name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#cluster_name Cluster#cluster_name}
        '''
        result = self._values.get("cluster_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''IAM role ARN.

        If set then AWS IAM Authenticator assume a role to perform cluster operations instead of the default AWS credential provider chain.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#role_arn Cluster#role_arn}
        '''
        result = self._values.get("role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterConfigAwsAuthConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ClusterConfigAwsAuthConfigList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.cluster.ClusterConfigAwsAuthConfigList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b854df2b206d96afecec5a2ed2b35380a9803d37a27e7a74d15b4ab5aeb51bd5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ClusterConfigAwsAuthConfigOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3f1a01f76074a87302ba6c7981f27cb19a2fef904ffc038be0899849f54f6a4)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ClusterConfigAwsAuthConfigOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a7248e0c7cd7e1f87a654ea67d6c49673564a7ffdeca93bd15e52d4a1ebccb7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0270d370731e6c4d0f8ffa836e92f8666bcb29f157793f35f5792455c871e969)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a656c58f14f94f06b70e94cc950636b6fef6d8103191b5643f3c0f013c8dc44e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ClusterConfigAwsAuthConfig]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ClusterConfigAwsAuthConfig]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ClusterConfigAwsAuthConfig]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95caf117a3a081c49e985fb4b70469523c419fac65b17c87f5869f0cd2cb5e27)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ClusterConfigAwsAuthConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.cluster.ClusterConfigAwsAuthConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b0c536e08c87fd836e6aa570012e2e4cfd8c6187ef047c50578db9fa89057e37)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetClusterName")
    def reset_cluster_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterName", []))

    @jsii.member(jsii_name="resetRoleArn")
    def reset_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRoleArn", []))

    @builtins.property
    @jsii.member(jsii_name="clusterNameInput")
    def cluster_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterNameInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterName")
    def cluster_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterName"))

    @cluster_name.setter
    def cluster_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad209a53319ceb78f8881f00068ae81fab2831c4619956d6bb0c585f15965ce5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterName", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49e255c01bae36c47431198c00c2c8f6ef0d9d3e4845829a126cd1466a38adde)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ClusterConfigAwsAuthConfig]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ClusterConfigAwsAuthConfig]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ClusterConfigAwsAuthConfig]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f989f48a03d680e36a62ce1dfb61862e772afa4bda167e7f91de04d8a946564c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="argocd.cluster.ClusterConfigExecProviderConfig",
    jsii_struct_bases=[],
    name_mapping={
        "api_version": "apiVersion",
        "args": "args",
        "command": "command",
        "env": "env",
        "install_hint": "installHint",
    },
)
class ClusterConfigExecProviderConfig:
    def __init__(
        self,
        *,
        api_version: typing.Optional[builtins.str] = None,
        args: typing.Optional[typing.Sequence[builtins.str]] = None,
        command: typing.Optional[builtins.str] = None,
        env: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        install_hint: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param api_version: Preferred input version of the ExecInfo. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#api_version Cluster#api_version}
        :param args: Arguments to pass to the command when executing it. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#args Cluster#args}
        :param command: Command to execute. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#command Cluster#command}
        :param env: Env defines additional environment variables to expose to the process. Passed as a map of strings. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#env Cluster#env}
        :param install_hint: This text is shown to the user when the executable doesn't seem to be present. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#install_hint Cluster#install_hint}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7263bcebabc3fd1f572ece816c6c522d02cb274b4acade00ff1758b20e3ed21)
            check_type(argname="argument api_version", value=api_version, expected_type=type_hints["api_version"])
            check_type(argname="argument args", value=args, expected_type=type_hints["args"])
            check_type(argname="argument command", value=command, expected_type=type_hints["command"])
            check_type(argname="argument env", value=env, expected_type=type_hints["env"])
            check_type(argname="argument install_hint", value=install_hint, expected_type=type_hints["install_hint"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if api_version is not None:
            self._values["api_version"] = api_version
        if args is not None:
            self._values["args"] = args
        if command is not None:
            self._values["command"] = command
        if env is not None:
            self._values["env"] = env
        if install_hint is not None:
            self._values["install_hint"] = install_hint

    @builtins.property
    def api_version(self) -> typing.Optional[builtins.str]:
        '''Preferred input version of the ExecInfo.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#api_version Cluster#api_version}
        '''
        result = self._values.get("api_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def args(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Arguments to pass to the command when executing it.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#args Cluster#args}
        '''
        result = self._values.get("args")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def command(self) -> typing.Optional[builtins.str]:
        '''Command to execute.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#command Cluster#command}
        '''
        result = self._values.get("command")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def env(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Env defines additional environment variables to expose to the process. Passed as a map of strings.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#env Cluster#env}
        '''
        result = self._values.get("env")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def install_hint(self) -> typing.Optional[builtins.str]:
        '''This text is shown to the user when the executable doesn't seem to be present.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#install_hint Cluster#install_hint}
        '''
        result = self._values.get("install_hint")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterConfigExecProviderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ClusterConfigExecProviderConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.cluster.ClusterConfigExecProviderConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c26bba3770ce047dcb5682316d04f2e6d422bae9eedd70413ad210710a94a702)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetApiVersion")
    def reset_api_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApiVersion", []))

    @jsii.member(jsii_name="resetArgs")
    def reset_args(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArgs", []))

    @jsii.member(jsii_name="resetCommand")
    def reset_command(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCommand", []))

    @jsii.member(jsii_name="resetEnv")
    def reset_env(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnv", []))

    @jsii.member(jsii_name="resetInstallHint")
    def reset_install_hint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstallHint", []))

    @builtins.property
    @jsii.member(jsii_name="apiVersionInput")
    def api_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="argsInput")
    def args_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "argsInput"))

    @builtins.property
    @jsii.member(jsii_name="commandInput")
    def command_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commandInput"))

    @builtins.property
    @jsii.member(jsii_name="envInput")
    def env_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "envInput"))

    @builtins.property
    @jsii.member(jsii_name="installHintInput")
    def install_hint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "installHintInput"))

    @builtins.property
    @jsii.member(jsii_name="apiVersion")
    def api_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiVersion"))

    @api_version.setter
    def api_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46e405e80cc980376493e1f26b9519e3110dc094fea1400a2fdfa77d46546964)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiVersion", value)

    @builtins.property
    @jsii.member(jsii_name="args")
    def args(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "args"))

    @args.setter
    def args(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aed1d5416086faac0e76fd0e44e7edf20605cd6aeaf072db2ddcc5bdd9499bda)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "args", value)

    @builtins.property
    @jsii.member(jsii_name="command")
    def command(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "command"))

    @command.setter
    def command(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__572b093243f4a804083f2ba49066aa28879319ed7599bbdabe7b6511971e0509)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "command", value)

    @builtins.property
    @jsii.member(jsii_name="env")
    def env(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "env"))

    @env.setter
    def env(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f987d91797b17b7e11a9542a10c8afaaf5f27c4128e48dc39907137cda9ddd17)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "env", value)

    @builtins.property
    @jsii.member(jsii_name="installHint")
    def install_hint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "installHint"))

    @install_hint.setter
    def install_hint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ded23b474131ae2ffe4ae7ea0f810f7929f6c93512b2e892540cb0c9ffdb4c9d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "installHint", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ClusterConfigExecProviderConfig]:
        return typing.cast(typing.Optional[ClusterConfigExecProviderConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ClusterConfigExecProviderConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba47d92c4869aff4795ae8288341f4177ab54c40ccb8d85d94b1b3d4ed94a2a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="argocd.cluster.ClusterConfigTlsClientConfig",
    jsii_struct_bases=[],
    name_mapping={
        "ca_data": "caData",
        "cert_data": "certData",
        "insecure": "insecure",
        "key_data": "keyData",
        "server_name": "serverName",
    },
)
class ClusterConfigTlsClientConfig:
    def __init__(
        self,
        *,
        ca_data: typing.Optional[builtins.str] = None,
        cert_data: typing.Optional[builtins.str] = None,
        insecure: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        key_data: typing.Optional[builtins.str] = None,
        server_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param ca_data: PEM-encoded bytes (typically read from a root certificates bundle). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#ca_data Cluster#ca_data}
        :param cert_data: PEM-encoded bytes (typically read from a client certificate file). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#cert_data Cluster#cert_data}
        :param insecure: Whether server should be accessed without verifying the TLS certificate. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#insecure Cluster#insecure}
        :param key_data: PEM-encoded bytes (typically read from a client certificate key file). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#key_data Cluster#key_data}
        :param server_name: Name to pass to the server for SNI and used in the client to check server certificates against. If empty, the hostname used to contact the server is used. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#server_name Cluster#server_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d58f7043819c3e39d56d8c0aedd26604f386086283d01664b3e293558a8f95a4)
            check_type(argname="argument ca_data", value=ca_data, expected_type=type_hints["ca_data"])
            check_type(argname="argument cert_data", value=cert_data, expected_type=type_hints["cert_data"])
            check_type(argname="argument insecure", value=insecure, expected_type=type_hints["insecure"])
            check_type(argname="argument key_data", value=key_data, expected_type=type_hints["key_data"])
            check_type(argname="argument server_name", value=server_name, expected_type=type_hints["server_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if ca_data is not None:
            self._values["ca_data"] = ca_data
        if cert_data is not None:
            self._values["cert_data"] = cert_data
        if insecure is not None:
            self._values["insecure"] = insecure
        if key_data is not None:
            self._values["key_data"] = key_data
        if server_name is not None:
            self._values["server_name"] = server_name

    @builtins.property
    def ca_data(self) -> typing.Optional[builtins.str]:
        '''PEM-encoded bytes (typically read from a root certificates bundle).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#ca_data Cluster#ca_data}
        '''
        result = self._values.get("ca_data")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cert_data(self) -> typing.Optional[builtins.str]:
        '''PEM-encoded bytes (typically read from a client certificate file).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#cert_data Cluster#cert_data}
        '''
        result = self._values.get("cert_data")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def insecure(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether server should be accessed without verifying the TLS certificate.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#insecure Cluster#insecure}
        '''
        result = self._values.get("insecure")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def key_data(self) -> typing.Optional[builtins.str]:
        '''PEM-encoded bytes (typically read from a client certificate key file).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#key_data Cluster#key_data}
        '''
        result = self._values.get("key_data")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def server_name(self) -> typing.Optional[builtins.str]:
        '''Name to pass to the server for SNI and used in the client to check server certificates against.

        If empty, the hostname used to contact the server is used.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#server_name Cluster#server_name}
        '''
        result = self._values.get("server_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterConfigTlsClientConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ClusterConfigTlsClientConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.cluster.ClusterConfigTlsClientConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8942cac46668048634eab8a8050d20180110d0e49fbbf299d92234e7d4baeb01)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCaData")
    def reset_ca_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCaData", []))

    @jsii.member(jsii_name="resetCertData")
    def reset_cert_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertData", []))

    @jsii.member(jsii_name="resetInsecure")
    def reset_insecure(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInsecure", []))

    @jsii.member(jsii_name="resetKeyData")
    def reset_key_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyData", []))

    @jsii.member(jsii_name="resetServerName")
    def reset_server_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServerName", []))

    @builtins.property
    @jsii.member(jsii_name="caDataInput")
    def ca_data_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "caDataInput"))

    @builtins.property
    @jsii.member(jsii_name="certDataInput")
    def cert_data_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certDataInput"))

    @builtins.property
    @jsii.member(jsii_name="insecureInput")
    def insecure_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "insecureInput"))

    @builtins.property
    @jsii.member(jsii_name="keyDataInput")
    def key_data_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyDataInput"))

    @builtins.property
    @jsii.member(jsii_name="serverNameInput")
    def server_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverNameInput"))

    @builtins.property
    @jsii.member(jsii_name="caData")
    def ca_data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "caData"))

    @ca_data.setter
    def ca_data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3fdd39be3dd77edf7d5d7f3020d407efd406ff4cdc3a727e0b17f3a13da5515f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caData", value)

    @builtins.property
    @jsii.member(jsii_name="certData")
    def cert_data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certData"))

    @cert_data.setter
    def cert_data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__977eb3c83332557815dc4c7709ce7a2cf7d7541e6acb9024881969b40469e155)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certData", value)

    @builtins.property
    @jsii.member(jsii_name="insecure")
    def insecure(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "insecure"))

    @insecure.setter
    def insecure(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca5ac15424c8a4a4d09272a72f55d898d63e456a31aab7f65b2db945ba505949)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "insecure", value)

    @builtins.property
    @jsii.member(jsii_name="keyData")
    def key_data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyData"))

    @key_data.setter
    def key_data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c27d0c564b7afe48b48c5305efd7eaec054642025ff6cdbd2d59db9e25340e46)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyData", value)

    @builtins.property
    @jsii.member(jsii_name="serverName")
    def server_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serverName"))

    @server_name.setter
    def server_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36acae56ae6a214b3fd23c059488db771aedc9e1d198d938b95b0e75e29ad267)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ClusterConfigTlsClientConfig]:
        return typing.cast(typing.Optional[ClusterConfigTlsClientConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ClusterConfigTlsClientConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a61d32c8c5b3aa23d6211f61a6d219ef542b14137746e39cc1e27a5b4ba155de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="argocd.cluster.ClusterInfo",
    jsii_struct_bases=[],
    name_mapping={},
)
class ClusterInfo:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterInfo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="argocd.cluster.ClusterInfoConnectionState",
    jsii_struct_bases=[],
    name_mapping={},
)
class ClusterInfoConnectionState:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterInfoConnectionState(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ClusterInfoConnectionStateList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.cluster.ClusterInfoConnectionStateList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4ca23ac854b3dc9f6edbb4e5834af8abab9a125691ec5bdb46135b276a0c6109)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ClusterInfoConnectionStateOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7a0dcb038e1d781be0ec80eb7fda0b0b7dd813292643497cedca6665dbb5a32)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ClusterInfoConnectionStateOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70a3815432f756785e80c988645c35365ae528e6e705d1e298f52d7a7dc2d166)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5a5b1766a826b9bd6a4051603c6ea14192b7c226b6e518996e3923ca0835b0b0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6fe41b0dca3832bd0c30a6dc45b9db1bb091a02e3693c68ac4f7bb2a06e4b3a3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class ClusterInfoConnectionStateOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.cluster.ClusterInfoConnectionStateOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__750c944145dfd846436cb2dde1343fad2674a0820afc05c1a58df82ad6dc5ae7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

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
    def internal_value(self) -> typing.Optional[ClusterInfoConnectionState]:
        return typing.cast(typing.Optional[ClusterInfoConnectionState], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ClusterInfoConnectionState],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3aa04344c8e4319bd12fa079139cb48037f43f3a8b0041baa229b28655110930)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ClusterInfoList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.cluster.ClusterInfoList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f93f962126588410bf906b73345088bbb51f385e815f209fb3084bfab011c67a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ClusterInfoOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__301ca62e5488da7088bb1a54125f607719342eda6d33dbb10e6ccd30c491f33d)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ClusterInfoOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__294904844c69c8423381cf7cb60d9ca4a046454c7881aaa03510be63d990ccc9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1e181920571fa5d1d9962823faf877948a28bd979b7df2f048be8d10d69e5fd1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6f7ccdc978abd1db8f10a5b0a13bbf6bfa58cbb0b39ed18c0c70af89d4a33248)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class ClusterInfoOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.cluster.ClusterInfoOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1396de9c3372a582ed03e9b216247027be6b42d309e363abbba6a0ab08563dec)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="applicationsCount")
    def applications_count(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "applicationsCount"))

    @builtins.property
    @jsii.member(jsii_name="connectionState")
    def connection_state(self) -> ClusterInfoConnectionStateList:
        return typing.cast(ClusterInfoConnectionStateList, jsii.get(self, "connectionState"))

    @builtins.property
    @jsii.member(jsii_name="serverVersion")
    def server_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serverVersion"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ClusterInfo]:
        return typing.cast(typing.Optional[ClusterInfo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ClusterInfo]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c47ac81d756bf49d5c51e4478ad1f0f7150b2414dfe4ae7e2da61c5e168c728)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="argocd.cluster.ClusterMetadata",
    jsii_struct_bases=[],
    name_mapping={"annotations": "annotations", "labels": "labels"},
)
class ClusterMetadata:
    def __init__(
        self,
        *,
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param annotations: An unstructured key value map stored with the cluster secret that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#annotations Cluster#annotations}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the cluster secret. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#labels Cluster#labels}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__588e0ba4558110fc2af6365d178cac40670ad434a19b6d66469a86929d933b3c)
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if annotations is not None:
            self._values["annotations"] = annotations
        if labels is not None:
            self._values["labels"] = labels

    @builtins.property
    def annotations(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''An unstructured key value map stored with the cluster secret that may be used to store arbitrary metadata.

        More info: http://kubernetes.io/docs/user-guide/annotations

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#annotations Cluster#annotations}
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Map of string keys and values that can be used to organize and categorize (scope and select) the cluster secret.

        May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/cluster#labels Cluster#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterMetadata(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ClusterMetadataList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.cluster.ClusterMetadataList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5f4e2b2e7a0ca53b96b421628222ebeb9a4c0f20b26351bd7cfd463f60b60fae)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ClusterMetadataOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41313b345f7a0986f7765cb01214fbf1407dd56d1d01993850b5cf21b96672e5)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ClusterMetadataOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85620c9c4ce7950d00c555d53cab9f41b34ae16c101c0da106ba9683be66ad45)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f48626f83d4e8a9c1d99270a4ffa54f165c05f475eb11ceca86568c1ae3354ff)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2218a17af62f9de7d67dd4812c5cf47b11caa84815c6a815ffa288489184bf85)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ClusterMetadata]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ClusterMetadata]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ClusterMetadata]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__863021100034bc59143e8cc0036cd24e194c49a0844e297584e78df2d0be154c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ClusterMetadataOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.cluster.ClusterMetadataOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__75814839e07b269e1a0f3bd1bb416aed0478333f8bdee15f657a6d91597286bf)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAnnotations")
    def reset_annotations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnnotations", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

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
    @jsii.member(jsii_name="annotations")
    def annotations(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "annotations"))

    @annotations.setter
    def annotations(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3516e6817431ce47c9aff8c821554cc113b9d122b754b5792a6622ff7907952)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "annotations", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fed4a3ab26bab7cd03b5ef0f77bd8556016fafba2cd34393488eeaffc67939d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ClusterMetadata]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ClusterMetadata]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ClusterMetadata]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17a8e40d63d0dff7dbbec12b491b9e57ccfdfb3d661602fc513438c4b7a6a782)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Cluster",
    "ClusterConfig",
    "ClusterConfigA",
    "ClusterConfigAOutputReference",
    "ClusterConfigAwsAuthConfig",
    "ClusterConfigAwsAuthConfigList",
    "ClusterConfigAwsAuthConfigOutputReference",
    "ClusterConfigExecProviderConfig",
    "ClusterConfigExecProviderConfigOutputReference",
    "ClusterConfigTlsClientConfig",
    "ClusterConfigTlsClientConfigOutputReference",
    "ClusterInfo",
    "ClusterInfoConnectionState",
    "ClusterInfoConnectionStateList",
    "ClusterInfoConnectionStateOutputReference",
    "ClusterInfoList",
    "ClusterInfoOutputReference",
    "ClusterMetadata",
    "ClusterMetadataList",
    "ClusterMetadataOutputReference",
]

publication.publish()

def _typecheckingstub__b74ed58f16a119a0d0ed009671e35fdf6f16637eb3f70e2ea966e7cd29745e04(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    config: typing.Union[ClusterConfigA, typing.Dict[builtins.str, typing.Any]],
    id: typing.Optional[builtins.str] = None,
    metadata: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ClusterMetadata, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: typing.Optional[builtins.str] = None,
    namespaces: typing.Optional[typing.Sequence[builtins.str]] = None,
    project: typing.Optional[builtins.str] = None,
    server: typing.Optional[builtins.str] = None,
    shard: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__6b93237249ce4340de04ca4b9d6b448dea5e8647cc70144fc186e12c0295485c(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4165cea0fb95ae8bf68cc5706f518f1efb249ca4a63fef5958f17fd24e0e8c8(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ClusterMetadata, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a61f61e9752a2326164142d2ebc01f9e9fecb2d74af22e9131defefcbf19ea33(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc98af5cdf14c08b1fb3339f748f030f11c63376f69a8e709c987685dc0c4deb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b031f05d00937342a563c12337ecb1e6ab4c9e6de838648389b38f55182a72df(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3cc273bc212f0456ea34720255d4dc0aa7474e3e67907b0a5c7e0fad568eb1fc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22cad3e145e520db51524e18c7836cee14faeeeeac0ba505dc4e1654e5044f39(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc63fe3dffbf3ede7259d394d2d6cfb4f57228bc1395fc4ca1a828574f559754(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b7198b9273ab923c023f395b7f3004e7b062f65c92932d8f4482f6167ef446f(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    config: typing.Union[ClusterConfigA, typing.Dict[builtins.str, typing.Any]],
    id: typing.Optional[builtins.str] = None,
    metadata: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ClusterMetadata, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: typing.Optional[builtins.str] = None,
    namespaces: typing.Optional[typing.Sequence[builtins.str]] = None,
    project: typing.Optional[builtins.str] = None,
    server: typing.Optional[builtins.str] = None,
    shard: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a5d269c60b9b05d98d508f90d124585cbe5e70615d3ff3472bb28e67b26f40e(
    *,
    aws_auth_config: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ClusterConfigAwsAuthConfig, typing.Dict[builtins.str, typing.Any]]]]] = None,
    bearer_token: typing.Optional[builtins.str] = None,
    exec_provider_config: typing.Optional[typing.Union[ClusterConfigExecProviderConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    password: typing.Optional[builtins.str] = None,
    tls_client_config: typing.Optional[typing.Union[ClusterConfigTlsClientConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1608149aac59463ab7cae8cd5e05420ee2b31f16514fde04ac917920dd6512b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6325eb30e2aed37b315cffbb80969a79ed0861e89cdbe2d55447f1bd77f380e9(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ClusterConfigAwsAuthConfig, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74d39086f4463f5fc08f92a9ab534f05283c7792b701b368cd4d8ee5f9a74a1d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb8ebe49e654e75ba4e397b8ae9c56547ea5734196ad39b4576e9fe0d9ef2c54(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d087a95e38c7611d49f84afe7f21e2850267c79ea5e1a4064d01cf5410df67a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab3ef0d52861137e9f3b9a1bc841445d174ae1b10c2c6622821e7251a89494e0(
    value: typing.Optional[ClusterConfigA],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__713cf43653054471c8e66b9391788a03b0f598aed33b3530541beb576c0af4a1(
    *,
    cluster_name: typing.Optional[builtins.str] = None,
    role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b854df2b206d96afecec5a2ed2b35380a9803d37a27e7a74d15b4ab5aeb51bd5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3f1a01f76074a87302ba6c7981f27cb19a2fef904ffc038be0899849f54f6a4(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a7248e0c7cd7e1f87a654ea67d6c49673564a7ffdeca93bd15e52d4a1ebccb7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0270d370731e6c4d0f8ffa836e92f8666bcb29f157793f35f5792455c871e969(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a656c58f14f94f06b70e94cc950636b6fef6d8103191b5643f3c0f013c8dc44e(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95caf117a3a081c49e985fb4b70469523c419fac65b17c87f5869f0cd2cb5e27(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ClusterConfigAwsAuthConfig]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0c536e08c87fd836e6aa570012e2e4cfd8c6187ef047c50578db9fa89057e37(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad209a53319ceb78f8881f00068ae81fab2831c4619956d6bb0c585f15965ce5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49e255c01bae36c47431198c00c2c8f6ef0d9d3e4845829a126cd1466a38adde(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f989f48a03d680e36a62ce1dfb61862e772afa4bda167e7f91de04d8a946564c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ClusterConfigAwsAuthConfig]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7263bcebabc3fd1f572ece816c6c522d02cb274b4acade00ff1758b20e3ed21(
    *,
    api_version: typing.Optional[builtins.str] = None,
    args: typing.Optional[typing.Sequence[builtins.str]] = None,
    command: typing.Optional[builtins.str] = None,
    env: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    install_hint: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c26bba3770ce047dcb5682316d04f2e6d422bae9eedd70413ad210710a94a702(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46e405e80cc980376493e1f26b9519e3110dc094fea1400a2fdfa77d46546964(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aed1d5416086faac0e76fd0e44e7edf20605cd6aeaf072db2ddcc5bdd9499bda(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__572b093243f4a804083f2ba49066aa28879319ed7599bbdabe7b6511971e0509(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f987d91797b17b7e11a9542a10c8afaaf5f27c4128e48dc39907137cda9ddd17(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ded23b474131ae2ffe4ae7ea0f810f7929f6c93512b2e892540cb0c9ffdb4c9d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba47d92c4869aff4795ae8288341f4177ab54c40ccb8d85d94b1b3d4ed94a2a8(
    value: typing.Optional[ClusterConfigExecProviderConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d58f7043819c3e39d56d8c0aedd26604f386086283d01664b3e293558a8f95a4(
    *,
    ca_data: typing.Optional[builtins.str] = None,
    cert_data: typing.Optional[builtins.str] = None,
    insecure: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    key_data: typing.Optional[builtins.str] = None,
    server_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8942cac46668048634eab8a8050d20180110d0e49fbbf299d92234e7d4baeb01(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3fdd39be3dd77edf7d5d7f3020d407efd406ff4cdc3a727e0b17f3a13da5515f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__977eb3c83332557815dc4c7709ce7a2cf7d7541e6acb9024881969b40469e155(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca5ac15424c8a4a4d09272a72f55d898d63e456a31aab7f65b2db945ba505949(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c27d0c564b7afe48b48c5305efd7eaec054642025ff6cdbd2d59db9e25340e46(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36acae56ae6a214b3fd23c059488db771aedc9e1d198d938b95b0e75e29ad267(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a61d32c8c5b3aa23d6211f61a6d219ef542b14137746e39cc1e27a5b4ba155de(
    value: typing.Optional[ClusterConfigTlsClientConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ca23ac854b3dc9f6edbb4e5834af8abab9a125691ec5bdb46135b276a0c6109(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7a0dcb038e1d781be0ec80eb7fda0b0b7dd813292643497cedca6665dbb5a32(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70a3815432f756785e80c988645c35365ae528e6e705d1e298f52d7a7dc2d166(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a5b1766a826b9bd6a4051603c6ea14192b7c226b6e518996e3923ca0835b0b0(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fe41b0dca3832bd0c30a6dc45b9db1bb091a02e3693c68ac4f7bb2a06e4b3a3(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__750c944145dfd846436cb2dde1343fad2674a0820afc05c1a58df82ad6dc5ae7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3aa04344c8e4319bd12fa079139cb48037f43f3a8b0041baa229b28655110930(
    value: typing.Optional[ClusterInfoConnectionState],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f93f962126588410bf906b73345088bbb51f385e815f209fb3084bfab011c67a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__301ca62e5488da7088bb1a54125f607719342eda6d33dbb10e6ccd30c491f33d(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__294904844c69c8423381cf7cb60d9ca4a046454c7881aaa03510be63d990ccc9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e181920571fa5d1d9962823faf877948a28bd979b7df2f048be8d10d69e5fd1(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f7ccdc978abd1db8f10a5b0a13bbf6bfa58cbb0b39ed18c0c70af89d4a33248(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1396de9c3372a582ed03e9b216247027be6b42d309e363abbba6a0ab08563dec(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c47ac81d756bf49d5c51e4478ad1f0f7150b2414dfe4ae7e2da61c5e168c728(
    value: typing.Optional[ClusterInfo],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__588e0ba4558110fc2af6365d178cac40670ad434a19b6d66469a86929d933b3c(
    *,
    annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f4e2b2e7a0ca53b96b421628222ebeb9a4c0f20b26351bd7cfd463f60b60fae(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41313b345f7a0986f7765cb01214fbf1407dd56d1d01993850b5cf21b96672e5(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85620c9c4ce7950d00c555d53cab9f41b34ae16c101c0da106ba9683be66ad45(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f48626f83d4e8a9c1d99270a4ffa54f165c05f475eb11ceca86568c1ae3354ff(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2218a17af62f9de7d67dd4812c5cf47b11caa84815c6a815ffa288489184bf85(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__863021100034bc59143e8cc0036cd24e194c49a0844e297584e78df2d0be154c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ClusterMetadata]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75814839e07b269e1a0f3bd1bb416aed0478333f8bdee15f657a6d91597286bf(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3516e6817431ce47c9aff8c821554cc113b9d122b754b5792a6622ff7907952(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fed4a3ab26bab7cd03b5ef0f77bd8556016fafba2cd34393488eeaffc67939d1(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17a8e40d63d0dff7dbbec12b491b9e57ccfdfb3d661602fc513438c4b7a6a782(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ClusterMetadata]],
) -> None:
    """Type checking stubs"""
    pass
