import reflex as rx
import json


with open("data/values.json", "r", encoding="utf-8") as f:
    values_data = json.load(f)


def value_card(value):

    return rx.box(

        rx.hstack(

            rx.box(
                value["icon"],
                bg="#18B7C8",
                color="white",
                border_radius="50%",
                width="55px",
                height="55px",
                display="flex",
                align_items="center",
                justify_content="center",
                font_size="1.4em",
                flex_shrink="0",
            ),

            rx.vstack(

                rx.text(
                    value["title"],
                    font_weight="bold",
                    color="#023047",
                    font_size="1.05em",
                ),

                rx.text(
                    value["description"],
                    color="gray",
                    font_size="0.9em",
                ),

                align_items="start",
                spacing="1",
            ),

            align="center",
            spacing="3",
        ),

        bg="white",
        padding="1.3em",
        border_radius="18px",
        width="250px",
        box_shadow="0 4px 12px rgba(0,0,0,0.06)",
    )


def about_values():

    return rx.center(

        rx.vstack(

            rx.heading(
                "Nuestros Valores",
                size="7",
                color="#023047",
            ),

            rx.hstack(

                *[
                    value_card(value)
                    for value in values_data
                ],

                justify="center",
                spacing="4",
                width="100%",
                flex_wrap="wrap",
            ),

            spacing="5",
            align="center",
        ),

        width="100%",
        margin_top="2em",
        margin_bottom="2em",
    )