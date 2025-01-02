import os

import flet as ft
from views import create_main_view


def main(page: ft.Page):
    page.title = "Flet FastAPI App"
    page.theme_mode = "light"
    page.padding = 20

    # Create and add main view
    main_view = create_main_view(page)
    page.add(main_view)


if __name__ == "__main__":
    ft.app(target=main, port=8550, view=ft.WEB_BROWSER)
