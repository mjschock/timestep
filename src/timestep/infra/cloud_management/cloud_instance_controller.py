import logging
import os
from typing import Dict, List, Optional

# from libcloud.compute.types import Provider as BaseProvider
from libcloud.common.types import Type
from libcloud.compute.base import (
    KeyPair,
    Node,
    NodeDriver,
    NodeImage,
    NodeLocation,
    NodeSize,
)
from libcloud.compute.providers import get_driver, set_driver

from timestep.infra.cloud_management.utils import get_or_create_key_pair

# class Provider(BaseProvider):
#     """
#     Custom provider class to support additional cloud providers.
#     """

#     MULTIPASS = "multipass"


class Provider(Type):
    """
    Defines for each of the supported providers

    Non-Dummy drivers are sorted in alphabetical order. Please preserve this
    ordering when adding new drivers.

    :cvar DUMMY: Example provider
    :cvar ABIQUO: Abiquo driver
    :cvar ALIYUN_ECS: Aliyun ECS driver.
    :cvar AURORACOMPUTE: Aurora Compute driver.
    :cvar AZURE: Azure (classic) driver.
    :cvar AZURE_ARM: Azure Resource Manager (modern) driver.
    :cvar CLOUDSIGMA: CloudSigma
    :cvar CLOUDSCALE: cloudscale.ch
    :cvar CLOUDSTACK: CloudStack
    :cvar DIMENSIONDATA: Dimension Data Cloud
    :cvar EC2: Amazon AWS.
    :cvar EXOSCALE: Exoscale driver.
    :cvar GCE: Google Compute Engine
    :cvar GRIDSCALE: gridscale
    :cvar IBM: IBM Developer Cloud
    :cvar IKOULA: Ikoula driver.
    :cvar KAMATERA: Kamatera driver
    :cvar KTUCLOUD: kt ucloud driver
    :cvar KUBEVIRT: kubevirt driver
    :cvar LIBVIRT: Libvirt driver
    :cvar LINODE: Linode.com
    :cvar NIMBUS: Nimbus
    :cvar NINEFOLD: Ninefold
    :cvar NTTC-CIS: NTT Communications CIS
    :cvar OPENNEBULA: OpenNebula.org
    :cvar OPSOURCE: Opsource Cloud
    :cvar OUTSCALE_INC: Outscale INC driver.
    :cvar OUTSCALE_SAS: Outscale SAS driver.
    :cvar OUTSCALE_SDK: Outscale SDK driver.
    :cvar RACKSPACE: Rackspace next-gen OpenStack based Cloud Servers
    :cvar RACKSPACE_FIRST_GEN: Rackspace First Gen Cloud Servers
    :cvar RIMUHOSTING: RimuHosting.com
    :cvar TERREMARK: Terremark
    :cvar UPCLOUD: UpCloud
    :cvar VCL: VCL driver
    :cvar VCLOUD: vmware vCloud
    :cvar VPSNET: VPS.net
    :cvar VSphere: VSphere driver.
    :cvar VULTR: vultr driver.
    """

    AZURE = "azure"
    AZURE_ARM = "azure_arm"
    DUMMY = "dummy"
    ABIQUO = "abiquo"
    ALIYUN_ECS = "aliyun_ecs"
    AURORACOMPUTE = "aurora_compute"
    BRIGHTBOX = "brightbox"
    CISCOCCS = "ciscoccs"
    CLOUDFRAMES = "cloudframes"
    CLOUDSIGMA = "cloudsigma"
    CLOUDSCALE = "cloudscale"
    CLOUDSTACK = "cloudstack"
    DIGITAL_OCEAN = "digitalocean"
    DIMENSIONDATA = "dimensiondata"
    EC2 = "ec2"
    EQUINIXMETAL = "equinixmetal"
    EUCALYPTUS = "eucalyptus"
    EXOSCALE = "exoscale"
    GANDI = "gandi"
    GCE = "gce"
    GIG_G8 = "gig_g8"
    GRIDSCALE = "gridscale"
    IBM = "ibm"
    IKOULA = "ikoula"
    INTERNETSOLUTIONS = "internetsolutions"
    KAMATERA = "kamatera"
    KTUCLOUD = "ktucloud"
    KUBEVIRT = "kubevirt"
    LIBVIRT = "libvirt"
    LINODE = "linode"
    MAXIHOST = "maxihost"
    MULTIPASS = "multipass"
    NIMBUS = "nimbus"
    NINEFOLD = "ninefold"
    NTTA = "ntta"
    NTTCIS = "nttcis"
    OPENNEBULA = "opennebula"
    OPENSTACK = "openstack"
    OPSOURCE = "opsource"
    OUTSCALE_INC = "outscale_inc"
    OUTSCALE_SAS = "outscale_sas"
    OUTSCALE = "outscale"
    OVH = "ovh"
    RACKSPACE = "rackspace"
    RACKSPACE_FIRST_GEN = "rackspace_first_gen"
    RIMUHOSTING = "rimuhosting"
    RUNABOVE = "runabove"
    SCALEWAY = "scaleway"
    TERREMARK = "terremark"
    UPCLOUD = "upcloud"
    VCL = "vcl"
    VCLOUD = "vcloud"
    VPSNET = "vpsnet"
    VSPHERE = "vsphere"
    VULTR = "vultr"

    # OpenStack based providers
    HPCLOUD = "hpcloud"
    ONAPP = "onapp"

    # Deprecated constants which aren't supported anymore
    RACKSPACE_UK = "rackspace_uk"
    RACKSPACE_NOVA_BETA = "rackspace_nova_beta"
    RACKSPACE_NOVA_DFW = "rackspace_nova_dfw"
    RACKSPACE_NOVA_LON = "rackspace_nova_lon"
    RACKSPACE_NOVA_ORD = "rackspace_nova_ord"

    EC2_US_EAST = "ec2_us_east"
    EC2_US_EAST_OHIO = "ec2_us_east_ohio"
    EC2_EU = "ec2_eu_west"  # deprecated name
    EC2_EU_WEST = "ec2_eu_west"
    EC2_EU_WEST2 = "ec2_eu_west_london"
    EC2_US_WEST = "ec2_us_west"
    EC2_AP_SOUTHEAST = "ec2_ap_southeast"
    EC2_AP_NORTHEAST = "ec2_ap_northeast"
    EC2_AP_NORTHEAST1 = "ec2_ap_northeast_1"
    EC2_AP_NORTHEAST2 = "ec2_ap_northeast_2"
    EC2_US_WEST_OREGON = "ec2_us_west_oregon"
    EC2_SA_EAST = "ec2_sa_east"
    EC2_AP_SOUTHEAST2 = "ec2_ap_southeast_2"
    EC2_CA_CENTRAL1 = "ec2_ca_central_1"

    CLOUDSIGMA_US = "cloudsigma_us"

    # Removed
    # SLICEHOST = 'slicehost'


class CloudInstanceController:
    """
    Manages cloud instances by finding the most cost-effective option
    across multiple cloud providers.
    """

    def __init__(self, credentials: Dict[str, Dict]):
        """
        Initialize cloud instance controller with credentials for multiple providers.

        Args:
            credentials (Dict[str, Dict]): A dictionary of cloud provider credentials
                Example: {
                    'aws': {'key': 'aws_access_key', 'secret': 'aws_secret_key'},
                    'digital_ocean': {'key': 'do_access_key'},
                    'gcp': {'key': 'gcp_service_account_key'}
                }
        """
        self.providers = {}
        self.logger = logging.getLogger(__name__)

        # Map of cloud providers supported by libcloud
        provider_map = {
            "aws": Provider.EC2,
            "azure": Provider.AZURE,
            "digital_ocean": Provider.DIGITAL_OCEAN,
            "dummy": Provider.DUMMY,
            "gcp": Provider.GCE,
            "linode": Provider.LINODE,
            "multipass": Provider.MULTIPASS,
        }

        set_driver(
            Provider.MULTIPASS,
            "timestep.infra.cloud_management.drivers.multipass",
            "MultipassNodeDriver",
        )

        # Initialize drivers for each provider
        for provider, creds in credentials.items():
            try:
                driver_class = get_driver(provider_map.get(provider))

                self.providers[provider] = driver_class(**creds)
                self.logger.info(f"Initialized {provider} cloud driver")

            except Exception as e:
                self.logger.error(f"Failed to initialize {provider} driver: {e}")
                raise e

    def create_instance(
        self,
        driver: NodeDriver,
        image: NodeImage,
        location: NodeLocation,
        name: str,
        ssh_key: str,
        size: NodeSize,
    ) -> Node:
        """
        Create the most cost-effective cloud instance matching specified requirements.

        Args:
            driver (NodeDriver): Cloud provider driver
            image (NodeImage): Image to use for the instance
            location (NodeLocation): Location to deploy the instance
            name (str): Name of the instance
            ssh_key (str): SSH key to use for the instance
            size (NodeSize): Instance size specifications

        Returns:
            Node: Created instance object
        """
        try:
            key_file_path = os.path.expanduser(f"{ssh_key}.pub")

            with open(key_file_path) as fp:
                key_material = fp.read()

            key_pair: KeyPair = get_or_create_key_pair(driver, name, key_material)

            node = driver.create_node(
                ex_create_attr={"ssh_keys": [key_pair.fingerprint]},
                name=name,
                image=image,
                location=location,
                size=size,
            )

            self.logger.info(f"Created instance: {node}")

            return node

        except Exception as e:
            self.logger.error(f"Failed to create instance: {e}")
            raise

    def find_matching_images(
        self,
        driver: NodeDriver,
        allowed_image_ids: List[str] = None,
        allowed_image_names: List[str] = None,
    ) -> List[NodeImage]:
        """
        Find images across providers that match allowed IDs or names.

        Args:
            driver (NodeDriver): Cloud provider driver
            allowed_image_ids (List[str], optional): Specific image IDs to match
            allowed_image_names (List[str], optional): Name patterns to match

        Returns:
            List[NodeImage]: List of matching images
        """
        matching_images = []

        try:
            images = driver.list_images()

            # Filter images based on IDs and names
            provider_matches = []

            for image in images:
                # Check if image matches any allowed ID
                id_match = (not allowed_image_ids) or (image.id in allowed_image_ids)

                # Check if image matches any name pattern
                name_match = (not allowed_image_names) or any(
                    name.lower() == str(image.name).lower()
                    for name in allowed_image_names
                )

                if id_match or name_match:
                    provider_matches.append(image)

            matching_images.extend(provider_matches)

        except Exception as e:
            self.logger.warning(f"Error finding images for {driver}: {e}")

        return matching_images

    def find_matching_locations(
        self,
        driver: NodeDriver,
        allowed_location_countries: List[str] = None,
        allowed_location_ids: List[str] = None,
        allowed_location_names: List[str] = None,
    ) -> List[NodeLocation]:
        """
        Find locations across providers, optionally filtering by preferred regions.

        Args:
            driver (NodeDriver): Cloud provider driver
            allowed_location_countries (List[str], optional): Country names to match
            allowed_location_ids (List[str], optional): Specific location IDs to match
            allowed_location_names (List[str], optional): Name patterns to match

        Returns:
            List[NodeLocation]: List of matching locations
        """
        matching_locations = []

        try:
            locations = driver.list_locations()

            # Filter locations if preferred regions specified
            provider_matches = []

            for location in locations:
                # Check if image matches any allowed ID
                country_match = (not allowed_location_countries) or any(
                    country.lower() == str(location.country).lower()
                    for country in allowed_location_countries
                )

                id_match = (not allowed_location_ids) or (
                    location.id in allowed_location_ids
                )

                # Check if image matches any name pattern
                name_match = (not allowed_location_names) or any(
                    name.lower() == str(location.name).lower()
                    for name in allowed_location_names
                )

                if country_match or id_match or name_match:
                    provider_matches.append(location)

            matching_locations.extend(provider_matches)

        except Exception as e:
            self.logger.warning(f"Error finding locations for {driver}: {e}")

        return matching_locations

    def find_matching_sizes(self, specs: Dict, limit: int = 3) -> List[NodeSize]:
        """
        Retrieve and compare instance pricing across providers.

        Args:
            specs (Dict): Desired instance specifications
                {
                    'min_cpu': int,  # Minimum number of CPUs
                    'min_bandwidth': int,  # Minimum bandwidth in Mbps
                    'min_disk': int,  # Minimum disk size in GB
                    'min_ram': int,  # Minimum RAM in MB
                }

        Returns:
            List[NodeSize]: List of matching instance sizes
        """
        available_instances = []

        for provider_name, driver in self.providers.items():
            try:
                # Fetch available nodes matching specifications
                sizes = driver.list_sizes()

                for size in sizes:
                    if (
                        (
                            specs["min_bandwidth"] is None
                            or size.bandwidth >= specs["min_bandwidth"]
                        )
                        and (
                            specs["min_cpu"] is None
                            or size.extra["vcpus"] >= specs["min_cpu"]
                        )
                        and (
                            specs["min_disk"] is None or size.disk >= specs["min_disk"]
                        )
                        and size.price > 0
                        and (specs["min_ram"] is None or size.ram >= specs["min_ram"])
                    ):
                        available_instances.append(
                            size,
                        )

            except Exception as e:
                self.logger.warning(
                    f"Error fetching instances for {provider_name}: {e}"
                )

        # Sort instances by hourly cost
        return sorted(available_instances, key=lambda x: int(x.price))[0:limit]

    def get_instance_by_name(self, driver: NodeDriver, name: str) -> Optional[Node]:
        """
        Retrieve a cloud instance by name.

        Args:
            name (str): Name of the instance to retrieve

        Returns:
            Node: Instance object if found, else None
        """
        try:
            nodes = driver.list_nodes()
            return next((node for node in nodes if node.name == name), None)

        except Exception as e:
            self.logger.error(f"Error fetching instance by name: {e}")
            return None

    def terminate_instance(self, instance_id: str, provider: Optional[str] = None):
        """
        Terminate a specific cloud instance.

        Args:
            instance_id (str): Unique identifier of the instance to terminate
            provider (Optional[str]): Specific provider (if known)
        """
        if provider:
            # If provider is specified, use its driver
            driver = self.providers.get(provider)
            if not driver:
                raise ValueError(f"Provider {provider} not initialized")

            nodes = driver.list_nodes()
            target_node = next((node for node in nodes if node.id == instance_id), None)

            if target_node:
                driver.destroy_node(target_node)
                self.logger.info(f"Terminated instance {instance_id} on {provider}")
            else:
                raise ValueError(f"Instance {instance_id} not found on {provider}")

        else:
            # If no provider specified, search across all providers
            for provider_name, driver in self.providers.items():
                try:
                    nodes = driver.list_nodes()
                    target_node = next(
                        (node for node in nodes if node.id == instance_id), None
                    )

                    if target_node:
                        driver.destroy_node(target_node)
                        self.logger.info(
                            f"Terminated instance {instance_id} on {provider_name}"
                        )
                        return

                except Exception as e:
                    self.logger.warning(f"Error searching {provider_name}: {e}")

            raise ValueError(f"Instance {instance_id} not found on any provider")
