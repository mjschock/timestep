"""
# `digitalocean_database_connection_pool`

Refer to the Terraform Registory for docs: [`digitalocean_database_connection_pool`](https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/database_connection_pool).
"""
import abc
import builtins
import datetime
import enum
import typing

import cdktf as _cdktf_9a9027ec
import constructs as _constructs_77d1e7e8
import jsii
import publication
import typing_extensions
from typeguard import check_type

from .._jsii import *


class DatabaseConnectionPool(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.databaseConnectionPool.DatabaseConnectionPool",
):
    """Represents a {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/database_connection_pool digitalocean_database_connection_pool}."""

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        cluster_id: builtins.str,
        db_name: builtins.str,
        mode: builtins.str,
        name: builtins.str,
        size: jsii.Number,
        id: typing.Optional[builtins.str] = None,
        user: typing.Optional[builtins.str] = None,
        connection: typing.Optional[
            typing.Union[
                typing.Union[
                    _cdktf_9a9027ec.SSHProvisionerConnection,
                    typing.Dict[builtins.str, typing.Any],
                ],
                typing.Union[
                    _cdktf_9a9027ec.WinrmProvisionerConnection,
                    typing.Dict[builtins.str, typing.Any],
                ],
            ]
        ] = None,
        count: typing.Optional[
            typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]
        ] = None,
        depends_on: typing.Optional[
            typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]
        ] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[
            typing.Union[
                _cdktf_9a9027ec.TerraformResourceLifecycle,
                typing.Dict[builtins.str, typing.Any],
            ]
        ] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[
            typing.Sequence[
                typing.Union[
                    typing.Union[
                        _cdktf_9a9027ec.FileProvisioner,
                        typing.Dict[builtins.str, typing.Any],
                    ],
                    typing.Union[
                        _cdktf_9a9027ec.LocalExecProvisioner,
                        typing.Dict[builtins.str, typing.Any],
                    ],
                    typing.Union[
                        _cdktf_9a9027ec.RemoteExecProvisioner,
                        typing.Dict[builtins.str, typing.Any],
                    ],
                ]
            ]
        ] = None,
    ) -> None:
        """Create a new {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/database_connection_pool digitalocean_database_connection_pool} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param cluster_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/database_connection_pool#cluster_id DatabaseConnectionPool#cluster_id}.
        :param db_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/database_connection_pool#db_name DatabaseConnectionPool#db_name}.
        :param mode: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/database_connection_pool#mode DatabaseConnectionPool#mode}.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/database_connection_pool#name DatabaseConnectionPool#name}.
        :param size: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/database_connection_pool#size DatabaseConnectionPool#size}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/database_connection_pool#id DatabaseConnectionPool#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param user: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/database_connection_pool#user DatabaseConnectionPool#user}.
        :param connection:
        :param count:
        :param depends_on:
        :param for_each:
        :param lifecycle:
        :param provider:
        :param provisioners:
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__b71fc51e9887e5a7862152c89945c8ca8420cc08862500d7e2f2a5446ae2fff3
            )
            check_type(
                argname="argument scope", value=scope, expected_type=type_hints["scope"]
            )
            check_type(
                argname="argument id_", value=id_, expected_type=type_hints["id_"]
            )
        config = DatabaseConnectionPoolConfig(
            cluster_id=cluster_id,
            db_name=db_name,
            mode=mode,
            name=name,
            size=size,
            id=id,
            user=user,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetUser")
    def reset_user(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUser", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(
            typing.Mapping[builtins.str, typing.Any],
            jsii.invoke(self, "synthesizeAttributes", []),
        )

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "host"))

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @builtins.property
    @jsii.member(jsii_name="privateHost")
    def private_host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateHost"))

    @builtins.property
    @jsii.member(jsii_name="privateUri")
    def private_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateUri"))

    @builtins.property
    @jsii.member(jsii_name="uri")
    def uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uri"))

    @builtins.property
    @jsii.member(jsii_name="clusterIdInput")
    def cluster_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "clusterIdInput")
        )

    @builtins.property
    @jsii.member(jsii_name="dbNameInput")
    def db_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dbNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="modeInput")
    def mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modeInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="sizeInput")
    def size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sizeInput"))

    @builtins.property
    @jsii.member(jsii_name="userInput")
    def user_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterId")
    def cluster_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterId"))

    @cluster_id.setter
    def cluster_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__7e9db62f313744edd1bdec2e874071f8854fa47f29a3b13394e8887ac575d884
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "clusterId", value)

    @builtins.property
    @jsii.member(jsii_name="dbName")
    def db_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dbName"))

    @db_name.setter
    def db_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__b7bfd0816a5477c98be738d6086705fbd07dfd16d29ad04630e64840344b04a8
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "dbName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__cb9857d3425e1701cc9227611b28e38bdfd3a201aeaf925719ec93380b4a9bdd
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mode"))

    @mode.setter
    def mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__2ebf0ce27ccb3a33e211dbbc2a8c19f9108848e58fd6a2f09f3dd21fb90f2ef0
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__c23481c1865c4698f5d3afa69aaac8c458f23f24a08a39a8d36a091d385a2711
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="size")
    def size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "size"))

    @size.setter
    def size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__05bad28fb496e4f3bf36366af49f9fc339fb09d2caf19bf0fb85f8aba06b9c3f
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "size", value)

    @builtins.property
    @jsii.member(jsii_name="user")
    def user(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "user"))

    @user.setter
    def user(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__6464a1fd4a7f75e75238c731c183f48ef78df358226632114a247ba984152758
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "user", value)


@jsii.data_type(
    jsii_type="digitalocean.databaseConnectionPool.DatabaseConnectionPoolConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "cluster_id": "clusterId",
        "db_name": "dbName",
        "mode": "mode",
        "name": "name",
        "size": "size",
        "id": "id",
        "user": "user",
    },
)
class DatabaseConnectionPoolConfig(_cdktf_9a9027ec.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[
            typing.Union[
                typing.Union[
                    _cdktf_9a9027ec.SSHProvisionerConnection,
                    typing.Dict[builtins.str, typing.Any],
                ],
                typing.Union[
                    _cdktf_9a9027ec.WinrmProvisionerConnection,
                    typing.Dict[builtins.str, typing.Any],
                ],
            ]
        ] = None,
        count: typing.Optional[
            typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]
        ] = None,
        depends_on: typing.Optional[
            typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]
        ] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[
            typing.Union[
                _cdktf_9a9027ec.TerraformResourceLifecycle,
                typing.Dict[builtins.str, typing.Any],
            ]
        ] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[
            typing.Sequence[
                typing.Union[
                    typing.Union[
                        _cdktf_9a9027ec.FileProvisioner,
                        typing.Dict[builtins.str, typing.Any],
                    ],
                    typing.Union[
                        _cdktf_9a9027ec.LocalExecProvisioner,
                        typing.Dict[builtins.str, typing.Any],
                    ],
                    typing.Union[
                        _cdktf_9a9027ec.RemoteExecProvisioner,
                        typing.Dict[builtins.str, typing.Any],
                    ],
                ]
            ]
        ] = None,
        cluster_id: builtins.str,
        db_name: builtins.str,
        mode: builtins.str,
        name: builtins.str,
        size: jsii.Number,
        id: typing.Optional[builtins.str] = None,
        user: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param connection:
        :param count:
        :param depends_on:
        :param for_each:
        :param lifecycle:
        :param provider:
        :param provisioners:
        :param cluster_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/database_connection_pool#cluster_id DatabaseConnectionPool#cluster_id}.
        :param db_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/database_connection_pool#db_name DatabaseConnectionPool#db_name}.
        :param mode: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/database_connection_pool#mode DatabaseConnectionPool#mode}.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/database_connection_pool#name DatabaseConnectionPool#name}.
        :param size: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/database_connection_pool#size DatabaseConnectionPool#size}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/database_connection_pool#id DatabaseConnectionPool#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param user: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/database_connection_pool#user DatabaseConnectionPool#user}.
        """
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__19a69e7b71aee7fc6e65c6adc1722347eb173e402a99a966f4f16c235c718d5a
            )
            check_type(
                argname="argument connection",
                value=connection,
                expected_type=type_hints["connection"],
            )
            check_type(
                argname="argument count", value=count, expected_type=type_hints["count"]
            )
            check_type(
                argname="argument depends_on",
                value=depends_on,
                expected_type=type_hints["depends_on"],
            )
            check_type(
                argname="argument for_each",
                value=for_each,
                expected_type=type_hints["for_each"],
            )
            check_type(
                argname="argument lifecycle",
                value=lifecycle,
                expected_type=type_hints["lifecycle"],
            )
            check_type(
                argname="argument provider",
                value=provider,
                expected_type=type_hints["provider"],
            )
            check_type(
                argname="argument provisioners",
                value=provisioners,
                expected_type=type_hints["provisioners"],
            )
            check_type(
                argname="argument cluster_id",
                value=cluster_id,
                expected_type=type_hints["cluster_id"],
            )
            check_type(
                argname="argument db_name",
                value=db_name,
                expected_type=type_hints["db_name"],
            )
            check_type(
                argname="argument mode", value=mode, expected_type=type_hints["mode"]
            )
            check_type(
                argname="argument name", value=name, expected_type=type_hints["name"]
            )
            check_type(
                argname="argument size", value=size, expected_type=type_hints["size"]
            )
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(
                argname="argument user", value=user, expected_type=type_hints["user"]
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster_id": cluster_id,
            "db_name": db_name,
            "mode": mode,
            "name": name,
            "size": size,
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
        if id is not None:
            self._values["id"] = id
        if user is not None:
            self._values["user"] = user

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.SSHProvisionerConnection,
            _cdktf_9a9027ec.WinrmProvisionerConnection,
        ]
    ]:
        """
        :stability: experimental
        """
        result = self._values.get("connection")
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.SSHProvisionerConnection,
                    _cdktf_9a9027ec.WinrmProvisionerConnection,
                ]
            ],
            result,
        )

    @builtins.property
    def count(
        self,
    ) -> typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]]:
        """
        :stability: experimental
        """
        result = self._values.get("count")
        return typing.cast(
            typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]],
            result,
        )

    @builtins.property
    def depends_on(
        self,
    ) -> typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]]:
        """
        :stability: experimental
        """
        result = self._values.get("depends_on")
        return typing.cast(
            typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]], result
        )

    @builtins.property
    def for_each(self) -> typing.Optional[_cdktf_9a9027ec.ITerraformIterator]:
        """
        :stability: experimental
        """
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle]:
        """
        :stability: experimental
        """
        result = self._values.get("lifecycle")
        return typing.cast(
            typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle], result
        )

    @builtins.property
    def provider(self) -> typing.Optional[_cdktf_9a9027ec.TerraformProvider]:
        """
        :stability: experimental
        """
        result = self._values.get("provider")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[
        typing.List[
            typing.Union[
                _cdktf_9a9027ec.FileProvisioner,
                _cdktf_9a9027ec.LocalExecProvisioner,
                _cdktf_9a9027ec.RemoteExecProvisioner,
            ]
        ]
    ]:
        """
        :stability: experimental
        """
        result = self._values.get("provisioners")
        return typing.cast(
            typing.Optional[
                typing.List[
                    typing.Union[
                        _cdktf_9a9027ec.FileProvisioner,
                        _cdktf_9a9027ec.LocalExecProvisioner,
                        _cdktf_9a9027ec.RemoteExecProvisioner,
                    ]
                ]
            ],
            result,
        )

    @builtins.property
    def cluster_id(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/database_connection_pool#cluster_id DatabaseConnectionPool#cluster_id}."""
        result = self._values.get("cluster_id")
        assert result is not None, "Required property 'cluster_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def db_name(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/database_connection_pool#db_name DatabaseConnectionPool#db_name}."""
        result = self._values.get("db_name")
        assert result is not None, "Required property 'db_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mode(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/database_connection_pool#mode DatabaseConnectionPool#mode}."""
        result = self._values.get("mode")
        assert result is not None, "Required property 'mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/database_connection_pool#name DatabaseConnectionPool#name}."""
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def size(self) -> jsii.Number:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/database_connection_pool#size DatabaseConnectionPool#size}."""
        result = self._values.get("size")
        assert result is not None, "Required property 'size' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/database_connection_pool#id DatabaseConnectionPool#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        """
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/database_connection_pool#user DatabaseConnectionPool#user}."""
        result = self._values.get("user")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseConnectionPoolConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DatabaseConnectionPool",
    "DatabaseConnectionPoolConfig",
]

publication.publish()


def _typecheckingstub__b71fc51e9887e5a7862152c89945c8ca8420cc08862500d7e2f2a5446ae2fff3(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    cluster_id: builtins.str,
    db_name: builtins.str,
    mode: builtins.str,
    name: builtins.str,
    size: jsii.Number,
    id: typing.Optional[builtins.str] = None,
    user: typing.Optional[builtins.str] = None,
    connection: typing.Optional[
        typing.Union[
            typing.Union[
                _cdktf_9a9027ec.SSHProvisionerConnection,
                typing.Dict[builtins.str, typing.Any],
            ],
            typing.Union[
                _cdktf_9a9027ec.WinrmProvisionerConnection,
                typing.Dict[builtins.str, typing.Any],
            ],
        ]
    ] = None,
    count: typing.Optional[
        typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]
    ] = None,
    depends_on: typing.Optional[
        typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]
    ] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.TerraformResourceLifecycle,
            typing.Dict[builtins.str, typing.Any],
        ]
    ] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[
        typing.Sequence[
            typing.Union[
                typing.Union[
                    _cdktf_9a9027ec.FileProvisioner,
                    typing.Dict[builtins.str, typing.Any],
                ],
                typing.Union[
                    _cdktf_9a9027ec.LocalExecProvisioner,
                    typing.Dict[builtins.str, typing.Any],
                ],
                typing.Union[
                    _cdktf_9a9027ec.RemoteExecProvisioner,
                    typing.Dict[builtins.str, typing.Any],
                ],
            ]
        ]
    ] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__7e9db62f313744edd1bdec2e874071f8854fa47f29a3b13394e8887ac575d884(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__b7bfd0816a5477c98be738d6086705fbd07dfd16d29ad04630e64840344b04a8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__cb9857d3425e1701cc9227611b28e38bdfd3a201aeaf925719ec93380b4a9bdd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__2ebf0ce27ccb3a33e211dbbc2a8c19f9108848e58fd6a2f09f3dd21fb90f2ef0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__c23481c1865c4698f5d3afa69aaac8c458f23f24a08a39a8d36a091d385a2711(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__05bad28fb496e4f3bf36366af49f9fc339fb09d2caf19bf0fb85f8aba06b9c3f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__6464a1fd4a7f75e75238c731c183f48ef78df358226632114a247ba984152758(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__19a69e7b71aee7fc6e65c6adc1722347eb173e402a99a966f4f16c235c718d5a(
    *,
    connection: typing.Optional[
        typing.Union[
            typing.Union[
                _cdktf_9a9027ec.SSHProvisionerConnection,
                typing.Dict[builtins.str, typing.Any],
            ],
            typing.Union[
                _cdktf_9a9027ec.WinrmProvisionerConnection,
                typing.Dict[builtins.str, typing.Any],
            ],
        ]
    ] = None,
    count: typing.Optional[
        typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]
    ] = None,
    depends_on: typing.Optional[
        typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]
    ] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.TerraformResourceLifecycle,
            typing.Dict[builtins.str, typing.Any],
        ]
    ] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[
        typing.Sequence[
            typing.Union[
                typing.Union[
                    _cdktf_9a9027ec.FileProvisioner,
                    typing.Dict[builtins.str, typing.Any],
                ],
                typing.Union[
                    _cdktf_9a9027ec.LocalExecProvisioner,
                    typing.Dict[builtins.str, typing.Any],
                ],
                typing.Union[
                    _cdktf_9a9027ec.RemoteExecProvisioner,
                    typing.Dict[builtins.str, typing.Any],
                ],
            ]
        ]
    ] = None,
    cluster_id: builtins.str,
    db_name: builtins.str,
    mode: builtins.str,
    name: builtins.str,
    size: jsii.Number,
    id: typing.Optional[builtins.str] = None,
    user: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
