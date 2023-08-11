'''
# `digitalocean_uptime_alert`

Refer to the Terraform Registory for docs: [`digitalocean_uptime_alert`](https://registry.terraform.io/providers/digitalocean/digitalocean/2.29.0/docs/resources/uptime_alert).
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


class UptimeAlert(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.uptimeAlert.UptimeAlert",
):
    '''Represents a {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.29.0/docs/resources/uptime_alert digitalocean_uptime_alert}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        check_id: builtins.str,
        name: builtins.str,
        notifications: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["UptimeAlertNotifications", typing.Dict[builtins.str, typing.Any]]]],
        type: builtins.str,
        comparison: typing.Optional[builtins.str] = None,
        period: typing.Optional[builtins.str] = None,
        threshold: typing.Optional[jsii.Number] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.29.0/docs/resources/uptime_alert digitalocean_uptime_alert} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param check_id: A unique identifier for a check. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.29.0/docs/resources/uptime_alert#check_id UptimeAlert#check_id}
        :param name: A human-friendly display name for the alert. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.29.0/docs/resources/uptime_alert#name UptimeAlert#name}
        :param notifications: notifications block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.29.0/docs/resources/uptime_alert#notifications UptimeAlert#notifications}
        :param type: The type of health check to perform. Enum: 'latency' 'down' 'down_global' 'ssl_expiry'. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.29.0/docs/resources/uptime_alert#type UptimeAlert#type}
        :param comparison: The comparison operator used against the alert's threshold. Enum: 'greater_than' 'less_than. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.29.0/docs/resources/uptime_alert#comparison UptimeAlert#comparison}
        :param period: Period of time the threshold must be exceeded to trigger the alert. Enum '2m' '3m' '5m' '10m' '15m' '30m' '1h' Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.29.0/docs/resources/uptime_alert#period UptimeAlert#period}
        :param threshold: The threshold at which the alert will enter a trigger state. The specific threshold is dependent on the alert type. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.29.0/docs/resources/uptime_alert#threshold UptimeAlert#threshold}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bdbafca4cdd070aa8cb65d8c185255af22f0754c063b5178f1b90feeb581523f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = UptimeAlertConfig(
            check_id=check_id,
            name=name,
            notifications=notifications,
            type=type,
            comparison=comparison,
            period=period,
            threshold=threshold,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="putNotifications")
    def put_notifications(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["UptimeAlertNotifications", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d4eb37689e35432ed615dd37699a4e3461d7fa29617d7f4787fc54bab027002)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNotifications", [value]))

    @jsii.member(jsii_name="resetComparison")
    def reset_comparison(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComparison", []))

    @jsii.member(jsii_name="resetPeriod")
    def reset_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPeriod", []))

    @jsii.member(jsii_name="resetThreshold")
    def reset_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThreshold", []))

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
    @jsii.member(jsii_name="notifications")
    def notifications(self) -> "UptimeAlertNotificationsList":
        return typing.cast("UptimeAlertNotificationsList", jsii.get(self, "notifications"))

    @builtins.property
    @jsii.member(jsii_name="checkIdInput")
    def check_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "checkIdInput"))

    @builtins.property
    @jsii.member(jsii_name="comparisonInput")
    def comparison_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "comparisonInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="notificationsInput")
    def notifications_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["UptimeAlertNotifications"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["UptimeAlertNotifications"]]], jsii.get(self, "notificationsInput"))

    @builtins.property
    @jsii.member(jsii_name="periodInput")
    def period_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "periodInput"))

    @builtins.property
    @jsii.member(jsii_name="thresholdInput")
    def threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "thresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="checkId")
    def check_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "checkId"))

    @check_id.setter
    def check_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43575005823e3fc632c83182081a05b943bb3657858b4f0ed527db14e35429d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "checkId", value)

    @builtins.property
    @jsii.member(jsii_name="comparison")
    def comparison(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comparison"))

    @comparison.setter
    def comparison(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f9d1c5decdbf2afd55b01e6da607f972cf988a09ea6835ad2f00115691f498d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comparison", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea7f216c08dbac632739a3b1868a10e65fb0bf5abb2ad9e55e0855a17c9d3c7f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="period")
    def period(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "period"))

    @period.setter
    def period(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc59c7e58dac332f11000e39bfb98c256d99543b38992c5162b9abd640f8b45b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "period", value)

    @builtins.property
    @jsii.member(jsii_name="threshold")
    def threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "threshold"))

    @threshold.setter
    def threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f44321be343b8ff6ca23b9369cca78145355aa9c320d7c9379f5203c947c791)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "threshold", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3eab012d2ba1012f3005dc65596efbb1ad2abbb4f566f31ab3f9c9f3d45bb105)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)


@jsii.data_type(
    jsii_type="digitalocean.uptimeAlert.UptimeAlertConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "check_id": "checkId",
        "name": "name",
        "notifications": "notifications",
        "type": "type",
        "comparison": "comparison",
        "period": "period",
        "threshold": "threshold",
    },
)
class UptimeAlertConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        check_id: builtins.str,
        name: builtins.str,
        notifications: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["UptimeAlertNotifications", typing.Dict[builtins.str, typing.Any]]]],
        type: builtins.str,
        comparison: typing.Optional[builtins.str] = None,
        period: typing.Optional[builtins.str] = None,
        threshold: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param check_id: A unique identifier for a check. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.29.0/docs/resources/uptime_alert#check_id UptimeAlert#check_id}
        :param name: A human-friendly display name for the alert. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.29.0/docs/resources/uptime_alert#name UptimeAlert#name}
        :param notifications: notifications block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.29.0/docs/resources/uptime_alert#notifications UptimeAlert#notifications}
        :param type: The type of health check to perform. Enum: 'latency' 'down' 'down_global' 'ssl_expiry'. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.29.0/docs/resources/uptime_alert#type UptimeAlert#type}
        :param comparison: The comparison operator used against the alert's threshold. Enum: 'greater_than' 'less_than. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.29.0/docs/resources/uptime_alert#comparison UptimeAlert#comparison}
        :param period: Period of time the threshold must be exceeded to trigger the alert. Enum '2m' '3m' '5m' '10m' '15m' '30m' '1h' Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.29.0/docs/resources/uptime_alert#period UptimeAlert#period}
        :param threshold: The threshold at which the alert will enter a trigger state. The specific threshold is dependent on the alert type. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.29.0/docs/resources/uptime_alert#threshold UptimeAlert#threshold}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1785329ca2fa080ba550210e67198aba8807aa6b27188cf18bd76ce63b2af978)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument check_id", value=check_id, expected_type=type_hints["check_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument notifications", value=notifications, expected_type=type_hints["notifications"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument comparison", value=comparison, expected_type=type_hints["comparison"])
            check_type(argname="argument period", value=period, expected_type=type_hints["period"])
            check_type(argname="argument threshold", value=threshold, expected_type=type_hints["threshold"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "check_id": check_id,
            "name": name,
            "notifications": notifications,
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
        if comparison is not None:
            self._values["comparison"] = comparison
        if period is not None:
            self._values["period"] = period
        if threshold is not None:
            self._values["threshold"] = threshold

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
    def check_id(self) -> builtins.str:
        '''A unique identifier for a check.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.29.0/docs/resources/uptime_alert#check_id UptimeAlert#check_id}
        '''
        result = self._values.get("check_id")
        assert result is not None, "Required property 'check_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''A human-friendly display name for the alert.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.29.0/docs/resources/uptime_alert#name UptimeAlert#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def notifications(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["UptimeAlertNotifications"]]:
        '''notifications block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.29.0/docs/resources/uptime_alert#notifications UptimeAlert#notifications}
        '''
        result = self._values.get("notifications")
        assert result is not None, "Required property 'notifications' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["UptimeAlertNotifications"]], result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of health check to perform. Enum: 'latency' 'down' 'down_global' 'ssl_expiry'.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.29.0/docs/resources/uptime_alert#type UptimeAlert#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def comparison(self) -> typing.Optional[builtins.str]:
        '''The comparison operator used against the alert's threshold. Enum: 'greater_than' 'less_than.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.29.0/docs/resources/uptime_alert#comparison UptimeAlert#comparison}
        '''
        result = self._values.get("comparison")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def period(self) -> typing.Optional[builtins.str]:
        '''Period of time the threshold must be exceeded to trigger the alert.

        Enum '2m' '3m' '5m' '10m' '15m' '30m' '1h'

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.29.0/docs/resources/uptime_alert#period UptimeAlert#period}
        '''
        result = self._values.get("period")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def threshold(self) -> typing.Optional[jsii.Number]:
        '''The threshold at which the alert will enter a trigger state.

        The specific threshold is dependent on the alert type.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.29.0/docs/resources/uptime_alert#threshold UptimeAlert#threshold}
        '''
        result = self._values.get("threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UptimeAlertConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="digitalocean.uptimeAlert.UptimeAlertNotifications",
    jsii_struct_bases=[],
    name_mapping={"email": "email", "slack": "slack"},
)
class UptimeAlertNotifications:
    def __init__(
        self,
        *,
        email: typing.Optional[typing.Sequence[builtins.str]] = None,
        slack: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["UptimeAlertNotificationsSlack", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param email: List of email addresses to sent notifications to. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.29.0/docs/resources/uptime_alert#email UptimeAlert#email}
        :param slack: slack block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.29.0/docs/resources/uptime_alert#slack UptimeAlert#slack}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9eab64033296ac1d162c65dffb40dfd154f1150ed2899e64804a2c1208167abc)
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
            check_type(argname="argument slack", value=slack, expected_type=type_hints["slack"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if email is not None:
            self._values["email"] = email
        if slack is not None:
            self._values["slack"] = slack

    @builtins.property
    def email(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of email addresses to sent notifications to.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.29.0/docs/resources/uptime_alert#email UptimeAlert#email}
        '''
        result = self._values.get("email")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def slack(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["UptimeAlertNotificationsSlack"]]]:
        '''slack block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.29.0/docs/resources/uptime_alert#slack UptimeAlert#slack}
        '''
        result = self._values.get("slack")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["UptimeAlertNotificationsSlack"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UptimeAlertNotifications(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class UptimeAlertNotificationsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.uptimeAlert.UptimeAlertNotificationsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ffbab489b4c1b31968894059d5eec7ed4d17b34633f82090e0f80ecdf6983bc8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "UptimeAlertNotificationsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d175bd0db78f9e0f35bfbb1da8a7d3d4f285ee7012ed7423958381518ebf79c)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("UptimeAlertNotificationsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54b4bcbb49ea3da9bc936f002733e0f517f6bd7e78a558c68067bc6c9bca94fa)
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
            type_hints = typing.get_type_hints(_typecheckingstub__64d83b87b70334d45be4c6d8f80a4323b2c98852a6f0af95387539c6faa0bf72)
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
            type_hints = typing.get_type_hints(_typecheckingstub__743e120a3bfb09aabbd94cc98b3db8c6bf0b5d1c31c9f6cad1f470926fd849b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[UptimeAlertNotifications]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[UptimeAlertNotifications]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[UptimeAlertNotifications]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a37e24770649926982269f8346b33abf7c4ebf1f15a78ab5c348148f4872314f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class UptimeAlertNotificationsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.uptimeAlert.UptimeAlertNotificationsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__16c50585778ca608a882a804e8818f2b32b391bf597065de0ee41994f7527678)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putSlack")
    def put_slack(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["UptimeAlertNotificationsSlack", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__312a1db2b01a70d7951bbc5e2847146fe90a165895b7a3a6480bb31ed67c68be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSlack", [value]))

    @jsii.member(jsii_name="resetEmail")
    def reset_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmail", []))

    @jsii.member(jsii_name="resetSlack")
    def reset_slack(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSlack", []))

    @builtins.property
    @jsii.member(jsii_name="slack")
    def slack(self) -> "UptimeAlertNotificationsSlackList":
        return typing.cast("UptimeAlertNotificationsSlackList", jsii.get(self, "slack"))

    @builtins.property
    @jsii.member(jsii_name="emailInput")
    def email_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "emailInput"))

    @builtins.property
    @jsii.member(jsii_name="slackInput")
    def slack_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["UptimeAlertNotificationsSlack"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["UptimeAlertNotificationsSlack"]]], jsii.get(self, "slackInput"))

    @builtins.property
    @jsii.member(jsii_name="email")
    def email(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "email"))

    @email.setter
    def email(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3ca581abc8e90b625f680381e058cf006c2dfd5953d5c87742bc47aaa876907)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "email", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, UptimeAlertNotifications]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, UptimeAlertNotifications]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, UptimeAlertNotifications]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef2639bed254d658cb3c9b3b8e770ef325b0c4a82063ef296a799541c46a2eeb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="digitalocean.uptimeAlert.UptimeAlertNotificationsSlack",
    jsii_struct_bases=[],
    name_mapping={"channel": "channel", "url": "url"},
)
class UptimeAlertNotificationsSlack:
    def __init__(self, *, channel: builtins.str, url: builtins.str) -> None:
        '''
        :param channel: The Slack channel to send alerts to. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.29.0/docs/resources/uptime_alert#channel UptimeAlert#channel}
        :param url: The webhook URL for Slack. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.29.0/docs/resources/uptime_alert#url UptimeAlert#url}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4bac7f3ac5543428eef0068642b6657996a9e8de1331541f3cffde1c7ae8f62b)
            check_type(argname="argument channel", value=channel, expected_type=type_hints["channel"])
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "channel": channel,
            "url": url,
        }

    @builtins.property
    def channel(self) -> builtins.str:
        '''The Slack channel to send alerts to.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.29.0/docs/resources/uptime_alert#channel UptimeAlert#channel}
        '''
        result = self._values.get("channel")
        assert result is not None, "Required property 'channel' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def url(self) -> builtins.str:
        '''The webhook URL for Slack.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.29.0/docs/resources/uptime_alert#url UptimeAlert#url}
        '''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UptimeAlertNotificationsSlack(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class UptimeAlertNotificationsSlackList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.uptimeAlert.UptimeAlertNotificationsSlackList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fb78e6f762fa300f3878ae4c95c0d27d8355ebee1e8acae7685f903d4df55a98)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "UptimeAlertNotificationsSlackOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86fef9bb0694f34f179bf4bfe3e6c1b72335b7e35c525b9110e16c266cd244e6)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("UptimeAlertNotificationsSlackOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__187d6559d39b3cdd6d72a3a296be930ef30f79bc3b3b54acb391036c18ed6343)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f41ae757bc220a5b6f6659fa954fd0f32beeba7a1447051746078300976130bf)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5dea4b5470be5d12712208ab8a89e9585c74c82f3fc0d33e92cc872a91663a3b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[UptimeAlertNotificationsSlack]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[UptimeAlertNotificationsSlack]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[UptimeAlertNotificationsSlack]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e65af19d04f8a5f76820ab976d4fcf1e4bed3810810ef85f74c817a0fc5de14)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class UptimeAlertNotificationsSlackOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.uptimeAlert.UptimeAlertNotificationsSlackOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f1fbf54103b6c8b58e59028c12a6f1842dbd813a9a73fd5ce8da72b2a23a7fac)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="channelInput")
    def channel_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "channelInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="channel")
    def channel(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "channel"))

    @channel.setter
    def channel(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0dc83acbf31701eb7447d0f6788e5be9832dec5a963b5ac4d5437789eb150af1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "channel", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7569fb4b37ae548b101d4449b05737864753d7986ae1feb866b33e05b8c55970)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, UptimeAlertNotificationsSlack]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, UptimeAlertNotificationsSlack]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, UptimeAlertNotificationsSlack]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4393354d0d6fab5dce10cdd81ac4c7a94823f3d3a22478204f7b8ba22ca49795)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "UptimeAlert",
    "UptimeAlertConfig",
    "UptimeAlertNotifications",
    "UptimeAlertNotificationsList",
    "UptimeAlertNotificationsOutputReference",
    "UptimeAlertNotificationsSlack",
    "UptimeAlertNotificationsSlackList",
    "UptimeAlertNotificationsSlackOutputReference",
]

publication.publish()

def _typecheckingstub__bdbafca4cdd070aa8cb65d8c185255af22f0754c063b5178f1b90feeb581523f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    check_id: builtins.str,
    name: builtins.str,
    notifications: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[UptimeAlertNotifications, typing.Dict[builtins.str, typing.Any]]]],
    type: builtins.str,
    comparison: typing.Optional[builtins.str] = None,
    period: typing.Optional[builtins.str] = None,
    threshold: typing.Optional[jsii.Number] = None,
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

def _typecheckingstub__5d4eb37689e35432ed615dd37699a4e3461d7fa29617d7f4787fc54bab027002(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[UptimeAlertNotifications, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43575005823e3fc632c83182081a05b943bb3657858b4f0ed527db14e35429d6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f9d1c5decdbf2afd55b01e6da607f972cf988a09ea6835ad2f00115691f498d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea7f216c08dbac632739a3b1868a10e65fb0bf5abb2ad9e55e0855a17c9d3c7f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc59c7e58dac332f11000e39bfb98c256d99543b38992c5162b9abd640f8b45b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f44321be343b8ff6ca23b9369cca78145355aa9c320d7c9379f5203c947c791(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3eab012d2ba1012f3005dc65596efbb1ad2abbb4f566f31ab3f9c9f3d45bb105(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1785329ca2fa080ba550210e67198aba8807aa6b27188cf18bd76ce63b2af978(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    check_id: builtins.str,
    name: builtins.str,
    notifications: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[UptimeAlertNotifications, typing.Dict[builtins.str, typing.Any]]]],
    type: builtins.str,
    comparison: typing.Optional[builtins.str] = None,
    period: typing.Optional[builtins.str] = None,
    threshold: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9eab64033296ac1d162c65dffb40dfd154f1150ed2899e64804a2c1208167abc(
    *,
    email: typing.Optional[typing.Sequence[builtins.str]] = None,
    slack: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[UptimeAlertNotificationsSlack, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffbab489b4c1b31968894059d5eec7ed4d17b34633f82090e0f80ecdf6983bc8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d175bd0db78f9e0f35bfbb1da8a7d3d4f285ee7012ed7423958381518ebf79c(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54b4bcbb49ea3da9bc936f002733e0f517f6bd7e78a558c68067bc6c9bca94fa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64d83b87b70334d45be4c6d8f80a4323b2c98852a6f0af95387539c6faa0bf72(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__743e120a3bfb09aabbd94cc98b3db8c6bf0b5d1c31c9f6cad1f470926fd849b4(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a37e24770649926982269f8346b33abf7c4ebf1f15a78ab5c348148f4872314f(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[UptimeAlertNotifications]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16c50585778ca608a882a804e8818f2b32b391bf597065de0ee41994f7527678(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__312a1db2b01a70d7951bbc5e2847146fe90a165895b7a3a6480bb31ed67c68be(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[UptimeAlertNotificationsSlack, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3ca581abc8e90b625f680381e058cf006c2dfd5953d5c87742bc47aaa876907(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef2639bed254d658cb3c9b3b8e770ef325b0c4a82063ef296a799541c46a2eeb(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, UptimeAlertNotifications]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bac7f3ac5543428eef0068642b6657996a9e8de1331541f3cffde1c7ae8f62b(
    *,
    channel: builtins.str,
    url: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb78e6f762fa300f3878ae4c95c0d27d8355ebee1e8acae7685f903d4df55a98(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86fef9bb0694f34f179bf4bfe3e6c1b72335b7e35c525b9110e16c266cd244e6(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__187d6559d39b3cdd6d72a3a296be930ef30f79bc3b3b54acb391036c18ed6343(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f41ae757bc220a5b6f6659fa954fd0f32beeba7a1447051746078300976130bf(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5dea4b5470be5d12712208ab8a89e9585c74c82f3fc0d33e92cc872a91663a3b(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e65af19d04f8a5f76820ab976d4fcf1e4bed3810810ef85f74c817a0fc5de14(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[UptimeAlertNotificationsSlack]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1fbf54103b6c8b58e59028c12a6f1842dbd813a9a73fd5ce8da72b2a23a7fac(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0dc83acbf31701eb7447d0f6788e5be9832dec5a963b5ac4d5437789eb150af1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7569fb4b37ae548b101d4449b05737864753d7986ae1feb866b33e05b8c55970(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4393354d0d6fab5dce10cdd81ac4c7a94823f3d3a22478204f7b8ba22ca49795(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, UptimeAlertNotificationsSlack]],
) -> None:
    """Type checking stubs"""
    pass
