import reflex as rx
import json

with open("data/samana.json", "r", encoding="utf-8") as file:
    DATA = json.load(file)

info = DATA["info"]


def info_card(item):

    return rx.hstack(

        rx.box(

            rx.image(
                src=item["icon"],
                width="32px",
                height="32px",
            ),

            bg="#EAF8FA",

            padding="12px",

            border_radius="999px",
        ),

        rx.vstack(

            rx.text(
                item["title"],
                font_weight="700",
                color="#0F172A",
                font_size="0.95rem",
            ),

            rx.text(
                item["value"],
                color="#64748B",
                font_size="0.85rem",
            ),

            align_items="start",

            spacing="1",
        ),

        spacing="4",

        align="center",
    )


def samana_info():

    return rx.box(

        rx.hstack(

            rx.link(
                info_card(info["location"]),
                href="https://maps.google.com/?q=Samana",
                text_decoration="none",
            ),

            info_card(info["duration"]),

            info_card(info["experience"]),

            info_card(info["season"]),

            justify="between",

            width="100%",
        ),

        bg="white",

        max_width="1200px",

        width="90%",

        margin="auto",

        margin_top="-40px",

        padding="1.5rem 2rem",

        border_radius="18px",

        box_shadow="0 8px 24px rgba(0,0,0,0.08)",

        position="relative",

        z_index="20",
    )