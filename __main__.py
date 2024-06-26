import os
import subprocess
import time
from typing import Any, Dict

import pulumi
from pulumi import FileAsset, get_organization, get_project, get_stack, ResourceOptions, StackReference
import pulumi_kubernetes as kubernetes
from pulumi_kubernetes import Provider
from pulumi_kubernetes.helm.v3 import ReleaseArgs, RepositoryOptsArgs
from pulumi_kubernetes.networking.v1 import IngressTLSArgs
from pulumi_digitalocean import Domain, DnsRecord, Droplet, get_image, RecordType, SshKey
import pulumi_std as std
import yaml

config = pulumi.Config()
cpus = 2
disk_size_gb = 80
memory_size_gb = 4
region = "sfo3"
ssh_key_path = os.path.expanduser("~/.ssh/id_ed25519") # TODO: std.pathexpand(_output()) ?
ssh_public_key = std.file(input=f"{ssh_key_path}.pub").result # TODO: file_output() without result?
subdomains = [
    "www",
]
user_data = f"""#cloud-config
disable_root: true
package_reboot_if_required: true
package_update: true
package_upgrade: true
runcmd:
  - sed -i -E '/^#?PermitRootLogin/s/^.*$/PermitRootLogin no/' /etc/ssh/sshd_config
  - sed -i -e '$aAllowUsers ubuntu' /etc/ssh/sshd_config
  - service ssh restart
  - [ runuser, -l, ubuntu, -c, "curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
      && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
      sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
      sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list" ]
  - [ runuser, -l, ubuntu, -c, sudo apt-get update ]
  - [ runuser, -l, ubuntu, -c, sudo apt-get install -y nvidia-container-runtime ]
  - [ runuser, -l, ubuntu, -c, curl -sLS https://get.arkade.dev | sudo sh ]
  - [ runuser, -l, ubuntu, -c, arkade get helm k3sup ]
  - [ runuser, -l, ubuntu, -c, echo '' >> ~/.bashrc && echo 'export PATH=$PATH:$HOME/.arkade/bin/' >> ~/.bashrc ]
  - [ runuser, -l, ubuntu, -c, ~/.arkade/bin/k3sup install --context {config.get('primary_domain_name')} --k3s-extra-args '--disable traefik --write-kubeconfig-mode "0644"' --local --user ubuntu ]
users:
  - default
  - groups: sudo
    name: ubuntu
    shell: /bin/bash
    ssh_authorized_keys:
      - {ssh_public_key}
    sudo: ALL=(ALL) NOPASSWD:ALL
"""

def wait_for_kubeconfig(host, username, private_key_path, timeout=600):
    start_time = time.time()

    while time.time() - start_time < timeout:
        try:
            cmd = f"""k3sup install \
                --context {config.get('primary_domain_name')} \
                --ip {host} \
                --local-path kubeconfig \
                --skip-install \
                --ssh-key {private_key_path} \
                --user {username}"""

            cp = subprocess.run(cmd, capture_output=True, encoding='utf-8', shell=True)

            if cp.returncode == 0:
                return std.file(input="kubeconfig").result

            else:
                print("Command failed, retrying...")

        except Exception as e:
            print(f"SSH connection failed: {e}, retrying...")
        
        time.sleep(10)
    
    raise TimeoutError("SSH connection timed out")

class Stack1(pulumi.ComponentResource):
    def __init__(self, opts=None):
        super().__init__('my:stack:Stack1', 'stack1', None, opts)

        if get_stack() == "local":
            cloud_config_file_path = 'cloud-config.yaml'
            pulumi.export('cloud_config', FileAsset(cloud_config_file_path))

            with open(cloud_config_file_path, 'w') as f:
                f.write(user_data)

            try:
                cmd = f"""multipass launch \
                    --cpus {cpus} \
                    --disk {disk_size_gb}G \
                    --memory {memory_size_gb}G \
                    --name {get_project()} \
                    --cloud-init cloud-config.yaml"""

                cp = subprocess.run(cmd, capture_output=True, encoding='utf-8', shell=True)
                cp.check_returncode()

            except subprocess.CalledProcessError as e:
                print('cp.stderr', cp.stderr)

            class MultipassInstance: # TODO make this a custom component resource pulumi.ComponentResource w/ create/destroy
                instance_info: Dict[str, Any]

                def __init__(self):
                    try:
                        cmd = f"""multipass info {get_project()} --format yaml"""

                        cp = subprocess.run(cmd, capture_output=True, encoding='utf-8', shell=True)
                        cp.check_returncode()

                        instance_info = yaml.safe_load(cp.stdout)
                        self.instance_info: Dict[str, Any] = instance_info
                        self.ipv4_address = pulumi.Output.from_input(self.instance_info.get(get_project())[0].get('ipv4')[0])

                    except subprocess.CalledProcessError as e:
                        print('cp.stderr', cp.stderr)

            instance = MultipassInstance()

            pulumi.export("ipv4", instance.ipv4_address)

            etc_hosts = [
                f"# cat .etchosts | sudo $(which hostctl) add ephemeral --wait 0",
                f"{instance.instance_info.get(get_project())[0].get('ipv4')[0]} {config.get('primary_domain_name')}"
            ]

            for subdomain in subdomains:
                etc_hosts.append(f"{instance.instance_info.get(get_project())[0].get('ipv4')[0]} {subdomain}.{config.get('primary_domain_name')}")
                pulumi.export(f"{subdomain}Fqdn", f"{subdomain}.{config.get('primary_domain_name')}")

            etc_hosts.append("")
            etc_hosts_file_path = '.etchosts'
            pulumi.export('etc_hosts', FileAsset(etc_hosts_file_path))

            with open(etc_hosts_file_path, 'w') as f:
                f.write("\n".join(etc_hosts))

        else:
            ssh_key = SshKey("ssh-key",
                name=f"{get_project()}",
                opts=pulumi.ResourceOptions(parent=self),
                public_key=ssh_public_key,
            )

            image = get_image(slug='ubuntu-22-04-x64')
            instance = Droplet(
                get_project(),
                image=image.id,
                opts=pulumi.ResourceOptions(parent=self),
                region=region,
                size=f"s-{cpus}vcpu-{memory_size_gb}gb",
                ssh_keys=[ssh_key.fingerprint],
                user_data=user_data,
            )

            pulumi.export("ipv4", instance.ipv4_address)

            domain = Domain(
                get_project(),
                name=config.get('primary_domain_name'),
                ip_address=instance.ipv4_address,
                opts=ResourceOptions(parent=self),
            )

            for subdomain in subdomains:
                dns_record = DnsRecord(
                    f"a-{subdomain}-dns-record",
                    domain=domain.id,
                    name=subdomain,
                    opts=ResourceOptions(parent=domain),
                    type=RecordType.A,
                    value=instance.ipv4_address
                )

                pulumi.export(f"{subdomain}Fqdn", dns_record.fqdn)

            mx_records = [ # TODO: Get these dynamically
                ("aspmx.l.google.com.", 1),
                ("alt1.aspmx.l.google.com.", 5),
                ("alt2.aspmx.l.google.com.", 5),
                ("alt3.aspmx.l.google.com.", 10),
                ("alt4.aspmx.l.google.com.", 10),
            ]

            for idx, (value, priority) in enumerate(mx_records):
                dns_record = DnsRecord(f"mx-{idx}-dns-record",
                    domain=domain.id,
                    name="@",
                    opts=ResourceOptions(parent=domain),
                    priority=priority,
                    ttl=1800,
                    type=RecordType.MX,
                    value=value,
                )

        kubeconfig = instance.ipv4_address.apply(lambda ip: wait_for_kubeconfig(
            host=ip,
            username="ubuntu",
            private_key_path=ssh_key_path,
        ))

        pulumi.export("kubeconfig", kubeconfig)

class Stack2(pulumi.ComponentResource):
    def __init__(self, opts=None, stack1: pulumi.ComponentResource=None):
        super().__init__('my:stack:Stack2', 'stack2', None, opts)

        infra = StackReference(
            f"{get_organization()}/{get_project()}/{get_stack()}",
            opts=ResourceOptions(parent=self),
        )

        if get_stack() == "local":
            # provider = Provider('k8s-yaml-rendered',
            #     opts=ResourceOptions(parent=self),
            #     render_yaml_to_directory='k8s'
            # )

            provider = Provider("k8s",
                kubeconfig=infra.get_output("kubeconfig"),
                opts=ResourceOptions(parent=self),
            )

        else:
            provider = Provider("k8s",
                kubeconfig=infra.get_output("kubeconfig"),
                opts=ResourceOptions(parent=self),
            )

        caddy_data = kubernetes.core.v1.PersistentVolumeClaim("caddy-data",
            metadata=kubernetes.meta.v1.ObjectMetaArgs(
                labels={
                    "io.kompose.service": "caddy-data",
                },
                name="caddy-data",
            ),
            opts=ResourceOptions(
                parent=self,
                provider=provider,
            ),
            spec=kubernetes.core.v1.PersistentVolumeClaimSpecArgs(
                access_modes=["ReadWriteOnce"],
                resources=kubernetes.core.v1.VolumeResourceRequirementsArgs(
                    requests={
                        "storage": "100Mi",
                    },
                ),
            ))

        caddy_config = kubernetes.core.v1.PersistentVolumeClaim("caddy-config",
            metadata=kubernetes.meta.v1.ObjectMetaArgs(
                labels={
                    "io.kompose.service": "caddy-config",
                },
                name="caddy-config",
            ),
            opts=ResourceOptions(
                parent=self,
                provider=provider,
            ),
            spec=kubernetes.core.v1.PersistentVolumeClaimSpecArgs(
                access_modes=["ReadWriteOnce"],
                resources=kubernetes.core.v1.VolumeResourceRequirementsArgs(
                    requests={
                        "storage": "100Mi",
                    },
                ),
            ))

        db_data = kubernetes.core.v1.PersistentVolumeClaim("db-data",
            metadata=kubernetes.meta.v1.ObjectMetaArgs(
                labels={
                    "io.kompose.service": "db-data",
                },
                name="db-data",
            ),
            opts=ResourceOptions(
                parent=self,
                provider=provider,
            ),
            spec=kubernetes.core.v1.PersistentVolumeClaimSpecArgs(
                access_modes=["ReadWriteOnce"],
                resources=kubernetes.core.v1.VolumeResourceRequirementsArgs(
                    requests={
                        "storage": "100Mi",
                    },
                ),
            ))

        upload_data = kubernetes.core.v1.PersistentVolumeClaim("upload-data",
            metadata=kubernetes.meta.v1.ObjectMetaArgs(
                labels={
                    "io.kompose.service": "upload-data",
                },
                name="upload-data",
            ),
            opts=ResourceOptions(
                parent=self,
                provider=provider,
            ),
            spec=kubernetes.core.v1.PersistentVolumeClaimSpecArgs(
                access_modes=["ReadWriteOnce"],
                resources=kubernetes.core.v1.VolumeResourceRequirementsArgs(
                    requests={
                        "storage": "100Mi",
                    },
                ),
            ))

        caddy_global_options = kubernetes.core.v1.ConfigMap("caddy-global-options",
            data={
                "acmeCA": "internal",
            },
            metadata=kubernetes.meta.v1.ObjectMetaArgs(
                name="caddy-global-options",
                namespace="caddy-system",
            ),
            opts=ResourceOptions(
                parent=self,
                provider=provider,
            ),
        )

        # # =========== GPU support ===========
        # helm repo add nvidia https://helm.ngc.nvidia.com/nvidia && helm repo update

        # # Create namespace if it doesn't exist
        # echo "Creating namespace gpu-operator"
        # kubectl create namespace gpu-operator || true

        # # Install GPU operator
        # echo "Installing GPU operator"
        # helm install gpu-operator -n gpu-operator --create-namespace \
        # nvidia/gpu-operator $HELM_OPTIONS \
        # --set 'toolkit.env[0].name=CONTAINERD_CONFIG' \
        # --set 'toolkit.env[0].value=/var/lib/rancher/k3s/agent/etc/containerd/config.toml' \
        # --set 'toolkit.env[1].name=CONTAINERD_SOCKET' \
        # --set 'toolkit.env[1].value=/run/k3s/containerd/containerd.sock' \
        # --set 'toolkit.env[2].name=CONTAINERD_RUNTIME_CLASS' \
        # --set 'toolkit.env[2].value=nvidia' || true

        # # Create RuntimeClass
        # echo "Creating RuntimeClass"
        # kubectl apply -f - <<EOF
        # apiVersion: node.k8s.io/v1
        # kind: RuntimeClass
        # metadata:
        # name: nvidia
        # handler: nvidia
        # EOF


        # See:
        # - https://catalog.ngc.nvidia.com/orgs/nvidia/helm-charts/gpu-operator
        # - https://github.com/skypilot-org/skypilot/blob/master/tests/kubernetes/scripts/deploy_k3s.sh#L99
        gpu_operator = kubernetes.helm.v3.Release(
            "gpu-operator",
            args=ReleaseArgs(
                atomic=True,
                chart="gpu-operator",
                cleanup_on_fail=True,
                create_namespace=True,
                namespace="gpu-operator",
                repository_opts=RepositoryOptsArgs(
                    repo="https://helm.ngc.nvidia.com/nvidia",
                ),
                values={
                    "toolkit": {
                        "env": [{
                            "name": "CONTAINERD_CONFIG",
                            "value": "/var/lib/rancher/k3s/agent/etc/containerd/config.toml",
                        }, {
                            "name": "CONTAINERD_SOCKET",
                            "value": "/run/k3s/containerd/containerd.sock",
                        }, {
                            "name": "CONTAINERD_RUNTIME_CLASS",
                            "value": "nvidia",
                        }]
                    }
                },
                version="24.3.0",
            ),
            opts=ResourceOptions(
                parent=self,
                provider=provider,
            ),
        )

        kubernetes.node.v1.RuntimeClass(
            "nvidia-runtime-class",
            handler="nvidia",
            metadata=kubernetes.meta.v1.ObjectMetaArgs(
                name="nvidia",
            ),
            opts=ResourceOptions(
                parent=self,
                provider=provider,
            ),
        )

        skypilot_service_account = kubernetes.core.v1.ServiceAccount(
            "skypilot-service-account",
            metadata=kubernetes.meta.v1.ObjectMetaArgs(
                labels={
                    "parent": "skypilot",
                },
                name="skypilot-service-account",
                namespace="default",
            ),
            opts=ResourceOptions(
                parent=self,
                provider=provider,
            ),
        )

        skypilot_service_account_role = kubernetes.rbac.v1.Role(
            "skypilot-service-account-role",
            metadata=kubernetes.meta.v1.ObjectMetaArgs(
                labels={
                    "parent": "skypilot",
                },
                name="skypilot-service-account-role",
                namespace="default",
            ),
            opts=ResourceOptions(
                parent=self,
                provider=provider,
            ),
            rules=[
                kubernetes.rbac.v1.PolicyRuleArgs(
                    api_groups=[""],
                    resources=["pods"],
                    verbs=["create", "delete", "get", "list", "patch"],
                ),
                kubernetes.rbac.v1.PolicyRuleArgs(
                    api_groups=[""],
                    resources=["pods/exec"],
                    verbs=["create", "delete", "get", "list"],
                ),
                kubernetes.rbac.v1.PolicyRuleArgs(
                    api_groups=[""],
                    resources=["pods/portforward"],
                    verbs=["create"],
                ),
                kubernetes.rbac.v1.PolicyRuleArgs(
                    api_groups=[""],
                    resources=["pods/status"],
                    verbs=["create", "delete", "get", "list"],
                ),
                kubernetes.rbac.v1.PolicyRuleArgs(
                    api_groups=["rbac.authorization.k8s.io"],
                    resources=["rolebindings"],
                    verbs=["create"],
                ),
                kubernetes.rbac.v1.PolicyRuleArgs(
                    api_groups=["rbac.authorization.k8s.io"],
                    # resource_names=["sky-ssh-jump-role"],
                    resources=["roles"],
                    verbs=["create"],
                ),
                kubernetes.rbac.v1.PolicyRuleArgs(
                    api_groups=[""],
                    resources=["secrets"],
                    verbs=["create"],
                ),
                kubernetes.rbac.v1.PolicyRuleArgs(
                    api_groups=[""],
                    resource_names=["sky-ssh-keys"],
                    resources=["secrets"],
                    verbs=["get", "patch"],
                ),
                kubernetes.rbac.v1.PolicyRuleArgs(
                    api_groups=[""],
                    resources=["serviceaccounts"],
                    verbs=["create"],
                ),
                kubernetes.rbac.v1.PolicyRuleArgs(
                    api_groups=[""],
                    resources=["services"],
                    verbs=["create", "delete", "get", "list"],
                ),
                # kubernetes.rbac.v1.PolicyRuleArgs(
                #     api_groups=[""],
                #     resource_names=["sky-ssh-jump-pod"],
                #     resources=["services"],
                #     verbs=["get"],
                # ),
            ]
        )

        skypilot_service_account_role_binding = kubernetes.rbac.v1.RoleBinding(
            "skypilot-service-account-role-binding",
            metadata=kubernetes.meta.v1.ObjectMetaArgs(
                labels={
                    "parent": "skypilot",
                },
                name="skypilot-service-account-role-binding",
                namespace="default",
            ),
            opts=ResourceOptions(
                parent=self,
                provider=provider,
            ),
            role_ref=kubernetes.rbac.v1.RoleRefArgs(
                api_group="rbac.authorization.k8s.io",
                kind="Role",
                name=skypilot_service_account_role.metadata.name,
            ),
            subjects=[
                kubernetes.rbac.v1.SubjectArgs(
                    api_group="",
                    kind="ServiceAccount",
                    name=skypilot_service_account.metadata.name,
                )
            ]
        )

        skypilot_service_account_cluster_role = kubernetes.rbac.v1.ClusterRole(
            "skypilot-service-account-cluster-role",
            metadata=kubernetes.meta.v1.ObjectMetaArgs(
                labels={
                    "parent": "skypilot",
                },
                name="skypilot-service-account-cluster-role",
            ),
            opts=ResourceOptions(
                parent=self,
                provider=provider,
            ),
            rules=[
                kubernetes.rbac.v1.PolicyRuleArgs(
                    api_groups=["networking.k8s.io"],
                    resources=["ingressclasses"],
                    verbs=["list"],
                ),
                kubernetes.rbac.v1.PolicyRuleArgs(
                    api_groups=[""],
                    resources=["nodes"],
                    verbs=["list"],
                ),
                kubernetes.rbac.v1.PolicyRuleArgs(
                    api_groups=["node.k8s.io"],
                    resources=["runtimeclasses"],
                    verbs=["list"],
                ),
            ]
        )

        skypilot_service_account_cluster_role_binding = kubernetes.rbac.v1.ClusterRoleBinding(
            "skypilot-service-account-cluster-role-binding",
            metadata=kubernetes.meta.v1.ObjectMetaArgs(
                labels={
                    "parent": "skypilot",
                },
                name="skypilot-service-account-cluster-role-binding",
            ),
            opts=ResourceOptions(
                parent=self,
                provider=provider,
            ),
            role_ref=kubernetes.rbac.v1.RoleRefArgs(
                api_group="rbac.authorization.k8s.io",
                kind="ClusterRole",
                name=skypilot_service_account_cluster_role.metadata.name,
            ),
            subjects=[
                kubernetes.rbac.v1.SubjectArgs(
                    kind="ServiceAccount",
                    name=skypilot_service_account.metadata.name,
                    namespace="default",
                )
            ]
        )

        app_deployment = kubernetes.apps.v1.Deployment("app-deployment",
            metadata=kubernetes.meta.v1.ObjectMetaArgs(
                labels={
                    "io.kompose.service": "app",
                },
                name="app",
            ),
            opts=ResourceOptions(
                ignore_changes=["spec.template.spec.containers[*]"] if get_stack() == "local" else None,
                parent=self,
                provider=provider,
            ),
            spec=kubernetes.apps.v1.DeploymentSpecArgs(
                replicas=1,
                selector=kubernetes.meta.v1.LabelSelectorArgs(
                    match_labels={
                        "io.kompose.service": "app",
                    },
                ),
                strategy=kubernetes.apps.v1.DeploymentStrategyArgs(
                    type="Recreate",
                ),
                template=kubernetes.core.v1.PodTemplateSpecArgs(
                    metadata=kubernetes.meta.v1.ObjectMetaArgs(
                        labels={
                            "io.kompose.service": "app",
                        },
                    ),
                    spec=kubernetes.core.v1.PodSpecArgs(
                        containers=[kubernetes.core.v1.ContainerArgs(
                            args=["reflex", "run", "--backend-only", "--env", "prod", "--loglevel", "debug"],
                            env=[
                                kubernetes.core.v1.EnvVarArgs(
                                    name="API_URL",
                                    value=f"https://{config.get('primary_domain_name')}",
                                ),
                                kubernetes.core.v1.EnvVarArgs(
                                    name="DB_URL",
                                    value="sqlite:///data/reflex.db",
                                ),
                            ],
                            image="mschock/reflex-app",
                            name="app",
                            ports=([
                                kubernetes.core.v1.ContainerPortArgs(
                                    container_port=3000,
                                    protocol="TCP",
                                ),
                            ] if get_stack() == "local" else []) + [
                                kubernetes.core.v1.ContainerPortArgs(
                                    container_port=8000,
                                    protocol="TCP",
                                ),
                            ],
                            volume_mounts=[
                                kubernetes.core.v1.VolumeMountArgs(
                                    mount_path="/home/ubuntu/app/data",
                                    name="db-data",
                                ),
                                kubernetes.core.v1.VolumeMountArgs(
                                    mount_path="/home/ubuntu/app/uploaded_files",
                                    name="upload-data",
                                ),
                            ],
                        )],
                        restart_policy="Always",
                        service_account_name=skypilot_service_account.metadata.name,
                        volumes=[
                            kubernetes.core.v1.VolumeArgs(
                                name="db-data",
                                persistent_volume_claim=kubernetes.core.v1.PersistentVolumeClaimVolumeSourceArgs(
                                    claim_name="db-data",
                                ),
                            ),
                            kubernetes.core.v1.VolumeArgs(
                                name="upload-data",
                                persistent_volume_claim=kubernetes.core.v1.PersistentVolumeClaimVolumeSourceArgs(
                                    claim_name="upload-data",
                                ),
                            ),
                        ],
                    ),
                ),
            ))

        app_service = kubernetes.core.v1.Service("app-service",
            metadata=kubernetes.meta.v1.ObjectMetaArgs(
                labels={
                    "io.kompose.service": "app",
                },
                name="app",
            ),
            opts=ResourceOptions(
                parent=self,
                provider=provider,
            ),
            spec=kubernetes.core.v1.ServiceSpecArgs(
                ports=([
                    kubernetes.core.v1.ServicePortArgs(
                        name="3000",
                        port=3000,
                        target_port=3000,
                    ),
                ] if get_stack() == "local" else []) + [
                    kubernetes.core.v1.ServicePortArgs(
                        name="8000",
                        port=8000,
                        target_port=8000,
                    ),
                ],
                selector={
                    "io.kompose.service": "app",
                },
            ))

        webserver_deployment = kubernetes.apps.v1.Deployment("webserver-deployment",
            metadata=kubernetes.meta.v1.ObjectMetaArgs(
                labels={
                    "io.kompose.service": "webserver",
                },
                name="webserver",
            ),
            opts=ResourceOptions(
                parent=self,
                provider=provider,
            ),
            spec=kubernetes.apps.v1.DeploymentSpecArgs(
                replicas=1,
                selector=kubernetes.meta.v1.LabelSelectorArgs(
                    match_labels={
                        "io.kompose.service": "webserver",
                    },
                ),
                strategy=kubernetes.apps.v1.DeploymentStrategyArgs(
                    type="Recreate",
                ),
                template=kubernetes.core.v1.PodTemplateSpecArgs(
                    metadata=kubernetes.meta.v1.ObjectMetaArgs(
                        labels={
                            "io.kompose.service": "webserver",
                        },
                    ),
                    spec=kubernetes.core.v1.PodSpecArgs(
                        containers=[kubernetes.core.v1.ContainerArgs(
                            args=["caddy", "run", "--config", "Caddyfile", "--adapter", "caddyfile"],
                            env=[kubernetes.core.v1.EnvVarArgs(
                                name="DOMAIN",
                                value=config.get('primary_domain_name'),
                            )],
                            image="mschock/webserver",
                            name="webserver",
                            ports=[
                                kubernetes.core.v1.ContainerPortArgs(
                                    container_port=80,
                                    protocol="TCP",
                                ),
                            ],
                            volume_mounts=[
                                kubernetes.core.v1.VolumeMountArgs(
                                    mount_path="/home/ubuntu/.local/share/caddy",
                                    name="caddy-data",
                                ),
                                kubernetes.core.v1.VolumeMountArgs(
                                    mount_path="/home/ubuntu/.config/caddy",
                                    name="caddy-config",
                                ),
                            ],
                        )],
                        restart_policy="Always",
                        volumes=[
                            kubernetes.core.v1.VolumeArgs(
                                name="caddy-data",
                                persistent_volume_claim=kubernetes.core.v1.PersistentVolumeClaimVolumeSourceArgs(
                                    claim_name="caddy-data",
                                ),
                            ),
                            kubernetes.core.v1.VolumeArgs(
                                name="caddy-config",
                                persistent_volume_claim=kubernetes.core.v1.PersistentVolumeClaimVolumeSourceArgs(
                                    claim_name="caddy-config",
                                ),
                            ),
                        ],
                    ),
                ),
            ))

        webserver_service = kubernetes.core.v1.Service("webserver-service",
            metadata=kubernetes.meta.v1.ObjectMetaArgs(
                labels={
                    "io.kompose.service": "webserver",
                },
                name="webserver",
            ),
            opts=ResourceOptions(
                parent=self,
                provider=provider,
            ),
            spec=kubernetes.core.v1.ServiceSpecArgs(
                ports=[
                    kubernetes.core.v1.ServicePortArgs(
                        name="2019",
                        port=2019,
                        target_port=80,
                    ),
                ],
                selector={
                    "io.kompose.service": "webserver",
                },
            ))

        ingress_controller = kubernetes.helm.v3.Release(
            "ic",
            args=ReleaseArgs(
                atomic=True,
                chart="caddy-ingress-controller",
                cleanup_on_fail=True,
                create_namespace=True,
                namespace="caddy-system",
                repository_opts=RepositoryOptsArgs(
                    repo="https://caddyserver.github.io/ingress",
                ),
                values={
                    "ingressController": {
                        "config": {
                            "acmeCA": config.get('ingress_controller_acme_ca'), # TODO: delete this for local?
                            "debug": config.get_bool('ingress_controller_debug'),
                            "email": config.get("ingress_controller_email"), # TODO: delete this for local?
                        },
                    },
                },
                version="1.1.0",
            ),
            opts=ResourceOptions(
                parent=self,
                provider=provider,
            ),
        )

        if get_stack() == "local":
            tls_secret = kubernetes.core.v1.Secret("tls-secret",
                data={
                    "tls.crt": std.filebase64(input=f"tls.crt").result,
                    "tls.key": std.filebase64(input=f"tls.key").result,
                },
                metadata=kubernetes.meta.v1.ObjectMetaArgs(
                    name=f"ssl-{config.get('primary_domain_name')}",
                    namespace="default",
                ),
                opts=ResourceOptions(
                    parent=self,
                    provider=provider,
                ),
                type="kubernetes.io/tls"
            )

            hosts = [config.get("primary_domain_name")] + [f"{subdomain}.{config.get('primary_domain_name')}" for subdomain in subdomains]

            tls = [IngressTLSArgs(
                hosts=hosts,
                secret_name=f"ssl-{config.get('primary_domain_name')}",
            )]

        else:
            tls = None

        ingress = kubernetes.networking.v1.Ingress("ingress",
            metadata=kubernetes.meta.v1.ObjectMetaArgs(
                annotations={
                    "kubernetes.io/ingress.class": "caddy",
                },
                name="ingress",
            ),
            opts=ResourceOptions(
                depends_on=[
                    ingress_controller,
                ],
                parent=self,
                provider=provider,
            ),
            spec=kubernetes.networking.v1.IngressSpecArgs(
                ingress_class_name="caddy",
                rules=[
                    kubernetes.networking.v1.IngressRuleArgs(
                        host=config.get('primary_domain_name'),
                        http=kubernetes.networking.v1.HTTPIngressRuleValueArgs(
                            paths=[
                                kubernetes.networking.v1.HTTPIngressPathArgs(
                                    backend=kubernetes.networking.v1.IngressBackendArgs(
                                        service=kubernetes.networking.v1.IngressServiceBackendArgs(
                                            name="webserver", # TODO: caddy?
                                            port=kubernetes.networking.v1.ServiceBackendPortArgs(
                                                number=2019,
                                            ),
                                        ),
                                    ),
                                    path="/",
                                    path_type="Prefix",
                                ),
                            ],
                        ),
                    ),
                    kubernetes.networking.v1.IngressRuleArgs(
                        host=infra.get_output("wwwFqdn"),
                        http=kubernetes.networking.v1.HTTPIngressRuleValueArgs(
                            paths=[
                                kubernetes.networking.v1.HTTPIngressPathArgs(
                                    backend=kubernetes.networking.v1.IngressBackendArgs(
                                        service=kubernetes.networking.v1.IngressServiceBackendArgs(
                                            name="webserver",
                                            port=kubernetes.networking.v1.ServiceBackendPortArgs(
                                                number=2019,
                                            ),
                                        ),
                                    ),
                                    path="/",
                                    path_type="Prefix",
                                ),
                            ],
                        ),
                    ),
                ],
                tls=tls,
            ))

stack1 = Stack1()
stack2 = Stack2(stack1=stack1)
