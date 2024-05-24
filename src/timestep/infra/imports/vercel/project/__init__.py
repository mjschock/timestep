'''
# `vercel_project`

Refer to the Terraform Registory for docs: [`vercel_project`](https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project).
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


class Project(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="vercel.project.Project",
):
    '''Represents a {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project vercel_project}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        auto_assign_custom_domains: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        automatically_expose_system_environment_variables: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        build_command: typing.Optional[builtins.str] = None,
        customer_success_code_visibility: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        dev_command: typing.Optional[builtins.str] = None,
        directory_listing: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        environment: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ProjectEnvironment", typing.Dict[builtins.str, typing.Any]]]]] = None,
        framework: typing.Optional[builtins.str] = None,
        function_failover: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        git_comments: typing.Optional[typing.Union["ProjectGitComments", typing.Dict[builtins.str, typing.Any]]] = None,
        git_fork_protection: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        git_lfs: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        git_repository: typing.Optional[typing.Union["ProjectGitRepository", typing.Dict[builtins.str, typing.Any]]] = None,
        ignore_command: typing.Optional[builtins.str] = None,
        install_command: typing.Optional[builtins.str] = None,
        options_allowlist: typing.Optional[typing.Union["ProjectOptionsAllowlistStruct", typing.Dict[builtins.str, typing.Any]]] = None,
        output_directory: typing.Optional[builtins.str] = None,
        password_protection: typing.Optional[typing.Union["ProjectPasswordProtection", typing.Dict[builtins.str, typing.Any]]] = None,
        preview_comments: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        prioritise_production_builds: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        protection_bypass_for_automation: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        public_source: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        root_directory: typing.Optional[builtins.str] = None,
        serverless_function_region: typing.Optional[builtins.str] = None,
        skew_protection: typing.Optional[builtins.str] = None,
        team_id: typing.Optional[builtins.str] = None,
        trusted_ips: typing.Optional[typing.Union["ProjectTrustedIps", typing.Dict[builtins.str, typing.Any]]] = None,
        vercel_authentication: typing.Optional[typing.Union["ProjectVercelAuthentication", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project vercel_project} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: The desired name for the project. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#name Project#name}
        :param auto_assign_custom_domains: Automatically assign custom production domains after each Production deployment via merge to the production branch or Vercel CLI deploy with --prod. Defaults to ``true`` Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#auto_assign_custom_domains Project#auto_assign_custom_domains}
        :param automatically_expose_system_environment_variables: Vercel provides a set of Environment Variables that are automatically populated by the System, such as the URL of the Deployment or the name of the Git branch deployed. To expose them to your Deployments, enable this field Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#automatically_expose_system_environment_variables Project#automatically_expose_system_environment_variables}
        :param build_command: The build command for this project. If omitted, this value will be automatically detected. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#build_command Project#build_command}
        :param customer_success_code_visibility: Allows Vercel Customer Support to inspect all Deployments' source code in this project to assist with debugging. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#customer_success_code_visibility Project#customer_success_code_visibility}
        :param dev_command: The dev command for this project. If omitted, this value will be automatically detected. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#dev_command Project#dev_command}
        :param directory_listing: If no index file is present within a directory, the directory contents will be displayed. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#directory_listing Project#directory_listing}
        :param environment: A set of Environment Variables that should be configured for the project. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#environment Project#environment}
        :param framework: The framework that is being used for this project. If omitted, no framework is selected. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#framework Project#framework}
        :param function_failover: Automatically failover Serverless Functions to the nearest region. You can customize regions through vercel.json. A new Deployment is required for your changes to take effect. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#function_failover Project#function_failover}
        :param git_comments: Configuration for Git Comments. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#git_comments Project#git_comments}
        :param git_fork_protection: Ensures that pull requests targeting your Git repository must be authorized by a member of your Team before deploying if your Project has Environment Variables or if the pull request includes a change to vercel.json. Defaults to ``true``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#git_fork_protection Project#git_fork_protection}
        :param git_lfs: Enables Git LFS support. Git LFS replaces large files such as audio samples, videos, datasets, and graphics with text pointers inside Git, while storing the file contents on a remote server like GitHub.com or GitHub Enterprise. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#git_lfs Project#git_lfs}
        :param git_repository: The Git Repository that will be connected to the project. When this is defined, any pushes to the specified connected Git Repository will be automatically deployed. This requires the corresponding Vercel for `Github <https://vercel.com/docs/concepts/git/vercel-for-github>`_, `Gitlab <https://vercel.com/docs/concepts/git/vercel-for-gitlab>`_ or `Bitbucket <https://vercel.com/docs/concepts/git/vercel-for-bitbucket>`_ plugins to be installed. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#git_repository Project#git_repository}
        :param ignore_command: When a commit is pushed to the Git repository that is connected with your Project, its SHA will determine if a new Build has to be issued. If the SHA was deployed before, no new Build will be issued. You can customize this behavior with a command that exits with code 1 (new Build needed) or code 0. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#ignore_command Project#ignore_command}
        :param install_command: The install command for this project. If omitted, this value will be automatically detected. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#install_command Project#install_command}
        :param options_allowlist: Disable Deployment Protection for CORS preflight ``OPTIONS`` requests for a list of paths. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#options_allowlist Project#options_allowlist}
        :param output_directory: The output directory of the project. If omitted, this value will be automatically detected. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#output_directory Project#output_directory}
        :param password_protection: Ensures visitors of your Preview Deployments must enter a password in order to gain access. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#password_protection Project#password_protection}
        :param preview_comments: Whether to enable comments on your Preview Deployments. If omitted, comments are controlled at the team level (default behaviour). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#preview_comments Project#preview_comments}
        :param prioritise_production_builds: If enabled, builds for the Production environment will be prioritized over Preview environments. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#prioritise_production_builds Project#prioritise_production_builds}
        :param protection_bypass_for_automation: Allow automation services to bypass Vercel Authentication and Password Protection for both Preview and Production Deployments on this project when using an HTTP header named ``x-vercel-protection-bypass`` with a value of the ``password_protection_for_automation_secret`` field. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#protection_bypass_for_automation Project#protection_bypass_for_automation}
        :param public_source: By default, visitors to the ``/_logs`` and ``/_src`` paths of your Production and Preview Deployments must log in with Vercel (requires being a member of your team) to see the Source, Logs and Deployment Status of your project. Setting ``public_source`` to ``true`` disables this behaviour, meaning the Source, Logs and Deployment Status can be publicly viewed. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#public_source Project#public_source}
        :param root_directory: The name of a directory or relative path to the source code of your project. If omitted, it will default to the project root. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#root_directory Project#root_directory}
        :param serverless_function_region: The region on Vercel's network to which your Serverless Functions are deployed. It should be close to any data source your Serverless Function might depend on. A new Deployment is required for your changes to take effect. Please see `Vercel's documentation <https://vercel.com/docs/concepts/edge-network/regions>`_ for a full list of regions. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#serverless_function_region Project#serverless_function_region}
        :param skew_protection: Ensures that outdated clients always fetch the correct version for a given deployment. This value defines how long Vercel keeps Skew Protection active. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#skew_protection Project#skew_protection}
        :param team_id: The team ID to add the project to. Required when configuring a team resource if a default team has not been set in the provider. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#team_id Project#team_id}
        :param trusted_ips: Ensures only visitors from an allowed IP address can access your deployment. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#trusted_ips Project#trusted_ips}
        :param vercel_authentication: Ensures visitors to your Preview Deployments are logged into Vercel and have a minimum of Viewer access on your team. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#vercel_authentication Project#vercel_authentication}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49c099ee126aad45fa06d4bd68c4f22a787cf4950c3cca80d1cc31a2fca9ec9b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = ProjectConfig(
            name=name,
            auto_assign_custom_domains=auto_assign_custom_domains,
            automatically_expose_system_environment_variables=automatically_expose_system_environment_variables,
            build_command=build_command,
            customer_success_code_visibility=customer_success_code_visibility,
            dev_command=dev_command,
            directory_listing=directory_listing,
            environment=environment,
            framework=framework,
            function_failover=function_failover,
            git_comments=git_comments,
            git_fork_protection=git_fork_protection,
            git_lfs=git_lfs,
            git_repository=git_repository,
            ignore_command=ignore_command,
            install_command=install_command,
            options_allowlist=options_allowlist,
            output_directory=output_directory,
            password_protection=password_protection,
            preview_comments=preview_comments,
            prioritise_production_builds=prioritise_production_builds,
            protection_bypass_for_automation=protection_bypass_for_automation,
            public_source=public_source,
            root_directory=root_directory,
            serverless_function_region=serverless_function_region,
            skew_protection=skew_protection,
            team_id=team_id,
            trusted_ips=trusted_ips,
            vercel_authentication=vercel_authentication,
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
        '''Generates CDKTF code for importing a Project resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the Project to import.
        :param import_from_id: The id of the existing Project that should be imported. Refer to the {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the Project to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__720fa96e1b043e5bc18f9be2793e78402b4c36f683ed7c5897912e3fd5e57265)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putEnvironment")
    def put_environment(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ProjectEnvironment", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cdab687584df13f5a66795d8385e6fae64c6873111ae3f11b02203a70530685e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEnvironment", [value]))

    @jsii.member(jsii_name="putGitComments")
    def put_git_comments(
        self,
        *,
        on_commit: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        on_pull_request: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param on_commit: Whether Commit comments are enabled. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#on_commit Project#on_commit}
        :param on_pull_request: Whether Pull Request comments are enabled. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#on_pull_request Project#on_pull_request}
        '''
        value = ProjectGitComments(
            on_commit=on_commit, on_pull_request=on_pull_request
        )

        return typing.cast(None, jsii.invoke(self, "putGitComments", [value]))

    @jsii.member(jsii_name="putGitRepository")
    def put_git_repository(
        self,
        *,
        repo: builtins.str,
        type: builtins.str,
        deploy_hooks: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ProjectGitRepositoryDeployHooks", typing.Dict[builtins.str, typing.Any]]]]] = None,
        production_branch: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param repo: The name of the git repository. For example: ``vercel/next.js``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#repo Project#repo}
        :param type: The git provider of the repository. Must be either ``github``, ``gitlab``, or ``bitbucket``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#type Project#type}
        :param deploy_hooks: Deploy hooks are unique URLs that allow you to trigger a deployment of a given branch. See https://vercel.com/docs/deployments/deploy-hooks for full information. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#deploy_hooks Project#deploy_hooks}
        :param production_branch: By default, every commit pushed to the main branch will trigger a Production Deployment instead of the usual Preview Deployment. You can switch to a different branch here. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#production_branch Project#production_branch}
        '''
        value = ProjectGitRepository(
            repo=repo,
            type=type,
            deploy_hooks=deploy_hooks,
            production_branch=production_branch,
        )

        return typing.cast(None, jsii.invoke(self, "putGitRepository", [value]))

    @jsii.member(jsii_name="putOptionsAllowlist")
    def put_options_allowlist(
        self,
        *,
        paths: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ProjectOptionsAllowlistPaths", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param paths: The allowed paths for the OPTIONS Allowlist. Incoming requests will bypass Deployment Protection if they have the method ``OPTIONS`` and **start with** one of the path values. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#paths Project#paths}
        '''
        value = ProjectOptionsAllowlistStruct(paths=paths)

        return typing.cast(None, jsii.invoke(self, "putOptionsAllowlist", [value]))

    @jsii.member(jsii_name="putPasswordProtection")
    def put_password_protection(
        self,
        *,
        deployment_type: builtins.str,
        password: builtins.str,
    ) -> None:
        '''
        :param deployment_type: The deployment environment to protect. Must be one of ``standard_protection``, ``all_deployments``, or ``only_preview_deployments``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#deployment_type Project#deployment_type}
        :param password: The password that visitors must enter to gain access to your Preview Deployments. Drift detection is not possible for this field. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#password Project#password}
        '''
        value = ProjectPasswordProtection(
            deployment_type=deployment_type, password=password
        )

        return typing.cast(None, jsii.invoke(self, "putPasswordProtection", [value]))

    @jsii.member(jsii_name="putTrustedIps")
    def put_trusted_ips(
        self,
        *,
        addresses: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ProjectTrustedIpsAddresses", typing.Dict[builtins.str, typing.Any]]]],
        deployment_type: builtins.str,
        protection_mode: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param addresses: The allowed IP addressses and CIDR ranges with optional descriptions. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#addresses Project#addresses}
        :param deployment_type: The deployment environment to protect. Must be one of ``standard_protection``, ``all_deployments``, ``only_production_deployments``, or ``only_preview_deployments``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#deployment_type Project#deployment_type}
        :param protection_mode: Whether or not Trusted IPs is optional to access a deployment. Must be either ``trusted_ip_required`` or ``trusted_ip_optional``. ``trusted_ip_optional`` is only available with Standalone Trusted IPs. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#protection_mode Project#protection_mode}
        '''
        value = ProjectTrustedIps(
            addresses=addresses,
            deployment_type=deployment_type,
            protection_mode=protection_mode,
        )

        return typing.cast(None, jsii.invoke(self, "putTrustedIps", [value]))

    @jsii.member(jsii_name="putVercelAuthentication")
    def put_vercel_authentication(self, *, deployment_type: builtins.str) -> None:
        '''
        :param deployment_type: The deployment environment to protect. Must be one of ``standard_protection``, ``all_deployments``, ``only_preview_deployments``, or ``none``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#deployment_type Project#deployment_type}
        '''
        value = ProjectVercelAuthentication(deployment_type=deployment_type)

        return typing.cast(None, jsii.invoke(self, "putVercelAuthentication", [value]))

    @jsii.member(jsii_name="resetAutoAssignCustomDomains")
    def reset_auto_assign_custom_domains(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoAssignCustomDomains", []))

    @jsii.member(jsii_name="resetAutomaticallyExposeSystemEnvironmentVariables")
    def reset_automatically_expose_system_environment_variables(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutomaticallyExposeSystemEnvironmentVariables", []))

    @jsii.member(jsii_name="resetBuildCommand")
    def reset_build_command(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBuildCommand", []))

    @jsii.member(jsii_name="resetCustomerSuccessCodeVisibility")
    def reset_customer_success_code_visibility(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomerSuccessCodeVisibility", []))

    @jsii.member(jsii_name="resetDevCommand")
    def reset_dev_command(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDevCommand", []))

    @jsii.member(jsii_name="resetDirectoryListing")
    def reset_directory_listing(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDirectoryListing", []))

    @jsii.member(jsii_name="resetEnvironment")
    def reset_environment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnvironment", []))

    @jsii.member(jsii_name="resetFramework")
    def reset_framework(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFramework", []))

    @jsii.member(jsii_name="resetFunctionFailover")
    def reset_function_failover(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFunctionFailover", []))

    @jsii.member(jsii_name="resetGitComments")
    def reset_git_comments(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGitComments", []))

    @jsii.member(jsii_name="resetGitForkProtection")
    def reset_git_fork_protection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGitForkProtection", []))

    @jsii.member(jsii_name="resetGitLfs")
    def reset_git_lfs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGitLfs", []))

    @jsii.member(jsii_name="resetGitRepository")
    def reset_git_repository(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGitRepository", []))

    @jsii.member(jsii_name="resetIgnoreCommand")
    def reset_ignore_command(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnoreCommand", []))

    @jsii.member(jsii_name="resetInstallCommand")
    def reset_install_command(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstallCommand", []))

    @jsii.member(jsii_name="resetOptionsAllowlist")
    def reset_options_allowlist(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOptionsAllowlist", []))

    @jsii.member(jsii_name="resetOutputDirectory")
    def reset_output_directory(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOutputDirectory", []))

    @jsii.member(jsii_name="resetPasswordProtection")
    def reset_password_protection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPasswordProtection", []))

    @jsii.member(jsii_name="resetPreviewComments")
    def reset_preview_comments(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreviewComments", []))

    @jsii.member(jsii_name="resetPrioritiseProductionBuilds")
    def reset_prioritise_production_builds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrioritiseProductionBuilds", []))

    @jsii.member(jsii_name="resetProtectionBypassForAutomation")
    def reset_protection_bypass_for_automation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProtectionBypassForAutomation", []))

    @jsii.member(jsii_name="resetPublicSource")
    def reset_public_source(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicSource", []))

    @jsii.member(jsii_name="resetRootDirectory")
    def reset_root_directory(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRootDirectory", []))

    @jsii.member(jsii_name="resetServerlessFunctionRegion")
    def reset_serverless_function_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServerlessFunctionRegion", []))

    @jsii.member(jsii_name="resetSkewProtection")
    def reset_skew_protection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSkewProtection", []))

    @jsii.member(jsii_name="resetTeamId")
    def reset_team_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTeamId", []))

    @jsii.member(jsii_name="resetTrustedIps")
    def reset_trusted_ips(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrustedIps", []))

    @jsii.member(jsii_name="resetVercelAuthentication")
    def reset_vercel_authentication(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVercelAuthentication", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="environment")
    def environment(self) -> "ProjectEnvironmentList":
        return typing.cast("ProjectEnvironmentList", jsii.get(self, "environment"))

    @builtins.property
    @jsii.member(jsii_name="gitComments")
    def git_comments(self) -> "ProjectGitCommentsOutputReference":
        return typing.cast("ProjectGitCommentsOutputReference", jsii.get(self, "gitComments"))

    @builtins.property
    @jsii.member(jsii_name="gitRepository")
    def git_repository(self) -> "ProjectGitRepositoryOutputReference":
        return typing.cast("ProjectGitRepositoryOutputReference", jsii.get(self, "gitRepository"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="optionsAllowlist")
    def options_allowlist(self) -> "ProjectOptionsAllowlistStructOutputReference":
        return typing.cast("ProjectOptionsAllowlistStructOutputReference", jsii.get(self, "optionsAllowlist"))

    @builtins.property
    @jsii.member(jsii_name="passwordProtection")
    def password_protection(self) -> "ProjectPasswordProtectionOutputReference":
        return typing.cast("ProjectPasswordProtectionOutputReference", jsii.get(self, "passwordProtection"))

    @builtins.property
    @jsii.member(jsii_name="protectionBypassForAutomationSecret")
    def protection_bypass_for_automation_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protectionBypassForAutomationSecret"))

    @builtins.property
    @jsii.member(jsii_name="trustedIps")
    def trusted_ips(self) -> "ProjectTrustedIpsOutputReference":
        return typing.cast("ProjectTrustedIpsOutputReference", jsii.get(self, "trustedIps"))

    @builtins.property
    @jsii.member(jsii_name="vercelAuthentication")
    def vercel_authentication(self) -> "ProjectVercelAuthenticationOutputReference":
        return typing.cast("ProjectVercelAuthenticationOutputReference", jsii.get(self, "vercelAuthentication"))

    @builtins.property
    @jsii.member(jsii_name="autoAssignCustomDomainsInput")
    def auto_assign_custom_domains_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "autoAssignCustomDomainsInput"))

    @builtins.property
    @jsii.member(jsii_name="automaticallyExposeSystemEnvironmentVariablesInput")
    def automatically_expose_system_environment_variables_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "automaticallyExposeSystemEnvironmentVariablesInput"))

    @builtins.property
    @jsii.member(jsii_name="buildCommandInput")
    def build_command_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "buildCommandInput"))

    @builtins.property
    @jsii.member(jsii_name="customerSuccessCodeVisibilityInput")
    def customer_success_code_visibility_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "customerSuccessCodeVisibilityInput"))

    @builtins.property
    @jsii.member(jsii_name="devCommandInput")
    def dev_command_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "devCommandInput"))

    @builtins.property
    @jsii.member(jsii_name="directoryListingInput")
    def directory_listing_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "directoryListingInput"))

    @builtins.property
    @jsii.member(jsii_name="environmentInput")
    def environment_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ProjectEnvironment"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ProjectEnvironment"]]], jsii.get(self, "environmentInput"))

    @builtins.property
    @jsii.member(jsii_name="frameworkInput")
    def framework_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "frameworkInput"))

    @builtins.property
    @jsii.member(jsii_name="functionFailoverInput")
    def function_failover_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "functionFailoverInput"))

    @builtins.property
    @jsii.member(jsii_name="gitCommentsInput")
    def git_comments_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, "ProjectGitComments"]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, "ProjectGitComments"]], jsii.get(self, "gitCommentsInput"))

    @builtins.property
    @jsii.member(jsii_name="gitForkProtectionInput")
    def git_fork_protection_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "gitForkProtectionInput"))

    @builtins.property
    @jsii.member(jsii_name="gitLfsInput")
    def git_lfs_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "gitLfsInput"))

    @builtins.property
    @jsii.member(jsii_name="gitRepositoryInput")
    def git_repository_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, "ProjectGitRepository"]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, "ProjectGitRepository"]], jsii.get(self, "gitRepositoryInput"))

    @builtins.property
    @jsii.member(jsii_name="ignoreCommandInput")
    def ignore_command_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ignoreCommandInput"))

    @builtins.property
    @jsii.member(jsii_name="installCommandInput")
    def install_command_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "installCommandInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="optionsAllowlistInput")
    def options_allowlist_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, "ProjectOptionsAllowlistStruct"]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, "ProjectOptionsAllowlistStruct"]], jsii.get(self, "optionsAllowlistInput"))

    @builtins.property
    @jsii.member(jsii_name="outputDirectoryInput")
    def output_directory_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "outputDirectoryInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordProtectionInput")
    def password_protection_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, "ProjectPasswordProtection"]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, "ProjectPasswordProtection"]], jsii.get(self, "passwordProtectionInput"))

    @builtins.property
    @jsii.member(jsii_name="previewCommentsInput")
    def preview_comments_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "previewCommentsInput"))

    @builtins.property
    @jsii.member(jsii_name="prioritiseProductionBuildsInput")
    def prioritise_production_builds_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "prioritiseProductionBuildsInput"))

    @builtins.property
    @jsii.member(jsii_name="protectionBypassForAutomationInput")
    def protection_bypass_for_automation_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "protectionBypassForAutomationInput"))

    @builtins.property
    @jsii.member(jsii_name="publicSourceInput")
    def public_source_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "publicSourceInput"))

    @builtins.property
    @jsii.member(jsii_name="rootDirectoryInput")
    def root_directory_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rootDirectoryInput"))

    @builtins.property
    @jsii.member(jsii_name="serverlessFunctionRegionInput")
    def serverless_function_region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverlessFunctionRegionInput"))

    @builtins.property
    @jsii.member(jsii_name="skewProtectionInput")
    def skew_protection_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "skewProtectionInput"))

    @builtins.property
    @jsii.member(jsii_name="teamIdInput")
    def team_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "teamIdInput"))

    @builtins.property
    @jsii.member(jsii_name="trustedIpsInput")
    def trusted_ips_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, "ProjectTrustedIps"]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, "ProjectTrustedIps"]], jsii.get(self, "trustedIpsInput"))

    @builtins.property
    @jsii.member(jsii_name="vercelAuthenticationInput")
    def vercel_authentication_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, "ProjectVercelAuthentication"]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, "ProjectVercelAuthentication"]], jsii.get(self, "vercelAuthenticationInput"))

    @builtins.property
    @jsii.member(jsii_name="autoAssignCustomDomains")
    def auto_assign_custom_domains(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "autoAssignCustomDomains"))

    @auto_assign_custom_domains.setter
    def auto_assign_custom_domains(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09bfbf8e6f6ca43b3b122c7c3146518746a1987f7a7b14739f4fc60a64a43ea2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoAssignCustomDomains", value)

    @builtins.property
    @jsii.member(jsii_name="automaticallyExposeSystemEnvironmentVariables")
    def automatically_expose_system_environment_variables(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "automaticallyExposeSystemEnvironmentVariables"))

    @automatically_expose_system_environment_variables.setter
    def automatically_expose_system_environment_variables(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__068aa71cba669f3882b84086964ec0c6e47861e57fa6d04e3b665854c4d26ee3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "automaticallyExposeSystemEnvironmentVariables", value)

    @builtins.property
    @jsii.member(jsii_name="buildCommand")
    def build_command(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "buildCommand"))

    @build_command.setter
    def build_command(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d5183aaafec140e6e26bae9613ed8520c55434c44f9fc2dc5d2f334b5a37f0d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "buildCommand", value)

    @builtins.property
    @jsii.member(jsii_name="customerSuccessCodeVisibility")
    def customer_success_code_visibility(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "customerSuccessCodeVisibility"))

    @customer_success_code_visibility.setter
    def customer_success_code_visibility(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc27cb3ce9f9bb9bf72439bdf683f8b3dfa55d5c3cafac26ec0349de290f04de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customerSuccessCodeVisibility", value)

    @builtins.property
    @jsii.member(jsii_name="devCommand")
    def dev_command(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "devCommand"))

    @dev_command.setter
    def dev_command(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb87e28cdb173f7b784cfe7f12150f4b82422e68d28604d3c0e5bce7b7f249db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "devCommand", value)

    @builtins.property
    @jsii.member(jsii_name="directoryListing")
    def directory_listing(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "directoryListing"))

    @directory_listing.setter
    def directory_listing(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0bf6dca47f5804f65d6afe1dc5738799e7c864ae7e7a7991ac563b7d133f06ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "directoryListing", value)

    @builtins.property
    @jsii.member(jsii_name="framework")
    def framework(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "framework"))

    @framework.setter
    def framework(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51827abcf9778d12beddbc8f34de36c228051b8caeceb29bd3351b35fa3bbbd9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "framework", value)

    @builtins.property
    @jsii.member(jsii_name="functionFailover")
    def function_failover(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "functionFailover"))

    @function_failover.setter
    def function_failover(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34366b3ce639dddbb2ab1178e5c5ed2557429f25224d2f75d3e4b7dbf65f9705)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "functionFailover", value)

    @builtins.property
    @jsii.member(jsii_name="gitForkProtection")
    def git_fork_protection(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "gitForkProtection"))

    @git_fork_protection.setter
    def git_fork_protection(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02f0ccfe143334b4e12810c6f5d8218689356ede28e9ab92ad565a86f7fdb285)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gitForkProtection", value)

    @builtins.property
    @jsii.member(jsii_name="gitLfs")
    def git_lfs(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "gitLfs"))

    @git_lfs.setter
    def git_lfs(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c443cbfa5ee0e85b55b79771a38a0275e4c91df83a5b1cccebb16060ed0e9e60)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gitLfs", value)

    @builtins.property
    @jsii.member(jsii_name="ignoreCommand")
    def ignore_command(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ignoreCommand"))

    @ignore_command.setter
    def ignore_command(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__796107b9a0d53427b537b237e3289b7141c5344f4061ac2de0a98a8e93c65deb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreCommand", value)

    @builtins.property
    @jsii.member(jsii_name="installCommand")
    def install_command(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "installCommand"))

    @install_command.setter
    def install_command(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4cda279aa1b70e174a4db7072b8192a243dd8b33048bde624e43a18ab2448e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "installCommand", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ebf7404659daa7380581c5ac9a6f56159c7913f7cc1980b8eb5b1ee47c0c44c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="outputDirectory")
    def output_directory(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "outputDirectory"))

    @output_directory.setter
    def output_directory(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a13d461a009980c59038d6e9c582ce0be03b8e3bdf8ec4e973af45c5d74cdd51)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outputDirectory", value)

    @builtins.property
    @jsii.member(jsii_name="previewComments")
    def preview_comments(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "previewComments"))

    @preview_comments.setter
    def preview_comments(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b104d19e2bd3888ca03d070073675bf200c2206ee8af7ae6eb55fa0940554a11)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "previewComments", value)

    @builtins.property
    @jsii.member(jsii_name="prioritiseProductionBuilds")
    def prioritise_production_builds(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "prioritiseProductionBuilds"))

    @prioritise_production_builds.setter
    def prioritise_production_builds(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9cea2430589eb6cf08532686cb0b1f9dcf17bf3befc766ec458802b255c1dde5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prioritiseProductionBuilds", value)

    @builtins.property
    @jsii.member(jsii_name="protectionBypassForAutomation")
    def protection_bypass_for_automation(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "protectionBypassForAutomation"))

    @protection_bypass_for_automation.setter
    def protection_bypass_for_automation(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8408b9a0c39839ac8f208377913136e1f483df0ab497e58b4a19716662610de2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protectionBypassForAutomation", value)

    @builtins.property
    @jsii.member(jsii_name="publicSource")
    def public_source(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "publicSource"))

    @public_source.setter
    def public_source(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d67090b7a7e8453f11d8f19a96168acb4f26460573eb1cfdf214a2c276bb948f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicSource", value)

    @builtins.property
    @jsii.member(jsii_name="rootDirectory")
    def root_directory(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rootDirectory"))

    @root_directory.setter
    def root_directory(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13c17dc380a755369354a3fa9e5a36762c0a2f49f4fe67a9c1705e859be973cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rootDirectory", value)

    @builtins.property
    @jsii.member(jsii_name="serverlessFunctionRegion")
    def serverless_function_region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serverlessFunctionRegion"))

    @serverless_function_region.setter
    def serverless_function_region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__325f3a842e938fdafe71a734ee50b3ffa1023ab32d72dc2f09e9b07c5d3e0f79)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverlessFunctionRegion", value)

    @builtins.property
    @jsii.member(jsii_name="skewProtection")
    def skew_protection(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "skewProtection"))

    @skew_protection.setter
    def skew_protection(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9933403f561ac28d60943d1781c968ad197d83bf4be25244ec132bb5ee65880c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skewProtection", value)

    @builtins.property
    @jsii.member(jsii_name="teamId")
    def team_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "teamId"))

    @team_id.setter
    def team_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c54663b4117ca93ee04db71b27b91288ec3da928b7c394e01974fb03a57a23b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "teamId", value)


@jsii.data_type(
    jsii_type="vercel.project.ProjectConfig",
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
        "auto_assign_custom_domains": "autoAssignCustomDomains",
        "automatically_expose_system_environment_variables": "automaticallyExposeSystemEnvironmentVariables",
        "build_command": "buildCommand",
        "customer_success_code_visibility": "customerSuccessCodeVisibility",
        "dev_command": "devCommand",
        "directory_listing": "directoryListing",
        "environment": "environment",
        "framework": "framework",
        "function_failover": "functionFailover",
        "git_comments": "gitComments",
        "git_fork_protection": "gitForkProtection",
        "git_lfs": "gitLfs",
        "git_repository": "gitRepository",
        "ignore_command": "ignoreCommand",
        "install_command": "installCommand",
        "options_allowlist": "optionsAllowlist",
        "output_directory": "outputDirectory",
        "password_protection": "passwordProtection",
        "preview_comments": "previewComments",
        "prioritise_production_builds": "prioritiseProductionBuilds",
        "protection_bypass_for_automation": "protectionBypassForAutomation",
        "public_source": "publicSource",
        "root_directory": "rootDirectory",
        "serverless_function_region": "serverlessFunctionRegion",
        "skew_protection": "skewProtection",
        "team_id": "teamId",
        "trusted_ips": "trustedIps",
        "vercel_authentication": "vercelAuthentication",
    },
)
class ProjectConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        auto_assign_custom_domains: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        automatically_expose_system_environment_variables: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        build_command: typing.Optional[builtins.str] = None,
        customer_success_code_visibility: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        dev_command: typing.Optional[builtins.str] = None,
        directory_listing: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        environment: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ProjectEnvironment", typing.Dict[builtins.str, typing.Any]]]]] = None,
        framework: typing.Optional[builtins.str] = None,
        function_failover: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        git_comments: typing.Optional[typing.Union["ProjectGitComments", typing.Dict[builtins.str, typing.Any]]] = None,
        git_fork_protection: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        git_lfs: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        git_repository: typing.Optional[typing.Union["ProjectGitRepository", typing.Dict[builtins.str, typing.Any]]] = None,
        ignore_command: typing.Optional[builtins.str] = None,
        install_command: typing.Optional[builtins.str] = None,
        options_allowlist: typing.Optional[typing.Union["ProjectOptionsAllowlistStruct", typing.Dict[builtins.str, typing.Any]]] = None,
        output_directory: typing.Optional[builtins.str] = None,
        password_protection: typing.Optional[typing.Union["ProjectPasswordProtection", typing.Dict[builtins.str, typing.Any]]] = None,
        preview_comments: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        prioritise_production_builds: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        protection_bypass_for_automation: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        public_source: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        root_directory: typing.Optional[builtins.str] = None,
        serverless_function_region: typing.Optional[builtins.str] = None,
        skew_protection: typing.Optional[builtins.str] = None,
        team_id: typing.Optional[builtins.str] = None,
        trusted_ips: typing.Optional[typing.Union["ProjectTrustedIps", typing.Dict[builtins.str, typing.Any]]] = None,
        vercel_authentication: typing.Optional[typing.Union["ProjectVercelAuthentication", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: The desired name for the project. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#name Project#name}
        :param auto_assign_custom_domains: Automatically assign custom production domains after each Production deployment via merge to the production branch or Vercel CLI deploy with --prod. Defaults to ``true`` Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#auto_assign_custom_domains Project#auto_assign_custom_domains}
        :param automatically_expose_system_environment_variables: Vercel provides a set of Environment Variables that are automatically populated by the System, such as the URL of the Deployment or the name of the Git branch deployed. To expose them to your Deployments, enable this field Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#automatically_expose_system_environment_variables Project#automatically_expose_system_environment_variables}
        :param build_command: The build command for this project. If omitted, this value will be automatically detected. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#build_command Project#build_command}
        :param customer_success_code_visibility: Allows Vercel Customer Support to inspect all Deployments' source code in this project to assist with debugging. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#customer_success_code_visibility Project#customer_success_code_visibility}
        :param dev_command: The dev command for this project. If omitted, this value will be automatically detected. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#dev_command Project#dev_command}
        :param directory_listing: If no index file is present within a directory, the directory contents will be displayed. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#directory_listing Project#directory_listing}
        :param environment: A set of Environment Variables that should be configured for the project. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#environment Project#environment}
        :param framework: The framework that is being used for this project. If omitted, no framework is selected. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#framework Project#framework}
        :param function_failover: Automatically failover Serverless Functions to the nearest region. You can customize regions through vercel.json. A new Deployment is required for your changes to take effect. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#function_failover Project#function_failover}
        :param git_comments: Configuration for Git Comments. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#git_comments Project#git_comments}
        :param git_fork_protection: Ensures that pull requests targeting your Git repository must be authorized by a member of your Team before deploying if your Project has Environment Variables or if the pull request includes a change to vercel.json. Defaults to ``true``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#git_fork_protection Project#git_fork_protection}
        :param git_lfs: Enables Git LFS support. Git LFS replaces large files such as audio samples, videos, datasets, and graphics with text pointers inside Git, while storing the file contents on a remote server like GitHub.com or GitHub Enterprise. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#git_lfs Project#git_lfs}
        :param git_repository: The Git Repository that will be connected to the project. When this is defined, any pushes to the specified connected Git Repository will be automatically deployed. This requires the corresponding Vercel for `Github <https://vercel.com/docs/concepts/git/vercel-for-github>`_, `Gitlab <https://vercel.com/docs/concepts/git/vercel-for-gitlab>`_ or `Bitbucket <https://vercel.com/docs/concepts/git/vercel-for-bitbucket>`_ plugins to be installed. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#git_repository Project#git_repository}
        :param ignore_command: When a commit is pushed to the Git repository that is connected with your Project, its SHA will determine if a new Build has to be issued. If the SHA was deployed before, no new Build will be issued. You can customize this behavior with a command that exits with code 1 (new Build needed) or code 0. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#ignore_command Project#ignore_command}
        :param install_command: The install command for this project. If omitted, this value will be automatically detected. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#install_command Project#install_command}
        :param options_allowlist: Disable Deployment Protection for CORS preflight ``OPTIONS`` requests for a list of paths. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#options_allowlist Project#options_allowlist}
        :param output_directory: The output directory of the project. If omitted, this value will be automatically detected. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#output_directory Project#output_directory}
        :param password_protection: Ensures visitors of your Preview Deployments must enter a password in order to gain access. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#password_protection Project#password_protection}
        :param preview_comments: Whether to enable comments on your Preview Deployments. If omitted, comments are controlled at the team level (default behaviour). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#preview_comments Project#preview_comments}
        :param prioritise_production_builds: If enabled, builds for the Production environment will be prioritized over Preview environments. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#prioritise_production_builds Project#prioritise_production_builds}
        :param protection_bypass_for_automation: Allow automation services to bypass Vercel Authentication and Password Protection for both Preview and Production Deployments on this project when using an HTTP header named ``x-vercel-protection-bypass`` with a value of the ``password_protection_for_automation_secret`` field. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#protection_bypass_for_automation Project#protection_bypass_for_automation}
        :param public_source: By default, visitors to the ``/_logs`` and ``/_src`` paths of your Production and Preview Deployments must log in with Vercel (requires being a member of your team) to see the Source, Logs and Deployment Status of your project. Setting ``public_source`` to ``true`` disables this behaviour, meaning the Source, Logs and Deployment Status can be publicly viewed. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#public_source Project#public_source}
        :param root_directory: The name of a directory or relative path to the source code of your project. If omitted, it will default to the project root. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#root_directory Project#root_directory}
        :param serverless_function_region: The region on Vercel's network to which your Serverless Functions are deployed. It should be close to any data source your Serverless Function might depend on. A new Deployment is required for your changes to take effect. Please see `Vercel's documentation <https://vercel.com/docs/concepts/edge-network/regions>`_ for a full list of regions. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#serverless_function_region Project#serverless_function_region}
        :param skew_protection: Ensures that outdated clients always fetch the correct version for a given deployment. This value defines how long Vercel keeps Skew Protection active. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#skew_protection Project#skew_protection}
        :param team_id: The team ID to add the project to. Required when configuring a team resource if a default team has not been set in the provider. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#team_id Project#team_id}
        :param trusted_ips: Ensures only visitors from an allowed IP address can access your deployment. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#trusted_ips Project#trusted_ips}
        :param vercel_authentication: Ensures visitors to your Preview Deployments are logged into Vercel and have a minimum of Viewer access on your team. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#vercel_authentication Project#vercel_authentication}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(git_comments, dict):
            git_comments = ProjectGitComments(**git_comments)
        if isinstance(git_repository, dict):
            git_repository = ProjectGitRepository(**git_repository)
        if isinstance(options_allowlist, dict):
            options_allowlist = ProjectOptionsAllowlistStruct(**options_allowlist)
        if isinstance(password_protection, dict):
            password_protection = ProjectPasswordProtection(**password_protection)
        if isinstance(trusted_ips, dict):
            trusted_ips = ProjectTrustedIps(**trusted_ips)
        if isinstance(vercel_authentication, dict):
            vercel_authentication = ProjectVercelAuthentication(**vercel_authentication)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4066b502f70d0adeea20900951ed8cb0053d0c63a9d4fb13365bdc1d5dd97b9d)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument auto_assign_custom_domains", value=auto_assign_custom_domains, expected_type=type_hints["auto_assign_custom_domains"])
            check_type(argname="argument automatically_expose_system_environment_variables", value=automatically_expose_system_environment_variables, expected_type=type_hints["automatically_expose_system_environment_variables"])
            check_type(argname="argument build_command", value=build_command, expected_type=type_hints["build_command"])
            check_type(argname="argument customer_success_code_visibility", value=customer_success_code_visibility, expected_type=type_hints["customer_success_code_visibility"])
            check_type(argname="argument dev_command", value=dev_command, expected_type=type_hints["dev_command"])
            check_type(argname="argument directory_listing", value=directory_listing, expected_type=type_hints["directory_listing"])
            check_type(argname="argument environment", value=environment, expected_type=type_hints["environment"])
            check_type(argname="argument framework", value=framework, expected_type=type_hints["framework"])
            check_type(argname="argument function_failover", value=function_failover, expected_type=type_hints["function_failover"])
            check_type(argname="argument git_comments", value=git_comments, expected_type=type_hints["git_comments"])
            check_type(argname="argument git_fork_protection", value=git_fork_protection, expected_type=type_hints["git_fork_protection"])
            check_type(argname="argument git_lfs", value=git_lfs, expected_type=type_hints["git_lfs"])
            check_type(argname="argument git_repository", value=git_repository, expected_type=type_hints["git_repository"])
            check_type(argname="argument ignore_command", value=ignore_command, expected_type=type_hints["ignore_command"])
            check_type(argname="argument install_command", value=install_command, expected_type=type_hints["install_command"])
            check_type(argname="argument options_allowlist", value=options_allowlist, expected_type=type_hints["options_allowlist"])
            check_type(argname="argument output_directory", value=output_directory, expected_type=type_hints["output_directory"])
            check_type(argname="argument password_protection", value=password_protection, expected_type=type_hints["password_protection"])
            check_type(argname="argument preview_comments", value=preview_comments, expected_type=type_hints["preview_comments"])
            check_type(argname="argument prioritise_production_builds", value=prioritise_production_builds, expected_type=type_hints["prioritise_production_builds"])
            check_type(argname="argument protection_bypass_for_automation", value=protection_bypass_for_automation, expected_type=type_hints["protection_bypass_for_automation"])
            check_type(argname="argument public_source", value=public_source, expected_type=type_hints["public_source"])
            check_type(argname="argument root_directory", value=root_directory, expected_type=type_hints["root_directory"])
            check_type(argname="argument serverless_function_region", value=serverless_function_region, expected_type=type_hints["serverless_function_region"])
            check_type(argname="argument skew_protection", value=skew_protection, expected_type=type_hints["skew_protection"])
            check_type(argname="argument team_id", value=team_id, expected_type=type_hints["team_id"])
            check_type(argname="argument trusted_ips", value=trusted_ips, expected_type=type_hints["trusted_ips"])
            check_type(argname="argument vercel_authentication", value=vercel_authentication, expected_type=type_hints["vercel_authentication"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
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
        if auto_assign_custom_domains is not None:
            self._values["auto_assign_custom_domains"] = auto_assign_custom_domains
        if automatically_expose_system_environment_variables is not None:
            self._values["automatically_expose_system_environment_variables"] = automatically_expose_system_environment_variables
        if build_command is not None:
            self._values["build_command"] = build_command
        if customer_success_code_visibility is not None:
            self._values["customer_success_code_visibility"] = customer_success_code_visibility
        if dev_command is not None:
            self._values["dev_command"] = dev_command
        if directory_listing is not None:
            self._values["directory_listing"] = directory_listing
        if environment is not None:
            self._values["environment"] = environment
        if framework is not None:
            self._values["framework"] = framework
        if function_failover is not None:
            self._values["function_failover"] = function_failover
        if git_comments is not None:
            self._values["git_comments"] = git_comments
        if git_fork_protection is not None:
            self._values["git_fork_protection"] = git_fork_protection
        if git_lfs is not None:
            self._values["git_lfs"] = git_lfs
        if git_repository is not None:
            self._values["git_repository"] = git_repository
        if ignore_command is not None:
            self._values["ignore_command"] = ignore_command
        if install_command is not None:
            self._values["install_command"] = install_command
        if options_allowlist is not None:
            self._values["options_allowlist"] = options_allowlist
        if output_directory is not None:
            self._values["output_directory"] = output_directory
        if password_protection is not None:
            self._values["password_protection"] = password_protection
        if preview_comments is not None:
            self._values["preview_comments"] = preview_comments
        if prioritise_production_builds is not None:
            self._values["prioritise_production_builds"] = prioritise_production_builds
        if protection_bypass_for_automation is not None:
            self._values["protection_bypass_for_automation"] = protection_bypass_for_automation
        if public_source is not None:
            self._values["public_source"] = public_source
        if root_directory is not None:
            self._values["root_directory"] = root_directory
        if serverless_function_region is not None:
            self._values["serverless_function_region"] = serverless_function_region
        if skew_protection is not None:
            self._values["skew_protection"] = skew_protection
        if team_id is not None:
            self._values["team_id"] = team_id
        if trusted_ips is not None:
            self._values["trusted_ips"] = trusted_ips
        if vercel_authentication is not None:
            self._values["vercel_authentication"] = vercel_authentication

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
        '''The desired name for the project.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#name Project#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auto_assign_custom_domains(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Automatically assign custom production domains after each Production deployment via merge to the production branch or Vercel CLI deploy with --prod.

        Defaults to ``true``

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#auto_assign_custom_domains Project#auto_assign_custom_domains}
        '''
        result = self._values.get("auto_assign_custom_domains")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def automatically_expose_system_environment_variables(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Vercel provides a set of Environment Variables that are automatically populated by the System, such as the URL of the Deployment or the name of the Git branch deployed.

        To expose them to your Deployments, enable this field

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#automatically_expose_system_environment_variables Project#automatically_expose_system_environment_variables}
        '''
        result = self._values.get("automatically_expose_system_environment_variables")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def build_command(self) -> typing.Optional[builtins.str]:
        '''The build command for this project. If omitted, this value will be automatically detected.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#build_command Project#build_command}
        '''
        result = self._values.get("build_command")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def customer_success_code_visibility(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Allows Vercel Customer Support to inspect all Deployments' source code in this project to assist with debugging.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#customer_success_code_visibility Project#customer_success_code_visibility}
        '''
        result = self._values.get("customer_success_code_visibility")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def dev_command(self) -> typing.Optional[builtins.str]:
        '''The dev command for this project. If omitted, this value will be automatically detected.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#dev_command Project#dev_command}
        '''
        result = self._values.get("dev_command")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def directory_listing(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''If no index file is present within a directory, the directory contents will be displayed.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#directory_listing Project#directory_listing}
        '''
        result = self._values.get("directory_listing")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def environment(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ProjectEnvironment"]]]:
        '''A set of Environment Variables that should be configured for the project.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#environment Project#environment}
        '''
        result = self._values.get("environment")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ProjectEnvironment"]]], result)

    @builtins.property
    def framework(self) -> typing.Optional[builtins.str]:
        '''The framework that is being used for this project. If omitted, no framework is selected.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#framework Project#framework}
        '''
        result = self._values.get("framework")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def function_failover(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Automatically failover Serverless Functions to the nearest region.

        You can customize regions through vercel.json. A new Deployment is required for your changes to take effect.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#function_failover Project#function_failover}
        '''
        result = self._values.get("function_failover")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def git_comments(self) -> typing.Optional["ProjectGitComments"]:
        '''Configuration for Git Comments.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#git_comments Project#git_comments}
        '''
        result = self._values.get("git_comments")
        return typing.cast(typing.Optional["ProjectGitComments"], result)

    @builtins.property
    def git_fork_protection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Ensures that pull requests targeting your Git repository must be authorized by a member of your Team before deploying if your Project has Environment Variables or if the pull request includes a change to vercel.json. Defaults to ``true``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#git_fork_protection Project#git_fork_protection}
        '''
        result = self._values.get("git_fork_protection")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def git_lfs(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Enables Git LFS support.

        Git LFS replaces large files such as audio samples, videos, datasets, and graphics with text pointers inside Git, while storing the file contents on a remote server like GitHub.com or GitHub Enterprise.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#git_lfs Project#git_lfs}
        '''
        result = self._values.get("git_lfs")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def git_repository(self) -> typing.Optional["ProjectGitRepository"]:
        '''The Git Repository that will be connected to the project.

        When this is defined, any pushes to the specified connected Git Repository will be automatically deployed. This requires the corresponding Vercel for `Github <https://vercel.com/docs/concepts/git/vercel-for-github>`_, `Gitlab <https://vercel.com/docs/concepts/git/vercel-for-gitlab>`_ or `Bitbucket <https://vercel.com/docs/concepts/git/vercel-for-bitbucket>`_ plugins to be installed.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#git_repository Project#git_repository}
        '''
        result = self._values.get("git_repository")
        return typing.cast(typing.Optional["ProjectGitRepository"], result)

    @builtins.property
    def ignore_command(self) -> typing.Optional[builtins.str]:
        '''When a commit is pushed to the Git repository that is connected with your Project, its SHA will determine if a new Build has to be issued.

        If the SHA was deployed before, no new Build will be issued. You can customize this behavior with a command that exits with code 1 (new Build needed) or code 0.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#ignore_command Project#ignore_command}
        '''
        result = self._values.get("ignore_command")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def install_command(self) -> typing.Optional[builtins.str]:
        '''The install command for this project. If omitted, this value will be automatically detected.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#install_command Project#install_command}
        '''
        result = self._values.get("install_command")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def options_allowlist(self) -> typing.Optional["ProjectOptionsAllowlistStruct"]:
        '''Disable Deployment Protection for CORS preflight ``OPTIONS`` requests for a list of paths.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#options_allowlist Project#options_allowlist}
        '''
        result = self._values.get("options_allowlist")
        return typing.cast(typing.Optional["ProjectOptionsAllowlistStruct"], result)

    @builtins.property
    def output_directory(self) -> typing.Optional[builtins.str]:
        '''The output directory of the project. If omitted, this value will be automatically detected.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#output_directory Project#output_directory}
        '''
        result = self._values.get("output_directory")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def password_protection(self) -> typing.Optional["ProjectPasswordProtection"]:
        '''Ensures visitors of your Preview Deployments must enter a password in order to gain access.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#password_protection Project#password_protection}
        '''
        result = self._values.get("password_protection")
        return typing.cast(typing.Optional["ProjectPasswordProtection"], result)

    @builtins.property
    def preview_comments(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to enable comments on your Preview Deployments. If omitted, comments are controlled at the team level (default behaviour).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#preview_comments Project#preview_comments}
        '''
        result = self._values.get("preview_comments")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def prioritise_production_builds(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''If enabled, builds for the Production environment will be prioritized over Preview environments.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#prioritise_production_builds Project#prioritise_production_builds}
        '''
        result = self._values.get("prioritise_production_builds")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def protection_bypass_for_automation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Allow automation services to bypass Vercel Authentication and Password Protection for both Preview and Production Deployments on this project when using an HTTP header named ``x-vercel-protection-bypass`` with a value of the ``password_protection_for_automation_secret`` field.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#protection_bypass_for_automation Project#protection_bypass_for_automation}
        '''
        result = self._values.get("protection_bypass_for_automation")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def public_source(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''By default, visitors to the ``/_logs`` and ``/_src`` paths of your Production and Preview Deployments must log in with Vercel (requires being a member of your team) to see the Source, Logs and Deployment Status of your project.

        Setting ``public_source`` to ``true`` disables this behaviour, meaning the Source, Logs and Deployment Status can be publicly viewed.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#public_source Project#public_source}
        '''
        result = self._values.get("public_source")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def root_directory(self) -> typing.Optional[builtins.str]:
        '''The name of a directory or relative path to the source code of your project.

        If omitted, it will default to the project root.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#root_directory Project#root_directory}
        '''
        result = self._values.get("root_directory")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def serverless_function_region(self) -> typing.Optional[builtins.str]:
        '''The region on Vercel's network to which your Serverless Functions are deployed.

        It should be close to any data source your Serverless Function might depend on. A new Deployment is required for your changes to take effect. Please see `Vercel's documentation <https://vercel.com/docs/concepts/edge-network/regions>`_ for a full list of regions.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#serverless_function_region Project#serverless_function_region}
        '''
        result = self._values.get("serverless_function_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def skew_protection(self) -> typing.Optional[builtins.str]:
        '''Ensures that outdated clients always fetch the correct version for a given deployment.

        This value defines how long Vercel keeps Skew Protection active.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#skew_protection Project#skew_protection}
        '''
        result = self._values.get("skew_protection")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def team_id(self) -> typing.Optional[builtins.str]:
        '''The team ID to add the project to.

        Required when configuring a team resource if a default team has not been set in the provider.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#team_id Project#team_id}
        '''
        result = self._values.get("team_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def trusted_ips(self) -> typing.Optional["ProjectTrustedIps"]:
        '''Ensures only visitors from an allowed IP address can access your deployment.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#trusted_ips Project#trusted_ips}
        '''
        result = self._values.get("trusted_ips")
        return typing.cast(typing.Optional["ProjectTrustedIps"], result)

    @builtins.property
    def vercel_authentication(self) -> typing.Optional["ProjectVercelAuthentication"]:
        '''Ensures visitors to your Preview Deployments are logged into Vercel and have a minimum of Viewer access on your team.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#vercel_authentication Project#vercel_authentication}
        '''
        result = self._values.get("vercel_authentication")
        return typing.cast(typing.Optional["ProjectVercelAuthentication"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProjectConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vercel.project.ProjectEnvironment",
    jsii_struct_bases=[],
    name_mapping={
        "key": "key",
        "target": "target",
        "value": "value",
        "git_branch": "gitBranch",
        "sensitive": "sensitive",
    },
)
class ProjectEnvironment:
    def __init__(
        self,
        *,
        key: builtins.str,
        target: typing.Sequence[builtins.str],
        value: builtins.str,
        git_branch: typing.Optional[builtins.str] = None,
        sensitive: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param key: The name of the Environment Variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#key Project#key}
        :param target: The environments that the Environment Variable should be present on. Valid targets are either ``production``, ``preview``, or ``development``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#target Project#target}
        :param value: The value of the Environment Variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#value Project#value}
        :param git_branch: The git branch of the Environment Variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#git_branch Project#git_branch}
        :param sensitive: Whether the Environment Variable is sensitive or not. (May be affected by a `team-wide environment variable policy <https://vercel.com/docs/projects/environment-variables/sensitive-environment-variables#environment-variables-policy>`_). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#sensitive Project#sensitive}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9907bb61c4e01d20bce819640f6f52f9e40b0a526df6e482cb92775ff273511b)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument git_branch", value=git_branch, expected_type=type_hints["git_branch"])
            check_type(argname="argument sensitive", value=sensitive, expected_type=type_hints["sensitive"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "target": target,
            "value": value,
        }
        if git_branch is not None:
            self._values["git_branch"] = git_branch
        if sensitive is not None:
            self._values["sensitive"] = sensitive

    @builtins.property
    def key(self) -> builtins.str:
        '''The name of the Environment Variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#key Project#key}
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target(self) -> typing.List[builtins.str]:
        '''The environments that the Environment Variable should be present on. Valid targets are either ``production``, ``preview``, or ``development``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#target Project#target}
        '''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def value(self) -> builtins.str:
        '''The value of the Environment Variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#value Project#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def git_branch(self) -> typing.Optional[builtins.str]:
        '''The git branch of the Environment Variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#git_branch Project#git_branch}
        '''
        result = self._values.get("git_branch")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sensitive(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether the Environment Variable is sensitive or not. (May be affected by a `team-wide environment variable policy <https://vercel.com/docs/projects/environment-variables/sensitive-environment-variables#environment-variables-policy>`_).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#sensitive Project#sensitive}
        '''
        result = self._values.get("sensitive")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProjectEnvironment(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ProjectEnvironmentList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="vercel.project.ProjectEnvironmentList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d6f28478f3f9d50eaf0845bccf989d4723e4c24302db9ab04733f9ad40d8e55e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ProjectEnvironmentOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c51e32a046690f213af2243880697b8e58f27e3e6c49c643bff230a9ce69ec9e)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ProjectEnvironmentOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__994cdb319b93dd96c55bb82029c889c53e299550e7d10c4f1ee6cf69519bf904)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a1fc0b0fc6beb24d921172c63e632f2c06fb9335313c8ea5b96f5d9f36a554b7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a71b560d92b3574a2844137532600ea387328d7c5f241b8ebc3e418c9b783534)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectEnvironment]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectEnvironment]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectEnvironment]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c9bd224e85d3ffcee5ea2691f889555724dd545bc36415fcf04c3a4e9735422)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ProjectEnvironmentOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="vercel.project.ProjectEnvironmentOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__df15c1a050b4dd329e3bb97486e40808f208424cd9ee083300650a93af8d6d13)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetGitBranch")
    def reset_git_branch(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGitBranch", []))

    @jsii.member(jsii_name="resetSensitive")
    def reset_sensitive(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSensitive", []))

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
            type_hints = typing.get_type_hints(_typecheckingstub__c224d5e4c4d0934b3f29c57f87b2bcff8c3f274b4e4e6eb184b99787e1c9c7dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gitBranch", value)

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d1405e8fe62c86db28fc6eca1c82232d61a84b36c517ec128087738efc359dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__0d194cf6f66b09d774f1d8d6c619462c4da099d6f39856b956016316e099eae7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sensitive", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "target"))

    @target.setter
    def target(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43eba72f9a6ef335b4714e5d0cdd28e8a2468a87fd49046f573e35dacae9af3a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30e2b969d9a2d094f69ad56117e7d41e849a4ad16907bbaffadeefb95918123c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectEnvironment]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectEnvironment]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectEnvironment]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77cde921e9ac1dde3572a40ab65546b86a2eb16742204a5d5fe20c27f6f1afdd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="vercel.project.ProjectGitComments",
    jsii_struct_bases=[],
    name_mapping={"on_commit": "onCommit", "on_pull_request": "onPullRequest"},
)
class ProjectGitComments:
    def __init__(
        self,
        *,
        on_commit: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        on_pull_request: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param on_commit: Whether Commit comments are enabled. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#on_commit Project#on_commit}
        :param on_pull_request: Whether Pull Request comments are enabled. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#on_pull_request Project#on_pull_request}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a81601ef9f0c9dfc987cfafec306d2316453d4dd70423949dc791f082a0f55d)
            check_type(argname="argument on_commit", value=on_commit, expected_type=type_hints["on_commit"])
            check_type(argname="argument on_pull_request", value=on_pull_request, expected_type=type_hints["on_pull_request"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "on_commit": on_commit,
            "on_pull_request": on_pull_request,
        }

    @builtins.property
    def on_commit(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Whether Commit comments are enabled.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#on_commit Project#on_commit}
        '''
        result = self._values.get("on_commit")
        assert result is not None, "Required property 'on_commit' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def on_pull_request(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Whether Pull Request comments are enabled.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#on_pull_request Project#on_pull_request}
        '''
        result = self._values.get("on_pull_request")
        assert result is not None, "Required property 'on_pull_request' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProjectGitComments(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ProjectGitCommentsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="vercel.project.ProjectGitCommentsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9e4113868bf26458e3a44b9c6bc2c089669070f038781c4e198fbd01cfd1db24)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="onCommitInput")
    def on_commit_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "onCommitInput"))

    @builtins.property
    @jsii.member(jsii_name="onPullRequestInput")
    def on_pull_request_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "onPullRequestInput"))

    @builtins.property
    @jsii.member(jsii_name="onCommit")
    def on_commit(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "onCommit"))

    @on_commit.setter
    def on_commit(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0037320d8bd2b94ad60f6b929d50589fc52281d98afc61d03e59f8eb60a598e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "onCommit", value)

    @builtins.property
    @jsii.member(jsii_name="onPullRequest")
    def on_pull_request(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "onPullRequest"))

    @on_pull_request.setter
    def on_pull_request(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7b7dc104ce87bfcd7cfba2f364dad6d13d33b44f8f1f007cb97f067134cc557)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "onPullRequest", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectGitComments]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectGitComments]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectGitComments]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ddba80e55173bb0ef1a09db9d42a97d4341398b30c16022d4b3eec958729bbe4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="vercel.project.ProjectGitRepository",
    jsii_struct_bases=[],
    name_mapping={
        "repo": "repo",
        "type": "type",
        "deploy_hooks": "deployHooks",
        "production_branch": "productionBranch",
    },
)
class ProjectGitRepository:
    def __init__(
        self,
        *,
        repo: builtins.str,
        type: builtins.str,
        deploy_hooks: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ProjectGitRepositoryDeployHooks", typing.Dict[builtins.str, typing.Any]]]]] = None,
        production_branch: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param repo: The name of the git repository. For example: ``vercel/next.js``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#repo Project#repo}
        :param type: The git provider of the repository. Must be either ``github``, ``gitlab``, or ``bitbucket``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#type Project#type}
        :param deploy_hooks: Deploy hooks are unique URLs that allow you to trigger a deployment of a given branch. See https://vercel.com/docs/deployments/deploy-hooks for full information. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#deploy_hooks Project#deploy_hooks}
        :param production_branch: By default, every commit pushed to the main branch will trigger a Production Deployment instead of the usual Preview Deployment. You can switch to a different branch here. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#production_branch Project#production_branch}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87e1d80fa17981d9673238df00bd57cdfffbd19a3dc00bc8fb01c77ae22178e3)
            check_type(argname="argument repo", value=repo, expected_type=type_hints["repo"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument deploy_hooks", value=deploy_hooks, expected_type=type_hints["deploy_hooks"])
            check_type(argname="argument production_branch", value=production_branch, expected_type=type_hints["production_branch"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "repo": repo,
            "type": type,
        }
        if deploy_hooks is not None:
            self._values["deploy_hooks"] = deploy_hooks
        if production_branch is not None:
            self._values["production_branch"] = production_branch

    @builtins.property
    def repo(self) -> builtins.str:
        '''The name of the git repository. For example: ``vercel/next.js``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#repo Project#repo}
        '''
        result = self._values.get("repo")
        assert result is not None, "Required property 'repo' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The git provider of the repository. Must be either ``github``, ``gitlab``, or ``bitbucket``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#type Project#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def deploy_hooks(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ProjectGitRepositoryDeployHooks"]]]:
        '''Deploy hooks are unique URLs that allow you to trigger a deployment of a given branch.

        See https://vercel.com/docs/deployments/deploy-hooks for full information.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#deploy_hooks Project#deploy_hooks}
        '''
        result = self._values.get("deploy_hooks")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ProjectGitRepositoryDeployHooks"]]], result)

    @builtins.property
    def production_branch(self) -> typing.Optional[builtins.str]:
        '''By default, every commit pushed to the main branch will trigger a Production Deployment instead of the usual Preview Deployment.

        You can switch to a different branch here.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#production_branch Project#production_branch}
        '''
        result = self._values.get("production_branch")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProjectGitRepository(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vercel.project.ProjectGitRepositoryDeployHooks",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "ref": "ref"},
)
class ProjectGitRepositoryDeployHooks:
    def __init__(self, *, name: builtins.str, ref: builtins.str) -> None:
        '''
        :param name: The name of the deploy hook. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#name Project#name}
        :param ref: The branch or commit hash that should be deployed. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#ref Project#ref}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9631eda8f7056207c3980cb0fd3329b067425182f3a28c71d13c50470d54ee79)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument ref", value=ref, expected_type=type_hints["ref"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "ref": ref,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the deploy hook.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#name Project#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ref(self) -> builtins.str:
        '''The branch or commit hash that should be deployed.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#ref Project#ref}
        '''
        result = self._values.get("ref")
        assert result is not None, "Required property 'ref' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProjectGitRepositoryDeployHooks(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ProjectGitRepositoryDeployHooksList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="vercel.project.ProjectGitRepositoryDeployHooksList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0c32b1935d118ac7e7e3a5b62534e30667f74928ae462c30c0ca1c8e5f342d31)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ProjectGitRepositoryDeployHooksOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c1758ab6ac8134c22793d5b420e3a80a9366a3f5b64f6d164db65d56ec125e2)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ProjectGitRepositoryDeployHooksOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17a38f79955fac2c2d5e8485ccc82edab783bb7374fe347975f398e3b3df876b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8511de7cf0331dabb6d2614614f3231f29c7ba7ff642c2880fd657402517e92e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__32a760ae1b3c9c3f3bb129286f735500acad6d3f75e4df21ad2f18cb5f17de61)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectGitRepositoryDeployHooks]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectGitRepositoryDeployHooks]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectGitRepositoryDeployHooks]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a10835ef6c0507ce540e1e8c6007cc5d060db43d2faf2bfb2d31d753394644b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ProjectGitRepositoryDeployHooksOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="vercel.project.ProjectGitRepositoryDeployHooksOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a2c3da7015c36883aa88fb3741f83a40812bb410c366ef226c5944e163455c54)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="refInput")
    def ref_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "refInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c4a8c1ec763d15df4d5f0e5f737600aaf2b356d98428e62a7571803028ea799)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="ref")
    def ref(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ref"))

    @ref.setter
    def ref(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b1f84f6406c8a92ef951b95399af1ea6223b2b10d1f728ea574411e02424a18)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ref", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectGitRepositoryDeployHooks]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectGitRepositoryDeployHooks]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectGitRepositoryDeployHooks]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a58db2eff26eb8af6abfa0d23aed83bf33eb3f11c98dd4cc6b5951972f9fe06e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ProjectGitRepositoryOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="vercel.project.ProjectGitRepositoryOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1875953fc88eb71c43e1df810a89e9c449bc27cf7f7c25e0283e077d93b21ce0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDeployHooks")
    def put_deploy_hooks(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ProjectGitRepositoryDeployHooks, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__701a90ed99d33e2ad4351644e0034fe33631e474475a8350f69eb4d01aebbca7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDeployHooks", [value]))

    @jsii.member(jsii_name="resetDeployHooks")
    def reset_deploy_hooks(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeployHooks", []))

    @jsii.member(jsii_name="resetProductionBranch")
    def reset_production_branch(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProductionBranch", []))

    @builtins.property
    @jsii.member(jsii_name="deployHooks")
    def deploy_hooks(self) -> ProjectGitRepositoryDeployHooksList:
        return typing.cast(ProjectGitRepositoryDeployHooksList, jsii.get(self, "deployHooks"))

    @builtins.property
    @jsii.member(jsii_name="deployHooksInput")
    def deploy_hooks_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectGitRepositoryDeployHooks]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectGitRepositoryDeployHooks]]], jsii.get(self, "deployHooksInput"))

    @builtins.property
    @jsii.member(jsii_name="productionBranchInput")
    def production_branch_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "productionBranchInput"))

    @builtins.property
    @jsii.member(jsii_name="repoInput")
    def repo_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repoInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="productionBranch")
    def production_branch(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "productionBranch"))

    @production_branch.setter
    def production_branch(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ff1e1e0c7ac4168e2e8c0bdc587dd9f00a2dd63f5e5376049d8cc19e4bd29ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "productionBranch", value)

    @builtins.property
    @jsii.member(jsii_name="repo")
    def repo(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repo"))

    @repo.setter
    def repo(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bee62eb81bba5ed900772b88586e10c54b5a85bb979a826de62738e2a3ed3592)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repo", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68c71286b6998637c41d232b023c530b8b9f5285b9646ca3176ca2cd979042a5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectGitRepository]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectGitRepository]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectGitRepository]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3404d4dec26e843a4f4be4703b237f7cb25a42a3c358eb80a04d90925e9929f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="vercel.project.ProjectOptionsAllowlistPaths",
    jsii_struct_bases=[],
    name_mapping={"value": "value"},
)
class ProjectOptionsAllowlistPaths:
    def __init__(self, *, value: builtins.str) -> None:
        '''
        :param value: The path prefix to compare with the incoming request path. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#value Project#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c53a4f71024c918cb132ebe91fce6e28cd16124ab192ffa143f225c12d15f82b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "value": value,
        }

    @builtins.property
    def value(self) -> builtins.str:
        '''The path prefix to compare with the incoming request path.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#value Project#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProjectOptionsAllowlistPaths(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ProjectOptionsAllowlistPathsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="vercel.project.ProjectOptionsAllowlistPathsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5c833d08db0ba6ab0d7a4620a46e588eac75bf8604904a34f859c43d679bb952)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ProjectOptionsAllowlistPathsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b9259473b8e2f06e14024d952760ef0a47a6d98777308558f8e8e1e20cc02c2)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ProjectOptionsAllowlistPathsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ce9a5e5fe9adc05ad407eadf14358f9a4a7a632c00f9cf1eb0fd61a30566ea9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9a4284f38751dc2f8abc6792118032d99421bbce616b1f82372b18443a836797)
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
            type_hints = typing.get_type_hints(_typecheckingstub__cc6ed0e6ccf86f0d9339ee4e30dae0bfbaacf221fe995cd6511adad56023a81a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectOptionsAllowlistPaths]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectOptionsAllowlistPaths]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectOptionsAllowlistPaths]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aefbbd0b6379ddd11f9a4b5df0e6dd57d0d0cb1b98a09ff5f0d83a45540e3165)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ProjectOptionsAllowlistPathsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="vercel.project.ProjectOptionsAllowlistPathsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__41f9b050d4f4f83c4242ffac98c1faf153dbf2e8ef37d23a49050c636ea8c6ee)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f1b5701e4f21ef72808258e2e5973d00218a0e814ed6e52f966b19533af21ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectOptionsAllowlistPaths]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectOptionsAllowlistPaths]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectOptionsAllowlistPaths]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5535dac4ea1bf51e9994c598bfc8b53bf1c320bcd96281a2726478fab319072d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="vercel.project.ProjectOptionsAllowlistStruct",
    jsii_struct_bases=[],
    name_mapping={"paths": "paths"},
)
class ProjectOptionsAllowlistStruct:
    def __init__(
        self,
        *,
        paths: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ProjectOptionsAllowlistPaths, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param paths: The allowed paths for the OPTIONS Allowlist. Incoming requests will bypass Deployment Protection if they have the method ``OPTIONS`` and **start with** one of the path values. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#paths Project#paths}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__116569af5d9b998b98017c50f724920329ac7265c333f34fd7ea1cae55a59f53)
            check_type(argname="argument paths", value=paths, expected_type=type_hints["paths"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "paths": paths,
        }

    @builtins.property
    def paths(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectOptionsAllowlistPaths]]:
        '''The allowed paths for the OPTIONS Allowlist.

        Incoming requests will bypass Deployment Protection if they have the method ``OPTIONS`` and **start with** one of the path values.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#paths Project#paths}
        '''
        result = self._values.get("paths")
        assert result is not None, "Required property 'paths' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectOptionsAllowlistPaths]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProjectOptionsAllowlistStruct(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ProjectOptionsAllowlistStructOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="vercel.project.ProjectOptionsAllowlistStructOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f1b2eb91af760585bbf50cedb7cae5edd5ecc53dee85981b659552aaf667ff19)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putPaths")
    def put_paths(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ProjectOptionsAllowlistPaths, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11c441276745bfebbb0edddfcb9612a6a67db0c2aa9547f1fe80d4d5372e2278)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPaths", [value]))

    @builtins.property
    @jsii.member(jsii_name="paths")
    def paths(self) -> ProjectOptionsAllowlistPathsList:
        return typing.cast(ProjectOptionsAllowlistPathsList, jsii.get(self, "paths"))

    @builtins.property
    @jsii.member(jsii_name="pathsInput")
    def paths_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectOptionsAllowlistPaths]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectOptionsAllowlistPaths]]], jsii.get(self, "pathsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectOptionsAllowlistStruct]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectOptionsAllowlistStruct]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectOptionsAllowlistStruct]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0181f76ac9aef24fcc8e991c8cf407b01310366323a74da46073fe26264345d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="vercel.project.ProjectPasswordProtection",
    jsii_struct_bases=[],
    name_mapping={"deployment_type": "deploymentType", "password": "password"},
)
class ProjectPasswordProtection:
    def __init__(
        self,
        *,
        deployment_type: builtins.str,
        password: builtins.str,
    ) -> None:
        '''
        :param deployment_type: The deployment environment to protect. Must be one of ``standard_protection``, ``all_deployments``, or ``only_preview_deployments``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#deployment_type Project#deployment_type}
        :param password: The password that visitors must enter to gain access to your Preview Deployments. Drift detection is not possible for this field. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#password Project#password}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c34019614cfbe77246cbe51d5a0beb44ae8abb92d97505901a89cc242f16028)
            check_type(argname="argument deployment_type", value=deployment_type, expected_type=type_hints["deployment_type"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "deployment_type": deployment_type,
            "password": password,
        }

    @builtins.property
    def deployment_type(self) -> builtins.str:
        '''The deployment environment to protect. Must be one of ``standard_protection``, ``all_deployments``, or ``only_preview_deployments``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#deployment_type Project#deployment_type}
        '''
        result = self._values.get("deployment_type")
        assert result is not None, "Required property 'deployment_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def password(self) -> builtins.str:
        '''The password that visitors must enter to gain access to your Preview Deployments.

        Drift detection is not possible for this field.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#password Project#password}
        '''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProjectPasswordProtection(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ProjectPasswordProtectionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="vercel.project.ProjectPasswordProtectionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1ce81478bc93bf2f3a68e1991dd33e5330aea6e8330f2a04eb06113849ffba32)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="deploymentTypeInput")
    def deployment_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deploymentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="deploymentType")
    def deployment_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deploymentType"))

    @deployment_type.setter
    def deployment_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__762eb28fd58c294659a5621de43acd6d013c214948971e67235d33db4e14df52)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deploymentType", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e359e56ffdd95efbc2479c9af54e4b2d675208340371f75cb71691e6cbd99e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectPasswordProtection]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectPasswordProtection]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectPasswordProtection]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9136ed2b29ba104b2f45d2e6a2e46e920bc86415df9eaa61e92b79f676a33c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="vercel.project.ProjectTrustedIps",
    jsii_struct_bases=[],
    name_mapping={
        "addresses": "addresses",
        "deployment_type": "deploymentType",
        "protection_mode": "protectionMode",
    },
)
class ProjectTrustedIps:
    def __init__(
        self,
        *,
        addresses: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ProjectTrustedIpsAddresses", typing.Dict[builtins.str, typing.Any]]]],
        deployment_type: builtins.str,
        protection_mode: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param addresses: The allowed IP addressses and CIDR ranges with optional descriptions. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#addresses Project#addresses}
        :param deployment_type: The deployment environment to protect. Must be one of ``standard_protection``, ``all_deployments``, ``only_production_deployments``, or ``only_preview_deployments``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#deployment_type Project#deployment_type}
        :param protection_mode: Whether or not Trusted IPs is optional to access a deployment. Must be either ``trusted_ip_required`` or ``trusted_ip_optional``. ``trusted_ip_optional`` is only available with Standalone Trusted IPs. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#protection_mode Project#protection_mode}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86234af8c1b1725c3855d9a10f640f683c8d5c80192c65a8c6848b183cab3890)
            check_type(argname="argument addresses", value=addresses, expected_type=type_hints["addresses"])
            check_type(argname="argument deployment_type", value=deployment_type, expected_type=type_hints["deployment_type"])
            check_type(argname="argument protection_mode", value=protection_mode, expected_type=type_hints["protection_mode"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "addresses": addresses,
            "deployment_type": deployment_type,
        }
        if protection_mode is not None:
            self._values["protection_mode"] = protection_mode

    @builtins.property
    def addresses(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ProjectTrustedIpsAddresses"]]:
        '''The allowed IP addressses and CIDR ranges with optional descriptions.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#addresses Project#addresses}
        '''
        result = self._values.get("addresses")
        assert result is not None, "Required property 'addresses' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ProjectTrustedIpsAddresses"]], result)

    @builtins.property
    def deployment_type(self) -> builtins.str:
        '''The deployment environment to protect. Must be one of ``standard_protection``, ``all_deployments``, ``only_production_deployments``, or ``only_preview_deployments``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#deployment_type Project#deployment_type}
        '''
        result = self._values.get("deployment_type")
        assert result is not None, "Required property 'deployment_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def protection_mode(self) -> typing.Optional[builtins.str]:
        '''Whether or not Trusted IPs is optional to access a deployment.

        Must be either ``trusted_ip_required`` or ``trusted_ip_optional``. ``trusted_ip_optional`` is only available with Standalone Trusted IPs.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#protection_mode Project#protection_mode}
        '''
        result = self._values.get("protection_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProjectTrustedIps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vercel.project.ProjectTrustedIpsAddresses",
    jsii_struct_bases=[],
    name_mapping={"value": "value", "note": "note"},
)
class ProjectTrustedIpsAddresses:
    def __init__(
        self,
        *,
        value: builtins.str,
        note: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param value: The address or CIDR range that can access deployments. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#value Project#value}
        :param note: A description for the value. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#note Project#note}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61f76a1c77124f90324b691d0fcb70d9d3a6eba86fb1d4061baf2f6fcaa8bce5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument note", value=note, expected_type=type_hints["note"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "value": value,
        }
        if note is not None:
            self._values["note"] = note

    @builtins.property
    def value(self) -> builtins.str:
        '''The address or CIDR range that can access deployments.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#value Project#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def note(self) -> typing.Optional[builtins.str]:
        '''A description for the value.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#note Project#note}
        '''
        result = self._values.get("note")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProjectTrustedIpsAddresses(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ProjectTrustedIpsAddressesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="vercel.project.ProjectTrustedIpsAddressesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a105a4523459994d46e08f9fb0bf521e91a6e87dbee1eb4375d45516c35e8b56)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ProjectTrustedIpsAddressesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3686216883190f2ff0946ace13800a243834dc3a71d61f612e29420dd99906d)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ProjectTrustedIpsAddressesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e6c7e6cd86c1856f656d41e8d22d5b7e19a35961bd80d43f33f64b59ec82f2d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ca980e95f69bcc86f5ab0ec0e91d2e53bffad574eaa7f71902a0b7c4f592a3a7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e81d3f9b93cd1bb3d5227a45c7596204392504cb30963aa1156aaa477503c55e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectTrustedIpsAddresses]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectTrustedIpsAddresses]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectTrustedIpsAddresses]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0bf771db323c2d0285d35b687e181649e7e473b258f9947490b7fa28a6866534)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ProjectTrustedIpsAddressesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="vercel.project.ProjectTrustedIpsAddressesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__795e0f8f5267de7bd50cc88094788e40fe57f18a9cc41fd901c80db78ca20fa7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetNote")
    def reset_note(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNote", []))

    @builtins.property
    @jsii.member(jsii_name="noteInput")
    def note_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "noteInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="note")
    def note(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "note"))

    @note.setter
    def note(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d72893cbfc5c7bab483fa79e697057f0f038492a45bf737fbcc267ef285f77e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "note", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6d0881e6d3a3701d172243d2399a5bc5bed3c827c0da09205978a4c82c36342)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectTrustedIpsAddresses]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectTrustedIpsAddresses]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectTrustedIpsAddresses]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd33363d650950c3114dfd93afceb95a13b953852ed01c23a6370aad05531d23)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ProjectTrustedIpsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="vercel.project.ProjectTrustedIpsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a4947a6cdea64e55e045fce9a0b90b79f1f3e713b805bb430fead888cd04dba3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAddresses")
    def put_addresses(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ProjectTrustedIpsAddresses, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d16065102234d6ad3cbd4bdecda5e4d7ceb465fa41eff46dcccd45126b81bbc0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAddresses", [value]))

    @jsii.member(jsii_name="resetProtectionMode")
    def reset_protection_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProtectionMode", []))

    @builtins.property
    @jsii.member(jsii_name="addresses")
    def addresses(self) -> ProjectTrustedIpsAddressesList:
        return typing.cast(ProjectTrustedIpsAddressesList, jsii.get(self, "addresses"))

    @builtins.property
    @jsii.member(jsii_name="addressesInput")
    def addresses_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectTrustedIpsAddresses]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectTrustedIpsAddresses]]], jsii.get(self, "addressesInput"))

    @builtins.property
    @jsii.member(jsii_name="deploymentTypeInput")
    def deployment_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deploymentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="protectionModeInput")
    def protection_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protectionModeInput"))

    @builtins.property
    @jsii.member(jsii_name="deploymentType")
    def deployment_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deploymentType"))

    @deployment_type.setter
    def deployment_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68d5233a0a3384529cad5e49954048a8c537ce782dd72e0560df5037ca9ddc1c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deploymentType", value)

    @builtins.property
    @jsii.member(jsii_name="protectionMode")
    def protection_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protectionMode"))

    @protection_mode.setter
    def protection_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8838e2189acd9a51ddb3544281d26059a974abbf46c24d6f0c19b2eaa6cd3e84)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protectionMode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectTrustedIps]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectTrustedIps]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectTrustedIps]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f13bfcd90dcaef70048a312f73e32f315271a1a723a1a3b1618df19dbc68a2fc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="vercel.project.ProjectVercelAuthentication",
    jsii_struct_bases=[],
    name_mapping={"deployment_type": "deploymentType"},
)
class ProjectVercelAuthentication:
    def __init__(self, *, deployment_type: builtins.str) -> None:
        '''
        :param deployment_type: The deployment environment to protect. Must be one of ``standard_protection``, ``all_deployments``, ``only_preview_deployments``, or ``none``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#deployment_type Project#deployment_type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fddaf5006c49c7ec25aec7a7d88e2a5d1b6a916198e9adc6937569fc466405d7)
            check_type(argname="argument deployment_type", value=deployment_type, expected_type=type_hints["deployment_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "deployment_type": deployment_type,
        }

    @builtins.property
    def deployment_type(self) -> builtins.str:
        '''The deployment environment to protect. Must be one of ``standard_protection``, ``all_deployments``, ``only_preview_deployments``, or ``none``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/project#deployment_type Project#deployment_type}
        '''
        result = self._values.get("deployment_type")
        assert result is not None, "Required property 'deployment_type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProjectVercelAuthentication(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ProjectVercelAuthenticationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="vercel.project.ProjectVercelAuthenticationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__974d7f4fc0875abe8746b38e4fa56422ab79c888c2f9b5595b92c804a8371776)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="deploymentTypeInput")
    def deployment_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deploymentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="deploymentType")
    def deployment_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deploymentType"))

    @deployment_type.setter
    def deployment_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__870d7c43d1334e8ca49a18f10550e5fe0d0fbb719ef3a093375715e9eba630ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deploymentType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectVercelAuthentication]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectVercelAuthentication]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectVercelAuthentication]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9cd94e19ce5963713c3aaebfb5bd5b9352fa6cbbc17c882163b79bec14b2cd4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Project",
    "ProjectConfig",
    "ProjectEnvironment",
    "ProjectEnvironmentList",
    "ProjectEnvironmentOutputReference",
    "ProjectGitComments",
    "ProjectGitCommentsOutputReference",
    "ProjectGitRepository",
    "ProjectGitRepositoryDeployHooks",
    "ProjectGitRepositoryDeployHooksList",
    "ProjectGitRepositoryDeployHooksOutputReference",
    "ProjectGitRepositoryOutputReference",
    "ProjectOptionsAllowlistPaths",
    "ProjectOptionsAllowlistPathsList",
    "ProjectOptionsAllowlistPathsOutputReference",
    "ProjectOptionsAllowlistStruct",
    "ProjectOptionsAllowlistStructOutputReference",
    "ProjectPasswordProtection",
    "ProjectPasswordProtectionOutputReference",
    "ProjectTrustedIps",
    "ProjectTrustedIpsAddresses",
    "ProjectTrustedIpsAddressesList",
    "ProjectTrustedIpsAddressesOutputReference",
    "ProjectTrustedIpsOutputReference",
    "ProjectVercelAuthentication",
    "ProjectVercelAuthenticationOutputReference",
]

publication.publish()

def _typecheckingstub__49c099ee126aad45fa06d4bd68c4f22a787cf4950c3cca80d1cc31a2fca9ec9b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    auto_assign_custom_domains: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    automatically_expose_system_environment_variables: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    build_command: typing.Optional[builtins.str] = None,
    customer_success_code_visibility: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    dev_command: typing.Optional[builtins.str] = None,
    directory_listing: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    environment: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ProjectEnvironment, typing.Dict[builtins.str, typing.Any]]]]] = None,
    framework: typing.Optional[builtins.str] = None,
    function_failover: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    git_comments: typing.Optional[typing.Union[ProjectGitComments, typing.Dict[builtins.str, typing.Any]]] = None,
    git_fork_protection: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    git_lfs: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    git_repository: typing.Optional[typing.Union[ProjectGitRepository, typing.Dict[builtins.str, typing.Any]]] = None,
    ignore_command: typing.Optional[builtins.str] = None,
    install_command: typing.Optional[builtins.str] = None,
    options_allowlist: typing.Optional[typing.Union[ProjectOptionsAllowlistStruct, typing.Dict[builtins.str, typing.Any]]] = None,
    output_directory: typing.Optional[builtins.str] = None,
    password_protection: typing.Optional[typing.Union[ProjectPasswordProtection, typing.Dict[builtins.str, typing.Any]]] = None,
    preview_comments: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    prioritise_production_builds: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    protection_bypass_for_automation: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    public_source: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    root_directory: typing.Optional[builtins.str] = None,
    serverless_function_region: typing.Optional[builtins.str] = None,
    skew_protection: typing.Optional[builtins.str] = None,
    team_id: typing.Optional[builtins.str] = None,
    trusted_ips: typing.Optional[typing.Union[ProjectTrustedIps, typing.Dict[builtins.str, typing.Any]]] = None,
    vercel_authentication: typing.Optional[typing.Union[ProjectVercelAuthentication, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__720fa96e1b043e5bc18f9be2793e78402b4c36f683ed7c5897912e3fd5e57265(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdab687584df13f5a66795d8385e6fae64c6873111ae3f11b02203a70530685e(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ProjectEnvironment, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09bfbf8e6f6ca43b3b122c7c3146518746a1987f7a7b14739f4fc60a64a43ea2(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__068aa71cba669f3882b84086964ec0c6e47861e57fa6d04e3b665854c4d26ee3(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d5183aaafec140e6e26bae9613ed8520c55434c44f9fc2dc5d2f334b5a37f0d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc27cb3ce9f9bb9bf72439bdf683f8b3dfa55d5c3cafac26ec0349de290f04de(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb87e28cdb173f7b784cfe7f12150f4b82422e68d28604d3c0e5bce7b7f249db(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0bf6dca47f5804f65d6afe1dc5738799e7c864ae7e7a7991ac563b7d133f06ae(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51827abcf9778d12beddbc8f34de36c228051b8caeceb29bd3351b35fa3bbbd9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34366b3ce639dddbb2ab1178e5c5ed2557429f25224d2f75d3e4b7dbf65f9705(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02f0ccfe143334b4e12810c6f5d8218689356ede28e9ab92ad565a86f7fdb285(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c443cbfa5ee0e85b55b79771a38a0275e4c91df83a5b1cccebb16060ed0e9e60(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__796107b9a0d53427b537b237e3289b7141c5344f4061ac2de0a98a8e93c65deb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4cda279aa1b70e174a4db7072b8192a243dd8b33048bde624e43a18ab2448e3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ebf7404659daa7380581c5ac9a6f56159c7913f7cc1980b8eb5b1ee47c0c44c6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a13d461a009980c59038d6e9c582ce0be03b8e3bdf8ec4e973af45c5d74cdd51(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b104d19e2bd3888ca03d070073675bf200c2206ee8af7ae6eb55fa0940554a11(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9cea2430589eb6cf08532686cb0b1f9dcf17bf3befc766ec458802b255c1dde5(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8408b9a0c39839ac8f208377913136e1f483df0ab497e58b4a19716662610de2(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d67090b7a7e8453f11d8f19a96168acb4f26460573eb1cfdf214a2c276bb948f(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13c17dc380a755369354a3fa9e5a36762c0a2f49f4fe67a9c1705e859be973cf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__325f3a842e938fdafe71a734ee50b3ffa1023ab32d72dc2f09e9b07c5d3e0f79(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9933403f561ac28d60943d1781c968ad197d83bf4be25244ec132bb5ee65880c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c54663b4117ca93ee04db71b27b91288ec3da928b7c394e01974fb03a57a23b9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4066b502f70d0adeea20900951ed8cb0053d0c63a9d4fb13365bdc1d5dd97b9d(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    auto_assign_custom_domains: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    automatically_expose_system_environment_variables: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    build_command: typing.Optional[builtins.str] = None,
    customer_success_code_visibility: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    dev_command: typing.Optional[builtins.str] = None,
    directory_listing: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    environment: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ProjectEnvironment, typing.Dict[builtins.str, typing.Any]]]]] = None,
    framework: typing.Optional[builtins.str] = None,
    function_failover: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    git_comments: typing.Optional[typing.Union[ProjectGitComments, typing.Dict[builtins.str, typing.Any]]] = None,
    git_fork_protection: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    git_lfs: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    git_repository: typing.Optional[typing.Union[ProjectGitRepository, typing.Dict[builtins.str, typing.Any]]] = None,
    ignore_command: typing.Optional[builtins.str] = None,
    install_command: typing.Optional[builtins.str] = None,
    options_allowlist: typing.Optional[typing.Union[ProjectOptionsAllowlistStruct, typing.Dict[builtins.str, typing.Any]]] = None,
    output_directory: typing.Optional[builtins.str] = None,
    password_protection: typing.Optional[typing.Union[ProjectPasswordProtection, typing.Dict[builtins.str, typing.Any]]] = None,
    preview_comments: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    prioritise_production_builds: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    protection_bypass_for_automation: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    public_source: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    root_directory: typing.Optional[builtins.str] = None,
    serverless_function_region: typing.Optional[builtins.str] = None,
    skew_protection: typing.Optional[builtins.str] = None,
    team_id: typing.Optional[builtins.str] = None,
    trusted_ips: typing.Optional[typing.Union[ProjectTrustedIps, typing.Dict[builtins.str, typing.Any]]] = None,
    vercel_authentication: typing.Optional[typing.Union[ProjectVercelAuthentication, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9907bb61c4e01d20bce819640f6f52f9e40b0a526df6e482cb92775ff273511b(
    *,
    key: builtins.str,
    target: typing.Sequence[builtins.str],
    value: builtins.str,
    git_branch: typing.Optional[builtins.str] = None,
    sensitive: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6f28478f3f9d50eaf0845bccf989d4723e4c24302db9ab04733f9ad40d8e55e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c51e32a046690f213af2243880697b8e58f27e3e6c49c643bff230a9ce69ec9e(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__994cdb319b93dd96c55bb82029c889c53e299550e7d10c4f1ee6cf69519bf904(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1fc0b0fc6beb24d921172c63e632f2c06fb9335313c8ea5b96f5d9f36a554b7(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a71b560d92b3574a2844137532600ea387328d7c5f241b8ebc3e418c9b783534(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c9bd224e85d3ffcee5ea2691f889555724dd545bc36415fcf04c3a4e9735422(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectEnvironment]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df15c1a050b4dd329e3bb97486e40808f208424cd9ee083300650a93af8d6d13(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c224d5e4c4d0934b3f29c57f87b2bcff8c3f274b4e4e6eb184b99787e1c9c7dc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d1405e8fe62c86db28fc6eca1c82232d61a84b36c517ec128087738efc359dc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d194cf6f66b09d774f1d8d6c619462c4da099d6f39856b956016316e099eae7(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43eba72f9a6ef335b4714e5d0cdd28e8a2468a87fd49046f573e35dacae9af3a(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30e2b969d9a2d094f69ad56117e7d41e849a4ad16907bbaffadeefb95918123c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77cde921e9ac1dde3572a40ab65546b86a2eb16742204a5d5fe20c27f6f1afdd(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectEnvironment]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a81601ef9f0c9dfc987cfafec306d2316453d4dd70423949dc791f082a0f55d(
    *,
    on_commit: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    on_pull_request: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e4113868bf26458e3a44b9c6bc2c089669070f038781c4e198fbd01cfd1db24(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0037320d8bd2b94ad60f6b929d50589fc52281d98afc61d03e59f8eb60a598e6(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7b7dc104ce87bfcd7cfba2f364dad6d13d33b44f8f1f007cb97f067134cc557(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddba80e55173bb0ef1a09db9d42a97d4341398b30c16022d4b3eec958729bbe4(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectGitComments]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87e1d80fa17981d9673238df00bd57cdfffbd19a3dc00bc8fb01c77ae22178e3(
    *,
    repo: builtins.str,
    type: builtins.str,
    deploy_hooks: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ProjectGitRepositoryDeployHooks, typing.Dict[builtins.str, typing.Any]]]]] = None,
    production_branch: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9631eda8f7056207c3980cb0fd3329b067425182f3a28c71d13c50470d54ee79(
    *,
    name: builtins.str,
    ref: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c32b1935d118ac7e7e3a5b62534e30667f74928ae462c30c0ca1c8e5f342d31(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c1758ab6ac8134c22793d5b420e3a80a9366a3f5b64f6d164db65d56ec125e2(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17a38f79955fac2c2d5e8485ccc82edab783bb7374fe347975f398e3b3df876b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8511de7cf0331dabb6d2614614f3231f29c7ba7ff642c2880fd657402517e92e(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32a760ae1b3c9c3f3bb129286f735500acad6d3f75e4df21ad2f18cb5f17de61(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a10835ef6c0507ce540e1e8c6007cc5d060db43d2faf2bfb2d31d753394644b2(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectGitRepositoryDeployHooks]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2c3da7015c36883aa88fb3741f83a40812bb410c366ef226c5944e163455c54(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c4a8c1ec763d15df4d5f0e5f737600aaf2b356d98428e62a7571803028ea799(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b1f84f6406c8a92ef951b95399af1ea6223b2b10d1f728ea574411e02424a18(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a58db2eff26eb8af6abfa0d23aed83bf33eb3f11c98dd4cc6b5951972f9fe06e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectGitRepositoryDeployHooks]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1875953fc88eb71c43e1df810a89e9c449bc27cf7f7c25e0283e077d93b21ce0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__701a90ed99d33e2ad4351644e0034fe33631e474475a8350f69eb4d01aebbca7(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ProjectGitRepositoryDeployHooks, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ff1e1e0c7ac4168e2e8c0bdc587dd9f00a2dd63f5e5376049d8cc19e4bd29ea(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bee62eb81bba5ed900772b88586e10c54b5a85bb979a826de62738e2a3ed3592(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68c71286b6998637c41d232b023c530b8b9f5285b9646ca3176ca2cd979042a5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3404d4dec26e843a4f4be4703b237f7cb25a42a3c358eb80a04d90925e9929f9(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectGitRepository]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c53a4f71024c918cb132ebe91fce6e28cd16124ab192ffa143f225c12d15f82b(
    *,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c833d08db0ba6ab0d7a4620a46e588eac75bf8604904a34f859c43d679bb952(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b9259473b8e2f06e14024d952760ef0a47a6d98777308558f8e8e1e20cc02c2(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ce9a5e5fe9adc05ad407eadf14358f9a4a7a632c00f9cf1eb0fd61a30566ea9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a4284f38751dc2f8abc6792118032d99421bbce616b1f82372b18443a836797(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc6ed0e6ccf86f0d9339ee4e30dae0bfbaacf221fe995cd6511adad56023a81a(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aefbbd0b6379ddd11f9a4b5df0e6dd57d0d0cb1b98a09ff5f0d83a45540e3165(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectOptionsAllowlistPaths]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41f9b050d4f4f83c4242ffac98c1faf153dbf2e8ef37d23a49050c636ea8c6ee(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f1b5701e4f21ef72808258e2e5973d00218a0e814ed6e52f966b19533af21ff(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5535dac4ea1bf51e9994c598bfc8b53bf1c320bcd96281a2726478fab319072d(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectOptionsAllowlistPaths]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__116569af5d9b998b98017c50f724920329ac7265c333f34fd7ea1cae55a59f53(
    *,
    paths: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ProjectOptionsAllowlistPaths, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1b2eb91af760585bbf50cedb7cae5edd5ecc53dee85981b659552aaf667ff19(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11c441276745bfebbb0edddfcb9612a6a67db0c2aa9547f1fe80d4d5372e2278(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ProjectOptionsAllowlistPaths, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0181f76ac9aef24fcc8e991c8cf407b01310366323a74da46073fe26264345d3(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectOptionsAllowlistStruct]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c34019614cfbe77246cbe51d5a0beb44ae8abb92d97505901a89cc242f16028(
    *,
    deployment_type: builtins.str,
    password: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ce81478bc93bf2f3a68e1991dd33e5330aea6e8330f2a04eb06113849ffba32(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__762eb28fd58c294659a5621de43acd6d013c214948971e67235d33db4e14df52(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e359e56ffdd95efbc2479c9af54e4b2d675208340371f75cb71691e6cbd99e1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9136ed2b29ba104b2f45d2e6a2e46e920bc86415df9eaa61e92b79f676a33c8(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectPasswordProtection]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86234af8c1b1725c3855d9a10f640f683c8d5c80192c65a8c6848b183cab3890(
    *,
    addresses: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ProjectTrustedIpsAddresses, typing.Dict[builtins.str, typing.Any]]]],
    deployment_type: builtins.str,
    protection_mode: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61f76a1c77124f90324b691d0fcb70d9d3a6eba86fb1d4061baf2f6fcaa8bce5(
    *,
    value: builtins.str,
    note: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a105a4523459994d46e08f9fb0bf521e91a6e87dbee1eb4375d45516c35e8b56(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3686216883190f2ff0946ace13800a243834dc3a71d61f612e29420dd99906d(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e6c7e6cd86c1856f656d41e8d22d5b7e19a35961bd80d43f33f64b59ec82f2d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca980e95f69bcc86f5ab0ec0e91d2e53bffad574eaa7f71902a0b7c4f592a3a7(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e81d3f9b93cd1bb3d5227a45c7596204392504cb30963aa1156aaa477503c55e(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0bf771db323c2d0285d35b687e181649e7e473b258f9947490b7fa28a6866534(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectTrustedIpsAddresses]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__795e0f8f5267de7bd50cc88094788e40fe57f18a9cc41fd901c80db78ca20fa7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d72893cbfc5c7bab483fa79e697057f0f038492a45bf737fbcc267ef285f77e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6d0881e6d3a3701d172243d2399a5bc5bed3c827c0da09205978a4c82c36342(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd33363d650950c3114dfd93afceb95a13b953852ed01c23a6370aad05531d23(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectTrustedIpsAddresses]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4947a6cdea64e55e045fce9a0b90b79f1f3e713b805bb430fead888cd04dba3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d16065102234d6ad3cbd4bdecda5e4d7ceb465fa41eff46dcccd45126b81bbc0(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ProjectTrustedIpsAddresses, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68d5233a0a3384529cad5e49954048a8c537ce782dd72e0560df5037ca9ddc1c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8838e2189acd9a51ddb3544281d26059a974abbf46c24d6f0c19b2eaa6cd3e84(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f13bfcd90dcaef70048a312f73e32f315271a1a723a1a3b1618df19dbc68a2fc(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectTrustedIps]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fddaf5006c49c7ec25aec7a7d88e2a5d1b6a916198e9adc6937569fc466405d7(
    *,
    deployment_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__974d7f4fc0875abe8746b38e4fa56422ab79c888c2f9b5595b92c804a8371776(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__870d7c43d1334e8ca49a18f10550e5fe0d0fbb719ef3a093375715e9eba630ce(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9cd94e19ce5963713c3aaebfb5bd5b9352fa6cbbc17c882163b79bec14b2cd4(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ProjectVercelAuthentication]],
) -> None:
    """Type checking stubs"""
    pass
