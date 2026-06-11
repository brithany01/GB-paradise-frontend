import reflex as rx
import json

with open("data/isla_saona.json", "r", encoding="utf-8") as file:
    DATA = json.load(file)

hero = DATA["hero"]


def isla_saona_hero():

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
                rgba(0,42,58,0.92) 0%,
                rgba(0,42,58,0.88) 18%,
                rgba(0,42,58,0.78) 35%,
                rgba(0,42,58,0.50) 55%,
                rgba(0,42,58,0.15) 80%,
                rgba(0,42,58,0.00) 100%
            )
            """,

            z_index="1",
        ),

        rx.hstack(

            # IZQUIERDA
            rx.vstack(

                # BREADCRUMB
                rx.hstack(

                    rx.text(
                        "Inicio",
                        color="white",
                        font_size="0.85rem",
                    ),

                    rx.text(
                        "›",
                        color="white",
                    ),

                    rx.text(
                        "Destinos",
                        color="white",
                        font_size="0.85rem",
                    ),

                    rx.text(
                        "›",
                        color="white",
                    ),

                    rx.text(
                        "Isla Saona Premium",
                        color="white",
                        font_size="0.85rem",
                    ),

                    spacing="2",
                ),

                # BADGE
                rx.badge(

                    hero["badge"],

                    bg="#FFC857",

                    color="#023047",

                    border_radius="999px",

                    padding="0.4em 0.9em",

                    font_weight="600",
                ),

                # TITULO
                rx.image(

                    src=hero["title_image"],

                    width="420px",
                ),

                # DESCRIPCION
                rx.text(

                    hero["description"],

                    color="white",

                    max_width="420px",

                    font_size="0.95rem",

                    line_height="1.7",
                ),

                # FEATURES
                rx.hstack(

                    *[
                        rx.text(
                            feature,
                            color="#FFC857",
                            font_size="0.85rem",
                            font_weight="500",
                        )
                        for feature in hero["features"]
                    ],

                    spacing="5",

                    wrap="wrap",
                ),

                align_items="start",

                spacing="4",

                z_index="2",

                width="55%",
            ),

            rx.spacer(),

            # TARJETA PRECIO
            rx.box(

                rx.vstack(

                    rx.text(
                        "Desde",
                        color="#64748B",
                        font_size="0.95rem",
                    ),

                    rx.heading(
                        hero["price"],
                        color="#18B7C8",
                        size="8",
                    ),

                    rx.text(
                        "por persona",
                        color="#64748B",
                        font_size="0.9rem",
                    ),

                    rx.divider(),

                    rx.text(
                        f"⭐ {hero['rating']} ({hero['reviews']})",
                        color="#0F172A",
                        font_size="0.9rem",
                    ),

                    rx.button(

                        "Reservar ahora",

                        bg="#F6B800",

                        color="white",

                        width="100%",

                        border_radius="12px",

                        height="50px",

                        font_weight="700",

                        on_click=rx.redirect("/reservation"),
                    ),

                    rx.text(
                        hero["cancelation"],
                        font_size="0.75rem",
                        color="#64748B",
                        text_align="center",
                    ),

                    spacing="4",

                    width="100%",
                ),

                bg="white",

                width="280px",

                padding="1.8rem",

                border_radius="20px",

                box_shadow="0 10px 30px rgba(0,0,0,0.15)",

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

        height="560px",

        position="relative",

        padding="2rem 4rem",

        overflow="hidden",
    )