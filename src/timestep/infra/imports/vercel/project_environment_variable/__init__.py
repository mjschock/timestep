'''
# `vercel_project_environment_variable`

Refer to the Terraform Registory for docs: [`vercel_project_environment_variable`](https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project_environment_variable).
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


class ProjectEnvironmentVariable(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="vercel.projectEnvironmentVariable.ProjectEnvironmentVariable",
):
    '''Represents a {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project_environment_variable vercel_project_environment_variable}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        key: builtins.str,
        project_id: builtins.str,
        target: typing.Sequence[builtins.str],
        value: builtins.str,
        git_branch: typing.Optional[builtins.str] = None,
        sensitive: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        team_id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project_environment_variable vercel_project_environment_variable} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param key: The name of the Environment Variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project_environment_variable#key ProjectEnvironmentVariable#key}
        :param project_id: The ID of the Vercel project. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project_environment_variable#project_id ProjectEnvironmentVariable#project_id}
        :param target: The environments that the Environment Variable should be present on. Valid targets are either ``production``, ``preview``, or ``development``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project_environment_variable#target ProjectEnvironmentVariable#target}
        :param value: The value of the Environment Variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project_environment_variable#value ProjectEnvironmentVariable#value}
        :param git_branch: The git branch of the Environment Variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project_environment_variable#git_branch ProjectEnvironmentVariable#git_branch}
        :param sensitive: Whether the Environment Variable is sensitive or not. (May be affected by a `team-wide environment variable policy <https://vercel.com/docs/projects/environment-variables/sensitive-environment-variables#environment-variables-policy>`_). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project_environment_variable#sensitive ProjectEnvironmentVariable#sensitive}
        :param team_id: The ID of the Vercel team.Required when configuring a team resource if a default team has not been set in the provider. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project_environment_variable#team_id ProjectEnvironmentVariable#team_id}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5181b162066811a791c6aaa90636a435d87d7ca6433d395caaad24f10039bad3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = ProjectEnvironmentVariableConfig(
            key=key,
            project_id=project_id,
            target=target,
            value=value,
            git_branch=git_branch,
            sensitive=sensitive,
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
        '''Generates CDKTF code for importing a ProjectEnvironmentVariable resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the ProjectEnvironmentVariable to import.
        :param import_from_id: The id of the existing ProjectEnvironmentVariable that should be imported. Refer to the {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project_environment_variable#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the ProjectEnvironmentVariable to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ac345078414e0cf915e6f2c960615f47d29cd7e7f38d7997027afee7d815f56)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="resetGitBranch")
    def reset_git_branch(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGitBranch", []))

    @jsii.member(jsii_name="resetSensitive")
    def reset_sensitive(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSensitive", []))

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
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="gitBranchInput")
    def git_branch_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gitBranchInput"))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="projectIdInput")
    def project_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectIdInput"))

    @builtins.property
    @jsii.member(jsii_name="sensitiveInput")
    def sensitive_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "sensitiveInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="teamIdInput")
    def team_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "teamIdInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="gitBranch")
    def git_branch(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gitBranch"))

    @git_branch.setter
    def git_branch(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40de1ece32fd8fffe39c8682903fd4e3e7242e56b8d5ecd41a2adc8167ff192a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gitBranch", value)

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4a1a1bebab1ccb446647f34d6cc5fa96e7249dcf6c53b22e8145426ee057dd2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="projectId")
    def project_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectId"))

    @project_id.setter
    def project_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0e1531388703db518b017352748ce397d7da9713e2f2861cc56d52082c1debb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectId", value)

    @builtins.property
    @jsii.member(jsii_name="sensitive")
    def sensitive(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "sensitive"))

    @sensitive.setter
    def sensitive(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dff008566c1d6091d1a8b621bbd87d7b07ca59209109140873f718802b23795c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sensitive", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "target"))

    @target.setter
    def target(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24ccfed7303bb8363aba0d5970b61627eb7eb03d1a0520a74a3730935b51ef2e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="teamId")
    def team_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "teamId"))

    @team_id.setter
    def team_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ffa1b1120d57d478c0203251723ca072ac09ccb06bcfee5e75ef922cf3a30f97)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "teamId", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2704179d60fdf79e15cb8f25ce0a588d817b689146009c2f19083d74509eeaf4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)


@jsii.data_type(
    jsii_type="vercel.projectEnvironmentVariable.ProjectEnvironmentVariableConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "key": "key",
        "project_id": "projectId",
        "target": "target",
        "value": "value",
        "git_branch": "gitBranch",
        "sensitive": "sensitive",
        "team_id": "teamId",
    },
)
class ProjectEnvironmentVariableConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        key: builtins.str,
        project_id: builtins.str,
        target: typing.Sequence[builtins.str],
        value: builtins.str,
        git_branch: typing.Optional[builtins.str] = None,
        sensitive: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
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
        :param key: The name of the Environment Variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project_environment_variable#key ProjectEnvironmentVariable#key}
        :param project_id: The ID of the Vercel project. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project_environment_variable#project_id ProjectEnvironmentVariable#project_id}
        :param target: The environments that the Environment Variable should be present on. Valid targets are either ``production``, ``preview``, or ``development``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project_environment_variable#target ProjectEnvironmentVariable#target}
        :param value: The value of the Environment Variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project_environment_variable#value ProjectEnvironmentVariable#value}
        :param git_branch: The git branch of the Environment Variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project_environment_variable#git_branch ProjectEnvironmentVariable#git_branch}
        :param sensitive: Whether the Environment Variable is sensitive or not. (May be affected by a `team-wide environment variable policy <https://vercel.com/docs/projects/environment-variables/sensitive-environment-variables#environment-variables-policy>`_). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project_environment_variable#sensitive ProjectEnvironmentVariable#sensitive}
        :param team_id: The ID of the Vercel team.Required when configuring a team resource if a default team has not been set in the provider. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project_environment_variable#team_id ProjectEnvironmentVariable#team_id}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c003388c337311885050755a1bed607e6af64217b14bd6aa849eafa1d4a82402)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument git_branch", value=git_branch, expected_type=type_hints["git_branch"])
            check_type(argname="argument sensitive", value=sensitive, expected_type=type_hints["sensitive"])
            check_type(argname="argument team_id", value=team_id, expected_type=type_hints["team_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "project_id": project_id,
            "target": target,
            "value": value,
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
        if git_branch is not None:
            self._values["git_branch"] = git_branch
        if sensitive is not None:
            self._values["sensitive"] = sensitive
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
    def key(self) -> builtins.str:
        '''The name of the Environment Variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project_environment_variable#key ProjectEnvironmentVariable#key}
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project_id(self) -> builtins.str:
        '''The ID of the Vercel project.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project_environment_variable#project_id ProjectEnvironmentVariable#project_id}
        '''
        result = self._values.get("project_id")
        assert result is not None, "Required property 'project_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target(self) -> typing.List[builtins.str]:
        '''The environments that the Environment Variable should be present on. Valid targets are either ``production``, ``preview``, or ``development``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project_environment_variable#target ProjectEnvironmentVariable#target}
        '''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def value(self) -> builtins.str:
        '''The value of the Environment Variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project_environment_variable#value ProjectEnvironmentVariable#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def git_branch(self) -> typing.Optional[builtins.str]:
        '''The git branch of the Environment Variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project_environment_variable#git_branch ProjectEnvironmentVariable#git_branch}
        '''
        result = self._values.get("git_branch")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sensitive(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether the Environment Variable is sensitive or not. (May be affected by a `team-wide environment variable policy <https://vercel.com/docs/projects/environment-variables/sensitive-environment-variables#environment-variables-policy>`_).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project_environment_variable#sensitive ProjectEnvironmentVariable#sensitive}
        '''
        result = self._values.get("sensitive")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def team_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the Vercel team.Required when configuring a team resource if a default team has not been set in the provider.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project_environment_variable#team_id ProjectEnvironmentVariable#team_id}
        '''
        result = self._values.get("team_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProjectEnvironmentVariableConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ProjectEnvironmentVariable",
    "ProjectEnvironmentVariableConfig",
]

publication.publish()

def _typecheckingstub__5181b162066811a791c6aaa90636a435d87d7ca6433d395caaad24f10039bad3(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    key: builtins.str,
    project_id: builtins.str,
    target: typing.Sequence[builtins.str],
    value: builtins.str,
    git_branch: typing.Optional[builtins.str] = None,
    sensitive: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
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

def _typecheckingstub__6ac345078414e0cf915e6f2c960615f47d29cd7e7f38d7997027afee7d815f56(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40de1ece32fd8fffe39c8682903fd4e3e7242e56b8d5ecd41a2adc8167ff192a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4a1a1bebab1ccb446647f34d6cc5fa96e7249dcf6c53b22e8145426ee057dd2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0e1531388703db518b017352748ce397d7da9713e2f2861cc56d52082c1debb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dff008566c1d6091d1a8b621bbd87d7b07ca59209109140873f718802b23795c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24ccfed7303bb8363aba0d5970b61627eb7eb03d1a0520a74a3730935b51ef2e(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffa1b1120d57d478c0203251723ca072ac09ccb06bcfee5e75ef922cf3a30f97(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2704179d60fdf79e15cb8f25ce0a588d817b689146009c2f19083d74509eeaf4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c003388c337311885050755a1bed607e6af64217b14bd6aa849eafa1d4a82402(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    key: builtins.str,
    project_id: builtins.str,
    target: typing.Sequence[builtins.str],
    value: builtins.str,
    git_branch: typing.Optional[builtins.str] = None,
    sensitive: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    team_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
