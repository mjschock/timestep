'''
# `timescale_peering_connection`

Refer to the Terraform Registory for docs: [`timescale_peering_connection`](https://registry.terraform.io/providers/timescale/timescale/1.11.0/docs/resources/peering_connection).
'''
from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)

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


class PeeringConnection(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="timescale.peeringConnection.PeeringConnection",
):
    '''Represents a {@link https://registry.terraform.io/providers/timescale/timescale/1.11.0/docs/resources/peering_connection timescale_peering_connection}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        peer_account_id: builtins.str,
        peer_region_code: builtins.str,
        peer_vpc_id: builtins.str,
        timescale_vpc_id: jsii.Number,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/timescale/timescale/1.11.0/docs/resources/peering_connection timescale_peering_connection} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param peer_account_id: AWS account ID where the VPC to be paired. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/timescale/timescale/1.11.0/docs/resources/peering_connection#peer_account_id PeeringConnection#peer_account_id}
        :param peer_region_code: Region code for the VPC to be paired. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/timescale/timescale/1.11.0/docs/resources/peering_connection#peer_region_code PeeringConnection#peer_region_code}
        :param peer_vpc_id: AWS ID for the VPC to be paired. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/timescale/timescale/1.11.0/docs/resources/peering_connection#peer_vpc_id PeeringConnection#peer_vpc_id}
        :param timescale_vpc_id: Timescale internal ID for a vpc. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/timescale/timescale/1.11.0/docs/resources/peering_connection#timescale_vpc_id PeeringConnection#timescale_vpc_id}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8773a189df62e9ae1eb1c45bf6f3fd2337760aa175a9544f8559071e14ec5f9b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = PeeringConnectionConfig(
            peer_account_id=peer_account_id,
            peer_region_code=peer_region_code,
            peer_vpc_id=peer_vpc_id,
            timescale_vpc_id=timescale_vpc_id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="generateConfigForImport")
    @builtins.classmethod
    def generate_config_for_import(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        import_to_id: builtins.str,
        import_from_id: builtins.str,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    ) -> _cdktf_9a9027ec.ImportableResource:
        '''Generates CDKTF code for importing a PeeringConnection resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the PeeringConnection to import.
        :param import_from_id: The id of the existing PeeringConnection that should be imported. Refer to the {@link https://registry.terraform.io/providers/timescale/timescale/1.11.0/docs/resources/peering_connection#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the PeeringConnection to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2825fe24f23c2610a981eb2bb31fdb56f09b137037e106bac1eaab900380d0c6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="errorMessage")
    def error_message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "errorMessage"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="peerCidr")
    def peer_cidr(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "peerCidr"))

    @builtins.property
    @jsii.member(jsii_name="provisionedId")
    def provisioned_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "provisionedId"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcId"))

    @builtins.property
    @jsii.member(jsii_name="peerAccountIdInput")
    def peer_account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "peerAccountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="peerRegionCodeInput")
    def peer_region_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "peerRegionCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="peerVpcIdInput")
    def peer_vpc_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "peerVpcIdInput"))

    @builtins.property
    @jsii.member(jsii_name="timescaleVpcIdInput")
    def timescale_vpc_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timescaleVpcIdInput"))

    @builtins.property
    @jsii.member(jsii_name="peerAccountId")
    def peer_account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "peerAccountId"))

    @peer_account_id.setter
    def peer_account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b47015fe9398d39189e75ee1cd2bdd27368cf0893fe6cc2f8be22e6e754ad2ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "peerAccountId", value)

    @builtins.property
    @jsii.member(jsii_name="peerRegionCode")
    def peer_region_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "peerRegionCode"))

    @peer_region_code.setter
    def peer_region_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70e94b7a668cc63862cc4eb2cdb666be52b2a19e59111c61f8ec0a9984d6ce45)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "peerRegionCode", value)

    @builtins.property
    @jsii.member(jsii_name="peerVpcId")
    def peer_vpc_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "peerVpcId"))

    @peer_vpc_id.setter
    def peer_vpc_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f0d840cf143b74fed83f8afe49a755881c965ba528902ec378e2fd58653b46f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "peerVpcId", value)

    @builtins.property
    @jsii.member(jsii_name="timescaleVpcId")
    def timescale_vpc_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timescaleVpcId"))

    @timescale_vpc_id.setter
    def timescale_vpc_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37c19c92c0d0ca43ac62c0632b22eb52daa35c3e186d44eda7ee39f9b7fe90ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timescaleVpcId", value)


@jsii.data_type(
    jsii_type="timescale.peeringConnection.PeeringConnectionConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "peer_account_id": "peerAccountId",
        "peer_region_code": "peerRegionCode",
        "peer_vpc_id": "peerVpcId",
        "timescale_vpc_id": "timescaleVpcId",
    },
)
class PeeringConnectionConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        peer_account_id: builtins.str,
        peer_region_code: builtins.str,
        peer_vpc_id: builtins.str,
        timescale_vpc_id: jsii.Number,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param peer_account_id: AWS account ID where the VPC to be paired. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/timescale/timescale/1.11.0/docs/resources/peering_connection#peer_account_id PeeringConnection#peer_account_id}
        :param peer_region_code: Region code for the VPC to be paired. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/timescale/timescale/1.11.0/docs/resources/peering_connection#peer_region_code PeeringConnection#peer_region_code}
        :param peer_vpc_id: AWS ID for the VPC to be paired. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/timescale/timescale/1.11.0/docs/resources/peering_connection#peer_vpc_id PeeringConnection#peer_vpc_id}
        :param timescale_vpc_id: Timescale internal ID for a vpc. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/timescale/timescale/1.11.0/docs/resources/peering_connection#timescale_vpc_id PeeringConnection#timescale_vpc_id}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd55e1c0de2947e0b291209f352079d65b68687bf788b0c0ee316b2cdb3a68c9)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument peer_account_id", value=peer_account_id, expected_type=type_hints["peer_account_id"])
            check_type(argname="argument peer_region_code", value=peer_region_code, expected_type=type_hints["peer_region_code"])
            check_type(argname="argument peer_vpc_id", value=peer_vpc_id, expected_type=type_hints["peer_vpc_id"])
            check_type(argname="argument timescale_vpc_id", value=timescale_vpc_id, expected_type=type_hints["timescale_vpc_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "peer_account_id": peer_account_id,
            "peer_region_code": peer_region_code,
            "peer_vpc_id": peer_vpc_id,
            "timescale_vpc_id": timescale_vpc_id,
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
    def peer_account_id(self) -> builtins.str:
        '''AWS account ID where the VPC to be paired.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/timescale/timescale/1.11.0/docs/resources/peering_connection#peer_account_id PeeringConnection#peer_account_id}
        '''
        result = self._values.get("peer_account_id")
        assert result is not None, "Required property 'peer_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def peer_region_code(self) -> builtins.str:
        '''Region code for the VPC to be paired.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/timescale/timescale/1.11.0/docs/resources/peering_connection#peer_region_code PeeringConnection#peer_region_code}
        '''
        result = self._values.get("peer_region_code")
        assert result is not None, "Required property 'peer_region_code' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def peer_vpc_id(self) -> builtins.str:
        '''AWS ID for the VPC to be paired.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/timescale/timescale/1.11.0/docs/resources/peering_connection#peer_vpc_id PeeringConnection#peer_vpc_id}
        '''
        result = self._values.get("peer_vpc_id")
        assert result is not None, "Required property 'peer_vpc_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def timescale_vpc_id(self) -> jsii.Number:
        '''Timescale internal ID for a vpc.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/timescale/timescale/1.11.0/docs/resources/peering_connection#timescale_vpc_id PeeringConnection#timescale_vpc_id}
        '''
        result = self._values.get("timescale_vpc_id")
        assert result is not None, "Required property 'timescale_vpc_id' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PeeringConnectionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "PeeringConnection",
    "PeeringConnectionConfig",
]

publication.publish()

def _typecheckingstub__8773a189df62e9ae1eb1c45bf6f3fd2337760aa175a9544f8559071e14ec5f9b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    peer_account_id: builtins.str,
    peer_region_code: builtins.str,
    peer_vpc_id: builtins.str,
    timescale_vpc_id: jsii.Number,
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

def _typecheckingstub__2825fe24f23c2610a981eb2bb31fdb56f09b137037e106bac1eaab900380d0c6(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b47015fe9398d39189e75ee1cd2bdd27368cf0893fe6cc2f8be22e6e754ad2ea(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70e94b7a668cc63862cc4eb2cdb666be52b2a19e59111c61f8ec0a9984d6ce45(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f0d840cf143b74fed83f8afe49a755881c965ba528902ec378e2fd58653b46f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37c19c92c0d0ca43ac62c0632b22eb52daa35c3e186d44eda7ee39f9b7fe90ec(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd55e1c0de2947e0b291209f352079d65b68687bf788b0c0ee316b2cdb3a68c9(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    peer_account_id: builtins.str,
    peer_region_code: builtins.str,
    peer_vpc_id: builtins.str,
    timescale_vpc_id: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass
