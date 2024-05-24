'''
# `vercel_log_drain`

Refer to the Terraform Registory for docs: [`vercel_log_drain`](https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/log_drain).
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


class LogDrain(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="vercel.logDrain.LogDrain",
):
    '''Represents a {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/log_drain vercel_log_drain}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        delivery_format: builtins.str,
        endpoint: builtins.str,
        environments: typing.Sequence[builtins.str],
        sources: typing.Sequence[builtins.str],
        headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        project_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        sampling_rate: typing.Optional[jsii.Number] = None,
        secret: typing.Optional[builtins.str] = None,
        team_id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/log_drain vercel_log_drain} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param delivery_format: The format log data should be delivered in. Can be ``json`` or ``ndjson``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/log_drain#delivery_format LogDrain#delivery_format}
        :param endpoint: Logs will be sent as POST requests to this URL. The endpoint will be verified, and must return a ``200`` status code and an ``x-vercel-verify`` header taken from the endpoint_verification data source. The value the ``x-vercel-verify`` header should be can be read from the ``vercel_endpoint_verification_code`` data source. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/log_drain#endpoint LogDrain#endpoint}
        :param environments: Logs from the selected environments will be forwarded to your webhook. At least one must be present. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/log_drain#environments LogDrain#environments}
        :param sources: A set of sources that the log drain should send logs for. Valid values are ``static``, ``edge``, ``external``, ``build`` and ``lambda``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/log_drain#sources LogDrain#sources}
        :param headers: Custom headers to include in requests to the log drain endpoint. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/log_drain#headers LogDrain#headers}
        :param project_ids: A list of project IDs that the log drain should be associated with. Logs from these projects will be sent log events to the specified endpoint. If omitted, logs will be sent for all projects. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/log_drain#project_ids LogDrain#project_ids}
        :param sampling_rate: A ratio of logs matching the sampling rate will be sent to your log drain. Should be a value between 0 and 1. If unspecified, all logs are sent. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/log_drain#sampling_rate LogDrain#sampling_rate}
        :param secret: A custom secret to be used for signing log events. You can use this secret to verify that log events are coming from Vercel and are not tampered with. See https://vercel.com/docs/observability/log-drains/log-drains-reference#secure-log-drains for full info. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/log_drain#secret LogDrain#secret}
        :param team_id: The ID of the team the Log Drain should exist under. Required when configuring a team resource if a default team has not been set in the provider. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/log_drain#team_id LogDrain#team_id}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__797c2ea200a5105fc03651576cb5a75ff8cb454e1e2a2d8b3a5127d48ff69854)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = LogDrainConfig(
            delivery_format=delivery_format,
            endpoint=endpoint,
            environments=environments,
            sources=sources,
            headers=headers,
            project_ids=project_ids,
            sampling_rate=sampling_rate,
            secret=secret,
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
        '''Generates CDKTF code for importing a LogDrain resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the LogDrain to import.
        :param import_from_id: The id of the existing LogDrain that should be imported. Refer to the {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/log_drain#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the LogDrain to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96fc74013479ce78d2848b46700948c4f7c284a51f035b2f182324fd262224ef)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="resetHeaders")
    def reset_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeaders", []))

    @jsii.member(jsii_name="resetProjectIds")
    def reset_project_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProjectIds", []))

    @jsii.member(jsii_name="resetSamplingRate")
    def reset_sampling_rate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSamplingRate", []))

    @jsii.member(jsii_name="resetSecret")
    def reset_secret(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecret", []))

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
    @jsii.member(jsii_name="deliveryFormatInput")
    def delivery_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deliveryFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointInput")
    def endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointInput"))

    @builtins.property
    @jsii.member(jsii_name="environmentsInput")
    def environments_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "environmentsInput"))

    @builtins.property
    @jsii.member(jsii_name="headersInput")
    def headers_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "headersInput"))

    @builtins.property
    @jsii.member(jsii_name="projectIdsInput")
    def project_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "projectIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="samplingRateInput")
    def sampling_rate_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "samplingRateInput"))

    @builtins.property
    @jsii.member(jsii_name="secretInput")
    def secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretInput"))

    @builtins.property
    @jsii.member(jsii_name="sourcesInput")
    def sources_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sourcesInput"))

    @builtins.property
    @jsii.member(jsii_name="teamIdInput")
    def team_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "teamIdInput"))

    @builtins.property
    @jsii.member(jsii_name="deliveryFormat")
    def delivery_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deliveryFormat"))

    @delivery_format.setter
    def delivery_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8894181e80dbbcbd613aa34549b53a2cddaf7347d34d3c52e199f516df20b7ee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deliveryFormat", value)

    @builtins.property
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpoint"))

    @endpoint.setter
    def endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__034b020af14f7aaff36db059c9f5890d1b6d8d254aef6402bd8ba910c52ef1d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpoint", value)

    @builtins.property
    @jsii.member(jsii_name="environments")
    def environments(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "environments"))

    @environments.setter
    def environments(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7964e2dea3389c3dd2eecb77cdaf174f5236186d433c4cb6b4b65be12454544)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environments", value)

    @builtins.property
    @jsii.member(jsii_name="headers")
    def headers(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "headers"))

    @headers.setter
    def headers(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03c423b9321ca6d80eb62d5f1cb26d54cc8f2a943a4b4353297b1777f33e37c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headers", value)

    @builtins.property
    @jsii.member(jsii_name="projectIds")
    def project_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "projectIds"))

    @project_ids.setter
    def project_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6dd2df2e550f3b3adcbc53292c00b7d682497582db559d80edff299029ecaeac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectIds", value)

    @builtins.property
    @jsii.member(jsii_name="samplingRate")
    def sampling_rate(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "samplingRate"))

    @sampling_rate.setter
    def sampling_rate(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1962c35556a6bad83f970f43409bb4f2477129b7605bf6f5e47bb1c9d21296c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "samplingRate", value)

    @builtins.property
    @jsii.member(jsii_name="secret")
    def secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secret"))

    @secret.setter
    def secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a01b045092d6d28e70c59caf95fdcab4f9b2c1bfcd2784058df3a6d97936d82)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secret", value)

    @builtins.property
    @jsii.member(jsii_name="sources")
    def sources(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sources"))

    @sources.setter
    def sources(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c75157638046ce44b89a8dab3ca0afa54b616ef9ae356fa557334f893d6cedd1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sources", value)

    @builtins.property
    @jsii.member(jsii_name="teamId")
    def team_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "teamId"))

    @team_id.setter
    def team_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51506e83736290915965de8a040a5e23ca6bfb177bbcd68c79eed89bf6a1b472)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "teamId", value)


@jsii.data_type(
    jsii_type="vercel.logDrain.LogDrainConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "delivery_format": "deliveryFormat",
        "endpoint": "endpoint",
        "environments": "environments",
        "sources": "sources",
        "headers": "headers",
        "project_ids": "projectIds",
        "sampling_rate": "samplingRate",
        "secret": "secret",
        "team_id": "teamId",
    },
)
class LogDrainConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        delivery_format: builtins.str,
        endpoint: builtins.str,
        environments: typing.Sequence[builtins.str],
        sources: typing.Sequence[builtins.str],
        headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        project_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        sampling_rate: typing.Optional[jsii.Number] = None,
        secret: typing.Optional[builtins.str] = None,
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
        :param delivery_format: The format log data should be delivered in. Can be ``json`` or ``ndjson``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/log_drain#delivery_format LogDrain#delivery_format}
        :param endpoint: Logs will be sent as POST requests to this URL. The endpoint will be verified, and must return a ``200`` status code and an ``x-vercel-verify`` header taken from the endpoint_verification data source. The value the ``x-vercel-verify`` header should be can be read from the ``vercel_endpoint_verification_code`` data source. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/log_drain#endpoint LogDrain#endpoint}
        :param environments: Logs from the selected environments will be forwarded to your webhook. At least one must be present. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/log_drain#environments LogDrain#environments}
        :param sources: A set of sources that the log drain should send logs for. Valid values are ``static``, ``edge``, ``external``, ``build`` and ``lambda``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/log_drain#sources LogDrain#sources}
        :param headers: Custom headers to include in requests to the log drain endpoint. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/log_drain#headers LogDrain#headers}
        :param project_ids: A list of project IDs that the log drain should be associated with. Logs from these projects will be sent log events to the specified endpoint. If omitted, logs will be sent for all projects. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/log_drain#project_ids LogDrain#project_ids}
        :param sampling_rate: A ratio of logs matching the sampling rate will be sent to your log drain. Should be a value between 0 and 1. If unspecified, all logs are sent. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/log_drain#sampling_rate LogDrain#sampling_rate}
        :param secret: A custom secret to be used for signing log events. You can use this secret to verify that log events are coming from Vercel and are not tampered with. See https://vercel.com/docs/observability/log-drains/log-drains-reference#secure-log-drains for full info. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/log_drain#secret LogDrain#secret}
        :param team_id: The ID of the team the Log Drain should exist under. Required when configuring a team resource if a default team has not been set in the provider. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/log_drain#team_id LogDrain#team_id}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d2b703ce656a9df883e932593c11d71b164b200789126d27fce74a3b116bc19)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument delivery_format", value=delivery_format, expected_type=type_hints["delivery_format"])
            check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
            check_type(argname="argument environments", value=environments, expected_type=type_hints["environments"])
            check_type(argname="argument sources", value=sources, expected_type=type_hints["sources"])
            check_type(argname="argument headers", value=headers, expected_type=type_hints["headers"])
            check_type(argname="argument project_ids", value=project_ids, expected_type=type_hints["project_ids"])
            check_type(argname="argument sampling_rate", value=sampling_rate, expected_type=type_hints["sampling_rate"])
            check_type(argname="argument secret", value=secret, expected_type=type_hints["secret"])
            check_type(argname="argument team_id", value=team_id, expected_type=type_hints["team_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "delivery_format": delivery_format,
            "endpoint": endpoint,
            "environments": environments,
            "sources": sources,
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
        if headers is not None:
            self._values["headers"] = headers
        if project_ids is not None:
            self._values["project_ids"] = project_ids
        if sampling_rate is not None:
            self._values["sampling_rate"] = sampling_rate
        if secret is not None:
            self._values["secret"] = secret
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
    def delivery_format(self) -> builtins.str:
        '''The format log data should be delivered in. Can be ``json`` or ``ndjson``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/log_drain#delivery_format LogDrain#delivery_format}
        '''
        result = self._values.get("delivery_format")
        assert result is not None, "Required property 'delivery_format' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def endpoint(self) -> builtins.str:
        '''Logs will be sent as POST requests to this URL.

        The endpoint will be verified, and must return a ``200`` status code and an ``x-vercel-verify`` header taken from the endpoint_verification data source. The value the ``x-vercel-verify`` header should be can be read from the ``vercel_endpoint_verification_code`` data source.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/log_drain#endpoint LogDrain#endpoint}
        '''
        result = self._values.get("endpoint")
        assert result is not None, "Required property 'endpoint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def environments(self) -> typing.List[builtins.str]:
        '''Logs from the selected environments will be forwarded to your webhook. At least one must be present.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/log_drain#environments LogDrain#environments}
        '''
        result = self._values.get("environments")
        assert result is not None, "Required property 'environments' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def sources(self) -> typing.List[builtins.str]:
        '''A set of sources that the log drain should send logs for.

        Valid values are ``static``, ``edge``, ``external``, ``build`` and ``lambda``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/log_drain#sources LogDrain#sources}
        '''
        result = self._values.get("sources")
        assert result is not None, "Required property 'sources' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def headers(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Custom headers to include in requests to the log drain endpoint.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/log_drain#headers LogDrain#headers}
        '''
        result = self._values.get("headers")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def project_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of project IDs that the log drain should be associated with.

        Logs from these projects will be sent log events to the specified endpoint. If omitted, logs will be sent for all projects.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/log_drain#project_ids LogDrain#project_ids}
        '''
        result = self._values.get("project_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def sampling_rate(self) -> typing.Optional[jsii.Number]:
        '''A ratio of logs matching the sampling rate will be sent to your log drain.

        Should be a value between 0 and 1. If unspecified, all logs are sent.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/log_drain#sampling_rate LogDrain#sampling_rate}
        '''
        result = self._values.get("sampling_rate")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def secret(self) -> typing.Optional[builtins.str]:
        '''A custom secret to be used for signing log events.

        You can use this secret to verify that log events are coming from Vercel and are not tampered with. See https://vercel.com/docs/observability/log-drains/log-drains-reference#secure-log-drains for full info.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/log_drain#secret LogDrain#secret}
        '''
        result = self._values.get("secret")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def team_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the team the Log Drain should exist under.

        Required when configuring a team resource if a default team has not been set in the provider.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/vercel/vercel/1.11.0/docs/resources/log_drain#team_id LogDrain#team_id}
        '''
        result = self._values.get("team_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogDrainConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "LogDrain",
    "LogDrainConfig",
]

publication.publish()

def _typecheckingstub__797c2ea200a5105fc03651576cb5a75ff8cb454e1e2a2d8b3a5127d48ff69854(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    delivery_format: builtins.str,
    endpoint: builtins.str,
    environments: typing.Sequence[builtins.str],
    sources: typing.Sequence[builtins.str],
    headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    project_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    sampling_rate: typing.Optional[jsii.Number] = None,
    secret: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__96fc74013479ce78d2848b46700948c4f7c284a51f035b2f182324fd262224ef(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8894181e80dbbcbd613aa34549b53a2cddaf7347d34d3c52e199f516df20b7ee(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__034b020af14f7aaff36db059c9f5890d1b6d8d254aef6402bd8ba910c52ef1d0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7964e2dea3389c3dd2eecb77cdaf174f5236186d433c4cb6b4b65be12454544(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03c423b9321ca6d80eb62d5f1cb26d54cc8f2a943a4b4353297b1777f33e37c0(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6dd2df2e550f3b3adcbc53292c00b7d682497582db559d80edff299029ecaeac(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1962c35556a6bad83f970f43409bb4f2477129b7605bf6f5e47bb1c9d21296c4(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a01b045092d6d28e70c59caf95fdcab4f9b2c1bfcd2784058df3a6d97936d82(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c75157638046ce44b89a8dab3ca0afa54b616ef9ae356fa557334f893d6cedd1(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51506e83736290915965de8a040a5e23ca6bfb177bbcd68c79eed89bf6a1b472(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d2b703ce656a9df883e932593c11d71b164b200789126d27fce74a3b116bc19(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    delivery_format: builtins.str,
    endpoint: builtins.str,
    environments: typing.Sequence[builtins.str],
    sources: typing.Sequence[builtins.str],
    headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    project_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    sampling_rate: typing.Optional[jsii.Number] = None,
    secret: typing.Optional[builtins.str] = None,
    team_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
