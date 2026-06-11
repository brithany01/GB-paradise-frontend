import reflex as rx
import json

with open("data/jarabacoa.json", "r", encoding="utf-8") as file:
    DATA = json.load(file)

cta = DATA["cta"]


def jarabacoa_cta():

    return rx.box(

        rx.vstack(

            rx.heading(
                cta["title"],
                color="white",
                font_size="2.5rem",
                text_align="center",
            ),

            rx.text(
                cta["subtitle"],
                color="rgba(255,255,255,0.9)",
                font_size="1.1rem",
                text_align="center",
                max_width="700px",
            ),

            rx.button(

                "Reservar ahora",

                bg="#F6B800",

                color="white",

                size="3",

                padding_left="2rem",

                padding_right="2rem",

                border_radius="14px",

                font_weight="700",

                margin_top="1rem",

                on_click=rx.redirect("/reservation"),

                _hover={
                    "bg": "#E2AA00"
                },
            ),

            spacing="4",

            align_items="center",
        ),

        width="100%",

        max_width="1400px",

        margin="auto",

        padding="5rem 2rem",

        border_radius="32px",

        background="linear-gradient(135deg, #18B7C8 0%, #023047 100%)",

        margin_top="3rem",

        margin_bottom="4rem",
    )