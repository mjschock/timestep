"""The home page of the app."""

from timestep import styles
from timestep.templates import template

import reflex as rx


@template(route="/", title="Home")
def index() -> rx.Component:
    """The home page.

    Returns:
        The UI for the home page.
    """
    with open("README.md", encoding="utf-8") as readme:
        content = readme.read()

    # return rx.markdown(content, component_map=styles.markdown_style)

    return rx.vstack(
        rx.heading("Home", size="8"),
        # rx.text("Welcome to Reflex!"),
        # rx.text(
        #     "You can edit this page in ",
        #     rx.code("{your_app}/pages/dashboard.py"),
        # ),
        rx.markdown(content, component_map=styles.markdown_style)
    )
