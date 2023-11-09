'''
# `argocd_account_token`

Refer to the Terraform Registory for docs: [`argocd_account_token`](https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/account_token).
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


class AccountToken(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.accountToken.AccountToken",
):
    '''Represents a {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/account_token argocd_account_token}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        account: typing.Optional[builtins.str] = None,
        expires_in: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        renew_after: typing.Optional[builtins.str] = None,
        renew_before: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/account_token argocd_account_token} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param account: Account name. Defaults to the current account. I.e. the account configured on the ``provider`` block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/account_token#account AccountToken#account}
        :param expires_in: Duration before the token will expire. Valid time units are ``ns``, ``us`` (or ``µs``), ``ms``, ``s``, ``m``, ``h``. E.g. ``12h``, ``7d``. Default: No expiration. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/account_token#expires_in AccountToken#expires_in}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/account_token#id AccountToken#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param renew_after: Duration to control token silent regeneration based on token age. Valid time units are ``ns``, ``us`` (or ``µs``), ``ms``, ``s``, ``m``, ``h``. If set, then the token will be regenerated if it is older than ``renew_after``. I.e. if ``currentDate - issued_at > renew_after``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/account_token#renew_after AccountToken#renew_after}
        :param renew_before: Duration to control token silent regeneration based on remaining token lifetime. If ``expires_in`` is set, Terraform will regenerate the token if ``expires_at - currentDate < renew_before``. Valid time units are ``ns``, ``us`` (or ``µs``), ``ms``, ``s``, ``m``, ``h``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/account_token#renew_before AccountToken#renew_before}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed28ac67126c10b379cb4eb5b8af155b16e35b7dc9c3a4905ca85c02c5cdea93)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AccountTokenConfig(
            account=account,
            expires_in=expires_in,
            id=id,
            renew_after=renew_after,
            renew_before=renew_before,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetAccount")
    def reset_account(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccount", []))

    @jsii.member(jsii_name="resetExpiresIn")
    def reset_expires_in(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpiresIn", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetRenewAfter")
    def reset_renew_after(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRenewAfter", []))

    @jsii.member(jsii_name="resetRenewBefore")
    def reset_renew_before(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRenewBefore", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="expiresAt")
    def expires_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expiresAt"))

    @builtins.property
    @jsii.member(jsii_name="issuedAt")
    def issued_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "issuedAt"))

    @builtins.property
    @jsii.member(jsii_name="jwt")
    def jwt(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "jwt"))

    @builtins.property
    @jsii.member(jsii_name="accountInput")
    def account_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountInput"))

    @builtins.property
    @jsii.member(jsii_name="expiresInInput")
    def expires_in_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expiresInInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="renewAfterInput")
    def renew_after_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "renewAfterInput"))

    @builtins.property
    @jsii.member(jsii_name="renewBeforeInput")
    def renew_before_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "renewBeforeInput"))

    @builtins.property
    @jsii.member(jsii_name="account")
    def account(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "account"))

    @account.setter
    def account(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__debe36cd37d50b406b5d3a021d447b385c1f0dcdf293b380962de5e834650c91)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "account", value)

    @builtins.property
    @jsii.member(jsii_name="expiresIn")
    def expires_in(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expiresIn"))

    @expires_in.setter
    def expires_in(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e389836e06ad3f183f49b198fb612299110848ea43661dace1757e2c9166add9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expiresIn", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__630f4fdeaea014568ba21732079e003e3e0cc40027327d084fc8c88ae76a6a29)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="renewAfter")
    def renew_after(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "renewAfter"))

    @renew_after.setter
    def renew_after(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8427cb12fc999d76ccc8db2ca2c6327693aeefce170926575ba8b8a261388754)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "renewAfter", value)

    @builtins.property
    @jsii.member(jsii_name="renewBefore")
    def renew_before(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "renewBefore"))

    @renew_before.setter
    def renew_before(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8c50c1aa8057d889433134f9ec30356df3e650aeb0ee41c329f884d96087c56)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "renewBefore", value)


@jsii.data_type(
    jsii_type="argocd.accountToken.AccountTokenConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "account": "account",
        "expires_in": "expiresIn",
        "id": "id",
        "renew_after": "renewAfter",
        "renew_before": "renewBefore",
    },
)
class AccountTokenConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        account: typing.Optional[builtins.str] = None,
        expires_in: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        renew_after: typing.Optional[builtins.str] = None,
        renew_before: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param account: Account name. Defaults to the current account. I.e. the account configured on the ``provider`` block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/account_token#account AccountToken#account}
        :param expires_in: Duration before the token will expire. Valid time units are ``ns``, ``us`` (or ``µs``), ``ms``, ``s``, ``m``, ``h``. E.g. ``12h``, ``7d``. Default: No expiration. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/account_token#expires_in AccountToken#expires_in}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/account_token#id AccountToken#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param renew_after: Duration to control token silent regeneration based on token age. Valid time units are ``ns``, ``us`` (or ``µs``), ``ms``, ``s``, ``m``, ``h``. If set, then the token will be regenerated if it is older than ``renew_after``. I.e. if ``currentDate - issued_at > renew_after``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/account_token#renew_after AccountToken#renew_after}
        :param renew_before: Duration to control token silent regeneration based on remaining token lifetime. If ``expires_in`` is set, Terraform will regenerate the token if ``expires_at - currentDate < renew_before``. Valid time units are ``ns``, ``us`` (or ``µs``), ``ms``, ``s``, ``m``, ``h``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/account_token#renew_before AccountToken#renew_before}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb22a0c72045277308d4bc17712668457338ef0806bbdc44ca11ac7e747e5e13)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument account", value=account, expected_type=type_hints["account"])
            check_type(argname="argument expires_in", value=expires_in, expected_type=type_hints["expires_in"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument renew_after", value=renew_after, expected_type=type_hints["renew_after"])
            check_type(argname="argument renew_before", value=renew_before, expected_type=type_hints["renew_before"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
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
        if account is not None:
            self._values["account"] = account
        if expires_in is not None:
            self._values["expires_in"] = expires_in
        if id is not None:
            self._values["id"] = id
        if renew_after is not None:
            self._values["renew_after"] = renew_after
        if renew_before is not None:
            self._values["renew_before"] = renew_before

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
    def account(self) -> typing.Optional[builtins.str]:
        '''Account name. Defaults to the current account. I.e. the account configured on the ``provider`` block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/account_token#account AccountToken#account}
        '''
        result = self._values.get("account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def expires_in(self) -> typing.Optional[builtins.str]:
        '''Duration before the token will expire.

        Valid time units are ``ns``, ``us`` (or ``µs``), ``ms``, ``s``, ``m``, ``h``. E.g. ``12h``, ``7d``. Default: No expiration.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/account_token#expires_in AccountToken#expires_in}
        '''
        result = self._values.get("expires_in")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/account_token#id AccountToken#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def renew_after(self) -> typing.Optional[builtins.str]:
        '''Duration to control token silent regeneration based on token age.

        Valid time units are ``ns``, ``us`` (or ``µs``), ``ms``, ``s``, ``m``, ``h``. If set, then the token will be regenerated if it is older than ``renew_after``. I.e. if ``currentDate - issued_at > renew_after``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/account_token#renew_after AccountToken#renew_after}
        '''
        result = self._values.get("renew_after")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def renew_before(self) -> typing.Optional[builtins.str]:
        '''Duration to control token silent regeneration based on remaining token lifetime.

        If ``expires_in`` is set, Terraform will regenerate the token if ``expires_at - currentDate < renew_before``. Valid time units are ``ns``, ``us`` (or ``µs``), ``ms``, ``s``, ``m``, ``h``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs/resources/account_token#renew_before AccountToken#renew_before}
        '''
        result = self._values.get("renew_before")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccountTokenConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AccountToken",
    "AccountTokenConfig",
]

publication.publish()

def _typecheckingstub__ed28ac67126c10b379cb4eb5b8af155b16e35b7dc9c3a4905ca85c02c5cdea93(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    account: typing.Optional[builtins.str] = None,
    expires_in: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    renew_after: typing.Optional[builtins.str] = None,
    renew_before: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__debe36cd37d50b406b5d3a021d447b385c1f0dcdf293b380962de5e834650c91(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e389836e06ad3f183f49b198fb612299110848ea43661dace1757e2c9166add9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__630f4fdeaea014568ba21732079e003e3e0cc40027327d084fc8c88ae76a6a29(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8427cb12fc999d76ccc8db2ca2c6327693aeefce170926575ba8b8a261388754(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8c50c1aa8057d889433134f9ec30356df3e650aeb0ee41c329f884d96087c56(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb22a0c72045277308d4bc17712668457338ef0806bbdc44ca11ac7e747e5e13(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    account: typing.Optional[builtins.str] = None,
    expires_in: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    renew_after: typing.Optional[builtins.str] = None,
    renew_before: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
