"""
# `digitalocean_custom_image`

Refer to the Terraform Registory for docs: [`digitalocean_custom_image`](https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/custom_image).
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


class CustomImage(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.customImage.CustomImage",
):
    """Represents a {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/custom_image digitalocean_custom_image}."""

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        regions: typing.Sequence[builtins.str],
        url: builtins.str,
        description: typing.Optional[builtins.str] = None,
        distribution: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[
            typing.Union["CustomImageTimeouts", typing.Dict[builtins.str, typing.Any]]
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
        """Create a new {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/custom_image digitalocean_custom_image} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/custom_image#name CustomImage#name}.
        :param regions: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/custom_image#regions CustomImage#regions}.
        :param url: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/custom_image#url CustomImage#url}.
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/custom_image#description CustomImage#description}.
        :param distribution: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/custom_image#distribution CustomImage#distribution}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/custom_image#id CustomImage#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/custom_image#tags CustomImage#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/custom_image#timeouts CustomImage#timeouts}
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
                _typecheckingstub__171ebb31ace35519f92c7859d58c76e44b6ada6c1abd91f9e58361ad2bf66ab7
            )
            check_type(
                argname="argument scope", value=scope, expected_type=type_hints["scope"]
            )
            check_type(
                argname="argument id_", value=id_, expected_type=type_hints["id_"]
            )
        config = CustomImageConfig(
            name=name,
            regions=regions,
            url=url,
            description=description,
            distribution=distribution,
            id=id,
            tags=tags,
            timeouts=timeouts,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(self, *, create: typing.Optional[builtins.str] = None) -> None:
        """
        :param create: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/custom_image#create CustomImage#create}.
        """
        value = CustomImageTimeouts(create=create)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDistribution")
    def reset_distribution(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDistribution", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

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
    @jsii.member(jsii_name="createdAt")
    def created_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdAt"))

    @builtins.property
    @jsii.member(jsii_name="imageId")
    def image_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "imageId"))

    @builtins.property
    @jsii.member(jsii_name="minDiskSize")
    def min_disk_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minDiskSize"))

    @builtins.property
    @jsii.member(jsii_name="public")
    def public(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "public"))

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
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "CustomImageTimeoutsOutputReference":
        return typing.cast(
            "CustomImageTimeoutsOutputReference", jsii.get(self, "timeouts")
        )

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "descriptionInput")
        )

    @builtins.property
    @jsii.member(jsii_name="distributionInput")
    def distribution_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "distributionInput")
        )

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="regionsInput")
    def regions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(
            typing.Optional[typing.List[builtins.str]], jsii.get(self, "regionsInput")
        )

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(
            typing.Optional[typing.List[builtins.str]], jsii.get(self, "tagsInput")
        )

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, "CustomImageTimeouts"]
    ]:
        return typing.cast(
            typing.Optional[
                typing.Union[_cdktf_9a9027ec.IResolvable, "CustomImageTimeouts"]
            ],
            jsii.get(self, "timeoutsInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__66ff67b193d574e8841b9744fd2fd5b63a231eafbc0ac296057532246f6468ea
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="distribution")
    def distribution(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "distribution"))

    @distribution.setter
    def distribution(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__4e303e999db7efd94d5abf82e762c300f7421ed1b738feb49597e352907c07a0
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "distribution", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__a394675a7e7e350108c301a866c38c938f4f60dd7530e52ed1193d62511d0467
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__d2f937013b0a4e344c6aba2be81ffc7fa6d8d2cc2c9616a1e4fce599c51185cf
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="regions")
    def regions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "regions"))

    @regions.setter
    def regions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__6dfdcc36b0338e4d3bec28d58e1cef9abe37f9b96c2891c7f8a9d2ff3ab3b56f
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "regions", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__b49f0e7f49de955b2e0531b077f8485edf0d26990bfb6f89dc4a984c62120518
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__320d4b137ef800ddf42e6f76639d5554134b771a7d2706cd3809713ffd3f8fef
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "url", value)


@jsii.data_type(
    jsii_type="digitalocean.customImage.CustomImageConfig",
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
        "regions": "regions",
        "url": "url",
        "description": "description",
        "distribution": "distribution",
        "id": "id",
        "tags": "tags",
        "timeouts": "timeouts",
    },
)
class CustomImageConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        name: builtins.str,
        regions: typing.Sequence[builtins.str],
        url: builtins.str,
        description: typing.Optional[builtins.str] = None,
        distribution: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[
            typing.Union["CustomImageTimeouts", typing.Dict[builtins.str, typing.Any]]
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
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/custom_image#name CustomImage#name}.
        :param regions: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/custom_image#regions CustomImage#regions}.
        :param url: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/custom_image#url CustomImage#url}.
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/custom_image#description CustomImage#description}.
        :param distribution: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/custom_image#distribution CustomImage#distribution}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/custom_image#id CustomImage#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/custom_image#tags CustomImage#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/custom_image#timeouts CustomImage#timeouts}
        """
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = CustomImageTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__9c51f912819edabdb64612858cc05e5b010e7d50c1b3883918c1fbd85e650aa9
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
                argname="argument name", value=name, expected_type=type_hints["name"]
            )
            check_type(
                argname="argument regions",
                value=regions,
                expected_type=type_hints["regions"],
            )
            check_type(
                argname="argument url", value=url, expected_type=type_hints["url"]
            )
            check_type(
                argname="argument description",
                value=description,
                expected_type=type_hints["description"],
            )
            check_type(
                argname="argument distribution",
                value=distribution,
                expected_type=type_hints["distribution"],
            )
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(
                argname="argument tags", value=tags, expected_type=type_hints["tags"]
            )
            check_type(
                argname="argument timeouts",
                value=timeouts,
                expected_type=type_hints["timeouts"],
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "regions": regions,
            "url": url,
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
        if description is not None:
            self._values["description"] = description
        if distribution is not None:
            self._values["distribution"] = distribution
        if id is not None:
            self._values["id"] = id
        if tags is not None:
            self._values["tags"] = tags
        if timeouts is not None:
            self._values["timeouts"] = timeouts

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
    def name(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/custom_image#name CustomImage#name}."""
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def regions(self) -> typing.List[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/custom_image#regions CustomImage#regions}."""
        result = self._values.get("regions")
        assert result is not None, "Required property 'regions' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def url(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/custom_image#url CustomImage#url}."""
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/custom_image#description CustomImage#description}."""
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def distribution(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/custom_image#distribution CustomImage#distribution}."""
        result = self._values.get("distribution")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/custom_image#id CustomImage#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        """
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/custom_image#tags CustomImage#tags}."""
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["CustomImageTimeouts"]:
        """timeouts block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/custom_image#timeouts CustomImage#timeouts}
        """
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["CustomImageTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CustomImageConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="digitalocean.customImage.CustomImageTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create"},
)
class CustomImageTimeouts:
    def __init__(self, *, create: typing.Optional[builtins.str] = None) -> None:
        """
        :param create: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/custom_image#create CustomImage#create}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__eec6bd395a87dc2b5f6ae9ca9337c6f02a8f925c4bcfd06f1b6bf8584cdf175a
            )
            check_type(
                argname="argument create",
                value=create,
                expected_type=type_hints["create"],
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/custom_image#create CustomImage#create}."""
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CustomImageTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CustomImageTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.customImage.CustomImageTimeoutsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        """
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__a3336b2cb19b1a89cdab535801b44ba905701719a51ee4c3a0f43bb10d92860b
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
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__669a42062b5eda36db5aa7f65798850015608d6c50b18fed1208d541a95cc3bf
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, CustomImageTimeouts]
    ]:
        return typing.cast(
            typing.Optional[
                typing.Union[_cdktf_9a9027ec.IResolvable, CustomImageTimeouts]
            ],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[
            typing.Union[_cdktf_9a9027ec.IResolvable, CustomImageTimeouts]
        ],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__9b7cceaa2d793bd73f679ab256d5c5a3c89fc59525da0b457f626ad4c12ee312
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


__all__ = [
    "CustomImage",
    "CustomImageConfig",
    "CustomImageTimeouts",
    "CustomImageTimeoutsOutputReference",
]

publication.publish()


def _typecheckingstub__171ebb31ace35519f92c7859d58c76e44b6ada6c1abd91f9e58361ad2bf66ab7(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    regions: typing.Sequence[builtins.str],
    url: builtins.str,
    description: typing.Optional[builtins.str] = None,
    distribution: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    timeouts: typing.Optional[
        typing.Union[CustomImageTimeouts, typing.Dict[builtins.str, typing.Any]]
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


def _typecheckingstub__66ff67b193d574e8841b9744fd2fd5b63a231eafbc0ac296057532246f6468ea(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__4e303e999db7efd94d5abf82e762c300f7421ed1b738feb49597e352907c07a0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a394675a7e7e350108c301a866c38c938f4f60dd7530e52ed1193d62511d0467(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d2f937013b0a4e344c6aba2be81ffc7fa6d8d2cc2c9616a1e4fce599c51185cf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__6dfdcc36b0338e4d3bec28d58e1cef9abe37f9b96c2891c7f8a9d2ff3ab3b56f(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__b49f0e7f49de955b2e0531b077f8485edf0d26990bfb6f89dc4a984c62120518(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__320d4b137ef800ddf42e6f76639d5554134b771a7d2706cd3809713ffd3f8fef(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__9c51f912819edabdb64612858cc05e5b010e7d50c1b3883918c1fbd85e650aa9(
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
    name: builtins.str,
    regions: typing.Sequence[builtins.str],
    url: builtins.str,
    description: typing.Optional[builtins.str] = None,
    distribution: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    timeouts: typing.Optional[
        typing.Union[CustomImageTimeouts, typing.Dict[builtins.str, typing.Any]]
    ] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__eec6bd395a87dc2b5f6ae9ca9337c6f02a8f925c4bcfd06f1b6bf8584cdf175a(
    *,
    create: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a3336b2cb19b1a89cdab535801b44ba905701719a51ee4c3a0f43bb10d92860b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__669a42062b5eda36db5aa7f65798850015608d6c50b18fed1208d541a95cc3bf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__9b7cceaa2d793bd73f679ab256d5c5a3c89fc59525da0b457f626ad4c12ee312(
    value: typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, CustomImageTimeouts]
    ],
) -> None:
    """Type checking stubs"""
    pass
