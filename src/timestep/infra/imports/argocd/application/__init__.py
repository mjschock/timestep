'''
# `argocd_application`

Refer to the Terraform Registory for docs: [`argocd_application`](https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application).
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


class Application(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.application.Application",
):
    '''Represents a {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application argocd_application}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        metadata: typing.Union["ApplicationMetadata", typing.Dict[builtins.str, typing.Any]],
        spec: typing.Union["ApplicationSpec", typing.Dict[builtins.str, typing.Any]],
        cascade: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["ApplicationTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        wait: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application argocd_application} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#metadata Application#metadata}
        :param spec: spec block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#spec Application#spec}
        :param cascade: Whether to applying cascading deletion when application is removed. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#cascade Application#cascade}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#id Application#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#timeouts Application#timeouts}
        :param wait: Upon application creation or update, wait for application health/sync status to be healthy/Synced, upon application deletion, wait for application to be removed, when set to true. Wait timeouts are controlled by Terraform Create, Update and Delete resource timeouts (all default to 5 minutes). **Note**: if ArgoCD decides not to sync an application (e.g. because the project to which the application belongs has a ``sync_window`` applied) then you will experience an expected timeout event if ``wait = true``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#wait Application#wait}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff2060e2db12056c6edfd8b05b5245c87e0ed133d702c76bb1f39740052edae3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ApplicationConfig(
            metadata=metadata,
            spec=spec,
            cascade=cascade,
            id=id,
            timeouts=timeouts,
            wait=wait,
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
        '''Generates CDKTF code for importing a Application resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the Application to import.
        :param import_from_id: The id of the existing Application that should be imported. Refer to the {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the Application to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8354a567245d0a18b236ea4b84300144d25413d265f7bc904b0374c52398799)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putMetadata")
    def put_metadata(
        self,
        *,
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param annotations: An unstructured key value map stored with the applications.argoproj.io that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#annotations Application#annotations}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the applications.argoproj.io. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#labels Application#labels}
        :param name: Name of the applications.argoproj.io, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#name Application#name}
        :param namespace: Namespace of the applications.argoproj.io, must be unique. Cannot be updated. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#namespace Application#namespace}
        '''
        value = ApplicationMetadata(
            annotations=annotations, labels=labels, name=name, namespace=namespace
        )

        return typing.cast(None, jsii.invoke(self, "putMetadata", [value]))

    @jsii.member(jsii_name="putSpec")
    def put_spec(
        self,
        *,
        destination: typing.Union["ApplicationSpecDestination", typing.Dict[builtins.str, typing.Any]],
        source: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ApplicationSpecSource", typing.Dict[builtins.str, typing.Any]]]],
        ignore_difference: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ApplicationSpecIgnoreDifference", typing.Dict[builtins.str, typing.Any]]]]] = None,
        info: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ApplicationSpecInfo", typing.Dict[builtins.str, typing.Any]]]]] = None,
        project: typing.Optional[builtins.str] = None,
        revision_history_limit: typing.Optional[jsii.Number] = None,
        sync_policy: typing.Optional[typing.Union["ApplicationSpecSyncPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param destination: destination block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#destination Application#destination}
        :param source: source block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#source Application#source}
        :param ignore_difference: ignore_difference block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#ignore_difference Application#ignore_difference}
        :param info: info block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#info Application#info}
        :param project: The project the application belongs to. Defaults to ``default``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#project Application#project}
        :param revision_history_limit: Limits the number of items kept in the application's revision history, which is used for informational purposes as well as for rollbacks to previous versions. This should only be changed in exceptional circumstances. Setting to zero will store no history. This will reduce storage used. Increasing will increase the space used to store the history, so we do not recommend increasing it. Default is 10. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#revision_history_limit Application#revision_history_limit}
        :param sync_policy: sync_policy block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#sync_policy Application#sync_policy}
        '''
        value = ApplicationSpec(
            destination=destination,
            source=source,
            ignore_difference=ignore_difference,
            info=info,
            project=project,
            revision_history_limit=revision_history_limit,
            sync_policy=sync_policy,
        )

        return typing.cast(None, jsii.invoke(self, "putSpec", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#create Application#create}.
        :param delete: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#delete Application#delete}.
        :param update: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#update Application#update}.
        '''
        value = ApplicationTimeouts(create=create, delete=delete, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetCascade")
    def reset_cascade(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCascade", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetWait")
    def reset_wait(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWait", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> "ApplicationMetadataOutputReference":
        return typing.cast("ApplicationMetadataOutputReference", jsii.get(self, "metadata"))

    @builtins.property
    @jsii.member(jsii_name="spec")
    def spec(self) -> "ApplicationSpecOutputReference":
        return typing.cast("ApplicationSpecOutputReference", jsii.get(self, "spec"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> "ApplicationStatusList":
        return typing.cast("ApplicationStatusList", jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "ApplicationTimeoutsOutputReference":
        return typing.cast("ApplicationTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="cascadeInput")
    def cascade_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "cascadeInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataInput")
    def metadata_input(self) -> typing.Optional["ApplicationMetadata"]:
        return typing.cast(typing.Optional["ApplicationMetadata"], jsii.get(self, "metadataInput"))

    @builtins.property
    @jsii.member(jsii_name="specInput")
    def spec_input(self) -> typing.Optional["ApplicationSpec"]:
        return typing.cast(typing.Optional["ApplicationSpec"], jsii.get(self, "specInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, "ApplicationTimeouts"]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, "ApplicationTimeouts"]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="waitInput")
    def wait_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "waitInput"))

    @builtins.property
    @jsii.member(jsii_name="cascade")
    def cascade(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "cascade"))

    @cascade.setter
    def cascade(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__053b48ff7396f7435e4fa88d9bbe0b94c2acdc2c7e61e2c81a8565007e1cf1a5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cascade", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b297bb4fb506ef8907df68284422087d5c670c98cf257a8602be9bae1e188b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="wait")
    def wait(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "wait"))

    @wait.setter
    def wait(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b141cee9ba1b0bd14e567dbaeae20a2c6db781e95b37c40265dc8144fc47fbf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wait", value)


@jsii.data_type(
    jsii_type="argocd.application.ApplicationConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "metadata": "metadata",
        "spec": "spec",
        "cascade": "cascade",
        "id": "id",
        "timeouts": "timeouts",
        "wait": "wait",
    },
)
class ApplicationConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        metadata: typing.Union["ApplicationMetadata", typing.Dict[builtins.str, typing.Any]],
        spec: typing.Union["ApplicationSpec", typing.Dict[builtins.str, typing.Any]],
        cascade: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["ApplicationTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        wait: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#metadata Application#metadata}
        :param spec: spec block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#spec Application#spec}
        :param cascade: Whether to applying cascading deletion when application is removed. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#cascade Application#cascade}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#id Application#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#timeouts Application#timeouts}
        :param wait: Upon application creation or update, wait for application health/sync status to be healthy/Synced, upon application deletion, wait for application to be removed, when set to true. Wait timeouts are controlled by Terraform Create, Update and Delete resource timeouts (all default to 5 minutes). **Note**: if ArgoCD decides not to sync an application (e.g. because the project to which the application belongs has a ``sync_window`` applied) then you will experience an expected timeout event if ``wait = true``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#wait Application#wait}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(metadata, dict):
            metadata = ApplicationMetadata(**metadata)
        if isinstance(spec, dict):
            spec = ApplicationSpec(**spec)
        if isinstance(timeouts, dict):
            timeouts = ApplicationTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__439a6f762db453a906fff9050680d3e514920bcdef53433337af2ecfad60171e)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument spec", value=spec, expected_type=type_hints["spec"])
            check_type(argname="argument cascade", value=cascade, expected_type=type_hints["cascade"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument wait", value=wait, expected_type=type_hints["wait"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "metadata": metadata,
            "spec": spec,
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
        if cascade is not None:
            self._values["cascade"] = cascade
        if id is not None:
            self._values["id"] = id
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if wait is not None:
            self._values["wait"] = wait

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
    def metadata(self) -> "ApplicationMetadata":
        '''metadata block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#metadata Application#metadata}
        '''
        result = self._values.get("metadata")
        assert result is not None, "Required property 'metadata' is missing"
        return typing.cast("ApplicationMetadata", result)

    @builtins.property
    def spec(self) -> "ApplicationSpec":
        '''spec block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#spec Application#spec}
        '''
        result = self._values.get("spec")
        assert result is not None, "Required property 'spec' is missing"
        return typing.cast("ApplicationSpec", result)

    @builtins.property
    def cascade(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to applying cascading deletion when application is removed.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#cascade Application#cascade}
        '''
        result = self._values.get("cascade")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#id Application#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["ApplicationTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#timeouts Application#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["ApplicationTimeouts"], result)

    @builtins.property
    def wait(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Upon application creation or update, wait for application health/sync status to be healthy/Synced, upon application deletion, wait for application to be removed, when set to true.

        Wait timeouts are controlled by Terraform Create, Update and Delete resource timeouts (all default to 5 minutes). **Note**: if ArgoCD decides not to sync an application (e.g. because the project to which the application belongs has a ``sync_window`` applied) then you will experience an expected timeout event if ``wait = true``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#wait Application#wait}
        '''
        result = self._values.get("wait")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="argocd.application.ApplicationMetadata",
    jsii_struct_bases=[],
    name_mapping={
        "annotations": "annotations",
        "labels": "labels",
        "name": "name",
        "namespace": "namespace",
    },
)
class ApplicationMetadata:
    def __init__(
        self,
        *,
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param annotations: An unstructured key value map stored with the applications.argoproj.io that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#annotations Application#annotations}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the applications.argoproj.io. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#labels Application#labels}
        :param name: Name of the applications.argoproj.io, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#name Application#name}
        :param namespace: Namespace of the applications.argoproj.io, must be unique. Cannot be updated. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#namespace Application#namespace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12ea5f81842268e5c2fb7092e46b5f2e8b9b3d4006534783a8da85ff74049579)
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if annotations is not None:
            self._values["annotations"] = annotations
        if labels is not None:
            self._values["labels"] = labels
        if name is not None:
            self._values["name"] = name
        if namespace is not None:
            self._values["namespace"] = namespace

    @builtins.property
    def annotations(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''An unstructured key value map stored with the applications.argoproj.io that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#annotations Application#annotations}
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Map of string keys and values that can be used to organize and categorize (scope and select) the applications.argoproj.io. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#labels Application#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the applications.argoproj.io, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#name Application#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Namespace of the applications.argoproj.io, must be unique. Cannot be updated. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#namespace Application#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationMetadata(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationMetadataOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.application.ApplicationMetadataOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3320f520ea709ddb87c7bbe756f53dbe41c62965e22c0e70a8d8b736aa99b96b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAnnotations")
    def reset_annotations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnnotations", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @builtins.property
    @jsii.member(jsii_name="generation")
    def generation(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "generation"))

    @builtins.property
    @jsii.member(jsii_name="resourceVersion")
    def resource_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceVersion"))

    @builtins.property
    @jsii.member(jsii_name="uid")
    def uid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uid"))

    @builtins.property
    @jsii.member(jsii_name="annotationsInput")
    def annotations_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "annotationsInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="annotations")
    def annotations(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "annotations"))

    @annotations.setter
    def annotations(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53a3ef0eed61a30f52f5589b61ac9fca8c6dca92188ef67c7229c1330f69b0d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "annotations", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f495be8bc7541447054583437a4a7af07a75fddc47f005e179d1874273047c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b344effed70d15e630d888e9c113c033823d214e4fc308ad86f67b011d51d69b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c02ae74fdc0c52dd0f328d4c880c36d143e2b979d1370c78849cab1d0cee9c37)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApplicationMetadata]:
        return typing.cast(typing.Optional[ApplicationMetadata], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ApplicationMetadata]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2bbdeac9cbcdf3c30071a9ba5625f2efcc79dcbf0b435e3a384e1a63cec5d7ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="argocd.application.ApplicationSpec",
    jsii_struct_bases=[],
    name_mapping={
        "destination": "destination",
        "source": "source",
        "ignore_difference": "ignoreDifference",
        "info": "info",
        "project": "project",
        "revision_history_limit": "revisionHistoryLimit",
        "sync_policy": "syncPolicy",
    },
)
class ApplicationSpec:
    def __init__(
        self,
        *,
        destination: typing.Union["ApplicationSpecDestination", typing.Dict[builtins.str, typing.Any]],
        source: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ApplicationSpecSource", typing.Dict[builtins.str, typing.Any]]]],
        ignore_difference: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ApplicationSpecIgnoreDifference", typing.Dict[builtins.str, typing.Any]]]]] = None,
        info: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ApplicationSpecInfo", typing.Dict[builtins.str, typing.Any]]]]] = None,
        project: typing.Optional[builtins.str] = None,
        revision_history_limit: typing.Optional[jsii.Number] = None,
        sync_policy: typing.Optional[typing.Union["ApplicationSpecSyncPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param destination: destination block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#destination Application#destination}
        :param source: source block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#source Application#source}
        :param ignore_difference: ignore_difference block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#ignore_difference Application#ignore_difference}
        :param info: info block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#info Application#info}
        :param project: The project the application belongs to. Defaults to ``default``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#project Application#project}
        :param revision_history_limit: Limits the number of items kept in the application's revision history, which is used for informational purposes as well as for rollbacks to previous versions. This should only be changed in exceptional circumstances. Setting to zero will store no history. This will reduce storage used. Increasing will increase the space used to store the history, so we do not recommend increasing it. Default is 10. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#revision_history_limit Application#revision_history_limit}
        :param sync_policy: sync_policy block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#sync_policy Application#sync_policy}
        '''
        if isinstance(destination, dict):
            destination = ApplicationSpecDestination(**destination)
        if isinstance(sync_policy, dict):
            sync_policy = ApplicationSpecSyncPolicy(**sync_policy)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12047fb70e97625aed3e2f1971053ec075ffaeb0b75d8f9e072fe6145f7d8a95)
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument ignore_difference", value=ignore_difference, expected_type=type_hints["ignore_difference"])
            check_type(argname="argument info", value=info, expected_type=type_hints["info"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument revision_history_limit", value=revision_history_limit, expected_type=type_hints["revision_history_limit"])
            check_type(argname="argument sync_policy", value=sync_policy, expected_type=type_hints["sync_policy"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination": destination,
            "source": source,
        }
        if ignore_difference is not None:
            self._values["ignore_difference"] = ignore_difference
        if info is not None:
            self._values["info"] = info
        if project is not None:
            self._values["project"] = project
        if revision_history_limit is not None:
            self._values["revision_history_limit"] = revision_history_limit
        if sync_policy is not None:
            self._values["sync_policy"] = sync_policy

    @builtins.property
    def destination(self) -> "ApplicationSpecDestination":
        '''destination block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#destination Application#destination}
        '''
        result = self._values.get("destination")
        assert result is not None, "Required property 'destination' is missing"
        return typing.cast("ApplicationSpecDestination", result)

    @builtins.property
    def source(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ApplicationSpecSource"]]:
        '''source block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#source Application#source}
        '''
        result = self._values.get("source")
        assert result is not None, "Required property 'source' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ApplicationSpecSource"]], result)

    @builtins.property
    def ignore_difference(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ApplicationSpecIgnoreDifference"]]]:
        '''ignore_difference block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#ignore_difference Application#ignore_difference}
        '''
        result = self._values.get("ignore_difference")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ApplicationSpecIgnoreDifference"]]], result)

    @builtins.property
    def info(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ApplicationSpecInfo"]]]:
        '''info block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#info Application#info}
        '''
        result = self._values.get("info")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ApplicationSpecInfo"]]], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''The project the application belongs to. Defaults to ``default``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#project Application#project}
        '''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def revision_history_limit(self) -> typing.Optional[jsii.Number]:
        '''Limits the number of items kept in the application's revision history, which is used for informational purposes as well as for rollbacks to previous versions.

        This should only be changed in exceptional circumstances. Setting to zero will store no history. This will reduce storage used. Increasing will increase the space used to store the history, so we do not recommend increasing it. Default is 10.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#revision_history_limit Application#revision_history_limit}
        '''
        result = self._values.get("revision_history_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def sync_policy(self) -> typing.Optional["ApplicationSpecSyncPolicy"]:
        '''sync_policy block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#sync_policy Application#sync_policy}
        '''
        result = self._values.get("sync_policy")
        return typing.cast(typing.Optional["ApplicationSpecSyncPolicy"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="argocd.application.ApplicationSpecDestination",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "namespace": "namespace", "server": "server"},
)
class ApplicationSpecDestination:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        server: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the target cluster. Can be used instead of ``server``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#name Application#name}
        :param namespace: Target namespace for the application's resources. The namespace will only be set for namespace-scoped resources that have not set a value for .metadata.namespace. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#namespace Application#namespace}
        :param server: URL of the target cluster and must be set to the Kubernetes control plane API. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#server Application#server}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4dd24961a7d63416c62e147aecefb2b2b4cce8ff6ebaa395d35e88481cc4b2fb)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument server", value=server, expected_type=type_hints["server"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if namespace is not None:
            self._values["namespace"] = namespace
        if server is not None:
            self._values["server"] = server

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the target cluster. Can be used instead of ``server``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#name Application#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Target namespace for the application's resources.

        The namespace will only be set for namespace-scoped resources that have not set a value for .metadata.namespace.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#namespace Application#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def server(self) -> typing.Optional[builtins.str]:
        '''URL of the target cluster and must be set to the Kubernetes control plane API.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#server Application#server}
        '''
        result = self._values.get("server")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationSpecDestination(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationSpecDestinationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.application.ApplicationSpecDestinationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__719bce6043ce804648a674ee3683e8ff86262c4bffd5c876c58baaaf646fb593)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @jsii.member(jsii_name="resetServer")
    def reset_server(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServer", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="serverInput")
    def server_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__473293ac11e0068ba7e9ede13b2fe1777b12d5d6aa0ab980a63b3fd83720be92)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af015e15cb8bdda37838de1f8e70ce1b9979f2f7a269307ab9f0989184d4258c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="server")
    def server(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "server"))

    @server.setter
    def server(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8fe609b4ab0a8c069aa48e51c2b40ed716ad5aecebf8f37dafdccba73f60d00f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "server", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApplicationSpecDestination]:
        return typing.cast(typing.Optional[ApplicationSpecDestination], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApplicationSpecDestination],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4254de5d3ff35f7cc8033b6fab8321603fd90afeba558dae4515ef44a922ae18)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="argocd.application.ApplicationSpecIgnoreDifference",
    jsii_struct_bases=[],
    name_mapping={
        "group": "group",
        "jq_path_expressions": "jqPathExpressions",
        "json_pointers": "jsonPointers",
        "kind": "kind",
        "name": "name",
        "namespace": "namespace",
    },
)
class ApplicationSpecIgnoreDifference:
    def __init__(
        self,
        *,
        group: typing.Optional[builtins.str] = None,
        jq_path_expressions: typing.Optional[typing.Sequence[builtins.str]] = None,
        json_pointers: typing.Optional[typing.Sequence[builtins.str]] = None,
        kind: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param group: The Kubernetes resource Group to match for. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#group Application#group}
        :param jq_path_expressions: List of JQ path expression strings targeting the field(s) to ignore. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#jq_path_expressions Application#jq_path_expressions}
        :param json_pointers: List of JSONPaths strings targeting the field(s) to ignore. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#json_pointers Application#json_pointers}
        :param kind: The Kubernetes resource Kind to match for. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#kind Application#kind}
        :param name: The Kubernetes resource Name to match for. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#name Application#name}
        :param namespace: The Kubernetes resource Namespace to match for. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#namespace Application#namespace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ef1b887193d869380370fa01aa4c450241f545f5b8f02621b707a1bff1b37ad)
            check_type(argname="argument group", value=group, expected_type=type_hints["group"])
            check_type(argname="argument jq_path_expressions", value=jq_path_expressions, expected_type=type_hints["jq_path_expressions"])
            check_type(argname="argument json_pointers", value=json_pointers, expected_type=type_hints["json_pointers"])
            check_type(argname="argument kind", value=kind, expected_type=type_hints["kind"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if group is not None:
            self._values["group"] = group
        if jq_path_expressions is not None:
            self._values["jq_path_expressions"] = jq_path_expressions
        if json_pointers is not None:
            self._values["json_pointers"] = json_pointers
        if kind is not None:
            self._values["kind"] = kind
        if name is not None:
            self._values["name"] = name
        if namespace is not None:
            self._values["namespace"] = namespace

    @builtins.property
    def group(self) -> typing.Optional[builtins.str]:
        '''The Kubernetes resource Group to match for.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#group Application#group}
        '''
        result = self._values.get("group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def jq_path_expressions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of JQ path expression strings targeting the field(s) to ignore.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#jq_path_expressions Application#jq_path_expressions}
        '''
        result = self._values.get("jq_path_expressions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def json_pointers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of JSONPaths strings targeting the field(s) to ignore.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#json_pointers Application#json_pointers}
        '''
        result = self._values.get("json_pointers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def kind(self) -> typing.Optional[builtins.str]:
        '''The Kubernetes resource Kind to match for.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#kind Application#kind}
        '''
        result = self._values.get("kind")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The Kubernetes resource Name to match for.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#name Application#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''The Kubernetes resource Namespace to match for.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#namespace Application#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationSpecIgnoreDifference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationSpecIgnoreDifferenceList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.application.ApplicationSpecIgnoreDifferenceList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f94bb0d3041263def2607283cf02b10204f1f1f80561e28859cfb13084b87090)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApplicationSpecIgnoreDifferenceOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__233cc7b59e49e3f4f49a232878f3646de6e1a05c645236c223d4d34095ee2ac3)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApplicationSpecIgnoreDifferenceOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__367774f0b63e9ec8af6d9caf0328a47c4c64b25883ce68cf2f55d54193b18079)
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
            type_hints = typing.get_type_hints(_typecheckingstub__149dba9dc5d8e68b95659c1c2eae0675bc02ab79da55c7c75f6cc79b384fbcea)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4cae609cd3c72a2f144c1c47eb5bf30e87f400634cee19345e696d3e8e81bc11)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ApplicationSpecIgnoreDifference]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ApplicationSpecIgnoreDifference]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ApplicationSpecIgnoreDifference]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__559e144a9bc52eda7a643a3d47d3333f2fd607ebd072d4cad821351b4241fe9b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationSpecIgnoreDifferenceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.application.ApplicationSpecIgnoreDifferenceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c79964aa9d48f5b057832a2bcd62b839f05d499dc5943154e866112b547e9ad4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetGroup")
    def reset_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroup", []))

    @jsii.member(jsii_name="resetJqPathExpressions")
    def reset_jq_path_expressions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJqPathExpressions", []))

    @jsii.member(jsii_name="resetJsonPointers")
    def reset_json_pointers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJsonPointers", []))

    @jsii.member(jsii_name="resetKind")
    def reset_kind(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKind", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @builtins.property
    @jsii.member(jsii_name="groupInput")
    def group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupInput"))

    @builtins.property
    @jsii.member(jsii_name="jqPathExpressionsInput")
    def jq_path_expressions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "jqPathExpressionsInput"))

    @builtins.property
    @jsii.member(jsii_name="jsonPointersInput")
    def json_pointers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "jsonPointersInput"))

    @builtins.property
    @jsii.member(jsii_name="kindInput")
    def kind_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kindInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="group")
    def group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "group"))

    @group.setter
    def group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc2516454797f80745ad7a5392b1cf019601ffc73bb4b4ac18863023e176ad88)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "group", value)

    @builtins.property
    @jsii.member(jsii_name="jqPathExpressions")
    def jq_path_expressions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "jqPathExpressions"))

    @jq_path_expressions.setter
    def jq_path_expressions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c0330d9dea81a5aa7463880f5a67445bab6e687c4fae8d4c7592280de21122d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jqPathExpressions", value)

    @builtins.property
    @jsii.member(jsii_name="jsonPointers")
    def json_pointers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "jsonPointers"))

    @json_pointers.setter
    def json_pointers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2936aa9aa32bcbf38199ddbcba4e31c45b94cfd36d0210bc578b62ae4e47dad9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jsonPointers", value)

    @builtins.property
    @jsii.member(jsii_name="kind")
    def kind(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kind"))

    @kind.setter
    def kind(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0da36795ca985a89da4eca5fbcb806009a7475efe9d277e5b18a4f6792a6a831)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kind", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61e274e4bba62121a1a8dd5c8607096a050b4dfc3c685c13f3a6202ee4c54a7e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1234b07c145430a578c70f4ce8e6884b78312b7632bdb03d95d2171a17512096)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ApplicationSpecIgnoreDifference]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ApplicationSpecIgnoreDifference]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ApplicationSpecIgnoreDifference]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73b92ee59e901bee9ad95ea401bda21211b4394ca1b0f165c8b57430933f46c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="argocd.application.ApplicationSpecInfo",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value"},
)
class ApplicationSpecInfo:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the information. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#name Application#name}
        :param value: Value of the information. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#value Application#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d8a5e81589680f910b4225b12a9dbf087ad1d165e54eeb83fad0dffba4827fc)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the information.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#name Application#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Value of the information.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#value Application#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationSpecInfo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationSpecInfoList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.application.ApplicationSpecInfoList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6bbfc6763fcb104e516dc41832b05746165d69d903ca5dde4d7e947fc0e068d6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ApplicationSpecInfoOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eaea8afb9c7221713150d4cce5c696da28fe2935cf6a6118a3c978e5a48bfc2a)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApplicationSpecInfoOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a456348a46ef6e10b28ff7eaa16915e334edb29c3a9fd5d2f24e3d07f428be8c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5dc286bb3fe3d8ef7006a628db3598a849b9542c181a468acd71f55e0a54f890)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1cf43d116cfb2f7a745e2a7af2320eaf78dccd07cfbae1bbedacb87efe1bfc81)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ApplicationSpecInfo]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ApplicationSpecInfo]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ApplicationSpecInfo]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f62d7618701c8d784b87bd0de1cb943df618ef71ecabada1f009e3db04637d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationSpecInfoOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.application.ApplicationSpecInfoOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__345990858536f554e55f53962d19480211e296fdb894e9741ae45bbf6ead2be8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ae1edb93656088fa65f258295c6baf3f0568dd0e1f8d31d1d2a4ef248330845)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c4443d740620fdd68d2b6898e42439b3d009a02fc9ded76e765a2d4a16b93a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ApplicationSpecInfo]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ApplicationSpecInfo]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ApplicationSpecInfo]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45c75aa7e5c4d70ad68af87e9b92646390c126f89c081fb6fe7409f9a8b363c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationSpecOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.application.ApplicationSpecOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__96c860e1b3d46f0bac46a0990ce67e68f786c770812b90a35bda5b12adf0c7dc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDestination")
    def put_destination(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        server: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the target cluster. Can be used instead of ``server``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#name Application#name}
        :param namespace: Target namespace for the application's resources. The namespace will only be set for namespace-scoped resources that have not set a value for .metadata.namespace. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#namespace Application#namespace}
        :param server: URL of the target cluster and must be set to the Kubernetes control plane API. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#server Application#server}
        '''
        value = ApplicationSpecDestination(
            name=name, namespace=namespace, server=server
        )

        return typing.cast(None, jsii.invoke(self, "putDestination", [value]))

    @jsii.member(jsii_name="putIgnoreDifference")
    def put_ignore_difference(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ApplicationSpecIgnoreDifference, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df2eeb53bfdec8548cfa827aafa5b62ee8334783663960a1c4fd402c5d8d50e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putIgnoreDifference", [value]))

    @jsii.member(jsii_name="putInfo")
    def put_info(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ApplicationSpecInfo, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5beb50587d462ca024aa2b08fbc32e917c8fff2e48388c18aaff98bc87a0598f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putInfo", [value]))

    @jsii.member(jsii_name="putSource")
    def put_source(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ApplicationSpecSource", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7cc9198e0e919b3cf37ecb9786a516e26dfc31091ecc1d9e318558726b458a6f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSource", [value]))

    @jsii.member(jsii_name="putSyncPolicy")
    def put_sync_policy(
        self,
        *,
        automated: typing.Optional[typing.Union["ApplicationSpecSyncPolicyAutomated", typing.Dict[builtins.str, typing.Any]]] = None,
        managed_namespace_metadata: typing.Optional[typing.Union["ApplicationSpecSyncPolicyManagedNamespaceMetadata", typing.Dict[builtins.str, typing.Any]]] = None,
        retry: typing.Optional[typing.Union["ApplicationSpecSyncPolicyRetry", typing.Dict[builtins.str, typing.Any]]] = None,
        sync_options: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param automated: automated block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#automated Application#automated}
        :param managed_namespace_metadata: managed_namespace_metadata block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#managed_namespace_metadata Application#managed_namespace_metadata}
        :param retry: retry block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#retry Application#retry}
        :param sync_options: List of sync options. More info: https://argo-cd.readthedocs.io/en/stable/user-guide/sync-options/. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#sync_options Application#sync_options}
        '''
        value = ApplicationSpecSyncPolicy(
            automated=automated,
            managed_namespace_metadata=managed_namespace_metadata,
            retry=retry,
            sync_options=sync_options,
        )

        return typing.cast(None, jsii.invoke(self, "putSyncPolicy", [value]))

    @jsii.member(jsii_name="resetIgnoreDifference")
    def reset_ignore_difference(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnoreDifference", []))

    @jsii.member(jsii_name="resetInfo")
    def reset_info(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInfo", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetRevisionHistoryLimit")
    def reset_revision_history_limit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRevisionHistoryLimit", []))

    @jsii.member(jsii_name="resetSyncPolicy")
    def reset_sync_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSyncPolicy", []))

    @builtins.property
    @jsii.member(jsii_name="destination")
    def destination(self) -> ApplicationSpecDestinationOutputReference:
        return typing.cast(ApplicationSpecDestinationOutputReference, jsii.get(self, "destination"))

    @builtins.property
    @jsii.member(jsii_name="ignoreDifference")
    def ignore_difference(self) -> ApplicationSpecIgnoreDifferenceList:
        return typing.cast(ApplicationSpecIgnoreDifferenceList, jsii.get(self, "ignoreDifference"))

    @builtins.property
    @jsii.member(jsii_name="info")
    def info(self) -> ApplicationSpecInfoList:
        return typing.cast(ApplicationSpecInfoList, jsii.get(self, "info"))

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> "ApplicationSpecSourceList":
        return typing.cast("ApplicationSpecSourceList", jsii.get(self, "source"))

    @builtins.property
    @jsii.member(jsii_name="syncPolicy")
    def sync_policy(self) -> "ApplicationSpecSyncPolicyOutputReference":
        return typing.cast("ApplicationSpecSyncPolicyOutputReference", jsii.get(self, "syncPolicy"))

    @builtins.property
    @jsii.member(jsii_name="destinationInput")
    def destination_input(self) -> typing.Optional[ApplicationSpecDestination]:
        return typing.cast(typing.Optional[ApplicationSpecDestination], jsii.get(self, "destinationInput"))

    @builtins.property
    @jsii.member(jsii_name="ignoreDifferenceInput")
    def ignore_difference_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ApplicationSpecIgnoreDifference]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ApplicationSpecIgnoreDifference]]], jsii.get(self, "ignoreDifferenceInput"))

    @builtins.property
    @jsii.member(jsii_name="infoInput")
    def info_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ApplicationSpecInfo]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ApplicationSpecInfo]]], jsii.get(self, "infoInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="revisionHistoryLimitInput")
    def revision_history_limit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "revisionHistoryLimitInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceInput")
    def source_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ApplicationSpecSource"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ApplicationSpecSource"]]], jsii.get(self, "sourceInput"))

    @builtins.property
    @jsii.member(jsii_name="syncPolicyInput")
    def sync_policy_input(self) -> typing.Optional["ApplicationSpecSyncPolicy"]:
        return typing.cast(typing.Optional["ApplicationSpecSyncPolicy"], jsii.get(self, "syncPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__883445e417d054d70523d710b48dbe2c631bda85f6596c1f12b78011c2911a4b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="revisionHistoryLimit")
    def revision_history_limit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "revisionHistoryLimit"))

    @revision_history_limit.setter
    def revision_history_limit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3c04f2d35b8e386bb09788ed7418a51c57948df1db57bd743be1873893d4913)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "revisionHistoryLimit", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApplicationSpec]:
        return typing.cast(typing.Optional[ApplicationSpec], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ApplicationSpec]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09a96425ae64f482351be4c73a27eef3d051f328c9d7a88f7916940bc69bfaca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="argocd.application.ApplicationSpecSource",
    jsii_struct_bases=[],
    name_mapping={
        "repo_url": "repoUrl",
        "chart": "chart",
        "directory": "directory",
        "helm": "helm",
        "kustomize": "kustomize",
        "path": "path",
        "plugin": "plugin",
        "ref": "ref",
        "target_revision": "targetRevision",
    },
)
class ApplicationSpecSource:
    def __init__(
        self,
        *,
        repo_url: builtins.str,
        chart: typing.Optional[builtins.str] = None,
        directory: typing.Optional[typing.Union["ApplicationSpecSourceDirectory", typing.Dict[builtins.str, typing.Any]]] = None,
        helm: typing.Optional[typing.Union["ApplicationSpecSourceHelm", typing.Dict[builtins.str, typing.Any]]] = None,
        kustomize: typing.Optional[typing.Union["ApplicationSpecSourceKustomize", typing.Dict[builtins.str, typing.Any]]] = None,
        path: typing.Optional[builtins.str] = None,
        plugin: typing.Optional[typing.Union["ApplicationSpecSourcePlugin", typing.Dict[builtins.str, typing.Any]]] = None,
        ref: typing.Optional[builtins.str] = None,
        target_revision: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param repo_url: URL to the repository (Git or Helm) that contains the application manifests. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#repo_url Application#repo_url}
        :param chart: Helm chart name. Must be specified for applications sourced from a Helm repo. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#chart Application#chart}
        :param directory: directory block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#directory Application#directory}
        :param helm: helm block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#helm Application#helm}
        :param kustomize: kustomize block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#kustomize Application#kustomize}
        :param path: Directory path within the repository. Only valid for applications sourced from Git. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#path Application#path}
        :param plugin: plugin block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#plugin Application#plugin}
        :param ref: Reference to another ``source`` within defined sources. See associated documentation on `Helm value files from external Git repository <https://argo-cd.readthedocs.io/en/stable/user-guide/multiple_sources/#helm-value-files-from-external-git-repository>`_ regarding combining ``ref`` with ``path`` and/or ``chart``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#ref Application#ref}
        :param target_revision: Revision of the source to sync the application to. In case of Git, this can be commit, tag, or branch. If omitted, will equal to HEAD. In case of Helm, this is a semver tag for the Chart's version. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#target_revision Application#target_revision}
        '''
        if isinstance(directory, dict):
            directory = ApplicationSpecSourceDirectory(**directory)
        if isinstance(helm, dict):
            helm = ApplicationSpecSourceHelm(**helm)
        if isinstance(kustomize, dict):
            kustomize = ApplicationSpecSourceKustomize(**kustomize)
        if isinstance(plugin, dict):
            plugin = ApplicationSpecSourcePlugin(**plugin)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df7987686619a417603fbb6387e0b68448dfe01fd1a6f1f12f9bac8e0bf5c760)
            check_type(argname="argument repo_url", value=repo_url, expected_type=type_hints["repo_url"])
            check_type(argname="argument chart", value=chart, expected_type=type_hints["chart"])
            check_type(argname="argument directory", value=directory, expected_type=type_hints["directory"])
            check_type(argname="argument helm", value=helm, expected_type=type_hints["helm"])
            check_type(argname="argument kustomize", value=kustomize, expected_type=type_hints["kustomize"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument plugin", value=plugin, expected_type=type_hints["plugin"])
            check_type(argname="argument ref", value=ref, expected_type=type_hints["ref"])
            check_type(argname="argument target_revision", value=target_revision, expected_type=type_hints["target_revision"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "repo_url": repo_url,
        }
        if chart is not None:
            self._values["chart"] = chart
        if directory is not None:
            self._values["directory"] = directory
        if helm is not None:
            self._values["helm"] = helm
        if kustomize is not None:
            self._values["kustomize"] = kustomize
        if path is not None:
            self._values["path"] = path
        if plugin is not None:
            self._values["plugin"] = plugin
        if ref is not None:
            self._values["ref"] = ref
        if target_revision is not None:
            self._values["target_revision"] = target_revision

    @builtins.property
    def repo_url(self) -> builtins.str:
        '''URL to the repository (Git or Helm) that contains the application manifests.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#repo_url Application#repo_url}
        '''
        result = self._values.get("repo_url")
        assert result is not None, "Required property 'repo_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def chart(self) -> typing.Optional[builtins.str]:
        '''Helm chart name. Must be specified for applications sourced from a Helm repo.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#chart Application#chart}
        '''
        result = self._values.get("chart")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def directory(self) -> typing.Optional["ApplicationSpecSourceDirectory"]:
        '''directory block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#directory Application#directory}
        '''
        result = self._values.get("directory")
        return typing.cast(typing.Optional["ApplicationSpecSourceDirectory"], result)

    @builtins.property
    def helm(self) -> typing.Optional["ApplicationSpecSourceHelm"]:
        '''helm block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#helm Application#helm}
        '''
        result = self._values.get("helm")
        return typing.cast(typing.Optional["ApplicationSpecSourceHelm"], result)

    @builtins.property
    def kustomize(self) -> typing.Optional["ApplicationSpecSourceKustomize"]:
        '''kustomize block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#kustomize Application#kustomize}
        '''
        result = self._values.get("kustomize")
        return typing.cast(typing.Optional["ApplicationSpecSourceKustomize"], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Directory path within the repository. Only valid for applications sourced from Git.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#path Application#path}
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def plugin(self) -> typing.Optional["ApplicationSpecSourcePlugin"]:
        '''plugin block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#plugin Application#plugin}
        '''
        result = self._values.get("plugin")
        return typing.cast(typing.Optional["ApplicationSpecSourcePlugin"], result)

    @builtins.property
    def ref(self) -> typing.Optional[builtins.str]:
        '''Reference to another ``source`` within defined sources.

        See associated documentation on `Helm value files from external Git repository <https://argo-cd.readthedocs.io/en/stable/user-guide/multiple_sources/#helm-value-files-from-external-git-repository>`_ regarding combining ``ref`` with ``path`` and/or ``chart``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#ref Application#ref}
        '''
        result = self._values.get("ref")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_revision(self) -> typing.Optional[builtins.str]:
        '''Revision of the source to sync the application to.

        In case of Git, this can be commit, tag, or branch. If omitted, will equal to HEAD. In case of Helm, this is a semver tag for the Chart's version.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#target_revision Application#target_revision}
        '''
        result = self._values.get("target_revision")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationSpecSource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="argocd.application.ApplicationSpecSourceDirectory",
    jsii_struct_bases=[],
    name_mapping={
        "exclude": "exclude",
        "include": "include",
        "jsonnet": "jsonnet",
        "recurse": "recurse",
    },
)
class ApplicationSpecSourceDirectory:
    def __init__(
        self,
        *,
        exclude: typing.Optional[builtins.str] = None,
        include: typing.Optional[builtins.str] = None,
        jsonnet: typing.Optional[typing.Union["ApplicationSpecSourceDirectoryJsonnet", typing.Dict[builtins.str, typing.Any]]] = None,
        recurse: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param exclude: Glob pattern to match paths against that should be explicitly excluded from being used during manifest generation. This takes precedence over the ``include`` field. To match multiple patterns, wrap the patterns in {} and separate them with commas. For example: '{config.yaml,env-use2/*}' Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#exclude Application#exclude}
        :param include: Glob pattern to match paths against that should be explicitly included during manifest generation. If this field is set, only matching manifests will be included. To match multiple patterns, wrap the patterns in {} and separate them with commas. For example: '{*.yml,*.yaml}' Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#include Application#include}
        :param jsonnet: jsonnet block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#jsonnet Application#jsonnet}
        :param recurse: Whether to scan a directory recursively for manifests. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#recurse Application#recurse}
        '''
        if isinstance(jsonnet, dict):
            jsonnet = ApplicationSpecSourceDirectoryJsonnet(**jsonnet)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2806c6d28c35b7da297dadbcd3b9a304c5413d05f1a906ade7b10745ab1f61e4)
            check_type(argname="argument exclude", value=exclude, expected_type=type_hints["exclude"])
            check_type(argname="argument include", value=include, expected_type=type_hints["include"])
            check_type(argname="argument jsonnet", value=jsonnet, expected_type=type_hints["jsonnet"])
            check_type(argname="argument recurse", value=recurse, expected_type=type_hints["recurse"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if exclude is not None:
            self._values["exclude"] = exclude
        if include is not None:
            self._values["include"] = include
        if jsonnet is not None:
            self._values["jsonnet"] = jsonnet
        if recurse is not None:
            self._values["recurse"] = recurse

    @builtins.property
    def exclude(self) -> typing.Optional[builtins.str]:
        '''Glob pattern to match paths against that should be explicitly excluded from being used during manifest generation.

        This takes precedence over the ``include`` field. To match multiple patterns, wrap the patterns in {} and separate them with commas. For example: '{config.yaml,env-use2/*}'

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#exclude Application#exclude}
        '''
        result = self._values.get("exclude")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def include(self) -> typing.Optional[builtins.str]:
        '''Glob pattern to match paths against that should be explicitly included during manifest generation.

        If this field is set, only matching manifests will be included. To match multiple patterns, wrap the patterns in {} and separate them with commas. For example: '{*.yml,*.yaml}'

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#include Application#include}
        '''
        result = self._values.get("include")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def jsonnet(self) -> typing.Optional["ApplicationSpecSourceDirectoryJsonnet"]:
        '''jsonnet block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#jsonnet Application#jsonnet}
        '''
        result = self._values.get("jsonnet")
        return typing.cast(typing.Optional["ApplicationSpecSourceDirectoryJsonnet"], result)

    @builtins.property
    def recurse(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to scan a directory recursively for manifests.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#recurse Application#recurse}
        '''
        result = self._values.get("recurse")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationSpecSourceDirectory(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="argocd.application.ApplicationSpecSourceDirectoryJsonnet",
    jsii_struct_bases=[],
    name_mapping={"ext_var": "extVar", "libs": "libs", "tla": "tla"},
)
class ApplicationSpecSourceDirectoryJsonnet:
    def __init__(
        self,
        *,
        ext_var: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ApplicationSpecSourceDirectoryJsonnetExtVar", typing.Dict[builtins.str, typing.Any]]]]] = None,
        libs: typing.Optional[typing.Sequence[builtins.str]] = None,
        tla: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ApplicationSpecSourceDirectoryJsonnetTla", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param ext_var: ext_var block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#ext_var Application#ext_var}
        :param libs: Additional library search dirs. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#libs Application#libs}
        :param tla: tla block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#tla Application#tla}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3bc5c6c29ec8f6c811b8a8d56094f1d67b33b36a8d4d9c917626282b0559b570)
            check_type(argname="argument ext_var", value=ext_var, expected_type=type_hints["ext_var"])
            check_type(argname="argument libs", value=libs, expected_type=type_hints["libs"])
            check_type(argname="argument tla", value=tla, expected_type=type_hints["tla"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if ext_var is not None:
            self._values["ext_var"] = ext_var
        if libs is not None:
            self._values["libs"] = libs
        if tla is not None:
            self._values["tla"] = tla

    @builtins.property
    def ext_var(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ApplicationSpecSourceDirectoryJsonnetExtVar"]]]:
        '''ext_var block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#ext_var Application#ext_var}
        '''
        result = self._values.get("ext_var")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ApplicationSpecSourceDirectoryJsonnetExtVar"]]], result)

    @builtins.property
    def libs(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Additional library search dirs.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#libs Application#libs}
        '''
        result = self._values.get("libs")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tla(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ApplicationSpecSourceDirectoryJsonnetTla"]]]:
        '''tla block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#tla Application#tla}
        '''
        result = self._values.get("tla")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ApplicationSpecSourceDirectoryJsonnetTla"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationSpecSourceDirectoryJsonnet(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="argocd.application.ApplicationSpecSourceDirectoryJsonnetExtVar",
    jsii_struct_bases=[],
    name_mapping={"code": "code", "name": "name", "value": "value"},
)
class ApplicationSpecSourceDirectoryJsonnetExtVar:
    def __init__(
        self,
        *,
        code: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param code: Determines whether the variable should be evaluated as jsonnet code or treated as string. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#code Application#code}
        :param name: Name of Jsonnet variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#name Application#name}
        :param value: Value of Jsonnet variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#value Application#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7cef95497ca2fbaeccf98be6eee7e9c6722109d0394d0e3a73d4a4dd7a8009d)
            check_type(argname="argument code", value=code, expected_type=type_hints["code"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if code is not None:
            self._values["code"] = code
        if name is not None:
            self._values["name"] = name
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def code(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Determines whether the variable should be evaluated as jsonnet code or treated as string.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#code Application#code}
        '''
        result = self._values.get("code")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of Jsonnet variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#name Application#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Value of Jsonnet variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#value Application#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationSpecSourceDirectoryJsonnetExtVar(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationSpecSourceDirectoryJsonnetExtVarList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.application.ApplicationSpecSourceDirectoryJsonnetExtVarList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e29dfe52f704a87055ff8a78f59919726100adafdd142431d8c957d111d508ee)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApplicationSpecSourceDirectoryJsonnetExtVarOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__389d19168187160e2bed3435933f1194323ab40248211f3de127c0ad9174f4c4)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApplicationSpecSourceDirectoryJsonnetExtVarOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03dac6a32750d927d97aec637197b47a9039926db08a05b0a2d4778a7aafca54)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f2c048d377bf8edc3ac409696dfb736f037f5fb31a83848ac3fa228b1dae1ded)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3b366a598e9345a5b72477808e65f28e1e1a89a7a9580ab868e6ed394086b279)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ApplicationSpecSourceDirectoryJsonnetExtVar]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ApplicationSpecSourceDirectoryJsonnetExtVar]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ApplicationSpecSourceDirectoryJsonnetExtVar]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4bc2b2c71b90ce3715a9f78e0664cfbc3318f29cc2ef546635b811c4c13fa65)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationSpecSourceDirectoryJsonnetExtVarOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.application.ApplicationSpecSourceDirectoryJsonnetExtVarOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__004a8e755a3b7dc56260cb50d75d97de6d76c46d373c564fec538d519576e8de)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCode")
    def reset_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCode", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="codeInput")
    def code_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "codeInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="code")
    def code(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "code"))

    @code.setter
    def code(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__816bbb64635d8a40f3e312149de45004789419334a9434904f78f0cb176e2007)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "code", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f478fffdd654272bb3ecf24306670779090c4833e1e25b89e8c7cda5f0076cc1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fa47ab859da88e84b1eb805e98f768914d1f11857bbf6bea5b76d9195ed1f1d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ApplicationSpecSourceDirectoryJsonnetExtVar]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ApplicationSpecSourceDirectoryJsonnetExtVar]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ApplicationSpecSourceDirectoryJsonnetExtVar]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f8824907fdef2e0c76018c6ffa3150d482f836290ca3fd0251fb6c029dc901e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationSpecSourceDirectoryJsonnetOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.application.ApplicationSpecSourceDirectoryJsonnetOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b271ce75960966f94e8f274146d1246228bea2d20e299451872c478cb8e1de8e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putExtVar")
    def put_ext_var(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ApplicationSpecSourceDirectoryJsonnetExtVar, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dfe2a695a8376492b74f9069965ac72b1635a22722b43278326a8a309df33ddf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putExtVar", [value]))

    @jsii.member(jsii_name="putTla")
    def put_tla(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ApplicationSpecSourceDirectoryJsonnetTla", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27243125bafd09a2e1733798747ebf1c395524f2bf8817207517579f5addb0ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTla", [value]))

    @jsii.member(jsii_name="resetExtVar")
    def reset_ext_var(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExtVar", []))

    @jsii.member(jsii_name="resetLibs")
    def reset_libs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLibs", []))

    @jsii.member(jsii_name="resetTla")
    def reset_tla(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTla", []))

    @builtins.property
    @jsii.member(jsii_name="extVar")
    def ext_var(self) -> ApplicationSpecSourceDirectoryJsonnetExtVarList:
        return typing.cast(ApplicationSpecSourceDirectoryJsonnetExtVarList, jsii.get(self, "extVar"))

    @builtins.property
    @jsii.member(jsii_name="tla")
    def tla(self) -> "ApplicationSpecSourceDirectoryJsonnetTlaList":
        return typing.cast("ApplicationSpecSourceDirectoryJsonnetTlaList", jsii.get(self, "tla"))

    @builtins.property
    @jsii.member(jsii_name="extVarInput")
    def ext_var_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ApplicationSpecSourceDirectoryJsonnetExtVar]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ApplicationSpecSourceDirectoryJsonnetExtVar]]], jsii.get(self, "extVarInput"))

    @builtins.property
    @jsii.member(jsii_name="libsInput")
    def libs_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "libsInput"))

    @builtins.property
    @jsii.member(jsii_name="tlaInput")
    def tla_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ApplicationSpecSourceDirectoryJsonnetTla"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ApplicationSpecSourceDirectoryJsonnetTla"]]], jsii.get(self, "tlaInput"))

    @builtins.property
    @jsii.member(jsii_name="libs")
    def libs(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "libs"))

    @libs.setter
    def libs(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91f1ea104ac67160f39e0f1a3d7f5b8ab6b6fb4b11d8d23f6617cea00f73f79a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "libs", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApplicationSpecSourceDirectoryJsonnet]:
        return typing.cast(typing.Optional[ApplicationSpecSourceDirectoryJsonnet], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApplicationSpecSourceDirectoryJsonnet],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cba06b93e0e3627cfaf31b87d2244bca1ba086e7600dc11af32fcb2ef2ac4a00)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="argocd.application.ApplicationSpecSourceDirectoryJsonnetTla",
    jsii_struct_bases=[],
    name_mapping={"code": "code", "name": "name", "value": "value"},
)
class ApplicationSpecSourceDirectoryJsonnetTla:
    def __init__(
        self,
        *,
        code: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param code: Determines whether the variable should be evaluated as jsonnet code or treated as string. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#code Application#code}
        :param name: Name of Jsonnet variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#name Application#name}
        :param value: Value of Jsonnet variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#value Application#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e955b3dcacf85c12f4753f824778a0da6ba6d579b008e754084d569864740cc)
            check_type(argname="argument code", value=code, expected_type=type_hints["code"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if code is not None:
            self._values["code"] = code
        if name is not None:
            self._values["name"] = name
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def code(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Determines whether the variable should be evaluated as jsonnet code or treated as string.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#code Application#code}
        '''
        result = self._values.get("code")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of Jsonnet variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#name Application#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Value of Jsonnet variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#value Application#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationSpecSourceDirectoryJsonnetTla(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationSpecSourceDirectoryJsonnetTlaList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.application.ApplicationSpecSourceDirectoryJsonnetTlaList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8052f86a5390d9a855034b9c5b8065542d59a637d697451625dce0be1547d5c5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApplicationSpecSourceDirectoryJsonnetTlaOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0971c37eaf7da6c6241383143cfd79e4f9e422a65b6dd0365c1016f43eb1e44b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApplicationSpecSourceDirectoryJsonnetTlaOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54ae7f7d492911c8971819208c9112914bf73a323b603ae13c93838628eb2284)
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
            type_hints = typing.get_type_hints(_typecheckingstub__bf5f2d1775a8ebf829b2c72b1c90cd3dd0bb9bdd4bbd2ae05d6a36029a94cb02)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3606f2eb178482efd35b9bd82dd2abca08bbce5328ecb764c03c560699f1c04f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ApplicationSpecSourceDirectoryJsonnetTla]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ApplicationSpecSourceDirectoryJsonnetTla]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ApplicationSpecSourceDirectoryJsonnetTla]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__beb37088bb66e76d0ca4aba98f2f52b2c157e057fc08e2147881c45ce345f01a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationSpecSourceDirectoryJsonnetTlaOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.application.ApplicationSpecSourceDirectoryJsonnetTlaOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cef12e11ab5f0258c3756144bd805b87b5da292563c9bca539111b712416f99a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCode")
    def reset_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCode", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="codeInput")
    def code_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "codeInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="code")
    def code(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "code"))

    @code.setter
    def code(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ded247989a2077df6e2b06f5eb1cf0fe60b017361be059dd67bc3f8e7362ff59)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "code", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94fe73bc5550498045a6714f6e26373adcf6f40abada2532d15794534993850a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4e7a3ed298ed0dfabb219035cb6d9dd99681d168b7c3045309c9dc1d04559e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ApplicationSpecSourceDirectoryJsonnetTla]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ApplicationSpecSourceDirectoryJsonnetTla]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ApplicationSpecSourceDirectoryJsonnetTla]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5b909f1cc487b3c4fb0b8b99a96d6f1e031c197d0aa8923484729e65ff20646)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationSpecSourceDirectoryOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.application.ApplicationSpecSourceDirectoryOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__66e38b779a0450fed90ecfcf80d5a13bcf178ff4cd490308fc266af07c0adb81)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putJsonnet")
    def put_jsonnet(
        self,
        *,
        ext_var: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ApplicationSpecSourceDirectoryJsonnetExtVar, typing.Dict[builtins.str, typing.Any]]]]] = None,
        libs: typing.Optional[typing.Sequence[builtins.str]] = None,
        tla: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ApplicationSpecSourceDirectoryJsonnetTla, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param ext_var: ext_var block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#ext_var Application#ext_var}
        :param libs: Additional library search dirs. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#libs Application#libs}
        :param tla: tla block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#tla Application#tla}
        '''
        value = ApplicationSpecSourceDirectoryJsonnet(
            ext_var=ext_var, libs=libs, tla=tla
        )

        return typing.cast(None, jsii.invoke(self, "putJsonnet", [value]))

    @jsii.member(jsii_name="resetExclude")
    def reset_exclude(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExclude", []))

    @jsii.member(jsii_name="resetInclude")
    def reset_include(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInclude", []))

    @jsii.member(jsii_name="resetJsonnet")
    def reset_jsonnet(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJsonnet", []))

    @jsii.member(jsii_name="resetRecurse")
    def reset_recurse(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRecurse", []))

    @builtins.property
    @jsii.member(jsii_name="jsonnet")
    def jsonnet(self) -> ApplicationSpecSourceDirectoryJsonnetOutputReference:
        return typing.cast(ApplicationSpecSourceDirectoryJsonnetOutputReference, jsii.get(self, "jsonnet"))

    @builtins.property
    @jsii.member(jsii_name="excludeInput")
    def exclude_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "excludeInput"))

    @builtins.property
    @jsii.member(jsii_name="includeInput")
    def include_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "includeInput"))

    @builtins.property
    @jsii.member(jsii_name="jsonnetInput")
    def jsonnet_input(self) -> typing.Optional[ApplicationSpecSourceDirectoryJsonnet]:
        return typing.cast(typing.Optional[ApplicationSpecSourceDirectoryJsonnet], jsii.get(self, "jsonnetInput"))

    @builtins.property
    @jsii.member(jsii_name="recurseInput")
    def recurse_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "recurseInput"))

    @builtins.property
    @jsii.member(jsii_name="exclude")
    def exclude(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "exclude"))

    @exclude.setter
    def exclude(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4cd2d1603d5fdddbde14676cf3a5c7a3510e3c416ec5f3a6ea9820481db6d292)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exclude", value)

    @builtins.property
    @jsii.member(jsii_name="include")
    def include(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "include"))

    @include.setter
    def include(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7ba38194dcdae9e45739f552ecd44b4a97d4dd79bbb6b0fab2ad6b6c0a9378c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "include", value)

    @builtins.property
    @jsii.member(jsii_name="recurse")
    def recurse(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "recurse"))

    @recurse.setter
    def recurse(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a24af30b70184790de594d12fae5ed1c119a179e8046f36fa4ad689b2e2196b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recurse", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApplicationSpecSourceDirectory]:
        return typing.cast(typing.Optional[ApplicationSpecSourceDirectory], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApplicationSpecSourceDirectory],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__530bdb7a3fb963fee9dc11339cf506c695df3be2a37c73beef94bb4030aa89f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="argocd.application.ApplicationSpecSourceHelm",
    jsii_struct_bases=[],
    name_mapping={
        "file_parameter": "fileParameter",
        "ignore_missing_value_files": "ignoreMissingValueFiles",
        "parameter": "parameter",
        "pass_credentials": "passCredentials",
        "release_name": "releaseName",
        "skip_crds": "skipCrds",
        "value_files": "valueFiles",
        "values": "values",
    },
)
class ApplicationSpecSourceHelm:
    def __init__(
        self,
        *,
        file_parameter: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ApplicationSpecSourceHelmFileParameter", typing.Dict[builtins.str, typing.Any]]]]] = None,
        ignore_missing_value_files: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        parameter: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ApplicationSpecSourceHelmParameter", typing.Dict[builtins.str, typing.Any]]]]] = None,
        pass_credentials: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        release_name: typing.Optional[builtins.str] = None,
        skip_crds: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        value_files: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param file_parameter: file_parameter block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#file_parameter Application#file_parameter}
        :param ignore_missing_value_files: Prevents 'helm template' from failing when ``value_files`` do not exist locally by not appending them to 'helm template --values'. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#ignore_missing_value_files Application#ignore_missing_value_files}
        :param parameter: parameter block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#parameter Application#parameter}
        :param pass_credentials: If true then adds '--pass-credentials' to Helm commands to pass credentials to all domains. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#pass_credentials Application#pass_credentials}
        :param release_name: Helm release name. If omitted it will use the application name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#release_name Application#release_name}
        :param skip_crds: Whether to skip custom resource definition installation step (Helm's `--skip-crds <https://helm.sh/docs/chart_best_practices/custom_resource_definitions/>`_). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#skip_crds Application#skip_crds}
        :param value_files: List of Helm value files to use when generating a template. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#value_files Application#value_files}
        :param values: Helm values to be passed to 'helm template', typically defined as a block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#values Application#values}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e0adb29abb6424b8da42fc68a29e142433ad33701bea68a6a62129506a57f40)
            check_type(argname="argument file_parameter", value=file_parameter, expected_type=type_hints["file_parameter"])
            check_type(argname="argument ignore_missing_value_files", value=ignore_missing_value_files, expected_type=type_hints["ignore_missing_value_files"])
            check_type(argname="argument parameter", value=parameter, expected_type=type_hints["parameter"])
            check_type(argname="argument pass_credentials", value=pass_credentials, expected_type=type_hints["pass_credentials"])
            check_type(argname="argument release_name", value=release_name, expected_type=type_hints["release_name"])
            check_type(argname="argument skip_crds", value=skip_crds, expected_type=type_hints["skip_crds"])
            check_type(argname="argument value_files", value=value_files, expected_type=type_hints["value_files"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if file_parameter is not None:
            self._values["file_parameter"] = file_parameter
        if ignore_missing_value_files is not None:
            self._values["ignore_missing_value_files"] = ignore_missing_value_files
        if parameter is not None:
            self._values["parameter"] = parameter
        if pass_credentials is not None:
            self._values["pass_credentials"] = pass_credentials
        if release_name is not None:
            self._values["release_name"] = release_name
        if skip_crds is not None:
            self._values["skip_crds"] = skip_crds
        if value_files is not None:
            self._values["value_files"] = value_files
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def file_parameter(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ApplicationSpecSourceHelmFileParameter"]]]:
        '''file_parameter block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#file_parameter Application#file_parameter}
        '''
        result = self._values.get("file_parameter")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ApplicationSpecSourceHelmFileParameter"]]], result)

    @builtins.property
    def ignore_missing_value_files(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Prevents 'helm template' from failing when ``value_files`` do not exist locally by not appending them to 'helm template --values'.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#ignore_missing_value_files Application#ignore_missing_value_files}
        '''
        result = self._values.get("ignore_missing_value_files")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def parameter(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ApplicationSpecSourceHelmParameter"]]]:
        '''parameter block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#parameter Application#parameter}
        '''
        result = self._values.get("parameter")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ApplicationSpecSourceHelmParameter"]]], result)

    @builtins.property
    def pass_credentials(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''If true then adds '--pass-credentials' to Helm commands to pass credentials to all domains.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#pass_credentials Application#pass_credentials}
        '''
        result = self._values.get("pass_credentials")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def release_name(self) -> typing.Optional[builtins.str]:
        '''Helm release name. If omitted it will use the application name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#release_name Application#release_name}
        '''
        result = self._values.get("release_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def skip_crds(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to skip custom resource definition installation step (Helm's `--skip-crds <https://helm.sh/docs/chart_best_practices/custom_resource_definitions/>`_).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#skip_crds Application#skip_crds}
        '''
        result = self._values.get("skip_crds")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def value_files(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of Helm value files to use when generating a template.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#value_files Application#value_files}
        '''
        result = self._values.get("value_files")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def values(self) -> typing.Optional[builtins.str]:
        '''Helm values to be passed to 'helm template', typically defined as a block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#values Application#values}
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationSpecSourceHelm(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="argocd.application.ApplicationSpecSourceHelmFileParameter",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "path": "path"},
)
class ApplicationSpecSourceHelmFileParameter:
    def __init__(self, *, name: builtins.str, path: builtins.str) -> None:
        '''
        :param name: Name of the Helm parameter. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#name Application#name}
        :param path: Path to the file containing the values for the Helm parameter. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#path Application#path}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe186f9cb859bccbd35fce614f2ccd9388b4c03b44058feacf89765955d08d34)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "path": path,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the Helm parameter.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#name Application#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> builtins.str:
        '''Path to the file containing the values for the Helm parameter.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#path Application#path}
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationSpecSourceHelmFileParameter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationSpecSourceHelmFileParameterList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.application.ApplicationSpecSourceHelmFileParameterList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5a458289a0039546cb1b15def1e413dbb06058be5a5063b8ff37d3a9218eb810)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApplicationSpecSourceHelmFileParameterOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4614ce1d1928057042aad2177ac49cdd08edea78ce87b03273e03900deaaa8e)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApplicationSpecSourceHelmFileParameterOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df1281ceb8360134db15e380deb345b9921fbf87746d936ecff6de17ed4c9ac1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5bbdd00e021a969d6b323b11e7a8bba0f13e39b124bbb51afaea2fa3163feef1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__63ad157b61bc4e7ab87bb0791e73f5bfbca6e714506ebb051dbefd49500f7070)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ApplicationSpecSourceHelmFileParameter]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ApplicationSpecSourceHelmFileParameter]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ApplicationSpecSourceHelmFileParameter]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47767669a634f3f6754df00fff9525858279e67699ecc23df747f684741426a3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationSpecSourceHelmFileParameterOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.application.ApplicationSpecSourceHelmFileParameterOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__92069268ce1f97fb9483c70ae5887bd9d969064bda847ecffbf5c6195c9e7e56)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__862beabf3f73e8f50d0d273f527c6e48764374ba40125de5652b06b4bcbbebcf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__100da5afa0f9f2f33e74801d664441d2b23c7ab321f360e51d814719e6513a11)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ApplicationSpecSourceHelmFileParameter]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ApplicationSpecSourceHelmFileParameter]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ApplicationSpecSourceHelmFileParameter]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f17df0071d9c544bf5f8caee7582dcbb006f747aabd3eb8e803763e43830bbf4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationSpecSourceHelmOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.application.ApplicationSpecSourceHelmOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0e648453ce42f39fc05a5c3153ac1bfb9f7f5fc2d28911a9dc1c929e72d4e5dd)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putFileParameter")
    def put_file_parameter(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ApplicationSpecSourceHelmFileParameter, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fdbd7963c14502a1822d326704d14215399088478cd67a59cdbd9677f2061527)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putFileParameter", [value]))

    @jsii.member(jsii_name="putParameter")
    def put_parameter(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ApplicationSpecSourceHelmParameter", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94eac0454670314dd2eb33f6583a655655c47e9236a4fbb14306643084ff216e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putParameter", [value]))

    @jsii.member(jsii_name="resetFileParameter")
    def reset_file_parameter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFileParameter", []))

    @jsii.member(jsii_name="resetIgnoreMissingValueFiles")
    def reset_ignore_missing_value_files(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnoreMissingValueFiles", []))

    @jsii.member(jsii_name="resetParameter")
    def reset_parameter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameter", []))

    @jsii.member(jsii_name="resetPassCredentials")
    def reset_pass_credentials(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassCredentials", []))

    @jsii.member(jsii_name="resetReleaseName")
    def reset_release_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReleaseName", []))

    @jsii.member(jsii_name="resetSkipCrds")
    def reset_skip_crds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSkipCrds", []))

    @jsii.member(jsii_name="resetValueFiles")
    def reset_value_files(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValueFiles", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="fileParameter")
    def file_parameter(self) -> ApplicationSpecSourceHelmFileParameterList:
        return typing.cast(ApplicationSpecSourceHelmFileParameterList, jsii.get(self, "fileParameter"))

    @builtins.property
    @jsii.member(jsii_name="parameter")
    def parameter(self) -> "ApplicationSpecSourceHelmParameterList":
        return typing.cast("ApplicationSpecSourceHelmParameterList", jsii.get(self, "parameter"))

    @builtins.property
    @jsii.member(jsii_name="fileParameterInput")
    def file_parameter_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ApplicationSpecSourceHelmFileParameter]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ApplicationSpecSourceHelmFileParameter]]], jsii.get(self, "fileParameterInput"))

    @builtins.property
    @jsii.member(jsii_name="ignoreMissingValueFilesInput")
    def ignore_missing_value_files_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "ignoreMissingValueFilesInput"))

    @builtins.property
    @jsii.member(jsii_name="parameterInput")
    def parameter_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ApplicationSpecSourceHelmParameter"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ApplicationSpecSourceHelmParameter"]]], jsii.get(self, "parameterInput"))

    @builtins.property
    @jsii.member(jsii_name="passCredentialsInput")
    def pass_credentials_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "passCredentialsInput"))

    @builtins.property
    @jsii.member(jsii_name="releaseNameInput")
    def release_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "releaseNameInput"))

    @builtins.property
    @jsii.member(jsii_name="skipCrdsInput")
    def skip_crds_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "skipCrdsInput"))

    @builtins.property
    @jsii.member(jsii_name="valueFilesInput")
    def value_files_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valueFilesInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="ignoreMissingValueFiles")
    def ignore_missing_value_files(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "ignoreMissingValueFiles"))

    @ignore_missing_value_files.setter
    def ignore_missing_value_files(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7df200f33b8468bccc802ee59787a3f78cfc2a002daf797f765b8079e053293)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreMissingValueFiles", value)

    @builtins.property
    @jsii.member(jsii_name="passCredentials")
    def pass_credentials(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "passCredentials"))

    @pass_credentials.setter
    def pass_credentials(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f69e8fb862286d7d161387959586092ccbd708a6a2281eba1f1cb75b1501704d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "passCredentials", value)

    @builtins.property
    @jsii.member(jsii_name="releaseName")
    def release_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "releaseName"))

    @release_name.setter
    def release_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fea4069d1cad4f6d0d6f4608e1c44983594c182523caa90547b5a4666638a656)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "releaseName", value)

    @builtins.property
    @jsii.member(jsii_name="skipCrds")
    def skip_crds(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "skipCrds"))

    @skip_crds.setter
    def skip_crds(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1e65febdb9f855f098567fedd04e4ba21a7af1b0b441cde1c9c786a0959c12f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skipCrds", value)

    @builtins.property
    @jsii.member(jsii_name="valueFiles")
    def value_files(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "valueFiles"))

    @value_files.setter
    def value_files(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c3b87f0669ef1241a1b5768402946ca07c276a74abae5cbb904ad6950d0c8fc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "valueFiles", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "values"))

    @values.setter
    def values(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b5a55ee578c52159dcbea39e5fff73f10944fe7aff547841e1f1176568b6f93c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApplicationSpecSourceHelm]:
        return typing.cast(typing.Optional[ApplicationSpecSourceHelm], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ApplicationSpecSourceHelm]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31e11abacb1b99eaf75fe179fe4b76a9705c3dbdacfa208ecf225b745cf77bb6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="argocd.application.ApplicationSpecSourceHelmParameter",
    jsii_struct_bases=[],
    name_mapping={"force_string": "forceString", "name": "name", "value": "value"},
)
class ApplicationSpecSourceHelmParameter:
    def __init__(
        self,
        *,
        force_string: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param force_string: Determines whether to tell Helm to interpret booleans and numbers as strings. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#force_string Application#force_string}
        :param name: Name of the Helm parameter. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#name Application#name}
        :param value: Value of the Helm parameter. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#value Application#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9cb567346cb6a29e10ecc65deb88a4d4ea35ed1560eeaf02da6688940335eb1)
            check_type(argname="argument force_string", value=force_string, expected_type=type_hints["force_string"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if force_string is not None:
            self._values["force_string"] = force_string
        if name is not None:
            self._values["name"] = name
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def force_string(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Determines whether to tell Helm to interpret booleans and numbers as strings.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#force_string Application#force_string}
        '''
        result = self._values.get("force_string")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the Helm parameter.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#name Application#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Value of the Helm parameter.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#value Application#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationSpecSourceHelmParameter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationSpecSourceHelmParameterList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.application.ApplicationSpecSourceHelmParameterList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6cd139b8f3e35799f995521df86ffd09c85f85408f872ac84eb09b05884562cc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApplicationSpecSourceHelmParameterOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84b80ed04ee511a21e45318908ae96398438264aa02545d292378fcbcbefde73)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApplicationSpecSourceHelmParameterOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b6f2eef2ad51c1e9f3915f8b5eaef5b2fba53bec3fb973ca397d69ee362826c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e2dc4a1e36deb47910bd3627899d6405834ae56f18dc78f6864ba73d228da06a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__bc825ec619cc4a38de1fdae6257e91b79f89376df277b85b4d683735c64ab7b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ApplicationSpecSourceHelmParameter]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ApplicationSpecSourceHelmParameter]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ApplicationSpecSourceHelmParameter]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2946f3ab23da1729269b6cee9072b755538391fdcd4b6e0677352f2a8f9d661a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationSpecSourceHelmParameterOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.application.ApplicationSpecSourceHelmParameterOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cbbdaf75a25cb1e1c4d46d5d0400af917a60642f740de90ad41ca72df61337b4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetForceString")
    def reset_force_string(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForceString", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="forceStringInput")
    def force_string_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "forceStringInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="forceString")
    def force_string(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "forceString"))

    @force_string.setter
    def force_string(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__710d00650a3e9d285e5e4796764945cfe0f9a881f460589b3b4607b3d627e710)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forceString", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e4fe7288c50d9dcd975e2cc832ad814bef5b417b9f338774f5ac8509df5ade8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d58b95d1309b97c04deb36da24e337eed1507c7a91162fe1c6f5b7b992ad7fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ApplicationSpecSourceHelmParameter]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ApplicationSpecSourceHelmParameter]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ApplicationSpecSourceHelmParameter]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f4281eb136d08ee1b84b2ef6e69c097c1c024e01a2256bca643ce6db1f45287)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="argocd.application.ApplicationSpecSourceKustomize",
    jsii_struct_bases=[],
    name_mapping={
        "common_annotations": "commonAnnotations",
        "common_labels": "commonLabels",
        "images": "images",
        "name_prefix": "namePrefix",
        "name_suffix": "nameSuffix",
        "version": "version",
    },
)
class ApplicationSpecSourceKustomize:
    def __init__(
        self,
        *,
        common_annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        common_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        images: typing.Optional[typing.Sequence[builtins.str]] = None,
        name_prefix: typing.Optional[builtins.str] = None,
        name_suffix: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param common_annotations: List of additional annotations to add to rendered manifests. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#common_annotations Application#common_annotations}
        :param common_labels: List of additional labels to add to rendered manifests. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#common_labels Application#common_labels}
        :param images: List of Kustomize image override specifications. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#images Application#images}
        :param name_prefix: Prefix appended to resources for Kustomize apps. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#name_prefix Application#name_prefix}
        :param name_suffix: Suffix appended to resources for Kustomize apps. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#name_suffix Application#name_suffix}
        :param version: Version of Kustomize to use for rendering manifests. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#version Application#version}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f62d81df08298daf480e1cd5c6e1ba1efc883eac8f488cae2a6073322622b4e)
            check_type(argname="argument common_annotations", value=common_annotations, expected_type=type_hints["common_annotations"])
            check_type(argname="argument common_labels", value=common_labels, expected_type=type_hints["common_labels"])
            check_type(argname="argument images", value=images, expected_type=type_hints["images"])
            check_type(argname="argument name_prefix", value=name_prefix, expected_type=type_hints["name_prefix"])
            check_type(argname="argument name_suffix", value=name_suffix, expected_type=type_hints["name_suffix"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if common_annotations is not None:
            self._values["common_annotations"] = common_annotations
        if common_labels is not None:
            self._values["common_labels"] = common_labels
        if images is not None:
            self._values["images"] = images
        if name_prefix is not None:
            self._values["name_prefix"] = name_prefix
        if name_suffix is not None:
            self._values["name_suffix"] = name_suffix
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def common_annotations(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''List of additional annotations to add to rendered manifests.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#common_annotations Application#common_annotations}
        '''
        result = self._values.get("common_annotations")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def common_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''List of additional labels to add to rendered manifests.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#common_labels Application#common_labels}
        '''
        result = self._values.get("common_labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def images(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of Kustomize image override specifications.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#images Application#images}
        '''
        result = self._values.get("images")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def name_prefix(self) -> typing.Optional[builtins.str]:
        '''Prefix appended to resources for Kustomize apps.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#name_prefix Application#name_prefix}
        '''
        result = self._values.get("name_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name_suffix(self) -> typing.Optional[builtins.str]:
        '''Suffix appended to resources for Kustomize apps.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#name_suffix Application#name_suffix}
        '''
        result = self._values.get("name_suffix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''Version of Kustomize to use for rendering manifests.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#version Application#version}
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationSpecSourceKustomize(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationSpecSourceKustomizeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.application.ApplicationSpecSourceKustomizeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8f62717bcac2aa72bb2509a0337f4ba31e2d2fb16c06ae9ca9d376ecc0cc84f5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCommonAnnotations")
    def reset_common_annotations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCommonAnnotations", []))

    @jsii.member(jsii_name="resetCommonLabels")
    def reset_common_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCommonLabels", []))

    @jsii.member(jsii_name="resetImages")
    def reset_images(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImages", []))

    @jsii.member(jsii_name="resetNamePrefix")
    def reset_name_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamePrefix", []))

    @jsii.member(jsii_name="resetNameSuffix")
    def reset_name_suffix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNameSuffix", []))

    @jsii.member(jsii_name="resetVersion")
    def reset_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersion", []))

    @builtins.property
    @jsii.member(jsii_name="commonAnnotationsInput")
    def common_annotations_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "commonAnnotationsInput"))

    @builtins.property
    @jsii.member(jsii_name="commonLabelsInput")
    def common_labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "commonLabelsInput"))

    @builtins.property
    @jsii.member(jsii_name="imagesInput")
    def images_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "imagesInput"))

    @builtins.property
    @jsii.member(jsii_name="namePrefixInput")
    def name_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namePrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="nameSuffixInput")
    def name_suffix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameSuffixInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="commonAnnotations")
    def common_annotations(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "commonAnnotations"))

    @common_annotations.setter
    def common_annotations(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40b79a627f2c374a3178c622aca7273a20f758dfc62f576447f8d302ecdc84a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "commonAnnotations", value)

    @builtins.property
    @jsii.member(jsii_name="commonLabels")
    def common_labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "commonLabels"))

    @common_labels.setter
    def common_labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bafba1b8348086d2f9c5206afdf21769cb59475f7c9fd76c6b9757d9093a7dbc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "commonLabels", value)

    @builtins.property
    @jsii.member(jsii_name="images")
    def images(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "images"))

    @images.setter
    def images(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16a6ea857e1512f8c0fa4962348ff8b7e4f0b90e1a1ad23af551bf40ca637528)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "images", value)

    @builtins.property
    @jsii.member(jsii_name="namePrefix")
    def name_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namePrefix"))

    @name_prefix.setter
    def name_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac2ffc3de435edb636067fea701a51a55ebd083cf4538cabb7aac7658b76654a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namePrefix", value)

    @builtins.property
    @jsii.member(jsii_name="nameSuffix")
    def name_suffix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nameSuffix"))

    @name_suffix.setter
    def name_suffix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51d1f758e8d64b7431f41a3d6958e659ba4c44a636582f9e47b4b6a48f731bc4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nameSuffix", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4f37266837882808180c6242ad0fa32fba29ccfd8a59623492df84e98eec999)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApplicationSpecSourceKustomize]:
        return typing.cast(typing.Optional[ApplicationSpecSourceKustomize], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApplicationSpecSourceKustomize],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15bf25b40ac59cff3ef2b2faba4982965eb1a139c0d226e499aae550d64c4721)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationSpecSourceList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.application.ApplicationSpecSourceList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__77cc2d932677ff5fd585f48970947974f69332c9a2acbbddde7675ee74701cea)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ApplicationSpecSourceOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__765c38c3205c56cad93e87d8519eb32216d2b61db63c058f0d29bb037893859f)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApplicationSpecSourceOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13204f5dbb92ce85fc93b56b22e0e508914df551fd01ad869171fdfbe98a1c29)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b344259dc66a623edf630be5fbe2901a97bad8688d2fbc11ce7da70c685eca20)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9ecf11cee045f5110e7137c1a8703989387c04c4465b9269a437e17477e9929b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ApplicationSpecSource]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ApplicationSpecSource]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ApplicationSpecSource]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b3e92dea0172401f906483a1f11aae3764e677c6db1ef2c18a51f3b58a1c7a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationSpecSourceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.application.ApplicationSpecSourceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b0c5744a9ca8d956c5ec9416a70ace50a5648c2a38e8ec0c0bea4a39a0b9288c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putDirectory")
    def put_directory(
        self,
        *,
        exclude: typing.Optional[builtins.str] = None,
        include: typing.Optional[builtins.str] = None,
        jsonnet: typing.Optional[typing.Union[ApplicationSpecSourceDirectoryJsonnet, typing.Dict[builtins.str, typing.Any]]] = None,
        recurse: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param exclude: Glob pattern to match paths against that should be explicitly excluded from being used during manifest generation. This takes precedence over the ``include`` field. To match multiple patterns, wrap the patterns in {} and separate them with commas. For example: '{config.yaml,env-use2/*}' Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#exclude Application#exclude}
        :param include: Glob pattern to match paths against that should be explicitly included during manifest generation. If this field is set, only matching manifests will be included. To match multiple patterns, wrap the patterns in {} and separate them with commas. For example: '{*.yml,*.yaml}' Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#include Application#include}
        :param jsonnet: jsonnet block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#jsonnet Application#jsonnet}
        :param recurse: Whether to scan a directory recursively for manifests. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#recurse Application#recurse}
        '''
        value = ApplicationSpecSourceDirectory(
            exclude=exclude, include=include, jsonnet=jsonnet, recurse=recurse
        )

        return typing.cast(None, jsii.invoke(self, "putDirectory", [value]))

    @jsii.member(jsii_name="putHelm")
    def put_helm(
        self,
        *,
        file_parameter: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ApplicationSpecSourceHelmFileParameter, typing.Dict[builtins.str, typing.Any]]]]] = None,
        ignore_missing_value_files: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        parameter: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ApplicationSpecSourceHelmParameter, typing.Dict[builtins.str, typing.Any]]]]] = None,
        pass_credentials: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        release_name: typing.Optional[builtins.str] = None,
        skip_crds: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        value_files: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param file_parameter: file_parameter block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#file_parameter Application#file_parameter}
        :param ignore_missing_value_files: Prevents 'helm template' from failing when ``value_files`` do not exist locally by not appending them to 'helm template --values'. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#ignore_missing_value_files Application#ignore_missing_value_files}
        :param parameter: parameter block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#parameter Application#parameter}
        :param pass_credentials: If true then adds '--pass-credentials' to Helm commands to pass credentials to all domains. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#pass_credentials Application#pass_credentials}
        :param release_name: Helm release name. If omitted it will use the application name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#release_name Application#release_name}
        :param skip_crds: Whether to skip custom resource definition installation step (Helm's `--skip-crds <https://helm.sh/docs/chart_best_practices/custom_resource_definitions/>`_). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#skip_crds Application#skip_crds}
        :param value_files: List of Helm value files to use when generating a template. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#value_files Application#value_files}
        :param values: Helm values to be passed to 'helm template', typically defined as a block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#values Application#values}
        '''
        value = ApplicationSpecSourceHelm(
            file_parameter=file_parameter,
            ignore_missing_value_files=ignore_missing_value_files,
            parameter=parameter,
            pass_credentials=pass_credentials,
            release_name=release_name,
            skip_crds=skip_crds,
            value_files=value_files,
            values=values,
        )

        return typing.cast(None, jsii.invoke(self, "putHelm", [value]))

    @jsii.member(jsii_name="putKustomize")
    def put_kustomize(
        self,
        *,
        common_annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        common_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        images: typing.Optional[typing.Sequence[builtins.str]] = None,
        name_prefix: typing.Optional[builtins.str] = None,
        name_suffix: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param common_annotations: List of additional annotations to add to rendered manifests. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#common_annotations Application#common_annotations}
        :param common_labels: List of additional labels to add to rendered manifests. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#common_labels Application#common_labels}
        :param images: List of Kustomize image override specifications. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#images Application#images}
        :param name_prefix: Prefix appended to resources for Kustomize apps. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#name_prefix Application#name_prefix}
        :param name_suffix: Suffix appended to resources for Kustomize apps. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#name_suffix Application#name_suffix}
        :param version: Version of Kustomize to use for rendering manifests. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#version Application#version}
        '''
        value = ApplicationSpecSourceKustomize(
            common_annotations=common_annotations,
            common_labels=common_labels,
            images=images,
            name_prefix=name_prefix,
            name_suffix=name_suffix,
            version=version,
        )

        return typing.cast(None, jsii.invoke(self, "putKustomize", [value]))

    @jsii.member(jsii_name="putPlugin")
    def put_plugin(
        self,
        *,
        env: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ApplicationSpecSourcePluginEnv", typing.Dict[builtins.str, typing.Any]]]]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param env: env block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#env Application#env}
        :param name: Name of the plugin. Only set the plugin name if the plugin is defined in ``argocd-cm``. If the plugin is defined as a sidecar, omit the name. The plugin will be automatically matched with the Application according to the plugin's discovery rules. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#name Application#name}
        '''
        value = ApplicationSpecSourcePlugin(env=env, name=name)

        return typing.cast(None, jsii.invoke(self, "putPlugin", [value]))

    @jsii.member(jsii_name="resetChart")
    def reset_chart(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetChart", []))

    @jsii.member(jsii_name="resetDirectory")
    def reset_directory(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDirectory", []))

    @jsii.member(jsii_name="resetHelm")
    def reset_helm(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHelm", []))

    @jsii.member(jsii_name="resetKustomize")
    def reset_kustomize(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKustomize", []))

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @jsii.member(jsii_name="resetPlugin")
    def reset_plugin(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlugin", []))

    @jsii.member(jsii_name="resetRef")
    def reset_ref(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRef", []))

    @jsii.member(jsii_name="resetTargetRevision")
    def reset_target_revision(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetRevision", []))

    @builtins.property
    @jsii.member(jsii_name="directory")
    def directory(self) -> ApplicationSpecSourceDirectoryOutputReference:
        return typing.cast(ApplicationSpecSourceDirectoryOutputReference, jsii.get(self, "directory"))

    @builtins.property
    @jsii.member(jsii_name="helm")
    def helm(self) -> ApplicationSpecSourceHelmOutputReference:
        return typing.cast(ApplicationSpecSourceHelmOutputReference, jsii.get(self, "helm"))

    @builtins.property
    @jsii.member(jsii_name="kustomize")
    def kustomize(self) -> ApplicationSpecSourceKustomizeOutputReference:
        return typing.cast(ApplicationSpecSourceKustomizeOutputReference, jsii.get(self, "kustomize"))

    @builtins.property
    @jsii.member(jsii_name="plugin")
    def plugin(self) -> "ApplicationSpecSourcePluginOutputReference":
        return typing.cast("ApplicationSpecSourcePluginOutputReference", jsii.get(self, "plugin"))

    @builtins.property
    @jsii.member(jsii_name="chartInput")
    def chart_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "chartInput"))

    @builtins.property
    @jsii.member(jsii_name="directoryInput")
    def directory_input(self) -> typing.Optional[ApplicationSpecSourceDirectory]:
        return typing.cast(typing.Optional[ApplicationSpecSourceDirectory], jsii.get(self, "directoryInput"))

    @builtins.property
    @jsii.member(jsii_name="helmInput")
    def helm_input(self) -> typing.Optional[ApplicationSpecSourceHelm]:
        return typing.cast(typing.Optional[ApplicationSpecSourceHelm], jsii.get(self, "helmInput"))

    @builtins.property
    @jsii.member(jsii_name="kustomizeInput")
    def kustomize_input(self) -> typing.Optional[ApplicationSpecSourceKustomize]:
        return typing.cast(typing.Optional[ApplicationSpecSourceKustomize], jsii.get(self, "kustomizeInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="pluginInput")
    def plugin_input(self) -> typing.Optional["ApplicationSpecSourcePlugin"]:
        return typing.cast(typing.Optional["ApplicationSpecSourcePlugin"], jsii.get(self, "pluginInput"))

    @builtins.property
    @jsii.member(jsii_name="refInput")
    def ref_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "refInput"))

    @builtins.property
    @jsii.member(jsii_name="repoUrlInput")
    def repo_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repoUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="targetRevisionInput")
    def target_revision_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetRevisionInput"))

    @builtins.property
    @jsii.member(jsii_name="chart")
    def chart(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "chart"))

    @chart.setter
    def chart(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4fb056599cfba845b251c32a4edd5efb1d8081800bbcb04aa334cd6fea741c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "chart", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3dbab1c0ef1b69104f766b4e271da898d8b7702eef6db6b22c17c0e4028ddb51)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="ref")
    def ref(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ref"))

    @ref.setter
    def ref(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9af4f3ef5ff931eaa5d74067b0e41a4eb3bdb1928184faf249a9bc88608266b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ref", value)

    @builtins.property
    @jsii.member(jsii_name="repoUrl")
    def repo_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repoUrl"))

    @repo_url.setter
    def repo_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8abb7adffc4520e6a99f590ee2011b6b73f5905df368342cf5a53149f40a9823)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repoUrl", value)

    @builtins.property
    @jsii.member(jsii_name="targetRevision")
    def target_revision(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetRevision"))

    @target_revision.setter
    def target_revision(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03303ccc922409280d356e8215f0804c655e20843ee0ab8569d87caf882903ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetRevision", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ApplicationSpecSource]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ApplicationSpecSource]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ApplicationSpecSource]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b274fac4cf1b68c781851ca8d256c488f9e7c3b6c52a7c56a1ab6fd78cd9083)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="argocd.application.ApplicationSpecSourcePlugin",
    jsii_struct_bases=[],
    name_mapping={"env": "env", "name": "name"},
)
class ApplicationSpecSourcePlugin:
    def __init__(
        self,
        *,
        env: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ApplicationSpecSourcePluginEnv", typing.Dict[builtins.str, typing.Any]]]]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param env: env block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#env Application#env}
        :param name: Name of the plugin. Only set the plugin name if the plugin is defined in ``argocd-cm``. If the plugin is defined as a sidecar, omit the name. The plugin will be automatically matched with the Application according to the plugin's discovery rules. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#name Application#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae8731d8745d57633f45b9fc4e2c2fc674b72f6abc612bd6cdecc5d908b93fcc)
            check_type(argname="argument env", value=env, expected_type=type_hints["env"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if env is not None:
            self._values["env"] = env
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def env(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ApplicationSpecSourcePluginEnv"]]]:
        '''env block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#env Application#env}
        '''
        result = self._values.get("env")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ApplicationSpecSourcePluginEnv"]]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the plugin.

        Only set the plugin name if the plugin is defined in ``argocd-cm``. If the plugin is defined as a sidecar, omit the name. The plugin will be automatically matched with the Application according to the plugin's discovery rules.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#name Application#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationSpecSourcePlugin(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="argocd.application.ApplicationSpecSourcePluginEnv",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value"},
)
class ApplicationSpecSourcePluginEnv:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#name Application#name}
        :param value: Value of the environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#value Application#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e95d0ed34e58c55a6ae4efcd9da381b73b72fe9b5e6747ab7fd605140e196c0)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#name Application#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Value of the environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#value Application#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationSpecSourcePluginEnv(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationSpecSourcePluginEnvList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.application.ApplicationSpecSourcePluginEnvList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__49b176469990e94b3440c9331392c9570b8282d6d6c23d5433b69644f9a58600)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApplicationSpecSourcePluginEnvOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bfcb819ce69d530bd08aa0a8a7b7f6659bbd6653ad4619b62c71047e3cd58b64)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApplicationSpecSourcePluginEnvOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20fb3e8e0db52a7428e0d4e1fd542cda78fa4984d99b3bad748b8b16a7235067)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4d083f4c3141f0e274cdacfbbe9dba3104bb139abdec4cc516105d4dcdf3b8cb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__daa18289324ed87dcf4b4761122449e2944de2818e3513a727eeb76d4229500b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ApplicationSpecSourcePluginEnv]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ApplicationSpecSourcePluginEnv]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ApplicationSpecSourcePluginEnv]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ca2697337c734837e106fcf4b6fbe39a92b09491f94d0f2b4702f64621d28fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationSpecSourcePluginEnvOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.application.ApplicationSpecSourcePluginEnvOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7e9711afe94235f11591c0d8de795f365ff9f8f5e917e37a7da410173ffa0727)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a40215c603323bd56f804979b9cc445013fb6ff3eabd40d93981b6ef42978515)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6134194328d51a7d6f26a350159aaf2757ee8d775cd5dcd189b64a4608616e74)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ApplicationSpecSourcePluginEnv]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ApplicationSpecSourcePluginEnv]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ApplicationSpecSourcePluginEnv]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af31ffc6a478d1934c08be8326444313eea0ab4f81026e3bc39ab14c219f83b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationSpecSourcePluginOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.application.ApplicationSpecSourcePluginOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__77391f0b63916840bc7ce4db7b64f7ffdc296c8f9159a24e4431d1fe6f328181)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putEnv")
    def put_env(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ApplicationSpecSourcePluginEnv, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1863ef5519ede519de02d082707f4249b41d8589a0aebba721bffceb8e804212)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEnv", [value]))

    @jsii.member(jsii_name="resetEnv")
    def reset_env(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnv", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="env")
    def env(self) -> ApplicationSpecSourcePluginEnvList:
        return typing.cast(ApplicationSpecSourcePluginEnvList, jsii.get(self, "env"))

    @builtins.property
    @jsii.member(jsii_name="envInput")
    def env_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ApplicationSpecSourcePluginEnv]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ApplicationSpecSourcePluginEnv]]], jsii.get(self, "envInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7adb3e9412ea37e4ab5fc45b2d0c9de1f8d999ae343c7c8ac3da709d9ccf74c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApplicationSpecSourcePlugin]:
        return typing.cast(typing.Optional[ApplicationSpecSourcePlugin], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApplicationSpecSourcePlugin],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__683048038985f04ca75699527cd4483f8d88b74d9aa109c16713639bc1dffd03)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="argocd.application.ApplicationSpecSyncPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "automated": "automated",
        "managed_namespace_metadata": "managedNamespaceMetadata",
        "retry": "retry",
        "sync_options": "syncOptions",
    },
)
class ApplicationSpecSyncPolicy:
    def __init__(
        self,
        *,
        automated: typing.Optional[typing.Union["ApplicationSpecSyncPolicyAutomated", typing.Dict[builtins.str, typing.Any]]] = None,
        managed_namespace_metadata: typing.Optional[typing.Union["ApplicationSpecSyncPolicyManagedNamespaceMetadata", typing.Dict[builtins.str, typing.Any]]] = None,
        retry: typing.Optional[typing.Union["ApplicationSpecSyncPolicyRetry", typing.Dict[builtins.str, typing.Any]]] = None,
        sync_options: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param automated: automated block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#automated Application#automated}
        :param managed_namespace_metadata: managed_namespace_metadata block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#managed_namespace_metadata Application#managed_namespace_metadata}
        :param retry: retry block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#retry Application#retry}
        :param sync_options: List of sync options. More info: https://argo-cd.readthedocs.io/en/stable/user-guide/sync-options/. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#sync_options Application#sync_options}
        '''
        if isinstance(automated, dict):
            automated = ApplicationSpecSyncPolicyAutomated(**automated)
        if isinstance(managed_namespace_metadata, dict):
            managed_namespace_metadata = ApplicationSpecSyncPolicyManagedNamespaceMetadata(**managed_namespace_metadata)
        if isinstance(retry, dict):
            retry = ApplicationSpecSyncPolicyRetry(**retry)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2204f71a52678d24edc534a56123a23f8ca57f9bed26a475ddd3f7210ac0a67a)
            check_type(argname="argument automated", value=automated, expected_type=type_hints["automated"])
            check_type(argname="argument managed_namespace_metadata", value=managed_namespace_metadata, expected_type=type_hints["managed_namespace_metadata"])
            check_type(argname="argument retry", value=retry, expected_type=type_hints["retry"])
            check_type(argname="argument sync_options", value=sync_options, expected_type=type_hints["sync_options"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if automated is not None:
            self._values["automated"] = automated
        if managed_namespace_metadata is not None:
            self._values["managed_namespace_metadata"] = managed_namespace_metadata
        if retry is not None:
            self._values["retry"] = retry
        if sync_options is not None:
            self._values["sync_options"] = sync_options

    @builtins.property
    def automated(self) -> typing.Optional["ApplicationSpecSyncPolicyAutomated"]:
        '''automated block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#automated Application#automated}
        '''
        result = self._values.get("automated")
        return typing.cast(typing.Optional["ApplicationSpecSyncPolicyAutomated"], result)

    @builtins.property
    def managed_namespace_metadata(
        self,
    ) -> typing.Optional["ApplicationSpecSyncPolicyManagedNamespaceMetadata"]:
        '''managed_namespace_metadata block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#managed_namespace_metadata Application#managed_namespace_metadata}
        '''
        result = self._values.get("managed_namespace_metadata")
        return typing.cast(typing.Optional["ApplicationSpecSyncPolicyManagedNamespaceMetadata"], result)

    @builtins.property
    def retry(self) -> typing.Optional["ApplicationSpecSyncPolicyRetry"]:
        '''retry block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#retry Application#retry}
        '''
        result = self._values.get("retry")
        return typing.cast(typing.Optional["ApplicationSpecSyncPolicyRetry"], result)

    @builtins.property
    def sync_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of sync options. More info: https://argo-cd.readthedocs.io/en/stable/user-guide/sync-options/.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#sync_options Application#sync_options}
        '''
        result = self._values.get("sync_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationSpecSyncPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="argocd.application.ApplicationSpecSyncPolicyAutomated",
    jsii_struct_bases=[],
    name_mapping={
        "allow_empty": "allowEmpty",
        "prune": "prune",
        "self_heal": "selfHeal",
    },
)
class ApplicationSpecSyncPolicyAutomated:
    def __init__(
        self,
        *,
        allow_empty: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        prune: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        self_heal: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param allow_empty: Allows apps have zero live resources. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#allow_empty Application#allow_empty}
        :param prune: Whether to delete resources from the cluster that are not found in the sources anymore as part of automated sync. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#prune Application#prune}
        :param self_heal: Whether to revert resources back to their desired state upon modification in the cluster. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#self_heal Application#self_heal}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a92a6213b23c25814ceab9c10e2fc18ffa0151e57ecafad373f1fdd6dddc214)
            check_type(argname="argument allow_empty", value=allow_empty, expected_type=type_hints["allow_empty"])
            check_type(argname="argument prune", value=prune, expected_type=type_hints["prune"])
            check_type(argname="argument self_heal", value=self_heal, expected_type=type_hints["self_heal"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if allow_empty is not None:
            self._values["allow_empty"] = allow_empty
        if prune is not None:
            self._values["prune"] = prune
        if self_heal is not None:
            self._values["self_heal"] = self_heal

    @builtins.property
    def allow_empty(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Allows apps have zero live resources.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#allow_empty Application#allow_empty}
        '''
        result = self._values.get("allow_empty")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def prune(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to delete resources from the cluster that are not found in the sources anymore as part of automated sync.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#prune Application#prune}
        '''
        result = self._values.get("prune")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def self_heal(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to revert resources back to their desired state upon modification in the cluster.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#self_heal Application#self_heal}
        '''
        result = self._values.get("self_heal")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationSpecSyncPolicyAutomated(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationSpecSyncPolicyAutomatedOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.application.ApplicationSpecSyncPolicyAutomatedOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__50ee07246fe9d7949d5797bd7aef95e21925a3cb13646ff7e5d3acc4dba0f9b8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAllowEmpty")
    def reset_allow_empty(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowEmpty", []))

    @jsii.member(jsii_name="resetPrune")
    def reset_prune(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrune", []))

    @jsii.member(jsii_name="resetSelfHeal")
    def reset_self_heal(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSelfHeal", []))

    @builtins.property
    @jsii.member(jsii_name="allowEmptyInput")
    def allow_empty_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "allowEmptyInput"))

    @builtins.property
    @jsii.member(jsii_name="pruneInput")
    def prune_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "pruneInput"))

    @builtins.property
    @jsii.member(jsii_name="selfHealInput")
    def self_heal_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "selfHealInput"))

    @builtins.property
    @jsii.member(jsii_name="allowEmpty")
    def allow_empty(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "allowEmpty"))

    @allow_empty.setter
    def allow_empty(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44b3b6fc03e01c665c0e53969b4a9e6f4d1a6847c5d8833f6a3191912a20f224)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowEmpty", value)

    @builtins.property
    @jsii.member(jsii_name="prune")
    def prune(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "prune"))

    @prune.setter
    def prune(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a63305a28d12c43cd91c9947613b895b289fa5ca06dff1e697f107b61496609)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prune", value)

    @builtins.property
    @jsii.member(jsii_name="selfHeal")
    def self_heal(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "selfHeal"))

    @self_heal.setter
    def self_heal(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3515a678c2452d5f4c1b15a7b8ce2390372f1859528b517c0ef194720abcaa72)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "selfHeal", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApplicationSpecSyncPolicyAutomated]:
        return typing.cast(typing.Optional[ApplicationSpecSyncPolicyAutomated], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApplicationSpecSyncPolicyAutomated],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e100920ee5822ca81e0f825ad71dce9b5a8e2bf27de0fa343d3342b00e9fff0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="argocd.application.ApplicationSpecSyncPolicyManagedNamespaceMetadata",
    jsii_struct_bases=[],
    name_mapping={"annotations": "annotations", "labels": "labels"},
)
class ApplicationSpecSyncPolicyManagedNamespaceMetadata:
    def __init__(
        self,
        *,
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param annotations: Annotations to apply to the namespace. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#annotations Application#annotations}
        :param labels: Labels to apply to the namespace. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#labels Application#labels}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b94d6acb4b03a8b480e5c00bf71f7d96dac16f37e781c2b5d43d6c12a40b12e)
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if annotations is not None:
            self._values["annotations"] = annotations
        if labels is not None:
            self._values["labels"] = labels

    @builtins.property
    def annotations(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Annotations to apply to the namespace.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#annotations Application#annotations}
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Labels to apply to the namespace.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#labels Application#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationSpecSyncPolicyManagedNamespaceMetadata(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationSpecSyncPolicyManagedNamespaceMetadataOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.application.ApplicationSpecSyncPolicyManagedNamespaceMetadataOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__635b64369342358b04006b53404455ce707831a1fbaefd1e068f0ea27ec67a97)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAnnotations")
    def reset_annotations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnnotations", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @builtins.property
    @jsii.member(jsii_name="annotationsInput")
    def annotations_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "annotationsInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="annotations")
    def annotations(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "annotations"))

    @annotations.setter
    def annotations(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75659c78fc16058cb9e1c1bbde3c7ea77e4cb6d04f937b1f1acc2bebad476ea8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "annotations", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__207464664aac4d0d0c3d90c6f84217087ac3dbce8b801cf0047369142cd7499c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ApplicationSpecSyncPolicyManagedNamespaceMetadata]:
        return typing.cast(typing.Optional[ApplicationSpecSyncPolicyManagedNamespaceMetadata], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApplicationSpecSyncPolicyManagedNamespaceMetadata],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77cd7a902aeeabf71eded9a122f1da18cb38c5555ddba706bde261f8e8e7893c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationSpecSyncPolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.application.ApplicationSpecSyncPolicyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__445b6bd787b8201744d7dc953d8e1ab5ee466520b359a978b3dcdd3feb4dddd4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAutomated")
    def put_automated(
        self,
        *,
        allow_empty: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        prune: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        self_heal: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param allow_empty: Allows apps have zero live resources. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#allow_empty Application#allow_empty}
        :param prune: Whether to delete resources from the cluster that are not found in the sources anymore as part of automated sync. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#prune Application#prune}
        :param self_heal: Whether to revert resources back to their desired state upon modification in the cluster. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#self_heal Application#self_heal}
        '''
        value = ApplicationSpecSyncPolicyAutomated(
            allow_empty=allow_empty, prune=prune, self_heal=self_heal
        )

        return typing.cast(None, jsii.invoke(self, "putAutomated", [value]))

    @jsii.member(jsii_name="putManagedNamespaceMetadata")
    def put_managed_namespace_metadata(
        self,
        *,
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param annotations: Annotations to apply to the namespace. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#annotations Application#annotations}
        :param labels: Labels to apply to the namespace. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#labels Application#labels}
        '''
        value = ApplicationSpecSyncPolicyManagedNamespaceMetadata(
            annotations=annotations, labels=labels
        )

        return typing.cast(None, jsii.invoke(self, "putManagedNamespaceMetadata", [value]))

    @jsii.member(jsii_name="putRetry")
    def put_retry(
        self,
        *,
        backoff: typing.Optional[typing.Union["ApplicationSpecSyncPolicyRetryBackoff", typing.Dict[builtins.str, typing.Any]]] = None,
        limit: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param backoff: backoff block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#backoff Application#backoff}
        :param limit: Maximum number of attempts for retrying a failed sync. If set to 0, no retries will be performed. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#limit Application#limit}
        '''
        value = ApplicationSpecSyncPolicyRetry(backoff=backoff, limit=limit)

        return typing.cast(None, jsii.invoke(self, "putRetry", [value]))

    @jsii.member(jsii_name="resetAutomated")
    def reset_automated(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutomated", []))

    @jsii.member(jsii_name="resetManagedNamespaceMetadata")
    def reset_managed_namespace_metadata(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManagedNamespaceMetadata", []))

    @jsii.member(jsii_name="resetRetry")
    def reset_retry(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetry", []))

    @jsii.member(jsii_name="resetSyncOptions")
    def reset_sync_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSyncOptions", []))

    @builtins.property
    @jsii.member(jsii_name="automated")
    def automated(self) -> ApplicationSpecSyncPolicyAutomatedOutputReference:
        return typing.cast(ApplicationSpecSyncPolicyAutomatedOutputReference, jsii.get(self, "automated"))

    @builtins.property
    @jsii.member(jsii_name="managedNamespaceMetadata")
    def managed_namespace_metadata(
        self,
    ) -> ApplicationSpecSyncPolicyManagedNamespaceMetadataOutputReference:
        return typing.cast(ApplicationSpecSyncPolicyManagedNamespaceMetadataOutputReference, jsii.get(self, "managedNamespaceMetadata"))

    @builtins.property
    @jsii.member(jsii_name="retry")
    def retry(self) -> "ApplicationSpecSyncPolicyRetryOutputReference":
        return typing.cast("ApplicationSpecSyncPolicyRetryOutputReference", jsii.get(self, "retry"))

    @builtins.property
    @jsii.member(jsii_name="automatedInput")
    def automated_input(self) -> typing.Optional[ApplicationSpecSyncPolicyAutomated]:
        return typing.cast(typing.Optional[ApplicationSpecSyncPolicyAutomated], jsii.get(self, "automatedInput"))

    @builtins.property
    @jsii.member(jsii_name="managedNamespaceMetadataInput")
    def managed_namespace_metadata_input(
        self,
    ) -> typing.Optional[ApplicationSpecSyncPolicyManagedNamespaceMetadata]:
        return typing.cast(typing.Optional[ApplicationSpecSyncPolicyManagedNamespaceMetadata], jsii.get(self, "managedNamespaceMetadataInput"))

    @builtins.property
    @jsii.member(jsii_name="retryInput")
    def retry_input(self) -> typing.Optional["ApplicationSpecSyncPolicyRetry"]:
        return typing.cast(typing.Optional["ApplicationSpecSyncPolicyRetry"], jsii.get(self, "retryInput"))

    @builtins.property
    @jsii.member(jsii_name="syncOptionsInput")
    def sync_options_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "syncOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="syncOptions")
    def sync_options(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "syncOptions"))

    @sync_options.setter
    def sync_options(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a56fc6ace3463c0dec7f966981609a326521bde0309752802a0e4040f3e17b9e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "syncOptions", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApplicationSpecSyncPolicy]:
        return typing.cast(typing.Optional[ApplicationSpecSyncPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ApplicationSpecSyncPolicy]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77144bb459206cad14cdd86d5b27f38648a0a18e902d28f7e99bbb1221afe05f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="argocd.application.ApplicationSpecSyncPolicyRetry",
    jsii_struct_bases=[],
    name_mapping={"backoff": "backoff", "limit": "limit"},
)
class ApplicationSpecSyncPolicyRetry:
    def __init__(
        self,
        *,
        backoff: typing.Optional[typing.Union["ApplicationSpecSyncPolicyRetryBackoff", typing.Dict[builtins.str, typing.Any]]] = None,
        limit: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param backoff: backoff block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#backoff Application#backoff}
        :param limit: Maximum number of attempts for retrying a failed sync. If set to 0, no retries will be performed. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#limit Application#limit}
        '''
        if isinstance(backoff, dict):
            backoff = ApplicationSpecSyncPolicyRetryBackoff(**backoff)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c95133c3d8902d550ed02cd6fe13bf9768a3f31bde9c39306155b37f7e3a826b)
            check_type(argname="argument backoff", value=backoff, expected_type=type_hints["backoff"])
            check_type(argname="argument limit", value=limit, expected_type=type_hints["limit"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if backoff is not None:
            self._values["backoff"] = backoff
        if limit is not None:
            self._values["limit"] = limit

    @builtins.property
    def backoff(self) -> typing.Optional["ApplicationSpecSyncPolicyRetryBackoff"]:
        '''backoff block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#backoff Application#backoff}
        '''
        result = self._values.get("backoff")
        return typing.cast(typing.Optional["ApplicationSpecSyncPolicyRetryBackoff"], result)

    @builtins.property
    def limit(self) -> typing.Optional[builtins.str]:
        '''Maximum number of attempts for retrying a failed sync. If set to 0, no retries will be performed.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#limit Application#limit}
        '''
        result = self._values.get("limit")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationSpecSyncPolicyRetry(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="argocd.application.ApplicationSpecSyncPolicyRetryBackoff",
    jsii_struct_bases=[],
    name_mapping={
        "duration": "duration",
        "factor": "factor",
        "max_duration": "maxDuration",
    },
)
class ApplicationSpecSyncPolicyRetryBackoff:
    def __init__(
        self,
        *,
        duration: typing.Optional[builtins.str] = None,
        factor: typing.Optional[builtins.str] = None,
        max_duration: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param duration: Duration is the amount to back off. Default unit is seconds, but could also be a duration (e.g. ``2m``, ``1h``), as a string. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#duration Application#duration}
        :param factor: Factor to multiply the base duration after each failed retry. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#factor Application#factor}
        :param max_duration: Maximum amount of time allowed for the backoff strategy. Default unit is seconds, but could also be a duration (e.g. ``2m``, ``1h``), as a string. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#max_duration Application#max_duration}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec2008fa9150d7b079feb7c8a2891fb028c4ddae7f2f46275f6c31e7785fdcc5)
            check_type(argname="argument duration", value=duration, expected_type=type_hints["duration"])
            check_type(argname="argument factor", value=factor, expected_type=type_hints["factor"])
            check_type(argname="argument max_duration", value=max_duration, expected_type=type_hints["max_duration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if duration is not None:
            self._values["duration"] = duration
        if factor is not None:
            self._values["factor"] = factor
        if max_duration is not None:
            self._values["max_duration"] = max_duration

    @builtins.property
    def duration(self) -> typing.Optional[builtins.str]:
        '''Duration is the amount to back off.

        Default unit is seconds, but could also be a duration (e.g. ``2m``, ``1h``), as a string.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#duration Application#duration}
        '''
        result = self._values.get("duration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def factor(self) -> typing.Optional[builtins.str]:
        '''Factor to multiply the base duration after each failed retry.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#factor Application#factor}
        '''
        result = self._values.get("factor")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_duration(self) -> typing.Optional[builtins.str]:
        '''Maximum amount of time allowed for the backoff strategy.

        Default unit is seconds, but could also be a duration (e.g. ``2m``, ``1h``), as a string.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#max_duration Application#max_duration}
        '''
        result = self._values.get("max_duration")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationSpecSyncPolicyRetryBackoff(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationSpecSyncPolicyRetryBackoffOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.application.ApplicationSpecSyncPolicyRetryBackoffOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1d07693dbfef83d9ea76bb3039b88585e3a497fbbe2cff0c5f16467daa52a21a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDuration")
    def reset_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDuration", []))

    @jsii.member(jsii_name="resetFactor")
    def reset_factor(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFactor", []))

    @jsii.member(jsii_name="resetMaxDuration")
    def reset_max_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxDuration", []))

    @builtins.property
    @jsii.member(jsii_name="durationInput")
    def duration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "durationInput"))

    @builtins.property
    @jsii.member(jsii_name="factorInput")
    def factor_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "factorInput"))

    @builtins.property
    @jsii.member(jsii_name="maxDurationInput")
    def max_duration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxDurationInput"))

    @builtins.property
    @jsii.member(jsii_name="duration")
    def duration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "duration"))

    @duration.setter
    def duration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__671157ac0f5f799f168779fb615d9d53cfe16b6d7798f60e42382a14ed876e26)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "duration", value)

    @builtins.property
    @jsii.member(jsii_name="factor")
    def factor(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "factor"))

    @factor.setter
    def factor(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b39308b24877b1f8ddab6c5d7abc20ced8ab3a561e930990727d802c91461b61)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "factor", value)

    @builtins.property
    @jsii.member(jsii_name="maxDuration")
    def max_duration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxDuration"))

    @max_duration.setter
    def max_duration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7fe9b5f7be1799b06b43f568f013d3f6bc14b7617f70e1c718cf506a99c4ccd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxDuration", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApplicationSpecSyncPolicyRetryBackoff]:
        return typing.cast(typing.Optional[ApplicationSpecSyncPolicyRetryBackoff], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApplicationSpecSyncPolicyRetryBackoff],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60ca13cc31bfeecc7c6cb63d6b8e9cd66fabc4e424db4195a87c9b5355d70272)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationSpecSyncPolicyRetryOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.application.ApplicationSpecSyncPolicyRetryOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__14bc665cf716892472d9827a4a8a629fd12273fba414fe30bbbeb1957b0408fd)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putBackoff")
    def put_backoff(
        self,
        *,
        duration: typing.Optional[builtins.str] = None,
        factor: typing.Optional[builtins.str] = None,
        max_duration: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param duration: Duration is the amount to back off. Default unit is seconds, but could also be a duration (e.g. ``2m``, ``1h``), as a string. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#duration Application#duration}
        :param factor: Factor to multiply the base duration after each failed retry. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#factor Application#factor}
        :param max_duration: Maximum amount of time allowed for the backoff strategy. Default unit is seconds, but could also be a duration (e.g. ``2m``, ``1h``), as a string. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#max_duration Application#max_duration}
        '''
        value = ApplicationSpecSyncPolicyRetryBackoff(
            duration=duration, factor=factor, max_duration=max_duration
        )

        return typing.cast(None, jsii.invoke(self, "putBackoff", [value]))

    @jsii.member(jsii_name="resetBackoff")
    def reset_backoff(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackoff", []))

    @jsii.member(jsii_name="resetLimit")
    def reset_limit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLimit", []))

    @builtins.property
    @jsii.member(jsii_name="backoff")
    def backoff(self) -> ApplicationSpecSyncPolicyRetryBackoffOutputReference:
        return typing.cast(ApplicationSpecSyncPolicyRetryBackoffOutputReference, jsii.get(self, "backoff"))

    @builtins.property
    @jsii.member(jsii_name="backoffInput")
    def backoff_input(self) -> typing.Optional[ApplicationSpecSyncPolicyRetryBackoff]:
        return typing.cast(typing.Optional[ApplicationSpecSyncPolicyRetryBackoff], jsii.get(self, "backoffInput"))

    @builtins.property
    @jsii.member(jsii_name="limitInput")
    def limit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "limitInput"))

    @builtins.property
    @jsii.member(jsii_name="limit")
    def limit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "limit"))

    @limit.setter
    def limit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd638cee7ad552e65aa2b6e7912ae8bcbdfcd74b3d0b9d20508374eaab310656)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "limit", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApplicationSpecSyncPolicyRetry]:
        return typing.cast(typing.Optional[ApplicationSpecSyncPolicyRetry], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApplicationSpecSyncPolicyRetry],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99c86125ceeaa55f985a4957a64c8499843bf6e2fa324dcb3e2d1217017fafde)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="argocd.application.ApplicationStatus",
    jsii_struct_bases=[],
    name_mapping={},
)
class ApplicationStatus:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationStatus(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="argocd.application.ApplicationStatusConditions",
    jsii_struct_bases=[],
    name_mapping={},
)
class ApplicationStatusConditions:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationStatusConditions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationStatusConditionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.application.ApplicationStatusConditionsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__81b09d36a7328065846643131c8971178b46a277212a7157c726a24cfce7e1a8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ApplicationStatusConditionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43b6db3f4d81c3a0f4b937df65d889f36239f13a7ec10596e30a9ae67c504cfa)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApplicationStatusConditionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f86e0530148703613412c1ebeebcb74e8efdc4314443954a865903a0dc36f78f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a9307bf5fdd4afe6f03fa53840f21d0c9a798e857dbf4daf54425b40aa81ede7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7096dba706ff2ac0eea9dfb65329b01c9478ab54d919fa7d3d5bbdd2b7ba9a68)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class ApplicationStatusConditionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.application.ApplicationStatusConditionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__990e0236dfd0328439346ab7d010cff782c6baf17b0648b1b68c915edfcdb1e4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="lastTransitionTime")
    def last_transition_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastTransitionTime"))

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "message"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApplicationStatusConditions]:
        return typing.cast(typing.Optional[ApplicationStatusConditions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApplicationStatusConditions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db16ec464b27395e85b31fe4763fee83f5b894f3c51669c68236ff6aafab1eff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="argocd.application.ApplicationStatusHealth",
    jsii_struct_bases=[],
    name_mapping={},
)
class ApplicationStatusHealth:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationStatusHealth(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationStatusHealthList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.application.ApplicationStatusHealthList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__008ce6be10a89e21494902d26b785876b5c86d9fa56e58ae7e7bd2e6c4f2f434)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ApplicationStatusHealthOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__746cccf95de0e9a19770f43b721a7a77df53f78c449cbcdc5d0ed678424a19e9)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApplicationStatusHealthOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1210d5e21aef485c494a6b8e29967c3aa41c34a391be05fd0a86400b8c32504)
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
            type_hints = typing.get_type_hints(_typecheckingstub__27df8a6287f73f7a15d304e683ac01a4c2610425e3466e88262149be6f115ccd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5ba757e9a1c00abc190259b2bec0c5af3a2e898d995ef71695750d76249b1366)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class ApplicationStatusHealthOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.application.ApplicationStatusHealthOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0e8e889ca6cc1117a0cd7c7f4b42761f1cdacd08187687776803f2b9c0b963dd)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "message"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApplicationStatusHealth]:
        return typing.cast(typing.Optional[ApplicationStatusHealth], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ApplicationStatusHealth]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36a7d03251ff2872f255b968d9d46d74aaf10a100f677aa9ba581b36a68c5514)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationStatusList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.application.ApplicationStatusList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b2801613e37fcc1a66c814cfb9f2dff4c012444d075f10803e27bbf2d48cd3ff)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ApplicationStatusOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b28b542427b9c58361357ad1c3aecf7eff4f496c426d58205df2be690f3f84c3)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApplicationStatusOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__460eebbbf8360bcd94fe9b6fa228071c13b8ee7ff3d304eddc15b0ace6e234d9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__dea20af62eedba799db4dbd3c2b89972ad95f5f8b2e8afcaac27b457f220ce02)
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
            type_hints = typing.get_type_hints(_typecheckingstub__55a8b0ec0a9a35a1f20f626682ce1222f7eb2cce23016a70b2155190adc48e0e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


@jsii.data_type(
    jsii_type="argocd.application.ApplicationStatusOperationState",
    jsii_struct_bases=[],
    name_mapping={},
)
class ApplicationStatusOperationState:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationStatusOperationState(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationStatusOperationStateList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.application.ApplicationStatusOperationStateList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2f2622b170189f3b1d195c46a75c26f6082f58225c2edf795e1d0bc868f36fa2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApplicationStatusOperationStateOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7571f63ec30eccc426711aadae2d43d487bdd1bc6ff22a79beb840a23596e3b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApplicationStatusOperationStateOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a23bae7f367ef8acba44c8b8740973ed2d8eaa7ee0a5eaf8ff6a2d8b5366235)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8aff1c2e6731a97ab5db1a18727a4591c3c2cddc8d349587d5c6f5ba0baca18f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d1f6bca309e66aaac71595e78caef8cde24adb5ed3ad8d07d3fb4529216ab219)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class ApplicationStatusOperationStateOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.application.ApplicationStatusOperationStateOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6f1da4dab81077a6d3f82b8ba2a85cba50596f3d04229751809a02501ce3783a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="finishedAt")
    def finished_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "finishedAt"))

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "message"))

    @builtins.property
    @jsii.member(jsii_name="phase")
    def phase(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "phase"))

    @builtins.property
    @jsii.member(jsii_name="retryCount")
    def retry_count(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "retryCount"))

    @builtins.property
    @jsii.member(jsii_name="startedAt")
    def started_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startedAt"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApplicationStatusOperationState]:
        return typing.cast(typing.Optional[ApplicationStatusOperationState], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApplicationStatusOperationState],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ef535740c550e270628c91f1a335fce330bf9ed0a6a233f01ce5e341c312464)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationStatusOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.application.ApplicationStatusOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__44fc19fb0dd52ac7e4533fd5964ff0442c70d18086d175edf49940df5b6edc06)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="conditions")
    def conditions(self) -> ApplicationStatusConditionsList:
        return typing.cast(ApplicationStatusConditionsList, jsii.get(self, "conditions"))

    @builtins.property
    @jsii.member(jsii_name="health")
    def health(self) -> ApplicationStatusHealthList:
        return typing.cast(ApplicationStatusHealthList, jsii.get(self, "health"))

    @builtins.property
    @jsii.member(jsii_name="operationState")
    def operation_state(self) -> ApplicationStatusOperationStateList:
        return typing.cast(ApplicationStatusOperationStateList, jsii.get(self, "operationState"))

    @builtins.property
    @jsii.member(jsii_name="reconciledAt")
    def reconciled_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "reconciledAt"))

    @builtins.property
    @jsii.member(jsii_name="resources")
    def resources(self) -> "ApplicationStatusResourcesList":
        return typing.cast("ApplicationStatusResourcesList", jsii.get(self, "resources"))

    @builtins.property
    @jsii.member(jsii_name="summary")
    def summary(self) -> "ApplicationStatusSummaryList":
        return typing.cast("ApplicationStatusSummaryList", jsii.get(self, "summary"))

    @builtins.property
    @jsii.member(jsii_name="sync")
    def sync(self) -> "ApplicationStatusSyncList":
        return typing.cast("ApplicationStatusSyncList", jsii.get(self, "sync"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApplicationStatus]:
        return typing.cast(typing.Optional[ApplicationStatus], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ApplicationStatus]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfb26388f2882a8c89305282219bca20a607bc1302b388389e035f01d77074e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="argocd.application.ApplicationStatusResources",
    jsii_struct_bases=[],
    name_mapping={},
)
class ApplicationStatusResources:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationStatusResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="argocd.application.ApplicationStatusResourcesHealth",
    jsii_struct_bases=[],
    name_mapping={},
)
class ApplicationStatusResourcesHealth:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationStatusResourcesHealth(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationStatusResourcesHealthList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.application.ApplicationStatusResourcesHealthList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e60925428c3df4a5322d39458cfba3c4fa62c42bffadf8aaf7185774c240398f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApplicationStatusResourcesHealthOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11e16a1e88c4e42db44fa50aaf19bebe3ee5edd848028a8829db8e20503efd36)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApplicationStatusResourcesHealthOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea3a3dd27b8c8d7dad40793b1db2524366ad82faa5f381f80032f5e672020d4b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d19990b0af531a63bf1cf8dc0ea6fb1c4465146b8fef784ffe93dda931717442)
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
            type_hints = typing.get_type_hints(_typecheckingstub__beb41c901e6c86783c4a9ac5b91a9cde9fb976200eb45c7e653b8f1cb8bd33a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class ApplicationStatusResourcesHealthOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.application.ApplicationStatusResourcesHealthOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0dd477b6d83e3e12654c522d6a24c1cdabbe6c32c2f85328c0395ebda0498102)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "message"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApplicationStatusResourcesHealth]:
        return typing.cast(typing.Optional[ApplicationStatusResourcesHealth], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApplicationStatusResourcesHealth],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fac379f7669b5e96b268ca2287dbfa65b1eca55e9543742115bdbf4fb757aa85)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationStatusResourcesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.application.ApplicationStatusResourcesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7fb824fe6cd84bc4e2521bf4c21017fd5a1b3b692af90c1fb00d745fb9f20f0d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ApplicationStatusResourcesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f08771d44c16f53ebd5b4929ef416538b16c3b7edfc816c87cdc353100bdcffd)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApplicationStatusResourcesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ac41be3aabc6fce1fa9aee040ef5d7aa12ca5ac20a2e062f8850708e841ed26)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d94f766616f41b83cd36aeadff9155e5c565df0d3a92ea389a87d249cd3d0578)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f3bedef7b4d8070c97fe52ea2d7a6c2308f5e5839f31011ec4cc541da091c8d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class ApplicationStatusResourcesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.application.ApplicationStatusResourcesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6120a2834d73ee93269bdc1aee702e7ff397f6075c0135d323701777fdca0b4f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="group")
    def group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "group"))

    @builtins.property
    @jsii.member(jsii_name="health")
    def health(self) -> ApplicationStatusResourcesHealthList:
        return typing.cast(ApplicationStatusResourcesHealthList, jsii.get(self, "health"))

    @builtins.property
    @jsii.member(jsii_name="hook")
    def hook(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "hook"))

    @builtins.property
    @jsii.member(jsii_name="kind")
    def kind(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kind"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @builtins.property
    @jsii.member(jsii_name="requiresPruning")
    def requires_pruning(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "requiresPruning"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="syncWave")
    def sync_wave(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "syncWave"))

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApplicationStatusResources]:
        return typing.cast(typing.Optional[ApplicationStatusResources], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApplicationStatusResources],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25178cc0fa2c60d0c71e419fadd2e93221b981131d052587be9cf678f1261175)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="argocd.application.ApplicationStatusSummary",
    jsii_struct_bases=[],
    name_mapping={},
)
class ApplicationStatusSummary:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationStatusSummary(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationStatusSummaryList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.application.ApplicationStatusSummaryList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6df299437d13c70e3622fc199f8358f2cd669cbcacdaae40f5cf39d74798b2ca)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ApplicationStatusSummaryOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2782e13e85b84ed828720c60492ead1df0733852128c1c897813ceee986e6ee)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApplicationStatusSummaryOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__392a6eaf919b1ef05aa041940bf228d473c7e7c9a896b94b6c5ded43be8c478e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e537d55c6855880de26c199bb36441762f7a02ae9bf414b64c185046e785fda9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__706f5478e45e055e7a6c42a2bf682361346c44322dfa488186664fbcbac10af7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class ApplicationStatusSummaryOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.application.ApplicationStatusSummaryOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6f4f9d45249861d70a1e1cb8a5c28daaa0179f505fc36e1e21a97f943344be3c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="externalUrls")
    def external_urls(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "externalUrls"))

    @builtins.property
    @jsii.member(jsii_name="images")
    def images(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "images"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApplicationStatusSummary]:
        return typing.cast(typing.Optional[ApplicationStatusSummary], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ApplicationStatusSummary]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ba8962aac88f864d57b9066cae1384dffafe121326840b20ab38dc0f6fea4a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="argocd.application.ApplicationStatusSync",
    jsii_struct_bases=[],
    name_mapping={},
)
class ApplicationStatusSync:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationStatusSync(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationStatusSyncList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.application.ApplicationStatusSyncList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2d46f24acab0f168d1595a24f09849eaec72090233e68de2fd70e2f20e3df0cd)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ApplicationStatusSyncOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad4f06839b383a38a4309d3c7bc30613517d652a2f2ce72cdcd5fc6e7d2fba1a)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApplicationStatusSyncOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13a926ea3c85a565f8bb6fe142c0dbeac4739e83ab3fa7ac1377a23b6331c9d2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__880a4b3caf33014b5fe4f0533b63c9d161c5f64c6e9ad55cac360e8c1945e5c3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e446747c31b610533bb0ca4942f4b45159de2e6b1e12a8a2fd3fe743f1e34b9d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class ApplicationStatusSyncOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.application.ApplicationStatusSyncOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4f113a2d85601a2901510b39121ce4768da1ba36ec7ee99c01213f8d8073ea28)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="revision")
    def revision(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "revision"))

    @builtins.property
    @jsii.member(jsii_name="revisions")
    def revisions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "revisions"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApplicationStatusSync]:
        return typing.cast(typing.Optional[ApplicationStatusSync], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ApplicationStatusSync]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4afa314780fe18217ded070eb9f1618d11d30f6c689037365c4b5d554d0e630)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="argocd.application.ApplicationTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class ApplicationTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#create Application#create}.
        :param delete: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#delete Application#delete}.
        :param update: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#update Application#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2edfc22b7a5fa7dc13b9d3d0a47f59fe654ab6c1498efb9e36eeac24c3000b76)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#create Application#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#delete Application#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/application#update Application#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.application.ApplicationTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__201e9d8d9b5b9b65b2e3c12262c0f2a8e2e61599982ee65ec2611eef4ba22693)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="updateInput")
    def update_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updateInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b6aa28092e7f6f713d689993e1bb6c0cd117868112ed898afbacf9f7054a649)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__478b6433cff24709ee1199fcfb6afda4c553352e78629d75098c3aff15c8407f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a667a575043f1b68a314d0543226f3d18f3518fb156fb7b704dbed7b546c59e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ApplicationTimeouts]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ApplicationTimeouts]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ApplicationTimeouts]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__abcabd5517236ba53f230b55a8a90ae5ec29fc86b195d7cb798cd5e9e074c1a6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Application",
    "ApplicationConfig",
    "ApplicationMetadata",
    "ApplicationMetadataOutputReference",
    "ApplicationSpec",
    "ApplicationSpecDestination",
    "ApplicationSpecDestinationOutputReference",
    "ApplicationSpecIgnoreDifference",
    "ApplicationSpecIgnoreDifferenceList",
    "ApplicationSpecIgnoreDifferenceOutputReference",
    "ApplicationSpecInfo",
    "ApplicationSpecInfoList",
    "ApplicationSpecInfoOutputReference",
    "ApplicationSpecOutputReference",
    "ApplicationSpecSource",
    "ApplicationSpecSourceDirectory",
    "ApplicationSpecSourceDirectoryJsonnet",
    "ApplicationSpecSourceDirectoryJsonnetExtVar",
    "ApplicationSpecSourceDirectoryJsonnetExtVarList",
    "ApplicationSpecSourceDirectoryJsonnetExtVarOutputReference",
    "ApplicationSpecSourceDirectoryJsonnetOutputReference",
    "ApplicationSpecSourceDirectoryJsonnetTla",
    "ApplicationSpecSourceDirectoryJsonnetTlaList",
    "ApplicationSpecSourceDirectoryJsonnetTlaOutputReference",
    "ApplicationSpecSourceDirectoryOutputReference",
    "ApplicationSpecSourceHelm",
    "ApplicationSpecSourceHelmFileParameter",
    "ApplicationSpecSourceHelmFileParameterList",
    "ApplicationSpecSourceHelmFileParameterOutputReference",
    "ApplicationSpecSourceHelmOutputReference",
    "ApplicationSpecSourceHelmParameter",
    "ApplicationSpecSourceHelmParameterList",
    "ApplicationSpecSourceHelmParameterOutputReference",
    "ApplicationSpecSourceKustomize",
    "ApplicationSpecSourceKustomizeOutputReference",
    "ApplicationSpecSourceList",
    "ApplicationSpecSourceOutputReference",
    "ApplicationSpecSourcePlugin",
    "ApplicationSpecSourcePluginEnv",
    "ApplicationSpecSourcePluginEnvList",
    "ApplicationSpecSourcePluginEnvOutputReference",
    "ApplicationSpecSourcePluginOutputReference",
    "ApplicationSpecSyncPolicy",
    "ApplicationSpecSyncPolicyAutomated",
    "ApplicationSpecSyncPolicyAutomatedOutputReference",
    "ApplicationSpecSyncPolicyManagedNamespaceMetadata",
    "ApplicationSpecSyncPolicyManagedNamespaceMetadataOutputReference",
    "ApplicationSpecSyncPolicyOutputReference",
    "ApplicationSpecSyncPolicyRetry",
    "ApplicationSpecSyncPolicyRetryBackoff",
    "ApplicationSpecSyncPolicyRetryBackoffOutputReference",
    "ApplicationSpecSyncPolicyRetryOutputReference",
    "ApplicationStatus",
    "ApplicationStatusConditions",
    "ApplicationStatusConditionsList",
    "ApplicationStatusConditionsOutputReference",
    "ApplicationStatusHealth",
    "ApplicationStatusHealthList",
    "ApplicationStatusHealthOutputReference",
    "ApplicationStatusList",
    "ApplicationStatusOperationState",
    "ApplicationStatusOperationStateList",
    "ApplicationStatusOperationStateOutputReference",
    "ApplicationStatusOutputReference",
    "ApplicationStatusResources",
    "ApplicationStatusResourcesHealth",
    "ApplicationStatusResourcesHealthList",
    "ApplicationStatusResourcesHealthOutputReference",
    "ApplicationStatusResourcesList",
    "ApplicationStatusResourcesOutputReference",
    "ApplicationStatusSummary",
    "ApplicationStatusSummaryList",
    "ApplicationStatusSummaryOutputReference",
    "ApplicationStatusSync",
    "ApplicationStatusSyncList",
    "ApplicationStatusSyncOutputReference",
    "ApplicationTimeouts",
    "ApplicationTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__ff2060e2db12056c6edfd8b05b5245c87e0ed133d702c76bb1f39740052edae3(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    metadata: typing.Union[ApplicationMetadata, typing.Dict[builtins.str, typing.Any]],
    spec: typing.Union[ApplicationSpec, typing.Dict[builtins.str, typing.Any]],
    cascade: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[ApplicationTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    wait: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
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

def _typecheckingstub__f8354a567245d0a18b236ea4b84300144d25413d265f7bc904b0374c52398799(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__053b48ff7396f7435e4fa88d9bbe0b94c2acdc2c7e61e2c81a8565007e1cf1a5(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b297bb4fb506ef8907df68284422087d5c670c98cf257a8602be9bae1e188b8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b141cee9ba1b0bd14e567dbaeae20a2c6db781e95b37c40265dc8144fc47fbf(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__439a6f762db453a906fff9050680d3e514920bcdef53433337af2ecfad60171e(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    metadata: typing.Union[ApplicationMetadata, typing.Dict[builtins.str, typing.Any]],
    spec: typing.Union[ApplicationSpec, typing.Dict[builtins.str, typing.Any]],
    cascade: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[ApplicationTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    wait: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12ea5f81842268e5c2fb7092e46b5f2e8b9b3d4006534783a8da85ff74049579(
    *,
    annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    name: typing.Optional[builtins.str] = None,
    namespace: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3320f520ea709ddb87c7bbe756f53dbe41c62965e22c0e70a8d8b736aa99b96b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53a3ef0eed61a30f52f5589b61ac9fca8c6dca92188ef67c7229c1330f69b0d5(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f495be8bc7541447054583437a4a7af07a75fddc47f005e179d1874273047c8(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b344effed70d15e630d888e9c113c033823d214e4fc308ad86f67b011d51d69b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c02ae74fdc0c52dd0f328d4c880c36d143e2b979d1370c78849cab1d0cee9c37(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bbdeac9cbcdf3c30071a9ba5625f2efcc79dcbf0b435e3a384e1a63cec5d7ff(
    value: typing.Optional[ApplicationMetadata],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12047fb70e97625aed3e2f1971053ec075ffaeb0b75d8f9e072fe6145f7d8a95(
    *,
    destination: typing.Union[ApplicationSpecDestination, typing.Dict[builtins.str, typing.Any]],
    source: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ApplicationSpecSource, typing.Dict[builtins.str, typing.Any]]]],
    ignore_difference: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ApplicationSpecIgnoreDifference, typing.Dict[builtins.str, typing.Any]]]]] = None,
    info: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ApplicationSpecInfo, typing.Dict[builtins.str, typing.Any]]]]] = None,
    project: typing.Optional[builtins.str] = None,
    revision_history_limit: typing.Optional[jsii.Number] = None,
    sync_policy: typing.Optional[typing.Union[ApplicationSpecSyncPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4dd24961a7d63416c62e147aecefb2b2b4cce8ff6ebaa395d35e88481cc4b2fb(
    *,
    name: typing.Optional[builtins.str] = None,
    namespace: typing.Optional[builtins.str] = None,
    server: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__719bce6043ce804648a674ee3683e8ff86262c4bffd5c876c58baaaf646fb593(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__473293ac11e0068ba7e9ede13b2fe1777b12d5d6aa0ab980a63b3fd83720be92(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af015e15cb8bdda37838de1f8e70ce1b9979f2f7a269307ab9f0989184d4258c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8fe609b4ab0a8c069aa48e51c2b40ed716ad5aecebf8f37dafdccba73f60d00f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4254de5d3ff35f7cc8033b6fab8321603fd90afeba558dae4515ef44a922ae18(
    value: typing.Optional[ApplicationSpecDestination],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ef1b887193d869380370fa01aa4c450241f545f5b8f02621b707a1bff1b37ad(
    *,
    group: typing.Optional[builtins.str] = None,
    jq_path_expressions: typing.Optional[typing.Sequence[builtins.str]] = None,
    json_pointers: typing.Optional[typing.Sequence[builtins.str]] = None,
    kind: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    namespace: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f94bb0d3041263def2607283cf02b10204f1f1f80561e28859cfb13084b87090(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__233cc7b59e49e3f4f49a232878f3646de6e1a05c645236c223d4d34095ee2ac3(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__367774f0b63e9ec8af6d9caf0328a47c4c64b25883ce68cf2f55d54193b18079(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__149dba9dc5d8e68b95659c1c2eae0675bc02ab79da55c7c75f6cc79b384fbcea(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4cae609cd3c72a2f144c1c47eb5bf30e87f400634cee19345e696d3e8e81bc11(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__559e144a9bc52eda7a643a3d47d3333f2fd607ebd072d4cad821351b4241fe9b(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ApplicationSpecIgnoreDifference]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c79964aa9d48f5b057832a2bcd62b839f05d499dc5943154e866112b547e9ad4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc2516454797f80745ad7a5392b1cf019601ffc73bb4b4ac18863023e176ad88(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c0330d9dea81a5aa7463880f5a67445bab6e687c4fae8d4c7592280de21122d(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2936aa9aa32bcbf38199ddbcba4e31c45b94cfd36d0210bc578b62ae4e47dad9(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0da36795ca985a89da4eca5fbcb806009a7475efe9d277e5b18a4f6792a6a831(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61e274e4bba62121a1a8dd5c8607096a050b4dfc3c685c13f3a6202ee4c54a7e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1234b07c145430a578c70f4ce8e6884b78312b7632bdb03d95d2171a17512096(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73b92ee59e901bee9ad95ea401bda21211b4394ca1b0f165c8b57430933f46c9(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ApplicationSpecIgnoreDifference]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d8a5e81589680f910b4225b12a9dbf087ad1d165e54eeb83fad0dffba4827fc(
    *,
    name: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bbfc6763fcb104e516dc41832b05746165d69d903ca5dde4d7e947fc0e068d6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eaea8afb9c7221713150d4cce5c696da28fe2935cf6a6118a3c978e5a48bfc2a(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a456348a46ef6e10b28ff7eaa16915e334edb29c3a9fd5d2f24e3d07f428be8c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5dc286bb3fe3d8ef7006a628db3598a849b9542c181a468acd71f55e0a54f890(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1cf43d116cfb2f7a745e2a7af2320eaf78dccd07cfbae1bbedacb87efe1bfc81(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f62d7618701c8d784b87bd0de1cb943df618ef71ecabada1f009e3db04637d2(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ApplicationSpecInfo]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__345990858536f554e55f53962d19480211e296fdb894e9741ae45bbf6ead2be8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ae1edb93656088fa65f258295c6baf3f0568dd0e1f8d31d1d2a4ef248330845(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c4443d740620fdd68d2b6898e42439b3d009a02fc9ded76e765a2d4a16b93a2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45c75aa7e5c4d70ad68af87e9b92646390c126f89c081fb6fe7409f9a8b363c6(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ApplicationSpecInfo]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96c860e1b3d46f0bac46a0990ce67e68f786c770812b90a35bda5b12adf0c7dc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df2eeb53bfdec8548cfa827aafa5b62ee8334783663960a1c4fd402c5d8d50e3(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ApplicationSpecIgnoreDifference, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5beb50587d462ca024aa2b08fbc32e917c8fff2e48388c18aaff98bc87a0598f(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ApplicationSpecInfo, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7cc9198e0e919b3cf37ecb9786a516e26dfc31091ecc1d9e318558726b458a6f(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ApplicationSpecSource, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__883445e417d054d70523d710b48dbe2c631bda85f6596c1f12b78011c2911a4b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3c04f2d35b8e386bb09788ed7418a51c57948df1db57bd743be1873893d4913(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09a96425ae64f482351be4c73a27eef3d051f328c9d7a88f7916940bc69bfaca(
    value: typing.Optional[ApplicationSpec],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df7987686619a417603fbb6387e0b68448dfe01fd1a6f1f12f9bac8e0bf5c760(
    *,
    repo_url: builtins.str,
    chart: typing.Optional[builtins.str] = None,
    directory: typing.Optional[typing.Union[ApplicationSpecSourceDirectory, typing.Dict[builtins.str, typing.Any]]] = None,
    helm: typing.Optional[typing.Union[ApplicationSpecSourceHelm, typing.Dict[builtins.str, typing.Any]]] = None,
    kustomize: typing.Optional[typing.Union[ApplicationSpecSourceKustomize, typing.Dict[builtins.str, typing.Any]]] = None,
    path: typing.Optional[builtins.str] = None,
    plugin: typing.Optional[typing.Union[ApplicationSpecSourcePlugin, typing.Dict[builtins.str, typing.Any]]] = None,
    ref: typing.Optional[builtins.str] = None,
    target_revision: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2806c6d28c35b7da297dadbcd3b9a304c5413d05f1a906ade7b10745ab1f61e4(
    *,
    exclude: typing.Optional[builtins.str] = None,
    include: typing.Optional[builtins.str] = None,
    jsonnet: typing.Optional[typing.Union[ApplicationSpecSourceDirectoryJsonnet, typing.Dict[builtins.str, typing.Any]]] = None,
    recurse: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3bc5c6c29ec8f6c811b8a8d56094f1d67b33b36a8d4d9c917626282b0559b570(
    *,
    ext_var: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ApplicationSpecSourceDirectoryJsonnetExtVar, typing.Dict[builtins.str, typing.Any]]]]] = None,
    libs: typing.Optional[typing.Sequence[builtins.str]] = None,
    tla: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ApplicationSpecSourceDirectoryJsonnetTla, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7cef95497ca2fbaeccf98be6eee7e9c6722109d0394d0e3a73d4a4dd7a8009d(
    *,
    code: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    name: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e29dfe52f704a87055ff8a78f59919726100adafdd142431d8c957d111d508ee(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__389d19168187160e2bed3435933f1194323ab40248211f3de127c0ad9174f4c4(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03dac6a32750d927d97aec637197b47a9039926db08a05b0a2d4778a7aafca54(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2c048d377bf8edc3ac409696dfb736f037f5fb31a83848ac3fa228b1dae1ded(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b366a598e9345a5b72477808e65f28e1e1a89a7a9580ab868e6ed394086b279(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4bc2b2c71b90ce3715a9f78e0664cfbc3318f29cc2ef546635b811c4c13fa65(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ApplicationSpecSourceDirectoryJsonnetExtVar]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__004a8e755a3b7dc56260cb50d75d97de6d76c46d373c564fec538d519576e8de(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__816bbb64635d8a40f3e312149de45004789419334a9434904f78f0cb176e2007(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f478fffdd654272bb3ecf24306670779090c4833e1e25b89e8c7cda5f0076cc1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fa47ab859da88e84b1eb805e98f768914d1f11857bbf6bea5b76d9195ed1f1d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f8824907fdef2e0c76018c6ffa3150d482f836290ca3fd0251fb6c029dc901e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ApplicationSpecSourceDirectoryJsonnetExtVar]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b271ce75960966f94e8f274146d1246228bea2d20e299451872c478cb8e1de8e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dfe2a695a8376492b74f9069965ac72b1635a22722b43278326a8a309df33ddf(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ApplicationSpecSourceDirectoryJsonnetExtVar, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27243125bafd09a2e1733798747ebf1c395524f2bf8817207517579f5addb0ec(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ApplicationSpecSourceDirectoryJsonnetTla, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91f1ea104ac67160f39e0f1a3d7f5b8ab6b6fb4b11d8d23f6617cea00f73f79a(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cba06b93e0e3627cfaf31b87d2244bca1ba086e7600dc11af32fcb2ef2ac4a00(
    value: typing.Optional[ApplicationSpecSourceDirectoryJsonnet],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e955b3dcacf85c12f4753f824778a0da6ba6d579b008e754084d569864740cc(
    *,
    code: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    name: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8052f86a5390d9a855034b9c5b8065542d59a637d697451625dce0be1547d5c5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0971c37eaf7da6c6241383143cfd79e4f9e422a65b6dd0365c1016f43eb1e44b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54ae7f7d492911c8971819208c9112914bf73a323b603ae13c93838628eb2284(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf5f2d1775a8ebf829b2c72b1c90cd3dd0bb9bdd4bbd2ae05d6a36029a94cb02(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3606f2eb178482efd35b9bd82dd2abca08bbce5328ecb764c03c560699f1c04f(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__beb37088bb66e76d0ca4aba98f2f52b2c157e057fc08e2147881c45ce345f01a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ApplicationSpecSourceDirectoryJsonnetTla]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cef12e11ab5f0258c3756144bd805b87b5da292563c9bca539111b712416f99a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ded247989a2077df6e2b06f5eb1cf0fe60b017361be059dd67bc3f8e7362ff59(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94fe73bc5550498045a6714f6e26373adcf6f40abada2532d15794534993850a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4e7a3ed298ed0dfabb219035cb6d9dd99681d168b7c3045309c9dc1d04559e1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5b909f1cc487b3c4fb0b8b99a96d6f1e031c197d0aa8923484729e65ff20646(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ApplicationSpecSourceDirectoryJsonnetTla]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66e38b779a0450fed90ecfcf80d5a13bcf178ff4cd490308fc266af07c0adb81(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4cd2d1603d5fdddbde14676cf3a5c7a3510e3c416ec5f3a6ea9820481db6d292(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7ba38194dcdae9e45739f552ecd44b4a97d4dd79bbb6b0fab2ad6b6c0a9378c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a24af30b70184790de594d12fae5ed1c119a179e8046f36fa4ad689b2e2196b6(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__530bdb7a3fb963fee9dc11339cf506c695df3be2a37c73beef94bb4030aa89f1(
    value: typing.Optional[ApplicationSpecSourceDirectory],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e0adb29abb6424b8da42fc68a29e142433ad33701bea68a6a62129506a57f40(
    *,
    file_parameter: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ApplicationSpecSourceHelmFileParameter, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ignore_missing_value_files: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    parameter: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ApplicationSpecSourceHelmParameter, typing.Dict[builtins.str, typing.Any]]]]] = None,
    pass_credentials: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    release_name: typing.Optional[builtins.str] = None,
    skip_crds: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    value_files: typing.Optional[typing.Sequence[builtins.str]] = None,
    values: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe186f9cb859bccbd35fce614f2ccd9388b4c03b44058feacf89765955d08d34(
    *,
    name: builtins.str,
    path: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a458289a0039546cb1b15def1e413dbb06058be5a5063b8ff37d3a9218eb810(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4614ce1d1928057042aad2177ac49cdd08edea78ce87b03273e03900deaaa8e(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df1281ceb8360134db15e380deb345b9921fbf87746d936ecff6de17ed4c9ac1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bbdd00e021a969d6b323b11e7a8bba0f13e39b124bbb51afaea2fa3163feef1(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63ad157b61bc4e7ab87bb0791e73f5bfbca6e714506ebb051dbefd49500f7070(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47767669a634f3f6754df00fff9525858279e67699ecc23df747f684741426a3(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ApplicationSpecSourceHelmFileParameter]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92069268ce1f97fb9483c70ae5887bd9d969064bda847ecffbf5c6195c9e7e56(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__862beabf3f73e8f50d0d273f527c6e48764374ba40125de5652b06b4bcbbebcf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__100da5afa0f9f2f33e74801d664441d2b23c7ab321f360e51d814719e6513a11(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f17df0071d9c544bf5f8caee7582dcbb006f747aabd3eb8e803763e43830bbf4(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ApplicationSpecSourceHelmFileParameter]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e648453ce42f39fc05a5c3153ac1bfb9f7f5fc2d28911a9dc1c929e72d4e5dd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fdbd7963c14502a1822d326704d14215399088478cd67a59cdbd9677f2061527(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ApplicationSpecSourceHelmFileParameter, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94eac0454670314dd2eb33f6583a655655c47e9236a4fbb14306643084ff216e(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ApplicationSpecSourceHelmParameter, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7df200f33b8468bccc802ee59787a3f78cfc2a002daf797f765b8079e053293(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f69e8fb862286d7d161387959586092ccbd708a6a2281eba1f1cb75b1501704d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fea4069d1cad4f6d0d6f4608e1c44983594c182523caa90547b5a4666638a656(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1e65febdb9f855f098567fedd04e4ba21a7af1b0b441cde1c9c786a0959c12f(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c3b87f0669ef1241a1b5768402946ca07c276a74abae5cbb904ad6950d0c8fc(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5a55ee578c52159dcbea39e5fff73f10944fe7aff547841e1f1176568b6f93c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31e11abacb1b99eaf75fe179fe4b76a9705c3dbdacfa208ecf225b745cf77bb6(
    value: typing.Optional[ApplicationSpecSourceHelm],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9cb567346cb6a29e10ecc65deb88a4d4ea35ed1560eeaf02da6688940335eb1(
    *,
    force_string: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    name: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6cd139b8f3e35799f995521df86ffd09c85f85408f872ac84eb09b05884562cc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84b80ed04ee511a21e45318908ae96398438264aa02545d292378fcbcbefde73(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b6f2eef2ad51c1e9f3915f8b5eaef5b2fba53bec3fb973ca397d69ee362826c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2dc4a1e36deb47910bd3627899d6405834ae56f18dc78f6864ba73d228da06a(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc825ec619cc4a38de1fdae6257e91b79f89376df277b85b4d683735c64ab7b9(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2946f3ab23da1729269b6cee9072b755538391fdcd4b6e0677352f2a8f9d661a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ApplicationSpecSourceHelmParameter]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbbdaf75a25cb1e1c4d46d5d0400af917a60642f740de90ad41ca72df61337b4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__710d00650a3e9d285e5e4796764945cfe0f9a881f460589b3b4607b3d627e710(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e4fe7288c50d9dcd975e2cc832ad814bef5b417b9f338774f5ac8509df5ade8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d58b95d1309b97c04deb36da24e337eed1507c7a91162fe1c6f5b7b992ad7fd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f4281eb136d08ee1b84b2ef6e69c097c1c024e01a2256bca643ce6db1f45287(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ApplicationSpecSourceHelmParameter]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f62d81df08298daf480e1cd5c6e1ba1efc883eac8f488cae2a6073322622b4e(
    *,
    common_annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    common_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    images: typing.Optional[typing.Sequence[builtins.str]] = None,
    name_prefix: typing.Optional[builtins.str] = None,
    name_suffix: typing.Optional[builtins.str] = None,
    version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f62717bcac2aa72bb2509a0337f4ba31e2d2fb16c06ae9ca9d376ecc0cc84f5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40b79a627f2c374a3178c622aca7273a20f758dfc62f576447f8d302ecdc84a9(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bafba1b8348086d2f9c5206afdf21769cb59475f7c9fd76c6b9757d9093a7dbc(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16a6ea857e1512f8c0fa4962348ff8b7e4f0b90e1a1ad23af551bf40ca637528(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac2ffc3de435edb636067fea701a51a55ebd083cf4538cabb7aac7658b76654a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51d1f758e8d64b7431f41a3d6958e659ba4c44a636582f9e47b4b6a48f731bc4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4f37266837882808180c6242ad0fa32fba29ccfd8a59623492df84e98eec999(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15bf25b40ac59cff3ef2b2faba4982965eb1a139c0d226e499aae550d64c4721(
    value: typing.Optional[ApplicationSpecSourceKustomize],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77cc2d932677ff5fd585f48970947974f69332c9a2acbbddde7675ee74701cea(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__765c38c3205c56cad93e87d8519eb32216d2b61db63c058f0d29bb037893859f(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13204f5dbb92ce85fc93b56b22e0e508914df551fd01ad869171fdfbe98a1c29(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b344259dc66a623edf630be5fbe2901a97bad8688d2fbc11ce7da70c685eca20(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ecf11cee045f5110e7137c1a8703989387c04c4465b9269a437e17477e9929b(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b3e92dea0172401f906483a1f11aae3764e677c6db1ef2c18a51f3b58a1c7a7(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ApplicationSpecSource]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0c5744a9ca8d956c5ec9416a70ace50a5648c2a38e8ec0c0bea4a39a0b9288c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4fb056599cfba845b251c32a4edd5efb1d8081800bbcb04aa334cd6fea741c2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3dbab1c0ef1b69104f766b4e271da898d8b7702eef6db6b22c17c0e4028ddb51(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9af4f3ef5ff931eaa5d74067b0e41a4eb3bdb1928184faf249a9bc88608266b7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8abb7adffc4520e6a99f590ee2011b6b73f5905df368342cf5a53149f40a9823(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03303ccc922409280d356e8215f0804c655e20843ee0ab8569d87caf882903ac(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b274fac4cf1b68c781851ca8d256c488f9e7c3b6c52a7c56a1ab6fd78cd9083(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ApplicationSpecSource]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae8731d8745d57633f45b9fc4e2c2fc674b72f6abc612bd6cdecc5d908b93fcc(
    *,
    env: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ApplicationSpecSourcePluginEnv, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e95d0ed34e58c55a6ae4efcd9da381b73b72fe9b5e6747ab7fd605140e196c0(
    *,
    name: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49b176469990e94b3440c9331392c9570b8282d6d6c23d5433b69644f9a58600(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfcb819ce69d530bd08aa0a8a7b7f6659bbd6653ad4619b62c71047e3cd58b64(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20fb3e8e0db52a7428e0d4e1fd542cda78fa4984d99b3bad748b8b16a7235067(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d083f4c3141f0e274cdacfbbe9dba3104bb139abdec4cc516105d4dcdf3b8cb(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__daa18289324ed87dcf4b4761122449e2944de2818e3513a727eeb76d4229500b(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ca2697337c734837e106fcf4b6fbe39a92b09491f94d0f2b4702f64621d28fd(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ApplicationSpecSourcePluginEnv]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e9711afe94235f11591c0d8de795f365ff9f8f5e917e37a7da410173ffa0727(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a40215c603323bd56f804979b9cc445013fb6ff3eabd40d93981b6ef42978515(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6134194328d51a7d6f26a350159aaf2757ee8d775cd5dcd189b64a4608616e74(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af31ffc6a478d1934c08be8326444313eea0ab4f81026e3bc39ab14c219f83b8(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ApplicationSpecSourcePluginEnv]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77391f0b63916840bc7ce4db7b64f7ffdc296c8f9159a24e4431d1fe6f328181(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1863ef5519ede519de02d082707f4249b41d8589a0aebba721bffceb8e804212(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ApplicationSpecSourcePluginEnv, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7adb3e9412ea37e4ab5fc45b2d0c9de1f8d999ae343c7c8ac3da709d9ccf74c8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__683048038985f04ca75699527cd4483f8d88b74d9aa109c16713639bc1dffd03(
    value: typing.Optional[ApplicationSpecSourcePlugin],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2204f71a52678d24edc534a56123a23f8ca57f9bed26a475ddd3f7210ac0a67a(
    *,
    automated: typing.Optional[typing.Union[ApplicationSpecSyncPolicyAutomated, typing.Dict[builtins.str, typing.Any]]] = None,
    managed_namespace_metadata: typing.Optional[typing.Union[ApplicationSpecSyncPolicyManagedNamespaceMetadata, typing.Dict[builtins.str, typing.Any]]] = None,
    retry: typing.Optional[typing.Union[ApplicationSpecSyncPolicyRetry, typing.Dict[builtins.str, typing.Any]]] = None,
    sync_options: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a92a6213b23c25814ceab9c10e2fc18ffa0151e57ecafad373f1fdd6dddc214(
    *,
    allow_empty: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    prune: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    self_heal: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50ee07246fe9d7949d5797bd7aef95e21925a3cb13646ff7e5d3acc4dba0f9b8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44b3b6fc03e01c665c0e53969b4a9e6f4d1a6847c5d8833f6a3191912a20f224(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a63305a28d12c43cd91c9947613b895b289fa5ca06dff1e697f107b61496609(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3515a678c2452d5f4c1b15a7b8ce2390372f1859528b517c0ef194720abcaa72(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e100920ee5822ca81e0f825ad71dce9b5a8e2bf27de0fa343d3342b00e9fff0(
    value: typing.Optional[ApplicationSpecSyncPolicyAutomated],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b94d6acb4b03a8b480e5c00bf71f7d96dac16f37e781c2b5d43d6c12a40b12e(
    *,
    annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__635b64369342358b04006b53404455ce707831a1fbaefd1e068f0ea27ec67a97(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75659c78fc16058cb9e1c1bbde3c7ea77e4cb6d04f937b1f1acc2bebad476ea8(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__207464664aac4d0d0c3d90c6f84217087ac3dbce8b801cf0047369142cd7499c(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77cd7a902aeeabf71eded9a122f1da18cb38c5555ddba706bde261f8e8e7893c(
    value: typing.Optional[ApplicationSpecSyncPolicyManagedNamespaceMetadata],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__445b6bd787b8201744d7dc953d8e1ab5ee466520b359a978b3dcdd3feb4dddd4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a56fc6ace3463c0dec7f966981609a326521bde0309752802a0e4040f3e17b9e(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77144bb459206cad14cdd86d5b27f38648a0a18e902d28f7e99bbb1221afe05f(
    value: typing.Optional[ApplicationSpecSyncPolicy],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c95133c3d8902d550ed02cd6fe13bf9768a3f31bde9c39306155b37f7e3a826b(
    *,
    backoff: typing.Optional[typing.Union[ApplicationSpecSyncPolicyRetryBackoff, typing.Dict[builtins.str, typing.Any]]] = None,
    limit: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec2008fa9150d7b079feb7c8a2891fb028c4ddae7f2f46275f6c31e7785fdcc5(
    *,
    duration: typing.Optional[builtins.str] = None,
    factor: typing.Optional[builtins.str] = None,
    max_duration: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d07693dbfef83d9ea76bb3039b88585e3a497fbbe2cff0c5f16467daa52a21a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__671157ac0f5f799f168779fb615d9d53cfe16b6d7798f60e42382a14ed876e26(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b39308b24877b1f8ddab6c5d7abc20ced8ab3a561e930990727d802c91461b61(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7fe9b5f7be1799b06b43f568f013d3f6bc14b7617f70e1c718cf506a99c4ccd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60ca13cc31bfeecc7c6cb63d6b8e9cd66fabc4e424db4195a87c9b5355d70272(
    value: typing.Optional[ApplicationSpecSyncPolicyRetryBackoff],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14bc665cf716892472d9827a4a8a629fd12273fba414fe30bbbeb1957b0408fd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd638cee7ad552e65aa2b6e7912ae8bcbdfcd74b3d0b9d20508374eaab310656(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99c86125ceeaa55f985a4957a64c8499843bf6e2fa324dcb3e2d1217017fafde(
    value: typing.Optional[ApplicationSpecSyncPolicyRetry],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81b09d36a7328065846643131c8971178b46a277212a7157c726a24cfce7e1a8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43b6db3f4d81c3a0f4b937df65d889f36239f13a7ec10596e30a9ae67c504cfa(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f86e0530148703613412c1ebeebcb74e8efdc4314443954a865903a0dc36f78f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9307bf5fdd4afe6f03fa53840f21d0c9a798e857dbf4daf54425b40aa81ede7(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7096dba706ff2ac0eea9dfb65329b01c9478ab54d919fa7d3d5bbdd2b7ba9a68(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__990e0236dfd0328439346ab7d010cff782c6baf17b0648b1b68c915edfcdb1e4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db16ec464b27395e85b31fe4763fee83f5b894f3c51669c68236ff6aafab1eff(
    value: typing.Optional[ApplicationStatusConditions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__008ce6be10a89e21494902d26b785876b5c86d9fa56e58ae7e7bd2e6c4f2f434(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__746cccf95de0e9a19770f43b721a7a77df53f78c449cbcdc5d0ed678424a19e9(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1210d5e21aef485c494a6b8e29967c3aa41c34a391be05fd0a86400b8c32504(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27df8a6287f73f7a15d304e683ac01a4c2610425e3466e88262149be6f115ccd(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ba757e9a1c00abc190259b2bec0c5af3a2e898d995ef71695750d76249b1366(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e8e889ca6cc1117a0cd7c7f4b42761f1cdacd08187687776803f2b9c0b963dd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36a7d03251ff2872f255b968d9d46d74aaf10a100f677aa9ba581b36a68c5514(
    value: typing.Optional[ApplicationStatusHealth],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2801613e37fcc1a66c814cfb9f2dff4c012444d075f10803e27bbf2d48cd3ff(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b28b542427b9c58361357ad1c3aecf7eff4f496c426d58205df2be690f3f84c3(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__460eebbbf8360bcd94fe9b6fa228071c13b8ee7ff3d304eddc15b0ace6e234d9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dea20af62eedba799db4dbd3c2b89972ad95f5f8b2e8afcaac27b457f220ce02(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55a8b0ec0a9a35a1f20f626682ce1222f7eb2cce23016a70b2155190adc48e0e(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f2622b170189f3b1d195c46a75c26f6082f58225c2edf795e1d0bc868f36fa2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7571f63ec30eccc426711aadae2d43d487bdd1bc6ff22a79beb840a23596e3b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a23bae7f367ef8acba44c8b8740973ed2d8eaa7ee0a5eaf8ff6a2d8b5366235(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8aff1c2e6731a97ab5db1a18727a4591c3c2cddc8d349587d5c6f5ba0baca18f(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1f6bca309e66aaac71595e78caef8cde24adb5ed3ad8d07d3fb4529216ab219(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f1da4dab81077a6d3f82b8ba2a85cba50596f3d04229751809a02501ce3783a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ef535740c550e270628c91f1a335fce330bf9ed0a6a233f01ce5e341c312464(
    value: typing.Optional[ApplicationStatusOperationState],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44fc19fb0dd52ac7e4533fd5964ff0442c70d18086d175edf49940df5b6edc06(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfb26388f2882a8c89305282219bca20a607bc1302b388389e035f01d77074e8(
    value: typing.Optional[ApplicationStatus],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e60925428c3df4a5322d39458cfba3c4fa62c42bffadf8aaf7185774c240398f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11e16a1e88c4e42db44fa50aaf19bebe3ee5edd848028a8829db8e20503efd36(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea3a3dd27b8c8d7dad40793b1db2524366ad82faa5f381f80032f5e672020d4b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d19990b0af531a63bf1cf8dc0ea6fb1c4465146b8fef784ffe93dda931717442(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__beb41c901e6c86783c4a9ac5b91a9cde9fb976200eb45c7e653b8f1cb8bd33a2(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0dd477b6d83e3e12654c522d6a24c1cdabbe6c32c2f85328c0395ebda0498102(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fac379f7669b5e96b268ca2287dbfa65b1eca55e9543742115bdbf4fb757aa85(
    value: typing.Optional[ApplicationStatusResourcesHealth],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fb824fe6cd84bc4e2521bf4c21017fd5a1b3b692af90c1fb00d745fb9f20f0d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f08771d44c16f53ebd5b4929ef416538b16c3b7edfc816c87cdc353100bdcffd(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ac41be3aabc6fce1fa9aee040ef5d7aa12ca5ac20a2e062f8850708e841ed26(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d94f766616f41b83cd36aeadff9155e5c565df0d3a92ea389a87d249cd3d0578(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3bedef7b4d8070c97fe52ea2d7a6c2308f5e5839f31011ec4cc541da091c8d2(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6120a2834d73ee93269bdc1aee702e7ff397f6075c0135d323701777fdca0b4f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25178cc0fa2c60d0c71e419fadd2e93221b981131d052587be9cf678f1261175(
    value: typing.Optional[ApplicationStatusResources],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6df299437d13c70e3622fc199f8358f2cd669cbcacdaae40f5cf39d74798b2ca(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2782e13e85b84ed828720c60492ead1df0733852128c1c897813ceee986e6ee(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__392a6eaf919b1ef05aa041940bf228d473c7e7c9a896b94b6c5ded43be8c478e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e537d55c6855880de26c199bb36441762f7a02ae9bf414b64c185046e785fda9(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__706f5478e45e055e7a6c42a2bf682361346c44322dfa488186664fbcbac10af7(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f4f9d45249861d70a1e1cb8a5c28daaa0179f505fc36e1e21a97f943344be3c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ba8962aac88f864d57b9066cae1384dffafe121326840b20ab38dc0f6fea4a7(
    value: typing.Optional[ApplicationStatusSummary],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d46f24acab0f168d1595a24f09849eaec72090233e68de2fd70e2f20e3df0cd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad4f06839b383a38a4309d3c7bc30613517d652a2f2ce72cdcd5fc6e7d2fba1a(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13a926ea3c85a565f8bb6fe142c0dbeac4739e83ab3fa7ac1377a23b6331c9d2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__880a4b3caf33014b5fe4f0533b63c9d161c5f64c6e9ad55cac360e8c1945e5c3(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e446747c31b610533bb0ca4942f4b45159de2e6b1e12a8a2fd3fe743f1e34b9d(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f113a2d85601a2901510b39121ce4768da1ba36ec7ee99c01213f8d8073ea28(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4afa314780fe18217ded070eb9f1618d11d30f6c689037365c4b5d554d0e630(
    value: typing.Optional[ApplicationStatusSync],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2edfc22b7a5fa7dc13b9d3d0a47f59fe654ab6c1498efb9e36eeac24c3000b76(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__201e9d8d9b5b9b65b2e3c12262c0f2a8e2e61599982ee65ec2611eef4ba22693(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b6aa28092e7f6f713d689993e1bb6c0cd117868112ed898afbacf9f7054a649(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__478b6433cff24709ee1199fcfb6afda4c553352e78629d75098c3aff15c8407f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a667a575043f1b68a314d0543226f3d18f3518fb156fb7b704dbed7b546c59e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abcabd5517236ba53f230b55a8a90ae5ec29fc86b195d7cb798cd5e9e074c1a6(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ApplicationTimeouts]],
) -> None:
    """Type checking stubs"""
    pass
