class AgentsService:
    async def create_agent(self):
        return {"message": "Agent created"}


async def init_agents_service():
    return AgentsService()
