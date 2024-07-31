`timestep serve`
- prefect server start in background
- prefect worker start in background
- llamafile serve in background
    - if hf, pull repo
    - if not gguf, convert
    - run llamafile in background pointing to external weights
- start timestep server
    - register LangChain Llamafile model in agent_service default agent

`agent.step()`
- optionally, train
