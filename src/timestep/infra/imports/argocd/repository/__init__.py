'''
# `argocd_repository`

Refer to the Terraform Registory for docs: [`argocd_repository`](https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository).
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


class Repository(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.repository.Repository",
):
    '''Represents a {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository argocd_repository}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        repo: builtins.str,
        enable_lfs: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_oci: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        githubapp_enterprise_base_url: typing.Optional[builtins.str] = None,
        githubapp_id: typing.Optional[builtins.str] = None,
        githubapp_installation_id: typing.Optional[builtins.str] = None,
        githubapp_private_key: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        insecure: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        ssh_private_key: typing.Optional[builtins.str] = None,
        tls_client_cert_data: typing.Optional[builtins.str] = None,
        tls_client_cert_key: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository argocd_repository} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param repo: URL of the repository. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository#repo Repository#repo}
        :param enable_lfs: Whether ``git-lfs`` support should be enabled for this repository. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository#enable_lfs Repository#enable_lfs}
        :param enable_oci: Whether ``helm-oci`` support should be enabled for this repository. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository#enable_oci Repository#enable_oci}
        :param githubapp_enterprise_base_url: GitHub API URL for GitHub app authentication. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository#githubapp_enterprise_base_url Repository#githubapp_enterprise_base_url}
        :param githubapp_id: ID of the GitHub app used to access the repo. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository#githubapp_id Repository#githubapp_id}
        :param githubapp_installation_id: The installation ID of the GitHub App used to access the repo. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository#githubapp_installation_id Repository#githubapp_installation_id}
        :param githubapp_private_key: Private key data (PEM) for authentication via GitHub app. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository#githubapp_private_key Repository#githubapp_private_key}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository#id Repository#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param insecure: Whether the connection to the repository ignores any errors when verifying TLS certificates or SSH host keys. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository#insecure Repository#insecure}
        :param name: Name to be used for this repo. Only used with Helm repos. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository#name Repository#name}
        :param password: Password or PAT used for authenticating at the remote repository. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository#password Repository#password}
        :param project: The project name, in case the repository is project scoped. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository#project Repository#project}
        :param ssh_private_key: PEM data for authenticating at the repo server. Only used with Git repos. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository#ssh_private_key Repository#ssh_private_key}
        :param tls_client_cert_data: TLS client certificate in PEM format for authenticating at the repo server. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository#tls_client_cert_data Repository#tls_client_cert_data}
        :param tls_client_cert_key: TLS client certificate private key in PEM format for authenticating at the repo server. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository#tls_client_cert_key Repository#tls_client_cert_key}
        :param type: Type of the repo. Can be either ``git`` or ``helm``. ``git`` is assumed if empty or absent. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository#type Repository#type}
        :param username: Username used for authenticating at the remote repository. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository#username Repository#username}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d336db88e9c6bd05bb9bb7fc5259ea874f4e539aa5f7ab04374c561d07a630eb)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = RepositoryConfig(
            repo=repo,
            enable_lfs=enable_lfs,
            enable_oci=enable_oci,
            githubapp_enterprise_base_url=githubapp_enterprise_base_url,
            githubapp_id=githubapp_id,
            githubapp_installation_id=githubapp_installation_id,
            githubapp_private_key=githubapp_private_key,
            id=id,
            insecure=insecure,
            name=name,
            password=password,
            project=project,
            ssh_private_key=ssh_private_key,
            tls_client_cert_data=tls_client_cert_data,
            tls_client_cert_key=tls_client_cert_key,
            type=type,
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

    @jsii.member(jsii_name="resetEnableLfs")
    def reset_enable_lfs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableLfs", []))

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

    @jsii.member(jsii_name="resetInsecure")
    def reset_insecure(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInsecure", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetSshPrivateKey")
    def reset_ssh_private_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSshPrivateKey", []))

    @jsii.member(jsii_name="resetTlsClientCertData")
    def reset_tls_client_cert_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTlsClientCertData", []))

    @jsii.member(jsii_name="resetTlsClientCertKey")
    def reset_tls_client_cert_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTlsClientCertKey", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

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
    @jsii.member(jsii_name="connectionStateStatus")
    def connection_state_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectionStateStatus"))

    @builtins.property
    @jsii.member(jsii_name="inheritedCreds")
    def inherited_creds(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "inheritedCreds"))

    @builtins.property
    @jsii.member(jsii_name="enableLfsInput")
    def enable_lfs_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableLfsInput"))

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
    @jsii.member(jsii_name="insecureInput")
    def insecure_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "insecureInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="repoInput")
    def repo_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repoInput"))

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
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="enableLfs")
    def enable_lfs(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableLfs"))

    @enable_lfs.setter
    def enable_lfs(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb802e836b15d5d02d653aa523dc93d8ee542ef1c95b5207647bd545d66d0aac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableLfs", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__c56dd5e8b3fb029738d5f9f09f7536c83a410cf886db0d13bd84f87b3ce286d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableOci", value)

    @builtins.property
    @jsii.member(jsii_name="githubappEnterpriseBaseUrl")
    def githubapp_enterprise_base_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "githubappEnterpriseBaseUrl"))

    @githubapp_enterprise_base_url.setter
    def githubapp_enterprise_base_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0ffce31bfc7683d4684ca6b1e7baecf7fb8b00620ab554ca6b134e73d2f10a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "githubappEnterpriseBaseUrl", value)

    @builtins.property
    @jsii.member(jsii_name="githubappId")
    def githubapp_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "githubappId"))

    @githubapp_id.setter
    def githubapp_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95fa251883871813b03c6dce7b9c255016ba8d5350fec70a63be47635f7197b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "githubappId", value)

    @builtins.property
    @jsii.member(jsii_name="githubappInstallationId")
    def githubapp_installation_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "githubappInstallationId"))

    @githubapp_installation_id.setter
    def githubapp_installation_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b7b595c34122273d5991f7e7e8726164e3a9b1b42f728ac875d4e372d7f8a35)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "githubappInstallationId", value)

    @builtins.property
    @jsii.member(jsii_name="githubappPrivateKey")
    def githubapp_private_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "githubappPrivateKey"))

    @githubapp_private_key.setter
    def githubapp_private_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f8600515b60022dbbe9d8371f5112e7e719c3bc746c3c2f02389f5cf84c0b60)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "githubappPrivateKey", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f63d8937911eb3ab717c1c962316321b572ac0edf50c9fc7a72c885c9b6bbaaf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__b4d04ae3ecb4dee9fa81b52d10be0b69372fbf43ec56afe618c0479cd0ad5dde)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "insecure", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8360ba3b69584989487fd4a36695c06b1caf07392e4ed6c846ef7c65b447f2cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__156be6f9edf0d2aa79dd22063ba8c9c08fb1b02448a14fc63c2e34f168853761)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2814755100919c391d93d40219f8f80fe687309f7be55147a43c644abc43ffd5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="repo")
    def repo(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repo"))

    @repo.setter
    def repo(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ec85ccfc574ec3a49593cb8da4e840cbdc49623e69489a5fe56bb299d18c701)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repo", value)

    @builtins.property
    @jsii.member(jsii_name="sshPrivateKey")
    def ssh_private_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sshPrivateKey"))

    @ssh_private_key.setter
    def ssh_private_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c8a8e7bf8b834bc76b4ff0bd8c0473210b3047e903e8593bf66c5428806c399)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sshPrivateKey", value)

    @builtins.property
    @jsii.member(jsii_name="tlsClientCertData")
    def tls_client_cert_data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tlsClientCertData"))

    @tls_client_cert_data.setter
    def tls_client_cert_data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd68565fe09f854724892ac355c842430f43b56723e1e0c243cd9d131cd73e1c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tlsClientCertData", value)

    @builtins.property
    @jsii.member(jsii_name="tlsClientCertKey")
    def tls_client_cert_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tlsClientCertKey"))

    @tls_client_cert_key.setter
    def tls_client_cert_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0e73d30ad2dc2899b6c7af4a5a0a49ec8b555557040ebb4c37bc12cbf33e909)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tlsClientCertKey", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56a884169b426dea12b1473df2d0265747f923f5e2f825895e0e135956417f6c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aed21865144bb51d81257c46745c759753422aa4841e298e126e0f5ff610a52e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)


@jsii.data_type(
    jsii_type="argocd.repository.RepositoryConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "repo": "repo",
        "enable_lfs": "enableLfs",
        "enable_oci": "enableOci",
        "githubapp_enterprise_base_url": "githubappEnterpriseBaseUrl",
        "githubapp_id": "githubappId",
        "githubapp_installation_id": "githubappInstallationId",
        "githubapp_private_key": "githubappPrivateKey",
        "id": "id",
        "insecure": "insecure",
        "name": "name",
        "password": "password",
        "project": "project",
        "ssh_private_key": "sshPrivateKey",
        "tls_client_cert_data": "tlsClientCertData",
        "tls_client_cert_key": "tlsClientCertKey",
        "type": "type",
        "username": "username",
    },
)
class RepositoryConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        repo: builtins.str,
        enable_lfs: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_oci: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        githubapp_enterprise_base_url: typing.Optional[builtins.str] = None,
        githubapp_id: typing.Optional[builtins.str] = None,
        githubapp_installation_id: typing.Optional[builtins.str] = None,
        githubapp_private_key: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        insecure: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        ssh_private_key: typing.Optional[builtins.str] = None,
        tls_client_cert_data: typing.Optional[builtins.str] = None,
        tls_client_cert_key: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
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
        :param repo: URL of the repository. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository#repo Repository#repo}
        :param enable_lfs: Whether ``git-lfs`` support should be enabled for this repository. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository#enable_lfs Repository#enable_lfs}
        :param enable_oci: Whether ``helm-oci`` support should be enabled for this repository. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository#enable_oci Repository#enable_oci}
        :param githubapp_enterprise_base_url: GitHub API URL for GitHub app authentication. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository#githubapp_enterprise_base_url Repository#githubapp_enterprise_base_url}
        :param githubapp_id: ID of the GitHub app used to access the repo. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository#githubapp_id Repository#githubapp_id}
        :param githubapp_installation_id: The installation ID of the GitHub App used to access the repo. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository#githubapp_installation_id Repository#githubapp_installation_id}
        :param githubapp_private_key: Private key data (PEM) for authentication via GitHub app. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository#githubapp_private_key Repository#githubapp_private_key}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository#id Repository#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param insecure: Whether the connection to the repository ignores any errors when verifying TLS certificates or SSH host keys. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository#insecure Repository#insecure}
        :param name: Name to be used for this repo. Only used with Helm repos. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository#name Repository#name}
        :param password: Password or PAT used for authenticating at the remote repository. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository#password Repository#password}
        :param project: The project name, in case the repository is project scoped. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository#project Repository#project}
        :param ssh_private_key: PEM data for authenticating at the repo server. Only used with Git repos. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository#ssh_private_key Repository#ssh_private_key}
        :param tls_client_cert_data: TLS client certificate in PEM format for authenticating at the repo server. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository#tls_client_cert_data Repository#tls_client_cert_data}
        :param tls_client_cert_key: TLS client certificate private key in PEM format for authenticating at the repo server. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository#tls_client_cert_key Repository#tls_client_cert_key}
        :param type: Type of the repo. Can be either ``git`` or ``helm``. ``git`` is assumed if empty or absent. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository#type Repository#type}
        :param username: Username used for authenticating at the remote repository. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository#username Repository#username}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b42e3a82feaa811eb3de26f011acd5d68f891430dd36a37b92cc324a002b928d)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument repo", value=repo, expected_type=type_hints["repo"])
            check_type(argname="argument enable_lfs", value=enable_lfs, expected_type=type_hints["enable_lfs"])
            check_type(argname="argument enable_oci", value=enable_oci, expected_type=type_hints["enable_oci"])
            check_type(argname="argument githubapp_enterprise_base_url", value=githubapp_enterprise_base_url, expected_type=type_hints["githubapp_enterprise_base_url"])
            check_type(argname="argument githubapp_id", value=githubapp_id, expected_type=type_hints["githubapp_id"])
            check_type(argname="argument githubapp_installation_id", value=githubapp_installation_id, expected_type=type_hints["githubapp_installation_id"])
            check_type(argname="argument githubapp_private_key", value=githubapp_private_key, expected_type=type_hints["githubapp_private_key"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument insecure", value=insecure, expected_type=type_hints["insecure"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument ssh_private_key", value=ssh_private_key, expected_type=type_hints["ssh_private_key"])
            check_type(argname="argument tls_client_cert_data", value=tls_client_cert_data, expected_type=type_hints["tls_client_cert_data"])
            check_type(argname="argument tls_client_cert_key", value=tls_client_cert_key, expected_type=type_hints["tls_client_cert_key"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "repo": repo,
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
        if enable_lfs is not None:
            self._values["enable_lfs"] = enable_lfs
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
        if insecure is not None:
            self._values["insecure"] = insecure
        if name is not None:
            self._values["name"] = name
        if password is not None:
            self._values["password"] = password
        if project is not None:
            self._values["project"] = project
        if ssh_private_key is not None:
            self._values["ssh_private_key"] = ssh_private_key
        if tls_client_cert_data is not None:
            self._values["tls_client_cert_data"] = tls_client_cert_data
        if tls_client_cert_key is not None:
            self._values["tls_client_cert_key"] = tls_client_cert_key
        if type is not None:
            self._values["type"] = type
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
    def repo(self) -> builtins.str:
        '''URL of the repository.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository#repo Repository#repo}
        '''
        result = self._values.get("repo")
        assert result is not None, "Required property 'repo' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enable_lfs(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether ``git-lfs`` support should be enabled for this repository.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository#enable_lfs Repository#enable_lfs}
        '''
        result = self._values.get("enable_lfs")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def enable_oci(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether ``helm-oci`` support should be enabled for this repository.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository#enable_oci Repository#enable_oci}
        '''
        result = self._values.get("enable_oci")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def githubapp_enterprise_base_url(self) -> typing.Optional[builtins.str]:
        '''GitHub API URL for GitHub app authentication.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository#githubapp_enterprise_base_url Repository#githubapp_enterprise_base_url}
        '''
        result = self._values.get("githubapp_enterprise_base_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def githubapp_id(self) -> typing.Optional[builtins.str]:
        '''ID of the GitHub app used to access the repo.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository#githubapp_id Repository#githubapp_id}
        '''
        result = self._values.get("githubapp_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def githubapp_installation_id(self) -> typing.Optional[builtins.str]:
        '''The installation ID of the GitHub App used to access the repo.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository#githubapp_installation_id Repository#githubapp_installation_id}
        '''
        result = self._values.get("githubapp_installation_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def githubapp_private_key(self) -> typing.Optional[builtins.str]:
        '''Private key data (PEM) for authentication via GitHub app.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository#githubapp_private_key Repository#githubapp_private_key}
        '''
        result = self._values.get("githubapp_private_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository#id Repository#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def insecure(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether the connection to the repository ignores any errors when verifying TLS certificates or SSH host keys.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository#insecure Repository#insecure}
        '''
        result = self._values.get("insecure")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name to be used for this repo. Only used with Helm repos.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository#name Repository#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''Password or PAT used for authenticating at the remote repository.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository#password Repository#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''The project name, in case the repository is project scoped.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository#project Repository#project}
        '''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ssh_private_key(self) -> typing.Optional[builtins.str]:
        '''PEM data for authenticating at the repo server. Only used with Git repos.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository#ssh_private_key Repository#ssh_private_key}
        '''
        result = self._values.get("ssh_private_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tls_client_cert_data(self) -> typing.Optional[builtins.str]:
        '''TLS client certificate in PEM format for authenticating at the repo server.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository#tls_client_cert_data Repository#tls_client_cert_data}
        '''
        result = self._values.get("tls_client_cert_data")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tls_client_cert_key(self) -> typing.Optional[builtins.str]:
        '''TLS client certificate private key in PEM format for authenticating at the repo server.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository#tls_client_cert_key Repository#tls_client_cert_key}
        '''
        result = self._values.get("tls_client_cert_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Type of the repo. Can be either ``git`` or ``helm``. ``git`` is assumed if empty or absent.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository#type Repository#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''Username used for authenticating at the remote repository.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/repository#username Repository#username}
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RepositoryConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Repository",
    "RepositoryConfig",
]

publication.publish()

def _typecheckingstub__d336db88e9c6bd05bb9bb7fc5259ea874f4e539aa5f7ab04374c561d07a630eb(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    repo: builtins.str,
    enable_lfs: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enable_oci: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    githubapp_enterprise_base_url: typing.Optional[builtins.str] = None,
    githubapp_id: typing.Optional[builtins.str] = None,
    githubapp_installation_id: typing.Optional[builtins.str] = None,
    githubapp_private_key: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    insecure: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    name: typing.Optional[builtins.str] = None,
    password: typing.Optional[builtins.str] = None,
    project: typing.Optional[builtins.str] = None,
    ssh_private_key: typing.Optional[builtins.str] = None,
    tls_client_cert_data: typing.Optional[builtins.str] = None,
    tls_client_cert_key: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__eb802e836b15d5d02d653aa523dc93d8ee542ef1c95b5207647bd545d66d0aac(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c56dd5e8b3fb029738d5f9f09f7536c83a410cf886db0d13bd84f87b3ce286d7(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0ffce31bfc7683d4684ca6b1e7baecf7fb8b00620ab554ca6b134e73d2f10a0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95fa251883871813b03c6dce7b9c255016ba8d5350fec70a63be47635f7197b4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b7b595c34122273d5991f7e7e8726164e3a9b1b42f728ac875d4e372d7f8a35(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f8600515b60022dbbe9d8371f5112e7e719c3bc746c3c2f02389f5cf84c0b60(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f63d8937911eb3ab717c1c962316321b572ac0edf50c9fc7a72c885c9b6bbaaf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4d04ae3ecb4dee9fa81b52d10be0b69372fbf43ec56afe618c0479cd0ad5dde(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8360ba3b69584989487fd4a36695c06b1caf07392e4ed6c846ef7c65b447f2cf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__156be6f9edf0d2aa79dd22063ba8c9c08fb1b02448a14fc63c2e34f168853761(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2814755100919c391d93d40219f8f80fe687309f7be55147a43c644abc43ffd5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ec85ccfc574ec3a49593cb8da4e840cbdc49623e69489a5fe56bb299d18c701(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c8a8e7bf8b834bc76b4ff0bd8c0473210b3047e903e8593bf66c5428806c399(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd68565fe09f854724892ac355c842430f43b56723e1e0c243cd9d131cd73e1c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0e73d30ad2dc2899b6c7af4a5a0a49ec8b555557040ebb4c37bc12cbf33e909(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56a884169b426dea12b1473df2d0265747f923f5e2f825895e0e135956417f6c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aed21865144bb51d81257c46745c759753422aa4841e298e126e0f5ff610a52e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b42e3a82feaa811eb3de26f011acd5d68f891430dd36a37b92cc324a002b928d(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    repo: builtins.str,
    enable_lfs: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enable_oci: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    githubapp_enterprise_base_url: typing.Optional[builtins.str] = None,
    githubapp_id: typing.Optional[builtins.str] = None,
    githubapp_installation_id: typing.Optional[builtins.str] = None,
    githubapp_private_key: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    insecure: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    name: typing.Optional[builtins.str] = None,
    password: typing.Optional[builtins.str] = None,
    project: typing.Optional[builtins.str] = None,
    ssh_private_key: typing.Optional[builtins.str] = None,
    tls_client_cert_data: typing.Optional[builtins.str] = None,
    tls_client_cert_key: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
    username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
