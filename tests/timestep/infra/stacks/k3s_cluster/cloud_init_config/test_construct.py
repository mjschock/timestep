from cdktf import TerraformStack, Testing
from cdktf_cdktf_provider_local.data_local_file import DataLocalFile
from cdktf_cdktf_provider_local.provider import LocalProvider
from timestep.config import Settings
from timestep.infra.stacks.k3s_cluster.cloud_init_config.construct import (
    CloudInitConfigConstruct,
)

# The tests below are example tests, you can find more information at
# https://cdk.tf/testing


class TestMain:
    mock_app = Testing.app()
    mock_config = Settings(
        cdktf_outdir=mock_app.outdir,
    )

    stack = TerraformStack(mock_app, "stack")

    cloud_init_config_construct_abstraction = CloudInitConfigConstruct(
        config=mock_config,
        id="cloud_init_config_construct",
        scope=stack,
    )

    synthesized = Testing.synth(stack)

    def test_should_have_a_local_provider(self):
        assert Testing.to_have_provider(
            self.synthesized,
            LocalProvider.TF_RESOURCE_TYPE,
        )

    def test_should_have_a_data_local_file(self):
        assert Testing.to_have_resource(
            self.synthesized,
            DataLocalFile.TF_RESOURCE_TYPE,
        )

    def test_check_validity(self):
        assert Testing.to_be_valid_terraform(Testing.full_synth(self.stack))
