import reflex as rx
import json


with open("data/punta_cana.json", "r", encoding="utf-8") as file:
    DATA = json.load(file)


cta = DATA["cta"]


def punta_cana_cta():

    return rx.box(

        rx.hstack(

            # Imagen izquierda
            rx.image(
                src="/cta_luggage.png",
                width="130px",
                height="130px",
                object_fit="contain",
            ),

            # Texto
            rx.vstack(

                rx.heading(
                    cta["title"],
                    color="white",
                    size="5",
                ),

                rx.text(
                    cta["description"],
                    color="white",
                    font_size="0.95em",
                ),

                spacing="1",
                align_items="center",
            ),

            rx.spacer(),

            # BOTÓN RESERVAS
            rx.link(

                rx.button(

                    "🗓️  " + cta["button"],

                    bg="#F6B800",
                    color="white",

                    font_weight="bold",

                    height="52px",

                    padding_left="1.8em",
                    padding_right="1.8em",

                    border_radius="12px",

                    _hover={
                        "bg": "#E0A900"
                    },
                ),

                href="/reservation",

                text_decoration="none",
            ),

            # Avión derecha
            rx.text(
                "✈",
                color="white",
                font_size="1.7em",
            ),

            width="100%",
            align="center",
        ),

        background="""
        linear-gradient(
            90deg,
            #18B7C8 0%,
            #11A7BC 40%,
            #0D91A4 100%
        )
        """,

        border_radius="18px",

        width="100%",

        padding="1.5em 2em",

        margin_top="2em",
        margin_bottom="3em",

        box_shadow="0 8px 20px rgba(0,0,0,0.08)",
    )