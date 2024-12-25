import asyncio
import json
import os
from contextlib import asynccontextmanager
from enum import Enum

import flet as ft
import flet.fastapi as flet_fastapi
import uvicorn
from connexion import AsyncApp, ConnexionMiddleware
from connexion.options import SwaggerUIOptions
from fastapi import FastAPI, Request
from openai import AsyncOpenAI

from timestep.config import settings

app_dir = settings.app_dir
connexion_app = AsyncApp(import_name=__name__)
default_hf_repo_id = settings.default_hf_repo_id

client = AsyncOpenAI(
    api_key="sk-no-key-required",
    # base_url="http://localhost:8080/v1",
    base_url="http://localhost:8000/v1",
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        print("=== Lifespan startup ===")

        await flet_fastapi.app_manager.start()
        yield
        await flet_fastapi.app_manager.shutdown()

    finally:
        print("=== Lifespan cleanup ===")
        print("Shutting down...")


fastapi_app = FastAPI(
    lifespan=lifespan,
    # servers= # TODO: add server for testing?
)

# connexion_app.add_api(
#     "api/openai/v1/openapi/openapi.yaml",
#     base_path="/openai/v1",
#     pythonic_params=True,
#     resolver_error=500,
# )

fastapi_app.mount("/api", ConnexionMiddleware(app=connexion_app, import_name=__name__))


class Message:
    def __init__(self, user_name: str, text: str, message_type: str):
        self.user_name = user_name
        self.text = text
        self.message_type = message_type


class ChatMessage(ft.Row):
    def __init__(self, message: Message):
        super().__init__()

        self.user_name_view = ft.Text(message.user_name, weight="bold")
        self.text_view = ft.Text(message.text, selectable=True)

        self.controls = [
            ft.CircleAvatar(
                content=ft.Text(self.get_initials(message.user_name)),
                color=ft.colors.WHITE,
                bgcolor=self.get_avatar_color(message.user_name),
            ),
            ft.Column(
                [
                    # ft.Text(message.user_name, weight="bold"),
                    self.user_name_view,
                    # ft.Text(message.text, selectable=True),
                    # ft.Text(self.text, selectable=True),
                    self.text_view,
                ],
                tight=True,
                spacing=5,
            ),
        ]
        self.vertical_alignment = ft.CrossAxisAlignment.START

    def get_initials(self, user_name: str):
        if user_name:
            return user_name[:1].capitalize()

        else:
            return "Unknown"  # or any default value you prefer

    def get_avatar_color(self, user_name: str):
        colors_lookup = [
            ft.colors.AMBER,
            ft.colors.BLUE,
            ft.colors.BROWN,
            ft.colors.CYAN,
            ft.colors.GREEN,
            ft.colors.INDIGO,
            ft.colors.LIME,
            ft.colors.ORANGE,
            ft.colors.PINK,
            ft.colors.PURPLE,
            ft.colors.RED,
            ft.colors.TEAL,
            ft.colors.YELLOW,
        ]

        return colors_lookup[hash(user_name) % len(colors_lookup)]

    def to_dict(self):
        if self.user_name_view.value == "Assistant":
            role = "assistant"

        elif self.user_name_view.value == "System":
            role = "system"

        else:
            role = "user"

        return {
            "content": self.text_view.value,
            "role": role,
        }

    def update_text(self, text: str):
        self.text_view.value = text
        self.update()


# async def main(page: ft.Page):
async def root_main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
    page.title = "Chat"

    def join_chat_click(e):
        if not join_user_name.value:
            join_user_name.error_text = "Name cannot be blank!"
            join_user_name.update()

        else:
            page.session.set("user_name", join_user_name.value)
            page.dialog.open = False
            new_message.prefix = ft.Text(f"{join_user_name.value}: ")
            page.pubsub.send_all(
                Message(
                    user_name=join_user_name.value,
                    text=f"{join_user_name.value} has joined the chat.",
                    message_type="login_message",
                )
            )
            page.update()

    def send_message_click(e):
        if new_message.value != "":
            page.pubsub.send_all(
                Message(
                    page.session.get("user_name"),
                    new_message.value,
                    message_type="chat_message",
                )
            )
            new_message.value = ""
            new_message.focus()
            page.update()

    async def on_message(message: Message):
        if message.message_type == "chat_message":
            m = ChatMessage(message)

        elif message.message_type == "login_message":
            # m = ft.Text(message.text, italic=True, color=ft.colors.BLACK45, size=12)
            m = ft.Text(message.text, italic=True, color=ft.colors.WHITE, size=12)

        chat.controls.append(m)
        page.update()

        if message.message_type == "chat_message" and not message.user_name in (
            "Assistant",
            "System",
        ):
            messages = [
                chat_message.to_dict()
                for chat_message in chat.controls
                if type(chat_message) == ChatMessage
            ]

            print("messages:")
            print(messages)

            assistant_message = ChatMessage(
                Message(
                    user_name="Assistant",
                    text="...",
                    message_type="chat_message",
                )
            )

            chat.controls.append(assistant_message)
            page.update()

            stream = await client.chat.completions.create(
                # max_tokens=100,
                max_completion_tokens=100,
                # messages=[{"role": "user", "content": "Say this is a test"}],
                messages=messages,
                # model="LLaMA_CPP",
                model="HuggingFaceTB/SmolVLM-Instruct",
                stop=[
                    # "<|assistant|>",
                    # "<|endoftext|>",
                    # "<|system|>",
                    # "<|user|>",
                    # "</s>",
                    # "<end_of_utterance>",
                ],
                stream=True,
            )

            chunks = []

            async for chunk in stream:
                # print(chunk.choices[0].delta.content or "", end="")
                # assistant_message.update_text(chunk.choices[0].delta.content or "")
                chunks.append(chunk.choices[0].delta.content or "")

                assistant_message.update_text("".join(chunks))

            # assistant_message.update_text(chat_completion.choices[0].message)

    page.pubsub.subscribe(on_message)

    # A dialog asking for a user display name
    join_user_name = ft.TextField(
        label="Enter your name to join the chat",
        autofocus=True,
        on_submit=join_chat_click,
    )

    page.dialog = ft.AlertDialog(
        open=True,
        modal=True,
        title=ft.Text("Welcome!"),
        content=ft.Column([join_user_name], width=300, height=70, tight=True),
        actions=[ft.ElevatedButton(text="Join chat", on_click=join_chat_click)],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    # Chat messages
    chat = ft.ListView(
        expand=True,
        spacing=10,
        auto_scroll=True,
    )

    # Add a welcome message
    message = Message(
        user_name="System",
        text="Welcome to the chat! Please enter your name to join.",
        message_type="chat_message",
    )
    await on_message(message)

    message = Message(
        user_name="Assistant",
        text="Hello! How can I help you today?",
        message_type="chat_message",
    )
    await on_message(message)

    # A new message entry form
    new_message = ft.TextField(
        hint_text="Write a message...",
        autofocus=True,
        shift_enter=True,
        min_lines=1,
        max_lines=5,
        filled=True,
        expand=True,
        on_submit=send_message_click,
    )

    # Add everything to the page
    page.add(
        ft.Container(
            content=chat,
            border=ft.border.all(1, ft.colors.OUTLINE),
            border_radius=5,
            padding=10,
            expand=True,
        ),
        ft.Row(
            [
                new_message,
                ft.IconButton(
                    icon=ft.icons.SEND_ROUNDED,
                    tooltip="Send message",
                    on_click=send_message_click,
                ),
            ]
        ),
    )


fastapi_app.mount("/", flet_fastapi.app(root_main))


class Engine(str, Enum):
    copilot_codex = "copilot-codex"


@fastapi_app.get("/v1/engines")
async def list_engines():
    # return [engine.value for engine in Engine]
    return {
        "data": [
            {
                "id": Engine.copilot_codex,
                "name": "Copilot Codex",
                "description": "OpenAI's Codex model, formerly known as GitHub Copilot",
            }
        ]
    }


@fastapi_app.post("/v1/engines/{engine}/completions")
async def create_code_completion(engine: Engine, request: Request):
    print(
        f"=== {__name__}.create_code_completion(engine: Engine, request: Request) ==="
    )
    print(f"engine: {engine}")
    print(f"request: {request}")

    if engine == Engine.copilot_codex:
        try:
            body = await request.json()

        except json.decoder.JSONDecodeError as e:
            print(f"Error: {e}")
            body = {
                "model": "LLaMA_CPP",
                "prompt": "int main() {",
            }

        # body["model"] = "LLaMA_CPP"

        # return await create_completion(body, token_info={}, user=None)
        raise NotImplementedError("Not implemented")

    else:
        raise NotImplementedError("Not implemented")


def main(*args, **kwargs):
    print(f"=== {__name__}.main(*args, **kwargs) ===")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

    cwd = os.getcwd()
    print(f"cwd: {cwd}")

    uvicorn.run(
        f"{__name__}:fastapi_app",
        # host="0.0.0.0",
        host=kwargs.get("host", "0.0.0.0"),
        log_level="info",
        loop="asyncio",
        # port=8000,
        # port=kwargs.get("port", 8000),
        port=kwargs.get("port", 8080),
        # reload=True,
        reload=kwargs.get("dev", False),
        reload_dirs=[
            # f"{os.getcwd()}/timestep",
            f"{os.getcwd()}/src/timestep",
        ],
        workers=1,
    )


if __name__ == "__main__":
    main()
