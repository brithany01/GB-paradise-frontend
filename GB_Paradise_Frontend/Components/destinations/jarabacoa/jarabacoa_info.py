import reflex as rx
import json

with open("data/jarabacoa.json", "r", encoding="utf-8") as file:
    DATA = json.load(file)

info = DATA["info"]


def info_card(item):

    return rx.hstack(

        rx.box(

            rx.image(
                src=item["icon"],
                width="38px",
                height="38px",
            ),

            bg="#EAF8FA",

            width="70px",

            height="70px",

            border_radius="999px",

            display="flex",

            align_items="center",

            justify_content="center",
        ),

        rx.vstack(

            rx.text(
                item["title"],
                font_weight="700",
                color="#0F172A",
                font_size="1.15rem",
            ),

            rx.text(
                item["value"],
                color="#64748B",
                font_size="1rem",
                max_width="220px",
            ),

            align_items="start",

            spacing="1",
        ),

        spacing="5",

        align="center",
    )


def jarabacoa_info():

    return rx.box(

        rx.hstack(

            rx.link(

                info_card(info["location"]),

                href="https://maps.google.com/?q=Jarabacoa",

                text_decoration="none",
            ),

            info_card(info["duration"]),

            info_card(info["experience"]),

            info_card(info["season"]),

            justify="between",

            width="100%",
        ),

        bg="white",

        max_width="1500px",

        width="85%",

        margin="auto",

        margin_top="-35px",

        padding="2.5rem 3rem",

        border_radius="28px",

        box_shadow="0 15px 40px rgba(0,0,0,0.08)",

        position="relative",

        z_index="20",
    )