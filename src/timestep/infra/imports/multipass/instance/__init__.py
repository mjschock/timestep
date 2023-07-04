"""
# `multipass_instance`

Refer to the Terraform Registory for docs: [`multipass_instance`](https://registry.terraform.io/providers/larstobi/multipass/1.4.2/docs/resources/instance).
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


class Instance(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="multipass.instance.Instance",
):
    """Represents a {@link https://registry.terraform.io/providers/larstobi/multipass/1.4.2/docs/resources/instance multipass_instance}."""

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        cloudinit_file: typing.Optional[builtins.str] = None,
        cpus: typing.Optional[jsii.Number] = None,
        disk: typing.Optional[builtins.str] = None,
        image: typing.Optional[builtins.str] = None,
        memory: typing.Optional[builtins.str] = None,
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
        """Create a new {@link https://registry.terraform.io/providers/larstobi/multipass/1.4.2/docs/resources/instance multipass_instance} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Name for the instance. If it is 'primary' (the configured primary instance name), the user's home directory is mounted inside the newly launched instance, in 'Home'. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/larstobi/multipass/1.4.2/docs/resources/instance#name Instance#name}
        :param cloudinit_file: Path to a user-data cloud-init configuration. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/larstobi/multipass/1.4.2/docs/resources/instance#cloudinit_file Instance#cloudinit_file}
        :param cpus: Number of CPUs to allocate. Minimum: 1, default: 1. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/larstobi/multipass/1.4.2/docs/resources/instance#cpus Instance#cpus}
        :param disk: Disk space to allocate. Positive integers, in KiB, MiB, GiB or TiB suffix. Minimum: 512MiB, default: 5GiB. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/larstobi/multipass/1.4.2/docs/resources/instance#disk Instance#disk}
        :param image: Optional image to launch. If omitted, then the default Ubuntu LTS will be used. can be either ‘release’ or ‘daily‘. If is omitted, ‘release’ will be used. can be a partial image hash or an Ubuntu release version, codename or alias. is a custom image URL that is in http://, https://, or file:// format. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/larstobi/multipass/1.4.2/docs/resources/instance#image Instance#image}
        :param memory: Amount of memory to allocate. Positive integers, in KiB, MiB, GiB or TiB suffix. Minimum: 128MiB, default: 1GiB. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/larstobi/multipass/1.4.2/docs/resources/instance#memory Instance#memory}
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
                _typecheckingstub__caab7dd612018262111b09a7437239a43d70df1bfe192c20b6cc1b1d41a9eb19
            )
            check_type(
                argname="argument scope", value=scope, expected_type=type_hints["scope"]
            )
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = InstanceConfig(
            name=name,
            cloudinit_file=cloudinit_file,
            cpus=cpus,
            disk=disk,
            image=image,
            memory=memory,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetCloudinitFile")
    def reset_cloudinit_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudinitFile", []))

    @jsii.member(jsii_name="resetCpus")
    def reset_cpus(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpus", []))

    @jsii.member(jsii_name="resetDisk")
    def reset_disk(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisk", []))

    @jsii.member(jsii_name="resetImage")
    def reset_image(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImage", []))

    @jsii.member(jsii_name="resetMemory")
    def reset_memory(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMemory", []))

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
    @jsii.member(jsii_name="cloudinitFileInput")
    def cloudinit_file_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "cloudinitFileInput")
        )

    @builtins.property
    @jsii.member(jsii_name="cpusInput")
    def cpus_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cpusInput"))

    @builtins.property
    @jsii.member(jsii_name="diskInput")
    def disk_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "diskInput"))

    @builtins.property
    @jsii.member(jsii_name="imageInput")
    def image_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageInput"))

    @builtins.property
    @jsii.member(jsii_name="memoryInput")
    def memory_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "memoryInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudinitFile")
    def cloudinit_file(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudinitFile"))

    @cloudinit_file.setter
    def cloudinit_file(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__62388f1e18e8fdd1e6e140d03892e8ae0526eaae939472079dd17b60f01d5964
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "cloudinitFile", value)

    @builtins.property
    @jsii.member(jsii_name="cpus")
    def cpus(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cpus"))

    @cpus.setter
    def cpus(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__3facc7f7d4cb46f91a06fea2d9e2eb20bb79cbc145691075fab47cc841ba2b2c
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "cpus", value)

    @builtins.property
    @jsii.member(jsii_name="disk")
    def disk(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "disk"))

    @disk.setter
    def disk(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__bdcedb549ba180183c1e2c9dbe4d938308dfb112b175a6aeb9e9bcaf9b784237
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "disk", value)

    @builtins.property
    @jsii.member(jsii_name="image")
    def image(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "image"))

    @image.setter
    def image(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__b8955771c0fee79d8192b21e63575d7acc3ce7a160102610301a66cace5a0dcb
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "image", value)

    @builtins.property
    @jsii.member(jsii_name="memory")
    def memory(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "memory"))

    @memory.setter
    def memory(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__10731eb2735bc488e3319b21efc3d3f3a3afd4393ee3ac6ea8106127f4f136c4
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "memory", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__ddd3de44c3b0642f34d1d76af5d1506b549aa7a10b3fff2aa03aa76056cdadb9
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="multipass.instance.InstanceConfig",
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
        "cloudinit_file": "cloudinitFile",
        "cpus": "cpus",
        "disk": "disk",
        "image": "image",
        "memory": "memory",
    },
)
class InstanceConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        cloudinit_file: typing.Optional[builtins.str] = None,
        cpus: typing.Optional[jsii.Number] = None,
        disk: typing.Optional[builtins.str] = None,
        image: typing.Optional[builtins.str] = None,
        memory: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param connection:
        :param count:
        :param depends_on:
        :param for_each:
        :param lifecycle:
        :param provider:
        :param provisioners:
        :param name: Name for the instance. If it is 'primary' (the configured primary instance name), the user's home directory is mounted inside the newly launched instance, in 'Home'. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/larstobi/multipass/1.4.2/docs/resources/instance#name Instance#name}
        :param cloudinit_file: Path to a user-data cloud-init configuration. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/larstobi/multipass/1.4.2/docs/resources/instance#cloudinit_file Instance#cloudinit_file}
        :param cpus: Number of CPUs to allocate. Minimum: 1, default: 1. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/larstobi/multipass/1.4.2/docs/resources/instance#cpus Instance#cpus}
        :param disk: Disk space to allocate. Positive integers, in KiB, MiB, GiB or TiB suffix. Minimum: 512MiB, default: 5GiB. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/larstobi/multipass/1.4.2/docs/resources/instance#disk Instance#disk}
        :param image: Optional image to launch. If omitted, then the default Ubuntu LTS will be used. can be either ‘release’ or ‘daily‘. If is omitted, ‘release’ will be used. can be a partial image hash or an Ubuntu release version, codename or alias. is a custom image URL that is in http://, https://, or file:// format. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/larstobi/multipass/1.4.2/docs/resources/instance#image Instance#image}
        :param memory: Amount of memory to allocate. Positive integers, in KiB, MiB, GiB or TiB suffix. Minimum: 128MiB, default: 1GiB. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/larstobi/multipass/1.4.2/docs/resources/instance#memory Instance#memory}
        """
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__5182833e234e9139c3c5f7092e7f09ed337a79bec09b6b7455d7ee47ad74298c
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
                argname="argument cloudinit_file",
                value=cloudinit_file,
                expected_type=type_hints["cloudinit_file"],
            )
            check_type(
                argname="argument cpus", value=cpus, expected_type=type_hints["cpus"]
            )
            check_type(
                argname="argument disk", value=disk, expected_type=type_hints["disk"]
            )
            check_type(
                argname="argument image", value=image, expected_type=type_hints["image"]
            )
            check_type(
                argname="argument memory",
                value=memory,
                expected_type=type_hints["memory"],
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
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
        if cloudinit_file is not None:
            self._values["cloudinit_file"] = cloudinit_file
        if cpus is not None:
            self._values["cpus"] = cpus
        if disk is not None:
            self._values["disk"] = disk
        if image is not None:
            self._values["image"] = image
        if memory is not None:
            self._values["memory"] = memory

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
        """Name for the instance.

        If it is 'primary' (the configured primary instance name), the user's home directory is mounted inside the newly launched instance, in 'Home'.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/larstobi/multipass/1.4.2/docs/resources/instance#name Instance#name}
        """
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cloudinit_file(self) -> typing.Optional[builtins.str]:
        """Path to a user-data cloud-init configuration.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/larstobi/multipass/1.4.2/docs/resources/instance#cloudinit_file Instance#cloudinit_file}
        """
        result = self._values.get("cloudinit_file")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cpus(self) -> typing.Optional[jsii.Number]:
        """Number of CPUs to allocate. Minimum: 1, default: 1.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/larstobi/multipass/1.4.2/docs/resources/instance#cpus Instance#cpus}
        """
        result = self._values.get("cpus")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def disk(self) -> typing.Optional[builtins.str]:
        """Disk space to allocate. Positive integers, in KiB, MiB, GiB or TiB suffix. Minimum: 512MiB, default: 5GiB.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/larstobi/multipass/1.4.2/docs/resources/instance#disk Instance#disk}
        """
        result = self._values.get("disk")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def image(self) -> typing.Optional[builtins.str]:
        """Optional image to launch.

        If omitted, then the default Ubuntu LTS will be used.  can be either ‘release’ or ‘daily‘. If  is omitted, ‘release’ will be used.  can be a partial image hash or an Ubuntu release version, codename or alias.  is a custom image URL that is in http://, https://, or file:// format.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/larstobi/multipass/1.4.2/docs/resources/instance#image Instance#image}
        """
        result = self._values.get("image")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def memory(self) -> typing.Optional[builtins.str]:
        """Amount of memory to allocate. Positive integers, in KiB, MiB, GiB or TiB suffix. Minimum: 128MiB, default: 1GiB.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/larstobi/multipass/1.4.2/docs/resources/instance#memory Instance#memory}
        """
        result = self._values.get("memory")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InstanceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Instance",
    "InstanceConfig",
]

publication.publish()


def _typecheckingstub__caab7dd612018262111b09a7437239a43d70df1bfe192c20b6cc1b1d41a9eb19(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    cloudinit_file: typing.Optional[builtins.str] = None,
    cpus: typing.Optional[jsii.Number] = None,
    disk: typing.Optional[builtins.str] = None,
    image: typing.Optional[builtins.str] = None,
    memory: typing.Optional[builtins.str] = None,
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


def _typecheckingstub__62388f1e18e8fdd1e6e140d03892e8ae0526eaae939472079dd17b60f01d5964(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__3facc7f7d4cb46f91a06fea2d9e2eb20bb79cbc145691075fab47cc841ba2b2c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__bdcedb549ba180183c1e2c9dbe4d938308dfb112b175a6aeb9e9bcaf9b784237(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__b8955771c0fee79d8192b21e63575d7acc3ce7a160102610301a66cace5a0dcb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__10731eb2735bc488e3319b21efc3d3f3a3afd4393ee3ac6ea8106127f4f136c4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__ddd3de44c3b0642f34d1d76af5d1506b549aa7a10b3fff2aa03aa76056cdadb9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__5182833e234e9139c3c5f7092e7f09ed337a79bec09b6b7455d7ee47ad74298c(
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
    cloudinit_file: typing.Optional[builtins.str] = None,
    cpus: typing.Optional[jsii.Number] = None,
    disk: typing.Optional[builtins.str] = None,
    image: typing.Optional[builtins.str] = None,
    memory: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
