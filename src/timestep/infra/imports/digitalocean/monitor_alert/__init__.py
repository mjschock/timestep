'''
# `digitalocean_monitor_alert`

Refer to the Terraform Registory for docs: [`digitalocean_monitor_alert`](https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/monitor_alert).
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


class MonitorAlert(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.monitorAlert.MonitorAlert",
):
    '''Represents a {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/monitor_alert digitalocean_monitor_alert}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        alerts: typing.Union["MonitorAlertAlerts", typing.Dict[builtins.str, typing.Any]],
        compare: builtins.str,
        description: builtins.str,
        type: builtins.str,
        value: jsii.Number,
        window: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        entities: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/monitor_alert digitalocean_monitor_alert} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param alerts: alerts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/monitor_alert#alerts MonitorAlert#alerts}
        :param compare: The comparison operator to use for value. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/monitor_alert#compare MonitorAlert#compare}
        :param description: Description of the alert policy. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/monitor_alert#description MonitorAlert#description}
        :param type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/monitor_alert#type MonitorAlert#type}.
        :param value: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/monitor_alert#value MonitorAlert#value}.
        :param window: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/monitor_alert#window MonitorAlert#window}.
        :param enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/monitor_alert#enabled MonitorAlert#enabled}.
        :param entities: The droplets to apply the alert policy to. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/monitor_alert#entities MonitorAlert#entities}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/monitor_alert#id MonitorAlert#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/monitor_alert#tags MonitorAlert#tags}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5128fa0109224accb0dd03354d8425045653660b86aabdeeb24c8ea5c20a01e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = MonitorAlertConfig(
            alerts=alerts,
            compare=compare,
            description=description,
            type=type,
            value=value,
            window=window,
            enabled=enabled,
            entities=entities,
            id=id,
            tags=tags,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAlerts")
    def put_alerts(
        self,
        *,
        email: typing.Optional[typing.Sequence[builtins.str]] = None,
        slack: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["MonitorAlertAlertsSlack", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param email: List of email addresses to sent notifications to. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/monitor_alert#email MonitorAlert#email}
        :param slack: slack block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/monitor_alert#slack MonitorAlert#slack}
        '''
        value = MonitorAlertAlerts(email=email, slack=slack)

        return typing.cast(None, jsii.invoke(self, "putAlerts", [value]))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetEntities")
    def reset_entities(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEntities", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="alerts")
    def alerts(self) -> "MonitorAlertAlertsOutputReference":
        return typing.cast("MonitorAlertAlertsOutputReference", jsii.get(self, "alerts"))

    @builtins.property
    @jsii.member(jsii_name="uuid")
    def uuid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uuid"))

    @builtins.property
    @jsii.member(jsii_name="alertsInput")
    def alerts_input(self) -> typing.Optional["MonitorAlertAlerts"]:
        return typing.cast(typing.Optional["MonitorAlertAlerts"], jsii.get(self, "alertsInput"))

    @builtins.property
    @jsii.member(jsii_name="compareInput")
    def compare_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "compareInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="entitiesInput")
    def entities_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "entitiesInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="windowInput")
    def window_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "windowInput"))

    @builtins.property
    @jsii.member(jsii_name="compare")
    def compare(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "compare"))

    @compare.setter
    def compare(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fad2ad6334f5a083354cd04b306d412a12c3c1d3cb790bbc9f31a51f8f691dd8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "compare", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f69ee9cedf878b9b2cbd8f81f2624b90e7c99fb81ca009aa08981945550f0e4f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c7f6c68999d5836b46d157b5a6990dd4d8180810a9f678f6443931d657f0a91)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="entities")
    def entities(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "entities"))

    @entities.setter
    def entities(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce6f7a4717fbf162c4bc1bca9801020658d64e41ac2d046d16140dbb32a4768b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "entities", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d5cb0f72d4c5d726273cbd8cc7cae1d8637aafadcd806583fadab9665ce4728)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__726da1accc79b2947448c9f2357c951563c22e2720cb5731f0da3b0436f87e2f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03b0bf52329216a6f3afb6d876cabd89c4e9f43c40eabb253af8ff0d56e2def7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1e4bd1b1c5fd5b309c2a815e5213836ee8ecc112448b5391ddf71e736253fdf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="window")
    def window(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "window"))

    @window.setter
    def window(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d18eff6bc860772fc8b9c13ecd59b9bd1c0f8f278104b383fc05919c722a1726)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "window", value)


@jsii.data_type(
    jsii_type="digitalocean.monitorAlert.MonitorAlertAlerts",
    jsii_struct_bases=[],
    name_mapping={"email": "email", "slack": "slack"},
)
class MonitorAlertAlerts:
    def __init__(
        self,
        *,
        email: typing.Optional[typing.Sequence[builtins.str]] = None,
        slack: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["MonitorAlertAlertsSlack", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param email: List of email addresses to sent notifications to. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/monitor_alert#email MonitorAlert#email}
        :param slack: slack block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/monitor_alert#slack MonitorAlert#slack}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fbee4225f525a9b48b4dfcd4839eeb836e249706395ce661bbe2a39f96f3c2a3)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/monitor_alert#email MonitorAlert#email}
        '''
        result = self._values.get("email")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def slack(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["MonitorAlertAlertsSlack"]]]:
        '''slack block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/monitor_alert#slack MonitorAlert#slack}
        '''
        result = self._values.get("slack")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["MonitorAlertAlertsSlack"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorAlertAlerts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorAlertAlertsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.monitorAlert.MonitorAlertAlertsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b77e8c02fe873ada7e31eafde445eaf96d6a9585180743673ed9b19c32b0c66b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSlack")
    def put_slack(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["MonitorAlertAlertsSlack", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1421dc962c243f4060d87ff333dff09887bc9b1fcb0b45a18cdca2cb11cb05e1)
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
    def slack(self) -> "MonitorAlertAlertsSlackList":
        return typing.cast("MonitorAlertAlertsSlackList", jsii.get(self, "slack"))

    @builtins.property
    @jsii.member(jsii_name="emailInput")
    def email_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "emailInput"))

    @builtins.property
    @jsii.member(jsii_name="slackInput")
    def slack_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["MonitorAlertAlertsSlack"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["MonitorAlertAlertsSlack"]]], jsii.get(self, "slackInput"))

    @builtins.property
    @jsii.member(jsii_name="email")
    def email(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "email"))

    @email.setter
    def email(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9201d9ddbcae89a7f8443a75a9489c53b8fe1c4222edf6d97246ed7a3232029d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "email", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MonitorAlertAlerts]:
        return typing.cast(typing.Optional[MonitorAlertAlerts], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[MonitorAlertAlerts]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a702abd5a7f85a971dd35515ce6c4c83fb152eff4270aeec87c10fb949e1520b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="digitalocean.monitorAlert.MonitorAlertAlertsSlack",
    jsii_struct_bases=[],
    name_mapping={"channel": "channel", "url": "url"},
)
class MonitorAlertAlertsSlack:
    def __init__(self, *, channel: builtins.str, url: builtins.str) -> None:
        '''
        :param channel: The Slack channel to send alerts to. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/monitor_alert#channel MonitorAlert#channel}
        :param url: The webhook URL for Slack. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/monitor_alert#url MonitorAlert#url}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0333c5916ca7ba2c3bc06cb1994759feede39d889d5a1baf7f3e3b5490fcb5f5)
            check_type(argname="argument channel", value=channel, expected_type=type_hints["channel"])
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "channel": channel,
            "url": url,
        }

    @builtins.property
    def channel(self) -> builtins.str:
        '''The Slack channel to send alerts to.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/monitor_alert#channel MonitorAlert#channel}
        '''
        result = self._values.get("channel")
        assert result is not None, "Required property 'channel' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def url(self) -> builtins.str:
        '''The webhook URL for Slack.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/monitor_alert#url MonitorAlert#url}
        '''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorAlertAlertsSlack(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorAlertAlertsSlackList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.monitorAlert.MonitorAlertAlertsSlackList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f6eab5488bf3f7f7e363b6541a549d91943b13820964261af7dafe5460f95753)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "MonitorAlertAlertsSlackOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b75d3479ff2d011cae7d72e1f9d0499a4dc9f0d52921c7f8ce5e8e665df0b93)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MonitorAlertAlertsSlackOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b55eae0139ef47dbcc51beae4b2ec87bec424107a2ca54aa3a1fabe23e4a1f4d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__abc9356d37892674f7884d70227be1644d99dd7dcfff3984816bf6fcfba34a4b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a576d3c602436a5b68e9512e8b498478a7da9e845b58b12e7a54c13263a1de2d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MonitorAlertAlertsSlack]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MonitorAlertAlertsSlack]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MonitorAlertAlertsSlack]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52764c52e2fef54b4e529a52a5eafe237587bfda8d589d4c274f3f00a516cf07)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MonitorAlertAlertsSlackOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.monitorAlert.MonitorAlertAlertsSlackOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__86cbd24004a9109a8a63b14d13c532b2b24d34a826cfd0ffde75b02812a2977e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e9a72b2844672d0bafebeebb0c05d9c95659f4324e15cecbe6ecc3ff1b771516)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "channel", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e2a68d241192aed61e8030e661397fcab2e89f5d546290a06e15d0507e402b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, MonitorAlertAlertsSlack]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, MonitorAlertAlertsSlack]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, MonitorAlertAlertsSlack]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d07c53564141a2e1f81e5b8b1870c1b6a27ebf171dfdc050704b473c0e95e89)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="digitalocean.monitorAlert.MonitorAlertConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "alerts": "alerts",
        "compare": "compare",
        "description": "description",
        "type": "type",
        "value": "value",
        "window": "window",
        "enabled": "enabled",
        "entities": "entities",
        "id": "id",
        "tags": "tags",
    },
)
class MonitorAlertConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        alerts: typing.Union[MonitorAlertAlerts, typing.Dict[builtins.str, typing.Any]],
        compare: builtins.str,
        description: builtins.str,
        type: builtins.str,
        value: jsii.Number,
        window: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        entities: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param alerts: alerts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/monitor_alert#alerts MonitorAlert#alerts}
        :param compare: The comparison operator to use for value. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/monitor_alert#compare MonitorAlert#compare}
        :param description: Description of the alert policy. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/monitor_alert#description MonitorAlert#description}
        :param type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/monitor_alert#type MonitorAlert#type}.
        :param value: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/monitor_alert#value MonitorAlert#value}.
        :param window: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/monitor_alert#window MonitorAlert#window}.
        :param enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/monitor_alert#enabled MonitorAlert#enabled}.
        :param entities: The droplets to apply the alert policy to. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/monitor_alert#entities MonitorAlert#entities}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/monitor_alert#id MonitorAlert#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/monitor_alert#tags MonitorAlert#tags}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(alerts, dict):
            alerts = MonitorAlertAlerts(**alerts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc58e8dcfcaa299dc5b276f5bfe648fce266838854772cb0e14f34e8e3aad16f)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument alerts", value=alerts, expected_type=type_hints["alerts"])
            check_type(argname="argument compare", value=compare, expected_type=type_hints["compare"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument window", value=window, expected_type=type_hints["window"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument entities", value=entities, expected_type=type_hints["entities"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "alerts": alerts,
            "compare": compare,
            "description": description,
            "type": type,
            "value": value,
            "window": window,
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
        if enabled is not None:
            self._values["enabled"] = enabled
        if entities is not None:
            self._values["entities"] = entities
        if id is not None:
            self._values["id"] = id
        if tags is not None:
            self._values["tags"] = tags

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
    def alerts(self) -> MonitorAlertAlerts:
        '''alerts block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/monitor_alert#alerts MonitorAlert#alerts}
        '''
        result = self._values.get("alerts")
        assert result is not None, "Required property 'alerts' is missing"
        return typing.cast(MonitorAlertAlerts, result)

    @builtins.property
    def compare(self) -> builtins.str:
        '''The comparison operator to use for value.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/monitor_alert#compare MonitorAlert#compare}
        '''
        result = self._values.get("compare")
        assert result is not None, "Required property 'compare' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> builtins.str:
        '''Description of the alert policy.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/monitor_alert#description MonitorAlert#description}
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/monitor_alert#type MonitorAlert#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/monitor_alert#value MonitorAlert#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def window(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/monitor_alert#window MonitorAlert#window}.'''
        result = self._values.get("window")
        assert result is not None, "Required property 'window' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/monitor_alert#enabled MonitorAlert#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def entities(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The droplets to apply the alert policy to.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/monitor_alert#entities MonitorAlert#entities}
        '''
        result = self._values.get("entities")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/monitor_alert#id MonitorAlert#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/monitor_alert#tags MonitorAlert#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorAlertConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "MonitorAlert",
    "MonitorAlertAlerts",
    "MonitorAlertAlertsOutputReference",
    "MonitorAlertAlertsSlack",
    "MonitorAlertAlertsSlackList",
    "MonitorAlertAlertsSlackOutputReference",
    "MonitorAlertConfig",
]

publication.publish()

def _typecheckingstub__a5128fa0109224accb0dd03354d8425045653660b86aabdeeb24c8ea5c20a01e(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    alerts: typing.Union[MonitorAlertAlerts, typing.Dict[builtins.str, typing.Any]],
    compare: builtins.str,
    description: builtins.str,
    type: builtins.str,
    value: jsii.Number,
    window: builtins.str,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    entities: typing.Optional[typing.Sequence[builtins.str]] = None,
    id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[builtins.str]] = None,
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

def _typecheckingstub__fad2ad6334f5a083354cd04b306d412a12c3c1d3cb790bbc9f31a51f8f691dd8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f69ee9cedf878b9b2cbd8f81f2624b90e7c99fb81ca009aa08981945550f0e4f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c7f6c68999d5836b46d157b5a6990dd4d8180810a9f678f6443931d657f0a91(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce6f7a4717fbf162c4bc1bca9801020658d64e41ac2d046d16140dbb32a4768b(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d5cb0f72d4c5d726273cbd8cc7cae1d8637aafadcd806583fadab9665ce4728(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__726da1accc79b2947448c9f2357c951563c22e2720cb5731f0da3b0436f87e2f(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03b0bf52329216a6f3afb6d876cabd89c4e9f43c40eabb253af8ff0d56e2def7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1e4bd1b1c5fd5b309c2a815e5213836ee8ecc112448b5391ddf71e736253fdf(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d18eff6bc860772fc8b9c13ecd59b9bd1c0f8f278104b383fc05919c722a1726(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fbee4225f525a9b48b4dfcd4839eeb836e249706395ce661bbe2a39f96f3c2a3(
    *,
    email: typing.Optional[typing.Sequence[builtins.str]] = None,
    slack: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[MonitorAlertAlertsSlack, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b77e8c02fe873ada7e31eafde445eaf96d6a9585180743673ed9b19c32b0c66b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1421dc962c243f4060d87ff333dff09887bc9b1fcb0b45a18cdca2cb11cb05e1(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[MonitorAlertAlertsSlack, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9201d9ddbcae89a7f8443a75a9489c53b8fe1c4222edf6d97246ed7a3232029d(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a702abd5a7f85a971dd35515ce6c4c83fb152eff4270aeec87c10fb949e1520b(
    value: typing.Optional[MonitorAlertAlerts],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0333c5916ca7ba2c3bc06cb1994759feede39d889d5a1baf7f3e3b5490fcb5f5(
    *,
    channel: builtins.str,
    url: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6eab5488bf3f7f7e363b6541a549d91943b13820964261af7dafe5460f95753(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b75d3479ff2d011cae7d72e1f9d0499a4dc9f0d52921c7f8ce5e8e665df0b93(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b55eae0139ef47dbcc51beae4b2ec87bec424107a2ca54aa3a1fabe23e4a1f4d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abc9356d37892674f7884d70227be1644d99dd7dcfff3984816bf6fcfba34a4b(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a576d3c602436a5b68e9512e8b498478a7da9e845b58b12e7a54c13263a1de2d(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52764c52e2fef54b4e529a52a5eafe237587bfda8d589d4c274f3f00a516cf07(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MonitorAlertAlertsSlack]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86cbd24004a9109a8a63b14d13c532b2b24d34a826cfd0ffde75b02812a2977e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9a72b2844672d0bafebeebb0c05d9c95659f4324e15cecbe6ecc3ff1b771516(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e2a68d241192aed61e8030e661397fcab2e89f5d546290a06e15d0507e402b6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d07c53564141a2e1f81e5b8b1870c1b6a27ebf171dfdc050704b473c0e95e89(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, MonitorAlertAlertsSlack]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc58e8dcfcaa299dc5b276f5bfe648fce266838854772cb0e14f34e8e3aad16f(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    alerts: typing.Union[MonitorAlertAlerts, typing.Dict[builtins.str, typing.Any]],
    compare: builtins.str,
    description: builtins.str,
    type: builtins.str,
    value: jsii.Number,
    window: builtins.str,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    entities: typing.Optional[typing.Sequence[builtins.str]] = None,
    id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
