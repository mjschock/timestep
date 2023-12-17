class AgentsService:
    def __init__(self, q: str | None = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit

    async def create_agent(self):
        agent_id = "agent_id"

        return agent_id


async def get_agent_service(q: str | None = None, skip: int = 2, limit: int = 100):
    return AgentsService(q=q, skip=skip, limit=limit)
