import random

import controlflow as cf
from langchain_openai import ChatOpenAI
from pydantic import BaseModel

model = ChatOpenAI(
    temperature=0.0,
)

cf.default_model = model


class StepOutput(BaseModel):
    rolls: list[int]


# this function will be used as a tool by task 2
def roll_dice(n: int) -> int:
    '''Roll n dice'''
    return [random.randint(1, 6) for _ in range(n)]

@cf.flow
def dice_flow():

    # task 1: ask the user how many dice to roll
    user_task = cf.Task(
        "Ask the user how many dice to roll", 
        result_type=int, 
        user_access=True
    )

    # task 2: roll the dice
    dice_task = cf.Task(
        "Roll the dice",
        context=dict(n=user_task),
        tools=[roll_dice],
        #result_type=list[int],
        result_type=StepOutput,
    )

    return dice_task


# run the workflow
result = dice_flow()
print(result)

with open("results.txt", "w") as f:
    f.write(f"{result}")

