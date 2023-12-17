import argparse

# import os
import uvicorn

# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/ready")
# async def get_ready():
#     return {
#         "ready": "okay",
#         "cwd": os.getcwd(),
#         # "files": os.listdir("."),
#     }

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--reload", action="store_true")
    args = parser.parse_args()

    print("args", args)
    print("args.reload", args.reload)

    # uvicorn_config = uvicorn.Config(
    #     # "src.web.app.main:app",
    #     # "app.main:app",
    #     # "web.app.main:app",
    #     # "web.server:app",
    #     # "server:app",
    #     "main:app",
    #     host="0.0.0.0",
    #     port=5000,
    #     proxy_headers=True,
    #     reload=args.reload,
    #     # reload_dirs=[
    #     #     "src/web/api",
    #     # ],
    # )
    # server = uvicorn.Server(uvicorn_config)
    # server.run()

    # uvicorn.run("main:app", port=5000, reload=True, access_log=False)
    # uvicorn.run("main:app", port=5000, reload=True, access_log=False, host="0.0.0.0", proxy_headers=True)  # noqa: E501
    uvicorn.run(
        "app.main:app",
        port=5000,
        reload=True,
        access_log=False,
        host="0.0.0.0",
        proxy_headers=True,
    )  # noqa: E501
