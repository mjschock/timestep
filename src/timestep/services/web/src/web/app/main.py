from fastapi import FastAPI

from .routers import agents

# app = FastAPI(dependencies=[Depends(get_query_token)])
app = FastAPI()


def get_ready_flow():
    return {
        "ready": "okay",
    }


@app.get("/ready")
async def get_ready():
    return get_ready_flow()


app.include_router(agents.router)
# app.include_router(users.router)
# app.include_router(items.router)
# app.include_router(
#     admin.router,
#     prefix="/admin",
#     tags=["admin"],
#     dependencies=[Depends(get_token_header)],
#     responses={418: {"description": "I'm a teapot"}},
# )


# @app.get("/")
# async def root():
#     return {"message": "Hello Bigger Applications!"}
