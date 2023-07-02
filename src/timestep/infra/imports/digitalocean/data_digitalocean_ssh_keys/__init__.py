"""
# `data_digitalocean_ssh_keys`

Refer to the Terraform Registory for docs: [`data_digitalocean_ssh_keys`](https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/data-sources/ssh_keys).
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


class DataDigitaloceanSshKeys(
    _cdktf_9a9027ec.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.dataDigitaloceanSshKeys.DataDigitaloceanSshKeys",
):
    """Represents a {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/data-sources/ssh_keys digitalocean_ssh_keys}."""

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        filter: typing.Optional[
            typing.Union[
                _cdktf_9a9027ec.IResolvable,
                typing.Sequence[
                    typing.Union[
                        "DataDigitaloceanSshKeysFilter",
                        typing.Dict[builtins.str, typing.Any],
                    ]
                ],
            ]
        ] = None,
        id: typing.Optional[builtins.str] = None,
        sort: typing.Optional[
            typing.Union[
                _cdktf_9a9027ec.IResolvable,
                typing.Sequence[
                    typing.Union[
                        "DataDigitaloceanSshKeysSort",
                        typing.Dict[builtins.str, typing.Any],
                    ]
                ],
            ]
        ] = None,
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
        """Create a new {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/data-sources/ssh_keys digitalocean_ssh_keys} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param filter: filter block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/data-sources/ssh_keys#filter DataDigitaloceanSshKeys#filter}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/data-sources/ssh_keys#id DataDigitaloceanSshKeys#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param sort: sort block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/data-sources/ssh_keys#sort DataDigitaloceanSshKeys#sort}
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
                _typecheckingstub__58640e3450c93f6c3efb3b4bec1229b337a7c4195c8a2b8026818ead8cf76117
            )
            check_type(
                argname="argument scope", value=scope, expected_type=type_hints["scope"]
            )
            check_type(
                argname="argument id_", value=id_, expected_type=type_hints["id_"]
            )
        config = DataDigitaloceanSshKeysConfig(
            filter=filter,
            id=id,
            sort=sort,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putFilter")
    def put_filter(
        self,
        value: typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.Sequence[
                typing.Union[
                    "DataDigitaloceanSshKeysFilter",
                    typing.Dict[builtins.str, typing.Any],
                ]
            ],
        ],
    ) -> None:
        """
        :param value: -
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__044f072120673dcbcc0a5828f4843b877939bc74d2bf49704dfde0a5a9982fd7
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        return typing.cast(None, jsii.invoke(self, "putFilter", [value]))

    @jsii.member(jsii_name="putSort")
    def put_sort(
        self,
        value: typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.Sequence[
                typing.Union[
                    "DataDigitaloceanSshKeysSort", typing.Dict[builtins.str, typing.Any]
                ]
            ],
        ],
    ) -> None:
        """
        :param value: -
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__419697b4e1b78d06187bb7eba0cf7921b223571889eecc4142313b384aa1fc15
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        return typing.cast(None, jsii.invoke(self, "putSort", [value]))

    @jsii.member(jsii_name="resetFilter")
    def reset_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilter", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetSort")
    def reset_sort(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSort", []))

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
    @jsii.member(jsii_name="filter")
    def filter(self) -> "DataDigitaloceanSshKeysFilterList":
        return typing.cast(
            "DataDigitaloceanSshKeysFilterList", jsii.get(self, "filter")
        )

    @builtins.property
    @jsii.member(jsii_name="sort")
    def sort(self) -> "DataDigitaloceanSshKeysSortList":
        return typing.cast("DataDigitaloceanSshKeysSortList", jsii.get(self, "sort"))

    @builtins.property
    @jsii.member(jsii_name="sshKeys")
    def ssh_keys(self) -> "DataDigitaloceanSshKeysSshKeysList":
        return typing.cast(
            "DataDigitaloceanSshKeysSshKeysList", jsii.get(self, "sshKeys")
        )

    @builtins.property
    @jsii.member(jsii_name="filterInput")
    def filter_input(
        self,
    ) -> typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable, typing.List["DataDigitaloceanSshKeysFilter"]
        ]
    ]:
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.IResolvable,
                    typing.List["DataDigitaloceanSshKeysFilter"],
                ]
            ],
            jsii.get(self, "filterInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="sortInput")
    def sort_input(
        self,
    ) -> typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable, typing.List["DataDigitaloceanSshKeysSort"]
        ]
    ]:
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.IResolvable,
                    typing.List["DataDigitaloceanSshKeysSort"],
                ]
            ],
            jsii.get(self, "sortInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__b3bd220889244ac1fe241789a56308e1ae940b180ba1d7adab908c90bc7492a3
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="digitalocean.dataDigitaloceanSshKeys.DataDigitaloceanSshKeysConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "filter": "filter",
        "id": "id",
        "sort": "sort",
    },
)
class DataDigitaloceanSshKeysConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        filter: typing.Optional[
            typing.Union[
                _cdktf_9a9027ec.IResolvable,
                typing.Sequence[
                    typing.Union[
                        "DataDigitaloceanSshKeysFilter",
                        typing.Dict[builtins.str, typing.Any],
                    ]
                ],
            ]
        ] = None,
        id: typing.Optional[builtins.str] = None,
        sort: typing.Optional[
            typing.Union[
                _cdktf_9a9027ec.IResolvable,
                typing.Sequence[
                    typing.Union[
                        "DataDigitaloceanSshKeysSort",
                        typing.Dict[builtins.str, typing.Any],
                    ]
                ],
            ]
        ] = None,
    ) -> None:
        """
        :param connection:
        :param count:
        :param depends_on:
        :param for_each:
        :param lifecycle:
        :param provider:
        :param provisioners:
        :param filter: filter block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/data-sources/ssh_keys#filter DataDigitaloceanSshKeys#filter}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/data-sources/ssh_keys#id DataDigitaloceanSshKeys#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param sort: sort block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/data-sources/ssh_keys#sort DataDigitaloceanSshKeys#sort}
        """
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__5b4b2757a406cd6c4333f6f2f4a5d3572c38b35a0d1d7ab7ab70fe2cf9bb8c1b
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
                argname="argument filter",
                value=filter,
                expected_type=type_hints["filter"],
            )
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(
                argname="argument sort", value=sort, expected_type=type_hints["sort"]
            )
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
        if filter is not None:
            self._values["filter"] = filter
        if id is not None:
            self._values["id"] = id
        if sort is not None:
            self._values["sort"] = sort

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
    def filter(
        self,
    ) -> typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable, typing.List["DataDigitaloceanSshKeysFilter"]
        ]
    ]:
        """filter block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/data-sources/ssh_keys#filter DataDigitaloceanSshKeys#filter}
        """
        result = self._values.get("filter")
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.IResolvable,
                    typing.List["DataDigitaloceanSshKeysFilter"],
                ]
            ],
            result,
        )

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/data-sources/ssh_keys#id DataDigitaloceanSshKeys#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        """
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sort(
        self,
    ) -> typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable, typing.List["DataDigitaloceanSshKeysSort"]
        ]
    ]:
        """sort block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/data-sources/ssh_keys#sort DataDigitaloceanSshKeys#sort}
        """
        result = self._values.get("sort")
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.IResolvable,
                    typing.List["DataDigitaloceanSshKeysSort"],
                ]
            ],
            result,
        )

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDigitaloceanSshKeysConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="digitalocean.dataDigitaloceanSshKeys.DataDigitaloceanSshKeysFilter",
    jsii_struct_bases=[],
    name_mapping={
        "key": "key",
        "values": "values",
        "all": "all",
        "match_by": "matchBy",
    },
)
class DataDigitaloceanSshKeysFilter:
    def __init__(
        self,
        *,
        key: builtins.str,
        values: typing.Sequence[builtins.str],
        all: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        match_by: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param key: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/data-sources/ssh_keys#key DataDigitaloceanSshKeys#key}.
        :param values: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/data-sources/ssh_keys#values DataDigitaloceanSshKeys#values}.
        :param all: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/data-sources/ssh_keys#all DataDigitaloceanSshKeys#all}.
        :param match_by: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/data-sources/ssh_keys#match_by DataDigitaloceanSshKeys#match_by}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__73b93fc1cd5fac455fb9c69574f68803a0522dbce7a607c122aafe6aac28dc89
            )
            check_type(
                argname="argument key", value=key, expected_type=type_hints["key"]
            )
            check_type(
                argname="argument values",
                value=values,
                expected_type=type_hints["values"],
            )
            check_type(
                argname="argument all", value=all, expected_type=type_hints["all"]
            )
            check_type(
                argname="argument match_by",
                value=match_by,
                expected_type=type_hints["match_by"],
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "values": values,
        }
        if all is not None:
            self._values["all"] = all
        if match_by is not None:
            self._values["match_by"] = match_by

    @builtins.property
    def key(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/data-sources/ssh_keys#key DataDigitaloceanSshKeys#key}."""
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/data-sources/ssh_keys#values DataDigitaloceanSshKeys#values}."""
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def all(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/data-sources/ssh_keys#all DataDigitaloceanSshKeys#all}."""
        result = self._values.get("all")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def match_by(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/data-sources/ssh_keys#match_by DataDigitaloceanSshKeys#match_by}."""
        result = self._values.get("match_by")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDigitaloceanSshKeysFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataDigitaloceanSshKeysFilterList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.dataDigitaloceanSshKeys.DataDigitaloceanSshKeysFilterList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        """
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__4877cb58735374787324a8f913211b12396507ebfece8da8ba805f83a5c9eafd
            )
            check_type(
                argname="argument terraform_resource",
                value=terraform_resource,
                expected_type=type_hints["terraform_resource"],
            )
            check_type(
                argname="argument terraform_attribute",
                value=terraform_attribute,
                expected_type=type_hints["terraform_attribute"],
            )
            check_type(
                argname="argument wraps_set",
                value=wraps_set,
                expected_type=type_hints["wraps_set"],
            )
        jsii.create(
            self.__class__, self, [terraform_resource, terraform_attribute, wraps_set]
        )

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DataDigitaloceanSshKeysFilterOutputReference":
        """
        :param index: the index of the item to return.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__f26d3d610ae132583b8611d794058f13cac299fd8e212caa6c2547c06076da4d
            )
            check_type(
                argname="argument index", value=index, expected_type=type_hints["index"]
            )
        return typing.cast(
            "DataDigitaloceanSshKeysFilterOutputReference",
            jsii.invoke(self, "get", [index]),
        )

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        """The attribute on the parent resource this class is referencing."""
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__94cac6aa7cc8fe96ad27a029a55f655b1ba0f5f0bbe24a0454f0b5ca4b90740a
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        """The parent resource."""
        return typing.cast(
            _cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource")
        )

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__0eb759d077eb59c46ed9de6d1711f9b84dc3eef7bd7aae9c533813567175024a
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        """whether the list is wrapping a set (will add tolist() to be able to access an item via an index)."""
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__53b1d65b12cea48cf06451e4fb01210d061d4e66d08908290d108860f3403234
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable, typing.List[DataDigitaloceanSshKeysFilter]
        ]
    ]:
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.IResolvable,
                    typing.List[DataDigitaloceanSshKeysFilter],
                ]
            ],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[
            typing.Union[
                _cdktf_9a9027ec.IResolvable, typing.List[DataDigitaloceanSshKeysFilter]
            ]
        ],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__b28680c088adb0531930a89440c738284b74b199196d8ce329bc5314a20e1ef5
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


class DataDigitaloceanSshKeysFilterOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.dataDigitaloceanSshKeys.DataDigitaloceanSshKeysFilterOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        """
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__91e4074b97ce561599e807e7e01a439cd2f86e8a3020b14caf025659bd4d87d2
            )
            check_type(
                argname="argument terraform_resource",
                value=terraform_resource,
                expected_type=type_hints["terraform_resource"],
            )
            check_type(
                argname="argument terraform_attribute",
                value=terraform_attribute,
                expected_type=type_hints["terraform_attribute"],
            )
            check_type(
                argname="argument complex_object_index",
                value=complex_object_index,
                expected_type=type_hints["complex_object_index"],
            )
            check_type(
                argname="argument complex_object_is_from_set",
                value=complex_object_is_from_set,
                expected_type=type_hints["complex_object_is_from_set"],
            )
        jsii.create(
            self.__class__,
            self,
            [
                terraform_resource,
                terraform_attribute,
                complex_object_index,
                complex_object_is_from_set,
            ],
        )

    @jsii.member(jsii_name="resetAll")
    def reset_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAll", []))

    @jsii.member(jsii_name="resetMatchBy")
    def reset_match_by(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchBy", []))

    @builtins.property
    @jsii.member(jsii_name="allInput")
    def all_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "allInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="matchByInput")
    def match_by_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "matchByInput")
        )

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(
            typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput")
        )

    @builtins.property
    @jsii.member(jsii_name="all")
    def all(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "all"),
        )

    @all.setter
    def all(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__a121459702d778e7b97ff44dc1d1515fd34d7c498315024554da9fc678a830a5
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "all", value)

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__d0fb89115b63886bbf2544820d21547bfd466afe821e6c956f6b7e21ff68c2c6
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="matchBy")
    def match_by(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "matchBy"))

    @match_by.setter
    def match_by(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__85697a5645db233ac75d9da213f4f48e4b48b8fef0d8b31aabae2ec158000fff
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "matchBy", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__e68444386f04b8d8fea0b36e348100b51ad91e53275b6d303d3a4c673c3df943
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, DataDigitaloceanSshKeysFilter]
    ]:
        return typing.cast(
            typing.Optional[
                typing.Union[_cdktf_9a9027ec.IResolvable, DataDigitaloceanSshKeysFilter]
            ],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[
            typing.Union[_cdktf_9a9027ec.IResolvable, DataDigitaloceanSshKeysFilter]
        ],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__f3a2df5343212e10f1d45c9cad733a10c6b5ce8e7633eebe41465f7770ab0a46
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="digitalocean.dataDigitaloceanSshKeys.DataDigitaloceanSshKeysSort",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "direction": "direction"},
)
class DataDigitaloceanSshKeysSort:
    def __init__(
        self,
        *,
        key: builtins.str,
        direction: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param key: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/data-sources/ssh_keys#key DataDigitaloceanSshKeys#key}.
        :param direction: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/data-sources/ssh_keys#direction DataDigitaloceanSshKeys#direction}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__1a4678a902462f7dcdd05be6b523b6f029c3ede80bbaf89e2c3dd924e0dd31fd
            )
            check_type(
                argname="argument key", value=key, expected_type=type_hints["key"]
            )
            check_type(
                argname="argument direction",
                value=direction,
                expected_type=type_hints["direction"],
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
        }
        if direction is not None:
            self._values["direction"] = direction

    @builtins.property
    def key(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/data-sources/ssh_keys#key DataDigitaloceanSshKeys#key}."""
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def direction(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/data-sources/ssh_keys#direction DataDigitaloceanSshKeys#direction}."""
        result = self._values.get("direction")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDigitaloceanSshKeysSort(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataDigitaloceanSshKeysSortList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.dataDigitaloceanSshKeys.DataDigitaloceanSshKeysSortList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        """
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__1c6aa5dfaeefdd7668d80bbb10c808235e9dc08600e711ac5384e0705f355d55
            )
            check_type(
                argname="argument terraform_resource",
                value=terraform_resource,
                expected_type=type_hints["terraform_resource"],
            )
            check_type(
                argname="argument terraform_attribute",
                value=terraform_attribute,
                expected_type=type_hints["terraform_attribute"],
            )
            check_type(
                argname="argument wraps_set",
                value=wraps_set,
                expected_type=type_hints["wraps_set"],
            )
        jsii.create(
            self.__class__, self, [terraform_resource, terraform_attribute, wraps_set]
        )

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DataDigitaloceanSshKeysSortOutputReference":
        """
        :param index: the index of the item to return.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__c837fae542b54c4e556a4c9c20f8068036be77c53381a3e96d1403427a3ee430
            )
            check_type(
                argname="argument index", value=index, expected_type=type_hints["index"]
            )
        return typing.cast(
            "DataDigitaloceanSshKeysSortOutputReference",
            jsii.invoke(self, "get", [index]),
        )

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        """The attribute on the parent resource this class is referencing."""
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__45800e84b827b7ee53a02fcde905c8018660d1867e7c08281ca49e201009285a
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        """The parent resource."""
        return typing.cast(
            _cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource")
        )

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__de9679e8fd3c51aedd25e873a604bfe75bf1562552be9bcba8cb206c0fc8e32c
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        """whether the list is wrapping a set (will add tolist() to be able to access an item via an index)."""
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__a675a3ee4dc33416e3e8fb4896886476af4fc3ef216c2c8f466ce3962ca29f49
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable, typing.List[DataDigitaloceanSshKeysSort]
        ]
    ]:
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.IResolvable,
                    typing.List[DataDigitaloceanSshKeysSort],
                ]
            ],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[
            typing.Union[
                _cdktf_9a9027ec.IResolvable, typing.List[DataDigitaloceanSshKeysSort]
            ]
        ],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__868e06f300da02fe01d3e7ac7e6528abc5975ad82ddfcfa37bf80af192f339dc
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


class DataDigitaloceanSshKeysSortOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.dataDigitaloceanSshKeys.DataDigitaloceanSshKeysSortOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        """
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__944c843ab6e376263da0bea5c812b0256356c20bbfb5b8c42d52c54d1fb578e4
            )
            check_type(
                argname="argument terraform_resource",
                value=terraform_resource,
                expected_type=type_hints["terraform_resource"],
            )
            check_type(
                argname="argument terraform_attribute",
                value=terraform_attribute,
                expected_type=type_hints["terraform_attribute"],
            )
            check_type(
                argname="argument complex_object_index",
                value=complex_object_index,
                expected_type=type_hints["complex_object_index"],
            )
            check_type(
                argname="argument complex_object_is_from_set",
                value=complex_object_is_from_set,
                expected_type=type_hints["complex_object_is_from_set"],
            )
        jsii.create(
            self.__class__,
            self,
            [
                terraform_resource,
                terraform_attribute,
                complex_object_index,
                complex_object_is_from_set,
            ],
        )

    @jsii.member(jsii_name="resetDirection")
    def reset_direction(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDirection", []))

    @builtins.property
    @jsii.member(jsii_name="directionInput")
    def direction_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "directionInput")
        )

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="direction")
    def direction(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "direction"))

    @direction.setter
    def direction(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__7661f62f904afaacedf3b0d9757c6d1d7abdd33f6af88884c1e4aba74793fb44
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "direction", value)

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__84fb83f710faee119813403fb9c987e885e764974fde0eb1cb70314084430812
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, DataDigitaloceanSshKeysSort]
    ]:
        return typing.cast(
            typing.Optional[
                typing.Union[_cdktf_9a9027ec.IResolvable, DataDigitaloceanSshKeysSort]
            ],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[
            typing.Union[_cdktf_9a9027ec.IResolvable, DataDigitaloceanSshKeysSort]
        ],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__b364da7e879afdb1d48d9e40ea3e2a38cc830d4efc446ca9c0febb257e838d56
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="digitalocean.dataDigitaloceanSshKeys.DataDigitaloceanSshKeysSshKeys",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataDigitaloceanSshKeysSshKeys:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDigitaloceanSshKeysSshKeys(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataDigitaloceanSshKeysSshKeysList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.dataDigitaloceanSshKeys.DataDigitaloceanSshKeysSshKeysList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        """
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__ffb8bf07a01cdfab3d67b86dba4433d5604b0151521780ce9c914bdd2ee5b77c
            )
            check_type(
                argname="argument terraform_resource",
                value=terraform_resource,
                expected_type=type_hints["terraform_resource"],
            )
            check_type(
                argname="argument terraform_attribute",
                value=terraform_attribute,
                expected_type=type_hints["terraform_attribute"],
            )
            check_type(
                argname="argument wraps_set",
                value=wraps_set,
                expected_type=type_hints["wraps_set"],
            )
        jsii.create(
            self.__class__, self, [terraform_resource, terraform_attribute, wraps_set]
        )

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataDigitaloceanSshKeysSshKeysOutputReference":
        """
        :param index: the index of the item to return.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__19b32cb3ed3f3d3c0f2b69760576d2e4ee1b08382b7bda405881382c1612398c
            )
            check_type(
                argname="argument index", value=index, expected_type=type_hints["index"]
            )
        return typing.cast(
            "DataDigitaloceanSshKeysSshKeysOutputReference",
            jsii.invoke(self, "get", [index]),
        )

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        """The attribute on the parent resource this class is referencing."""
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__c6012a40d1ff0a2b38efd7e94f943d4e3ceeca696c1be5fae7395b894c24ce85
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        """The parent resource."""
        return typing.cast(
            _cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource")
        )

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__147b6c2179f556dad6f6f4753f03479536cdc86f5015648ba037a6341119885a
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        """whether the list is wrapping a set (will add tolist() to be able to access an item via an index)."""
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__dfcccf0c3513cddb480af38cf883595bce3cbe561a696079a0bbad3e58d30772
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "wrapsSet", value)


class DataDigitaloceanSshKeysSshKeysOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.dataDigitaloceanSshKeys.DataDigitaloceanSshKeysSshKeysOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        """
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__d8b4902f1559101ebf0f7c265734cfdb6a838bbfeee8ff9b117e35b65166a3a2
            )
            check_type(
                argname="argument terraform_resource",
                value=terraform_resource,
                expected_type=type_hints["terraform_resource"],
            )
            check_type(
                argname="argument terraform_attribute",
                value=terraform_attribute,
                expected_type=type_hints["terraform_attribute"],
            )
            check_type(
                argname="argument complex_object_index",
                value=complex_object_index,
                expected_type=type_hints["complex_object_index"],
            )
            check_type(
                argname="argument complex_object_is_from_set",
                value=complex_object_is_from_set,
                expected_type=type_hints["complex_object_is_from_set"],
            )
        jsii.create(
            self.__class__,
            self,
            [
                terraform_resource,
                terraform_attribute,
                complex_object_index,
                complex_object_is_from_set,
            ],
        )

    @builtins.property
    @jsii.member(jsii_name="fingerprint")
    def fingerprint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fingerprint"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="publicKey")
    def public_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicKey"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataDigitaloceanSshKeysSshKeys]:
        return typing.cast(
            typing.Optional[DataDigitaloceanSshKeysSshKeys],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataDigitaloceanSshKeysSshKeys],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__7c0fa660a8e2a818d693a04c52173f09089e43cb69b68dfef95e5f4c437ac9a1
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataDigitaloceanSshKeys",
    "DataDigitaloceanSshKeysConfig",
    "DataDigitaloceanSshKeysFilter",
    "DataDigitaloceanSshKeysFilterList",
    "DataDigitaloceanSshKeysFilterOutputReference",
    "DataDigitaloceanSshKeysSort",
    "DataDigitaloceanSshKeysSortList",
    "DataDigitaloceanSshKeysSortOutputReference",
    "DataDigitaloceanSshKeysSshKeys",
    "DataDigitaloceanSshKeysSshKeysList",
    "DataDigitaloceanSshKeysSshKeysOutputReference",
]

publication.publish()


def _typecheckingstub__58640e3450c93f6c3efb3b4bec1229b337a7c4195c8a2b8026818ead8cf76117(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    filter: typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.Sequence[
                typing.Union[
                    DataDigitaloceanSshKeysFilter, typing.Dict[builtins.str, typing.Any]
                ]
            ],
        ]
    ] = None,
    id: typing.Optional[builtins.str] = None,
    sort: typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.Sequence[
                typing.Union[
                    DataDigitaloceanSshKeysSort, typing.Dict[builtins.str, typing.Any]
                ]
            ],
        ]
    ] = None,
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


def _typecheckingstub__044f072120673dcbcc0a5828f4843b877939bc74d2bf49704dfde0a5a9982fd7(
    value: typing.Union[
        _cdktf_9a9027ec.IResolvable,
        typing.Sequence[
            typing.Union[
                DataDigitaloceanSshKeysFilter, typing.Dict[builtins.str, typing.Any]
            ]
        ],
    ],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__419697b4e1b78d06187bb7eba0cf7921b223571889eecc4142313b384aa1fc15(
    value: typing.Union[
        _cdktf_9a9027ec.IResolvable,
        typing.Sequence[
            typing.Union[
                DataDigitaloceanSshKeysSort, typing.Dict[builtins.str, typing.Any]
            ]
        ],
    ],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__b3bd220889244ac1fe241789a56308e1ae940b180ba1d7adab908c90bc7492a3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__5b4b2757a406cd6c4333f6f2f4a5d3572c38b35a0d1d7ab7ab70fe2cf9bb8c1b(
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
    filter: typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.Sequence[
                typing.Union[
                    DataDigitaloceanSshKeysFilter, typing.Dict[builtins.str, typing.Any]
                ]
            ],
        ]
    ] = None,
    id: typing.Optional[builtins.str] = None,
    sort: typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.Sequence[
                typing.Union[
                    DataDigitaloceanSshKeysSort, typing.Dict[builtins.str, typing.Any]
                ]
            ],
        ]
    ] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__73b93fc1cd5fac455fb9c69574f68803a0522dbce7a607c122aafe6aac28dc89(
    *,
    key: builtins.str,
    values: typing.Sequence[builtins.str],
    all: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    match_by: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__4877cb58735374787324a8f913211b12396507ebfece8da8ba805f83a5c9eafd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__f26d3d610ae132583b8611d794058f13cac299fd8e212caa6c2547c06076da4d(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__94cac6aa7cc8fe96ad27a029a55f655b1ba0f5f0bbe24a0454f0b5ca4b90740a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__0eb759d077eb59c46ed9de6d1711f9b84dc3eef7bd7aae9c533813567175024a(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__53b1d65b12cea48cf06451e4fb01210d061d4e66d08908290d108860f3403234(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__b28680c088adb0531930a89440c738284b74b199196d8ce329bc5314a20e1ef5(
    value: typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable, typing.List[DataDigitaloceanSshKeysFilter]
        ]
    ],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__91e4074b97ce561599e807e7e01a439cd2f86e8a3020b14caf025659bd4d87d2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a121459702d778e7b97ff44dc1d1515fd34d7c498315024554da9fc678a830a5(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d0fb89115b63886bbf2544820d21547bfd466afe821e6c956f6b7e21ff68c2c6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__85697a5645db233ac75d9da213f4f48e4b48b8fef0d8b31aabae2ec158000fff(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__e68444386f04b8d8fea0b36e348100b51ad91e53275b6d303d3a4c673c3df943(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__f3a2df5343212e10f1d45c9cad733a10c6b5ce8e7633eebe41465f7770ab0a46(
    value: typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, DataDigitaloceanSshKeysFilter]
    ],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__1a4678a902462f7dcdd05be6b523b6f029c3ede80bbaf89e2c3dd924e0dd31fd(
    *,
    key: builtins.str,
    direction: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__1c6aa5dfaeefdd7668d80bbb10c808235e9dc08600e711ac5384e0705f355d55(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__c837fae542b54c4e556a4c9c20f8068036be77c53381a3e96d1403427a3ee430(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__45800e84b827b7ee53a02fcde905c8018660d1867e7c08281ca49e201009285a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__de9679e8fd3c51aedd25e873a604bfe75bf1562552be9bcba8cb206c0fc8e32c(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a675a3ee4dc33416e3e8fb4896886476af4fc3ef216c2c8f466ce3962ca29f49(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__868e06f300da02fe01d3e7ac7e6528abc5975ad82ddfcfa37bf80af192f339dc(
    value: typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable, typing.List[DataDigitaloceanSshKeysSort]
        ]
    ],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__944c843ab6e376263da0bea5c812b0256356c20bbfb5b8c42d52c54d1fb578e4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__7661f62f904afaacedf3b0d9757c6d1d7abdd33f6af88884c1e4aba74793fb44(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__84fb83f710faee119813403fb9c987e885e764974fde0eb1cb70314084430812(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__b364da7e879afdb1d48d9e40ea3e2a38cc830d4efc446ca9c0febb257e838d56(
    value: typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, DataDigitaloceanSshKeysSort]
    ],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__ffb8bf07a01cdfab3d67b86dba4433d5604b0151521780ce9c914bdd2ee5b77c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__19b32cb3ed3f3d3c0f2b69760576d2e4ee1b08382b7bda405881382c1612398c(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__c6012a40d1ff0a2b38efd7e94f943d4e3ceeca696c1be5fae7395b894c24ce85(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__147b6c2179f556dad6f6f4753f03479536cdc86f5015648ba037a6341119885a(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__dfcccf0c3513cddb480af38cf883595bce3cbe561a696079a0bbad3e58d30772(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d8b4902f1559101ebf0f7c265734cfdb6a838bbfeee8ff9b117e35b65166a3a2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__7c0fa660a8e2a818d693a04c52173f09089e43cb69b68dfef95e5f4c437ac9a1(
    value: typing.Optional[DataDigitaloceanSshKeysSshKeys],
) -> None:
    """Type checking stubs"""
    pass
