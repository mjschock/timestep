'''
# `vercel_deployment`

Refer to the Terraform Registory for docs: [`vercel_deployment`](https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/deployment).
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


class Deployment(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="vercel.deployment.Deployment",
):
    '''Represents a {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/deployment vercel_deployment}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        project_id: builtins.str,
        delete_on_destroy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        files: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        path_prefix: typing.Optional[builtins.str] = None,
        production: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        project_settings: typing.Optional[typing.Union["DeploymentProjectSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        ref: typing.Optional[builtins.str] = None,
        team_id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/deployment vercel_deployment} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param project_id: The project ID to add the deployment to. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/deployment#project_id Deployment#project_id}
        :param delete_on_destroy: Set to true to hard delete the Vercel deployment when destroying the Terraform resource. If unspecified, deployments are retained indefinitely. Note that deleted deployments are not recoverable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/deployment#delete_on_destroy Deployment#delete_on_destroy}
        :param environment: A map of environment variable names to values. These are specific to a Deployment, and can also be configured on the ``vercel_project`` resource. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/deployment#environment Deployment#environment}
        :param files: A map of files to be uploaded for the deployment. This should be provided by a ``vercel_project_directory`` or ``vercel_file`` data source. Required if ``git_source`` is not set. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/deployment#files Deployment#files}
        :param path_prefix: If specified then the ``path_prefix`` will be stripped from the start of file paths as they are uploaded to Vercel. If this is omitted, then any leading ``../``s will be stripped. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/deployment#path_prefix Deployment#path_prefix}
        :param production: true if the deployment is a production deployment, meaning production aliases will be assigned. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/deployment#production Deployment#production}
        :param project_settings: Project settings that will be applied to the deployment. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/deployment#project_settings Deployment#project_settings}
        :param ref: The branch or commit hash that should be deployed. Note this will only work if the project is configured to use a Git repository. Required if ``ref`` is not set. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/deployment#ref Deployment#ref}
        :param team_id: The team ID to add the deployment to. Required when configuring a team resource if a default team has not been set in the provider. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/deployment#team_id Deployment#team_id}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a41fcb2e205310304b9275230d4f34d58c35cdbb2150465cd8493f62ec9d2d7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = DeploymentConfig(
            project_id=project_id,
            delete_on_destroy=delete_on_destroy,
            environment=environment,
            files=files,
            path_prefix=path_prefix,
            production=production,
            project_settings=project_settings,
            ref=ref,
            team_id=team_id,
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
        '''Generates CDKTF code for importing a Deployment resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the Deployment to import.
        :param import_from_id: The id of the existing Deployment that should be imported. Refer to the {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/deployment#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the Deployment to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2fb712dab0d58c66e77235ea4a55fa8ed0c4326decaf17171d60595b29cf38cd)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putProjectSettings")
    def put_project_settings(
        self,
        *,
        build_command: typing.Optional[builtins.str] = None,
        framework: typing.Optional[builtins.str] = None,
        install_command: typing.Optional[builtins.str] = None,
        output_directory: typing.Optional[builtins.str] = None,
        root_directory: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param build_command: The build command for this deployment. If omitted, this value will be taken from the project or automatically detected. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/deployment#build_command Deployment#build_command}
        :param framework: The framework that is being used for this deployment. If omitted, no framework is selected. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/deployment#framework Deployment#framework}
        :param install_command: The install command for this deployment. If omitted, this value will be taken from the project or automatically detected. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/deployment#install_command Deployment#install_command}
        :param output_directory: The output directory of the deployment. If omitted, this value will be taken from the project or automatically detected. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/deployment#output_directory Deployment#output_directory}
        :param root_directory: The name of a directory or relative path to the source code of your project. When null is used it will default to the project root. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/deployment#root_directory Deployment#root_directory}
        '''
        value = DeploymentProjectSettings(
            build_command=build_command,
            framework=framework,
            install_command=install_command,
            output_directory=output_directory,
            root_directory=root_directory,
        )

        return typing.cast(None, jsii.invoke(self, "putProjectSettings", [value]))

    @jsii.member(jsii_name="resetDeleteOnDestroy")
    def reset_delete_on_destroy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeleteOnDestroy", []))

    @jsii.member(jsii_name="resetEnvironment")
    def reset_environment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnvironment", []))

    @jsii.member(jsii_name="resetFiles")
    def reset_files(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFiles", []))

    @jsii.member(jsii_name="resetPathPrefix")
    def reset_path_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPathPrefix", []))

    @jsii.member(jsii_name="resetProduction")
    def reset_production(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProduction", []))

    @jsii.member(jsii_name="resetProjectSettings")
    def reset_project_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProjectSettings", []))

    @jsii.member(jsii_name="resetRef")
    def reset_ref(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRef", []))

    @jsii.member(jsii_name="resetTeamId")
    def reset_team_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTeamId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="domains")
    def domains(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "domains"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="projectSettings")
    def project_settings(self) -> "DeploymentProjectSettingsOutputReference":
        return typing.cast("DeploymentProjectSettingsOutputReference", jsii.get(self, "projectSettings"))

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @builtins.property
    @jsii.member(jsii_name="deleteOnDestroyInput")
    def delete_on_destroy_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "deleteOnDestroyInput"))

    @builtins.property
    @jsii.member(jsii_name="environmentInput")
    def environment_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "environmentInput"))

    @builtins.property
    @jsii.member(jsii_name="filesInput")
    def files_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "filesInput"))

    @builtins.property
    @jsii.member(jsii_name="pathPrefixInput")
    def path_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="productionInput")
    def production_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "productionInput"))

    @builtins.property
    @jsii.member(jsii_name="projectIdInput")
    def project_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectIdInput"))

    @builtins.property
    @jsii.member(jsii_name="projectSettingsInput")
    def project_settings_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, "DeploymentProjectSettings"]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, "DeploymentProjectSettings"]], jsii.get(self, "projectSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="refInput")
    def ref_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "refInput"))

    @builtins.property
    @jsii.member(jsii_name="teamIdInput")
    def team_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "teamIdInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteOnDestroy")
    def delete_on_destroy(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "deleteOnDestroy"))

    @delete_on_destroy.setter
    def delete_on_destroy(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d97078f031f0063260dcfc0c066178e36b9523e3b98d54e91180b99c6ff299e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deleteOnDestroy", value)

    @builtins.property
    @jsii.member(jsii_name="environment")
    def environment(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "environment"))

    @environment.setter
    def environment(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__757cd409e462371d9a2e1c170f55593552dcfc19f55424031937980a48ca3b4a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environment", value)

    @builtins.property
    @jsii.member(jsii_name="files")
    def files(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "files"))

    @files.setter
    def files(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63c8781253c2ad19cfd4c9581d63c2c1e5f348ebcc98eaf32e8463595c25da4d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "files", value)

    @builtins.property
    @jsii.member(jsii_name="pathPrefix")
    def path_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pathPrefix"))

    @path_prefix.setter
    def path_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96cc6004ec10fbb9411b26cb9e1c71b05c2414363bb0ed1c2a8fa13269d7f655)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pathPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="production")
    def production(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "production"))

    @production.setter
    def production(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56e31402731bb3c291ba8d6253268e3fe1391c6235e3f5d894dd3a5c1f74f37d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "production", value)

    @builtins.property
    @jsii.member(jsii_name="projectId")
    def project_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectId"))

    @project_id.setter
    def project_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e671ab97b443ce531407725122f1d7a26c152bf7dbdc2de3f5e2d1342998ce54)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectId", value)

    @builtins.property
    @jsii.member(jsii_name="ref")
    def ref(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ref"))

    @ref.setter
    def ref(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79206d4c28db1dbb5fa057901742f0e6a283afbf864248e5eb49780627caf21d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ref", value)

    @builtins.property
    @jsii.member(jsii_name="teamId")
    def team_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "teamId"))

    @team_id.setter
    def team_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92621e3e0647f49324a7798d1376aca4780b7a573cca1db907ab20f2569408a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "teamId", value)


@jsii.data_type(
    jsii_type="vercel.deployment.DeploymentConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "project_id": "projectId",
        "delete_on_destroy": "deleteOnDestroy",
        "environment": "environment",
        "files": "files",
        "path_prefix": "pathPrefix",
        "production": "production",
        "project_settings": "projectSettings",
        "ref": "ref",
        "team_id": "teamId",
    },
)
class DeploymentConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        project_id: builtins.str,
        delete_on_destroy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        files: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        path_prefix: typing.Optional[builtins.str] = None,
        production: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        project_settings: typing.Optional[typing.Union["DeploymentProjectSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        ref: typing.Optional[builtins.str] = None,
        team_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param project_id: The project ID to add the deployment to. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/deployment#project_id Deployment#project_id}
        :param delete_on_destroy: Set to true to hard delete the Vercel deployment when destroying the Terraform resource. If unspecified, deployments are retained indefinitely. Note that deleted deployments are not recoverable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/deployment#delete_on_destroy Deployment#delete_on_destroy}
        :param environment: A map of environment variable names to values. These are specific to a Deployment, and can also be configured on the ``vercel_project`` resource. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/deployment#environment Deployment#environment}
        :param files: A map of files to be uploaded for the deployment. This should be provided by a ``vercel_project_directory`` or ``vercel_file`` data source. Required if ``git_source`` is not set. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/deployment#files Deployment#files}
        :param path_prefix: If specified then the ``path_prefix`` will be stripped from the start of file paths as they are uploaded to Vercel. If this is omitted, then any leading ``../``s will be stripped. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/deployment#path_prefix Deployment#path_prefix}
        :param production: true if the deployment is a production deployment, meaning production aliases will be assigned. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/deployment#production Deployment#production}
        :param project_settings: Project settings that will be applied to the deployment. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/deployment#project_settings Deployment#project_settings}
        :param ref: The branch or commit hash that should be deployed. Note this will only work if the project is configured to use a Git repository. Required if ``ref`` is not set. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/deployment#ref Deployment#ref}
        :param team_id: The team ID to add the deployment to. Required when configuring a team resource if a default team has not been set in the provider. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/deployment#team_id Deployment#team_id}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(project_settings, dict):
            project_settings = DeploymentProjectSettings(**project_settings)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04722e391e9a0bfade0637012284816ac3b64f665c34939f28cfe21a36f23607)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument delete_on_destroy", value=delete_on_destroy, expected_type=type_hints["delete_on_destroy"])
            check_type(argname="argument environment", value=environment, expected_type=type_hints["environment"])
            check_type(argname="argument files", value=files, expected_type=type_hints["files"])
            check_type(argname="argument path_prefix", value=path_prefix, expected_type=type_hints["path_prefix"])
            check_type(argname="argument production", value=production, expected_type=type_hints["production"])
            check_type(argname="argument project_settings", value=project_settings, expected_type=type_hints["project_settings"])
            check_type(argname="argument ref", value=ref, expected_type=type_hints["ref"])
            check_type(argname="argument team_id", value=team_id, expected_type=type_hints["team_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "project_id": project_id,
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
        if delete_on_destroy is not None:
            self._values["delete_on_destroy"] = delete_on_destroy
        if environment is not None:
            self._values["environment"] = environment
        if files is not None:
            self._values["files"] = files
        if path_prefix is not None:
            self._values["path_prefix"] = path_prefix
        if production is not None:
            self._values["production"] = production
        if project_settings is not None:
            self._values["project_settings"] = project_settings
        if ref is not None:
            self._values["ref"] = ref
        if team_id is not None:
            self._values["team_id"] = team_id

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
    def project_id(self) -> builtins.str:
        '''The project ID to add the deployment to.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/deployment#project_id Deployment#project_id}
        '''
        result = self._values.get("project_id")
        assert result is not None, "Required property 'project_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def delete_on_destroy(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Set to true to hard delete the Vercel deployment when destroying the Terraform resource.

        If unspecified, deployments are retained indefinitely. Note that deleted deployments are not recoverable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/deployment#delete_on_destroy Deployment#delete_on_destroy}
        '''
        result = self._values.get("delete_on_destroy")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def environment(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of environment variable names to values.

        These are specific to a Deployment, and can also be configured on the ``vercel_project`` resource.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/deployment#environment Deployment#environment}
        '''
        result = self._values.get("environment")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def files(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of files to be uploaded for the deployment.

        This should be provided by a ``vercel_project_directory`` or ``vercel_file`` data source. Required if ``git_source`` is not set.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/deployment#files Deployment#files}
        '''
        result = self._values.get("files")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def path_prefix(self) -> typing.Optional[builtins.str]:
        '''If specified then the ``path_prefix`` will be stripped from the start of file paths as they are uploaded to Vercel.

        If this is omitted, then any leading ``../``s will be stripped.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/deployment#path_prefix Deployment#path_prefix}
        '''
        result = self._values.get("path_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def production(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''true if the deployment is a production deployment, meaning production aliases will be assigned.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/deployment#production Deployment#production}
        '''
        result = self._values.get("production")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def project_settings(self) -> typing.Optional["DeploymentProjectSettings"]:
        '''Project settings that will be applied to the deployment.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/deployment#project_settings Deployment#project_settings}
        '''
        result = self._values.get("project_settings")
        return typing.cast(typing.Optional["DeploymentProjectSettings"], result)

    @builtins.property
    def ref(self) -> typing.Optional[builtins.str]:
        '''The branch or commit hash that should be deployed.

        Note this will only work if the project is configured to use a Git repository. Required if ``ref`` is not set.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/deployment#ref Deployment#ref}
        '''
        result = self._values.get("ref")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def team_id(self) -> typing.Optional[builtins.str]:
        '''The team ID to add the deployment to.

        Required when configuring a team resource if a default team has not been set in the provider.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/deployment#team_id Deployment#team_id}
        '''
        result = self._values.get("team_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeploymentConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vercel.deployment.DeploymentProjectSettings",
    jsii_struct_bases=[],
    name_mapping={
        "build_command": "buildCommand",
        "framework": "framework",
        "install_command": "installCommand",
        "output_directory": "outputDirectory",
        "root_directory": "rootDirectory",
    },
)
class DeploymentProjectSettings:
    def __init__(
        self,
        *,
        build_command: typing.Optional[builtins.str] = None,
        framework: typing.Optional[builtins.str] = None,
        install_command: typing.Optional[builtins.str] = None,
        output_directory: typing.Optional[builtins.str] = None,
        root_directory: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param build_command: The build command for this deployment. If omitted, this value will be taken from the project or automatically detected. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/deployment#build_command Deployment#build_command}
        :param framework: The framework that is being used for this deployment. If omitted, no framework is selected. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/deployment#framework Deployment#framework}
        :param install_command: The install command for this deployment. If omitted, this value will be taken from the project or automatically detected. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/deployment#install_command Deployment#install_command}
        :param output_directory: The output directory of the deployment. If omitted, this value will be taken from the project or automatically detected. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/deployment#output_directory Deployment#output_directory}
        :param root_directory: The name of a directory or relative path to the source code of your project. When null is used it will default to the project root. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/deployment#root_directory Deployment#root_directory}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d816adb9d46b4c732f3e440cf4b8e009cab8e646812e93adabcd68f92d5a474a)
            check_type(argname="argument build_command", value=build_command, expected_type=type_hints["build_command"])
            check_type(argname="argument framework", value=framework, expected_type=type_hints["framework"])
            check_type(argname="argument install_command", value=install_command, expected_type=type_hints["install_command"])
            check_type(argname="argument output_directory", value=output_directory, expected_type=type_hints["output_directory"])
            check_type(argname="argument root_directory", value=root_directory, expected_type=type_hints["root_directory"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if build_command is not None:
            self._values["build_command"] = build_command
        if framework is not None:
            self._values["framework"] = framework
        if install_command is not None:
            self._values["install_command"] = install_command
        if output_directory is not None:
            self._values["output_directory"] = output_directory
        if root_directory is not None:
            self._values["root_directory"] = root_directory

    @builtins.property
    def build_command(self) -> typing.Optional[builtins.str]:
        '''The build command for this deployment. If omitted, this value will be taken from the project or automatically detected.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/deployment#build_command Deployment#build_command}
        '''
        result = self._values.get("build_command")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def framework(self) -> typing.Optional[builtins.str]:
        '''The framework that is being used for this deployment. If omitted, no framework is selected.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/deployment#framework Deployment#framework}
        '''
        result = self._values.get("framework")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def install_command(self) -> typing.Optional[builtins.str]:
        '''The install command for this deployment. If omitted, this value will be taken from the project or automatically detected.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/deployment#install_command Deployment#install_command}
        '''
        result = self._values.get("install_command")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def output_directory(self) -> typing.Optional[builtins.str]:
        '''The output directory of the deployment. If omitted, this value will be taken from the project or automatically detected.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/deployment#output_directory Deployment#output_directory}
        '''
        result = self._values.get("output_directory")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def root_directory(self) -> typing.Optional[builtins.str]:
        '''The name of a directory or relative path to the source code of your project.

        When null is used it will default to the project root.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/deployment#root_directory Deployment#root_directory}
        '''
        result = self._values.get("root_directory")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeploymentProjectSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DeploymentProjectSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="vercel.deployment.DeploymentProjectSettingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b92fcbf410a56d4c30681d32a129411c01eea7c284342795cba8cd1375738bcf)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBuildCommand")
    def reset_build_command(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBuildCommand", []))

    @jsii.member(jsii_name="resetFramework")
    def reset_framework(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFramework", []))

    @jsii.member(jsii_name="resetInstallCommand")
    def reset_install_command(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstallCommand", []))

    @jsii.member(jsii_name="resetOutputDirectory")
    def reset_output_directory(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOutputDirectory", []))

    @jsii.member(jsii_name="resetRootDirectory")
    def reset_root_directory(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRootDirectory", []))

    @builtins.property
    @jsii.member(jsii_name="buildCommandInput")
    def build_command_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "buildCommandInput"))

    @builtins.property
    @jsii.member(jsii_name="frameworkInput")
    def framework_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "frameworkInput"))

    @builtins.property
    @jsii.member(jsii_name="installCommandInput")
    def install_command_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "installCommandInput"))

    @builtins.property
    @jsii.member(jsii_name="outputDirectoryInput")
    def output_directory_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "outputDirectoryInput"))

    @builtins.property
    @jsii.member(jsii_name="rootDirectoryInput")
    def root_directory_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rootDirectoryInput"))

    @builtins.property
    @jsii.member(jsii_name="buildCommand")
    def build_command(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "buildCommand"))

    @build_command.setter
    def build_command(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00514b182cedec328cc59b014d54d3635fb3f2aa4b70407fbd293f3a45286d8f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "buildCommand", value)

    @builtins.property
    @jsii.member(jsii_name="framework")
    def framework(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "framework"))

    @framework.setter
    def framework(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__142b2000d60eca70aff059ea8081b00feccdaf824dc9746f67019902b0241df7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "framework", value)

    @builtins.property
    @jsii.member(jsii_name="installCommand")
    def install_command(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "installCommand"))

    @install_command.setter
    def install_command(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e55220b1e3fa5e184788b73e8703af470fdda2e33d2ba2b8519ec50b79c76b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "installCommand", value)

    @builtins.property
    @jsii.member(jsii_name="outputDirectory")
    def output_directory(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "outputDirectory"))

    @output_directory.setter
    def output_directory(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7495d6af5a9b1c7fa5a33964dc640726a7166506509594649b228aa250adcd2f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outputDirectory", value)

    @builtins.property
    @jsii.member(jsii_name="rootDirectory")
    def root_directory(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rootDirectory"))

    @root_directory.setter
    def root_directory(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67893373e8d735cee4716a010f64c93d68683870e5bb3fc9e8f6a3b29fcffc9b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rootDirectory", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DeploymentProjectSettings]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DeploymentProjectSettings]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DeploymentProjectSettings]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f42d7a731037d3c020a071dccd1516010950d1bef6e76225ca41cf35cb9ce1c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Deployment",
    "DeploymentConfig",
    "DeploymentProjectSettings",
    "DeploymentProjectSettingsOutputReference",
]

publication.publish()

def _typecheckingstub__6a41fcb2e205310304b9275230d4f34d58c35cdbb2150465cd8493f62ec9d2d7(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    project_id: builtins.str,
    delete_on_destroy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    files: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    path_prefix: typing.Optional[builtins.str] = None,
    production: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    project_settings: typing.Optional[typing.Union[DeploymentProjectSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    ref: typing.Optional[builtins.str] = None,
    team_id: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__2fb712dab0d58c66e77235ea4a55fa8ed0c4326decaf17171d60595b29cf38cd(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d97078f031f0063260dcfc0c066178e36b9523e3b98d54e91180b99c6ff299e9(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__757cd409e462371d9a2e1c170f55593552dcfc19f55424031937980a48ca3b4a(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63c8781253c2ad19cfd4c9581d63c2c1e5f348ebcc98eaf32e8463595c25da4d(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96cc6004ec10fbb9411b26cb9e1c71b05c2414363bb0ed1c2a8fa13269d7f655(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56e31402731bb3c291ba8d6253268e3fe1391c6235e3f5d894dd3a5c1f74f37d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e671ab97b443ce531407725122f1d7a26c152bf7dbdc2de3f5e2d1342998ce54(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79206d4c28db1dbb5fa057901742f0e6a283afbf864248e5eb49780627caf21d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92621e3e0647f49324a7798d1376aca4780b7a573cca1db907ab20f2569408a1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04722e391e9a0bfade0637012284816ac3b64f665c34939f28cfe21a36f23607(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    project_id: builtins.str,
    delete_on_destroy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    files: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    path_prefix: typing.Optional[builtins.str] = None,
    production: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    project_settings: typing.Optional[typing.Union[DeploymentProjectSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    ref: typing.Optional[builtins.str] = None,
    team_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d816adb9d46b4c732f3e440cf4b8e009cab8e646812e93adabcd68f92d5a474a(
    *,
    build_command: typing.Optional[builtins.str] = None,
    framework: typing.Optional[builtins.str] = None,
    install_command: typing.Optional[builtins.str] = None,
    output_directory: typing.Optional[builtins.str] = None,
    root_directory: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b92fcbf410a56d4c30681d32a129411c01eea7c284342795cba8cd1375738bcf(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00514b182cedec328cc59b014d54d3635fb3f2aa4b70407fbd293f3a45286d8f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__142b2000d60eca70aff059ea8081b00feccdaf824dc9746f67019902b0241df7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e55220b1e3fa5e184788b73e8703af470fdda2e33d2ba2b8519ec50b79c76b5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7495d6af5a9b1c7fa5a33964dc640726a7166506509594649b228aa250adcd2f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67893373e8d735cee4716a010f64c93d68683870e5bb3fc9e8f6a3b29fcffc9b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f42d7a731037d3c020a071dccd1516010950d1bef6e76225ca41cf35cb9ce1c9(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DeploymentProjectSettings]],
) -> None:
    """Type checking stubs"""
    pass
