import reflex as rx
import json

from .experience_card import experience_card


with open("data/experiences.json", "r", encoding="utf-8") as f:
    experiences_data = json.load(f)


def experience_grid():

    return rx.center(

        rx.vstack(

            rx.heading(
                "Descubre Experiencias Inolvidables",
                size="8",
                color="#023047",
                text_align="center",
            ),

            rx.hstack(

                *[
                    experience_card(exp)
                    for exp in experiences_data
                ],

                spacing="4",
                justify="center",
                width="100%",
                flex_wrap="wrap",
            ),

            spacing="6",
            width="100%",
            align="center",
        ),

        width="100%",
        margin_top="2em",
        margin_bottom="3em",
    )