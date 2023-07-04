"""
# `data_digitalocean_images`

Refer to the Terraform Registory for docs: [`data_digitalocean_images`](https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/data-sources/images).
"""
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


class DataDigitaloceanImages(
    _cdktf_9a9027ec.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.dataDigitaloceanImages.DataDigitaloceanImages",
):
    """Represents a {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/data-sources/images digitalocean_images}."""

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
                        "DataDigitaloceanImagesFilter",
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
                        "DataDigitaloceanImagesSort",
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
        """Create a new {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/data-sources/images digitalocean_images} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param filter: filter block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/data-sources/images#filter DataDigitaloceanImages#filter}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/data-sources/images#id DataDigitaloceanImages#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param sort: sort block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/data-sources/images#sort DataDigitaloceanImages#sort}
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
                _typecheckingstub__68907d0faf07ebcf5f90fdea1b316a509f5f6eb3f6bd72f867c2233f6ec91aea
            )
            check_type(
                argname="argument scope", value=scope, expected_type=type_hints["scope"]
            )
            check_type(
                argname="argument id_", value=id_, expected_type=type_hints["id_"]
            )
        config = DataDigitaloceanImagesConfig(
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
                    "DataDigitaloceanImagesFilter",
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
                _typecheckingstub__e459810dc775a00a7fc357858107d393f118ccb20ffef7142115cecff9320a0c
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
                    "DataDigitaloceanImagesSort", typing.Dict[builtins.str, typing.Any]
                ]
            ],
        ],
    ) -> None:
        """
        :param value: -
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__2030648cc5e151bf95aac17936329c026f3a0ab559fa61002bb98bb97021dfc2
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
    def filter(self) -> "DataDigitaloceanImagesFilterList":
        return typing.cast("DataDigitaloceanImagesFilterList", jsii.get(self, "filter"))

    @builtins.property
    @jsii.member(jsii_name="images")
    def images(self) -> "DataDigitaloceanImagesImagesList":
        return typing.cast("DataDigitaloceanImagesImagesList", jsii.get(self, "images"))

    @builtins.property
    @jsii.member(jsii_name="sort")
    def sort(self) -> "DataDigitaloceanImagesSortList":
        return typing.cast("DataDigitaloceanImagesSortList", jsii.get(self, "sort"))

    @builtins.property
    @jsii.member(jsii_name="filterInput")
    def filter_input(
        self,
    ) -> typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable, typing.List["DataDigitaloceanImagesFilter"]
        ]
    ]:
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.IResolvable,
                    typing.List["DataDigitaloceanImagesFilter"],
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
            _cdktf_9a9027ec.IResolvable, typing.List["DataDigitaloceanImagesSort"]
        ]
    ]:
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.IResolvable,
                    typing.List["DataDigitaloceanImagesSort"],
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
                _typecheckingstub__fed6e584548c7ccaf87f0442db5456ffab1cb4bf5110bf2d0582dd1dd80eb57d
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="digitalocean.dataDigitaloceanImages.DataDigitaloceanImagesConfig",
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
class DataDigitaloceanImagesConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
                        "DataDigitaloceanImagesFilter",
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
                        "DataDigitaloceanImagesSort",
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
        :param filter: filter block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/data-sources/images#filter DataDigitaloceanImages#filter}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/data-sources/images#id DataDigitaloceanImages#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param sort: sort block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/data-sources/images#sort DataDigitaloceanImages#sort}
        """
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__6c0d91b039eb82cd4309084f5f45e147b329457d23b5281035608e90159545aa
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
            _cdktf_9a9027ec.IResolvable, typing.List["DataDigitaloceanImagesFilter"]
        ]
    ]:
        """filter block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/data-sources/images#filter DataDigitaloceanImages#filter}
        """
        result = self._values.get("filter")
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.IResolvable,
                    typing.List["DataDigitaloceanImagesFilter"],
                ]
            ],
            result,
        )

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/data-sources/images#id DataDigitaloceanImages#id}.

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
            _cdktf_9a9027ec.IResolvable, typing.List["DataDigitaloceanImagesSort"]
        ]
    ]:
        """sort block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/data-sources/images#sort DataDigitaloceanImages#sort}
        """
        result = self._values.get("sort")
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.IResolvable,
                    typing.List["DataDigitaloceanImagesSort"],
                ]
            ],
            result,
        )

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDigitaloceanImagesConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="digitalocean.dataDigitaloceanImages.DataDigitaloceanImagesFilter",
    jsii_struct_bases=[],
    name_mapping={
        "key": "key",
        "values": "values",
        "all": "all",
        "match_by": "matchBy",
    },
)
class DataDigitaloceanImagesFilter:
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
        :param key: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/data-sources/images#key DataDigitaloceanImages#key}.
        :param values: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/data-sources/images#values DataDigitaloceanImages#values}.
        :param all: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/data-sources/images#all DataDigitaloceanImages#all}.
        :param match_by: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/data-sources/images#match_by DataDigitaloceanImages#match_by}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__f9fa79193c9695699b3875c8988de4aa2ad023d598d6800d289effb7f45394c6
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
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/data-sources/images#key DataDigitaloceanImages#key}."""
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/data-sources/images#values DataDigitaloceanImages#values}."""
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def all(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/data-sources/images#all DataDigitaloceanImages#all}."""
        result = self._values.get("all")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def match_by(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/data-sources/images#match_by DataDigitaloceanImages#match_by}."""
        result = self._values.get("match_by")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDigitaloceanImagesFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataDigitaloceanImagesFilterList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.dataDigitaloceanImages.DataDigitaloceanImagesFilterList",
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
                _typecheckingstub__7bdae12ff07755ffbfdf715443f06abdc34c55f584c5b00991257840757b9c40
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
    def get(self, index: jsii.Number) -> "DataDigitaloceanImagesFilterOutputReference":
        """
        :param index: the index of the item to return.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__a54e2ec062be11febe06e97c91a3383f9e3b86e206870c9f4dfc005d31948ae4
            )
            check_type(
                argname="argument index", value=index, expected_type=type_hints["index"]
            )
        return typing.cast(
            "DataDigitaloceanImagesFilterOutputReference",
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
                _typecheckingstub__f5854e45a3855941c0d3f36737bd653fae44846ae0e54af71c932eb2ffcf6105
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
                _typecheckingstub__4d623de8a084d6ea9dd9bc9290e390ad6ebd9e586552dbd7466e65b5f734e9e0
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
                _typecheckingstub__9f17fc47231904997860302f70746629972ba37c7f45a2773e008b01f8c1d84a
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
            _cdktf_9a9027ec.IResolvable, typing.List[DataDigitaloceanImagesFilter]
        ]
    ]:
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.IResolvable,
                    typing.List[DataDigitaloceanImagesFilter],
                ]
            ],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[
            typing.Union[
                _cdktf_9a9027ec.IResolvable, typing.List[DataDigitaloceanImagesFilter]
            ]
        ],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__267d177e78b300439e08872867501999dcc76f9417b5bb37d7ee2456f097f67a
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


class DataDigitaloceanImagesFilterOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.dataDigitaloceanImages.DataDigitaloceanImagesFilterOutputReference",
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
                _typecheckingstub__3ef50be90f6caa945a9b156506e53b5dfb96669249efd0c010bc55254434b644
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
                _typecheckingstub__0f0d3c4ea5297752f58ea8ef82ab8db799a663ede22b1b88345fd2038cc746f9
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
                _typecheckingstub__dd1ee8149aa15ae3af9e56c30aeebd7e3414178094023c7739679b0ef9169856
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
                _typecheckingstub__871c114ed4f61d4c635039cce1e7011d5719e995ef5db6099e1c314a6b9e7e91
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
                _typecheckingstub__a0e4ea83e8dfb9e17ec0b41df8c6dc28f66fdd92ce87304f5947a45894a193a1
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
        typing.Union[_cdktf_9a9027ec.IResolvable, DataDigitaloceanImagesFilter]
    ]:
        return typing.cast(
            typing.Optional[
                typing.Union[_cdktf_9a9027ec.IResolvable, DataDigitaloceanImagesFilter]
            ],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[
            typing.Union[_cdktf_9a9027ec.IResolvable, DataDigitaloceanImagesFilter]
        ],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__a350faedfecd88a3bcd71ed7477376d3b593ae3ecd64dc1b36ef48fd3c62e52f
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="digitalocean.dataDigitaloceanImages.DataDigitaloceanImagesImages",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataDigitaloceanImagesImages:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDigitaloceanImagesImages(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataDigitaloceanImagesImagesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.dataDigitaloceanImages.DataDigitaloceanImagesImagesList",
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
                _typecheckingstub__21f7bca2197ba440ad619fa7c56adea00ccf1a7a8a96aef9683537553dcbfc7d
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
    def get(self, index: jsii.Number) -> "DataDigitaloceanImagesImagesOutputReference":
        """
        :param index: the index of the item to return.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__9efeab7c252d0f02b5264b43b05bf83fdeb4c1dfbc4da6292256abd67e51a736
            )
            check_type(
                argname="argument index", value=index, expected_type=type_hints["index"]
            )
        return typing.cast(
            "DataDigitaloceanImagesImagesOutputReference",
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
                _typecheckingstub__753650ede469b174cd644d2f26800c1fe784d46029431be2dc25d65cbb78cb69
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
                _typecheckingstub__c1af9ff097963916604ff4cfb0f9a6688455db59895dd2ea39b896b81b9eca8f
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
                _typecheckingstub__452afc4b54a385f465016c9f3dd775858fc2e19c56cb6f1c93db174e19ea80f9
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "wrapsSet", value)


class DataDigitaloceanImagesImagesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.dataDigitaloceanImages.DataDigitaloceanImagesImagesOutputReference",
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
                _typecheckingstub__51f77922e889ed18267e082d0c527e7cd95dacca5a308e88357df59b63663d38
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
    @jsii.member(jsii_name="created")
    def created(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "created"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @builtins.property
    @jsii.member(jsii_name="distribution")
    def distribution(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "distribution"))

    @builtins.property
    @jsii.member(jsii_name="errorMessage")
    def error_message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "errorMessage"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="image")
    def image(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "image"))

    @builtins.property
    @jsii.member(jsii_name="minDiskSize")
    def min_disk_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minDiskSize"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="private")
    def private(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "private"))

    @builtins.property
    @jsii.member(jsii_name="regions")
    def regions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "regions"))

    @builtins.property
    @jsii.member(jsii_name="sizeGigabytes")
    def size_gigabytes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sizeGigabytes"))

    @builtins.property
    @jsii.member(jsii_name="slug")
    def slug(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "slug"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataDigitaloceanImagesImages]:
        return typing.cast(
            typing.Optional[DataDigitaloceanImagesImages],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataDigitaloceanImagesImages],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__67e2897eb08ad0b51be1d0247f682bda74b5eed8040f25b85e17aa819eae755d
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="digitalocean.dataDigitaloceanImages.DataDigitaloceanImagesSort",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "direction": "direction"},
)
class DataDigitaloceanImagesSort:
    def __init__(
        self,
        *,
        key: builtins.str,
        direction: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param key: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/data-sources/images#key DataDigitaloceanImages#key}.
        :param direction: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/data-sources/images#direction DataDigitaloceanImages#direction}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__6a0f731242dbca8d4221d8e62869aa01d74f40ce45d42cbe7222fc2f9279c410
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
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/data-sources/images#key DataDigitaloceanImages#key}."""
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def direction(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/data-sources/images#direction DataDigitaloceanImages#direction}."""
        result = self._values.get("direction")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDigitaloceanImagesSort(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataDigitaloceanImagesSortList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.dataDigitaloceanImages.DataDigitaloceanImagesSortList",
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
                _typecheckingstub__ffad1d5fbc96c21d5942088f0b5ab7d42f6e54234bf21eee9e87712863a2c0d8
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
    def get(self, index: jsii.Number) -> "DataDigitaloceanImagesSortOutputReference":
        """
        :param index: the index of the item to return.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__10539c12785ed26648f01e1fe9a6bb10545eb013b4d682f51a2de1df65d855fa
            )
            check_type(
                argname="argument index", value=index, expected_type=type_hints["index"]
            )
        return typing.cast(
            "DataDigitaloceanImagesSortOutputReference",
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
                _typecheckingstub__585e35c306676e9fb643aa818e7370893f98709456dfc92f81ac4f3d11f333b8
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
                _typecheckingstub__8cf22e1da534ab846b1717ec39e190136e681592faa3867d9c2c4ec5635dcb15
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
                _typecheckingstub__4da69bcb8be1a31c4a1f9a31d71c3a288e26037285a2908ce236b9b01bd2269f
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
            _cdktf_9a9027ec.IResolvable, typing.List[DataDigitaloceanImagesSort]
        ]
    ]:
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.IResolvable, typing.List[DataDigitaloceanImagesSort]
                ]
            ],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[
            typing.Union[
                _cdktf_9a9027ec.IResolvable, typing.List[DataDigitaloceanImagesSort]
            ]
        ],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__d49120111fd39d07dd8da64b72804df786f0dc298c161f6d8431f889275b02b0
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


class DataDigitaloceanImagesSortOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.dataDigitaloceanImages.DataDigitaloceanImagesSortOutputReference",
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
                _typecheckingstub__700dd5ee2f5a0fc273cddc1c31ba979f09ccd79472640ccfcab0594232c6436e
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
                _typecheckingstub__5d6e70827217e81a618c0ba80df946a13389854f6fd234e57b178696dd1f2820
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
                _typecheckingstub__fc07f680a90757ca158f9145df874ce39a2f802b86e6502c77bf455f8e772b13
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
        typing.Union[_cdktf_9a9027ec.IResolvable, DataDigitaloceanImagesSort]
    ]:
        return typing.cast(
            typing.Optional[
                typing.Union[_cdktf_9a9027ec.IResolvable, DataDigitaloceanImagesSort]
            ],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[
            typing.Union[_cdktf_9a9027ec.IResolvable, DataDigitaloceanImagesSort]
        ],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__bfce7c3020669ae63382618486f675f19bb6724103659af86d8c4543a7e721af
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataDigitaloceanImages",
    "DataDigitaloceanImagesConfig",
    "DataDigitaloceanImagesFilter",
    "DataDigitaloceanImagesFilterList",
    "DataDigitaloceanImagesFilterOutputReference",
    "DataDigitaloceanImagesImages",
    "DataDigitaloceanImagesImagesList",
    "DataDigitaloceanImagesImagesOutputReference",
    "DataDigitaloceanImagesSort",
    "DataDigitaloceanImagesSortList",
    "DataDigitaloceanImagesSortOutputReference",
]

publication.publish()


def _typecheckingstub__68907d0faf07ebcf5f90fdea1b316a509f5f6eb3f6bd72f867c2233f6ec91aea(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    filter: typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.Sequence[
                typing.Union[
                    DataDigitaloceanImagesFilter, typing.Dict[builtins.str, typing.Any]
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
                    DataDigitaloceanImagesSort, typing.Dict[builtins.str, typing.Any]
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


def _typecheckingstub__e459810dc775a00a7fc357858107d393f118ccb20ffef7142115cecff9320a0c(
    value: typing.Union[
        _cdktf_9a9027ec.IResolvable,
        typing.Sequence[
            typing.Union[
                DataDigitaloceanImagesFilter, typing.Dict[builtins.str, typing.Any]
            ]
        ],
    ],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__2030648cc5e151bf95aac17936329c026f3a0ab559fa61002bb98bb97021dfc2(
    value: typing.Union[
        _cdktf_9a9027ec.IResolvable,
        typing.Sequence[
            typing.Union[
                DataDigitaloceanImagesSort, typing.Dict[builtins.str, typing.Any]
            ]
        ],
    ],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__fed6e584548c7ccaf87f0442db5456ffab1cb4bf5110bf2d0582dd1dd80eb57d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__6c0d91b039eb82cd4309084f5f45e147b329457d23b5281035608e90159545aa(
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
                    DataDigitaloceanImagesFilter, typing.Dict[builtins.str, typing.Any]
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
                    DataDigitaloceanImagesSort, typing.Dict[builtins.str, typing.Any]
                ]
            ],
        ]
    ] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__f9fa79193c9695699b3875c8988de4aa2ad023d598d6800d289effb7f45394c6(
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


def _typecheckingstub__7bdae12ff07755ffbfdf715443f06abdc34c55f584c5b00991257840757b9c40(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a54e2ec062be11febe06e97c91a3383f9e3b86e206870c9f4dfc005d31948ae4(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__f5854e45a3855941c0d3f36737bd653fae44846ae0e54af71c932eb2ffcf6105(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__4d623de8a084d6ea9dd9bc9290e390ad6ebd9e586552dbd7466e65b5f734e9e0(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__9f17fc47231904997860302f70746629972ba37c7f45a2773e008b01f8c1d84a(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__267d177e78b300439e08872867501999dcc76f9417b5bb37d7ee2456f097f67a(
    value: typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable, typing.List[DataDigitaloceanImagesFilter]
        ]
    ],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__3ef50be90f6caa945a9b156506e53b5dfb96669249efd0c010bc55254434b644(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__0f0d3c4ea5297752f58ea8ef82ab8db799a663ede22b1b88345fd2038cc746f9(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__dd1ee8149aa15ae3af9e56c30aeebd7e3414178094023c7739679b0ef9169856(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__871c114ed4f61d4c635039cce1e7011d5719e995ef5db6099e1c314a6b9e7e91(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a0e4ea83e8dfb9e17ec0b41df8c6dc28f66fdd92ce87304f5947a45894a193a1(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a350faedfecd88a3bcd71ed7477376d3b593ae3ecd64dc1b36ef48fd3c62e52f(
    value: typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, DataDigitaloceanImagesFilter]
    ],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__21f7bca2197ba440ad619fa7c56adea00ccf1a7a8a96aef9683537553dcbfc7d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__9efeab7c252d0f02b5264b43b05bf83fdeb4c1dfbc4da6292256abd67e51a736(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__753650ede469b174cd644d2f26800c1fe784d46029431be2dc25d65cbb78cb69(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__c1af9ff097963916604ff4cfb0f9a6688455db59895dd2ea39b896b81b9eca8f(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__452afc4b54a385f465016c9f3dd775858fc2e19c56cb6f1c93db174e19ea80f9(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__51f77922e889ed18267e082d0c527e7cd95dacca5a308e88357df59b63663d38(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__67e2897eb08ad0b51be1d0247f682bda74b5eed8040f25b85e17aa819eae755d(
    value: typing.Optional[DataDigitaloceanImagesImages],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__6a0f731242dbca8d4221d8e62869aa01d74f40ce45d42cbe7222fc2f9279c410(
    *,
    key: builtins.str,
    direction: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__ffad1d5fbc96c21d5942088f0b5ab7d42f6e54234bf21eee9e87712863a2c0d8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__10539c12785ed26648f01e1fe9a6bb10545eb013b4d682f51a2de1df65d855fa(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__585e35c306676e9fb643aa818e7370893f98709456dfc92f81ac4f3d11f333b8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__8cf22e1da534ab846b1717ec39e190136e681592faa3867d9c2c4ec5635dcb15(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__4da69bcb8be1a31c4a1f9a31d71c3a288e26037285a2908ce236b9b01bd2269f(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d49120111fd39d07dd8da64b72804df786f0dc298c161f6d8431f889275b02b0(
    value: typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable, typing.List[DataDigitaloceanImagesSort]
        ]
    ],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__700dd5ee2f5a0fc273cddc1c31ba979f09ccd79472640ccfcab0594232c6436e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__5d6e70827217e81a618c0ba80df946a13389854f6fd234e57b178696dd1f2820(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__fc07f680a90757ca158f9145df874ce39a2f802b86e6502c77bf455f8e772b13(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__bfce7c3020669ae63382618486f675f19bb6724103659af86d8c4543a7e721af(
    value: typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, DataDigitaloceanImagesSort]
    ],
) -> None:
    """Type checking stubs"""
    pass
