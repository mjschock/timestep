import os
import subprocess
import time

import pulumi
from pulumi import get_organization, get_project, get_stack, ResourceOptions, StackReference
import pulumi_kubernetes as kubernetes
from pulumi_kubernetes import Provider, core
from pulumi_kubernetes.apps.v1 import Deployment, DeploymentSpecArgs
from pulumi_kubernetes.core.v1 import Service, ConfigMap, Secret, TypedLocalObjectReferenceArgs, PodTemplateSpecArgs, PodSpecArgs, ContainerArgs, ContainerPortArgs
from pulumi_kubernetes.networking.v1 import Ingress, IngressSpecArgs, IngressRuleArgs, HTTPIngressRuleValueArgs, HTTPIngressPathArgs, IngressBackendArgs, IngressServiceBackendArgs, ServiceBackendPortArgs
from pulumi_kubernetes.meta.v1 import LabelSelectorArgs, ObjectMetaArgs
from pulumi_kubernetes.helm.v3 import Release, ReleaseArgs, RepositoryOptsArgs
from pulumi_digitalocean import Domain, DnsRecord, Droplet, get_image, RecordType, SshKey
import pulumi_std as std

print('organization', get_organization())
print('project: ', get_project())
print('stack: ', get_stack())

config = pulumi.Config()
cpus = 2
disk_size_gb = 80
memory_size_gb = 4
region = "sfo3"
ssh_key_path = os.path.expanduser("~/.ssh/id_ed25519")
ssh_public_key = std.file(input=f"{ssh_key_path}.pub").result
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
  - [ runuser, -l, ubuntu, -c, ~/.arkade/bin/k3sup install --context timestep.ai --k3s-extra-args '--disable traefik --write-kubeconfig-mode "0644"' --local --user ubuntu ]
users:
  - default
  - groups: sudo
    name: ubuntu
    shell: /bin/bash
    ssh_authorized_keys:
      - {ssh_public_key}
    sudo: ALL=(ALL) NOPASSWD:ALL
"""

# Create an SSH key in DigitalOcean
ssh_key = SshKey("ssh-key",
    # name=f"{project_name}-ssh-key",
    name=f"{pulumi.get_project()}",
    public_key=ssh_public_key,
)

def wait_for_kubeconfig(host, username, private_key_path, timeout=600):
    start_time = time.time()

    while time.time() - start_time < timeout:
        try:
            cmd = f"""k3sup install \
                --context timestep.ai \
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

# droplet_type = "hoa-assistant-app-%s" %get_stack()
# droplet_type_tag = do.Tag(droplet_type)

# Stack 1
class Stack1(pulumi.ComponentResource):
    def __init__(self, opts=None):
        super().__init__('my:stack:Stack1', 'stack1', None, opts)

        # Get the latest Ubuntu image
        image = get_image(slug='ubuntu-22-04-x64')
        # instance_name = "web-%s" %x
        # name_tag = do.Tag(instance_name)

        if get_stack() == "local":
            raise NotImplementedError()

        # Create a DigitalOcean droplet
        droplet = Droplet(
            # project_name,
            pulumi.get_project(),
            image=image.id,
            opts=pulumi.ResourceOptions(parent=self),
            region=region,
            # ssh_keys=[f"{ssh_key_id}"],
            size=f"s-{cpus}vcpu-{memory_size_gb}gb",
            ssh_keys=[ssh_key.fingerprint],  # Use the SSH key fingerprint
            # tags=[name_tag.id, droplet_type_tag.id],
            user_data=user_data,
        )

        pulumi.export("ipv4", droplet.ipv4_address)

        domain = Domain(
            get_project(),
            name="timestep.ai",
            ip_address=droplet.ipv4_address,
            opts=ResourceOptions(parent=self),
        )

        pulumi.export(f"domain_name", domain.name)

        subdomains = [
            "alice",
            "bob",
            "example1",
            "example2",
            "www",
        ]

        for subdomain in subdomains:
            dns_record = DnsRecord(
                f"{subdomain}_dns_record",
                domain=domain.id,
                name=subdomain,
                opts=ResourceOptions(parent=domain),
                type=RecordType.A,
                value=droplet.ipv4_address
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
            dns_record = DnsRecord(f"mx_{idx}",
                domain=domain.id,
                name="@",
                opts=ResourceOptions(parent=domain),
                priority=priority,
                ttl=1800,
                type=RecordType.MX,
                value=value,
            )

            # pulumi.export(f"mxFqdn_{idx}", mx.fqdn)

        # pulumi.export("mxFqdn", mx.fqdn)

        # timestep_ai = Domain("timestep.ai", name="timestep.ai", opts = pulumi.ResourceOptions(protect=True))
        # www_timestep_ai = Domain("www.timestep.ai", name="www.timestep.ai", opts = pulumi.ResourceOptions(protect=True))

        # Export the droplet ID
        # self.register_outputs({'droplet_id': droplet.id})

        # Wait for the droplet to be ready and check command execution
        kubeConfig = droplet.ipv4_address.apply(lambda ip: wait_for_kubeconfig(
            host=ip,
            username="ubuntu",
            private_key_path=ssh_key_path,
        ))

        pulumi.export("kubeConfig", kubeConfig)

# Stack 2
class Stack2(pulumi.ComponentResource):
    def __init__(self, opts=None, stack1: pulumi.ComponentResource=None):
        super().__init__('my:stack:Stack2', 'stack2', None, opts)

        infra = StackReference(f"{get_organization()}/{get_project()}/{get_stack()}")

        if get_stack() == "local":
            provider = Provider('k8s-yaml-rendered',
                opts=ResourceOptions(parent=self),
                render_yaml_to_directory='yaml' # TODO: deploy or k8s?
            )

        else:
            provider = Provider("k8s",
                kubeconfig=infra.get_output("kubeConfig"),
                opts=ResourceOptions(parent=self),
            )

        caddy_data = kubernetes.core.v1.PersistentVolumeClaim("caddyData",
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

        db_data = kubernetes.core.v1.PersistentVolumeClaim("dbData",
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

        upload_data = kubernetes.core.v1.PersistentVolumeClaim("uploadData",
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

        # service = core.v1.Service(..., ResourceOptions(provider=provider))

        # kubernetes.core.v1.Namespace(
        #     "default",
        #     metadata=kubernetes.meta.v1.ObjectMetaArgs(
        #         labels={},
        #         name="default",
        #     ),
        #     opts=ResourceOptions(provider=provider),
        # )

        # Consume the output of Stack1
        # this.consumedOutput = pulumi.interpolate`Consumed output: ${stack1.output}`;
        # consumed_output = pulumi.Output.concat('Consumed output: ', stack1.output
        # cloud_instance = StackReference(f"my:stack:Stack1")
        # consumed_output = pulumi.Output.concat('Consumed output: ', stack1.output)

        # # Export the consumed output
        # self.register_outputs({'consumed_output': consumed_output})

        # # Output to a JSONL file
        # jsonl_file = os.path.join(os.getcwd(), 'output.jsonl')
        # with open(jsonl_file, 'a') as f:
        #     droplet_id = stack1.register_outputs()['droplet_id'].apply(lambda id: f'{{ "uuid": "{id}" }}\n')
        #     f.write(droplet_id)

        # caddy_global_options = kubernetes.core.v1.ConfigMap("caddyGlobalOptions",
        #     data={
        #         "acmeCA": "internal",
        #     },
        #     metadata=kubernetes.meta.v1.ObjectMetaArgs(
        #         name="caddy-global-options",
        #         namespace="caddy-system",
        #     ),
        #     opts=ResourceOptions(
        #         parent=provider,
        #         provider=provider,
        #     ),
        # )

        example1_deployment = kubernetes.apps.v1.Deployment("example1",
            metadata=kubernetes.meta.v1.ObjectMetaArgs(
                labels={
                    "app": "example1",
                },
                name="example1",
            ),
            opts=ResourceOptions(
                parent=self,
                provider=provider,
            ),
            spec=kubernetes.apps.v1.DeploymentSpecArgs(
                replicas=1,
                selector=kubernetes.meta.v1.LabelSelectorArgs(
                    match_labels={
                        "app": "example1",
                    },
                ),
                template=kubernetes.core.v1.PodTemplateSpecArgs(
                    metadata=kubernetes.meta.v1.ObjectMetaArgs(
                        labels={
                            "app": "example1",
                        },
                    ),
                    spec=kubernetes.core.v1.PodSpecArgs(
                        containers=[kubernetes.core.v1.ContainerArgs(
                            args=[
                                "-listen=:8080",
                                "-text=\"hello world 1\"\n",
                            ],
                            image="hashicorp/http-echo",
                            name="httpecho",
                            ports=[kubernetes.core.v1.ContainerPortArgs(
                                container_port=8080,
                            )],
                        )],
                    ),
                ),
            ))

        example2_deployment = kubernetes.apps.v1.Deployment("example2",
            metadata=kubernetes.meta.v1.ObjectMetaArgs(
                labels={
                    "app": "example2",
                },
                name="example2",
            ),
            opts=ResourceOptions(
                parent=self,
                provider=provider,
            ),
            spec=kubernetes.apps.v1.DeploymentSpecArgs(
                replicas=1,
                selector=kubernetes.meta.v1.LabelSelectorArgs(
                    match_labels={
                        "app": "example2",
                    },
                ),
                template=kubernetes.core.v1.PodTemplateSpecArgs(
                    metadata=kubernetes.meta.v1.ObjectMetaArgs(
                        labels={
                            "app": "example2",
                        },
                    ),
                    spec=kubernetes.core.v1.PodSpecArgs(
                        containers=[kubernetes.core.v1.ContainerArgs(
                            args=[
                                "-listen=:8080",
                                "-text=\"hello world 2\"\n",
                            ],
                            image="hashicorp/http-echo",
                            name="httpecho",
                            ports=[kubernetes.core.v1.ContainerPortArgs(
                                container_port=8080,
                            )],
                        )],
                    ),
                ),
            ))

        app_deployment = kubernetes.apps.v1.Deployment("app",
            metadata=kubernetes.meta.v1.ObjectMetaArgs(
                labels={
                    "io.kompose.service": "app",
                },
                name="app",
            ),
            opts=ResourceOptions(
                depends_on=[
                    db_data,
                    upload_data,
                ],
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
                            env=[kubernetes.core.v1.EnvVarArgs(
                                name="DB_URL",
                                value="sqlite:///data/reflex.db",
                            )],
                            # image="local/reflex-app",
                            image="mschock/reflex-app",
                            name="app",
                            volume_mounts=[
                                kubernetes.core.v1.VolumeMountArgs(
                                    mount_path="/app/data",
                                    name="db-data",
                                ),
                                kubernetes.core.v1.VolumeMountArgs(
                                    mount_path="/app/uploaded_files",
                                    name="upload-data",
                                ),
                            ],
                        )],
                        restart_policy="Always",
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

        webserver_deployment = kubernetes.apps.v1.Deployment("webserver",
            metadata=kubernetes.meta.v1.ObjectMetaArgs(
                labels={
                    "io.kompose.service": "webserver",
                },
                name="webserver",
            ),
            opts=ResourceOptions(
                depends_on=[
                    app_deployment,
                    caddy_data,
                ],
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
                            env=[kubernetes.core.v1.EnvVarArgs(
                                name="DOMAIN",
                                # value="localhost",
                                value=infra.get_output("domain_name"),
                            )],
                           # image="webserver",
                            image="mschock/webserver",
                            name="webserver",
                            ports=[
                                kubernetes.core.v1.ContainerPortArgs(
                                    container_port=443,
                                    protocol="TCP",
                                ),
                                kubernetes.core.v1.ContainerPortArgs(
                                    container_port=80,
                                    protocol="TCP",
                                ),
                            ],
                            volume_mounts=[kubernetes.core.v1.VolumeMountArgs(
                                mount_path="/root/.caddy",
                                name="caddy-data",
                            )],
                        )],
                        restart_policy="Always",
                        volumes=[kubernetes.core.v1.VolumeArgs(
                            name="caddy-data",
                            persistent_volume_claim=kubernetes.core.v1.PersistentVolumeClaimVolumeSourceArgs(
                                claim_name="caddy-data",
                            ),
                        )],
                    ),
                ),
            ))

        example1_service = kubernetes.core.v1.Service("example1",
            metadata=kubernetes.meta.v1.ObjectMetaArgs(
                name="example1",
            ),
            opts=ResourceOptions(
                depends_on=[example1_deployment],
                parent=example1_deployment,
                provider=provider,
            ),
            spec=kubernetes.core.v1.ServiceSpecArgs(
                ports=[kubernetes.core.v1.ServicePortArgs(
                    name="http",
                    port=8080,
                    protocol="TCP",
                    target_port=8080,
                )],
                selector={
                    "app": "example1",
                },
                type=kubernetes.core.v1.ServiceSpecType.CLUSTER_IP,
            ))

        example2_service = kubernetes.core.v1.Service("example2",
            metadata=kubernetes.meta.v1.ObjectMetaArgs(
                name="example2",
            ),
            opts=ResourceOptions(
                depends_on=[example2_deployment],
                parent=example2_deployment,
                provider=provider,
            ),
            spec=kubernetes.core.v1.ServiceSpecArgs(
                ports=[kubernetes.core.v1.ServicePortArgs(
                    name="http",
                    port=8080,
                    protocol="TCP",
                    target_port=8080,
                )],
                selector={
                    "app": "example2",
                },
                type=kubernetes.core.v1.ServiceSpecType.CLUSTER_IP,
            ))

        webserver_service = kubernetes.core.v1.Service("webserver",
            metadata=kubernetes.meta.v1.ObjectMetaArgs(
                labels={
                    "io.kompose.service": "webserver",
                },
                name="webserver",
            ),
            opts=ResourceOptions(
                depends_on=[webserver_deployment],
                parent=example2_deployment,
                provider=provider,
            ),
            spec=kubernetes.core.v1.ServiceSpecArgs(
                ports=[
                    kubernetes.core.v1.ServicePortArgs(
                        # name="443",
                        name="2019",
                        # port=443,
                        port=2019,
                        # target_port=443,
                        target_port=80,
                    ),
                    # kubernetes.core.v1.ServicePortArgs(
                    #     name="80",
                    #     port=80,
                    #     target_port=80,
                    # ),
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
                # skip_crds=True,
                values={
                    "ingressController": {
                        "config": {
                            "acmeCA": config.get('ingress_controller_acme_ca'),
                            "debug": config.get_bool('ingress_controller_debug'),
                            "email": config.get("ingress_controller_email"),
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

        example_ingress = kubernetes.networking.v1.Ingress("example",
            metadata=kubernetes.meta.v1.ObjectMetaArgs(
                annotations={
                    "kubernetes.io/ingress.class": "caddy",
                },
                name="example",
            ),
            opts=ResourceOptions(
                depends_on=[
                    example1_service,
                    example2_service,
                    ingress_controller,
                ],
                parent=self,
                provider=provider,
            ),
            spec=kubernetes.networking.v1.IngressSpecArgs(
                rules=[
                    kubernetes.networking.v1.IngressRuleArgs(
                        # host="example1.kubernetes.localhost",
                        host=infra.get_output("example1Fqdn"),
                        http=kubernetes.networking.v1.HTTPIngressRuleValueArgs(
                            paths=[
                                kubernetes.networking.v1.HTTPIngressPathArgs(
                                    backend=kubernetes.networking.v1.IngressBackendArgs(
                                        service=kubernetes.networking.v1.IngressServiceBackendArgs(
                                            name="example1",
                                            port=kubernetes.networking.v1.ServiceBackendPortArgs(
                                                number=8080,
                                            ),
                                        ),
                                    ),
                                    path="/hello1",
                                    path_type="Prefix",
                                ),
                                kubernetes.networking.v1.HTTPIngressPathArgs(
                                    backend=kubernetes.networking.v1.IngressBackendArgs(
                                        service=kubernetes.networking.v1.IngressServiceBackendArgs(
                                            name="example2",
                                            port=kubernetes.networking.v1.ServiceBackendPortArgs(
                                                number=8080,
                                            ),
                                        ),
                                    ),
                                    path="/hello2",
                                    path_type="Prefix",
                                ),
                            ],
                        ),
                    ),
                    kubernetes.networking.v1.IngressRuleArgs(
                        # host="example2.kubernetes.localhost",
                        host=infra.get_output("example2Fqdn"),
                        http=kubernetes.networking.v1.HTTPIngressRuleValueArgs(
                            paths=[
                                kubernetes.networking.v1.HTTPIngressPathArgs(
                                    backend=kubernetes.networking.v1.IngressBackendArgs(
                                        service=kubernetes.networking.v1.IngressServiceBackendArgs(
                                            name="example1",
                                            port=kubernetes.networking.v1.ServiceBackendPortArgs(
                                                number=8080,
                                            ),
                                        ),
                                    ),
                                    path="/hello1",
                                    path_type="Prefix",
                                ),
                                kubernetes.networking.v1.HTTPIngressPathArgs(
                                    backend=kubernetes.networking.v1.IngressBackendArgs(
                                        service=kubernetes.networking.v1.IngressServiceBackendArgs(
                                            name="example2",
                                            port=kubernetes.networking.v1.ServiceBackendPortArgs(
                                                number=8080,
                                            ),
                                        ),
                                    ),
                                    path="/hello2",
                                    path_type="Prefix",
                                ),
                            ],
                        ),
                    ),
                    kubernetes.networking.v1.IngressRuleArgs(
                        # host="example2.kubernetes.localhost",
                        host=infra.get_output("domain_name"),
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
                ],
            ))

        # labels = { 'app': 'caddy' }

        # dep = Deployment('caddy',
        #     metadata=ObjectMetaArgs(
        #         annotations={
        #             "kubernetes.io/ingress.class": "caddy",
        #         },
        #         labels=labels,
        #         name="caddy",
        #         namespace="default",
        #     ),
        #     opts=ResourceOptions(provider=render_provider),
        #     # ResourceOptions(provider=provider),
        #     spec=DeploymentSpecArgs(
        #         replicas=1,
        #         selector=LabelSelectorArgs(
        #             match_labels=labels,
        #         ),
        #         template=PodTemplateSpecArgs(
        #             metadata=ObjectMetaArgs(
        #                 annotations={
        #                     "kubernetes.io/ingress.class": "caddy",
        #                 },
        #                 labels=labels,
        #             ),
        #             spec=PodSpecArgs(
        #                 containers=[
        #                     ContainerArgs(
        #                         # args=[
        #                         #     "-listen=:8080",
        #                         #     '-text="hello world 1"',
        #                         # ],
        #                         image="caddy/caddy",
        #                         name="caddy",
        #                         ports=[
        #                             ContainerPortArgs(
        #                                 container_port=80,
        #                             )
        #                         ]
        #                     )
        #                 ]
        #             ),
        #         )
        #     )
        # )

        # svc = Service('example1',
        #     spec={
        #         # 'type': 'ClusterIP',
        #         'selector': labels,
        #         'ports': [
        #             {
        #                 'name': "2019",
        #                 'port': 2019,
        #                 'targetPort': 80,
        #             },
        #         ],
        #     },
        #     opts=ResourceOptions(provider=provider)
        #     # opts=ResourceOptions(
        #     #     providers={
        #     #         "k8s": provider,
        #     #         "k8s-yaml-rendered": render_provider
        #     #     }
        #     # )
        # )

        # ngress = Ingress(
        #     "ingress",
        #     opts=ResourceOptions(
        #         parent=ingresscontroller,
        #         # provider=render_provider
        #         provider=provider,
        #     ),
        #     spec=IngressSpecArgs(
        #         ingress_class_name="caddy",
        #         rules=[
        #             IngressRuleArgs(
        #                 host=infra.get_output("domain_name"),
        #                 http=HTTPIngressRuleValueArgs(
        #                     paths=[
        #                         HTTPIngressPathArgs(
        #                             backend=IngressBackendArgs(
        #                                 service=IngressServiceBackendArgs(
        #                                     name="caddy",
        #                                     port=ServiceBackendPortArgs(
        #                                         number=2019,
        #                                     )
        #                                 )
        #                             ),
        #                             path="/",
        #                             path_type="Prefix",
        #                         ),
        #                     ],
        #                 ),
        #             ), 
        #             IngressRuleArgs(
        #                 host=infra.get_output("wwwFqdn"),
        #                 http=HTTPIngressRuleValueArgs(
        #                     paths=[
        #                         HTTPIngressPathArgs(
        #                             backend=IngressBackendArgs(
        #                                 service=IngressServiceBackendArgs(
        #                                     name="caddy",
        #                                     port=ServiceBackendPortArgs(
        #                                         number=2019,
        #                                     )
        #                                 )
        #                             ),
        #                             path="/",
        #                             path_type="Prefix",
        #                         ),
        #                     ],
        #                 ),
        #             ),
        #         ],
        #     ),
        # )

        # Use Helm to install the Nginx ingress controller
        # ingresscontroller = kubernetes.helm.v3.Release(
        #     "ingresscontroller",
        #     chart="nginx-ingress",
        #     namespace=ingress_ns.metadata.name,
        #     repository_opts=kubernetes.helm.v3.RepositoryOptsArgs(
        #         repo="https://helm.nginx.com/stable",
        #     ),
        #     skip_crds=True,
        #     values={
        #         "controller": {
        #             "enableCustomResources": False,
        #             "appprotect": {
        #                 "enable": False,
        #             },
        #             "appprotectdos": {
        #                 "enable": False,
        #             },
        #             "service": {
        #                 "extraLabels": app_labels,
        #             },
        #         },
        #     },
        #     version="0.14.1"
        # )




# Create Stack 1
stack1 = Stack1()

# Create Stack 2
stack2 = Stack2(stack1=stack1)

# Export the consumed output
# pulumi.export('consumedOutput', stack2.consumed_output)
# pulumi.export('dropletId', stack1.register_outputs['droplet_id'])
