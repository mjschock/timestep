import logging
import os
from typing import Dict, List, Optional

from libcloud.compute.base import (
    KeyPair,
    Node,
    NodeDriver,
    NodeImage,
    NodeLocation,
    NodeSize,
)
from libcloud.compute.providers import get_driver
from libcloud.compute.types import Provider

from timestep.infra.cloud_management.utils import get_or_create_key_pair


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
        }

        # Initialize drivers for each provider
        for provider, creds in credentials.items():
            try:
                driver_class = get_driver(provider_map.get(provider))

                self.providers[provider] = driver_class(**creds)
                self.logger.info(f"Initialized {provider} cloud driver")

            except Exception as e:
                self.logger.error(f"Failed to initialize {provider} driver: {e}")

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
