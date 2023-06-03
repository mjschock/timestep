'''
# `digitalocean_kubernetes_cluster`

Refer to the Terraform Registory for docs: [`digitalocean_kubernetes_cluster`](https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster).
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


class KubernetesCluster(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.kubernetesCluster.KubernetesCluster",
):
    '''Represents a {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster digitalocean_kubernetes_cluster}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        node_pool: typing.Union["KubernetesClusterNodePool", typing.Dict[builtins.str, typing.Any]],
        region: builtins.str,
        version: builtins.str,
        auto_upgrade: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        ha: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        maintenance_policy: typing.Optional[typing.Union["KubernetesClusterMaintenancePolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        registry_integration: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        surge_upgrade: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["KubernetesClusterTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        vpc_uuid: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster digitalocean_kubernetes_cluster} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#name KubernetesCluster#name}.
        :param node_pool: node_pool block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#node_pool KubernetesCluster#node_pool}
        :param region: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#region KubernetesCluster#region}.
        :param version: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#version KubernetesCluster#version}.
        :param auto_upgrade: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#auto_upgrade KubernetesCluster#auto_upgrade}.
        :param ha: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#ha KubernetesCluster#ha}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#id KubernetesCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param maintenance_policy: maintenance_policy block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#maintenance_policy KubernetesCluster#maintenance_policy}
        :param registry_integration: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#registry_integration KubernetesCluster#registry_integration}.
        :param surge_upgrade: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#surge_upgrade KubernetesCluster#surge_upgrade}.
        :param tags: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#tags KubernetesCluster#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#timeouts KubernetesCluster#timeouts}
        :param vpc_uuid: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#vpc_uuid KubernetesCluster#vpc_uuid}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9214e633254b00f1797cbedabc09c9c19ed1c4a8a6d27c64a8d89a3ab878ef15)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = KubernetesClusterConfig(
            name=name,
            node_pool=node_pool,
            region=region,
            version=version,
            auto_upgrade=auto_upgrade,
            ha=ha,
            id=id,
            maintenance_policy=maintenance_policy,
            registry_integration=registry_integration,
            surge_upgrade=surge_upgrade,
            tags=tags,
            timeouts=timeouts,
            vpc_uuid=vpc_uuid,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putMaintenancePolicy")
    def put_maintenance_policy(
        self,
        *,
        day: typing.Optional[builtins.str] = None,
        start_time: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param day: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#day KubernetesCluster#day}.
        :param start_time: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#start_time KubernetesCluster#start_time}.
        '''
        value = KubernetesClusterMaintenancePolicy(day=day, start_time=start_time)

        return typing.cast(None, jsii.invoke(self, "putMaintenancePolicy", [value]))

    @jsii.member(jsii_name="putNodePool")
    def put_node_pool(
        self,
        *,
        name: builtins.str,
        size: builtins.str,
        auto_scale: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        max_nodes: typing.Optional[jsii.Number] = None,
        min_nodes: typing.Optional[jsii.Number] = None,
        node_count: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        taint: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KubernetesClusterNodePoolTaint", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#name KubernetesCluster#name}.
        :param size: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#size KubernetesCluster#size}.
        :param auto_scale: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#auto_scale KubernetesCluster#auto_scale}.
        :param labels: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#labels KubernetesCluster#labels}.
        :param max_nodes: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#max_nodes KubernetesCluster#max_nodes}.
        :param min_nodes: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#min_nodes KubernetesCluster#min_nodes}.
        :param node_count: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#node_count KubernetesCluster#node_count}.
        :param tags: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#tags KubernetesCluster#tags}.
        :param taint: taint block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#taint KubernetesCluster#taint}
        '''
        value = KubernetesClusterNodePool(
            name=name,
            size=size,
            auto_scale=auto_scale,
            labels=labels,
            max_nodes=max_nodes,
            min_nodes=min_nodes,
            node_count=node_count,
            tags=tags,
            taint=taint,
        )

        return typing.cast(None, jsii.invoke(self, "putNodePool", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(self, *, create: typing.Optional[builtins.str] = None) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#create KubernetesCluster#create}.
        '''
        value = KubernetesClusterTimeouts(create=create)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAutoUpgrade")
    def reset_auto_upgrade(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoUpgrade", []))

    @jsii.member(jsii_name="resetHa")
    def reset_ha(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHa", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMaintenancePolicy")
    def reset_maintenance_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaintenancePolicy", []))

    @jsii.member(jsii_name="resetRegistryIntegration")
    def reset_registry_integration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegistryIntegration", []))

    @jsii.member(jsii_name="resetSurgeUpgrade")
    def reset_surge_upgrade(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSurgeUpgrade", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetVpcUuid")
    def reset_vpc_uuid(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpcUuid", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

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
    @jsii.member(jsii_name="ipv4Address")
    def ipv4_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipv4Address"))

    @builtins.property
    @jsii.member(jsii_name="kubeConfig")
    def kube_config(self) -> "KubernetesClusterKubeConfigList":
        return typing.cast("KubernetesClusterKubeConfigList", jsii.get(self, "kubeConfig"))

    @builtins.property
    @jsii.member(jsii_name="maintenancePolicy")
    def maintenance_policy(self) -> "KubernetesClusterMaintenancePolicyOutputReference":
        return typing.cast("KubernetesClusterMaintenancePolicyOutputReference", jsii.get(self, "maintenancePolicy"))

    @builtins.property
    @jsii.member(jsii_name="nodePool")
    def node_pool(self) -> "KubernetesClusterNodePoolOutputReference":
        return typing.cast("KubernetesClusterNodePoolOutputReference", jsii.get(self, "nodePool"))

    @builtins.property
    @jsii.member(jsii_name="serviceSubnet")
    def service_subnet(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceSubnet"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "KubernetesClusterTimeoutsOutputReference":
        return typing.cast("KubernetesClusterTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="updatedAt")
    def updated_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "updatedAt"))

    @builtins.property
    @jsii.member(jsii_name="urn")
    def urn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "urn"))

    @builtins.property
    @jsii.member(jsii_name="autoUpgradeInput")
    def auto_upgrade_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "autoUpgradeInput"))

    @builtins.property
    @jsii.member(jsii_name="haInput")
    def ha_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "haInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="maintenancePolicyInput")
    def maintenance_policy_input(
        self,
    ) -> typing.Optional["KubernetesClusterMaintenancePolicy"]:
        return typing.cast(typing.Optional["KubernetesClusterMaintenancePolicy"], jsii.get(self, "maintenancePolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="nodePoolInput")
    def node_pool_input(self) -> typing.Optional["KubernetesClusterNodePool"]:
        return typing.cast(typing.Optional["KubernetesClusterNodePool"], jsii.get(self, "nodePoolInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="registryIntegrationInput")
    def registry_integration_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "registryIntegrationInput"))

    @builtins.property
    @jsii.member(jsii_name="surgeUpgradeInput")
    def surge_upgrade_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "surgeUpgradeInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, "KubernetesClusterTimeouts"]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, "KubernetesClusterTimeouts"]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="vpcUuidInput")
    def vpc_uuid_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpcUuidInput"))

    @builtins.property
    @jsii.member(jsii_name="autoUpgrade")
    def auto_upgrade(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "autoUpgrade"))

    @auto_upgrade.setter
    def auto_upgrade(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e70f8e6b9cd6116fd998e9b7158e1f1cb6f037bee1b67228c6ffc1facd4f9f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoUpgrade", value)

    @builtins.property
    @jsii.member(jsii_name="ha")
    def ha(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "ha"))

    @ha.setter
    def ha(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28db8f2b58a21cc03c339170bcc515d46d85fa0da49b21d742650092f2b301e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ha", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0cda50dc2e07cc92c381930a95166247ba5f45e75dbc63c5d7e2d48f316a7d4c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ddeb69d1aa03b3a2b361094ca1b52751cebf2851ea4df1cda3f28e71baf7734)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c03d49ea6e71a7e66fa9b2bfda327fd9715c5c89965b72c7def9a1073bea6fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="registryIntegration")
    def registry_integration(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "registryIntegration"))

    @registry_integration.setter
    def registry_integration(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38a15864f045c0458e12fb2bb0eba92ff6b9fba52e07ea6796334457d628b4cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "registryIntegration", value)

    @builtins.property
    @jsii.member(jsii_name="surgeUpgrade")
    def surge_upgrade(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "surgeUpgrade"))

    @surge_upgrade.setter
    def surge_upgrade(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d9469ce2dd032aaf99dd1b7ac1b0faff30c4be2faccd5c8dfb6dec90b384f7c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "surgeUpgrade", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9eb3a0d071cb430bc69a797f621b58be8da1b915f8a0534c928e19e952f166eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8260a075d15bea06f8bf7753b01cce0126b4c9614190a51f68e42c7207c3174)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="vpcUuid")
    def vpc_uuid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcUuid"))

    @vpc_uuid.setter
    def vpc_uuid(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__addef1027d57cff948844513d2bed644f18df3bb1277fe4d7b52e8a2b2e8a256)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcUuid", value)


@jsii.data_type(
    jsii_type="digitalocean.kubernetesCluster.KubernetesClusterConfig",
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
        "node_pool": "nodePool",
        "region": "region",
        "version": "version",
        "auto_upgrade": "autoUpgrade",
        "ha": "ha",
        "id": "id",
        "maintenance_policy": "maintenancePolicy",
        "registry_integration": "registryIntegration",
        "surge_upgrade": "surgeUpgrade",
        "tags": "tags",
        "timeouts": "timeouts",
        "vpc_uuid": "vpcUuid",
    },
)
class KubernetesClusterConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        name: builtins.str,
        node_pool: typing.Union["KubernetesClusterNodePool", typing.Dict[builtins.str, typing.Any]],
        region: builtins.str,
        version: builtins.str,
        auto_upgrade: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        ha: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        maintenance_policy: typing.Optional[typing.Union["KubernetesClusterMaintenancePolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        registry_integration: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        surge_upgrade: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["KubernetesClusterTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        vpc_uuid: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#name KubernetesCluster#name}.
        :param node_pool: node_pool block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#node_pool KubernetesCluster#node_pool}
        :param region: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#region KubernetesCluster#region}.
        :param version: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#version KubernetesCluster#version}.
        :param auto_upgrade: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#auto_upgrade KubernetesCluster#auto_upgrade}.
        :param ha: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#ha KubernetesCluster#ha}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#id KubernetesCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param maintenance_policy: maintenance_policy block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#maintenance_policy KubernetesCluster#maintenance_policy}
        :param registry_integration: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#registry_integration KubernetesCluster#registry_integration}.
        :param surge_upgrade: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#surge_upgrade KubernetesCluster#surge_upgrade}.
        :param tags: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#tags KubernetesCluster#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#timeouts KubernetesCluster#timeouts}
        :param vpc_uuid: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#vpc_uuid KubernetesCluster#vpc_uuid}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(node_pool, dict):
            node_pool = KubernetesClusterNodePool(**node_pool)
        if isinstance(maintenance_policy, dict):
            maintenance_policy = KubernetesClusterMaintenancePolicy(**maintenance_policy)
        if isinstance(timeouts, dict):
            timeouts = KubernetesClusterTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a412395cee00a5f49ecce3d5a8e7aba75b2295b85d2d0556b9a67dbfa961228)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument node_pool", value=node_pool, expected_type=type_hints["node_pool"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            check_type(argname="argument auto_upgrade", value=auto_upgrade, expected_type=type_hints["auto_upgrade"])
            check_type(argname="argument ha", value=ha, expected_type=type_hints["ha"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument maintenance_policy", value=maintenance_policy, expected_type=type_hints["maintenance_policy"])
            check_type(argname="argument registry_integration", value=registry_integration, expected_type=type_hints["registry_integration"])
            check_type(argname="argument surge_upgrade", value=surge_upgrade, expected_type=type_hints["surge_upgrade"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument vpc_uuid", value=vpc_uuid, expected_type=type_hints["vpc_uuid"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "node_pool": node_pool,
            "region": region,
            "version": version,
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
        if auto_upgrade is not None:
            self._values["auto_upgrade"] = auto_upgrade
        if ha is not None:
            self._values["ha"] = ha
        if id is not None:
            self._values["id"] = id
        if maintenance_policy is not None:
            self._values["maintenance_policy"] = maintenance_policy
        if registry_integration is not None:
            self._values["registry_integration"] = registry_integration
        if surge_upgrade is not None:
            self._values["surge_upgrade"] = surge_upgrade
        if tags is not None:
            self._values["tags"] = tags
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if vpc_uuid is not None:
            self._values["vpc_uuid"] = vpc_uuid

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
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#name KubernetesCluster#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def node_pool(self) -> "KubernetesClusterNodePool":
        '''node_pool block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#node_pool KubernetesCluster#node_pool}
        '''
        result = self._values.get("node_pool")
        assert result is not None, "Required property 'node_pool' is missing"
        return typing.cast("KubernetesClusterNodePool", result)

    @builtins.property
    def region(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#region KubernetesCluster#region}.'''
        result = self._values.get("region")
        assert result is not None, "Required property 'region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#version KubernetesCluster#version}.'''
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auto_upgrade(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#auto_upgrade KubernetesCluster#auto_upgrade}.'''
        result = self._values.get("auto_upgrade")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def ha(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#ha KubernetesCluster#ha}.'''
        result = self._values.get("ha")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#id KubernetesCluster#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def maintenance_policy(
        self,
    ) -> typing.Optional["KubernetesClusterMaintenancePolicy"]:
        '''maintenance_policy block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#maintenance_policy KubernetesCluster#maintenance_policy}
        '''
        result = self._values.get("maintenance_policy")
        return typing.cast(typing.Optional["KubernetesClusterMaintenancePolicy"], result)

    @builtins.property
    def registry_integration(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#registry_integration KubernetesCluster#registry_integration}.'''
        result = self._values.get("registry_integration")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def surge_upgrade(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#surge_upgrade KubernetesCluster#surge_upgrade}.'''
        result = self._values.get("surge_upgrade")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#tags KubernetesCluster#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["KubernetesClusterTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#timeouts KubernetesCluster#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["KubernetesClusterTimeouts"], result)

    @builtins.property
    def vpc_uuid(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#vpc_uuid KubernetesCluster#vpc_uuid}.'''
        result = self._values.get("vpc_uuid")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesClusterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="digitalocean.kubernetesCluster.KubernetesClusterKubeConfig",
    jsii_struct_bases=[],
    name_mapping={},
)
class KubernetesClusterKubeConfig:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesClusterKubeConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KubernetesClusterKubeConfigList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.kubernetesCluster.KubernetesClusterKubeConfigList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4f755941d7b50ee8f71dc2218f5224232790f8ac9bfff4411117cb1df7d2e0fe)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "KubernetesClusterKubeConfigOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65cbfed2f2f352a9c07524e7fe428031ebfdf25e1dd37e94f341d3725cb44649)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KubernetesClusterKubeConfigOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a2f344b2942fb91a73935341d84e6b4cd34a3bfd15ed9c35c10e996bccdf666)
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
            type_hints = typing.get_type_hints(_typecheckingstub__794f1f0d7ce12a5ad48ba01b1c4827a5fbb32e6b3dfb6784ec03ba084e4eebe4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b4b93ff268cefbd3596605555f699a031c3805fe08544c910554f01c7e9988a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class KubernetesClusterKubeConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.kubernetesCluster.KubernetesClusterKubeConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fa10b4ff5259c84ce49f66e999052230820c8829d4d1e502b6f4899cd48e63f0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

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
    def internal_value(self) -> typing.Optional[KubernetesClusterKubeConfig]:
        return typing.cast(typing.Optional[KubernetesClusterKubeConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KubernetesClusterKubeConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eff50d15f327bcba874d4f5e536bf0ed77972e53123cec243afbb91970c92fab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="digitalocean.kubernetesCluster.KubernetesClusterMaintenancePolicy",
    jsii_struct_bases=[],
    name_mapping={"day": "day", "start_time": "startTime"},
)
class KubernetesClusterMaintenancePolicy:
    def __init__(
        self,
        *,
        day: typing.Optional[builtins.str] = None,
        start_time: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param day: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#day KubernetesCluster#day}.
        :param start_time: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#start_time KubernetesCluster#start_time}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9ec8b09c70f3b40d46de01e9b9e27ffddd1dd9474cd9b5b3d3f7f07d5fc7cf7)
            check_type(argname="argument day", value=day, expected_type=type_hints["day"])
            check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if day is not None:
            self._values["day"] = day
        if start_time is not None:
            self._values["start_time"] = start_time

    @builtins.property
    def day(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#day KubernetesCluster#day}.'''
        result = self._values.get("day")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def start_time(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#start_time KubernetesCluster#start_time}.'''
        result = self._values.get("start_time")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesClusterMaintenancePolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KubernetesClusterMaintenancePolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.kubernetesCluster.KubernetesClusterMaintenancePolicyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1a4480ad0cea400f07b973646d895634b25183be161cde790dccda952e0bead0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDay")
    def reset_day(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDay", []))

    @jsii.member(jsii_name="resetStartTime")
    def reset_start_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartTime", []))

    @builtins.property
    @jsii.member(jsii_name="duration")
    def duration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "duration"))

    @builtins.property
    @jsii.member(jsii_name="dayInput")
    def day_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dayInput"))

    @builtins.property
    @jsii.member(jsii_name="startTimeInput")
    def start_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="day")
    def day(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "day"))

    @day.setter
    def day(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2bbada4e61bd8731ea73504a2e184aa8bdfb97c2de8c950481337a57af4e330)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "day", value)

    @builtins.property
    @jsii.member(jsii_name="startTime")
    def start_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startTime"))

    @start_time.setter
    def start_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70e1175421b845712c71c95b8c7a649639130d71e37267b075c23a3e2773aee3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startTime", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[KubernetesClusterMaintenancePolicy]:
        return typing.cast(typing.Optional[KubernetesClusterMaintenancePolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KubernetesClusterMaintenancePolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7dc349d87f2e64287acf019723876289e072576ac2b8960a6c2192e52d59e8a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="digitalocean.kubernetesCluster.KubernetesClusterNodePool",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "size": "size",
        "auto_scale": "autoScale",
        "labels": "labels",
        "max_nodes": "maxNodes",
        "min_nodes": "minNodes",
        "node_count": "nodeCount",
        "tags": "tags",
        "taint": "taint",
    },
)
class KubernetesClusterNodePool:
    def __init__(
        self,
        *,
        name: builtins.str,
        size: builtins.str,
        auto_scale: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        max_nodes: typing.Optional[jsii.Number] = None,
        min_nodes: typing.Optional[jsii.Number] = None,
        node_count: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        taint: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KubernetesClusterNodePoolTaint", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#name KubernetesCluster#name}.
        :param size: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#size KubernetesCluster#size}.
        :param auto_scale: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#auto_scale KubernetesCluster#auto_scale}.
        :param labels: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#labels KubernetesCluster#labels}.
        :param max_nodes: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#max_nodes KubernetesCluster#max_nodes}.
        :param min_nodes: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#min_nodes KubernetesCluster#min_nodes}.
        :param node_count: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#node_count KubernetesCluster#node_count}.
        :param tags: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#tags KubernetesCluster#tags}.
        :param taint: taint block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#taint KubernetesCluster#taint}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__200ad1fe1a0e453d050edc6f55f8cfcf9675797b35e36d9257803ba58c8a3e1f)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument size", value=size, expected_type=type_hints["size"])
            check_type(argname="argument auto_scale", value=auto_scale, expected_type=type_hints["auto_scale"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument max_nodes", value=max_nodes, expected_type=type_hints["max_nodes"])
            check_type(argname="argument min_nodes", value=min_nodes, expected_type=type_hints["min_nodes"])
            check_type(argname="argument node_count", value=node_count, expected_type=type_hints["node_count"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument taint", value=taint, expected_type=type_hints["taint"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "size": size,
        }
        if auto_scale is not None:
            self._values["auto_scale"] = auto_scale
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

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#name KubernetesCluster#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def size(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#size KubernetesCluster#size}.'''
        result = self._values.get("size")
        assert result is not None, "Required property 'size' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auto_scale(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#auto_scale KubernetesCluster#auto_scale}.'''
        result = self._values.get("auto_scale")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#labels KubernetesCluster#labels}.'''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def max_nodes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#max_nodes KubernetesCluster#max_nodes}.'''
        result = self._values.get("max_nodes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_nodes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#min_nodes KubernetesCluster#min_nodes}.'''
        result = self._values.get("min_nodes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def node_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#node_count KubernetesCluster#node_count}.'''
        result = self._values.get("node_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#tags KubernetesCluster#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def taint(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesClusterNodePoolTaint"]]]:
        '''taint block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#taint KubernetesCluster#taint}
        '''
        result = self._values.get("taint")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesClusterNodePoolTaint"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesClusterNodePool(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="digitalocean.kubernetesCluster.KubernetesClusterNodePoolNodes",
    jsii_struct_bases=[],
    name_mapping={},
)
class KubernetesClusterNodePoolNodes:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesClusterNodePoolNodes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KubernetesClusterNodePoolNodesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.kubernetesCluster.KubernetesClusterNodePoolNodesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__07238336a752ba03007dabc79e618b772fe7e5992f2bad57917049164f370910)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "KubernetesClusterNodePoolNodesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6c791ce6b7faeb3d26827bd5f1936d93ee02e67cc7f1179eb6f6281f87d92ae)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KubernetesClusterNodePoolNodesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1438f710354c8bcab08beddefc460cbf28ca8f70ccd788e2367710724619e4fa)
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
            type_hints = typing.get_type_hints(_typecheckingstub__fd559ce6ee83f1390bbc24edbcad575e7404c26a0fbfec11d34f327a8b2df363)
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
            type_hints = typing.get_type_hints(_typecheckingstub__80fb4b9e9b80177ef002070b93266f871e7f3a79999324eb4f4c2c16407e9054)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class KubernetesClusterNodePoolNodesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.kubernetesCluster.KubernetesClusterNodePoolNodesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8259ffff7e9b0c74bab22a53929bbaca66eb30b9b8db423d947c5efa32152bbc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

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
    def internal_value(self) -> typing.Optional[KubernetesClusterNodePoolNodes]:
        return typing.cast(typing.Optional[KubernetesClusterNodePoolNodes], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KubernetesClusterNodePoolNodes],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc670916a32fb348e109274b8a6223ec00045359b4dd52a4b06938578145928d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KubernetesClusterNodePoolOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.kubernetesCluster.KubernetesClusterNodePoolOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__85dbbf0dada731b9ddc238fcc7f5fb82b753ed4530e19d9438523e03eb121dc8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putTaint")
    def put_taint(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KubernetesClusterNodePoolTaint", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2b6322c3cc9ad4d3ada2ab6272f895a50e8a4f13cb98487ad340696778975f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTaint", [value]))

    @jsii.member(jsii_name="resetAutoScale")
    def reset_auto_scale(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoScale", []))

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

    @builtins.property
    @jsii.member(jsii_name="actualNodeCount")
    def actual_node_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "actualNodeCount"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="nodes")
    def nodes(self) -> KubernetesClusterNodePoolNodesList:
        return typing.cast(KubernetesClusterNodePoolNodesList, jsii.get(self, "nodes"))

    @builtins.property
    @jsii.member(jsii_name="taint")
    def taint(self) -> "KubernetesClusterNodePoolTaintList":
        return typing.cast("KubernetesClusterNodePoolTaintList", jsii.get(self, "taint"))

    @builtins.property
    @jsii.member(jsii_name="autoScaleInput")
    def auto_scale_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "autoScaleInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="maxNodesInput")
    def max_nodes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxNodesInput"))

    @builtins.property
    @jsii.member(jsii_name="minNodesInput")
    def min_nodes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minNodesInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeCountInput")
    def node_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "nodeCountInput"))

    @builtins.property
    @jsii.member(jsii_name="sizeInput")
    def size_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sizeInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="taintInput")
    def taint_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesClusterNodePoolTaint"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesClusterNodePoolTaint"]]], jsii.get(self, "taintInput"))

    @builtins.property
    @jsii.member(jsii_name="autoScale")
    def auto_scale(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "autoScale"))

    @auto_scale.setter
    def auto_scale(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1eb56213f4ad26981cf1d550826988c1ce69362a0230defc3d37ada3e5b17b5a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoScale", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a1323a7970de08fa2e4d61d42ab8824627fd65f133b95f9f54c20e1891bf53b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="maxNodes")
    def max_nodes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxNodes"))

    @max_nodes.setter
    def max_nodes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2202743ac342186c741d615a83d37622ae9f63512f687e3ab54d37c2f3790a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxNodes", value)

    @builtins.property
    @jsii.member(jsii_name="minNodes")
    def min_nodes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minNodes"))

    @min_nodes.setter
    def min_nodes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50214cf97cec2cd54af10f24505746dfd3c884e5e61d9f4afcec20c6e50f51cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minNodes", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5d9cb95a991d61e5bd086748dfcdc76f20e4e126b64f833c64d23bef0759d6a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="nodeCount")
    def node_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "nodeCount"))

    @node_count.setter
    def node_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9698c48161623ead56c0d31c0a55ef9b439c58663a81d8b26a042d88a9a38218)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodeCount", value)

    @builtins.property
    @jsii.member(jsii_name="size")
    def size(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "size"))

    @size.setter
    def size(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9f85e80d2540fba75c1bda0255b8932956c0bc0925c2736c05a5bab465b7107)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "size", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aceeaf35cba16f46e93ab5dade9c52661dbd2dde58d094f2e7b6a9335d51ebb1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[KubernetesClusterNodePool]:
        return typing.cast(typing.Optional[KubernetesClusterNodePool], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[KubernetesClusterNodePool]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12612d98dc5f0d32464398bac6dfb8770fd3d55c26d27de8115c8c2efcd56227)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="digitalocean.kubernetesCluster.KubernetesClusterNodePoolTaint",
    jsii_struct_bases=[],
    name_mapping={"effect": "effect", "key": "key", "value": "value"},
)
class KubernetesClusterNodePoolTaint:
    def __init__(
        self,
        *,
        effect: builtins.str,
        key: builtins.str,
        value: builtins.str,
    ) -> None:
        '''
        :param effect: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#effect KubernetesCluster#effect}.
        :param key: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#key KubernetesCluster#key}.
        :param value: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#value KubernetesCluster#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8808d4a52e7ea4725bb4939ee1178660392f2794ab00c86e9f54c4a870055fa2)
            check_type(argname="argument effect", value=effect, expected_type=type_hints["effect"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "effect": effect,
            "key": key,
            "value": value,
        }

    @builtins.property
    def effect(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#effect KubernetesCluster#effect}.'''
        result = self._values.get("effect")
        assert result is not None, "Required property 'effect' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#key KubernetesCluster#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#value KubernetesCluster#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesClusterNodePoolTaint(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KubernetesClusterNodePoolTaintList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.kubernetesCluster.KubernetesClusterNodePoolTaintList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0f221f6b3d85190414f3487bae929f452a932236a571649c8f54c2fe453dc8aa)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "KubernetesClusterNodePoolTaintOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7fc728030336e5f48bf8aae29b44cd64fff1780602dd8645677aaab9d01def44)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KubernetesClusterNodePoolTaintOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc1b01f9838d6319ab788331ceedbe5e383f993a21924b5c3b78ba861f1614d2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5d0489016c8e0f8f0edb8f9d390950c2c1c73bf6a58d483f48575087346ca021)
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
            type_hints = typing.get_type_hints(_typecheckingstub__21d416bea0c52d498e864353bff40089f4f19e8e5fdec7f76cbed94524047d11)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesClusterNodePoolTaint]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesClusterNodePoolTaint]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesClusterNodePoolTaint]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76d0af0f06b7028fd2f2177da934b0b719034c5d792d4302d2d803a3a29b4825)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KubernetesClusterNodePoolTaintOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.kubernetesCluster.KubernetesClusterNodePoolTaintOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__050e86d51b40cb10cb7635c87fa49d8746c3d72d2478c0b9545eaa07e869863d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

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
            type_hints = typing.get_type_hints(_typecheckingstub__4ab50d96c56bce4cf27a13532903d72edfb4709ea24dfbdfb232e7c8a5338100)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "effect", value)

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be4c3b6289ebbaef26cfa7fc80c7e421f7809a92e5ca6320b4cbd3e3bd522a68)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21f8591bb15ccdbd965c34f3f3af2531f9bdcc8b1fb54b7a1e48ef084619020c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesClusterNodePoolTaint]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesClusterNodePoolTaint]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesClusterNodePoolTaint]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c9457ad3d89f68814b2e4d5830044762ebcc11862689f71dc61bbf880c71334)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="digitalocean.kubernetesCluster.KubernetesClusterTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create"},
)
class KubernetesClusterTimeouts:
    def __init__(self, *, create: typing.Optional[builtins.str] = None) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#create KubernetesCluster#create}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__270027534d5c28bca83d38f8059307358a68c714bcf489a17e5539dff9b88894)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/kubernetes_cluster#create KubernetesCluster#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesClusterTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KubernetesClusterTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.kubernetesCluster.KubernetesClusterTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a9bf1539149620548f9453ad8c67c8517d3048b1911548751125a95cab4888b4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08486738e9fd0b2fe975d42581b6e491e814e6417fe12aef47f825cfbaa20289)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesClusterTimeouts]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesClusterTimeouts]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesClusterTimeouts]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1cd36288cb760623bb511812dcc0c36ac25e6efea2274b442815a93fc2120762)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "KubernetesCluster",
    "KubernetesClusterConfig",
    "KubernetesClusterKubeConfig",
    "KubernetesClusterKubeConfigList",
    "KubernetesClusterKubeConfigOutputReference",
    "KubernetesClusterMaintenancePolicy",
    "KubernetesClusterMaintenancePolicyOutputReference",
    "KubernetesClusterNodePool",
    "KubernetesClusterNodePoolNodes",
    "KubernetesClusterNodePoolNodesList",
    "KubernetesClusterNodePoolNodesOutputReference",
    "KubernetesClusterNodePoolOutputReference",
    "KubernetesClusterNodePoolTaint",
    "KubernetesClusterNodePoolTaintList",
    "KubernetesClusterNodePoolTaintOutputReference",
    "KubernetesClusterTimeouts",
    "KubernetesClusterTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__9214e633254b00f1797cbedabc09c9c19ed1c4a8a6d27c64a8d89a3ab878ef15(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    node_pool: typing.Union[KubernetesClusterNodePool, typing.Dict[builtins.str, typing.Any]],
    region: builtins.str,
    version: builtins.str,
    auto_upgrade: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ha: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    maintenance_policy: typing.Optional[typing.Union[KubernetesClusterMaintenancePolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    registry_integration: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    surge_upgrade: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[KubernetesClusterTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    vpc_uuid: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__5e70f8e6b9cd6116fd998e9b7158e1f1cb6f037bee1b67228c6ffc1facd4f9f2(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28db8f2b58a21cc03c339170bcc515d46d85fa0da49b21d742650092f2b301e5(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0cda50dc2e07cc92c381930a95166247ba5f45e75dbc63c5d7e2d48f316a7d4c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ddeb69d1aa03b3a2b361094ca1b52751cebf2851ea4df1cda3f28e71baf7734(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c03d49ea6e71a7e66fa9b2bfda327fd9715c5c89965b72c7def9a1073bea6fb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38a15864f045c0458e12fb2bb0eba92ff6b9fba52e07ea6796334457d628b4cb(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d9469ce2dd032aaf99dd1b7ac1b0faff30c4be2faccd5c8dfb6dec90b384f7c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9eb3a0d071cb430bc69a797f621b58be8da1b915f8a0534c928e19e952f166eb(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8260a075d15bea06f8bf7753b01cce0126b4c9614190a51f68e42c7207c3174(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__addef1027d57cff948844513d2bed644f18df3bb1277fe4d7b52e8a2b2e8a256(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a412395cee00a5f49ecce3d5a8e7aba75b2295b85d2d0556b9a67dbfa961228(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    node_pool: typing.Union[KubernetesClusterNodePool, typing.Dict[builtins.str, typing.Any]],
    region: builtins.str,
    version: builtins.str,
    auto_upgrade: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ha: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    maintenance_policy: typing.Optional[typing.Union[KubernetesClusterMaintenancePolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    registry_integration: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    surge_upgrade: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[KubernetesClusterTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    vpc_uuid: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f755941d7b50ee8f71dc2218f5224232790f8ac9bfff4411117cb1df7d2e0fe(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65cbfed2f2f352a9c07524e7fe428031ebfdf25e1dd37e94f341d3725cb44649(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a2f344b2942fb91a73935341d84e6b4cd34a3bfd15ed9c35c10e996bccdf666(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__794f1f0d7ce12a5ad48ba01b1c4827a5fbb32e6b3dfb6784ec03ba084e4eebe4(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4b93ff268cefbd3596605555f699a031c3805fe08544c910554f01c7e9988a0(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa10b4ff5259c84ce49f66e999052230820c8829d4d1e502b6f4899cd48e63f0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eff50d15f327bcba874d4f5e536bf0ed77972e53123cec243afbb91970c92fab(
    value: typing.Optional[KubernetesClusterKubeConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9ec8b09c70f3b40d46de01e9b9e27ffddd1dd9474cd9b5b3d3f7f07d5fc7cf7(
    *,
    day: typing.Optional[builtins.str] = None,
    start_time: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a4480ad0cea400f07b973646d895634b25183be161cde790dccda952e0bead0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2bbada4e61bd8731ea73504a2e184aa8bdfb97c2de8c950481337a57af4e330(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70e1175421b845712c71c95b8c7a649639130d71e37267b075c23a3e2773aee3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7dc349d87f2e64287acf019723876289e072576ac2b8960a6c2192e52d59e8a(
    value: typing.Optional[KubernetesClusterMaintenancePolicy],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__200ad1fe1a0e453d050edc6f55f8cfcf9675797b35e36d9257803ba58c8a3e1f(
    *,
    name: builtins.str,
    size: builtins.str,
    auto_scale: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    max_nodes: typing.Optional[jsii.Number] = None,
    min_nodes: typing.Optional[jsii.Number] = None,
    node_count: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    taint: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesClusterNodePoolTaint, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07238336a752ba03007dabc79e618b772fe7e5992f2bad57917049164f370910(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6c791ce6b7faeb3d26827bd5f1936d93ee02e67cc7f1179eb6f6281f87d92ae(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1438f710354c8bcab08beddefc460cbf28ca8f70ccd788e2367710724619e4fa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd559ce6ee83f1390bbc24edbcad575e7404c26a0fbfec11d34f327a8b2df363(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80fb4b9e9b80177ef002070b93266f871e7f3a79999324eb4f4c2c16407e9054(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8259ffff7e9b0c74bab22a53929bbaca66eb30b9b8db423d947c5efa32152bbc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc670916a32fb348e109274b8a6223ec00045359b4dd52a4b06938578145928d(
    value: typing.Optional[KubernetesClusterNodePoolNodes],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85dbbf0dada731b9ddc238fcc7f5fb82b753ed4530e19d9438523e03eb121dc8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2b6322c3cc9ad4d3ada2ab6272f895a50e8a4f13cb98487ad340696778975f9(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesClusterNodePoolTaint, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1eb56213f4ad26981cf1d550826988c1ce69362a0230defc3d37ada3e5b17b5a(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a1323a7970de08fa2e4d61d42ab8824627fd65f133b95f9f54c20e1891bf53b(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2202743ac342186c741d615a83d37622ae9f63512f687e3ab54d37c2f3790a1(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50214cf97cec2cd54af10f24505746dfd3c884e5e61d9f4afcec20c6e50f51cf(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5d9cb95a991d61e5bd086748dfcdc76f20e4e126b64f833c64d23bef0759d6a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9698c48161623ead56c0d31c0a55ef9b439c58663a81d8b26a042d88a9a38218(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9f85e80d2540fba75c1bda0255b8932956c0bc0925c2736c05a5bab465b7107(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aceeaf35cba16f46e93ab5dade9c52661dbd2dde58d094f2e7b6a9335d51ebb1(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12612d98dc5f0d32464398bac6dfb8770fd3d55c26d27de8115c8c2efcd56227(
    value: typing.Optional[KubernetesClusterNodePool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8808d4a52e7ea4725bb4939ee1178660392f2794ab00c86e9f54c4a870055fa2(
    *,
    effect: builtins.str,
    key: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f221f6b3d85190414f3487bae929f452a932236a571649c8f54c2fe453dc8aa(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fc728030336e5f48bf8aae29b44cd64fff1780602dd8645677aaab9d01def44(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc1b01f9838d6319ab788331ceedbe5e383f993a21924b5c3b78ba861f1614d2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d0489016c8e0f8f0edb8f9d390950c2c1c73bf6a58d483f48575087346ca021(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21d416bea0c52d498e864353bff40089f4f19e8e5fdec7f76cbed94524047d11(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76d0af0f06b7028fd2f2177da934b0b719034c5d792d4302d2d803a3a29b4825(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesClusterNodePoolTaint]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__050e86d51b40cb10cb7635c87fa49d8746c3d72d2478c0b9545eaa07e869863d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ab50d96c56bce4cf27a13532903d72edfb4709ea24dfbdfb232e7c8a5338100(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be4c3b6289ebbaef26cfa7fc80c7e421f7809a92e5ca6320b4cbd3e3bd522a68(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21f8591bb15ccdbd965c34f3f3af2531f9bdcc8b1fb54b7a1e48ef084619020c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c9457ad3d89f68814b2e4d5830044762ebcc11862689f71dc61bbf880c71334(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesClusterNodePoolTaint]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__270027534d5c28bca83d38f8059307358a68c714bcf489a17e5539dff9b88894(
    *,
    create: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9bf1539149620548f9453ad8c67c8517d3048b1911548751125a95cab4888b4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08486738e9fd0b2fe975d42581b6e491e814e6417fe12aef47f825cfbaa20289(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1cd36288cb760623bb511812dcc0c36ac25e6efea2274b442815a93fc2120762(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesClusterTimeouts]],
) -> None:
    """Type checking stubs"""
    pass
