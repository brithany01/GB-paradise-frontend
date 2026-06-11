import reflex as rx
import json


with open("data/punta_cana.json", "r", encoding="utf-8") as file:
    DATA = json.load(file)

info = DATA["info"]


def info_item(icon, title, text):

    return rx.hstack(

        rx.box(

            rx.text(
                icon,
                font_size="2em",
            ),

            bg="#F1FAFC",

            width="58px",
            height="58px",

            border_radius="50%",

            display="flex",
            align_items="center",
            justify_content="center",
        ),

        rx.vstack(

            rx.text(
                title,
                font_weight="600",
                color="#0F172A",
            ),

            rx.text(
                text,
                color="#64748B",
                font_size="0.85em",
            ),

            align_items="start",
            spacing="1",
        ),

        spacing="4",
    )


def punta_cana_info():

    return rx.box(

        rx.hstack(

            # UBICACIÓN CON GOOGLE MAPS
            rx.link(

                info_item(
                    "📍",
                    "Ubicación",
                    info["location"]
                ),

                href="https://www.google.com/maps/search/?api=1&query=Punta+Cana+Republica+Dominicana",

                target="_blank",

                text_decoration="none",

                color="inherit",

                _hover={
                    "transform": "scale(1.02)",
                    "cursor": "pointer",
                },
            ),

            rx.divider(
                orientation="vertical",
                height="60px",
            ),

            # DURACIÓN
            info_item(
                "📅",
                "Duración",
                info["duration"]
            ),

            rx.divider(
                orientation="vertical",
                height="60px",
            ),

            # EXPERIENCIA
            info_item(
                "🏔️",
                "Tipo de experiencia",
                info["experience"]
            ),

            rx.divider(
                orientation="vertical",
                height="60px",
            ),

            # TEMPORADA
            info_item(
                "☀️",
                "Mejor temporada",
                info["season"]
            ),

            width="100%",
            justify="between",
            align="center",
        ),

        bg="white",

        width="78%",

        padding="2em",

        border_radius="22px",

        box_shadow="0 8px 25px rgba(0,0,0,0.08)",

        margin_top="-60px",

        margin_left="auto",
        margin_right="auto",

        position="relative",

        z_index="20",
    )