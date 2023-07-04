"""
# `digitalocean_loadbalancer`

Refer to the Terraform Registory for docs: [`digitalocean_loadbalancer`](https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer).
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


class Loadbalancer(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.loadbalancer.Loadbalancer",
):
    """Represents a {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer digitalocean_loadbalancer}."""

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        forwarding_rule: typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.Sequence[
                typing.Union[
                    "LoadbalancerForwardingRule", typing.Dict[builtins.str, typing.Any]
                ]
            ],
        ],
        name: builtins.str,
        region: builtins.str,
        algorithm: typing.Optional[builtins.str] = None,
        disable_lets_encrypt_dns_records: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        droplet_ids: typing.Optional[typing.Sequence[jsii.Number]] = None,
        droplet_tag: typing.Optional[builtins.str] = None,
        enable_backend_keepalive: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        enable_proxy_protocol: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        firewall: typing.Optional[
            typing.Union["LoadbalancerFirewall", typing.Dict[builtins.str, typing.Any]]
        ] = None,
        healthcheck: typing.Optional[
            typing.Union[
                "LoadbalancerHealthcheck", typing.Dict[builtins.str, typing.Any]
            ]
        ] = None,
        http_idle_timeout_seconds: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        project_id: typing.Optional[builtins.str] = None,
        redirect_http_to_https: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        size: typing.Optional[builtins.str] = None,
        size_unit: typing.Optional[jsii.Number] = None,
        sticky_sessions: typing.Optional[
            typing.Union[
                "LoadbalancerStickySessions", typing.Dict[builtins.str, typing.Any]
            ]
        ] = None,
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
        """Create a new {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer digitalocean_loadbalancer} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param forwarding_rule: forwarding_rule block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#forwarding_rule Loadbalancer#forwarding_rule}
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#name Loadbalancer#name}.
        :param region: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#region Loadbalancer#region}.
        :param algorithm: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#algorithm Loadbalancer#algorithm}.
        :param disable_lets_encrypt_dns_records: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#disable_lets_encrypt_dns_records Loadbalancer#disable_lets_encrypt_dns_records}.
        :param droplet_ids: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#droplet_ids Loadbalancer#droplet_ids}.
        :param droplet_tag: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#droplet_tag Loadbalancer#droplet_tag}.
        :param enable_backend_keepalive: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#enable_backend_keepalive Loadbalancer#enable_backend_keepalive}.
        :param enable_proxy_protocol: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#enable_proxy_protocol Loadbalancer#enable_proxy_protocol}.
        :param firewall: firewall block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#firewall Loadbalancer#firewall}
        :param healthcheck: healthcheck block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#healthcheck Loadbalancer#healthcheck}
        :param http_idle_timeout_seconds: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#http_idle_timeout_seconds Loadbalancer#http_idle_timeout_seconds}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#id Loadbalancer#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param project_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#project_id Loadbalancer#project_id}.
        :param redirect_http_to_https: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#redirect_http_to_https Loadbalancer#redirect_http_to_https}.
        :param size: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#size Loadbalancer#size}.
        :param size_unit: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#size_unit Loadbalancer#size_unit}.
        :param sticky_sessions: sticky_sessions block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#sticky_sessions Loadbalancer#sticky_sessions}
        :param vpc_uuid: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#vpc_uuid Loadbalancer#vpc_uuid}.
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
                _typecheckingstub__d82ed87de19cd568fa86b7a7c77f2d004363f2161dc89018a7d94215882fd65a
            )
            check_type(
                argname="argument scope", value=scope, expected_type=type_hints["scope"]
            )
            check_type(
                argname="argument id_", value=id_, expected_type=type_hints["id_"]
            )
        config = LoadbalancerConfig(
            forwarding_rule=forwarding_rule,
            name=name,
            region=region,
            algorithm=algorithm,
            disable_lets_encrypt_dns_records=disable_lets_encrypt_dns_records,
            droplet_ids=droplet_ids,
            droplet_tag=droplet_tag,
            enable_backend_keepalive=enable_backend_keepalive,
            enable_proxy_protocol=enable_proxy_protocol,
            firewall=firewall,
            healthcheck=healthcheck,
            http_idle_timeout_seconds=http_idle_timeout_seconds,
            id=id,
            project_id=project_id,
            redirect_http_to_https=redirect_http_to_https,
            size=size,
            size_unit=size_unit,
            sticky_sessions=sticky_sessions,
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

    @jsii.member(jsii_name="putFirewall")
    def put_firewall(
        self,
        *,
        allow: typing.Optional[typing.Sequence[builtins.str]] = None,
        deny: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        """
        :param allow: the rules for ALLOWING traffic to the LB (strings in the form: 'ip:1.2.3.4' or 'cidr:1.2.0.0/16'). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#allow Loadbalancer#allow}
        :param deny: the rules for DENYING traffic to the LB (strings in the form: 'ip:1.2.3.4' or 'cidr:1.2.0.0/16'). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#deny Loadbalancer#deny}
        """
        value = LoadbalancerFirewall(allow=allow, deny=deny)

        return typing.cast(None, jsii.invoke(self, "putFirewall", [value]))

    @jsii.member(jsii_name="putForwardingRule")
    def put_forwarding_rule(
        self,
        value: typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.Sequence[
                typing.Union[
                    "LoadbalancerForwardingRule", typing.Dict[builtins.str, typing.Any]
                ]
            ],
        ],
    ) -> None:
        """
        :param value: -
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__bd5ed63e80ad541aa4586bfa44cd20fb3d628683cb3823fcd0e2ec837ef2e7d7
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        return typing.cast(None, jsii.invoke(self, "putForwardingRule", [value]))

    @jsii.member(jsii_name="putHealthcheck")
    def put_healthcheck(
        self,
        *,
        port: jsii.Number,
        protocol: builtins.str,
        check_interval_seconds: typing.Optional[jsii.Number] = None,
        healthy_threshold: typing.Optional[jsii.Number] = None,
        path: typing.Optional[builtins.str] = None,
        response_timeout_seconds: typing.Optional[jsii.Number] = None,
        unhealthy_threshold: typing.Optional[jsii.Number] = None,
    ) -> None:
        """
        :param port: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#port Loadbalancer#port}.
        :param protocol: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#protocol Loadbalancer#protocol}.
        :param check_interval_seconds: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#check_interval_seconds Loadbalancer#check_interval_seconds}.
        :param healthy_threshold: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#healthy_threshold Loadbalancer#healthy_threshold}.
        :param path: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#path Loadbalancer#path}.
        :param response_timeout_seconds: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#response_timeout_seconds Loadbalancer#response_timeout_seconds}.
        :param unhealthy_threshold: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#unhealthy_threshold Loadbalancer#unhealthy_threshold}.
        """
        value = LoadbalancerHealthcheck(
            port=port,
            protocol=protocol,
            check_interval_seconds=check_interval_seconds,
            healthy_threshold=healthy_threshold,
            path=path,
            response_timeout_seconds=response_timeout_seconds,
            unhealthy_threshold=unhealthy_threshold,
        )

        return typing.cast(None, jsii.invoke(self, "putHealthcheck", [value]))

    @jsii.member(jsii_name="putStickySessions")
    def put_sticky_sessions(
        self,
        *,
        cookie_name: typing.Optional[builtins.str] = None,
        cookie_ttl_seconds: typing.Optional[jsii.Number] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param cookie_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#cookie_name Loadbalancer#cookie_name}.
        :param cookie_ttl_seconds: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#cookie_ttl_seconds Loadbalancer#cookie_ttl_seconds}.
        :param type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#type Loadbalancer#type}.
        """
        value = LoadbalancerStickySessions(
            cookie_name=cookie_name, cookie_ttl_seconds=cookie_ttl_seconds, type=type
        )

        return typing.cast(None, jsii.invoke(self, "putStickySessions", [value]))

    @jsii.member(jsii_name="resetAlgorithm")
    def reset_algorithm(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlgorithm", []))

    @jsii.member(jsii_name="resetDisableLetsEncryptDnsRecords")
    def reset_disable_lets_encrypt_dns_records(self) -> None:
        return typing.cast(
            None, jsii.invoke(self, "resetDisableLetsEncryptDnsRecords", [])
        )

    @jsii.member(jsii_name="resetDropletIds")
    def reset_droplet_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDropletIds", []))

    @jsii.member(jsii_name="resetDropletTag")
    def reset_droplet_tag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDropletTag", []))

    @jsii.member(jsii_name="resetEnableBackendKeepalive")
    def reset_enable_backend_keepalive(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableBackendKeepalive", []))

    @jsii.member(jsii_name="resetEnableProxyProtocol")
    def reset_enable_proxy_protocol(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableProxyProtocol", []))

    @jsii.member(jsii_name="resetFirewall")
    def reset_firewall(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFirewall", []))

    @jsii.member(jsii_name="resetHealthcheck")
    def reset_healthcheck(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthcheck", []))

    @jsii.member(jsii_name="resetHttpIdleTimeoutSeconds")
    def reset_http_idle_timeout_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpIdleTimeoutSeconds", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetProjectId")
    def reset_project_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProjectId", []))

    @jsii.member(jsii_name="resetRedirectHttpToHttps")
    def reset_redirect_http_to_https(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedirectHttpToHttps", []))

    @jsii.member(jsii_name="resetSize")
    def reset_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSize", []))

    @jsii.member(jsii_name="resetSizeUnit")
    def reset_size_unit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSizeUnit", []))

    @jsii.member(jsii_name="resetStickySessions")
    def reset_sticky_sessions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStickySessions", []))

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
    @jsii.member(jsii_name="firewall")
    def firewall(self) -> "LoadbalancerFirewallOutputReference":
        return typing.cast(
            "LoadbalancerFirewallOutputReference", jsii.get(self, "firewall")
        )

    @builtins.property
    @jsii.member(jsii_name="forwardingRule")
    def forwarding_rule(self) -> "LoadbalancerForwardingRuleList":
        return typing.cast(
            "LoadbalancerForwardingRuleList", jsii.get(self, "forwardingRule")
        )

    @builtins.property
    @jsii.member(jsii_name="healthcheck")
    def healthcheck(self) -> "LoadbalancerHealthcheckOutputReference":
        return typing.cast(
            "LoadbalancerHealthcheckOutputReference", jsii.get(self, "healthcheck")
        )

    @builtins.property
    @jsii.member(jsii_name="ip")
    def ip(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ip"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="stickySessions")
    def sticky_sessions(self) -> "LoadbalancerStickySessionsOutputReference":
        return typing.cast(
            "LoadbalancerStickySessionsOutputReference",
            jsii.get(self, "stickySessions"),
        )

    @builtins.property
    @jsii.member(jsii_name="urn")
    def urn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "urn"))

    @builtins.property
    @jsii.member(jsii_name="algorithmInput")
    def algorithm_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "algorithmInput")
        )

    @builtins.property
    @jsii.member(jsii_name="disableLetsEncryptDnsRecordsInput")
    def disable_lets_encrypt_dns_records_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "disableLetsEncryptDnsRecordsInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="dropletIdsInput")
    def droplet_ids_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(
            typing.Optional[typing.List[jsii.Number]], jsii.get(self, "dropletIdsInput")
        )

    @builtins.property
    @jsii.member(jsii_name="dropletTagInput")
    def droplet_tag_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "dropletTagInput")
        )

    @builtins.property
    @jsii.member(jsii_name="enableBackendKeepaliveInput")
    def enable_backend_keepalive_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "enableBackendKeepaliveInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="enableProxyProtocolInput")
    def enable_proxy_protocol_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "enableProxyProtocolInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="firewallInput")
    def firewall_input(self) -> typing.Optional["LoadbalancerFirewall"]:
        return typing.cast(
            typing.Optional["LoadbalancerFirewall"], jsii.get(self, "firewallInput")
        )

    @builtins.property
    @jsii.member(jsii_name="forwardingRuleInput")
    def forwarding_rule_input(
        self,
    ) -> typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable, typing.List["LoadbalancerForwardingRule"]
        ]
    ]:
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.IResolvable,
                    typing.List["LoadbalancerForwardingRule"],
                ]
            ],
            jsii.get(self, "forwardingRuleInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="healthcheckInput")
    def healthcheck_input(self) -> typing.Optional["LoadbalancerHealthcheck"]:
        return typing.cast(
            typing.Optional["LoadbalancerHealthcheck"],
            jsii.get(self, "healthcheckInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="httpIdleTimeoutSecondsInput")
    def http_idle_timeout_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(
            typing.Optional[jsii.Number], jsii.get(self, "httpIdleTimeoutSecondsInput")
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
    @jsii.member(jsii_name="projectIdInput")
    def project_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "projectIdInput")
        )

    @builtins.property
    @jsii.member(jsii_name="redirectHttpToHttpsInput")
    def redirect_http_to_https_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "redirectHttpToHttpsInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="sizeInput")
    def size_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sizeInput"))

    @builtins.property
    @jsii.member(jsii_name="sizeUnitInput")
    def size_unit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(
            typing.Optional[jsii.Number], jsii.get(self, "sizeUnitInput")
        )

    @builtins.property
    @jsii.member(jsii_name="stickySessionsInput")
    def sticky_sessions_input(self) -> typing.Optional["LoadbalancerStickySessions"]:
        return typing.cast(
            typing.Optional["LoadbalancerStickySessions"],
            jsii.get(self, "stickySessionsInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="vpcUuidInput")
    def vpc_uuid_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "vpcUuidInput")
        )

    @builtins.property
    @jsii.member(jsii_name="algorithm")
    def algorithm(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "algorithm"))

    @algorithm.setter
    def algorithm(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__c1c029f9f9144f54bfe30e790c976fe43eecc41eff3a6d3e83b6ddc50c12c838
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "algorithm", value)

    @builtins.property
    @jsii.member(jsii_name="disableLetsEncryptDnsRecords")
    def disable_lets_encrypt_dns_records(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "disableLetsEncryptDnsRecords"),
        )

    @disable_lets_encrypt_dns_records.setter
    def disable_lets_encrypt_dns_records(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__cd7fa5eb679567b5c65e161cfc9e133a3cc4c766f93e77b394f918dd9ec3a03e
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "disableLetsEncryptDnsRecords", value)

    @builtins.property
    @jsii.member(jsii_name="dropletIds")
    def droplet_ids(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "dropletIds"))

    @droplet_ids.setter
    def droplet_ids(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__a14ccd6a7bf4182926c2dab1f19dde0f0fd78d8e208c2cb74bdf034ed9ee60a4
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "dropletIds", value)

    @builtins.property
    @jsii.member(jsii_name="dropletTag")
    def droplet_tag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dropletTag"))

    @droplet_tag.setter
    def droplet_tag(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__30c05211ff86d86212d65a5e3b9cd99fbc38f15ec0d5689d30948b0d95301825
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "dropletTag", value)

    @builtins.property
    @jsii.member(jsii_name="enableBackendKeepalive")
    def enable_backend_keepalive(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "enableBackendKeepalive"),
        )

    @enable_backend_keepalive.setter
    def enable_backend_keepalive(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__8c43a4ef1b4dc32529293bf9c78b0c8bfa3137a6b1d4aed486b09d429bb8b203
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "enableBackendKeepalive", value)

    @builtins.property
    @jsii.member(jsii_name="enableProxyProtocol")
    def enable_proxy_protocol(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "enableProxyProtocol"),
        )

    @enable_proxy_protocol.setter
    def enable_proxy_protocol(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__2749c5df1cf9936ba0120d1939f6758a23144d4e0fd8ab608c2b901896665097
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "enableProxyProtocol", value)

    @builtins.property
    @jsii.member(jsii_name="httpIdleTimeoutSeconds")
    def http_idle_timeout_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "httpIdleTimeoutSeconds"))

    @http_idle_timeout_seconds.setter
    def http_idle_timeout_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__38854568ba1a89df7336049a11a654ed185f4e4d7dd83b4e559216ccb14cb4f5
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "httpIdleTimeoutSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__1eea1476614f93b81045b47c159695d0aff9d15d8007d0ccf20d9e63bd236c59
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
                _typecheckingstub__1f90f1ea8d906af4f0c7899b1e25cb0cea34ae3a4714a72f83f61f8a7f0228f2
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="projectId")
    def project_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectId"))

    @project_id.setter
    def project_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__80df80ce962df4101523944187d78eeff94ea703a93151a89d2f1330f2357e7a
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "projectId", value)

    @builtins.property
    @jsii.member(jsii_name="redirectHttpToHttps")
    def redirect_http_to_https(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "redirectHttpToHttps"),
        )

    @redirect_http_to_https.setter
    def redirect_http_to_https(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__cfa6452309d95f576c219f628fff153f8644af860facdad9c3f5595f9c0ad172
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "redirectHttpToHttps", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__40c25fe85b541d52dda19c029091c00fe2ffb58fef01ecfff225779730d9abb0
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="size")
    def size(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "size"))

    @size.setter
    def size(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__1886136bfddb2515a79448878e1bb895d58940c56d191b6ad24b156c03ac5a86
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "size", value)

    @builtins.property
    @jsii.member(jsii_name="sizeUnit")
    def size_unit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sizeUnit"))

    @size_unit.setter
    def size_unit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__a9faa3634a9974e0ecf16806dea04b17caad32b3333f629317491c84f1d87a95
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "sizeUnit", value)

    @builtins.property
    @jsii.member(jsii_name="vpcUuid")
    def vpc_uuid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcUuid"))

    @vpc_uuid.setter
    def vpc_uuid(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__e732268b4195189339976d385f5e2f86c0a4d26f21f8683df6e5913a792cd409
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "vpcUuid", value)


@jsii.data_type(
    jsii_type="digitalocean.loadbalancer.LoadbalancerConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "forwarding_rule": "forwardingRule",
        "name": "name",
        "region": "region",
        "algorithm": "algorithm",
        "disable_lets_encrypt_dns_records": "disableLetsEncryptDnsRecords",
        "droplet_ids": "dropletIds",
        "droplet_tag": "dropletTag",
        "enable_backend_keepalive": "enableBackendKeepalive",
        "enable_proxy_protocol": "enableProxyProtocol",
        "firewall": "firewall",
        "healthcheck": "healthcheck",
        "http_idle_timeout_seconds": "httpIdleTimeoutSeconds",
        "id": "id",
        "project_id": "projectId",
        "redirect_http_to_https": "redirectHttpToHttps",
        "size": "size",
        "size_unit": "sizeUnit",
        "sticky_sessions": "stickySessions",
        "vpc_uuid": "vpcUuid",
    },
)
class LoadbalancerConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        forwarding_rule: typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.Sequence[
                typing.Union[
                    "LoadbalancerForwardingRule", typing.Dict[builtins.str, typing.Any]
                ]
            ],
        ],
        name: builtins.str,
        region: builtins.str,
        algorithm: typing.Optional[builtins.str] = None,
        disable_lets_encrypt_dns_records: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        droplet_ids: typing.Optional[typing.Sequence[jsii.Number]] = None,
        droplet_tag: typing.Optional[builtins.str] = None,
        enable_backend_keepalive: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        enable_proxy_protocol: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        firewall: typing.Optional[
            typing.Union["LoadbalancerFirewall", typing.Dict[builtins.str, typing.Any]]
        ] = None,
        healthcheck: typing.Optional[
            typing.Union[
                "LoadbalancerHealthcheck", typing.Dict[builtins.str, typing.Any]
            ]
        ] = None,
        http_idle_timeout_seconds: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        project_id: typing.Optional[builtins.str] = None,
        redirect_http_to_https: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        size: typing.Optional[builtins.str] = None,
        size_unit: typing.Optional[jsii.Number] = None,
        sticky_sessions: typing.Optional[
            typing.Union[
                "LoadbalancerStickySessions", typing.Dict[builtins.str, typing.Any]
            ]
        ] = None,
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
        :param forwarding_rule: forwarding_rule block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#forwarding_rule Loadbalancer#forwarding_rule}
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#name Loadbalancer#name}.
        :param region: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#region Loadbalancer#region}.
        :param algorithm: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#algorithm Loadbalancer#algorithm}.
        :param disable_lets_encrypt_dns_records: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#disable_lets_encrypt_dns_records Loadbalancer#disable_lets_encrypt_dns_records}.
        :param droplet_ids: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#droplet_ids Loadbalancer#droplet_ids}.
        :param droplet_tag: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#droplet_tag Loadbalancer#droplet_tag}.
        :param enable_backend_keepalive: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#enable_backend_keepalive Loadbalancer#enable_backend_keepalive}.
        :param enable_proxy_protocol: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#enable_proxy_protocol Loadbalancer#enable_proxy_protocol}.
        :param firewall: firewall block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#firewall Loadbalancer#firewall}
        :param healthcheck: healthcheck block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#healthcheck Loadbalancer#healthcheck}
        :param http_idle_timeout_seconds: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#http_idle_timeout_seconds Loadbalancer#http_idle_timeout_seconds}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#id Loadbalancer#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param project_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#project_id Loadbalancer#project_id}.
        :param redirect_http_to_https: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#redirect_http_to_https Loadbalancer#redirect_http_to_https}.
        :param size: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#size Loadbalancer#size}.
        :param size_unit: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#size_unit Loadbalancer#size_unit}.
        :param sticky_sessions: sticky_sessions block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#sticky_sessions Loadbalancer#sticky_sessions}
        :param vpc_uuid: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#vpc_uuid Loadbalancer#vpc_uuid}.
        """
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(firewall, dict):
            firewall = LoadbalancerFirewall(**firewall)
        if isinstance(healthcheck, dict):
            healthcheck = LoadbalancerHealthcheck(**healthcheck)
        if isinstance(sticky_sessions, dict):
            sticky_sessions = LoadbalancerStickySessions(**sticky_sessions)
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__7a389e8117824126a128605aa931389ac2c407fdb34b1dcf1b5f50b9db613817
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
                argname="argument forwarding_rule",
                value=forwarding_rule,
                expected_type=type_hints["forwarding_rule"],
            )
            check_type(
                argname="argument name", value=name, expected_type=type_hints["name"]
            )
            check_type(
                argname="argument region",
                value=region,
                expected_type=type_hints["region"],
            )
            check_type(
                argname="argument algorithm",
                value=algorithm,
                expected_type=type_hints["algorithm"],
            )
            check_type(
                argname="argument disable_lets_encrypt_dns_records",
                value=disable_lets_encrypt_dns_records,
                expected_type=type_hints["disable_lets_encrypt_dns_records"],
            )
            check_type(
                argname="argument droplet_ids",
                value=droplet_ids,
                expected_type=type_hints["droplet_ids"],
            )
            check_type(
                argname="argument droplet_tag",
                value=droplet_tag,
                expected_type=type_hints["droplet_tag"],
            )
            check_type(
                argname="argument enable_backend_keepalive",
                value=enable_backend_keepalive,
                expected_type=type_hints["enable_backend_keepalive"],
            )
            check_type(
                argname="argument enable_proxy_protocol",
                value=enable_proxy_protocol,
                expected_type=type_hints["enable_proxy_protocol"],
            )
            check_type(
                argname="argument firewall",
                value=firewall,
                expected_type=type_hints["firewall"],
            )
            check_type(
                argname="argument healthcheck",
                value=healthcheck,
                expected_type=type_hints["healthcheck"],
            )
            check_type(
                argname="argument http_idle_timeout_seconds",
                value=http_idle_timeout_seconds,
                expected_type=type_hints["http_idle_timeout_seconds"],
            )
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(
                argname="argument project_id",
                value=project_id,
                expected_type=type_hints["project_id"],
            )
            check_type(
                argname="argument redirect_http_to_https",
                value=redirect_http_to_https,
                expected_type=type_hints["redirect_http_to_https"],
            )
            check_type(
                argname="argument size", value=size, expected_type=type_hints["size"]
            )
            check_type(
                argname="argument size_unit",
                value=size_unit,
                expected_type=type_hints["size_unit"],
            )
            check_type(
                argname="argument sticky_sessions",
                value=sticky_sessions,
                expected_type=type_hints["sticky_sessions"],
            )
            check_type(
                argname="argument vpc_uuid",
                value=vpc_uuid,
                expected_type=type_hints["vpc_uuid"],
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "forwarding_rule": forwarding_rule,
            "name": name,
            "region": region,
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
        if algorithm is not None:
            self._values["algorithm"] = algorithm
        if disable_lets_encrypt_dns_records is not None:
            self._values[
                "disable_lets_encrypt_dns_records"
            ] = disable_lets_encrypt_dns_records
        if droplet_ids is not None:
            self._values["droplet_ids"] = droplet_ids
        if droplet_tag is not None:
            self._values["droplet_tag"] = droplet_tag
        if enable_backend_keepalive is not None:
            self._values["enable_backend_keepalive"] = enable_backend_keepalive
        if enable_proxy_protocol is not None:
            self._values["enable_proxy_protocol"] = enable_proxy_protocol
        if firewall is not None:
            self._values["firewall"] = firewall
        if healthcheck is not None:
            self._values["healthcheck"] = healthcheck
        if http_idle_timeout_seconds is not None:
            self._values["http_idle_timeout_seconds"] = http_idle_timeout_seconds
        if id is not None:
            self._values["id"] = id
        if project_id is not None:
            self._values["project_id"] = project_id
        if redirect_http_to_https is not None:
            self._values["redirect_http_to_https"] = redirect_http_to_https
        if size is not None:
            self._values["size"] = size
        if size_unit is not None:
            self._values["size_unit"] = size_unit
        if sticky_sessions is not None:
            self._values["sticky_sessions"] = sticky_sessions
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
    def forwarding_rule(
        self,
    ) -> typing.Union[
        _cdktf_9a9027ec.IResolvable, typing.List["LoadbalancerForwardingRule"]
    ]:
        """forwarding_rule block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#forwarding_rule Loadbalancer#forwarding_rule}
        """
        result = self._values.get("forwarding_rule")
        assert result is not None, "Required property 'forwarding_rule' is missing"
        return typing.cast(
            typing.Union[
                _cdktf_9a9027ec.IResolvable, typing.List["LoadbalancerForwardingRule"]
            ],
            result,
        )

    @builtins.property
    def name(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#name Loadbalancer#name}."""
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def region(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#region Loadbalancer#region}."""
        result = self._values.get("region")
        assert result is not None, "Required property 'region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def algorithm(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#algorithm Loadbalancer#algorithm}."""
        result = self._values.get("algorithm")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disable_lets_encrypt_dns_records(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#disable_lets_encrypt_dns_records Loadbalancer#disable_lets_encrypt_dns_records}."""
        result = self._values.get("disable_lets_encrypt_dns_records")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def droplet_ids(self) -> typing.Optional[typing.List[jsii.Number]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#droplet_ids Loadbalancer#droplet_ids}."""
        result = self._values.get("droplet_ids")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    @builtins.property
    def droplet_tag(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#droplet_tag Loadbalancer#droplet_tag}."""
        result = self._values.get("droplet_tag")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_backend_keepalive(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#enable_backend_keepalive Loadbalancer#enable_backend_keepalive}."""
        result = self._values.get("enable_backend_keepalive")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def enable_proxy_protocol(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#enable_proxy_protocol Loadbalancer#enable_proxy_protocol}."""
        result = self._values.get("enable_proxy_protocol")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def firewall(self) -> typing.Optional["LoadbalancerFirewall"]:
        """firewall block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#firewall Loadbalancer#firewall}
        """
        result = self._values.get("firewall")
        return typing.cast(typing.Optional["LoadbalancerFirewall"], result)

    @builtins.property
    def healthcheck(self) -> typing.Optional["LoadbalancerHealthcheck"]:
        """healthcheck block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#healthcheck Loadbalancer#healthcheck}
        """
        result = self._values.get("healthcheck")
        return typing.cast(typing.Optional["LoadbalancerHealthcheck"], result)

    @builtins.property
    def http_idle_timeout_seconds(self) -> typing.Optional[jsii.Number]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#http_idle_timeout_seconds Loadbalancer#http_idle_timeout_seconds}."""
        result = self._values.get("http_idle_timeout_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#id Loadbalancer#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        """
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project_id(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#project_id Loadbalancer#project_id}."""
        result = self._values.get("project_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def redirect_http_to_https(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#redirect_http_to_https Loadbalancer#redirect_http_to_https}."""
        result = self._values.get("redirect_http_to_https")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def size(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#size Loadbalancer#size}."""
        result = self._values.get("size")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def size_unit(self) -> typing.Optional[jsii.Number]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#size_unit Loadbalancer#size_unit}."""
        result = self._values.get("size_unit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def sticky_sessions(self) -> typing.Optional["LoadbalancerStickySessions"]:
        """sticky_sessions block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#sticky_sessions Loadbalancer#sticky_sessions}
        """
        result = self._values.get("sticky_sessions")
        return typing.cast(typing.Optional["LoadbalancerStickySessions"], result)

    @builtins.property
    def vpc_uuid(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#vpc_uuid Loadbalancer#vpc_uuid}."""
        result = self._values.get("vpc_uuid")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadbalancerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="digitalocean.loadbalancer.LoadbalancerFirewall",
    jsii_struct_bases=[],
    name_mapping={"allow": "allow", "deny": "deny"},
)
class LoadbalancerFirewall:
    def __init__(
        self,
        *,
        allow: typing.Optional[typing.Sequence[builtins.str]] = None,
        deny: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        """
        :param allow: the rules for ALLOWING traffic to the LB (strings in the form: 'ip:1.2.3.4' or 'cidr:1.2.0.0/16'). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#allow Loadbalancer#allow}
        :param deny: the rules for DENYING traffic to the LB (strings in the form: 'ip:1.2.3.4' or 'cidr:1.2.0.0/16'). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#deny Loadbalancer#deny}
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__00ed21c0e1bd0756b45c7fe039e3f606f1b577f2ee9146ca2e07122024d3a93f
            )
            check_type(
                argname="argument allow", value=allow, expected_type=type_hints["allow"]
            )
            check_type(
                argname="argument deny", value=deny, expected_type=type_hints["deny"]
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if allow is not None:
            self._values["allow"] = allow
        if deny is not None:
            self._values["deny"] = deny

    @builtins.property
    def allow(self) -> typing.Optional[typing.List[builtins.str]]:
        """the rules for ALLOWING traffic to the LB (strings in the form: 'ip:1.2.3.4' or 'cidr:1.2.0.0/16').

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#allow Loadbalancer#allow}
        """
        result = self._values.get("allow")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def deny(self) -> typing.Optional[typing.List[builtins.str]]:
        """the rules for DENYING traffic to the LB (strings in the form: 'ip:1.2.3.4' or 'cidr:1.2.0.0/16').

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#deny Loadbalancer#deny}
        """
        result = self._values.get("deny")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadbalancerFirewall(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LoadbalancerFirewallOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.loadbalancer.LoadbalancerFirewallOutputReference",
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
                _typecheckingstub__05c3853b713c0d72fa06bd0ac79eb8fa1a66c88f917b76f37b9cdfc55348914f
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

    @jsii.member(jsii_name="resetAllow")
    def reset_allow(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllow", []))

    @jsii.member(jsii_name="resetDeny")
    def reset_deny(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeny", []))

    @builtins.property
    @jsii.member(jsii_name="allowInput")
    def allow_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(
            typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowInput")
        )

    @builtins.property
    @jsii.member(jsii_name="denyInput")
    def deny_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(
            typing.Optional[typing.List[builtins.str]], jsii.get(self, "denyInput")
        )

    @builtins.property
    @jsii.member(jsii_name="allow")
    def allow(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allow"))

    @allow.setter
    def allow(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__a45ce8b02969776dac7a08582a85a83cd85a6b163080b203372501b673754263
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "allow", value)

    @builtins.property
    @jsii.member(jsii_name="deny")
    def deny(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "deny"))

    @deny.setter
    def deny(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__35a86fe57848a1807470bfcf2956510fff4ceb9badc02dfc71cb69b36b5e0228
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "deny", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LoadbalancerFirewall]:
        return typing.cast(
            typing.Optional[LoadbalancerFirewall], jsii.get(self, "internalValue")
        )

    @internal_value.setter
    def internal_value(self, value: typing.Optional[LoadbalancerFirewall]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__05812c22aadacc8b39c2062895788adcc77ac90af3d191869994c7c43a02cbc8
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="digitalocean.loadbalancer.LoadbalancerForwardingRule",
    jsii_struct_bases=[],
    name_mapping={
        "entry_port": "entryPort",
        "entry_protocol": "entryProtocol",
        "target_port": "targetPort",
        "target_protocol": "targetProtocol",
        "certificate_id": "certificateId",
        "certificate_name": "certificateName",
        "tls_passthrough": "tlsPassthrough",
    },
)
class LoadbalancerForwardingRule:
    def __init__(
        self,
        *,
        entry_port: jsii.Number,
        entry_protocol: builtins.str,
        target_port: jsii.Number,
        target_protocol: builtins.str,
        certificate_id: typing.Optional[builtins.str] = None,
        certificate_name: typing.Optional[builtins.str] = None,
        tls_passthrough: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
    ) -> None:
        """
        :param entry_port: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#entry_port Loadbalancer#entry_port}.
        :param entry_protocol: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#entry_protocol Loadbalancer#entry_protocol}.
        :param target_port: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#target_port Loadbalancer#target_port}.
        :param target_protocol: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#target_protocol Loadbalancer#target_protocol}.
        :param certificate_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#certificate_id Loadbalancer#certificate_id}.
        :param certificate_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#certificate_name Loadbalancer#certificate_name}.
        :param tls_passthrough: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#tls_passthrough Loadbalancer#tls_passthrough}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__2e9377f6c4c07d6d9e60069c276b3f6f0fdd89d9c124cd755252f181bb084b0e
            )
            check_type(
                argname="argument entry_port",
                value=entry_port,
                expected_type=type_hints["entry_port"],
            )
            check_type(
                argname="argument entry_protocol",
                value=entry_protocol,
                expected_type=type_hints["entry_protocol"],
            )
            check_type(
                argname="argument target_port",
                value=target_port,
                expected_type=type_hints["target_port"],
            )
            check_type(
                argname="argument target_protocol",
                value=target_protocol,
                expected_type=type_hints["target_protocol"],
            )
            check_type(
                argname="argument certificate_id",
                value=certificate_id,
                expected_type=type_hints["certificate_id"],
            )
            check_type(
                argname="argument certificate_name",
                value=certificate_name,
                expected_type=type_hints["certificate_name"],
            )
            check_type(
                argname="argument tls_passthrough",
                value=tls_passthrough,
                expected_type=type_hints["tls_passthrough"],
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "entry_port": entry_port,
            "entry_protocol": entry_protocol,
            "target_port": target_port,
            "target_protocol": target_protocol,
        }
        if certificate_id is not None:
            self._values["certificate_id"] = certificate_id
        if certificate_name is not None:
            self._values["certificate_name"] = certificate_name
        if tls_passthrough is not None:
            self._values["tls_passthrough"] = tls_passthrough

    @builtins.property
    def entry_port(self) -> jsii.Number:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#entry_port Loadbalancer#entry_port}."""
        result = self._values.get("entry_port")
        assert result is not None, "Required property 'entry_port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def entry_protocol(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#entry_protocol Loadbalancer#entry_protocol}."""
        result = self._values.get("entry_protocol")
        assert result is not None, "Required property 'entry_protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_port(self) -> jsii.Number:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#target_port Loadbalancer#target_port}."""
        result = self._values.get("target_port")
        assert result is not None, "Required property 'target_port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def target_protocol(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#target_protocol Loadbalancer#target_protocol}."""
        result = self._values.get("target_protocol")
        assert result is not None, "Required property 'target_protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def certificate_id(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#certificate_id Loadbalancer#certificate_id}."""
        result = self._values.get("certificate_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certificate_name(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#certificate_name Loadbalancer#certificate_name}."""
        result = self._values.get("certificate_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tls_passthrough(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#tls_passthrough Loadbalancer#tls_passthrough}."""
        result = self._values.get("tls_passthrough")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadbalancerForwardingRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LoadbalancerForwardingRuleList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.loadbalancer.LoadbalancerForwardingRuleList",
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
                _typecheckingstub__5f6017a09663b46c7e625e1d5315148fe9d59bae9601ca0113391d2ae656c0eb
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
    def get(self, index: jsii.Number) -> "LoadbalancerForwardingRuleOutputReference":
        """
        :param index: the index of the item to return.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__0ce68658c444dd7e080dca91beebcf4214b2818b028149835f74eec5e05b654d
            )
            check_type(
                argname="argument index", value=index, expected_type=type_hints["index"]
            )
        return typing.cast(
            "LoadbalancerForwardingRuleOutputReference",
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
                _typecheckingstub__9e552ae2b695402ad0ba2462273bc5073fbd4999995912c867a499c8d9126cfa
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
                _typecheckingstub__5633b61b7885f540edecce29716fa8fe2236a5030be297a28ef9c0afc71d4424
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
                _typecheckingstub__43d015209e8410808e75aa0a7c4eb31c9825057d885412d2a8080a78b45693c7
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
            _cdktf_9a9027ec.IResolvable, typing.List[LoadbalancerForwardingRule]
        ]
    ]:
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.IResolvable, typing.List[LoadbalancerForwardingRule]
                ]
            ],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[
            typing.Union[
                _cdktf_9a9027ec.IResolvable, typing.List[LoadbalancerForwardingRule]
            ]
        ],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__c5e3db522fd9a0b5f2968d9f8c947be0b16937f28aa2f068b5d99641e4dba06e
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


class LoadbalancerForwardingRuleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.loadbalancer.LoadbalancerForwardingRuleOutputReference",
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
                _typecheckingstub__b19ab6d46c426bacbd097869fe10bb45a7c3756ea53cedb4d884911fa535ec36
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

    @jsii.member(jsii_name="resetCertificateId")
    def reset_certificate_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificateId", []))

    @jsii.member(jsii_name="resetCertificateName")
    def reset_certificate_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificateName", []))

    @jsii.member(jsii_name="resetTlsPassthrough")
    def reset_tls_passthrough(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTlsPassthrough", []))

    @builtins.property
    @jsii.member(jsii_name="certificateIdInput")
    def certificate_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "certificateIdInput")
        )

    @builtins.property
    @jsii.member(jsii_name="certificateNameInput")
    def certificate_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "certificateNameInput")
        )

    @builtins.property
    @jsii.member(jsii_name="entryPortInput")
    def entry_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(
            typing.Optional[jsii.Number], jsii.get(self, "entryPortInput")
        )

    @builtins.property
    @jsii.member(jsii_name="entryProtocolInput")
    def entry_protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "entryProtocolInput")
        )

    @builtins.property
    @jsii.member(jsii_name="targetPortInput")
    def target_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(
            typing.Optional[jsii.Number], jsii.get(self, "targetPortInput")
        )

    @builtins.property
    @jsii.member(jsii_name="targetProtocolInput")
    def target_protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "targetProtocolInput")
        )

    @builtins.property
    @jsii.member(jsii_name="tlsPassthroughInput")
    def tls_passthrough_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "tlsPassthroughInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="certificateId")
    def certificate_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateId"))

    @certificate_id.setter
    def certificate_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__8b83f227f0ea6de501ab2e2d0f1eba948062e5134a135bb23779392b682aaac6
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "certificateId", value)

    @builtins.property
    @jsii.member(jsii_name="certificateName")
    def certificate_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateName"))

    @certificate_name.setter
    def certificate_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__281cc866675e9e7ab4fc5894d5c9999a884063ea592192ff49a94bbebe66810a
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "certificateName", value)

    @builtins.property
    @jsii.member(jsii_name="entryPort")
    def entry_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "entryPort"))

    @entry_port.setter
    def entry_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__e7cf1b04ad8430839613284d5de8faa0c630c03e099ebc48dd902bed29d0039f
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "entryPort", value)

    @builtins.property
    @jsii.member(jsii_name="entryProtocol")
    def entry_protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "entryProtocol"))

    @entry_protocol.setter
    def entry_protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__5e396d26f1d3699b2ce0ca38027dd28f1a90ba2945a62052565e7933b196df86
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "entryProtocol", value)

    @builtins.property
    @jsii.member(jsii_name="targetPort")
    def target_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "targetPort"))

    @target_port.setter
    def target_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__5c1b6c114ebeb1c4516e22f4fdb457246b1c696e8da3a0e3c5246c659c111a9b
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "targetPort", value)

    @builtins.property
    @jsii.member(jsii_name="targetProtocol")
    def target_protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetProtocol"))

    @target_protocol.setter
    def target_protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__c2771b2c16b125f913e20a71a6919cc779a65cd16328b5ce820ab16496784515
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "targetProtocol", value)

    @builtins.property
    @jsii.member(jsii_name="tlsPassthrough")
    def tls_passthrough(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "tlsPassthrough"),
        )

    @tls_passthrough.setter
    def tls_passthrough(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__a39141ee49fb1c0a0c4dd968891459d0fc980db758c0a65abe6b6f211d556af2
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "tlsPassthrough", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, LoadbalancerForwardingRule]
    ]:
        return typing.cast(
            typing.Optional[
                typing.Union[_cdktf_9a9027ec.IResolvable, LoadbalancerForwardingRule]
            ],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[
            typing.Union[_cdktf_9a9027ec.IResolvable, LoadbalancerForwardingRule]
        ],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__d11e8dbe8e55335fc0f097866a26dac6ab78b0f35ac1f4baf398d3ca203c9b88
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="digitalocean.loadbalancer.LoadbalancerHealthcheck",
    jsii_struct_bases=[],
    name_mapping={
        "port": "port",
        "protocol": "protocol",
        "check_interval_seconds": "checkIntervalSeconds",
        "healthy_threshold": "healthyThreshold",
        "path": "path",
        "response_timeout_seconds": "responseTimeoutSeconds",
        "unhealthy_threshold": "unhealthyThreshold",
    },
)
class LoadbalancerHealthcheck:
    def __init__(
        self,
        *,
        port: jsii.Number,
        protocol: builtins.str,
        check_interval_seconds: typing.Optional[jsii.Number] = None,
        healthy_threshold: typing.Optional[jsii.Number] = None,
        path: typing.Optional[builtins.str] = None,
        response_timeout_seconds: typing.Optional[jsii.Number] = None,
        unhealthy_threshold: typing.Optional[jsii.Number] = None,
    ) -> None:
        """
        :param port: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#port Loadbalancer#port}.
        :param protocol: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#protocol Loadbalancer#protocol}.
        :param check_interval_seconds: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#check_interval_seconds Loadbalancer#check_interval_seconds}.
        :param healthy_threshold: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#healthy_threshold Loadbalancer#healthy_threshold}.
        :param path: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#path Loadbalancer#path}.
        :param response_timeout_seconds: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#response_timeout_seconds Loadbalancer#response_timeout_seconds}.
        :param unhealthy_threshold: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#unhealthy_threshold Loadbalancer#unhealthy_threshold}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__64504b692dda95eed7845261f1b9facf73722d01c05d20ef6a8b36b61e5f5c64
            )
            check_type(
                argname="argument port", value=port, expected_type=type_hints["port"]
            )
            check_type(
                argname="argument protocol",
                value=protocol,
                expected_type=type_hints["protocol"],
            )
            check_type(
                argname="argument check_interval_seconds",
                value=check_interval_seconds,
                expected_type=type_hints["check_interval_seconds"],
            )
            check_type(
                argname="argument healthy_threshold",
                value=healthy_threshold,
                expected_type=type_hints["healthy_threshold"],
            )
            check_type(
                argname="argument path", value=path, expected_type=type_hints["path"]
            )
            check_type(
                argname="argument response_timeout_seconds",
                value=response_timeout_seconds,
                expected_type=type_hints["response_timeout_seconds"],
            )
            check_type(
                argname="argument unhealthy_threshold",
                value=unhealthy_threshold,
                expected_type=type_hints["unhealthy_threshold"],
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "port": port,
            "protocol": protocol,
        }
        if check_interval_seconds is not None:
            self._values["check_interval_seconds"] = check_interval_seconds
        if healthy_threshold is not None:
            self._values["healthy_threshold"] = healthy_threshold
        if path is not None:
            self._values["path"] = path
        if response_timeout_seconds is not None:
            self._values["response_timeout_seconds"] = response_timeout_seconds
        if unhealthy_threshold is not None:
            self._values["unhealthy_threshold"] = unhealthy_threshold

    @builtins.property
    def port(self) -> jsii.Number:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#port Loadbalancer#port}."""
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def protocol(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#protocol Loadbalancer#protocol}."""
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def check_interval_seconds(self) -> typing.Optional[jsii.Number]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#check_interval_seconds Loadbalancer#check_interval_seconds}."""
        result = self._values.get("check_interval_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def healthy_threshold(self) -> typing.Optional[jsii.Number]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#healthy_threshold Loadbalancer#healthy_threshold}."""
        result = self._values.get("healthy_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#path Loadbalancer#path}."""
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def response_timeout_seconds(self) -> typing.Optional[jsii.Number]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#response_timeout_seconds Loadbalancer#response_timeout_seconds}."""
        result = self._values.get("response_timeout_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def unhealthy_threshold(self) -> typing.Optional[jsii.Number]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#unhealthy_threshold Loadbalancer#unhealthy_threshold}."""
        result = self._values.get("unhealthy_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadbalancerHealthcheck(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LoadbalancerHealthcheckOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.loadbalancer.LoadbalancerHealthcheckOutputReference",
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
                _typecheckingstub__6bd498549ea82a744f8d6a4ba508146b7f0d76fe03d9f5937327b1653bfadf37
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

    @jsii.member(jsii_name="resetCheckIntervalSeconds")
    def reset_check_interval_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCheckIntervalSeconds", []))

    @jsii.member(jsii_name="resetHealthyThreshold")
    def reset_healthy_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthyThreshold", []))

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @jsii.member(jsii_name="resetResponseTimeoutSeconds")
    def reset_response_timeout_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponseTimeoutSeconds", []))

    @jsii.member(jsii_name="resetUnhealthyThreshold")
    def reset_unhealthy_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUnhealthyThreshold", []))

    @builtins.property
    @jsii.member(jsii_name="checkIntervalSecondsInput")
    def check_interval_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(
            typing.Optional[jsii.Number], jsii.get(self, "checkIntervalSecondsInput")
        )

    @builtins.property
    @jsii.member(jsii_name="healthyThresholdInput")
    def healthy_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(
            typing.Optional[jsii.Number], jsii.get(self, "healthyThresholdInput")
        )

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "protocolInput")
        )

    @builtins.property
    @jsii.member(jsii_name="responseTimeoutSecondsInput")
    def response_timeout_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(
            typing.Optional[jsii.Number], jsii.get(self, "responseTimeoutSecondsInput")
        )

    @builtins.property
    @jsii.member(jsii_name="unhealthyThresholdInput")
    def unhealthy_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(
            typing.Optional[jsii.Number], jsii.get(self, "unhealthyThresholdInput")
        )

    @builtins.property
    @jsii.member(jsii_name="checkIntervalSeconds")
    def check_interval_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "checkIntervalSeconds"))

    @check_interval_seconds.setter
    def check_interval_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__4b210f25788a55cabc1a2a04685d969e75cd46eb69d08b1e886684fb488b7c1e
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "checkIntervalSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="healthyThreshold")
    def healthy_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "healthyThreshold"))

    @healthy_threshold.setter
    def healthy_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__7b0772cc78ae1531552c3b9f85a4130698ba8391189dee79145e3738a5887952
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "healthyThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__dcd9c17556a083a30f888c431e0b5d5146bab1c0376ea7af54f0f3c51003dc25
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__b46d9ba8b5c66458bbb5e2728aff206bac3eaf2da300f58d591449538fd59100
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__8b0853b1fb5b1070a1b91550be0bbcea7135b27f899d73434f9a7624a04cb5de
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="responseTimeoutSeconds")
    def response_timeout_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "responseTimeoutSeconds"))

    @response_timeout_seconds.setter
    def response_timeout_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__a37706e15433feec6c726cf30fcc499c4c84173b1c14b37d4842ffc94a950a85
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "responseTimeoutSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="unhealthyThreshold")
    def unhealthy_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "unhealthyThreshold"))

    @unhealthy_threshold.setter
    def unhealthy_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__15fd1b724b91001f21ea9759ec37801f7a8d095ef2a09190f40391b221cfa29f
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "unhealthyThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LoadbalancerHealthcheck]:
        return typing.cast(
            typing.Optional[LoadbalancerHealthcheck], jsii.get(self, "internalValue")
        )

    @internal_value.setter
    def internal_value(self, value: typing.Optional[LoadbalancerHealthcheck]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__af39177c9f0a88b630d3d5d4411b05067a832b384b4acda5320a9fbd1d6c2d2b
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="digitalocean.loadbalancer.LoadbalancerStickySessions",
    jsii_struct_bases=[],
    name_mapping={
        "cookie_name": "cookieName",
        "cookie_ttl_seconds": "cookieTtlSeconds",
        "type": "type",
    },
)
class LoadbalancerStickySessions:
    def __init__(
        self,
        *,
        cookie_name: typing.Optional[builtins.str] = None,
        cookie_ttl_seconds: typing.Optional[jsii.Number] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param cookie_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#cookie_name Loadbalancer#cookie_name}.
        :param cookie_ttl_seconds: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#cookie_ttl_seconds Loadbalancer#cookie_ttl_seconds}.
        :param type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#type Loadbalancer#type}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__ffab55ce7a8f0940933f8fd8bcabf9a168ea90f7230834276bd9ab8c52407a81
            )
            check_type(
                argname="argument cookie_name",
                value=cookie_name,
                expected_type=type_hints["cookie_name"],
            )
            check_type(
                argname="argument cookie_ttl_seconds",
                value=cookie_ttl_seconds,
                expected_type=type_hints["cookie_ttl_seconds"],
            )
            check_type(
                argname="argument type", value=type, expected_type=type_hints["type"]
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cookie_name is not None:
            self._values["cookie_name"] = cookie_name
        if cookie_ttl_seconds is not None:
            self._values["cookie_ttl_seconds"] = cookie_ttl_seconds
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def cookie_name(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#cookie_name Loadbalancer#cookie_name}."""
        result = self._values.get("cookie_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cookie_ttl_seconds(self) -> typing.Optional[jsii.Number]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#cookie_ttl_seconds Loadbalancer#cookie_ttl_seconds}."""
        result = self._values.get("cookie_ttl_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.28.1/docs/resources/loadbalancer#type Loadbalancer#type}."""
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadbalancerStickySessions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LoadbalancerStickySessionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.loadbalancer.LoadbalancerStickySessionsOutputReference",
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
                _typecheckingstub__0e9a5b16f1e4af28bcf738149af1c8a8ebce4feab90eb6a823c247890906093b
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

    @jsii.member(jsii_name="resetCookieName")
    def reset_cookie_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCookieName", []))

    @jsii.member(jsii_name="resetCookieTtlSeconds")
    def reset_cookie_ttl_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCookieTtlSeconds", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="cookieNameInput")
    def cookie_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "cookieNameInput")
        )

    @builtins.property
    @jsii.member(jsii_name="cookieTtlSecondsInput")
    def cookie_ttl_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(
            typing.Optional[jsii.Number], jsii.get(self, "cookieTtlSecondsInput")
        )

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="cookieName")
    def cookie_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cookieName"))

    @cookie_name.setter
    def cookie_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__d80a6e8a14cd0c6e477f3e4cb9986b62fbd7b8fd900f4d240f15fc3c4a0ca956
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "cookieName", value)

    @builtins.property
    @jsii.member(jsii_name="cookieTtlSeconds")
    def cookie_ttl_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cookieTtlSeconds"))

    @cookie_ttl_seconds.setter
    def cookie_ttl_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__c81a0a960cedb4c9b147031753573c97a4e694b28767e7dae143fa9917344e19
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "cookieTtlSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__e6f97ba96bfb50ee36aab0399c4b057db5d9d76a30b4e24226d0d9cbfff03f21
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LoadbalancerStickySessions]:
        return typing.cast(
            typing.Optional[LoadbalancerStickySessions], jsii.get(self, "internalValue")
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LoadbalancerStickySessions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__53c13bf05d772d6142e4109bbbba8b6f84108d51ed1c6d287e3abb04833438b7
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


__all__ = [
    "Loadbalancer",
    "LoadbalancerConfig",
    "LoadbalancerFirewall",
    "LoadbalancerFirewallOutputReference",
    "LoadbalancerForwardingRule",
    "LoadbalancerForwardingRuleList",
    "LoadbalancerForwardingRuleOutputReference",
    "LoadbalancerHealthcheck",
    "LoadbalancerHealthcheckOutputReference",
    "LoadbalancerStickySessions",
    "LoadbalancerStickySessionsOutputReference",
]

publication.publish()


def _typecheckingstub__d82ed87de19cd568fa86b7a7c77f2d004363f2161dc89018a7d94215882fd65a(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    forwarding_rule: typing.Union[
        _cdktf_9a9027ec.IResolvable,
        typing.Sequence[
            typing.Union[
                LoadbalancerForwardingRule, typing.Dict[builtins.str, typing.Any]
            ]
        ],
    ],
    name: builtins.str,
    region: builtins.str,
    algorithm: typing.Optional[builtins.str] = None,
    disable_lets_encrypt_dns_records: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    droplet_ids: typing.Optional[typing.Sequence[jsii.Number]] = None,
    droplet_tag: typing.Optional[builtins.str] = None,
    enable_backend_keepalive: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    enable_proxy_protocol: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    firewall: typing.Optional[
        typing.Union[LoadbalancerFirewall, typing.Dict[builtins.str, typing.Any]]
    ] = None,
    healthcheck: typing.Optional[
        typing.Union[LoadbalancerHealthcheck, typing.Dict[builtins.str, typing.Any]]
    ] = None,
    http_idle_timeout_seconds: typing.Optional[jsii.Number] = None,
    id: typing.Optional[builtins.str] = None,
    project_id: typing.Optional[builtins.str] = None,
    redirect_http_to_https: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    size: typing.Optional[builtins.str] = None,
    size_unit: typing.Optional[jsii.Number] = None,
    sticky_sessions: typing.Optional[
        typing.Union[LoadbalancerStickySessions, typing.Dict[builtins.str, typing.Any]]
    ] = None,
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


def _typecheckingstub__bd5ed63e80ad541aa4586bfa44cd20fb3d628683cb3823fcd0e2ec837ef2e7d7(
    value: typing.Union[
        _cdktf_9a9027ec.IResolvable,
        typing.Sequence[
            typing.Union[
                LoadbalancerForwardingRule, typing.Dict[builtins.str, typing.Any]
            ]
        ],
    ],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__c1c029f9f9144f54bfe30e790c976fe43eecc41eff3a6d3e83b6ddc50c12c838(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__cd7fa5eb679567b5c65e161cfc9e133a3cc4c766f93e77b394f918dd9ec3a03e(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a14ccd6a7bf4182926c2dab1f19dde0f0fd78d8e208c2cb74bdf034ed9ee60a4(
    value: typing.List[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__30c05211ff86d86212d65a5e3b9cd99fbc38f15ec0d5689d30948b0d95301825(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__8c43a4ef1b4dc32529293bf9c78b0c8bfa3137a6b1d4aed486b09d429bb8b203(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__2749c5df1cf9936ba0120d1939f6758a23144d4e0fd8ab608c2b901896665097(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__38854568ba1a89df7336049a11a654ed185f4e4d7dd83b4e559216ccb14cb4f5(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__1eea1476614f93b81045b47c159695d0aff9d15d8007d0ccf20d9e63bd236c59(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__1f90f1ea8d906af4f0c7899b1e25cb0cea34ae3a4714a72f83f61f8a7f0228f2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__80df80ce962df4101523944187d78eeff94ea703a93151a89d2f1330f2357e7a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__cfa6452309d95f576c219f628fff153f8644af860facdad9c3f5595f9c0ad172(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__40c25fe85b541d52dda19c029091c00fe2ffb58fef01ecfff225779730d9abb0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__1886136bfddb2515a79448878e1bb895d58940c56d191b6ad24b156c03ac5a86(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a9faa3634a9974e0ecf16806dea04b17caad32b3333f629317491c84f1d87a95(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__e732268b4195189339976d385f5e2f86c0a4d26f21f8683df6e5913a792cd409(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__7a389e8117824126a128605aa931389ac2c407fdb34b1dcf1b5f50b9db613817(
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
    forwarding_rule: typing.Union[
        _cdktf_9a9027ec.IResolvable,
        typing.Sequence[
            typing.Union[
                LoadbalancerForwardingRule, typing.Dict[builtins.str, typing.Any]
            ]
        ],
    ],
    name: builtins.str,
    region: builtins.str,
    algorithm: typing.Optional[builtins.str] = None,
    disable_lets_encrypt_dns_records: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    droplet_ids: typing.Optional[typing.Sequence[jsii.Number]] = None,
    droplet_tag: typing.Optional[builtins.str] = None,
    enable_backend_keepalive: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    enable_proxy_protocol: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    firewall: typing.Optional[
        typing.Union[LoadbalancerFirewall, typing.Dict[builtins.str, typing.Any]]
    ] = None,
    healthcheck: typing.Optional[
        typing.Union[LoadbalancerHealthcheck, typing.Dict[builtins.str, typing.Any]]
    ] = None,
    http_idle_timeout_seconds: typing.Optional[jsii.Number] = None,
    id: typing.Optional[builtins.str] = None,
    project_id: typing.Optional[builtins.str] = None,
    redirect_http_to_https: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    size: typing.Optional[builtins.str] = None,
    size_unit: typing.Optional[jsii.Number] = None,
    sticky_sessions: typing.Optional[
        typing.Union[LoadbalancerStickySessions, typing.Dict[builtins.str, typing.Any]]
    ] = None,
    vpc_uuid: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__00ed21c0e1bd0756b45c7fe039e3f606f1b577f2ee9146ca2e07122024d3a93f(
    *,
    allow: typing.Optional[typing.Sequence[builtins.str]] = None,
    deny: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__05c3853b713c0d72fa06bd0ac79eb8fa1a66c88f917b76f37b9cdfc55348914f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a45ce8b02969776dac7a08582a85a83cd85a6b163080b203372501b673754263(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__35a86fe57848a1807470bfcf2956510fff4ceb9badc02dfc71cb69b36b5e0228(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__05812c22aadacc8b39c2062895788adcc77ac90af3d191869994c7c43a02cbc8(
    value: typing.Optional[LoadbalancerFirewall],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__2e9377f6c4c07d6d9e60069c276b3f6f0fdd89d9c124cd755252f181bb084b0e(
    *,
    entry_port: jsii.Number,
    entry_protocol: builtins.str,
    target_port: jsii.Number,
    target_protocol: builtins.str,
    certificate_id: typing.Optional[builtins.str] = None,
    certificate_name: typing.Optional[builtins.str] = None,
    tls_passthrough: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__5f6017a09663b46c7e625e1d5315148fe9d59bae9601ca0113391d2ae656c0eb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__0ce68658c444dd7e080dca91beebcf4214b2818b028149835f74eec5e05b654d(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__9e552ae2b695402ad0ba2462273bc5073fbd4999995912c867a499c8d9126cfa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__5633b61b7885f540edecce29716fa8fe2236a5030be297a28ef9c0afc71d4424(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__43d015209e8410808e75aa0a7c4eb31c9825057d885412d2a8080a78b45693c7(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__c5e3db522fd9a0b5f2968d9f8c947be0b16937f28aa2f068b5d99641e4dba06e(
    value: typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable, typing.List[LoadbalancerForwardingRule]
        ]
    ],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__b19ab6d46c426bacbd097869fe10bb45a7c3756ea53cedb4d884911fa535ec36(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__8b83f227f0ea6de501ab2e2d0f1eba948062e5134a135bb23779392b682aaac6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__281cc866675e9e7ab4fc5894d5c9999a884063ea592192ff49a94bbebe66810a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__e7cf1b04ad8430839613284d5de8faa0c630c03e099ebc48dd902bed29d0039f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__5e396d26f1d3699b2ce0ca38027dd28f1a90ba2945a62052565e7933b196df86(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__5c1b6c114ebeb1c4516e22f4fdb457246b1c696e8da3a0e3c5246c659c111a9b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__c2771b2c16b125f913e20a71a6919cc779a65cd16328b5ce820ab16496784515(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a39141ee49fb1c0a0c4dd968891459d0fc980db758c0a65abe6b6f211d556af2(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d11e8dbe8e55335fc0f097866a26dac6ab78b0f35ac1f4baf398d3ca203c9b88(
    value: typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, LoadbalancerForwardingRule]
    ],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__64504b692dda95eed7845261f1b9facf73722d01c05d20ef6a8b36b61e5f5c64(
    *,
    port: jsii.Number,
    protocol: builtins.str,
    check_interval_seconds: typing.Optional[jsii.Number] = None,
    healthy_threshold: typing.Optional[jsii.Number] = None,
    path: typing.Optional[builtins.str] = None,
    response_timeout_seconds: typing.Optional[jsii.Number] = None,
    unhealthy_threshold: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__6bd498549ea82a744f8d6a4ba508146b7f0d76fe03d9f5937327b1653bfadf37(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__4b210f25788a55cabc1a2a04685d969e75cd46eb69d08b1e886684fb488b7c1e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__7b0772cc78ae1531552c3b9f85a4130698ba8391189dee79145e3738a5887952(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__dcd9c17556a083a30f888c431e0b5d5146bab1c0376ea7af54f0f3c51003dc25(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__b46d9ba8b5c66458bbb5e2728aff206bac3eaf2da300f58d591449538fd59100(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__8b0853b1fb5b1070a1b91550be0bbcea7135b27f899d73434f9a7624a04cb5de(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a37706e15433feec6c726cf30fcc499c4c84173b1c14b37d4842ffc94a950a85(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__15fd1b724b91001f21ea9759ec37801f7a8d095ef2a09190f40391b221cfa29f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__af39177c9f0a88b630d3d5d4411b05067a832b384b4acda5320a9fbd1d6c2d2b(
    value: typing.Optional[LoadbalancerHealthcheck],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__ffab55ce7a8f0940933f8fd8bcabf9a168ea90f7230834276bd9ab8c52407a81(
    *,
    cookie_name: typing.Optional[builtins.str] = None,
    cookie_ttl_seconds: typing.Optional[jsii.Number] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__0e9a5b16f1e4af28bcf738149af1c8a8ebce4feab90eb6a823c247890906093b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d80a6e8a14cd0c6e477f3e4cb9986b62fbd7b8fd900f4d240f15fc3c4a0ca956(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__c81a0a960cedb4c9b147031753573c97a4e694b28767e7dae143fa9917344e19(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__e6f97ba96bfb50ee36aab0399c4b057db5d9d76a30b4e24226d0d9cbfff03f21(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__53c13bf05d772d6142e4109bbbba8b6f84108d51ed1c6d287e3abb04833438b7(
    value: typing.Optional[LoadbalancerStickySessions],
) -> None:
    """Type checking stubs"""
    pass
