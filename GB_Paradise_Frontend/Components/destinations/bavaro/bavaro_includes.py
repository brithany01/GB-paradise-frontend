import reflex as rx
import json

with open("data/bavaro.json", "r", encoding="utf-8") as file:
    DATA = json.load(file)

includes = DATA["includes"]


def include_card(item):

    return rx.box(

        rx.vstack(

            rx.box(

                rx.image(
                    src=item["icon"],
                    width="34px",
                    height="34px",
                ),

                bg="#EAF8FA",

                padding="12px",

                border_radius="999px",
            ),

            rx.text(
                item["title"],
                text_align="center",
                font_weight="700",
                color="#023047",
                font_size="0.85rem",
            ),

            rx.text(
                item["description"],
                text_align="center",
                color="#64748B",
                font_size="0.75rem",
            ),

            spacing="2",

            align_items="center",
        ),

        bg="white",

        width="180px",

        height="125px",

        border="1px solid #E5E7EB",

        border_radius="16px",

        display="flex",

        align_items="center",

        justify_content="center",

        transition="all 0.3s ease",

        _hover={
            "transform": "translateY(-4px)",
            "box_shadow": "0 10px 20px rgba(0,0,0,0.08)"
        },
    )


def bavaro_includes():

    return rx.vstack(

        rx.vstack(

            rx.heading(
                "¿Qué incluye tu experiencia?",
                color="#023047",
                size="5",
            ),

            rx.box(
                width="40px",
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

            wrap="wrap",

            width="100%",
        ),

        width="100%",

        max_width="1400px",

        margin="auto",

        padding_top="1.5rem",

        align_items="center",
    )