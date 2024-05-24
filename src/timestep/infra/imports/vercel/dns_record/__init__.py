'''
# `vercel_dns_record`

Refer to the Terraform Registory for docs: [`vercel_dns_record`](https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/dns_record).
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


class DnsRecord(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="vercel.dnsRecord.DnsRecord",
):
    '''Represents a {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/dns_record vercel_dns_record}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        domain: builtins.str,
        name: builtins.str,
        type: builtins.str,
        comment: typing.Optional[builtins.str] = None,
        mx_priority: typing.Optional[jsii.Number] = None,
        srv: typing.Optional[typing.Union["DnsRecordSrv", typing.Dict[builtins.str, typing.Any]]] = None,
        team_id: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[jsii.Number] = None,
        value: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/dns_record vercel_dns_record} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param domain: The domain name, or zone, that the DNS record should be created beneath. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/dns_record#domain DnsRecord#domain}
        :param name: The subdomain name of the record. This should be an empty string if the rercord is for the root domain. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/dns_record#name DnsRecord#name}
        :param type: The type of DNS record. Available types: ``A``, ``AAAA``, ``ALIAS``, ``CAA``, ``CNAME``, ``MX``, ``NS``, ``SRV``, ``TXT``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/dns_record#type DnsRecord#type}
        :param comment: A comment explaining what the DNS record is for. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/dns_record#comment DnsRecord#comment}
        :param mx_priority: The priority of the MX record. The priority specifies the sequence that an email server receives emails. A smaller value indicates a higher priority. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/dns_record#mx_priority DnsRecord#mx_priority}
        :param srv: Settings for an SRV record. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/dns_record#srv DnsRecord#srv}
        :param team_id: The team ID that the domain and DNS records belong to. Required when configuring a team resource if a default team has not been set in the provider. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/dns_record#team_id DnsRecord#team_id}
        :param ttl: The TTL value in seconds. Must be a number between 60 and 2147483647. If unspecified, it will default to 60 seconds. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/dns_record#ttl DnsRecord#ttl}
        :param value: The value of the DNS record. The format depends on the 'type' property. For an 'A' record, this should be a valid IPv4 address. For an 'AAAA' record, this should be an IPv6 address. For 'ALIAS' records, this should be a hostname. For 'CAA' records, this should specify specify which Certificate Authorities (CAs) are allowed to issue certificates for the domain. For 'CNAME' records, this should be a different domain name. For 'MX' records, this should specify the mail server responsible for accepting messages on behalf of the domain name. For 'TXT' records, this can contain arbitrary text. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/dns_record#value DnsRecord#value}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d3f29bdfc4c49b618d8103478b7ca672c5560ca2526d0ac1a2958c2955f36ba)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = DnsRecordConfig(
            domain=domain,
            name=name,
            type=type,
            comment=comment,
            mx_priority=mx_priority,
            srv=srv,
            team_id=team_id,
            ttl=ttl,
            value=value,
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
        '''Generates CDKTF code for importing a DnsRecord resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the DnsRecord to import.
        :param import_from_id: The id of the existing DnsRecord that should be imported. Refer to the {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/dns_record#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the DnsRecord to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1efc50c38f88a6efe939468d40d696e3eff6254df192f550c0ca9716b199b32e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putSrv")
    def put_srv(
        self,
        *,
        port: jsii.Number,
        priority: jsii.Number,
        target: builtins.str,
        weight: jsii.Number,
    ) -> None:
        '''
        :param port: The TCP or UDP port on which the service is to be found. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/dns_record#port DnsRecord#port}
        :param priority: The priority of the target host, lower value means more preferred. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/dns_record#priority DnsRecord#priority}
        :param target: The canonical hostname of the machine providing the service, ending in a dot. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/dns_record#target DnsRecord#target}
        :param weight: A relative weight for records with the same priority, higher value means higher chance of getting picked. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/dns_record#weight DnsRecord#weight}
        '''
        value = DnsRecordSrv(
            port=port, priority=priority, target=target, weight=weight
        )

        return typing.cast(None, jsii.invoke(self, "putSrv", [value]))

    @jsii.member(jsii_name="resetComment")
    def reset_comment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComment", []))

    @jsii.member(jsii_name="resetMxPriority")
    def reset_mx_priority(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMxPriority", []))

    @jsii.member(jsii_name="resetSrv")
    def reset_srv(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSrv", []))

    @jsii.member(jsii_name="resetTeamId")
    def reset_team_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTeamId", []))

    @jsii.member(jsii_name="resetTtl")
    def reset_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTtl", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

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
    @jsii.member(jsii_name="srv")
    def srv(self) -> "DnsRecordSrvOutputReference":
        return typing.cast("DnsRecordSrvOutputReference", jsii.get(self, "srv"))

    @builtins.property
    @jsii.member(jsii_name="commentInput")
    def comment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commentInput"))

    @builtins.property
    @jsii.member(jsii_name="domainInput")
    def domain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainInput"))

    @builtins.property
    @jsii.member(jsii_name="mxPriorityInput")
    def mx_priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "mxPriorityInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="srvInput")
    def srv_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, "DnsRecordSrv"]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, "DnsRecordSrv"]], jsii.get(self, "srvInput"))

    @builtins.property
    @jsii.member(jsii_name="teamIdInput")
    def team_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "teamIdInput"))

    @builtins.property
    @jsii.member(jsii_name="ttlInput")
    def ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ttlInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="comment")
    def comment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comment"))

    @comment.setter
    def comment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6414200c454cf166496dcb16cfb020a736aeadf65f78d7705c6f4888160f0d34)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comment", value)

    @builtins.property
    @jsii.member(jsii_name="domain")
    def domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domain"))

    @domain.setter
    def domain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__daa25df1fe2d8d3f383a57a043efdbc5e3f7ac4874056ecedb1a37cf2cb370d9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domain", value)

    @builtins.property
    @jsii.member(jsii_name="mxPriority")
    def mx_priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "mxPriority"))

    @mx_priority.setter
    def mx_priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd5e0921aaaa725ed833ca6e28ed28abbfb5a6b802be2d2ccdd42dd7ae823cc1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mxPriority", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18dff0f89431b9b9d75d1b54632d3e061d9411b4690880ae995080f278bad441)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="teamId")
    def team_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "teamId"))

    @team_id.setter
    def team_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13b3f7b2b15648146e5f1430b9b0cf9fe7031bd644df0cc615c99336d2e42396)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "teamId", value)

    @builtins.property
    @jsii.member(jsii_name="ttl")
    def ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ttl"))

    @ttl.setter
    def ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c564e26c4e05c6560f992e6e698f7fee6ed27ec805df91e2557f041ee5e2a39e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ttl", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ab52c0a71ef733bcf0f272af14a077e4608f56adf3080e02d5cef7fa9d7d03e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c1610dd82e7cf3c7d83f79b25725bccdc01acaac8d25b98b41ec5830a1ea5f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)


@jsii.data_type(
    jsii_type="vercel.dnsRecord.DnsRecordConfig",
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
        "name": "name",
        "type": "type",
        "comment": "comment",
        "mx_priority": "mxPriority",
        "srv": "srv",
        "team_id": "teamId",
        "ttl": "ttl",
        "value": "value",
    },
)
class DnsRecordConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        name: builtins.str,
        type: builtins.str,
        comment: typing.Optional[builtins.str] = None,
        mx_priority: typing.Optional[jsii.Number] = None,
        srv: typing.Optional[typing.Union["DnsRecordSrv", typing.Dict[builtins.str, typing.Any]]] = None,
        team_id: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[jsii.Number] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param domain: The domain name, or zone, that the DNS record should be created beneath. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/dns_record#domain DnsRecord#domain}
        :param name: The subdomain name of the record. This should be an empty string if the rercord is for the root domain. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/dns_record#name DnsRecord#name}
        :param type: The type of DNS record. Available types: ``A``, ``AAAA``, ``ALIAS``, ``CAA``, ``CNAME``, ``MX``, ``NS``, ``SRV``, ``TXT``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/dns_record#type DnsRecord#type}
        :param comment: A comment explaining what the DNS record is for. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/dns_record#comment DnsRecord#comment}
        :param mx_priority: The priority of the MX record. The priority specifies the sequence that an email server receives emails. A smaller value indicates a higher priority. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/dns_record#mx_priority DnsRecord#mx_priority}
        :param srv: Settings for an SRV record. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/dns_record#srv DnsRecord#srv}
        :param team_id: The team ID that the domain and DNS records belong to. Required when configuring a team resource if a default team has not been set in the provider. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/dns_record#team_id DnsRecord#team_id}
        :param ttl: The TTL value in seconds. Must be a number between 60 and 2147483647. If unspecified, it will default to 60 seconds. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/dns_record#ttl DnsRecord#ttl}
        :param value: The value of the DNS record. The format depends on the 'type' property. For an 'A' record, this should be a valid IPv4 address. For an 'AAAA' record, this should be an IPv6 address. For 'ALIAS' records, this should be a hostname. For 'CAA' records, this should specify specify which Certificate Authorities (CAs) are allowed to issue certificates for the domain. For 'CNAME' records, this should be a different domain name. For 'MX' records, this should specify the mail server responsible for accepting messages on behalf of the domain name. For 'TXT' records, this can contain arbitrary text. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/dns_record#value DnsRecord#value}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(srv, dict):
            srv = DnsRecordSrv(**srv)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1abc1349e12d930b7b4515fa36182b33ab3d458212ec0a6e29b30fc3a3c0986a)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument mx_priority", value=mx_priority, expected_type=type_hints["mx_priority"])
            check_type(argname="argument srv", value=srv, expected_type=type_hints["srv"])
            check_type(argname="argument team_id", value=team_id, expected_type=type_hints["team_id"])
            check_type(argname="argument ttl", value=ttl, expected_type=type_hints["ttl"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain": domain,
            "name": name,
            "type": type,
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
        if comment is not None:
            self._values["comment"] = comment
        if mx_priority is not None:
            self._values["mx_priority"] = mx_priority
        if srv is not None:
            self._values["srv"] = srv
        if team_id is not None:
            self._values["team_id"] = team_id
        if ttl is not None:
            self._values["ttl"] = ttl
        if value is not None:
            self._values["value"] = value

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
        '''The domain name, or zone, that the DNS record should be created beneath.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/dns_record#domain DnsRecord#domain}
        '''
        result = self._values.get("domain")
        assert result is not None, "Required property 'domain' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The subdomain name of the record.

        This should be an empty string if the rercord is for the root domain.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/dns_record#name DnsRecord#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of DNS record. Available types: ``A``, ``AAAA``, ``ALIAS``, ``CAA``, ``CNAME``, ``MX``, ``NS``, ``SRV``, ``TXT``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/dns_record#type DnsRecord#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''A comment explaining what the DNS record is for.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/dns_record#comment DnsRecord#comment}
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mx_priority(self) -> typing.Optional[jsii.Number]:
        '''The priority of the MX record.

        The priority specifies the sequence that an email server receives emails. A smaller value indicates a higher priority.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/dns_record#mx_priority DnsRecord#mx_priority}
        '''
        result = self._values.get("mx_priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def srv(self) -> typing.Optional["DnsRecordSrv"]:
        '''Settings for an SRV record.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/dns_record#srv DnsRecord#srv}
        '''
        result = self._values.get("srv")
        return typing.cast(typing.Optional["DnsRecordSrv"], result)

    @builtins.property
    def team_id(self) -> typing.Optional[builtins.str]:
        '''The team ID that the domain and DNS records belong to.

        Required when configuring a team resource if a default team has not been set in the provider.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/dns_record#team_id DnsRecord#team_id}
        '''
        result = self._values.get("team_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ttl(self) -> typing.Optional[jsii.Number]:
        '''The TTL value in seconds.

        Must be a number between 60 and 2147483647. If unspecified, it will default to 60 seconds.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/dns_record#ttl DnsRecord#ttl}
        '''
        result = self._values.get("ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''The value of the DNS record.

        The format depends on the 'type' property.
        For an 'A' record, this should be a valid IPv4 address.
        For an 'AAAA' record, this should be an IPv6 address.
        For 'ALIAS' records, this should be a hostname.
        For 'CAA' records, this should specify specify which Certificate Authorities (CAs) are allowed to issue certificates for the domain.
        For 'CNAME' records, this should be a different domain name.
        For 'MX' records, this should specify the mail server responsible for accepting messages on behalf of the domain name.
        For 'TXT' records, this can contain arbitrary text.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/dns_record#value DnsRecord#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DnsRecordConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vercel.dnsRecord.DnsRecordSrv",
    jsii_struct_bases=[],
    name_mapping={
        "port": "port",
        "priority": "priority",
        "target": "target",
        "weight": "weight",
    },
)
class DnsRecordSrv:
    def __init__(
        self,
        *,
        port: jsii.Number,
        priority: jsii.Number,
        target: builtins.str,
        weight: jsii.Number,
    ) -> None:
        '''
        :param port: The TCP or UDP port on which the service is to be found. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/dns_record#port DnsRecord#port}
        :param priority: The priority of the target host, lower value means more preferred. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/dns_record#priority DnsRecord#priority}
        :param target: The canonical hostname of the machine providing the service, ending in a dot. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/dns_record#target DnsRecord#target}
        :param weight: A relative weight for records with the same priority, higher value means higher chance of getting picked. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/dns_record#weight DnsRecord#weight}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8b9d7ca56969b6d908a1893c1a4b31b31fe84d1249d28d76a9648517ff1b53f)
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "port": port,
            "priority": priority,
            "target": target,
            "weight": weight,
        }

    @builtins.property
    def port(self) -> jsii.Number:
        '''The TCP or UDP port on which the service is to be found.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/dns_record#port DnsRecord#port}
        '''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def priority(self) -> jsii.Number:
        '''The priority of the target host, lower value means more preferred.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/dns_record#priority DnsRecord#priority}
        '''
        result = self._values.get("priority")
        assert result is not None, "Required property 'priority' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def target(self) -> builtins.str:
        '''The canonical hostname of the machine providing the service, ending in a dot.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/dns_record#target DnsRecord#target}
        '''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def weight(self) -> jsii.Number:
        '''A relative weight for records with the same priority, higher value means higher chance of getting picked.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/dns_record#weight DnsRecord#weight}
        '''
        result = self._values.get("weight")
        assert result is not None, "Required property 'weight' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DnsRecordSrv(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DnsRecordSrvOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="vercel.dnsRecord.DnsRecordSrvOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ef391bc8621dea57e33e2adc89a416678226fb22e73a3b7bb0efe3ba68e45f14)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="weightInput")
    def weight_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "weightInput"))

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d595477fc9bcaf3dcba34f3f3f9e46eb382120db7fcc2e353d55fd7376eeb30)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70c6e8de84c2742949b257e2b0beb632c8d117858bbdaca2e808f278793c07dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de57f7e60de27db426671129e04f7f199021480d47bcba8379512d24cd80d3ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="weight")
    def weight(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "weight"))

    @weight.setter
    def weight(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__617ae8f874eca81a3a23760958eeeb44bdac6fead032fd3ed03facdca30392f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weight", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DnsRecordSrv]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DnsRecordSrv]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DnsRecordSrv]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa5baed801d2b6bda32a20d3f4786d1e0498ecc252cfafc52f0171f7822f50ee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DnsRecord",
    "DnsRecordConfig",
    "DnsRecordSrv",
    "DnsRecordSrvOutputReference",
]

publication.publish()

def _typecheckingstub__2d3f29bdfc4c49b618d8103478b7ca672c5560ca2526d0ac1a2958c2955f36ba(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    domain: builtins.str,
    name: builtins.str,
    type: builtins.str,
    comment: typing.Optional[builtins.str] = None,
    mx_priority: typing.Optional[jsii.Number] = None,
    srv: typing.Optional[typing.Union[DnsRecordSrv, typing.Dict[builtins.str, typing.Any]]] = None,
    team_id: typing.Optional[builtins.str] = None,
    ttl: typing.Optional[jsii.Number] = None,
    value: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__1efc50c38f88a6efe939468d40d696e3eff6254df192f550c0ca9716b199b32e(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6414200c454cf166496dcb16cfb020a736aeadf65f78d7705c6f4888160f0d34(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__daa25df1fe2d8d3f383a57a043efdbc5e3f7ac4874056ecedb1a37cf2cb370d9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd5e0921aaaa725ed833ca6e28ed28abbfb5a6b802be2d2ccdd42dd7ae823cc1(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18dff0f89431b9b9d75d1b54632d3e061d9411b4690880ae995080f278bad441(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13b3f7b2b15648146e5f1430b9b0cf9fe7031bd644df0cc615c99336d2e42396(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c564e26c4e05c6560f992e6e698f7fee6ed27ec805df91e2557f041ee5e2a39e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ab52c0a71ef733bcf0f272af14a077e4608f56adf3080e02d5cef7fa9d7d03e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c1610dd82e7cf3c7d83f79b25725bccdc01acaac8d25b98b41ec5830a1ea5f8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1abc1349e12d930b7b4515fa36182b33ab3d458212ec0a6e29b30fc3a3c0986a(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    domain: builtins.str,
    name: builtins.str,
    type: builtins.str,
    comment: typing.Optional[builtins.str] = None,
    mx_priority: typing.Optional[jsii.Number] = None,
    srv: typing.Optional[typing.Union[DnsRecordSrv, typing.Dict[builtins.str, typing.Any]]] = None,
    team_id: typing.Optional[builtins.str] = None,
    ttl: typing.Optional[jsii.Number] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8b9d7ca56969b6d908a1893c1a4b31b31fe84d1249d28d76a9648517ff1b53f(
    *,
    port: jsii.Number,
    priority: jsii.Number,
    target: builtins.str,
    weight: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef391bc8621dea57e33e2adc89a416678226fb22e73a3b7bb0efe3ba68e45f14(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d595477fc9bcaf3dcba34f3f3f9e46eb382120db7fcc2e353d55fd7376eeb30(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70c6e8de84c2742949b257e2b0beb632c8d117858bbdaca2e808f278793c07dc(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de57f7e60de27db426671129e04f7f199021480d47bcba8379512d24cd80d3ec(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__617ae8f874eca81a3a23760958eeeb44bdac6fead032fd3ed03facdca30392f4(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa5baed801d2b6bda32a20d3f4786d1e0498ecc252cfafc52f0171f7822f50ee(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DnsRecordSrv]],
) -> None:
    """Type checking stubs"""
    pass
