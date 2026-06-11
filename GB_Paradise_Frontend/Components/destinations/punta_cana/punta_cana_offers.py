import reflex as rx
import json

with open("data/punta_cana.json", "r", encoding="utf-8") as file:
    DATA = json.load(file)

offers = DATA["offers"]


def offer_card(item):

    return rx.box(

        rx.box(

            rx.image(
                src=item["image"],
                width="100%",
                height="140px",
                object_fit="cover",
            ),

            rx.badge(
                item["discount"],
                color_scheme="teal",

                position="absolute",
                top="10px",
                left="10px",
            ),

            position="relative",
        ),

        rx.vstack(

            rx.text(
                item["title"],
                font_weight="700",
                font_size="1em",
                color="#0F172A",
            ),

            rx.text(
                "3 días / 2 noches",
                font_size="0.85em",
                color="#64748B",
            ),

            rx.hstack(

                rx.text(
                    item["price"],
                    color="#18B7C8",
                    font_weight="bold",
                    font_size="1.3em",
                ),

                rx.spacer(),

                rx.text(
                    "⭐ 4.8",
                    font_size="0.85em",
                    color="#64748B",
                ),

                width="100%",
            ),

            width="100%",
            align_items="start",
            spacing="2",
        ),

        bg="white",

        border_radius="16px",

        overflow="hidden",

        width="240px",

        box_shadow="0 5px 15px rgba(0,0,0,0.08)",

        transition="0.3s",

        _hover={
            "transform": "translateY(-4px)"
        },
    )


def punta_cana_offers():

    return rx.vstack(

        rx.heading(
            "Ofertas destacadas en Punta Cana",
            size="6",
            color="#023047",
        ),

        rx.hstack(

            *[
                offer_card(item)
                for item in offers
            ],

            spacing="5",

            justify="center",

            width="100%",
        ),

        width="100%",

        align_items="center",

        padding_top="2em",
        padding_bottom="2em",
    )