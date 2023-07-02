"""
# `digitalocean_droplet`

Refer to the Terraform Registory for docs: [`digitalocean_droplet`](https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet).
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


class Droplet(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.droplet.Droplet",
):
    """Represents a {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet digitalocean_droplet}."""

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        image: builtins.str,
        name: builtins.str,
        size: builtins.str,
        backups: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        droplet_agent: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        graceful_shutdown: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        id: typing.Optional[builtins.str] = None,
        ipv6: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        ipv6_address: typing.Optional[builtins.str] = None,
        monitoring: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        private_networking: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        region: typing.Optional[builtins.str] = None,
        resize_disk: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        ssh_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[
            typing.Union["DropletTimeouts", typing.Dict[builtins.str, typing.Any]]
        ] = None,
        user_data: typing.Optional[builtins.str] = None,
        volume_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        vpc_uuid: typing.Optional[builtins.str] = None,
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
        """Create a new {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet digitalocean_droplet} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param image: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#image Droplet#image}.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#name Droplet#name}.
        :param size: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#size Droplet#size}.
        :param backups: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#backups Droplet#backups}.
        :param droplet_agent: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#droplet_agent Droplet#droplet_agent}.
        :param graceful_shutdown: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#graceful_shutdown Droplet#graceful_shutdown}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#id Droplet#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ipv6: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#ipv6 Droplet#ipv6}.
        :param ipv6_address: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#ipv6_address Droplet#ipv6_address}.
        :param monitoring: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#monitoring Droplet#monitoring}.
        :param private_networking: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#private_networking Droplet#private_networking}.
        :param region: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#region Droplet#region}.
        :param resize_disk: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#resize_disk Droplet#resize_disk}.
        :param ssh_keys: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#ssh_keys Droplet#ssh_keys}.
        :param tags: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#tags Droplet#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#timeouts Droplet#timeouts}
        :param user_data: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#user_data Droplet#user_data}.
        :param volume_ids: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#volume_ids Droplet#volume_ids}.
        :param vpc_uuid: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#vpc_uuid Droplet#vpc_uuid}.
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
                _typecheckingstub__825ebb5957d3077be5eaf63a86667764bcb6fee7c40c51593b73d9cfa3163b34
            )
            check_type(
                argname="argument scope", value=scope, expected_type=type_hints["scope"]
            )
            check_type(
                argname="argument id_", value=id_, expected_type=type_hints["id_"]
            )
        config = DropletConfig(
            image=image,
            name=name,
            size=size,
            backups=backups,
            droplet_agent=droplet_agent,
            graceful_shutdown=graceful_shutdown,
            id=id,
            ipv6=ipv6,
            ipv6_address=ipv6_address,
            monitoring=monitoring,
            private_networking=private_networking,
            region=region,
            resize_disk=resize_disk,
            ssh_keys=ssh_keys,
            tags=tags,
            timeouts=timeouts,
            user_data=user_data,
            volume_ids=volume_ids,
            vpc_uuid=vpc_uuid,
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
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param create: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#create Droplet#create}.
        :param delete: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#delete Droplet#delete}.
        :param update: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#update Droplet#update}.
        """
        value = DropletTimeouts(create=create, delete=delete, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetBackups")
    def reset_backups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackups", []))

    @jsii.member(jsii_name="resetDropletAgent")
    def reset_droplet_agent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDropletAgent", []))

    @jsii.member(jsii_name="resetGracefulShutdown")
    def reset_graceful_shutdown(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGracefulShutdown", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIpv6")
    def reset_ipv6(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpv6", []))

    @jsii.member(jsii_name="resetIpv6Address")
    def reset_ipv6_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpv6Address", []))

    @jsii.member(jsii_name="resetMonitoring")
    def reset_monitoring(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMonitoring", []))

    @jsii.member(jsii_name="resetPrivateNetworking")
    def reset_private_networking(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateNetworking", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetResizeDisk")
    def reset_resize_disk(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResizeDisk", []))

    @jsii.member(jsii_name="resetSshKeys")
    def reset_ssh_keys(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSshKeys", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetUserData")
    def reset_user_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserData", []))

    @jsii.member(jsii_name="resetVolumeIds")
    def reset_volume_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolumeIds", []))

    @jsii.member(jsii_name="resetVpcUuid")
    def reset_vpc_uuid(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpcUuid", []))

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
    @jsii.member(jsii_name="disk")
    def disk(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "disk"))

    @builtins.property
    @jsii.member(jsii_name="ipv4Address")
    def ipv4_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipv4Address"))

    @builtins.property
    @jsii.member(jsii_name="ipv4AddressPrivate")
    def ipv4_address_private(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipv4AddressPrivate"))

    @builtins.property
    @jsii.member(jsii_name="locked")
    def locked(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "locked"))

    @builtins.property
    @jsii.member(jsii_name="memory")
    def memory(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "memory"))

    @builtins.property
    @jsii.member(jsii_name="priceHourly")
    def price_hourly(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priceHourly"))

    @builtins.property
    @jsii.member(jsii_name="priceMonthly")
    def price_monthly(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priceMonthly"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "DropletTimeoutsOutputReference":
        return typing.cast("DropletTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="urn")
    def urn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "urn"))

    @builtins.property
    @jsii.member(jsii_name="vcpus")
    def vcpus(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "vcpus"))

    @builtins.property
    @jsii.member(jsii_name="backupsInput")
    def backups_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "backupsInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="dropletAgentInput")
    def droplet_agent_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "dropletAgentInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="gracefulShutdownInput")
    def graceful_shutdown_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "gracefulShutdownInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="imageInput")
    def image_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageInput"))

    @builtins.property
    @jsii.member(jsii_name="ipv6AddressInput")
    def ipv6_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "ipv6AddressInput")
        )

    @builtins.property
    @jsii.member(jsii_name="ipv6Input")
    def ipv6_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "ipv6Input"),
        )

    @builtins.property
    @jsii.member(jsii_name="monitoringInput")
    def monitoring_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "monitoringInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="privateNetworkingInput")
    def private_networking_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "privateNetworkingInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="resizeDiskInput")
    def resize_disk_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "resizeDiskInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="sizeInput")
    def size_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sizeInput"))

    @builtins.property
    @jsii.member(jsii_name="sshKeysInput")
    def ssh_keys_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(
            typing.Optional[typing.List[builtins.str]], jsii.get(self, "sshKeysInput")
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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, "DropletTimeouts"]]:
        return typing.cast(
            typing.Optional[
                typing.Union[_cdktf_9a9027ec.IResolvable, "DropletTimeouts"]
            ],
            jsii.get(self, "timeoutsInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="userDataInput")
    def user_data_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "userDataInput")
        )

    @builtins.property
    @jsii.member(jsii_name="volumeIdsInput")
    def volume_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(
            typing.Optional[typing.List[builtins.str]], jsii.get(self, "volumeIdsInput")
        )

    @builtins.property
    @jsii.member(jsii_name="vpcUuidInput")
    def vpc_uuid_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "vpcUuidInput")
        )

    @builtins.property
    @jsii.member(jsii_name="backups")
    def backups(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "backups"),
        )

    @backups.setter
    def backups(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__43a71278b993ce675f517a511f1bb2582c68662dad6a2de24bc4549a3b595f05
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "backups", value)

    @builtins.property
    @jsii.member(jsii_name="dropletAgent")
    def droplet_agent(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "dropletAgent"),
        )

    @droplet_agent.setter
    def droplet_agent(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__4ed694afd03aa17631506b42341a15082baceb2e0bd3021e6ef429795eadf2d5
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "dropletAgent", value)

    @builtins.property
    @jsii.member(jsii_name="gracefulShutdown")
    def graceful_shutdown(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "gracefulShutdown"),
        )

    @graceful_shutdown.setter
    def graceful_shutdown(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__3ec24c9cd5c6674df98d80eccf20abe9a947146a997ea764da459567f9abe9da
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "gracefulShutdown", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__7eec729e3a02b659372443cd4c1987633756e711273f6c01069962945f46741d
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="image")
    def image(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "image"))

    @image.setter
    def image(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__9fff91f4a262c2edd5b8195b0542672d1dd6fc72d6e22d84361a28562b7d3be0
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "image", value)

    @builtins.property
    @jsii.member(jsii_name="ipv6")
    def ipv6(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "ipv6"),
        )

    @ipv6.setter
    def ipv6(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__4686aa1628ed7a049dc5084ba5b2a2fd92fb0d7635d1f55c91401570ca652e66
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "ipv6", value)

    @builtins.property
    @jsii.member(jsii_name="ipv6Address")
    def ipv6_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipv6Address"))

    @ipv6_address.setter
    def ipv6_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__eb6bdbdd1266d0622895639eb65e29c1aa364de8d28b64ea05346eaf5cc36f9e
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "ipv6Address", value)

    @builtins.property
    @jsii.member(jsii_name="monitoring")
    def monitoring(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "monitoring"),
        )

    @monitoring.setter
    def monitoring(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__448f26d2b947c73b536a7df3987dd9287a1b89996b269e17dfdfa8d8a4265f5d
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "monitoring", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__ae3d070e64be835450aa5ef1dd0078a571c59524c83242a4d753779cc86edb74
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="privateNetworking")
    def private_networking(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "privateNetworking"),
        )

    @private_networking.setter
    def private_networking(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__a9ef50dc4640b2790bd8ecbbdaeb63a4ebca2007defce7fe2bb7c550020c997e
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "privateNetworking", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__a499f795e2efda4368ce014586693c9affaffac069297480a9f24d79f1d9a55a
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="resizeDisk")
    def resize_disk(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "resizeDisk"),
        )

    @resize_disk.setter
    def resize_disk(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__f1a1cb39b89d98d5ee5de06236a93c0dac515497cc3d9cd70580c2d600937538
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "resizeDisk", value)

    @builtins.property
    @jsii.member(jsii_name="size")
    def size(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "size"))

    @size.setter
    def size(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__2c2b9dfb24b38e01fb8a91975622665765ab7072c2d4b0110590b48a95dc8ed8
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "size", value)

    @builtins.property
    @jsii.member(jsii_name="sshKeys")
    def ssh_keys(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sshKeys"))

    @ssh_keys.setter
    def ssh_keys(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__3ad7a90002b08dc3c61db40fbd22415215343cbddc4e82bc0495f58eb069ca46
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "sshKeys", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__0df2032d98d0f4401df5cedcbda588c49f3d7100fac8a6a7153fd0752c82f633
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="userData")
    def user_data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userData"))

    @user_data.setter
    def user_data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__7c5bdbc764a628a66de91ab16e723c4b498de32624906eff8824c2667a2dbe0a
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "userData", value)

    @builtins.property
    @jsii.member(jsii_name="volumeIds")
    def volume_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "volumeIds"))

    @volume_ids.setter
    def volume_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__cee6fda74f7f578063d3668542d842c9bcc916ba05fa909268e88fcc012132a0
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "volumeIds", value)

    @builtins.property
    @jsii.member(jsii_name="vpcUuid")
    def vpc_uuid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcUuid"))

    @vpc_uuid.setter
    def vpc_uuid(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__ad5209dd1feb379352e5d01d2979d85737bc9da871a5b26e144086ac0d8e0dcb
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "vpcUuid", value)


@jsii.data_type(
    jsii_type="digitalocean.droplet.DropletConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "image": "image",
        "name": "name",
        "size": "size",
        "backups": "backups",
        "droplet_agent": "dropletAgent",
        "graceful_shutdown": "gracefulShutdown",
        "id": "id",
        "ipv6": "ipv6",
        "ipv6_address": "ipv6Address",
        "monitoring": "monitoring",
        "private_networking": "privateNetworking",
        "region": "region",
        "resize_disk": "resizeDisk",
        "ssh_keys": "sshKeys",
        "tags": "tags",
        "timeouts": "timeouts",
        "user_data": "userData",
        "volume_ids": "volumeIds",
        "vpc_uuid": "vpcUuid",
    },
)
class DropletConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        image: builtins.str,
        name: builtins.str,
        size: builtins.str,
        backups: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        droplet_agent: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        graceful_shutdown: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        id: typing.Optional[builtins.str] = None,
        ipv6: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        ipv6_address: typing.Optional[builtins.str] = None,
        monitoring: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        private_networking: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        region: typing.Optional[builtins.str] = None,
        resize_disk: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        ssh_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[
            typing.Union["DropletTimeouts", typing.Dict[builtins.str, typing.Any]]
        ] = None,
        user_data: typing.Optional[builtins.str] = None,
        volume_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        vpc_uuid: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param connection:
        :param count:
        :param depends_on:
        :param for_each:
        :param lifecycle:
        :param provider:
        :param provisioners:
        :param image: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#image Droplet#image}.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#name Droplet#name}.
        :param size: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#size Droplet#size}.
        :param backups: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#backups Droplet#backups}.
        :param droplet_agent: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#droplet_agent Droplet#droplet_agent}.
        :param graceful_shutdown: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#graceful_shutdown Droplet#graceful_shutdown}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#id Droplet#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ipv6: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#ipv6 Droplet#ipv6}.
        :param ipv6_address: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#ipv6_address Droplet#ipv6_address}.
        :param monitoring: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#monitoring Droplet#monitoring}.
        :param private_networking: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#private_networking Droplet#private_networking}.
        :param region: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#region Droplet#region}.
        :param resize_disk: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#resize_disk Droplet#resize_disk}.
        :param ssh_keys: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#ssh_keys Droplet#ssh_keys}.
        :param tags: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#tags Droplet#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#timeouts Droplet#timeouts}
        :param user_data: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#user_data Droplet#user_data}.
        :param volume_ids: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#volume_ids Droplet#volume_ids}.
        :param vpc_uuid: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#vpc_uuid Droplet#vpc_uuid}.
        """
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = DropletTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__7497c3c5aabade017e143d433ba6571587f3a52f1c938c80b75c21ceffeb891c
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
                argname="argument image", value=image, expected_type=type_hints["image"]
            )
            check_type(
                argname="argument name", value=name, expected_type=type_hints["name"]
            )
            check_type(
                argname="argument size", value=size, expected_type=type_hints["size"]
            )
            check_type(
                argname="argument backups",
                value=backups,
                expected_type=type_hints["backups"],
            )
            check_type(
                argname="argument droplet_agent",
                value=droplet_agent,
                expected_type=type_hints["droplet_agent"],
            )
            check_type(
                argname="argument graceful_shutdown",
                value=graceful_shutdown,
                expected_type=type_hints["graceful_shutdown"],
            )
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(
                argname="argument ipv6", value=ipv6, expected_type=type_hints["ipv6"]
            )
            check_type(
                argname="argument ipv6_address",
                value=ipv6_address,
                expected_type=type_hints["ipv6_address"],
            )
            check_type(
                argname="argument monitoring",
                value=monitoring,
                expected_type=type_hints["monitoring"],
            )
            check_type(
                argname="argument private_networking",
                value=private_networking,
                expected_type=type_hints["private_networking"],
            )
            check_type(
                argname="argument region",
                value=region,
                expected_type=type_hints["region"],
            )
            check_type(
                argname="argument resize_disk",
                value=resize_disk,
                expected_type=type_hints["resize_disk"],
            )
            check_type(
                argname="argument ssh_keys",
                value=ssh_keys,
                expected_type=type_hints["ssh_keys"],
            )
            check_type(
                argname="argument tags", value=tags, expected_type=type_hints["tags"]
            )
            check_type(
                argname="argument timeouts",
                value=timeouts,
                expected_type=type_hints["timeouts"],
            )
            check_type(
                argname="argument user_data",
                value=user_data,
                expected_type=type_hints["user_data"],
            )
            check_type(
                argname="argument volume_ids",
                value=volume_ids,
                expected_type=type_hints["volume_ids"],
            )
            check_type(
                argname="argument vpc_uuid",
                value=vpc_uuid,
                expected_type=type_hints["vpc_uuid"],
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "image": image,
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
        if backups is not None:
            self._values["backups"] = backups
        if droplet_agent is not None:
            self._values["droplet_agent"] = droplet_agent
        if graceful_shutdown is not None:
            self._values["graceful_shutdown"] = graceful_shutdown
        if id is not None:
            self._values["id"] = id
        if ipv6 is not None:
            self._values["ipv6"] = ipv6
        if ipv6_address is not None:
            self._values["ipv6_address"] = ipv6_address
        if monitoring is not None:
            self._values["monitoring"] = monitoring
        if private_networking is not None:
            self._values["private_networking"] = private_networking
        if region is not None:
            self._values["region"] = region
        if resize_disk is not None:
            self._values["resize_disk"] = resize_disk
        if ssh_keys is not None:
            self._values["ssh_keys"] = ssh_keys
        if tags is not None:
            self._values["tags"] = tags
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if user_data is not None:
            self._values["user_data"] = user_data
        if volume_ids is not None:
            self._values["volume_ids"] = volume_ids
        if vpc_uuid is not None:
            self._values["vpc_uuid"] = vpc_uuid

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
    def image(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#image Droplet#image}."""
        result = self._values.get("image")
        assert result is not None, "Required property 'image' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#name Droplet#name}."""
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def size(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#size Droplet#size}."""
        result = self._values.get("size")
        assert result is not None, "Required property 'size' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def backups(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#backups Droplet#backups}."""
        result = self._values.get("backups")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def droplet_agent(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#droplet_agent Droplet#droplet_agent}."""
        result = self._values.get("droplet_agent")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def graceful_shutdown(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#graceful_shutdown Droplet#graceful_shutdown}."""
        result = self._values.get("graceful_shutdown")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#id Droplet#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        """
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ipv6(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#ipv6 Droplet#ipv6}."""
        result = self._values.get("ipv6")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def ipv6_address(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#ipv6_address Droplet#ipv6_address}."""
        result = self._values.get("ipv6_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def monitoring(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#monitoring Droplet#monitoring}."""
        result = self._values.get("monitoring")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def private_networking(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#private_networking Droplet#private_networking}."""
        result = self._values.get("private_networking")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#region Droplet#region}."""
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resize_disk(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#resize_disk Droplet#resize_disk}."""
        result = self._values.get("resize_disk")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def ssh_keys(self) -> typing.Optional[typing.List[builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#ssh_keys Droplet#ssh_keys}."""
        result = self._values.get("ssh_keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#tags Droplet#tags}."""
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["DropletTimeouts"]:
        """timeouts block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#timeouts Droplet#timeouts}
        """
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["DropletTimeouts"], result)

    @builtins.property
    def user_data(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#user_data Droplet#user_data}."""
        result = self._values.get("user_data")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def volume_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#volume_ids Droplet#volume_ids}."""
        result = self._values.get("volume_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def vpc_uuid(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#vpc_uuid Droplet#vpc_uuid}."""
        result = self._values.get("vpc_uuid")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DropletConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="digitalocean.droplet.DropletTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class DropletTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param create: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#create Droplet#create}.
        :param delete: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#delete Droplet#delete}.
        :param update: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#update Droplet#update}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__4305c1ef1b2711fdbf65d83fcae4c83a7771a02b894bc4b256379292d0a251db
            )
            check_type(
                argname="argument create",
                value=create,
                expected_type=type_hints["create"],
            )
            check_type(
                argname="argument delete",
                value=delete,
                expected_type=type_hints["delete"],
            )
            check_type(
                argname="argument update",
                value=update,
                expected_type=type_hints["update"],
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#create Droplet#create}."""
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#delete Droplet#delete}."""
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/droplet#update Droplet#update}."""
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DropletTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DropletTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.droplet.DropletTimeoutsOutputReference",
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
                _typecheckingstub__649c42cd2054f1a5fa636bc647c95b7d397abee57fec02574a0dc4f18a965e2f
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

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="updateInput")
    def update_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updateInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__837f328e1d8dfc51d6a026ab52774ec8565c58c4788456880ef865c7b7a15649
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__36b27ed56f5601b588af258d90a8bea95c038016c48f31321e4ccfdc0a1a1b6e
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__9cabca426f54abdf05f2308ac92cab6d735293e3b87c7c94e5a1e6d1df3a2630
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DropletTimeouts]]:
        return typing.cast(
            typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DropletTimeouts]],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[
            typing.Union[_cdktf_9a9027ec.IResolvable, DropletTimeouts]
        ],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__72215bc371e04e1d0c15716b3c0bc5761e0a776330d5f68d8c7c6703722cf350
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


__all__ = [
    "Droplet",
    "DropletConfig",
    "DropletTimeouts",
    "DropletTimeoutsOutputReference",
]

publication.publish()


def _typecheckingstub__825ebb5957d3077be5eaf63a86667764bcb6fee7c40c51593b73d9cfa3163b34(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    image: builtins.str,
    name: builtins.str,
    size: builtins.str,
    backups: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    droplet_agent: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    graceful_shutdown: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    id: typing.Optional[builtins.str] = None,
    ipv6: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    ipv6_address: typing.Optional[builtins.str] = None,
    monitoring: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    private_networking: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    region: typing.Optional[builtins.str] = None,
    resize_disk: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    ssh_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    timeouts: typing.Optional[
        typing.Union[DropletTimeouts, typing.Dict[builtins.str, typing.Any]]
    ] = None,
    user_data: typing.Optional[builtins.str] = None,
    volume_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    vpc_uuid: typing.Optional[builtins.str] = None,
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


def _typecheckingstub__43a71278b993ce675f517a511f1bb2582c68662dad6a2de24bc4549a3b595f05(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__4ed694afd03aa17631506b42341a15082baceb2e0bd3021e6ef429795eadf2d5(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__3ec24c9cd5c6674df98d80eccf20abe9a947146a997ea764da459567f9abe9da(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__7eec729e3a02b659372443cd4c1987633756e711273f6c01069962945f46741d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__9fff91f4a262c2edd5b8195b0542672d1dd6fc72d6e22d84361a28562b7d3be0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__4686aa1628ed7a049dc5084ba5b2a2fd92fb0d7635d1f55c91401570ca652e66(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__eb6bdbdd1266d0622895639eb65e29c1aa364de8d28b64ea05346eaf5cc36f9e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__448f26d2b947c73b536a7df3987dd9287a1b89996b269e17dfdfa8d8a4265f5d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__ae3d070e64be835450aa5ef1dd0078a571c59524c83242a4d753779cc86edb74(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a9ef50dc4640b2790bd8ecbbdaeb63a4ebca2007defce7fe2bb7c550020c997e(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a499f795e2efda4368ce014586693c9affaffac069297480a9f24d79f1d9a55a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__f1a1cb39b89d98d5ee5de06236a93c0dac515497cc3d9cd70580c2d600937538(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__2c2b9dfb24b38e01fb8a91975622665765ab7072c2d4b0110590b48a95dc8ed8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__3ad7a90002b08dc3c61db40fbd22415215343cbddc4e82bc0495f58eb069ca46(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__0df2032d98d0f4401df5cedcbda588c49f3d7100fac8a6a7153fd0752c82f633(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__7c5bdbc764a628a66de91ab16e723c4b498de32624906eff8824c2667a2dbe0a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__cee6fda74f7f578063d3668542d842c9bcc916ba05fa909268e88fcc012132a0(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__ad5209dd1feb379352e5d01d2979d85737bc9da871a5b26e144086ac0d8e0dcb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__7497c3c5aabade017e143d433ba6571587f3a52f1c938c80b75c21ceffeb891c(
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
    image: builtins.str,
    name: builtins.str,
    size: builtins.str,
    backups: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    droplet_agent: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    graceful_shutdown: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    id: typing.Optional[builtins.str] = None,
    ipv6: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    ipv6_address: typing.Optional[builtins.str] = None,
    monitoring: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    private_networking: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    region: typing.Optional[builtins.str] = None,
    resize_disk: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    ssh_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    timeouts: typing.Optional[
        typing.Union[DropletTimeouts, typing.Dict[builtins.str, typing.Any]]
    ] = None,
    user_data: typing.Optional[builtins.str] = None,
    volume_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    vpc_uuid: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__4305c1ef1b2711fdbf65d83fcae4c83a7771a02b894bc4b256379292d0a251db(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__649c42cd2054f1a5fa636bc647c95b7d397abee57fec02574a0dc4f18a965e2f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__837f328e1d8dfc51d6a026ab52774ec8565c58c4788456880ef865c7b7a15649(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__36b27ed56f5601b588af258d90a8bea95c038016c48f31321e4ccfdc0a1a1b6e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__9cabca426f54abdf05f2308ac92cab6d735293e3b87c7c94e5a1e6d1df3a2630(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__72215bc371e04e1d0c15716b3c0bc5761e0a776330d5f68d8c7c6703722cf350(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DropletTimeouts]],
) -> None:
    """Type checking stubs"""
    pass
