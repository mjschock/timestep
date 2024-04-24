import mesa


# class Agent(mesa.Agent):
# TODO: Take inspiration from https://pettingzoo.farama.org/tutorials/langchain/langchain/#gymnasium-agent
class Agent:
    """
    An agent.
    """

    # def __init__(self, unique_id, model):
    #     """
    #     Customize the agent
    #     """
    #     self.unique_id = unique_id
    #     super().__init__(unique_id, model)

    # def step(self):
    #     """
    #     Modify this method to change what an individual agent will do during each step.
    #     Can include logic based on neighbors states.
    #     """
    #     pass

    def act(self, observation):
        """
        Choose an action based on the observation.
        """
        action = None

        return action
