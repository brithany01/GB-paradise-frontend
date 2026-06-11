import reflex as rx
import json

with open("data/isla_saona.json", "r", encoding="utf-8") as file:
    DATA = json.load(file)

includes = DATA["includes"]


def include_card(item):

    return rx.box(

        rx.vstack(

            rx.box(

                rx.image(
                    src=item["icon"],
                    width="38px",
                    height="38px",
                ),

                bg="#EAF8FA",

                padding="12px",

                border_radius="999px",
            ),

            rx.text(
                item["title"],
                font_weight="700",
                color="#023047",
                font_size="0.85rem",
                text_align="center",
            ),

            rx.text(
                item["description"],
                color="#64748B",
                font_size="0.75rem",
                text_align="center",
            ),

            spacing="2",

            align_items="center",
        ),

        bg="white",

        width="180px",

        height="130px",

        border_radius="16px",

        border="1px solid #E5E7EB",

        display="flex",

        align_items="center",

        justify_content="center",

        box_shadow="0 2px 10px rgba(0,0,0,0.03)",
    )


def isla_saona_includes():

    return rx.vstack(

        rx.vstack(

            rx.heading(
                "¿Qué incluye tu experiencia?",
                color="#023047",
                size="5",
            ),

            rx.box(
                width="45px",
                height="4px",
                bg="#F6B800",
                border_radius="999px",
            ),

            spacing="2",

            align_items="center",
        ),

        rx.hstack(

            *[
                include_card(item)
                for item in includes
            ],

            spacing="3",

            justify="center",

            width="100%",

            wrap="nowrap",
        ),

        width="100%",

        max_width="1400px",

        margin="auto",

        padding_top="2rem",

        padding_bottom="2rem",

        align_items="center",
    )