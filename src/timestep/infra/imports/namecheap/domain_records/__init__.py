'''
# `namecheap_domain_records`

Refer to the Terraform Registory for docs: [`namecheap_domain_records`](https://registry.terraform.io/providers/namecheap/namecheap/2.1.0/docs/resources/domain_records).
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


class DomainRecords(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="namecheap.domainRecords.DomainRecords",
):
    '''Represents a {@link https://registry.terraform.io/providers/namecheap/namecheap/2.1.0/docs/resources/domain_records namecheap_domain_records}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        domain: builtins.str,
        email_type: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        mode: typing.Optional[builtins.str] = None,
        nameservers: typing.Optional[typing.Sequence[builtins.str]] = None,
        record: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DomainRecordsRecord", typing.Dict[builtins.str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/namecheap/namecheap/2.1.0/docs/resources/domain_records namecheap_domain_records} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param domain: Purchased available domain name on your account. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/namecheap/namecheap/2.1.0/docs/resources/domain_records#domain DomainRecords#domain}
        :param email_type: Possible values: NONE, MXE, MX, FWD, OX, GMAIL. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/namecheap/namecheap/2.1.0/docs/resources/domain_records#email_type DomainRecords#email_type}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/namecheap/namecheap/2.1.0/docs/resources/domain_records#id DomainRecords#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param mode: Possible values: MERGE (default), OVERWRITE. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/namecheap/namecheap/2.1.0/docs/resources/domain_records#mode DomainRecords#mode}
        :param nameservers: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/namecheap/namecheap/2.1.0/docs/resources/domain_records#nameservers DomainRecords#nameservers}.
        :param record: record block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/namecheap/namecheap/2.1.0/docs/resources/domain_records#record DomainRecords#record}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b313967db773a536c66889272b80880720543e147e5b84201f4a8143bdead2a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DomainRecordsConfig(
            domain=domain,
            email_type=email_type,
            id=id,
            mode=mode,
            nameservers=nameservers,
            record=record,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="generateConfigForImport")
    @builtins.classmethod
    def generate_config_for_import(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        import_to_id: builtins.str,
        import_from_id: builtins.str,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    ) -> _cdktf_9a9027ec.ImportableResource:
        '''Generates CDKTF code for importing a DomainRecords resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the DomainRecords to import.
        :param import_from_id: The id of the existing DomainRecords that should be imported. Refer to the {@link https://registry.terraform.io/providers/namecheap/namecheap/2.1.0/docs/resources/domain_records#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the DomainRecords to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe0674d0638597aaf2c35a88eb205405daf8f7e65b85a339ce779d73a06c9687)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putRecord")
    def put_record(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DomainRecordsRecord", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94d43f757255215793d0ae9f9039f8d0e20c7404c0c4cac91ad1a23d28bb77a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRecord", [value]))

    @jsii.member(jsii_name="resetEmailType")
    def reset_email_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmailType", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMode")
    def reset_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMode", []))

    @jsii.member(jsii_name="resetNameservers")
    def reset_nameservers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNameservers", []))

    @jsii.member(jsii_name="resetRecord")
    def reset_record(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRecord", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="record")
    def record(self) -> "DomainRecordsRecordList":
        return typing.cast("DomainRecordsRecordList", jsii.get(self, "record"))

    @builtins.property
    @jsii.member(jsii_name="domainInput")
    def domain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainInput"))

    @builtins.property
    @jsii.member(jsii_name="emailTypeInput")
    def email_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emailTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="modeInput")
    def mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modeInput"))

    @builtins.property
    @jsii.member(jsii_name="nameserversInput")
    def nameservers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "nameserversInput"))

    @builtins.property
    @jsii.member(jsii_name="recordInput")
    def record_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DomainRecordsRecord"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DomainRecordsRecord"]]], jsii.get(self, "recordInput"))

    @builtins.property
    @jsii.member(jsii_name="domain")
    def domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domain"))

    @domain.setter
    def domain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b7cf27e1dc49be06e701d7b9bb2ab46cf813d47319bdab345ba5e1aa5561eb3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domain", value)

    @builtins.property
    @jsii.member(jsii_name="emailType")
    def email_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "emailType"))

    @email_type.setter
    def email_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__746c5bf8b16a57f0e97c73bcb115b1ccebe8e2ef34dd54a77c52e5b5ba7bb535)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emailType", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ece4d601106b831e442d86c8ab9fdee1584a4c44bb753243dda237163463732)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mode"))

    @mode.setter
    def mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fca3ca9caba003addf698da52c96c7dbb84efb1d1e8f217cd7e57b7e68d3f026)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="nameservers")
    def nameservers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "nameservers"))

    @nameservers.setter
    def nameservers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ffa74f4d91c5e03c88bb15e8756461a652a7f91ac4c1494dd90dcc41bdd96b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nameservers", value)


@jsii.data_type(
    jsii_type="namecheap.domainRecords.DomainRecordsConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "domain": "domain",
        "email_type": "emailType",
        "id": "id",
        "mode": "mode",
        "nameservers": "nameservers",
        "record": "record",
    },
)
class DomainRecordsConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        domain: builtins.str,
        email_type: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        mode: typing.Optional[builtins.str] = None,
        nameservers: typing.Optional[typing.Sequence[builtins.str]] = None,
        record: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DomainRecordsRecord", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param domain: Purchased available domain name on your account. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/namecheap/namecheap/2.1.0/docs/resources/domain_records#domain DomainRecords#domain}
        :param email_type: Possible values: NONE, MXE, MX, FWD, OX, GMAIL. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/namecheap/namecheap/2.1.0/docs/resources/domain_records#email_type DomainRecords#email_type}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/namecheap/namecheap/2.1.0/docs/resources/domain_records#id DomainRecords#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param mode: Possible values: MERGE (default), OVERWRITE. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/namecheap/namecheap/2.1.0/docs/resources/domain_records#mode DomainRecords#mode}
        :param nameservers: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/namecheap/namecheap/2.1.0/docs/resources/domain_records#nameservers DomainRecords#nameservers}.
        :param record: record block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/namecheap/namecheap/2.1.0/docs/resources/domain_records#record DomainRecords#record}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b34344030379806aa3086d5ab494850e220590ceee86f5af83465926d15b3768)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
            check_type(argname="argument email_type", value=email_type, expected_type=type_hints["email_type"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument nameservers", value=nameservers, expected_type=type_hints["nameservers"])
            check_type(argname="argument record", value=record, expected_type=type_hints["record"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain": domain,
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
        if email_type is not None:
            self._values["email_type"] = email_type
        if id is not None:
            self._values["id"] = id
        if mode is not None:
            self._values["mode"] = mode
        if nameservers is not None:
            self._values["nameservers"] = nameservers
        if record is not None:
            self._values["record"] = record

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
    def domain(self) -> builtins.str:
        '''Purchased available domain name on your account.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/namecheap/namecheap/2.1.0/docs/resources/domain_records#domain DomainRecords#domain}
        '''
        result = self._values.get("domain")
        assert result is not None, "Required property 'domain' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def email_type(self) -> typing.Optional[builtins.str]:
        '''Possible values: NONE, MXE, MX, FWD, OX, GMAIL.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/namecheap/namecheap/2.1.0/docs/resources/domain_records#email_type DomainRecords#email_type}
        '''
        result = self._values.get("email_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/namecheap/namecheap/2.1.0/docs/resources/domain_records#id DomainRecords#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mode(self) -> typing.Optional[builtins.str]:
        '''Possible values: MERGE (default), OVERWRITE.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/namecheap/namecheap/2.1.0/docs/resources/domain_records#mode DomainRecords#mode}
        '''
        result = self._values.get("mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def nameservers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/namecheap/namecheap/2.1.0/docs/resources/domain_records#nameservers DomainRecords#nameservers}.'''
        result = self._values.get("nameservers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def record(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DomainRecordsRecord"]]]:
        '''record block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/namecheap/namecheap/2.1.0/docs/resources/domain_records#record DomainRecords#record}
        '''
        result = self._values.get("record")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DomainRecordsRecord"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DomainRecordsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="namecheap.domainRecords.DomainRecordsRecord",
    jsii_struct_bases=[],
    name_mapping={
        "address": "address",
        "hostname": "hostname",
        "type": "type",
        "mx_pref": "mxPref",
        "ttl": "ttl",
    },
)
class DomainRecordsRecord:
    def __init__(
        self,
        *,
        address: builtins.str,
        hostname: builtins.str,
        type: builtins.str,
        mx_pref: typing.Optional[jsii.Number] = None,
        ttl: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param address: Possible values are URL or IP address. The value for this parameter is based on record type. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/namecheap/namecheap/2.1.0/docs/resources/domain_records#address DomainRecords#address}
        :param hostname: Sub-domain/hostname to create the record for. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/namecheap/namecheap/2.1.0/docs/resources/domain_records#hostname DomainRecords#hostname}
        :param type: Possible values: A, AAAA, ALIAS, CAA, CNAME, MX, MXE, NS, TXT, URL, URL301, FRAME. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/namecheap/namecheap/2.1.0/docs/resources/domain_records#type DomainRecords#type}
        :param mx_pref: MX preference for host. Applicable for MX records only. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/namecheap/namecheap/2.1.0/docs/resources/domain_records#mx_pref DomainRecords#mx_pref}
        :param ttl: Time to live for all record types. Possible values: any value between 60 to 60000. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/namecheap/namecheap/2.1.0/docs/resources/domain_records#ttl DomainRecords#ttl}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a86a2c2de9e6dc6723130ba4921818ca9dc4a090b79f8fec182783c276e87b01)
            check_type(argname="argument address", value=address, expected_type=type_hints["address"])
            check_type(argname="argument hostname", value=hostname, expected_type=type_hints["hostname"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument mx_pref", value=mx_pref, expected_type=type_hints["mx_pref"])
            check_type(argname="argument ttl", value=ttl, expected_type=type_hints["ttl"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "address": address,
            "hostname": hostname,
            "type": type,
        }
        if mx_pref is not None:
            self._values["mx_pref"] = mx_pref
        if ttl is not None:
            self._values["ttl"] = ttl

    @builtins.property
    def address(self) -> builtins.str:
        '''Possible values are URL or IP address. The value for this parameter is based on record type.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/namecheap/namecheap/2.1.0/docs/resources/domain_records#address DomainRecords#address}
        '''
        result = self._values.get("address")
        assert result is not None, "Required property 'address' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def hostname(self) -> builtins.str:
        '''Sub-domain/hostname to create the record for.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/namecheap/namecheap/2.1.0/docs/resources/domain_records#hostname DomainRecords#hostname}
        '''
        result = self._values.get("hostname")
        assert result is not None, "Required property 'hostname' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Possible values: A, AAAA, ALIAS, CAA, CNAME, MX, MXE, NS, TXT, URL, URL301, FRAME.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/namecheap/namecheap/2.1.0/docs/resources/domain_records#type DomainRecords#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mx_pref(self) -> typing.Optional[jsii.Number]:
        '''MX preference for host. Applicable for MX records only.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/namecheap/namecheap/2.1.0/docs/resources/domain_records#mx_pref DomainRecords#mx_pref}
        '''
        result = self._values.get("mx_pref")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ttl(self) -> typing.Optional[jsii.Number]:
        '''Time to live for all record types. Possible values: any value between 60 to 60000.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/namecheap/namecheap/2.1.0/docs/resources/domain_records#ttl DomainRecords#ttl}
        '''
        result = self._values.get("ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DomainRecordsRecord(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DomainRecordsRecordList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="namecheap.domainRecords.DomainRecordsRecordList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__23e5b2f5c2d64f9cb91f94809e9e1762fb9ebf5f33b6fdaf94c7cfa3848f032e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DomainRecordsRecordOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b91f3b6263fbbe650595662ad47dfe1c6a62ab700e43556b437de182ba5ae27)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DomainRecordsRecordOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6722bced99bae94cd387a1d1ef8f5905d3ed5f3a58d7b010940ef27b00682d73)
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
            type_hints = typing.get_type_hints(_typecheckingstub__80bffe48bb5668f51c19b5230e09589dd7e48f14bd91670236368d1ae48d6eb2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__cf655be942fb22989bfbf94052f6f854a5aa944d63bf06f784e58ba3b2228e51)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DomainRecordsRecord]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DomainRecordsRecord]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DomainRecordsRecord]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15c105a62352b83f961ff7d5171ec39dc283b928b60d8004db5cd75b3e1f1a98)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DomainRecordsRecordOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="namecheap.domainRecords.DomainRecordsRecordOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2dc18c8561d13c91dc664e32fd97cd6db82666848828a109dcb0182efda6dcad)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetMxPref")
    def reset_mx_pref(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMxPref", []))

    @jsii.member(jsii_name="resetTtl")
    def reset_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTtl", []))

    @builtins.property
    @jsii.member(jsii_name="addressInput")
    def address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "addressInput"))

    @builtins.property
    @jsii.member(jsii_name="hostnameInput")
    def hostname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostnameInput"))

    @builtins.property
    @jsii.member(jsii_name="mxPrefInput")
    def mx_pref_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "mxPrefInput"))

    @builtins.property
    @jsii.member(jsii_name="ttlInput")
    def ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ttlInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="address")
    def address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "address"))

    @address.setter
    def address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56cf0268a707c13c91861ec3421856fdd10cd4f8d2ab3eca15a5c4fba70b9725)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "address", value)

    @builtins.property
    @jsii.member(jsii_name="hostname")
    def hostname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostname"))

    @hostname.setter
    def hostname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ebb6b8134dc3483f6f67082d00f81be649e579e31062ff1a6b7a4d1df0401c29)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostname", value)

    @builtins.property
    @jsii.member(jsii_name="mxPref")
    def mx_pref(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "mxPref"))

    @mx_pref.setter
    def mx_pref(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81685d924fde802744c41060f4f1fd110fc24695c2f7145f7a65586e5de13163)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mxPref", value)

    @builtins.property
    @jsii.member(jsii_name="ttl")
    def ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ttl"))

    @ttl.setter
    def ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90364dc9d895dbd2eaeed1f3eb153f09bc2575f742b3f259599ec13bf61bcbfa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ttl", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d04ca74190bfb976113df29b06ad404e6f5ef553a3d9272c13310f9c478b71c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DomainRecordsRecord]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DomainRecordsRecord]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DomainRecordsRecord]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04e3014aa80e6a75a923d177e3d41c02ed15a43aacc8dba064b6f4387ec1fa52)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DomainRecords",
    "DomainRecordsConfig",
    "DomainRecordsRecord",
    "DomainRecordsRecordList",
    "DomainRecordsRecordOutputReference",
]

publication.publish()

def _typecheckingstub__0b313967db773a536c66889272b80880720543e147e5b84201f4a8143bdead2a(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    domain: builtins.str,
    email_type: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    mode: typing.Optional[builtins.str] = None,
    nameservers: typing.Optional[typing.Sequence[builtins.str]] = None,
    record: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DomainRecordsRecord, typing.Dict[builtins.str, typing.Any]]]]] = None,
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

def _typecheckingstub__fe0674d0638597aaf2c35a88eb205405daf8f7e65b85a339ce779d73a06c9687(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94d43f757255215793d0ae9f9039f8d0e20c7404c0c4cac91ad1a23d28bb77a2(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DomainRecordsRecord, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b7cf27e1dc49be06e701d7b9bb2ab46cf813d47319bdab345ba5e1aa5561eb3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__746c5bf8b16a57f0e97c73bcb115b1ccebe8e2ef34dd54a77c52e5b5ba7bb535(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ece4d601106b831e442d86c8ab9fdee1584a4c44bb753243dda237163463732(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fca3ca9caba003addf698da52c96c7dbb84efb1d1e8f217cd7e57b7e68d3f026(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ffa74f4d91c5e03c88bb15e8756461a652a7f91ac4c1494dd90dcc41bdd96b9(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b34344030379806aa3086d5ab494850e220590ceee86f5af83465926d15b3768(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    domain: builtins.str,
    email_type: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    mode: typing.Optional[builtins.str] = None,
    nameservers: typing.Optional[typing.Sequence[builtins.str]] = None,
    record: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DomainRecordsRecord, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a86a2c2de9e6dc6723130ba4921818ca9dc4a090b79f8fec182783c276e87b01(
    *,
    address: builtins.str,
    hostname: builtins.str,
    type: builtins.str,
    mx_pref: typing.Optional[jsii.Number] = None,
    ttl: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23e5b2f5c2d64f9cb91f94809e9e1762fb9ebf5f33b6fdaf94c7cfa3848f032e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b91f3b6263fbbe650595662ad47dfe1c6a62ab700e43556b437de182ba5ae27(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6722bced99bae94cd387a1d1ef8f5905d3ed5f3a58d7b010940ef27b00682d73(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80bffe48bb5668f51c19b5230e09589dd7e48f14bd91670236368d1ae48d6eb2(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf655be942fb22989bfbf94052f6f854a5aa944d63bf06f784e58ba3b2228e51(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15c105a62352b83f961ff7d5171ec39dc283b928b60d8004db5cd75b3e1f1a98(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DomainRecordsRecord]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2dc18c8561d13c91dc664e32fd97cd6db82666848828a109dcb0182efda6dcad(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56cf0268a707c13c91861ec3421856fdd10cd4f8d2ab3eca15a5c4fba70b9725(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ebb6b8134dc3483f6f67082d00f81be649e579e31062ff1a6b7a4d1df0401c29(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81685d924fde802744c41060f4f1fd110fc24695c2f7145f7a65586e5de13163(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90364dc9d895dbd2eaeed1f3eb153f09bc2575f742b3f259599ec13bf61bcbfa(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d04ca74190bfb976113df29b06ad404e6f5ef553a3d9272c13310f9c478b71c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04e3014aa80e6a75a923d177e3d41c02ed15a43aacc8dba064b6f4387ec1fa52(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DomainRecordsRecord]],
) -> None:
    """Type checking stubs"""
    pass
