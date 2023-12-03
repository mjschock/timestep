'''
# `provider`

Refer to the Terraform Registory for docs: [`argocd`](https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs).
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


class ArgocdProvider(
    _cdktf_9a9027ec.TerraformProvider,
    metaclass=jsii.JSIIMeta,
    jsii_type="argocd.provider.ArgocdProvider",
):
    '''Represents a {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs argocd}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        alias: typing.Optional[builtins.str] = None,
        auth_token: typing.Optional[builtins.str] = None,
        cert_file: typing.Optional[builtins.str] = None,
        client_cert_file: typing.Optional[builtins.str] = None,
        client_cert_key: typing.Optional[builtins.str] = None,
        config_path: typing.Optional[builtins.str] = None,
        context: typing.Optional[builtins.str] = None,
        core: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        grpc_web: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        grpc_web_root_path: typing.Optional[builtins.str] = None,
        headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        insecure: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        kubernetes: typing.Optional[typing.Union["ArgocdProviderKubernetes", typing.Dict[builtins.str, typing.Any]]] = None,
        password: typing.Optional[builtins.str] = None,
        plain_text: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        port_forward: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        port_forward_with_namespace: typing.Optional[builtins.str] = None,
        server_addr: typing.Optional[builtins.str] = None,
        use_local_config: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        user_agent: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs argocd} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param alias: Alias name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#alias ArgocdProvider#alias}
        :param auth_token: ArgoCD authentication token, takes precedence over ``username``/``password``. Can be set through the ``ARGOCD_AUTH_TOKEN`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#auth_token ArgocdProvider#auth_token}
        :param cert_file: Additional root CA certificates file to add to the client TLS connection pool. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#cert_file ArgocdProvider#cert_file}
        :param client_cert_file: Client certificate. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#client_cert_file ArgocdProvider#client_cert_file}
        :param client_cert_key: Client certificate key. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#client_cert_key ArgocdProvider#client_cert_key}
        :param config_path: Override the default config path of ``$HOME/.config/argocd/config``. Only relevant when ``use_local_config``. Can be set through the ``ARGOCD_CONFIG_PATH`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#config_path ArgocdProvider#config_path}
        :param context: Context to choose when using a local ArgoCD config file. Only relevant when ``use_local_config``. Can be set through ``ARGOCD_CONTEXT`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#context ArgocdProvider#context}
        :param core: Configure direct access using Kubernetes API server. **Warning**: this feature works by starting a local ArgoCD API server that talks directly to the Kubernetes API using the **current context in the default kubeconfig** (``~/.kube/config``). This behavior cannot be overridden using either environment variables or the ``kubernetes`` block in the provider configuration at present). If the server fails to start (e.g. your kubeconfig is misconfigured) then the provider will fail as a result of the ``argocd`` module forcing it to exit and no logs will be available to help you debug this. The error message will be similar to .. epigraph:: ``The plugin encountered an error, and failed to respond to the plugin.(*GRPCProvider).ReadResource call. The plugin logs may contain more details.`` To debug this, you will need to login via the ArgoCD CLI using ``argocd login --core`` and then running an operation. E.g. ``argocd app list``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#core ArgocdProvider#core}
        :param grpc_web: Whether to use gRPC web proxy client. Useful if Argo CD server is behind proxy which does not support HTTP2. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#grpc_web ArgocdProvider#grpc_web}
        :param grpc_web_root_path: Use the gRPC web proxy client and set the web root, e.g. ``argo-cd``. Useful if the Argo CD server is behind a proxy at a non-root path. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#grpc_web_root_path ArgocdProvider#grpc_web_root_path}
        :param headers: Additional headers to add to each request to the ArgoCD server. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#headers ArgocdProvider#headers}
        :param insecure: Whether to skip TLS server certificate. Can be set through the ``ARGOCD_INSECURE`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#insecure ArgocdProvider#insecure}
        :param kubernetes: kubernetes block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#kubernetes ArgocdProvider#kubernetes}
        :param password: Authentication password. Can be set through the ``ARGOCD_AUTH_PASSWORD`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#password ArgocdProvider#password}
        :param plain_text: Whether to initiate an unencrypted connection to ArgoCD server. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#plain_text ArgocdProvider#plain_text}
        :param port_forward: Connect to a random argocd-server port using port forwarding. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#port_forward ArgocdProvider#port_forward}
        :param port_forward_with_namespace: Namespace name which should be used for port forwarding. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#port_forward_with_namespace ArgocdProvider#port_forward_with_namespace}
        :param server_addr: ArgoCD server address with port. Can be set through the ``ARGOCD_SERVER`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#server_addr ArgocdProvider#server_addr}
        :param use_local_config: Use the authentication settings found in the local config file. Useful when you have previously logged in using SSO. Conflicts with ``auth_token``, ``username`` and ``password``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#use_local_config ArgocdProvider#use_local_config}
        :param user_agent: User-Agent request header override. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#user_agent ArgocdProvider#user_agent}
        :param username: Authentication username. Can be set through the ``ARGOCD_AUTH_USERNAME`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#username ArgocdProvider#username}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c57d8a28e881a142bb69356638ceb10d3b1607e24458dcd505f7289c5110f4a9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = ArgocdProviderConfig(
            alias=alias,
            auth_token=auth_token,
            cert_file=cert_file,
            client_cert_file=client_cert_file,
            client_cert_key=client_cert_key,
            config_path=config_path,
            context=context,
            core=core,
            grpc_web=grpc_web,
            grpc_web_root_path=grpc_web_root_path,
            headers=headers,
            insecure=insecure,
            kubernetes=kubernetes,
            password=password,
            plain_text=plain_text,
            port_forward=port_forward,
            port_forward_with_namespace=port_forward_with_namespace,
            server_addr=server_addr,
            use_local_config=use_local_config,
            user_agent=user_agent,
            username=username,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="generateConfigForImport")
    @builtins.classmethod
    def generate_config_for_import(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        import_to_id: builtins.str,
        import_from_id: builtins.str,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    ) -> _cdktf_9a9027ec.ImportableResource:
        '''Generates CDKTF code for importing a ArgocdProvider resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the ArgocdProvider to import.
        :param import_from_id: The id of the existing ArgocdProvider that should be imported. Refer to the {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the ArgocdProvider to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b37044febe27eff1c07a066aa2a746199ec8d133a57e81e340a4ef5277ec00b4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="resetAlias")
    def reset_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlias", []))

    @jsii.member(jsii_name="resetAuthToken")
    def reset_auth_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthToken", []))

    @jsii.member(jsii_name="resetCertFile")
    def reset_cert_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertFile", []))

    @jsii.member(jsii_name="resetClientCertFile")
    def reset_client_cert_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientCertFile", []))

    @jsii.member(jsii_name="resetClientCertKey")
    def reset_client_cert_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientCertKey", []))

    @jsii.member(jsii_name="resetConfigPath")
    def reset_config_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfigPath", []))

    @jsii.member(jsii_name="resetContext")
    def reset_context(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContext", []))

    @jsii.member(jsii_name="resetCore")
    def reset_core(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCore", []))

    @jsii.member(jsii_name="resetGrpcWeb")
    def reset_grpc_web(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGrpcWeb", []))

    @jsii.member(jsii_name="resetGrpcWebRootPath")
    def reset_grpc_web_root_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGrpcWebRootPath", []))

    @jsii.member(jsii_name="resetHeaders")
    def reset_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeaders", []))

    @jsii.member(jsii_name="resetInsecure")
    def reset_insecure(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInsecure", []))

    @jsii.member(jsii_name="resetKubernetes")
    def reset_kubernetes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKubernetes", []))

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetPlainText")
    def reset_plain_text(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlainText", []))

    @jsii.member(jsii_name="resetPortForward")
    def reset_port_forward(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPortForward", []))

    @jsii.member(jsii_name="resetPortForwardWithNamespace")
    def reset_port_forward_with_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPortForwardWithNamespace", []))

    @jsii.member(jsii_name="resetServerAddr")
    def reset_server_addr(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServerAddr", []))

    @jsii.member(jsii_name="resetUseLocalConfig")
    def reset_use_local_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseLocalConfig", []))

    @jsii.member(jsii_name="resetUserAgent")
    def reset_user_agent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserAgent", []))

    @jsii.member(jsii_name="resetUsername")
    def reset_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsername", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="aliasInput")
    def alias_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aliasInput"))

    @builtins.property
    @jsii.member(jsii_name="authTokenInput")
    def auth_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="certFileInput")
    def cert_file_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certFileInput"))

    @builtins.property
    @jsii.member(jsii_name="clientCertFileInput")
    def client_cert_file_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientCertFileInput"))

    @builtins.property
    @jsii.member(jsii_name="clientCertKeyInput")
    def client_cert_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientCertKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="configPathInput")
    def config_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configPathInput"))

    @builtins.property
    @jsii.member(jsii_name="contextInput")
    def context_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contextInput"))

    @builtins.property
    @jsii.member(jsii_name="coreInput")
    def core_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "coreInput"))

    @builtins.property
    @jsii.member(jsii_name="grpcWebInput")
    def grpc_web_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "grpcWebInput"))

    @builtins.property
    @jsii.member(jsii_name="grpcWebRootPathInput")
    def grpc_web_root_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "grpcWebRootPathInput"))

    @builtins.property
    @jsii.member(jsii_name="headersInput")
    def headers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "headersInput"))

    @builtins.property
    @jsii.member(jsii_name="insecureInput")
    def insecure_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "insecureInput"))

    @builtins.property
    @jsii.member(jsii_name="kubernetesInput")
    def kubernetes_input(self) -> typing.Optional["ArgocdProviderKubernetes"]:
        return typing.cast(typing.Optional["ArgocdProviderKubernetes"], jsii.get(self, "kubernetesInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="plainTextInput")
    def plain_text_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "plainTextInput"))

    @builtins.property
    @jsii.member(jsii_name="portForwardInput")
    def port_forward_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "portForwardInput"))

    @builtins.property
    @jsii.member(jsii_name="portForwardWithNamespaceInput")
    def port_forward_with_namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "portForwardWithNamespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="serverAddrInput")
    def server_addr_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverAddrInput"))

    @builtins.property
    @jsii.member(jsii_name="useLocalConfigInput")
    def use_local_config_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "useLocalConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="userAgentInput")
    def user_agent_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userAgentInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="alias")
    def alias(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alias"))

    @alias.setter
    def alias(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba74c87f557e2d5b5fbe9608a07b667beb094853e4f8ce1714abc94b6f63daaa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alias", value)

    @builtins.property
    @jsii.member(jsii_name="authToken")
    def auth_token(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authToken"))

    @auth_token.setter
    def auth_token(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e339fdeb62a420f74a048f011a3205824299b98e7b8629e921416b01cb9d762c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authToken", value)

    @builtins.property
    @jsii.member(jsii_name="certFile")
    def cert_file(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certFile"))

    @cert_file.setter
    def cert_file(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__104ce17b8f7711780baea8a7485e00a748404280d32505180ee386ca90b15fcd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certFile", value)

    @builtins.property
    @jsii.member(jsii_name="clientCertFile")
    def client_cert_file(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientCertFile"))

    @client_cert_file.setter
    def client_cert_file(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95fa7d34c83928ec3ebc4df6e5e9f09152dc5034837492dd4ae50b462119abd7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientCertFile", value)

    @builtins.property
    @jsii.member(jsii_name="clientCertKey")
    def client_cert_key(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientCertKey"))

    @client_cert_key.setter
    def client_cert_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd1f4f8ad3ba1bbc9bbc319c5819b0e376bb067e22760af8332cd4b7cf1eae2d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientCertKey", value)

    @builtins.property
    @jsii.member(jsii_name="configPath")
    def config_path(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configPath"))

    @config_path.setter
    def config_path(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf988e9cb0fcfa208e42362c2af2dd04ffdf20c2775bb0c20622ae5085886563)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configPath", value)

    @builtins.property
    @jsii.member(jsii_name="context")
    def context(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "context"))

    @context.setter
    def context(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30950b2002d6ef9f37d0ca9137e22a08c3ff8252d3c6086b899eb9ef0d919634)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "context", value)

    @builtins.property
    @jsii.member(jsii_name="core")
    def core(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "core"))

    @core.setter
    def core(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ba75af1e0b2d9a7b12e79a85d2ddc5332be46c83a2be274f7fcbda4907fd38e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "core", value)

    @builtins.property
    @jsii.member(jsii_name="grpcWeb")
    def grpc_web(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "grpcWeb"))

    @grpc_web.setter
    def grpc_web(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8201e5838ca8c3256a5eedb8b12956ca3416a0b9319b29ec0061acf02c98f60)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "grpcWeb", value)

    @builtins.property
    @jsii.member(jsii_name="grpcWebRootPath")
    def grpc_web_root_path(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "grpcWebRootPath"))

    @grpc_web_root_path.setter
    def grpc_web_root_path(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29a8f0cc79f4d4cca58fd85a36ef071b312a95c460af36e5b437cdc79c38b472)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "grpcWebRootPath", value)

    @builtins.property
    @jsii.member(jsii_name="headers")
    def headers(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "headers"))

    @headers.setter
    def headers(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f82bf36b43681aec89f626070424cb1e72713502232a603955925a7e318608c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headers", value)

    @builtins.property
    @jsii.member(jsii_name="insecure")
    def insecure(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "insecure"))

    @insecure.setter
    def insecure(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__098e0cc032fdbfddd7a17c68f8986189f01fd58bd26b6ea0f4efd821fe41f7d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "insecure", value)

    @builtins.property
    @jsii.member(jsii_name="kubernetes")
    def kubernetes(self) -> typing.Optional["ArgocdProviderKubernetes"]:
        return typing.cast(typing.Optional["ArgocdProviderKubernetes"], jsii.get(self, "kubernetes"))

    @kubernetes.setter
    def kubernetes(self, value: typing.Optional["ArgocdProviderKubernetes"]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83083106d25d0de50f05662781a6a7f969fdeb64b671ff7fc60f4fb35d1eb1ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kubernetes", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "password"))

    @password.setter
    def password(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b5187fd0e9db8d74bba4ccefbaa6fd7de4b67a3bef60cd06fd8615ef65e870a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="plainText")
    def plain_text(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "plainText"))

    @plain_text.setter
    def plain_text(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35c5a2dffab69f51e196ec97ad0731331d67a5358e195dfb4d553489cba41a8c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "plainText", value)

    @builtins.property
    @jsii.member(jsii_name="portForward")
    def port_forward(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "portForward"))

    @port_forward.setter
    def port_forward(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e43d48aa6e4ddabb27aaa47f80cf4b6f91fc5caa123c4189cfcf39350d71f63f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "portForward", value)

    @builtins.property
    @jsii.member(jsii_name="portForwardWithNamespace")
    def port_forward_with_namespace(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "portForwardWithNamespace"))

    @port_forward_with_namespace.setter
    def port_forward_with_namespace(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3401f43e6a048269214b2bf985784826c735058a496393e1fa21fd41ddd9b1d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "portForwardWithNamespace", value)

    @builtins.property
    @jsii.member(jsii_name="serverAddr")
    def server_addr(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverAddr"))

    @server_addr.setter
    def server_addr(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b03276b7bd3a1eaba47fb34f1cfb9506487f734f338fbc09e2bbdc8a613b8a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverAddr", value)

    @builtins.property
    @jsii.member(jsii_name="useLocalConfig")
    def use_local_config(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "useLocalConfig"))

    @use_local_config.setter
    def use_local_config(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95cd25ab52fe173d482702dca4e0d24e9315957f0543bbc7b3e5c6c5324601bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useLocalConfig", value)

    @builtins.property
    @jsii.member(jsii_name="userAgent")
    def user_agent(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userAgent"))

    @user_agent.setter
    def user_agent(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70c45977c9692b35cfc8109b59ba40e714f3f445a07d048749424b0556a8333e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userAgent", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "username"))

    @username.setter
    def username(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95d1f25388846df30480033a80cf92b733ace06cec22b9ad485107bb10d08c05)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)


@jsii.data_type(
    jsii_type="argocd.provider.ArgocdProviderConfig",
    jsii_struct_bases=[],
    name_mapping={
        "alias": "alias",
        "auth_token": "authToken",
        "cert_file": "certFile",
        "client_cert_file": "clientCertFile",
        "client_cert_key": "clientCertKey",
        "config_path": "configPath",
        "context": "context",
        "core": "core",
        "grpc_web": "grpcWeb",
        "grpc_web_root_path": "grpcWebRootPath",
        "headers": "headers",
        "insecure": "insecure",
        "kubernetes": "kubernetes",
        "password": "password",
        "plain_text": "plainText",
        "port_forward": "portForward",
        "port_forward_with_namespace": "portForwardWithNamespace",
        "server_addr": "serverAddr",
        "use_local_config": "useLocalConfig",
        "user_agent": "userAgent",
        "username": "username",
    },
)
class ArgocdProviderConfig:
    def __init__(
        self,
        *,
        alias: typing.Optional[builtins.str] = None,
        auth_token: typing.Optional[builtins.str] = None,
        cert_file: typing.Optional[builtins.str] = None,
        client_cert_file: typing.Optional[builtins.str] = None,
        client_cert_key: typing.Optional[builtins.str] = None,
        config_path: typing.Optional[builtins.str] = None,
        context: typing.Optional[builtins.str] = None,
        core: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        grpc_web: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        grpc_web_root_path: typing.Optional[builtins.str] = None,
        headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        insecure: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        kubernetes: typing.Optional[typing.Union["ArgocdProviderKubernetes", typing.Dict[builtins.str, typing.Any]]] = None,
        password: typing.Optional[builtins.str] = None,
        plain_text: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        port_forward: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        port_forward_with_namespace: typing.Optional[builtins.str] = None,
        server_addr: typing.Optional[builtins.str] = None,
        use_local_config: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        user_agent: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param alias: Alias name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#alias ArgocdProvider#alias}
        :param auth_token: ArgoCD authentication token, takes precedence over ``username``/``password``. Can be set through the ``ARGOCD_AUTH_TOKEN`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#auth_token ArgocdProvider#auth_token}
        :param cert_file: Additional root CA certificates file to add to the client TLS connection pool. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#cert_file ArgocdProvider#cert_file}
        :param client_cert_file: Client certificate. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#client_cert_file ArgocdProvider#client_cert_file}
        :param client_cert_key: Client certificate key. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#client_cert_key ArgocdProvider#client_cert_key}
        :param config_path: Override the default config path of ``$HOME/.config/argocd/config``. Only relevant when ``use_local_config``. Can be set through the ``ARGOCD_CONFIG_PATH`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#config_path ArgocdProvider#config_path}
        :param context: Context to choose when using a local ArgoCD config file. Only relevant when ``use_local_config``. Can be set through ``ARGOCD_CONTEXT`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#context ArgocdProvider#context}
        :param core: Configure direct access using Kubernetes API server. **Warning**: this feature works by starting a local ArgoCD API server that talks directly to the Kubernetes API using the **current context in the default kubeconfig** (``~/.kube/config``). This behavior cannot be overridden using either environment variables or the ``kubernetes`` block in the provider configuration at present). If the server fails to start (e.g. your kubeconfig is misconfigured) then the provider will fail as a result of the ``argocd`` module forcing it to exit and no logs will be available to help you debug this. The error message will be similar to .. epigraph:: ``The plugin encountered an error, and failed to respond to the plugin.(*GRPCProvider).ReadResource call. The plugin logs may contain more details.`` To debug this, you will need to login via the ArgoCD CLI using ``argocd login --core`` and then running an operation. E.g. ``argocd app list``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#core ArgocdProvider#core}
        :param grpc_web: Whether to use gRPC web proxy client. Useful if Argo CD server is behind proxy which does not support HTTP2. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#grpc_web ArgocdProvider#grpc_web}
        :param grpc_web_root_path: Use the gRPC web proxy client and set the web root, e.g. ``argo-cd``. Useful if the Argo CD server is behind a proxy at a non-root path. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#grpc_web_root_path ArgocdProvider#grpc_web_root_path}
        :param headers: Additional headers to add to each request to the ArgoCD server. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#headers ArgocdProvider#headers}
        :param insecure: Whether to skip TLS server certificate. Can be set through the ``ARGOCD_INSECURE`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#insecure ArgocdProvider#insecure}
        :param kubernetes: kubernetes block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#kubernetes ArgocdProvider#kubernetes}
        :param password: Authentication password. Can be set through the ``ARGOCD_AUTH_PASSWORD`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#password ArgocdProvider#password}
        :param plain_text: Whether to initiate an unencrypted connection to ArgoCD server. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#plain_text ArgocdProvider#plain_text}
        :param port_forward: Connect to a random argocd-server port using port forwarding. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#port_forward ArgocdProvider#port_forward}
        :param port_forward_with_namespace: Namespace name which should be used for port forwarding. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#port_forward_with_namespace ArgocdProvider#port_forward_with_namespace}
        :param server_addr: ArgoCD server address with port. Can be set through the ``ARGOCD_SERVER`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#server_addr ArgocdProvider#server_addr}
        :param use_local_config: Use the authentication settings found in the local config file. Useful when you have previously logged in using SSO. Conflicts with ``auth_token``, ``username`` and ``password``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#use_local_config ArgocdProvider#use_local_config}
        :param user_agent: User-Agent request header override. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#user_agent ArgocdProvider#user_agent}
        :param username: Authentication username. Can be set through the ``ARGOCD_AUTH_USERNAME`` environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#username ArgocdProvider#username}
        '''
        if isinstance(kubernetes, dict):
            kubernetes = ArgocdProviderKubernetes(**kubernetes)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67cacfbcd7f2a88a7b8c8e59c9c360be54a6d89ae908ac89ed0900f200d33675)
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
            check_type(argname="argument auth_token", value=auth_token, expected_type=type_hints["auth_token"])
            check_type(argname="argument cert_file", value=cert_file, expected_type=type_hints["cert_file"])
            check_type(argname="argument client_cert_file", value=client_cert_file, expected_type=type_hints["client_cert_file"])
            check_type(argname="argument client_cert_key", value=client_cert_key, expected_type=type_hints["client_cert_key"])
            check_type(argname="argument config_path", value=config_path, expected_type=type_hints["config_path"])
            check_type(argname="argument context", value=context, expected_type=type_hints["context"])
            check_type(argname="argument core", value=core, expected_type=type_hints["core"])
            check_type(argname="argument grpc_web", value=grpc_web, expected_type=type_hints["grpc_web"])
            check_type(argname="argument grpc_web_root_path", value=grpc_web_root_path, expected_type=type_hints["grpc_web_root_path"])
            check_type(argname="argument headers", value=headers, expected_type=type_hints["headers"])
            check_type(argname="argument insecure", value=insecure, expected_type=type_hints["insecure"])
            check_type(argname="argument kubernetes", value=kubernetes, expected_type=type_hints["kubernetes"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument plain_text", value=plain_text, expected_type=type_hints["plain_text"])
            check_type(argname="argument port_forward", value=port_forward, expected_type=type_hints["port_forward"])
            check_type(argname="argument port_forward_with_namespace", value=port_forward_with_namespace, expected_type=type_hints["port_forward_with_namespace"])
            check_type(argname="argument server_addr", value=server_addr, expected_type=type_hints["server_addr"])
            check_type(argname="argument use_local_config", value=use_local_config, expected_type=type_hints["use_local_config"])
            check_type(argname="argument user_agent", value=user_agent, expected_type=type_hints["user_agent"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if alias is not None:
            self._values["alias"] = alias
        if auth_token is not None:
            self._values["auth_token"] = auth_token
        if cert_file is not None:
            self._values["cert_file"] = cert_file
        if client_cert_file is not None:
            self._values["client_cert_file"] = client_cert_file
        if client_cert_key is not None:
            self._values["client_cert_key"] = client_cert_key
        if config_path is not None:
            self._values["config_path"] = config_path
        if context is not None:
            self._values["context"] = context
        if core is not None:
            self._values["core"] = core
        if grpc_web is not None:
            self._values["grpc_web"] = grpc_web
        if grpc_web_root_path is not None:
            self._values["grpc_web_root_path"] = grpc_web_root_path
        if headers is not None:
            self._values["headers"] = headers
        if insecure is not None:
            self._values["insecure"] = insecure
        if kubernetes is not None:
            self._values["kubernetes"] = kubernetes
        if password is not None:
            self._values["password"] = password
        if plain_text is not None:
            self._values["plain_text"] = plain_text
        if port_forward is not None:
            self._values["port_forward"] = port_forward
        if port_forward_with_namespace is not None:
            self._values["port_forward_with_namespace"] = port_forward_with_namespace
        if server_addr is not None:
            self._values["server_addr"] = server_addr
        if use_local_config is not None:
            self._values["use_local_config"] = use_local_config
        if user_agent is not None:
            self._values["user_agent"] = user_agent
        if username is not None:
            self._values["username"] = username

    @builtins.property
    def alias(self) -> typing.Optional[builtins.str]:
        '''Alias name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#alias ArgocdProvider#alias}
        '''
        result = self._values.get("alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def auth_token(self) -> typing.Optional[builtins.str]:
        '''ArgoCD authentication token, takes precedence over ``username``/``password``. Can be set through the ``ARGOCD_AUTH_TOKEN`` environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#auth_token ArgocdProvider#auth_token}
        '''
        result = self._values.get("auth_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cert_file(self) -> typing.Optional[builtins.str]:
        '''Additional root CA certificates file to add to the client TLS connection pool.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#cert_file ArgocdProvider#cert_file}
        '''
        result = self._values.get("cert_file")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_cert_file(self) -> typing.Optional[builtins.str]:
        '''Client certificate.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#client_cert_file ArgocdProvider#client_cert_file}
        '''
        result = self._values.get("client_cert_file")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_cert_key(self) -> typing.Optional[builtins.str]:
        '''Client certificate key.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#client_cert_key ArgocdProvider#client_cert_key}
        '''
        result = self._values.get("client_cert_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def config_path(self) -> typing.Optional[builtins.str]:
        '''Override the default config path of ``$HOME/.config/argocd/config``. Only relevant when ``use_local_config``. Can be set through the ``ARGOCD_CONFIG_PATH`` environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#config_path ArgocdProvider#config_path}
        '''
        result = self._values.get("config_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def context(self) -> typing.Optional[builtins.str]:
        '''Context to choose when using a local ArgoCD config file.

        Only relevant when ``use_local_config``. Can be set through ``ARGOCD_CONTEXT`` environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#context ArgocdProvider#context}
        '''
        result = self._values.get("context")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def core(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Configure direct access using Kubernetes API server.

        **Warning**: this feature works by starting a local ArgoCD API server that talks directly to the Kubernetes API using the **current context in the default kubeconfig** (``~/.kube/config``). This behavior cannot be overridden using either environment variables or the ``kubernetes`` block in the provider configuration at present).

        If the server fails to start (e.g. your kubeconfig is misconfigured) then the provider will fail as a result of the ``argocd`` module forcing it to exit and no logs will be available to help you debug this. The error message will be similar to
        .. epigraph::

           ``The plugin encountered an error, and failed to respond to the plugin.(*GRPCProvider).ReadResource call. The plugin logs may contain more details.``

        To debug this, you will need to login via the ArgoCD CLI using ``argocd login --core`` and then running an operation. E.g. ``argocd app list``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#core ArgocdProvider#core}
        '''
        result = self._values.get("core")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def grpc_web(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to use gRPC web proxy client.

        Useful if Argo CD server is behind proxy which does not support HTTP2.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#grpc_web ArgocdProvider#grpc_web}
        '''
        result = self._values.get("grpc_web")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def grpc_web_root_path(self) -> typing.Optional[builtins.str]:
        '''Use the gRPC web proxy client and set the web root, e.g. ``argo-cd``. Useful if the Argo CD server is behind a proxy at a non-root path.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#grpc_web_root_path ArgocdProvider#grpc_web_root_path}
        '''
        result = self._values.get("grpc_web_root_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def headers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Additional headers to add to each request to the ArgoCD server.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#headers ArgocdProvider#headers}
        '''
        result = self._values.get("headers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def insecure(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to skip TLS server certificate. Can be set through the ``ARGOCD_INSECURE`` environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#insecure ArgocdProvider#insecure}
        '''
        result = self._values.get("insecure")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def kubernetes(self) -> typing.Optional["ArgocdProviderKubernetes"]:
        '''kubernetes block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#kubernetes ArgocdProvider#kubernetes}
        '''
        result = self._values.get("kubernetes")
        return typing.cast(typing.Optional["ArgocdProviderKubernetes"], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''Authentication password. Can be set through the ``ARGOCD_AUTH_PASSWORD`` environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#password ArgocdProvider#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def plain_text(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to initiate an unencrypted connection to ArgoCD server.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#plain_text ArgocdProvider#plain_text}
        '''
        result = self._values.get("plain_text")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def port_forward(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Connect to a random argocd-server port using port forwarding.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#port_forward ArgocdProvider#port_forward}
        '''
        result = self._values.get("port_forward")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def port_forward_with_namespace(self) -> typing.Optional[builtins.str]:
        '''Namespace name which should be used for port forwarding.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#port_forward_with_namespace ArgocdProvider#port_forward_with_namespace}
        '''
        result = self._values.get("port_forward_with_namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def server_addr(self) -> typing.Optional[builtins.str]:
        '''ArgoCD server address with port. Can be set through the ``ARGOCD_SERVER`` environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#server_addr ArgocdProvider#server_addr}
        '''
        result = self._values.get("server_addr")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def use_local_config(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Use the authentication settings found in the local config file.

        Useful when you have previously logged in using SSO. Conflicts with ``auth_token``, ``username`` and ``password``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#use_local_config ArgocdProvider#use_local_config}
        '''
        result = self._values.get("use_local_config")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def user_agent(self) -> typing.Optional[builtins.str]:
        '''User-Agent request header override.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#user_agent ArgocdProvider#user_agent}
        '''
        result = self._values.get("user_agent")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''Authentication username. Can be set through the ``ARGOCD_AUTH_USERNAME`` environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#username ArgocdProvider#username}
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ArgocdProviderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="argocd.provider.ArgocdProviderKubernetes",
    jsii_struct_bases=[],
    name_mapping={
        "client_certificate": "clientCertificate",
        "client_key": "clientKey",
        "cluster_ca_certificate": "clusterCaCertificate",
        "config_context": "configContext",
        "config_context_auth_info": "configContextAuthInfo",
        "config_context_cluster": "configContextCluster",
        "exec": "exec",
        "host": "host",
        "insecure": "insecure",
        "password": "password",
        "token": "token",
        "username": "username",
    },
)
class ArgocdProviderKubernetes:
    def __init__(
        self,
        *,
        client_certificate: typing.Optional[builtins.str] = None,
        client_key: typing.Optional[builtins.str] = None,
        cluster_ca_certificate: typing.Optional[builtins.str] = None,
        config_context: typing.Optional[builtins.str] = None,
        config_context_auth_info: typing.Optional[builtins.str] = None,
        config_context_cluster: typing.Optional[builtins.str] = None,
        exec: typing.Optional[typing.Union["ArgocdProviderKubernetesExec", typing.Dict[builtins.str, typing.Any]]] = None,
        host: typing.Optional[builtins.str] = None,
        insecure: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        password: typing.Optional[builtins.str] = None,
        token: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param client_certificate: PEM-encoded client certificate for TLS authentication. Can be sourced from ``KUBE_CLIENT_CERT_DATA``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#client_certificate ArgocdProvider#client_certificate}
        :param client_key: PEM-encoded client certificate key for TLS authentication. Can be sourced from ``KUBE_CLIENT_KEY_DATA``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#client_key ArgocdProvider#client_key}
        :param cluster_ca_certificate: PEM-encoded root certificates bundle for TLS authentication. Can be sourced from ``KUBE_CLUSTER_CA_CERT_DATA``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#cluster_ca_certificate ArgocdProvider#cluster_ca_certificate}
        :param config_context: Context to choose from the config file. Can be sourced from ``KUBE_CTX``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#config_context ArgocdProvider#config_context}
        :param config_context_auth_info: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#config_context_auth_info ArgocdProvider#config_context_auth_info}.
        :param config_context_cluster: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#config_context_cluster ArgocdProvider#config_context_cluster}.
        :param exec: exec block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#exec ArgocdProvider#exec}
        :param host: The hostname (in form of URI) of the Kubernetes API. Can be sourced from ``KUBE_HOST``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#host ArgocdProvider#host}
        :param insecure: Whether server should be accessed without verifying the TLS certificate. Can be sourced from ``KUBE_INSECURE``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#insecure ArgocdProvider#insecure}
        :param password: The password to use for HTTP basic authentication when accessing the Kubernetes API. Can be sourced from ``KUBE_PASSWORD``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#password ArgocdProvider#password}
        :param token: Token to authenticate an service account. Can be sourced from ``KUBE_TOKEN``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#token ArgocdProvider#token}
        :param username: The username to use for HTTP basic authentication when accessing the Kubernetes API. Can be sourced from ``KUBE_USER``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#username ArgocdProvider#username}
        '''
        if isinstance(exec, dict):
            exec = ArgocdProviderKubernetesExec(**exec)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2e26cb5fe50e40afa4aeb1da705b2d44eea2f7128a5adb82f7a8a0f26d21aec)
            check_type(argname="argument client_certificate", value=client_certificate, expected_type=type_hints["client_certificate"])
            check_type(argname="argument client_key", value=client_key, expected_type=type_hints["client_key"])
            check_type(argname="argument cluster_ca_certificate", value=cluster_ca_certificate, expected_type=type_hints["cluster_ca_certificate"])
            check_type(argname="argument config_context", value=config_context, expected_type=type_hints["config_context"])
            check_type(argname="argument config_context_auth_info", value=config_context_auth_info, expected_type=type_hints["config_context_auth_info"])
            check_type(argname="argument config_context_cluster", value=config_context_cluster, expected_type=type_hints["config_context_cluster"])
            check_type(argname="argument exec", value=exec, expected_type=type_hints["exec"])
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument insecure", value=insecure, expected_type=type_hints["insecure"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument token", value=token, expected_type=type_hints["token"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if client_certificate is not None:
            self._values["client_certificate"] = client_certificate
        if client_key is not None:
            self._values["client_key"] = client_key
        if cluster_ca_certificate is not None:
            self._values["cluster_ca_certificate"] = cluster_ca_certificate
        if config_context is not None:
            self._values["config_context"] = config_context
        if config_context_auth_info is not None:
            self._values["config_context_auth_info"] = config_context_auth_info
        if config_context_cluster is not None:
            self._values["config_context_cluster"] = config_context_cluster
        if exec is not None:
            self._values["exec"] = exec
        if host is not None:
            self._values["host"] = host
        if insecure is not None:
            self._values["insecure"] = insecure
        if password is not None:
            self._values["password"] = password
        if token is not None:
            self._values["token"] = token
        if username is not None:
            self._values["username"] = username

    @builtins.property
    def client_certificate(self) -> typing.Optional[builtins.str]:
        '''PEM-encoded client certificate for TLS authentication. Can be sourced from ``KUBE_CLIENT_CERT_DATA``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#client_certificate ArgocdProvider#client_certificate}
        '''
        result = self._values.get("client_certificate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_key(self) -> typing.Optional[builtins.str]:
        '''PEM-encoded client certificate key for TLS authentication. Can be sourced from ``KUBE_CLIENT_KEY_DATA``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#client_key ArgocdProvider#client_key}
        '''
        result = self._values.get("client_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cluster_ca_certificate(self) -> typing.Optional[builtins.str]:
        '''PEM-encoded root certificates bundle for TLS authentication. Can be sourced from ``KUBE_CLUSTER_CA_CERT_DATA``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#cluster_ca_certificate ArgocdProvider#cluster_ca_certificate}
        '''
        result = self._values.get("cluster_ca_certificate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def config_context(self) -> typing.Optional[builtins.str]:
        '''Context to choose from the config file. Can be sourced from ``KUBE_CTX``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#config_context ArgocdProvider#config_context}
        '''
        result = self._values.get("config_context")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def config_context_auth_info(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#config_context_auth_info ArgocdProvider#config_context_auth_info}.'''
        result = self._values.get("config_context_auth_info")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def config_context_cluster(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#config_context_cluster ArgocdProvider#config_context_cluster}.'''
        result = self._values.get("config_context_cluster")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def exec(self) -> typing.Optional["ArgocdProviderKubernetesExec"]:
        '''exec block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#exec ArgocdProvider#exec}
        '''
        result = self._values.get("exec")
        return typing.cast(typing.Optional["ArgocdProviderKubernetesExec"], result)

    @builtins.property
    def host(self) -> typing.Optional[builtins.str]:
        '''The hostname (in form of URI) of the Kubernetes API. Can be sourced from ``KUBE_HOST``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#host ArgocdProvider#host}
        '''
        result = self._values.get("host")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def insecure(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether server should be accessed without verifying the TLS certificate. Can be sourced from ``KUBE_INSECURE``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#insecure ArgocdProvider#insecure}
        '''
        result = self._values.get("insecure")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''The password to use for HTTP basic authentication when accessing the Kubernetes API. Can be sourced from ``KUBE_PASSWORD``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#password ArgocdProvider#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def token(self) -> typing.Optional[builtins.str]:
        '''Token to authenticate an service account. Can be sourced from ``KUBE_TOKEN``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#token ArgocdProvider#token}
        '''
        result = self._values.get("token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''The username to use for HTTP basic authentication when accessing the Kubernetes API. Can be sourced from ``KUBE_USER``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#username ArgocdProvider#username}
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ArgocdProviderKubernetes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="argocd.provider.ArgocdProviderKubernetesExec",
    jsii_struct_bases=[],
    name_mapping={
        "api_version": "apiVersion",
        "command": "command",
        "args": "args",
        "env": "env",
    },
)
class ArgocdProviderKubernetesExec:
    def __init__(
        self,
        *,
        api_version: builtins.str,
        command: builtins.str,
        args: typing.Optional[typing.Sequence[builtins.str]] = None,
        env: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param api_version: API version to use when decoding the ExecCredentials resource, e.g. ``client.authentication.k8s.io/v1beta1``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#api_version ArgocdProvider#api_version}
        :param command: Command to execute. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#command ArgocdProvider#command}
        :param args: Map of environment variables to set when executing the plugin. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#args ArgocdProvider#args}
        :param env: List of arguments to pass when executing the plugin. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#env ArgocdProvider#env}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36d51d9007488066088b3f6a4bddfb3f051253a4b1db7e864b3a626b217f033a)
            check_type(argname="argument api_version", value=api_version, expected_type=type_hints["api_version"])
            check_type(argname="argument command", value=command, expected_type=type_hints["command"])
            check_type(argname="argument args", value=args, expected_type=type_hints["args"])
            check_type(argname="argument env", value=env, expected_type=type_hints["env"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_version": api_version,
            "command": command,
        }
        if args is not None:
            self._values["args"] = args
        if env is not None:
            self._values["env"] = env

    @builtins.property
    def api_version(self) -> builtins.str:
        '''API version to use when decoding the ExecCredentials resource, e.g. ``client.authentication.k8s.io/v1beta1``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#api_version ArgocdProvider#api_version}
        '''
        result = self._values.get("api_version")
        assert result is not None, "Required property 'api_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def command(self) -> builtins.str:
        '''Command to execute.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#command ArgocdProvider#command}
        '''
        result = self._values.get("command")
        assert result is not None, "Required property 'command' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def args(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Map of environment variables to set when executing the plugin.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#args ArgocdProvider#args}
        '''
        result = self._values.get("args")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def env(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''List of arguments to pass when executing the plugin.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/oboukili/argocd/6.0.3/docs#env ArgocdProvider#env}
        '''
        result = self._values.get("env")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ArgocdProviderKubernetesExec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ArgocdProvider",
    "ArgocdProviderConfig",
    "ArgocdProviderKubernetes",
    "ArgocdProviderKubernetesExec",
]

publication.publish()

def _typecheckingstub__c57d8a28e881a142bb69356638ceb10d3b1607e24458dcd505f7289c5110f4a9(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    alias: typing.Optional[builtins.str] = None,
    auth_token: typing.Optional[builtins.str] = None,
    cert_file: typing.Optional[builtins.str] = None,
    client_cert_file: typing.Optional[builtins.str] = None,
    client_cert_key: typing.Optional[builtins.str] = None,
    config_path: typing.Optional[builtins.str] = None,
    context: typing.Optional[builtins.str] = None,
    core: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    grpc_web: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    grpc_web_root_path: typing.Optional[builtins.str] = None,
    headers: typing.Optional[typing.Sequence[builtins.str]] = None,
    insecure: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    kubernetes: typing.Optional[typing.Union[ArgocdProviderKubernetes, typing.Dict[builtins.str, typing.Any]]] = None,
    password: typing.Optional[builtins.str] = None,
    plain_text: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    port_forward: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    port_forward_with_namespace: typing.Optional[builtins.str] = None,
    server_addr: typing.Optional[builtins.str] = None,
    use_local_config: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    user_agent: typing.Optional[builtins.str] = None,
    username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b37044febe27eff1c07a066aa2a746199ec8d133a57e81e340a4ef5277ec00b4(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba74c87f557e2d5b5fbe9608a07b667beb094853e4f8ce1714abc94b6f63daaa(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e339fdeb62a420f74a048f011a3205824299b98e7b8629e921416b01cb9d762c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__104ce17b8f7711780baea8a7485e00a748404280d32505180ee386ca90b15fcd(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95fa7d34c83928ec3ebc4df6e5e9f09152dc5034837492dd4ae50b462119abd7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd1f4f8ad3ba1bbc9bbc319c5819b0e376bb067e22760af8332cd4b7cf1eae2d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf988e9cb0fcfa208e42362c2af2dd04ffdf20c2775bb0c20622ae5085886563(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30950b2002d6ef9f37d0ca9137e22a08c3ff8252d3c6086b899eb9ef0d919634(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ba75af1e0b2d9a7b12e79a85d2ddc5332be46c83a2be274f7fcbda4907fd38e(
    value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8201e5838ca8c3256a5eedb8b12956ca3416a0b9319b29ec0061acf02c98f60(
    value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29a8f0cc79f4d4cca58fd85a36ef071b312a95c460af36e5b437cdc79c38b472(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f82bf36b43681aec89f626070424cb1e72713502232a603955925a7e318608c(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__098e0cc032fdbfddd7a17c68f8986189f01fd58bd26b6ea0f4efd821fe41f7d8(
    value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83083106d25d0de50f05662781a6a7f969fdeb64b671ff7fc60f4fb35d1eb1ab(
    value: typing.Optional[ArgocdProviderKubernetes],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b5187fd0e9db8d74bba4ccefbaa6fd7de4b67a3bef60cd06fd8615ef65e870a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35c5a2dffab69f51e196ec97ad0731331d67a5358e195dfb4d553489cba41a8c(
    value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e43d48aa6e4ddabb27aaa47f80cf4b6f91fc5caa123c4189cfcf39350d71f63f(
    value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3401f43e6a048269214b2bf985784826c735058a496393e1fa21fd41ddd9b1d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b03276b7bd3a1eaba47fb34f1cfb9506487f734f338fbc09e2bbdc8a613b8a2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95cd25ab52fe173d482702dca4e0d24e9315957f0543bbc7b3e5c6c5324601bd(
    value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70c45977c9692b35cfc8109b59ba40e714f3f445a07d048749424b0556a8333e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95d1f25388846df30480033a80cf92b733ace06cec22b9ad485107bb10d08c05(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67cacfbcd7f2a88a7b8c8e59c9c360be54a6d89ae908ac89ed0900f200d33675(
    *,
    alias: typing.Optional[builtins.str] = None,
    auth_token: typing.Optional[builtins.str] = None,
    cert_file: typing.Optional[builtins.str] = None,
    client_cert_file: typing.Optional[builtins.str] = None,
    client_cert_key: typing.Optional[builtins.str] = None,
    config_path: typing.Optional[builtins.str] = None,
    context: typing.Optional[builtins.str] = None,
    core: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    grpc_web: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    grpc_web_root_path: typing.Optional[builtins.str] = None,
    headers: typing.Optional[typing.Sequence[builtins.str]] = None,
    insecure: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    kubernetes: typing.Optional[typing.Union[ArgocdProviderKubernetes, typing.Dict[builtins.str, typing.Any]]] = None,
    password: typing.Optional[builtins.str] = None,
    plain_text: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    port_forward: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    port_forward_with_namespace: typing.Optional[builtins.str] = None,
    server_addr: typing.Optional[builtins.str] = None,
    use_local_config: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    user_agent: typing.Optional[builtins.str] = None,
    username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2e26cb5fe50e40afa4aeb1da705b2d44eea2f7128a5adb82f7a8a0f26d21aec(
    *,
    client_certificate: typing.Optional[builtins.str] = None,
    client_key: typing.Optional[builtins.str] = None,
    cluster_ca_certificate: typing.Optional[builtins.str] = None,
    config_context: typing.Optional[builtins.str] = None,
    config_context_auth_info: typing.Optional[builtins.str] = None,
    config_context_cluster: typing.Optional[builtins.str] = None,
    exec: typing.Optional[typing.Union[ArgocdProviderKubernetesExec, typing.Dict[builtins.str, typing.Any]]] = None,
    host: typing.Optional[builtins.str] = None,
    insecure: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    password: typing.Optional[builtins.str] = None,
    token: typing.Optional[builtins.str] = None,
    username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36d51d9007488066088b3f6a4bddfb3f051253a4b1db7e864b3a626b217f033a(
    *,
    api_version: builtins.str,
    command: builtins.str,
    args: typing.Optional[typing.Sequence[builtins.str]] = None,
    env: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
