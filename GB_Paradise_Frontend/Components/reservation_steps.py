import reflex as rx
import json


with open("data/reservation_steps.json", encoding="utf-8") as f:
    steps = json.load(f)


def step_card(step):

    colors = [
        "#DFF6FB",
        "#EEF8DF",
        "#FFF1D9",
        "#F3E4FF",
        "#E0F7FA",
    ]

    index = int(step["number"]) - 1

    return rx.box(

        rx.vstack(

            rx.box(
                step["number"],
                bg="#18B7C8",
                color="white",
                border_radius="50%",
                width="40px",
                height="40px",
                display="flex",
                align_items="center",
                justify_content="center",
                font_weight="bold",
            ),

            rx.box(
                "✓",
                bg=colors[index],
                border_radius="50%",
                width="100px",
                height="100px",
                display="flex",
                align_items="center",
                justify_content="center",
                font_size="2.2em",
            ),

            rx.text(
                step["title"],
                font_weight="bold",
                color="#023047",
                text_align="center",
                font_size="1.15em",
            ),

            rx.text(
                step["description"],
                text_align="center",
                color="#4A5568",
                font_size="0.95em",
            ),

            spacing="4",
            align="center",
        ),

        bg="white",
        border_radius="20px",
        padding="1.5em",
        width="220px",
        min_height="260px",
        box_shadow="0 8px 20px rgba(0,0,0,0.05)",
    )


def reservation_steps():

    return rx.vstack(

        rx.text(
            "¿Cómo funciona tu reserva?",
            font_size="2.3em",
            font_weight="bold",
            color="#023047",
        ),

        rx.hstack(
            *[step_card(step) for step in steps],
            spacing="4",
            justify="between",
            width="100%",
            wrap="nowrap",
        ),

        spacing="6",
        width="100%",
        margin_top="2em",
    )