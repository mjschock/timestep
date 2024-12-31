""" Salad Cloud. """

import typing
from typing import Dict, Iterator, List, Optional, Tuple, Union

import requests

from sky import clouds
from sky.clouds import service_catalog
from sky.utils import resources_utils

if typing.TYPE_CHECKING:
    from sky import resources as resources_lib

_CREDENTIAL_FILES = [
    # credential files for Salad Cloud
    'config.json',
]

@clouds.CLOUD_REGISTRY.register
class SaladCloud(clouds.Cloud):
    """Salad GPU Cloud"""

    _REPR = 'SaladCloud'
    _CLOUD_UNSUPPORTED_FEATURES = {
        clouds.CloudImplementationFeatures.CLONE_DISK_FROM_CLUSTER:
            'Migrating '
            f'disk is not supported in {_REPR}.',
        clouds.CloudImplementationFeatures.IMAGE_ID:
            'Specifying image ID '
            f'is not supported for {_REPR}.',
        clouds.CloudImplementationFeatures.CUSTOM_DISK_TIER:
            'Custom disk tiers'
            f' is not supported in {_REPR}.',
    }
    _MAX_CLUSTER_NAME_LEN_LIMIT = 120
    _regions: List[clouds.Region] = []

    # Using the latest SkyPilot provisioner API
    PROVISIONER_VERSION = clouds.ProvisionerVersion.SKYPILOT
    STATUS_VERSION = clouds.StatusVersion.SKYPILOT

    @classmethod
    def _unsupported_features_for_resources(
        cls, resources: 'resources_lib.Resources'
    ) -> Dict[clouds.CloudImplementationFeatures, str]:
        """Returns unsupported features based on the provided resources."""
        del resources  # unused
        return cls._CLOUD_UNSUPPORTED_FEATURES

    @classmethod
    def _max_cluster_name_length(cls) -> Optional[int]:
        return cls._MAX_CLUSTER_NAME_LEN_LIMIT

    @classmethod
    def regions_with_offering(
        cls,
        instance_type: str,
        accelerators: Optional[Dict[str, int]],
        use_spot: bool,
        region: Optional[str],
        zone: Optional[str],
    ) -> List[clouds.Region]:
        assert zone is None, 'Salad Cloud does not support zones.'
        del accelerators, zone  # unused

        regions = service_catalog.get_region_zones_for_instance_type(
            instance_type, use_spot, 'salad')

        if region is not None:
            regions = [r for r in regions if r.name == region]
        return regions

    @classmethod
    def get_vcpus_mem_from_instance_type(
        cls,
        instance_type: str,
    ) -> Tuple[Optional[float], Optional[float]]:
        return service_catalog.get_vcpus_mem_from_instance_type(
            instance_type, clouds='salad')

    @classmethod
    def zones_provision_loop(
        cls,
        *,
        region: str,
        num_nodes: int,
        instance_type: str,
        accelerators: Optional[Dict[str, int]] = None,
        use_spot: bool = False,
    ) -> Iterator[None]:
        del num_nodes  # unused
        regions = cls.regions_with_offering(instance_type,
                                          accelerators,
                                          use_spot,
                                          region=region,
                                          zone=None)
        for r in regions:
            assert r.zones is None, r
            yield r.zones

    def instance_type_to_hourly_cost(
        self,
        instance_type: str,
        use_spot: bool,
        region: Optional[str] = None,
        zone: Optional[str] = None,
    ) -> float:
        return service_catalog.get_hourly_cost(
            instance_type,
            use_spot=use_spot,
            region=region,
            zone=zone,
            clouds='salad',
        )

    def accelerators_to_hourly_cost(
        self,
        accelerators: Dict[str, int],
        use_spot: bool,
        region: Optional[str] = None,
        zone: Optional[str] = None,
    ) -> float:
        """Returns the hourly cost of accelerators in dollars/hour."""
        del accelerators, use_spot, region, zone  # unused
        return 0.0

    def get_egress_cost(self, num_gigabytes: float) -> float:
        return 0.0

    def __repr__(self):
        return self._REPR

    @classmethod
    def get_default_instance_type(
        cls,
        cpus: Optional[str] = None,
        memory: Optional[str] = None,
        disk_tier: Optional[resources_utils.DiskTier] = None,
    ) -> Optional[str]:
        """Returns the default instance type for Salad Cloud."""
        return service_catalog.get_default_instance_type(cpus=cpus,
                                                       memory=memory,
                                                       disk_tier=disk_tier,
                                                       clouds='salad')

    @classmethod
    def get_accelerators_from_instance_type(
            cls, instance_type: str) -> Optional[Dict[str, Union[int, float]]]:
        return service_catalog.get_accelerators_from_instance_type(
            instance_type, clouds='salad')

    @classmethod
    def get_zone_shell_cmd(cls) -> Optional[str]:
        return None

    def make_deploy_resources_variables(
            self,
            resources: 'resources_lib.Resources',
            cluster_name: resources_utils.ClusterName,
            region: 'clouds.Region',
            zones: Optional[List['clouds.Zone']],
            num_nodes: int,
            dryrun: bool = False) -> Dict[str, Optional[str]]:
        del zones, dryrun, cluster_name

        r = resources
        acc_dict = self.get_accelerators_from_instance_type(r.instance_type)
        custom_resources = resources_utils.make_ray_custom_resources_str(
            acc_dict)

        return {
            'instance_type': resources.instance_type,
            'custom_resources': custom_resources,
            'region': region.name,
        }

    def _get_feasible_launchable_resources(
            self, resources: 'resources_lib.Resources'):
        """Returns a list of feasible resources for the given resources."""
        if resources.instance_type is not None:
            assert resources.is_launchable(), resources
            resources = resources.copy(accelerators=None)
            return resources_utils.FeasibleResources([resources], [], None)

        def _make(instance_list):
            resource_list = []
            for instance_type in instance_list:
                r = resources.copy(
                    cloud=SaladCloud(),
                    instance_type=instance_type,
                    accelerators=None,
                    cpus=None,
                )
                resource_list.append(r)
            return resource_list

        # Handle filter on accelerators
        accelerators = resources.accelerators
        if accelerators is None:
            # Return a default instance type
            default_instance_type = SaladCloud.get_default_instance_type(
                cpus=resources.cpus,
                memory=resources.memory,
                disk_tier=resources.disk_tier)
            if default_instance_type is None:
                return resources_utils.FeasibleResources([], [], None)
            else:
                return resources_utils.FeasibleResources(
                    _make([default_instance_type]), [], None)

        assert len(accelerators) == 1, resources
        acc, acc_count = list(accelerators.items())[0]
        (instance_list, fuzzy_candidate_list) = (
            service_catalog.get_instance_type_for_accelerator(
                acc,
                acc_count,
                use_spot=resources.use_spot,
                cpus=resources.cpus,
                memory=resources.memory,
                region=resources.region,
                zone=resources.zone,
                clouds='salad',
            ))
        if instance_list is None:
            return resources_utils.FeasibleResources([], fuzzy_candidate_list,
                                                   None)
        return resources_utils.FeasibleResources(_make(instance_list),
                                               fuzzy_candidate_list, None)

    @classmethod
    def check_credentials(cls) -> Tuple[bool, Optional[str]]:
        """Verify that the user has valid credentials for Salad Cloud."""
        try:
            # Test credentials endpoint from API spec
            response = requests.get('https://api.salad.com/api/public/')
            if response.status_code == 204:
                return True, None
            return False, ('Failed to authenticate with Salad Cloud. '
                         'Please check your credentials.')
        except requests.exceptions.ConnectionError:
            return False, ('Failed to verify Salad Cloud credentials. '
                         'Check your network connection.')
        except Exception as e:  # pylint: disable=broad-except
            return False, str(e)

    def get_credential_file_mounts(self) -> Dict[str, str]:
        return {
            f'~/.salad/{filename}': f'~/.salad/{filename}'
            for filename in _CREDENTIAL_FILES
        }

    @classmethod
    def get_user_identities(cls) -> Optional[List[List[str]]]:
        return None

    def instance_type_exists(self, instance_type: str) -> bool:
        return service_catalog.instance_type_exists(instance_type, 'salad')

    def validate_region_zone(self, region: Optional[str], zone: Optional[str]):
        return service_catalog.validate_region_zone(region,
                                                  zone,
                                                  clouds='salad')
