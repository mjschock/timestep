# Objectives

- Picks the cheapest cloud instance (currently only Multipass and DigitalOcean are supported) to deploy a primary k3s node
- Uses SkyPilot to run compute at any scale, optimizing for the cheapest (or nearest) compute across all clouds (currently only Kubernetes and Paperspace are supported)
- Follows the princples of the 12-factor app (e.g., where the same logic is run whether deploying to local or prod, differentiated only by config pulled in from the environment)
- The primary node supports Dora and ROS 2
- Automatic HTTPs is provided both locally and on the Internet via Caddy
- Boilerplate logic for serving a multi-agent system is included (backed by a lightweight open-source multimodal modal with tools, by default)
    - Use any commercial model by providing keys
    - The multi-agent system is boot up first to run as a developer team with checks
        - Agent protocol API conformity for each agent
- Each environment conforms to the PettingZoo standard
