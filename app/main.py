import os
from typing import Union

from fastapi import FastAPI
from prefect.deployments import Deployment
from prefect.server.schemas.schedules import CronSchedule

from app.flows import repo_info

app = FastAPI()


@app.get("/api/")
def read_root():
    # return {"Hello": "World"}
    prefect_api_url = os.environ.get("PREFECT_API_URL")
    return {"PREFECT_API_URL": prefect_api_url}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/prefect/deployments")
def create_deployment(repo_owner: str = "PrefectHQ", repo_name: str = "prefect"):
    deployment = Deployment.build_from_flow(
        flow=repo_info,
        name="example-deployment",
        parameters={
            "repo_owner": repo_owner,
            "repo_name": repo_name,
        },
        version=1,
        schedule=(CronSchedule(cron="* * * * *", timezone="America/Los_Angeles")),
        work_queue_name="default",
        work_pool_name="default-agent-pool",
    )
    deployment.apply()
