import reflex as rx
import json

with open("data/jarabacoa.json", "r", encoding="utf-8") as file:
    DATA = json.load(file)

hero = DATA["hero"]


def jarabacoa_hero():

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
                        text_shadow="0 2px 10px rgba(0,0,0,0.9)",
                    ),

                    rx.text("›", color="white"),

                    rx.text(
                        "Destinos",
                        color="white",
                        font_size="0.9rem",
                        text_shadow="0 2px 10px rgba(0,0,0,0.9)",
                    ),

                    rx.text("›", color="white"),

                    rx.text(
                        "Jarabacoa Adventure",
                        color="white",
                        font_size="0.9rem",
                        text_shadow="0 2px 10px rgba(0,0,0,0.9)",
                    ),

                    spacing="2",
                ),

                # BADGE
                rx.badge(

                    hero["badge"],

                    bg="rgba(255,255,255,0.15)",

                    color="white",

                    border="1px solid rgba(255,255,255,0.3)",

                    backdrop_filter="blur(10px)",

                    border_radius="999px",

                    padding="0.5em 1em",

                    margin_top="1em",
                ),

                # TITULO
                rx.image(

                    src=hero["title_image"],

                    width="620px",

                    margin_top="-10px",
                ),

                # SUBTITULO
                rx.text(

                    hero["subtitle"],

                    color="white",

                    font_size="2.3rem",

                    font_weight="700",

                    text_shadow="0 4px 15px rgba(0,0,0,0.9)",
                ),

                # DESCRIPCION
                rx.text(

                    hero["description"],

                    color="white",

                    font_size="1.1rem",

                    max_width="620px",

                    line_height="1.8",

                    text_shadow="0 3px 12px rgba(0,0,0,0.85)",
                ),

                # FEATURES
                rx.hstack(

                    *[
                        rx.text(
                            feature,
                            color="white",
                            font_size="1rem",
                            font_weight="500",
                            text_shadow="0 3px 10px rgba(0,0,0,0.9)",
                        )
                        for feature in hero["features"]
                    ],

                    spacing="6",

                    wrap="wrap",

                    margin_top="0.4rem",
                ),

                justify="start",

                align_items="start",

                spacing="3",

                width="60%",

                margin_top="-140px",

                z_index="2",
            ),

            rx.spacer(),

            # TARJETA PRECIO REDUCIDA
            rx.box(

                rx.vstack(

                    rx.text(
                        "Desde",
                        color="#64748B",
                        font_size="1rem",
                    ),

                    rx.heading(
                        hero["price"],
                        color="#18B7C8",
                        font_size="3rem",
                        font_weight="700",
                    ),

                    rx.text(
                        "por persona",
                        color="#64748B",
                        font_size="1rem",
                    ),

                    rx.divider(),

                    rx.text(
                        f"⭐ {hero['rating']} ({hero['reviews']})",
                        color="#0F172A",
                        font_weight="600",
                        font_size="0.95rem",
                    ),

                    rx.button(

                        "📅 Reservar ahora",

                        bg="#F6B800",

                        color="white",

                        width="100%",

                        height="52px",

                        border_radius="14px",

                        font_weight="700",

                        font_size="0.95rem",

                        on_click=rx.redirect("/reservation"),

                        _hover={
                            "bg": "#E2AA00"
                        },
                    ),

                    rx.text(

                        hero["cancelation"],

                        color="#64748B",

                        font_size="0.85rem",

                        text_align="center",
                    ),

                    spacing="3",

                    width="100%",
                ),

                bg="white",

                width="340px",

                padding="2rem",

                border_radius="24px",

                box_shadow="0 15px 40px rgba(0,0,0,0.15)",

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

        height="760px",

        position="relative",

        padding="6rem 5rem 8rem 5rem",

        overflow="hidden",
    )