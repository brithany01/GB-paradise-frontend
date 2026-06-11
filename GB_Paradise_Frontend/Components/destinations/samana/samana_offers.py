import reflex as rx
import json

with open("data/samana.json", "r", encoding="utf-8") as file:
    DATA = json.load(file)

offers = DATA["offers"]


def offer_card(item):

    return rx.box(

        # Imagen
        rx.box(

            rx.image(
                src=item["image"],
                width="100%",
                height="120px",
                object_fit="cover",
            ),

            rx.badge(

                item["discount"],

                bg="#18B7C8",

                color="white",

                position="absolute",

                top="10px",

                left="10px",

                padding="0.3em 0.7em",

                border_radius="999px",
            ),

            position="relative",
        ),

        # Contenido
        rx.vstack(

            rx.hstack(

                rx.text(
                    item["duration"],
                    color="#64748B",
                    font_size="0.75rem",
                ),

                rx.spacer(),

                rx.text(
                    f"⭐ {item['rating']}",
                    color="#64748B",
                    font_size="0.75rem",
                ),

                width="100%",
            ),

            rx.text(
                item["title"],
                font_weight="700",
                color="#0F172A",
                font_size="0.9rem",
            ),

            rx.hstack(

                rx.text(
                    item["old_price"],
                    text_decoration="line-through",
                    color="#94A3B8",
                    font_size="0.75rem",
                ),

                rx.text(
                    item["price"],
                    color="#18B7C8",
                    font_weight="700",
                    font_size="1rem",
                ),

                spacing="2",
            ),

            rx.button(

                "Reservar",

                width="100%",

                height="40px",

                bg="#F6B800",

                color="white",

                border_radius="10px",

                font_weight="600",

                font_size="0.85rem",

                on_click=rx.redirect("/reservation"),

                _hover={
                    "bg": "#E2AA00"
                },
            ),

            align_items="start",

            spacing="2",

            width="100%",

            padding="1rem",
        ),

        bg="white",

        width="220px",

        flex_shrink="0",

        overflow="hidden",

        border_radius="20px",

        box_shadow="0 8px 24px rgba(0,0,0,0.08)",

        transition="all 0.3s ease",

        _hover={
            "transform": "translateY(-4px)",
            "box_shadow": "0 16px 40px rgba(0,0,0,0.12)"
        },
    )


def samana_offers():

    return rx.vstack(

        rx.vstack(

            rx.heading(
                "Ofertas destacadas",
                color="#023047",
                size="6",
            ),

            rx.text(
                "Descubre las mejores experiencias en Samaná",
                color="#64748B",
            ),

            spacing="2",

            align_items="center",
        ),

        rx.hstack(

            *[
                offer_card(item)
                for item in offers
            ],

            spacing="4",

            justify="center",

            wrap="nowrap",

            width="100%",
        ),

        width="100%",

        max_width="1500px",

        margin="auto",

        padding_top="4rem",

        padding_bottom="4rem",

        align_items="center",
    )