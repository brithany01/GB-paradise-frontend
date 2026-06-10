import reflex as rx
import json


with open("data/reservation_benefits.json", encoding="utf-8") as f:
    benefits = json.load(f)


def reservation_benefits():

    return rx.box(

        rx.vstack(

            rx.image(
                src="/reservation_benefits.png",
                width="100%",
                border_radius="16px 16px 0 0",
            ),

            rx.text(
                "Beneficios de reservar con nosotros",
                font_weight="bold",
                color="#023047",
                text_align="center",
            ),

            *[
                rx.hstack(
                    rx.text("✓", color="#18B7C8"),
                    rx.text(item["title"]),
                    width="100%",
                )
                for item in benefits
            ],

            spacing="3",
            width="100%",
        ),

        bg="white",
        border_radius="20px",
        padding="1em",
        width="320px",
        box_shadow="0 8px 20px rgba(0,0,0,0.05)",
    )