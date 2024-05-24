'''
# `supabase_settings`

Refer to the Terraform Registory for docs: [`supabase_settings`](https://registry.terraform.io/providers/supabase/supabase/1.4.0/docs/resources/settings).
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


class Settings(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="supabase.settings.Settings",
):
    '''Represents a {@link https://registry.terraform.io/providers/supabase/supabase/1.4.0/docs/resources/settings supabase_settings}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        project_ref: builtins.str,
        api: typing.Optional[builtins.str] = None,
        auth: typing.Optional[builtins.str] = None,
        database: typing.Optional[builtins.str] = None,
        network: typing.Optional[builtins.str] = None,
        pooler: typing.Optional[builtins.str] = None,
        storage: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/supabase/supabase/1.4.0/docs/resources/settings supabase_settings} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param project_ref: Project reference ID. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/supabase/supabase/1.4.0/docs/resources/settings#project_ref Settings#project_ref}
        :param api: API settings as `serialised JSON <https://api.supabase.com/api/v1#/services/updatePostgRESTConfig>`_. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/supabase/supabase/1.4.0/docs/resources/settings#api Settings#api}
        :param auth: Auth settings as `serialised JSON <https://api.supabase.com/api/v1#/projects%20config/updateV1AuthConfig>`_. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/supabase/supabase/1.4.0/docs/resources/settings#auth Settings#auth}
        :param database: Database settings as `serialised JSON <https://api.supabase.com/api/v1#/projects%20config/updateConfig>`_. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/supabase/supabase/1.4.0/docs/resources/settings#database Settings#database}
        :param network: Network settings as serialised JSON. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/supabase/supabase/1.4.0/docs/resources/settings#network Settings#network}
        :param pooler: Pooler settings as serialised JSON. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/supabase/supabase/1.4.0/docs/resources/settings#pooler Settings#pooler}
        :param storage: Storage settings as serialised JSON. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/supabase/supabase/1.4.0/docs/resources/settings#storage Settings#storage}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c042aa4e691289c5cc68bda8565870a9fd542e3067a3c3617d180ddcc0940fe6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = SettingsConfig(
            project_ref=project_ref,
            api=api,
            auth=auth,
            database=database,
            network=network,
            pooler=pooler,
            storage=storage,
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
        '''Generates CDKTF code for importing a Settings resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the Settings to import.
        :param import_from_id: The id of the existing Settings that should be imported. Refer to the {@link https://registry.terraform.io/providers/supabase/supabase/1.4.0/docs/resources/settings#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the Settings to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad97b4ea59b0f94f0747a4ecbd803ccdd841f0779a15ac53f2fc9e288c4b50a3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="resetApi")
    def reset_api(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApi", []))

    @jsii.member(jsii_name="resetAuth")
    def reset_auth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuth", []))

    @jsii.member(jsii_name="resetDatabase")
    def reset_database(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatabase", []))

    @jsii.member(jsii_name="resetNetwork")
    def reset_network(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetwork", []))

    @jsii.member(jsii_name="resetPooler")
    def reset_pooler(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPooler", []))

    @jsii.member(jsii_name="resetStorage")
    def reset_storage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorage", []))

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
    @jsii.member(jsii_name="apiInput")
    def api_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiInput"))

    @builtins.property
    @jsii.member(jsii_name="authInput")
    def auth_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseInput")
    def database_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseInput"))

    @builtins.property
    @jsii.member(jsii_name="networkInput")
    def network_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkInput"))

    @builtins.property
    @jsii.member(jsii_name="poolerInput")
    def pooler_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "poolerInput"))

    @builtins.property
    @jsii.member(jsii_name="projectRefInput")
    def project_ref_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectRefInput"))

    @builtins.property
    @jsii.member(jsii_name="storageInput")
    def storage_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageInput"))

    @builtins.property
    @jsii.member(jsii_name="api")
    def api(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "api"))

    @api.setter
    def api(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b041649c8b469e6c410890b5711e5c39d4f880aaf15da6a5fd726af8808386b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "api", value)

    @builtins.property
    @jsii.member(jsii_name="auth")
    def auth(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "auth"))

    @auth.setter
    def auth(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__236ceccc2d1568871f1efa6fca667513297f8bf1e85c19929607a611b360d968)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "auth", value)

    @builtins.property
    @jsii.member(jsii_name="database")
    def database(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "database"))

    @database.setter
    def database(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ee6f5fcf791dc75072fec2791f74be613965173509020c8d3f324da6653e3d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "database", value)

    @builtins.property
    @jsii.member(jsii_name="network")
    def network(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "network"))

    @network.setter
    def network(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95efe24207a97883e3f11f394f0f28083fa537e5783654238694c086ef1b0c93)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "network", value)

    @builtins.property
    @jsii.member(jsii_name="pooler")
    def pooler(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pooler"))

    @pooler.setter
    def pooler(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44e187a4cfd7e8f26a22fc73a5fa98021777b53645fbea3752cce6822e8651ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pooler", value)

    @builtins.property
    @jsii.member(jsii_name="projectRef")
    def project_ref(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectRef"))

    @project_ref.setter
    def project_ref(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00b243990bee24741aca52e609e3b6756b296bd36c2b7e9ab314336cbd253c6b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectRef", value)

    @builtins.property
    @jsii.member(jsii_name="storage")
    def storage(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storage"))

    @storage.setter
    def storage(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b77cb6c7f95096fed8dbd3a2a9d450d33444d6c952c61ba46bed85968190a97)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storage", value)


@jsii.data_type(
    jsii_type="supabase.settings.SettingsConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "project_ref": "projectRef",
        "api": "api",
        "auth": "auth",
        "database": "database",
        "network": "network",
        "pooler": "pooler",
        "storage": "storage",
    },
)
class SettingsConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        project_ref: builtins.str,
        api: typing.Optional[builtins.str] = None,
        auth: typing.Optional[builtins.str] = None,
        database: typing.Optional[builtins.str] = None,
        network: typing.Optional[builtins.str] = None,
        pooler: typing.Optional[builtins.str] = None,
        storage: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param project_ref: Project reference ID. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/supabase/supabase/1.4.0/docs/resources/settings#project_ref Settings#project_ref}
        :param api: API settings as `serialised JSON <https://api.supabase.com/api/v1#/services/updatePostgRESTConfig>`_. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/supabase/supabase/1.4.0/docs/resources/settings#api Settings#api}
        :param auth: Auth settings as `serialised JSON <https://api.supabase.com/api/v1#/projects%20config/updateV1AuthConfig>`_. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/supabase/supabase/1.4.0/docs/resources/settings#auth Settings#auth}
        :param database: Database settings as `serialised JSON <https://api.supabase.com/api/v1#/projects%20config/updateConfig>`_. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/supabase/supabase/1.4.0/docs/resources/settings#database Settings#database}
        :param network: Network settings as serialised JSON. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/supabase/supabase/1.4.0/docs/resources/settings#network Settings#network}
        :param pooler: Pooler settings as serialised JSON. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/supabase/supabase/1.4.0/docs/resources/settings#pooler Settings#pooler}
        :param storage: Storage settings as serialised JSON. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/supabase/supabase/1.4.0/docs/resources/settings#storage Settings#storage}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b67494b2e28a03be10091dc24c421fedd06918db539728b7a39b27b999263dcb)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument project_ref", value=project_ref, expected_type=type_hints["project_ref"])
            check_type(argname="argument api", value=api, expected_type=type_hints["api"])
            check_type(argname="argument auth", value=auth, expected_type=type_hints["auth"])
            check_type(argname="argument database", value=database, expected_type=type_hints["database"])
            check_type(argname="argument network", value=network, expected_type=type_hints["network"])
            check_type(argname="argument pooler", value=pooler, expected_type=type_hints["pooler"])
            check_type(argname="argument storage", value=storage, expected_type=type_hints["storage"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "project_ref": project_ref,
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
        if api is not None:
            self._values["api"] = api
        if auth is not None:
            self._values["auth"] = auth
        if database is not None:
            self._values["database"] = database
        if network is not None:
            self._values["network"] = network
        if pooler is not None:
            self._values["pooler"] = pooler
        if storage is not None:
            self._values["storage"] = storage

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
    def project_ref(self) -> builtins.str:
        '''Project reference ID.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/supabase/supabase/1.4.0/docs/resources/settings#project_ref Settings#project_ref}
        '''
        result = self._values.get("project_ref")
        assert result is not None, "Required property 'project_ref' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def api(self) -> typing.Optional[builtins.str]:
        '''API settings as `serialised JSON <https://api.supabase.com/api/v1#/services/updatePostgRESTConfig>`_.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/supabase/supabase/1.4.0/docs/resources/settings#api Settings#api}
        '''
        result = self._values.get("api")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def auth(self) -> typing.Optional[builtins.str]:
        '''Auth settings as `serialised JSON <https://api.supabase.com/api/v1#/projects%20config/updateV1AuthConfig>`_.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/supabase/supabase/1.4.0/docs/resources/settings#auth Settings#auth}
        '''
        result = self._values.get("auth")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def database(self) -> typing.Optional[builtins.str]:
        '''Database settings as `serialised JSON <https://api.supabase.com/api/v1#/projects%20config/updateConfig>`_.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/supabase/supabase/1.4.0/docs/resources/settings#database Settings#database}
        '''
        result = self._values.get("database")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def network(self) -> typing.Optional[builtins.str]:
        '''Network settings as serialised JSON.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/supabase/supabase/1.4.0/docs/resources/settings#network Settings#network}
        '''
        result = self._values.get("network")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pooler(self) -> typing.Optional[builtins.str]:
        '''Pooler settings as serialised JSON.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/supabase/supabase/1.4.0/docs/resources/settings#pooler Settings#pooler}
        '''
        result = self._values.get("pooler")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage(self) -> typing.Optional[builtins.str]:
        '''Storage settings as serialised JSON.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/supabase/supabase/1.4.0/docs/resources/settings#storage Settings#storage}
        '''
        result = self._values.get("storage")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SettingsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Settings",
    "SettingsConfig",
]

publication.publish()

def _typecheckingstub__c042aa4e691289c5cc68bda8565870a9fd542e3067a3c3617d180ddcc0940fe6(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    project_ref: builtins.str,
    api: typing.Optional[builtins.str] = None,
    auth: typing.Optional[builtins.str] = None,
    database: typing.Optional[builtins.str] = None,
    network: typing.Optional[builtins.str] = None,
    pooler: typing.Optional[builtins.str] = None,
    storage: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__ad97b4ea59b0f94f0747a4ecbd803ccdd841f0779a15ac53f2fc9e288c4b50a3(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b041649c8b469e6c410890b5711e5c39d4f880aaf15da6a5fd726af8808386b6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__236ceccc2d1568871f1efa6fca667513297f8bf1e85c19929607a611b360d968(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ee6f5fcf791dc75072fec2791f74be613965173509020c8d3f324da6653e3d1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95efe24207a97883e3f11f394f0f28083fa537e5783654238694c086ef1b0c93(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44e187a4cfd7e8f26a22fc73a5fa98021777b53645fbea3752cce6822e8651ad(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00b243990bee24741aca52e609e3b6756b296bd36c2b7e9ab314336cbd253c6b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b77cb6c7f95096fed8dbd3a2a9d450d33444d6c952c61ba46bed85968190a97(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b67494b2e28a03be10091dc24c421fedd06918db539728b7a39b27b999263dcb(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    project_ref: builtins.str,
    api: typing.Optional[builtins.str] = None,
    auth: typing.Optional[builtins.str] = None,
    database: typing.Optional[builtins.str] = None,
    network: typing.Optional[builtins.str] = None,
    pooler: typing.Optional[builtins.str] = None,
    storage: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
