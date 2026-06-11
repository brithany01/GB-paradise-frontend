import reflex as rx
import json

with open("data/punta_cana.json", "r", encoding="utf-8") as file:
    DATA = json.load(file)

includes = DATA["includes"]


def include_card(item):

    return rx.box(

        rx.vstack(

            rx.box(
                rx.text(
                    "✓",
                    font_size="1.5em",
                    color="#18B7C8",
                    font_weight="bold",
                ),

                width="55px",
                height="55px",

                border_radius="50%",

                bg="#ECFAFD",

                display="flex",
                align_items="center",
                justify_content="center",
            ),

            rx.text(
                item["title"],
                font_weight="600",
                text_align="center",
                font_size="0.85em",
                color="#0F172A",
            ),

            rx.text(
                item["description"],
                color="#64748B",
                text_align="center",
                font_size="0.72em",
            ),

            spacing="2",
            align="center",
        ),

        bg="white",

        border="1px solid #EAEAEA",

        border_radius="14px",

        width="150px",
        height="140px",

        display="flex",
        align_items="center",
        justify_content="center",

        box_shadow="0 3px 10px rgba(0,0,0,0.05)",
    )


def punta_cana_includes():

    return rx.vstack(

        rx.heading(
            "¿Qué incluye tu experiencia?",
            size="5",
            color="#023047",
        ),

        rx.flex(

            *[
                include_card(item)
                for item in includes
            ],

            wrap="wrap",
            gap="16px",
            width="100%",
        ),

        width="50%",
        align_items="start",
    )