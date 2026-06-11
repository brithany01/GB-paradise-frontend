import reflex as rx
import json

with open("data/bavaro.json", "r", encoding="utf-8") as file:
    DATA = json.load(file)

info = DATA["info"]


def info_card(item):

    return rx.hstack(

        rx.box(

            rx.image(
                src=item["icon"],
                width="30px",
                height="30px",
            ),

            bg="#EAF8FA",

            padding="14px",

            border_radius="999px",
        ),

        rx.vstack(

            rx.text(
                item["title"],
                font_weight="700",
                color="#0F172A",
                font_size="1rem",
            ),

            rx.text(
                item["value"],
                color="#64748B",
                font_size="0.9rem",
            ),

            align_items="start",

            spacing="1",
        ),

        spacing="4",

        align="center",
    )


def bavaro_info():

    return rx.box(

        rx.hstack(

            info_card(info["location"]),

            info_card(info["duration"]),

            info_card(info["experience"]),

            info_card(info["season"]),

            justify="between",

            width="100%",
        ),

        bg="white",

        max_width="1400px",

        width="92%",

        margin="auto",

        margin_top="-95px",

        padding="2rem",

        border_radius="20px",

        box_shadow="0 10px 25px rgba(0,0,0,0.08)",

        position="relative",

        z_index="10",
    )