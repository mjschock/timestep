# Work

Copied and modified from https://github.com/mjschock/timestep/pull/85#issue-2438922792

## Create tickets for line of work
- [ ] Migrate mjschock/timestep to Timestep-AI/timestep
  - [x] Delete Timestep-AI/timestep
  - [x] Transfer mjschock/timestep to Timestep-AI/timestep
  - [ ] Verify that GitLab is still mirroring correctly (and make sure it's open)
 
- [ ] Add GitHub workflows for lightest Linux/Mac/Windows that have at least the following jobs:
  - CLI test:
     -  `pipx install timestep` followed by `timestep --version ` assertion
     -  Idea A:
        - [ ] `timestep serve`;
     - Idea B:
       - [ ] `timestep up`; `URL=http://localhost:8000 bash -c "$(curl -fsSL https://agentprotocol.ai/test.sh)"`
    `URL=http://localhost:8000 bash -c "$(curl -fsSL https://agentprotocol.ai/test.sh)"`
    - Dev test(`git clone https://github.com/Timestep-AI/timestep.git`; `make`; followed by, e.g.:
      - `timestep up`
      - `timestep verify` which would invoke tests including ap test, agent/model performance tests, or others such as agbenchmark, hf leader boards, berkeley tool-calling leaderboards, etc.
    - * could alternatively be `timestep serve` followed by `timestep evals ...` but aiming to limit to at most 3 commands (e.g. evals, serve, train) or maybe one (timestep up with options such as `timestep up --domain timestep.local --target local --verify` or `timestep up --domain timestep.ai --target remote --verify`

- [ ] Implement Target Option
    - By default, timestep will deploy an OpenAI and Agent Protocol conforming API spec at localhost
    - You will be able to choose a remote target where we'll use libcloud to pick the cheapest/nearest/fastest Ubuntu instance where we'll use arcade plus k3sup to install our primary k3s node. We'll also provide the ability to select an object store using libcloud with the default using the licloud code for local (e.g., the files controller will store files locally using the same api - we're aiming to keep the same logic across all targets, using the config to determine behavior)
    - with the k3s primary node installed, we can then install a Helm chart for Prefect Server, a Prefect Worker, and Timestep Server. 
    - The same `step` workflow will run for long-running work such as ControlFlow Multi-Agent agent step invocations
      - When each agent takes a step, it will not only return it's step output but we'll use it's step input to determine whether it is in training mode. In inference mode (default), it will run an agent flow and return the step output might include the predictions made. In training mode, the agent will clone run training on it's models as configured in the step input (e.g., hyperameters, target model, etc.).  Artifacts will be tracked in prefect with larger data referenced to local disk / Prefect with libcloud wrapping
     - The default training strategy will git clone llama-cpp and use the fine-tuning cli to run training.
     - In any case, the default serving strategy will wrap the defafult models in the default agent which will conform to the ap spec and the OpenAI API with a set of Jupyter notebooks showcasing how to use various OpenAI compatable libraries with a local instance of timestep-ai simply by replacing the OPENAI_API_KEY to locahost.

- Other things on the horizon
  - thinking of various generalizations:
    - assistants_controller controls agents with models and tools
    - audio_controller tracks the default agent with default models and audio control tools
    - batch_controller runs agent step flow deployments in parallel, optionally scaling out to the cloud with libcloud/sky-pilot
    - chat_controller runs the chat completions against the default agent's default model.
    - completions_controller does the same
    - embeddings_controller does the same, using the default agent's default embedding model
    - files_controller controls file io using libcloud and prefect artifacts
    - fine_tuning_controller runs training for an agent and it's models
    - images_controller controls agents with models image editing/generation tools
    - models_controller controls model persistance in memory and/or on-device/in-the-cloud
    - moderations_controller controls agent moderation (e.g., use Llama Guard to moderate agent behavior)
    - vector_stores_controller by default uses a libcloud local store and SQLlite plus sqllite-vec to back a RAG-tool
    - agent_controller satisfies ap protocal using the default agent and it's default models/tools (how we namespace the agent is TBD)
       - security_controller controls authz and we could move this to v2 api
  - tests run app tests, code test suites, integration tests, agent/model tests, locust tests, jupyter notebooks, etc. (should this be equivalent to `timestep evals` or `timestep test(s)` or `timestep verify`?)
  - `timestep serve` would, by default, not only expose the API above, but also, optionally, run training of the default agent and it's models to learn to better invoke it's tools and generate predictions
  - 