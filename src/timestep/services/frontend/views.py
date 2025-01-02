import os

import flet as ft
import httpx

# Get backend URL from environment variable or use default
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")


class ItemList(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.items = []
        self.items_view = ft.Column(scroll="auto", height=400)

    def build(self):
        return self.items_view

    async def load_items(self):
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{BACKEND_URL}/api/items")
            if response.status_code == 200:
                self.items = response.json()
                await self.update_view()

    async def update_view(self):
        self.items_view.controls = [
            ft.Card(
                content=ft.Container(
                    content=ft.Column(
                        [
                            ft.Text(item["name"], size=20, weight="bold"),
                            ft.Text(item["description"]),
                            ft.ElevatedButton(
                                "Delete",
                                on_click=lambda e, id=item["id"]: self.delete_item(
                                    e, id
                                ),
                            ),
                        ]
                    ),
                    padding=10,
                ),
                margin=5,
            )
            for item in self.items
        ]
        await self.update_async()

    async def delete_item(self, e, item_id):
        async with httpx.AsyncClient() as client:
            response = await client.delete(f"{BACKEND_URL}/api/items/{item_id}")
            if response.status_code == 200:
                await self.load_items()


def create_main_view(page: ft.Page) -> ft.Column:
    item_list = ItemList()
    name_field = ft.TextField(label="Name", width=300)
    description_field = ft.TextField(label="Description", width=300)

    async def add_item(e):
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{BACKEND_URL}/api/items",
                json={"name": name_field.value, "description": description_field.value},
            )
            if response.status_code == 200:
                name_field.value = ""
                description_field.value = ""
                await page.update_async()
                await item_list.load_items()

    return ft.Column(
        [
            ft.Text("Items Manager", size=30, weight="bold"),
            ft.Column(
                [
                    name_field,
                    description_field,
                    ft.ElevatedButton("Add Item", on_click=add_item),
                ]
            ),
            item_list,
        ]
    )
