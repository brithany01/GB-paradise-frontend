import reflex as rx
import json

with open("data/punta_cana.json", "r", encoding="utf-8") as file:
    DATA = json.load(file)

hero = DATA["hero"]


def punta_cana_hero():

    return rx.box(

        rx.hstack(

            # IZQUIERDA
            rx.vstack(

                # Breadcrumb
                rx.hstack(

                    rx.text(
                        "Inicio",
                        color="white",
                        font_size="0.9em",
                    ),

                    rx.text("›", color="white"),

                    rx.text(
                        "Destinos",
                        color="white",
                        font_size="0.9em",
                    ),

                    rx.text("›", color="white"),

                    rx.text(
                        "Punta Cana Paradise",
                        color="white",
                        font_size="0.9em",
                    ),

                    spacing="2",
                ),

                # Badge
                rx.badge(
                    hero["badge"],

                    bg="rgba(255,255,255,0.15)",

                    color="white",

                    border="1px solid rgba(255,255,255,0.4)",

                    border_radius="999px",

                    padding="0.4em 0.9em",

                    backdrop_filter="blur(8px)",

                    margin_top="1em",
                ),

                # Título
                rx.heading(
                    "Punta Cana\nParadise",

                    white_space="pre-line",

                    color="white",

                    font_size="5rem",

                    font_weight="700",

                    line_height="0.95",

                    text_shadow="0 4px 20px rgba(0,0,0,0.35)",

                    margin_top="0.3em",
                ),

                # Subtítulo
                rx.text(
                    "Relájate en el paraíso",

                    color="#7EEBFF",

                    font_size="2rem",

                    font_style="italic",

                    font_family="cursive",

                    text_shadow="0 2px 12px rgba(0,0,0,0.35)",
                ),

                # Descripción
                rx.text(
                    hero["description"],

                    color="white",

                    max_width="550px",

                    font_size="1.05em",

                    line_height="1.8",

                    text_shadow="0 2px 10px rgba(0,0,0,0.35)",
                ),

                # Características
                rx.hstack(

                    rx.text(
                        f"📅 {hero['duration']}",
                        color="white",
                    ),

                    rx.text(
                        f"🏖️ {hero['category']}",
                        color="white",
                    ),

                    rx.text(
                        f"🎁 {hero['package']}",
                        color="white",
                    ),

                    spacing="8",

                    margin_top="1em",
                ),

                align_items="start",

                width="60%",

                z_index="2",
            ),

            rx.spacer(),

            # TARJETA DE PRECIO
            rx.box(

                rx.vstack(

                    rx.text(
                        "Desde",
                        color="#64748B",
                        font_size="1.2em",
                    ),

                    rx.heading(
                        hero["price"],
                        color="#18B7C8",
                        font_size="3.2rem",
                        font_weight="700",
                    ),

                    rx.text(
                        "por persona",
                        color="#64748B",
                    ),

                    rx.text(
                        f"⭐ {hero['rating']} ({hero['reviews']})",
                        color="#0F172A",
                        font_weight="500",
                    ),

rx.link(

                    rx.button(

                        "📅 Reservar ahora",

                        bg="#F6B800",

                        color="white",

                        width="100%",

                        height="56px",

                        border_radius="14px",

                        font_weight="600",

                        _hover={
                            "bg": "#E2AA00"
                        },
                    ),

                    href="/reservation",

                    text_decoration="none",

                    width="100%",
                ),

                    rx.text(
                        hero["cancelation"],

                        color="#64748B",

                        font_size="0.85em",

                        text_align="center",
                    ),

                    spacing="4",

                    align_items="start",
                ),

                bg="white",

                width="370px",

                padding="2.5em",

                border_radius="24px",

                box_shadow="0 15px 40px rgba(0,0,0,0.15)",

                z_index="2",
            ),

            width="100%",

            align="center",
        ),

        background_image=f"url('{hero['background_image']}')",

        background_size="cover",

        background_position="center",

        width="100%",

        height="720px",

        padding="4em 5em",

        position="relative",

        overflow="hidden",
    )