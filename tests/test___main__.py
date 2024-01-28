# from cdktf import TerraformStack, Testing

# # The tests below are example tests, you can find more information at
# # https://cdk.tf/testing


# class TestMain:
#     stack = TerraformStack(Testing.app(), "stack")
#     # app_abstraction = MyApplicationsAbstraction(stack, "app-abstraction")
#     # synthesized = Testing.synth(stack)

#     # def test_should_contain_container(self):
#     #    assert Testing.to_have_resource(self.synthesized, Container.TF_RESOURCE_TYPE)

#     # def test_should_use_an_ubuntu_image(self):
#     #    assert Testing.to_have_resource_with_properties(
#     #       self.synthesized, Image.TF_RESOURCE_TYPE, {
#     #        "name": "ubuntu:latest",
#     #    })

#     # def test_check_validity(self):
#     #    assert Testing.to_be_valid_terraform(Testing.full_synth(stack))

import pytest
from prefect import flow
from prefect.testing.utilities import prefect_test_harness
from prefect_shell import ShellOperation


@pytest.fixture(autouse=True, scope="session")
def prefect_test_fixture():
    with prefect_test_harness():
        yield

@flow
def agent_protocol_check(agent_id="default"):
    shell_output = ShellOperation(
        commands=[
            "set -e",
            f"URL=https://www.$PRIMARY_DOMAIN_NAME/api/agents/{agent_id} bash tests/test.sh" # TODO: fix for needing www since redir is changing to GET  # noqa: E501
        ]
    ).run()

    return shell_output

def test_default_agent():
    assert agent_protocol_check() == "ok"
