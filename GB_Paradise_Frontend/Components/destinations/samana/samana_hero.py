import reflex as rx
import json

with open("data/samana.json", "r", encoding="utf-8") as file:
    DATA = json.load(file)

hero = DATA["hero"]


def samana_hero():

    return rx.box(

        # OVERLAY OSCURO
        rx.box(

            position="absolute",

            top="0",

            left="0",

            width="100%",

            height="100%",

            background="""
            linear-gradient(
                90deg,
                rgba(0,0,0,0.92) 0%,
                rgba(0,0,0,0.88) 20%,
                rgba(0,0,0,0.78) 40%,
                rgba(0,0,0,0.55) 60%,
                rgba(0,0,0,0.25) 80%,
                rgba(0,0,0,0.05) 100%
            )
            """,

            z_index="1",
        ),

        rx.hstack(

            # CONTENIDO IZQUIERDO
            rx.vstack(

                # BREADCRUMB
                rx.hstack(

                    rx.text(
                        "🏠 Inicio",
                        color="white",
                        font_size="0.9rem",
                    ),

                    rx.text("›", color="white"),

                    rx.text(
                        "Destinos",
                        color="white",
                        font_size="0.9rem",
                    ),

                    rx.text("›", color="white"),

                    rx.text(
                        "Samaná Experience",
                        color="white",
                        font_size="0.9rem",
                    ),

                    spacing="2",
                ),

                # BADGE
                rx.badge(

                    hero["badge"],

                    bg="rgba(255,255,255,0.15)",

                    color="white",

                    border="1px solid rgba(255,255,255,0.3)",

                    border_radius="999px",

                    padding="0.5em 1em",

                    margin_top="1em",
                ),

                # TITULO
                rx.image(

                    src=hero["title_image"],

                    width="500px",

                    margin_top="-5px",
                ),

                # SUBTITULO
                rx.text(

                    hero["subtitle"],

                    color="white",

                    font_size="1.8rem",

                    font_weight="700",
                ),

                # DESCRIPCION
                rx.text(

                    hero["description"],

                    color="white",

                    font_size="1rem",

                    max_width="550px",

                    line_height="1.7",
                ),

                # FEATURES
                rx.hstack(

                    *[
                        rx.text(
                            feature,
                            color="white",
                            font_size="0.95rem",
                            font_weight="500",
                        )
                        for feature in hero["features"]
                    ],

                    spacing="6",

                    wrap="wrap",
                ),

                align_items="start",

                spacing="4",

                width="60%",

                z_index="2",
            ),

            rx.spacer(),

            # TARJETA PRECIO
            rx.box(

                rx.vstack(

                    rx.text(
                        "Desde",
                        color="#64748B",
                    ),

                    rx.heading(
                        hero["price"],
                        color="#18B7C8",
                        font_size="2.5rem",
                    ),

                    rx.text(
                        "por persona",
                        color="#64748B",
                    ),

                    rx.divider(),

                    rx.text(
                        f"⭐ {hero['rating']} ({hero['reviews']})",
                        font_weight="600",
                    ),

                    rx.button(

                        "📅 Reservar ahora",

                        width="100%",

                        height="45px",

                        bg="#F6B800",

                        color="white",

                        border_radius="12px",

                        on_click=rx.redirect("/reservation"),
                    ),

                    rx.text(
                        hero["cancelation"],
                        color="#64748B",
                        font_size="0.85rem",
                        text_align="center",
                    ),

                    spacing="4",

                    width="100%",
                ),

                bg="white",

                width="300px",

                padding="1.6rem",

                border_radius="20px",

                box_shadow="0 15px 40px rgba(0,0,0,0.15)",

                margin_top="80px",

                z_index="2",
            ),

            width="100%",

            align="center",
        ),

        background_image=f"url('{hero['image']}')",

        background_size="cover",

        background_position="center",

        background_repeat="no-repeat",

        width="100%",

        height="700px",

        position="relative",

        padding="5rem",

        overflow="hidden",
    )