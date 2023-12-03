'''
# `argocd_repository_credentials`

Refer to the Terraform Registory for docs: [`argocd_repository_credentials`](https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_credentials).
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


class RepositoryCredentials(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.repositoryCredentials.RepositoryCredentials",
):
    '''Represents a {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_credentials argocd_repository_credentials}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        url: builtins.str,
        enable_oci: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        githubapp_enterprise_base_url: typing.Optional[builtins.str] = None,
        githubapp_id: typing.Optional[builtins.str] = None,
        githubapp_installation_id: typing.Optional[builtins.str] = None,
        githubapp_private_key: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        ssh_private_key: typing.Optional[builtins.str] = None,
        tls_client_cert_data: typing.Optional[builtins.str] = None,
        tls_client_cert_key: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_credentials argocd_repository_credentials} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param url: URL that these credentials matches to. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_credentials#url RepositoryCredentials#url}
        :param enable_oci: Whether ``helm-oci`` support should be enabled for this repo. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_credentials#enable_oci RepositoryCredentials#enable_oci}
        :param githubapp_enterprise_base_url: GitHub API URL for GitHub app authentication. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_credentials#githubapp_enterprise_base_url RepositoryCredentials#githubapp_enterprise_base_url}
        :param githubapp_id: Github App ID of the app used to access the repo for GitHub app authentication. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_credentials#githubapp_id RepositoryCredentials#githubapp_id}
        :param githubapp_installation_id: ID of the installed GitHub App for GitHub app authentication. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_credentials#githubapp_installation_id RepositoryCredentials#githubapp_installation_id}
        :param githubapp_private_key: Private key data (PEM) for authentication via GitHub app. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_credentials#githubapp_private_key RepositoryCredentials#githubapp_private_key}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_credentials#id RepositoryCredentials#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param password: Password for authenticating at the repo server. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_credentials#password RepositoryCredentials#password}
        :param ssh_private_key: Private key data for authenticating at the repo server using SSH (only Git repos). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_credentials#ssh_private_key RepositoryCredentials#ssh_private_key}
        :param tls_client_cert_data: TLS client cert data for authenticating at the repo server. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_credentials#tls_client_cert_data RepositoryCredentials#tls_client_cert_data}
        :param tls_client_cert_key: TLS client cert key for authenticating at the repo server. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_credentials#tls_client_cert_key RepositoryCredentials#tls_client_cert_key}
        :param username: Username for authenticating at the repo server. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_credentials#username RepositoryCredentials#username}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0267d6d72972534089404e6476947ab78f4667c368586d376a48fb2ca5368ef4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = RepositoryCredentialsConfig(
            url=url,
            enable_oci=enable_oci,
            githubapp_enterprise_base_url=githubapp_enterprise_base_url,
            githubapp_id=githubapp_id,
            githubapp_installation_id=githubapp_installation_id,
            githubapp_private_key=githubapp_private_key,
            id=id,
            password=password,
            ssh_private_key=ssh_private_key,
            tls_client_cert_data=tls_client_cert_data,
            tls_client_cert_key=tls_client_cert_key,
            username=username,
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
        '''Generates CDKTF code for importing a RepositoryCredentials resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the RepositoryCredentials to import.
        :param import_from_id: The id of the existing RepositoryCredentials that should be imported. Refer to the {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_credentials#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the RepositoryCredentials to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d6528b3663ea9b4ede3e98cc1d4c1219b00e4e7e4483a7b149a2b248f5c4d33)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="resetEnableOci")
    def reset_enable_oci(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableOci", []))

    @jsii.member(jsii_name="resetGithubappEnterpriseBaseUrl")
    def reset_githubapp_enterprise_base_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGithubappEnterpriseBaseUrl", []))

    @jsii.member(jsii_name="resetGithubappId")
    def reset_githubapp_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGithubappId", []))

    @jsii.member(jsii_name="resetGithubappInstallationId")
    def reset_githubapp_installation_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGithubappInstallationId", []))

    @jsii.member(jsii_name="resetGithubappPrivateKey")
    def reset_githubapp_private_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGithubappPrivateKey", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetSshPrivateKey")
    def reset_ssh_private_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSshPrivateKey", []))

    @jsii.member(jsii_name="resetTlsClientCertData")
    def reset_tls_client_cert_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTlsClientCertData", []))

    @jsii.member(jsii_name="resetTlsClientCertKey")
    def reset_tls_client_cert_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTlsClientCertKey", []))

    @jsii.member(jsii_name="resetUsername")
    def reset_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsername", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="enableOciInput")
    def enable_oci_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableOciInput"))

    @builtins.property
    @jsii.member(jsii_name="githubappEnterpriseBaseUrlInput")
    def githubapp_enterprise_base_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "githubappEnterpriseBaseUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="githubappIdInput")
    def githubapp_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "githubappIdInput"))

    @builtins.property
    @jsii.member(jsii_name="githubappInstallationIdInput")
    def githubapp_installation_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "githubappInstallationIdInput"))

    @builtins.property
    @jsii.member(jsii_name="githubappPrivateKeyInput")
    def githubapp_private_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "githubappPrivateKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="sshPrivateKeyInput")
    def ssh_private_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sshPrivateKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsClientCertDataInput")
    def tls_client_cert_data_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tlsClientCertDataInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsClientCertKeyInput")
    def tls_client_cert_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tlsClientCertKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="enableOci")
    def enable_oci(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableOci"))

    @enable_oci.setter
    def enable_oci(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5469d3bab591acdbf6c44423b71c7c11323c7c58317c858c3ffabe42dce8211e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableOci", value)

    @builtins.property
    @jsii.member(jsii_name="githubappEnterpriseBaseUrl")
    def githubapp_enterprise_base_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "githubappEnterpriseBaseUrl"))

    @githubapp_enterprise_base_url.setter
    def githubapp_enterprise_base_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68c02861aeb8dda13844e5a7b3233ed0d3fe8a4e695004852fc99011120ba773)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "githubappEnterpriseBaseUrl", value)

    @builtins.property
    @jsii.member(jsii_name="githubappId")
    def githubapp_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "githubappId"))

    @githubapp_id.setter
    def githubapp_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fde9a27d0906991a26c91cca865bdb63cb7349e06e43a0399238081275d61c9c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "githubappId", value)

    @builtins.property
    @jsii.member(jsii_name="githubappInstallationId")
    def githubapp_installation_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "githubappInstallationId"))

    @githubapp_installation_id.setter
    def githubapp_installation_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4b5edf9793671966c60abbdce5b0cead369bb601f9da8a4baccc831949b7003)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "githubappInstallationId", value)

    @builtins.property
    @jsii.member(jsii_name="githubappPrivateKey")
    def githubapp_private_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "githubappPrivateKey"))

    @githubapp_private_key.setter
    def githubapp_private_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6838a57e6799588f4df7159c16d207a4cb4870be7fa40f0059eb611ca380978)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "githubappPrivateKey", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73efb0ff461e2616a4443b7b00fc4b602a04c0d70dcf7ab1a2a34865d7a106cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1df75e46e50235ce8691746a56372100f35524e3b93eadad4085182864dcf434)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="sshPrivateKey")
    def ssh_private_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sshPrivateKey"))

    @ssh_private_key.setter
    def ssh_private_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13db93eb2ba1d538c6aa9327d025d1bc2192204e0bc22fcfdbebbaf91d17c8e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sshPrivateKey", value)

    @builtins.property
    @jsii.member(jsii_name="tlsClientCertData")
    def tls_client_cert_data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tlsClientCertData"))

    @tls_client_cert_data.setter
    def tls_client_cert_data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__013a5290ee9565d27b1d32bd27f47331e3b92ede1c16f387eb396c8212d81159)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tlsClientCertData", value)

    @builtins.property
    @jsii.member(jsii_name="tlsClientCertKey")
    def tls_client_cert_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tlsClientCertKey"))

    @tls_client_cert_key.setter
    def tls_client_cert_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52d362904056fe0a85851e8304c9f0a21f50ac04b2d24b558a9ec0c344f65615)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tlsClientCertKey", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b07dbed897e6f48acf06855994aa4836c2681c71d80050fdd84688f033b53dd3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c3b9e2cb15e2ab8a356052ecc7de25e2a361163b64bb4a763939905a9a3c2a3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)


@jsii.data_type(
    jsii_type="argocd.repositoryCredentials.RepositoryCredentialsConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "url": "url",
        "enable_oci": "enableOci",
        "githubapp_enterprise_base_url": "githubappEnterpriseBaseUrl",
        "githubapp_id": "githubappId",
        "githubapp_installation_id": "githubappInstallationId",
        "githubapp_private_key": "githubappPrivateKey",
        "id": "id",
        "password": "password",
        "ssh_private_key": "sshPrivateKey",
        "tls_client_cert_data": "tlsClientCertData",
        "tls_client_cert_key": "tlsClientCertKey",
        "username": "username",
    },
)
class RepositoryCredentialsConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        url: builtins.str,
        enable_oci: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        githubapp_enterprise_base_url: typing.Optional[builtins.str] = None,
        githubapp_id: typing.Optional[builtins.str] = None,
        githubapp_installation_id: typing.Optional[builtins.str] = None,
        githubapp_private_key: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        ssh_private_key: typing.Optional[builtins.str] = None,
        tls_client_cert_data: typing.Optional[builtins.str] = None,
        tls_client_cert_key: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param url: URL that these credentials matches to. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_credentials#url RepositoryCredentials#url}
        :param enable_oci: Whether ``helm-oci`` support should be enabled for this repo. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_credentials#enable_oci RepositoryCredentials#enable_oci}
        :param githubapp_enterprise_base_url: GitHub API URL for GitHub app authentication. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_credentials#githubapp_enterprise_base_url RepositoryCredentials#githubapp_enterprise_base_url}
        :param githubapp_id: Github App ID of the app used to access the repo for GitHub app authentication. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_credentials#githubapp_id RepositoryCredentials#githubapp_id}
        :param githubapp_installation_id: ID of the installed GitHub App for GitHub app authentication. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_credentials#githubapp_installation_id RepositoryCredentials#githubapp_installation_id}
        :param githubapp_private_key: Private key data (PEM) for authentication via GitHub app. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_credentials#githubapp_private_key RepositoryCredentials#githubapp_private_key}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_credentials#id RepositoryCredentials#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param password: Password for authenticating at the repo server. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_credentials#password RepositoryCredentials#password}
        :param ssh_private_key: Private key data for authenticating at the repo server using SSH (only Git repos). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_credentials#ssh_private_key RepositoryCredentials#ssh_private_key}
        :param tls_client_cert_data: TLS client cert data for authenticating at the repo server. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_credentials#tls_client_cert_data RepositoryCredentials#tls_client_cert_data}
        :param tls_client_cert_key: TLS client cert key for authenticating at the repo server. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_credentials#tls_client_cert_key RepositoryCredentials#tls_client_cert_key}
        :param username: Username for authenticating at the repo server. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_credentials#username RepositoryCredentials#username}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6d32713b1f1ef328ae65e46104e0db99378891f52671d78b616b8f02bc7aea9)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument enable_oci", value=enable_oci, expected_type=type_hints["enable_oci"])
            check_type(argname="argument githubapp_enterprise_base_url", value=githubapp_enterprise_base_url, expected_type=type_hints["githubapp_enterprise_base_url"])
            check_type(argname="argument githubapp_id", value=githubapp_id, expected_type=type_hints["githubapp_id"])
            check_type(argname="argument githubapp_installation_id", value=githubapp_installation_id, expected_type=type_hints["githubapp_installation_id"])
            check_type(argname="argument githubapp_private_key", value=githubapp_private_key, expected_type=type_hints["githubapp_private_key"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument ssh_private_key", value=ssh_private_key, expected_type=type_hints["ssh_private_key"])
            check_type(argname="argument tls_client_cert_data", value=tls_client_cert_data, expected_type=type_hints["tls_client_cert_data"])
            check_type(argname="argument tls_client_cert_key", value=tls_client_cert_key, expected_type=type_hints["tls_client_cert_key"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "url": url,
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
        if enable_oci is not None:
            self._values["enable_oci"] = enable_oci
        if githubapp_enterprise_base_url is not None:
            self._values["githubapp_enterprise_base_url"] = githubapp_enterprise_base_url
        if githubapp_id is not None:
            self._values["githubapp_id"] = githubapp_id
        if githubapp_installation_id is not None:
            self._values["githubapp_installation_id"] = githubapp_installation_id
        if githubapp_private_key is not None:
            self._values["githubapp_private_key"] = githubapp_private_key
        if id is not None:
            self._values["id"] = id
        if password is not None:
            self._values["password"] = password
        if ssh_private_key is not None:
            self._values["ssh_private_key"] = ssh_private_key
        if tls_client_cert_data is not None:
            self._values["tls_client_cert_data"] = tls_client_cert_data
        if tls_client_cert_key is not None:
            self._values["tls_client_cert_key"] = tls_client_cert_key
        if username is not None:
            self._values["username"] = username

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
    def url(self) -> builtins.str:
        '''URL that these credentials matches to.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_credentials#url RepositoryCredentials#url}
        '''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enable_oci(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether ``helm-oci`` support should be enabled for this repo.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_credentials#enable_oci RepositoryCredentials#enable_oci}
        '''
        result = self._values.get("enable_oci")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def githubapp_enterprise_base_url(self) -> typing.Optional[builtins.str]:
        '''GitHub API URL for GitHub app authentication.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_credentials#githubapp_enterprise_base_url RepositoryCredentials#githubapp_enterprise_base_url}
        '''
        result = self._values.get("githubapp_enterprise_base_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def githubapp_id(self) -> typing.Optional[builtins.str]:
        '''Github App ID of the app used to access the repo for GitHub app authentication.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_credentials#githubapp_id RepositoryCredentials#githubapp_id}
        '''
        result = self._values.get("githubapp_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def githubapp_installation_id(self) -> typing.Optional[builtins.str]:
        '''ID of the installed GitHub App for GitHub app authentication.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_credentials#githubapp_installation_id RepositoryCredentials#githubapp_installation_id}
        '''
        result = self._values.get("githubapp_installation_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def githubapp_private_key(self) -> typing.Optional[builtins.str]:
        '''Private key data (PEM) for authentication via GitHub app.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_credentials#githubapp_private_key RepositoryCredentials#githubapp_private_key}
        '''
        result = self._values.get("githubapp_private_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_credentials#id RepositoryCredentials#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''Password for authenticating at the repo server.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_credentials#password RepositoryCredentials#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ssh_private_key(self) -> typing.Optional[builtins.str]:
        '''Private key data for authenticating at the repo server using SSH (only Git repos).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_credentials#ssh_private_key RepositoryCredentials#ssh_private_key}
        '''
        result = self._values.get("ssh_private_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tls_client_cert_data(self) -> typing.Optional[builtins.str]:
        '''TLS client cert data for authenticating at the repo server.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_credentials#tls_client_cert_data RepositoryCredentials#tls_client_cert_data}
        '''
        result = self._values.get("tls_client_cert_data")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tls_client_cert_key(self) -> typing.Optional[builtins.str]:
        '''TLS client cert key for authenticating at the repo server.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_credentials#tls_client_cert_key RepositoryCredentials#tls_client_cert_key}
        '''
        result = self._values.get("tls_client_cert_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''Username for authenticating at the repo server.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository_credentials#username RepositoryCredentials#username}
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RepositoryCredentialsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "RepositoryCredentials",
    "RepositoryCredentialsConfig",
]

publication.publish()

def _typecheckingstub__0267d6d72972534089404e6476947ab78f4667c368586d376a48fb2ca5368ef4(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    url: builtins.str,
    enable_oci: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    githubapp_enterprise_base_url: typing.Optional[builtins.str] = None,
    githubapp_id: typing.Optional[builtins.str] = None,
    githubapp_installation_id: typing.Optional[builtins.str] = None,
    githubapp_private_key: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    password: typing.Optional[builtins.str] = None,
    ssh_private_key: typing.Optional[builtins.str] = None,
    tls_client_cert_data: typing.Optional[builtins.str] = None,
    tls_client_cert_key: typing.Optional[builtins.str] = None,
    username: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__3d6528b3663ea9b4ede3e98cc1d4c1219b00e4e7e4483a7b149a2b248f5c4d33(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5469d3bab591acdbf6c44423b71c7c11323c7c58317c858c3ffabe42dce8211e(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68c02861aeb8dda13844e5a7b3233ed0d3fe8a4e695004852fc99011120ba773(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fde9a27d0906991a26c91cca865bdb63cb7349e06e43a0399238081275d61c9c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4b5edf9793671966c60abbdce5b0cead369bb601f9da8a4baccc831949b7003(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6838a57e6799588f4df7159c16d207a4cb4870be7fa40f0059eb611ca380978(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73efb0ff461e2616a4443b7b00fc4b602a04c0d70dcf7ab1a2a34865d7a106cf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1df75e46e50235ce8691746a56372100f35524e3b93eadad4085182864dcf434(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13db93eb2ba1d538c6aa9327d025d1bc2192204e0bc22fcfdbebbaf91d17c8e1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__013a5290ee9565d27b1d32bd27f47331e3b92ede1c16f387eb396c8212d81159(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52d362904056fe0a85851e8304c9f0a21f50ac04b2d24b558a9ec0c344f65615(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b07dbed897e6f48acf06855994aa4836c2681c71d80050fdd84688f033b53dd3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c3b9e2cb15e2ab8a356052ecc7de25e2a361163b64bb4a763939905a9a3c2a3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6d32713b1f1ef328ae65e46104e0db99378891f52671d78b616b8f02bc7aea9(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    url: builtins.str,
    enable_oci: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    githubapp_enterprise_base_url: typing.Optional[builtins.str] = None,
    githubapp_id: typing.Optional[builtins.str] = None,
    githubapp_installation_id: typing.Optional[builtins.str] = None,
    githubapp_private_key: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    password: typing.Optional[builtins.str] = None,
    ssh_private_key: typing.Optional[builtins.str] = None,
    tls_client_cert_data: typing.Optional[builtins.str] = None,
    tls_client_cert_key: typing.Optional[builtins.str] = None,
    username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
