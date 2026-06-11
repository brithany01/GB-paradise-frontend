import reflex as rx
import json

with open("data/jarabacoa.json", "r", encoding="utf-8") as file:
    DATA = json.load(file)

includes = DATA["includes"]


def include_card(item):

    return rx.box(

        rx.vstack(

            rx.box(

                rx.image(
                    src=item["icon"],
                    width="42px",
                    height="42px",
                ),

                bg="#EAF8FA",

                padding="14px",

                border_radius="999px",
            ),

            rx.text(
                item["title"],
                font_weight="700",
                color="#0F172A",
                font_size="1rem",
                text_align="center",
            ),

            rx.text(
                item["description"],
                color="#64748B",
                font_size="0.9rem",
                text_align="center",
            ),

            spacing="3",

            align_items="center",
        ),

        bg="white",

        width="220px",

        min_height="170px",

        padding="1.5rem",

        border_radius="18px",

        border="1px solid #E5E7EB",

        box_shadow="0 4px 12px rgba(0,0,0,0.04)",

        transition="all 0.3s ease",

        _hover={
            "transform": "translateY(-5px)",
            "box_shadow": "0 10px 24px rgba(0,0,0,0.08)"
        },
    )


def jarabacoa_includes():

    return rx.vstack(

        # Título
        rx.vstack(

            rx.heading(
                "¿Qué incluye tu experiencia?",
                color="#023047",
                size="6",
            ),

            rx.box(
                width="60px",
                height="4px",
                bg="#F6B800",
                border_radius="999px",
            ),

            spacing="2",
            align_items="center",
        ),

        # Cards
        rx.hstack(

            *[
                include_card(item)
                for item in includes
            ],

            spacing="4",

            justify="center",

            wrap="wrap",

            width="100%",
        ),

        width="100%",

        max_width="1400px",

        margin="auto",

        padding_top="4rem",

        padding_bottom="3rem",

        align_items="center",
    )