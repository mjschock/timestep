'''
# `argocd_repository_certificate`

Refer to the Terraform Registory for docs: [`argocd_repository_certificate`](https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_certificate).
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


class RepositoryCertificate(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.repositoryCertificate.RepositoryCertificate",
):
    '''Represents a {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_certificate argocd_repository_certificate}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        https: typing.Optional[typing.Union["RepositoryCertificateHttps", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        ssh: typing.Optional[typing.Union["RepositoryCertificateSsh", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_certificate argocd_repository_certificate} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param https: https block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_certificate#https RepositoryCertificate#https}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_certificate#id RepositoryCertificate#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ssh: ssh block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_certificate#ssh RepositoryCertificate#ssh}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd8f8940733b6bf9ac81d0f86a74bb8e66b7b73ab5e339b0481170b5cfbdd10c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = RepositoryCertificateConfig(
            https=https,
            id=id,
            ssh=ssh,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putHttps")
    def put_https(self, *, cert_data: builtins.str, server_name: builtins.str) -> None:
        '''
        :param cert_data: The actual certificate data, dependent on the certificate type. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_certificate#cert_data RepositoryCertificate#cert_data}
        :param server_name: DNS name of the server this certificate is intended for. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_certificate#server_name RepositoryCertificate#server_name}
        '''
        value = RepositoryCertificateHttps(
            cert_data=cert_data, server_name=server_name
        )

        return typing.cast(None, jsii.invoke(self, "putHttps", [value]))

    @jsii.member(jsii_name="putSsh")
    def put_ssh(
        self,
        *,
        cert_data: builtins.str,
        cert_subtype: builtins.str,
        server_name: builtins.str,
    ) -> None:
        '''
        :param cert_data: The actual certificate data, dependent on the certificate type. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_certificate#cert_data RepositoryCertificate#cert_data}
        :param cert_subtype: The sub type of the cert, i.e. ``ssh-rsa``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_certificate#cert_subtype RepositoryCertificate#cert_subtype}
        :param server_name: DNS name of the server this certificate is intended for. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_certificate#server_name RepositoryCertificate#server_name}
        '''
        value = RepositoryCertificateSsh(
            cert_data=cert_data, cert_subtype=cert_subtype, server_name=server_name
        )

        return typing.cast(None, jsii.invoke(self, "putSsh", [value]))

    @jsii.member(jsii_name="resetHttps")
    def reset_https(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttps", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetSsh")
    def reset_ssh(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSsh", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="https")
    def https(self) -> "RepositoryCertificateHttpsOutputReference":
        return typing.cast("RepositoryCertificateHttpsOutputReference", jsii.get(self, "https"))

    @builtins.property
    @jsii.member(jsii_name="ssh")
    def ssh(self) -> "RepositoryCertificateSshOutputReference":
        return typing.cast("RepositoryCertificateSshOutputReference", jsii.get(self, "ssh"))

    @builtins.property
    @jsii.member(jsii_name="httpsInput")
    def https_input(self) -> typing.Optional["RepositoryCertificateHttps"]:
        return typing.cast(typing.Optional["RepositoryCertificateHttps"], jsii.get(self, "httpsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="sshInput")
    def ssh_input(self) -> typing.Optional["RepositoryCertificateSsh"]:
        return typing.cast(typing.Optional["RepositoryCertificateSsh"], jsii.get(self, "sshInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f91e639b4b024e2330ea3d4718d53270bbb4485c7056a549a99fe987b500cb28)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="argocd.repositoryCertificate.RepositoryCertificateConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "https": "https",
        "id": "id",
        "ssh": "ssh",
    },
)
class RepositoryCertificateConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        https: typing.Optional[typing.Union["RepositoryCertificateHttps", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        ssh: typing.Optional[typing.Union["RepositoryCertificateSsh", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param https: https block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_certificate#https RepositoryCertificate#https}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_certificate#id RepositoryCertificate#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ssh: ssh block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_certificate#ssh RepositoryCertificate#ssh}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(https, dict):
            https = RepositoryCertificateHttps(**https)
        if isinstance(ssh, dict):
            ssh = RepositoryCertificateSsh(**ssh)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b82e4d63877b1196c482f9bdb1d28ff75369c0286a8f1122a90cb3d4d9cd4d0)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument https", value=https, expected_type=type_hints["https"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument ssh", value=ssh, expected_type=type_hints["ssh"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
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
        if https is not None:
            self._values["https"] = https
        if id is not None:
            self._values["id"] = id
        if ssh is not None:
            self._values["ssh"] = ssh

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
    def https(self) -> typing.Optional["RepositoryCertificateHttps"]:
        '''https block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_certificate#https RepositoryCertificate#https}
        '''
        result = self._values.get("https")
        return typing.cast(typing.Optional["RepositoryCertificateHttps"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_certificate#id RepositoryCertificate#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ssh(self) -> typing.Optional["RepositoryCertificateSsh"]:
        '''ssh block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_certificate#ssh RepositoryCertificate#ssh}
        '''
        result = self._values.get("ssh")
        return typing.cast(typing.Optional["RepositoryCertificateSsh"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RepositoryCertificateConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="argocd.repositoryCertificate.RepositoryCertificateHttps",
    jsii_struct_bases=[],
    name_mapping={"cert_data": "certData", "server_name": "serverName"},
)
class RepositoryCertificateHttps:
    def __init__(self, *, cert_data: builtins.str, server_name: builtins.str) -> None:
        '''
        :param cert_data: The actual certificate data, dependent on the certificate type. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_certificate#cert_data RepositoryCertificate#cert_data}
        :param server_name: DNS name of the server this certificate is intended for. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_certificate#server_name RepositoryCertificate#server_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a78893448fb1a67ce2a1823a0602d3c6ed8c5205d3201169d7bc6d482cf4a180)
            check_type(argname="argument cert_data", value=cert_data, expected_type=type_hints["cert_data"])
            check_type(argname="argument server_name", value=server_name, expected_type=type_hints["server_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cert_data": cert_data,
            "server_name": server_name,
        }

    @builtins.property
    def cert_data(self) -> builtins.str:
        '''The actual certificate data, dependent on the certificate type.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_certificate#cert_data RepositoryCertificate#cert_data}
        '''
        result = self._values.get("cert_data")
        assert result is not None, "Required property 'cert_data' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def server_name(self) -> builtins.str:
        '''DNS name of the server this certificate is intended for.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_certificate#server_name RepositoryCertificate#server_name}
        '''
        result = self._values.get("server_name")
        assert result is not None, "Required property 'server_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RepositoryCertificateHttps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RepositoryCertificateHttpsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.repositoryCertificate.RepositoryCertificateHttpsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9c8ebb7801301b2f030d2a3bb5bb2de9931087f96f488755e31cdcf771ef2755)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="certInfo")
    def cert_info(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certInfo"))

    @builtins.property
    @jsii.member(jsii_name="certSubtype")
    def cert_subtype(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certSubtype"))

    @builtins.property
    @jsii.member(jsii_name="certDataInput")
    def cert_data_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certDataInput"))

    @builtins.property
    @jsii.member(jsii_name="serverNameInput")
    def server_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverNameInput"))

    @builtins.property
    @jsii.member(jsii_name="certData")
    def cert_data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certData"))

    @cert_data.setter
    def cert_data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9bc3cb8dc26bb0ec2e883c7a3a2f6b444abc0ca7718490a9eb34e435a680dac4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certData", value)

    @builtins.property
    @jsii.member(jsii_name="serverName")
    def server_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serverName"))

    @server_name.setter
    def server_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e70f3c5eca23e69dc03ed3cf675087c0a047e14704a801c5b73c77bd4368147)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[RepositoryCertificateHttps]:
        return typing.cast(typing.Optional[RepositoryCertificateHttps], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[RepositoryCertificateHttps],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01dcff62265c78905809cea7a4f3e56b8558a1653bdb84afd7fd528274e7015f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="argocd.repositoryCertificate.RepositoryCertificateSsh",
    jsii_struct_bases=[],
    name_mapping={
        "cert_data": "certData",
        "cert_subtype": "certSubtype",
        "server_name": "serverName",
    },
)
class RepositoryCertificateSsh:
    def __init__(
        self,
        *,
        cert_data: builtins.str,
        cert_subtype: builtins.str,
        server_name: builtins.str,
    ) -> None:
        '''
        :param cert_data: The actual certificate data, dependent on the certificate type. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_certificate#cert_data RepositoryCertificate#cert_data}
        :param cert_subtype: The sub type of the cert, i.e. ``ssh-rsa``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_certificate#cert_subtype RepositoryCertificate#cert_subtype}
        :param server_name: DNS name of the server this certificate is intended for. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_certificate#server_name RepositoryCertificate#server_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9946a55c10d47b438b4f9b6daea41349331957094d221ab239bc0433ccab9a5)
            check_type(argname="argument cert_data", value=cert_data, expected_type=type_hints["cert_data"])
            check_type(argname="argument cert_subtype", value=cert_subtype, expected_type=type_hints["cert_subtype"])
            check_type(argname="argument server_name", value=server_name, expected_type=type_hints["server_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cert_data": cert_data,
            "cert_subtype": cert_subtype,
            "server_name": server_name,
        }

    @builtins.property
    def cert_data(self) -> builtins.str:
        '''The actual certificate data, dependent on the certificate type.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_certificate#cert_data RepositoryCertificate#cert_data}
        '''
        result = self._values.get("cert_data")
        assert result is not None, "Required property 'cert_data' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cert_subtype(self) -> builtins.str:
        '''The sub type of the cert, i.e. ``ssh-rsa``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_certificate#cert_subtype RepositoryCertificate#cert_subtype}
        '''
        result = self._values.get("cert_subtype")
        assert result is not None, "Required property 'cert_subtype' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def server_name(self) -> builtins.str:
        '''DNS name of the server this certificate is intended for.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_certificate#server_name RepositoryCertificate#server_name}
        '''
        result = self._values.get("server_name")
        assert result is not None, "Required property 'server_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RepositoryCertificateSsh(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RepositoryCertificateSshOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.repositoryCertificate.RepositoryCertificateSshOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9e3e12a659819ca8c4f3f36b8ae0e24db6af671ed7c35853ac3aa7b6688f830a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="certInfo")
    def cert_info(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certInfo"))

    @builtins.property
    @jsii.member(jsii_name="certDataInput")
    def cert_data_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certDataInput"))

    @builtins.property
    @jsii.member(jsii_name="certSubtypeInput")
    def cert_subtype_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certSubtypeInput"))

    @builtins.property
    @jsii.member(jsii_name="serverNameInput")
    def server_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverNameInput"))

    @builtins.property
    @jsii.member(jsii_name="certData")
    def cert_data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certData"))

    @cert_data.setter
    def cert_data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4538e360e574fba54c19dc0b3c0e23ce2deafd405c522420c7328a9fadf79846)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certData", value)

    @builtins.property
    @jsii.member(jsii_name="certSubtype")
    def cert_subtype(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certSubtype"))

    @cert_subtype.setter
    def cert_subtype(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc8ce276cbc6bc9e4088a7b9bb7cd315dbbf0911e589740f8a789eded372d24d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certSubtype", value)

    @builtins.property
    @jsii.member(jsii_name="serverName")
    def server_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serverName"))

    @server_name.setter
    def server_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec0516975e66fae329473d293e681bc818ac4ef8c858b3fb8cd31478ec470feb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[RepositoryCertificateSsh]:
        return typing.cast(typing.Optional[RepositoryCertificateSsh], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[RepositoryCertificateSsh]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9af772b612c6d6ced3fe2a1677d9f0bca615ab1a222f9af19b93bf8d82bb3fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "RepositoryCertificate",
    "RepositoryCertificateConfig",
    "RepositoryCertificateHttps",
    "RepositoryCertificateHttpsOutputReference",
    "RepositoryCertificateSsh",
    "RepositoryCertificateSshOutputReference",
]

publication.publish()

def _typecheckingstub__fd8f8940733b6bf9ac81d0f86a74bb8e66b7b73ab5e339b0481170b5cfbdd10c(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    https: typing.Optional[typing.Union[RepositoryCertificateHttps, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    ssh: typing.Optional[typing.Union[RepositoryCertificateSsh, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__f91e639b4b024e2330ea3d4718d53270bbb4485c7056a549a99fe987b500cb28(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b82e4d63877b1196c482f9bdb1d28ff75369c0286a8f1122a90cb3d4d9cd4d0(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    https: typing.Optional[typing.Union[RepositoryCertificateHttps, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    ssh: typing.Optional[typing.Union[RepositoryCertificateSsh, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a78893448fb1a67ce2a1823a0602d3c6ed8c5205d3201169d7bc6d482cf4a180(
    *,
    cert_data: builtins.str,
    server_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c8ebb7801301b2f030d2a3bb5bb2de9931087f96f488755e31cdcf771ef2755(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bc3cb8dc26bb0ec2e883c7a3a2f6b444abc0ca7718490a9eb34e435a680dac4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e70f3c5eca23e69dc03ed3cf675087c0a047e14704a801c5b73c77bd4368147(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01dcff62265c78905809cea7a4f3e56b8558a1653bdb84afd7fd528274e7015f(
    value: typing.Optional[RepositoryCertificateHttps],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9946a55c10d47b438b4f9b6daea41349331957094d221ab239bc0433ccab9a5(
    *,
    cert_data: builtins.str,
    cert_subtype: builtins.str,
    server_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e3e12a659819ca8c4f3f36b8ae0e24db6af671ed7c35853ac3aa7b6688f830a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4538e360e574fba54c19dc0b3c0e23ce2deafd405c522420c7328a9fadf79846(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc8ce276cbc6bc9e4088a7b9bb7cd315dbbf0911e589740f8a789eded372d24d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec0516975e66fae329473d293e681bc818ac4ef8c858b3fb8cd31478ec470feb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9af772b612c6d6ced3fe2a1677d9f0bca615ab1a222f9af19b93bf8d82bb3fa(
    value: typing.Optional[RepositoryCertificateSsh],
) -> None:
    """Type checking stubs"""
    pass
