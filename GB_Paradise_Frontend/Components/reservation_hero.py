import reflex as rx
import json


with open("data/reservation_hero.json", "r", encoding="utf-8") as file:
    HERO_DATA = json.load(file)


def reservation_hero():

    data = HERO_DATA["packages"]

    return rx.box(

        # Overlay
        rx.box(
            width="100%",
            height="100%",
            position="absolute",
            top="0",
            left="0",
            background="""
            linear-gradient(
                90deg,
                rgba(255,255,255,0.95) 0%,
                rgba(255,255,255,0.85) 20%,
                rgba(255,255,255,0.55) 40%,
                rgba(255,255,255,0.10) 65%,
                rgba(255,255,255,0) 80%
            )
            """,
        ),

        rx.hstack(

            # IZQUIERDA
            rx.vstack(

                rx.image(
                    src=data["title_image"],
                    width="720px",
                    margin_top="-60px",
                    margin_bottom="-90px",
                ),

                rx.text(
                    data["description"],
                    color="#023047",
                    font_size="1.25em",
                    max_width="620px",
                    margin_left="120px",
                    margin_top="15px",
                    line_height="1.6",
                ),

                align_items="start",
                spacing="0",
                width="55%",
                z_index="20",
            ),

            rx.spacer(),

            # TARJETA DERECHA
            rx.box(

                rx.vstack(

                    rx.box(
                        "🛡️",
                        bg="#18B7C8",
                        color="white",
                        border_radius="50%",
                        width="75px",
                        height="75px",
                        display="flex",
                        align_items="center",
                        justify_content="center",
                        font_size="2em",
                    ),

                    rx.text(
                        data["card_title"],
                        font_weight="bold",
                        color="#023047",
                        text_align="center",
                        font_size="1.2em",
                    ),

                    rx.text(
                        data["card_description"],
                        text_align="center",
                        color="#023047",
                        font_size="1em",
                        line_height="1.6",
                    ),

                    spacing="3",
                    align="center",
                ),

                bg="white",
                padding="2.2em",
                border_radius="25px",
                width="290px",
                box_shadow="0 10px 25px rgba(0,0,0,0.10)",

                # SUBE LA TARJETA
                margin_top="-110px",

                z_index="20",
            ),

            width="100%",
            align="center",
        ),

        background_image="url('/reservation_hero_bg.png')",
        background_size="cover",
        background_position="center",

        width="100%",
        min_height="500px",

        border_radius="25px",

        padding="5em 5em 3em 6em",

        margin_top="1em",

        position="relative",
        overflow="hidden",
    )