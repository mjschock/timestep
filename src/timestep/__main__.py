from cdktf import App

from timestep.config import Settings
from timestep.infra.stacks.main.stack import MainStack


def main() -> None:
    config = Settings()
    app: App = App(
        context={
            "allowSepCharsInLogicalIds": "true",
            "excludeStackIdFromLogicalIds": "true",
        },
        outdir=config.cdktf_outdir,
        skip_validation=False,
        stack_traces=True,
    )

    assert app.node.get_context("allowSepCharsInLogicalIds") == "true"
    assert app.node.get_context("excludeStackIdFromLogicalIds") == "true"

    MainStack(
        config=config,
        id=config.primary_domain_name,
        scope=app,
    )

    app.synth()


if __name__ == "__main__":
    main()
