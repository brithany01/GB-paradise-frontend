import reflex as rx
import json


with open("data/reservation_cta.json", encoding="utf-8") as f:
    cta = json.load(f)


def reservation_cta():

    return rx.box(

        rx.hstack(

            rx.image(
                src="/reservation_cta.png",
                height="120px",
            ),

            rx.vstack(

                rx.text(
                    cta["title"],
                    font_size="1.5em",
                    font_weight="bold",
                    color="#023047",
                ),

                rx.text(
                    cta["description"],
                    color="#023047",
                ),

                align_items="start",
            ),

            rx.spacer(),

            rx.button(
                cta["button_text"],
                bg="#18B7C8",
                color="white",
                border_radius="999px",
                padding_x="2em",
            ),

            width="100%",
            align="center",
        ),

        bg="#EAFBFF",
        border_radius="20px",
        padding="1em 2em",
        width="100%",
        margin_top="2em",
    )