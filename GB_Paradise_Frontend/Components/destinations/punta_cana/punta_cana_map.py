import reflex as rx
import json

with open("data/punta_cana.json", "r", encoding="utf-8") as file:
    DATA = json.load(file)

map_data = DATA["map"]


def punta_cana_map():

    return rx.box(

        rx.image(
            src=map_data["image"],
            width="100%",
            height="100%",
            object_fit="cover",
        ),

        rx.box(

            rx.vstack(

                rx.heading(
                    map_data["title"],
                    size="4",
                ),

                rx.text(
                    "República Dominicana",
                    color="#64748B",
                    font_size="0.85em",
                ),

                *[
                    rx.hstack(

                        rx.text(
                            "✓",
                            color="#18B7C8",
                        ),

                        rx.text(
                            feature,
                            font_size="0.8em",
                        ),

                        spacing="2",
                    )

                    for feature in map_data["features"]
                ],

                spacing="2",
                align_items="start",
            ),

            position="absolute",

            top="20px",
            right="20px",

            bg="white",

            width="260px",

            padding="1.3em",

            border_radius="16px",

            box_shadow="0 8px 25px rgba(0,0,0,0.12)",
        ),

        width="50%",
        height="340px",

        position="relative",

        overflow="hidden",

        border_radius="20px",

        bg="#E8F7FF",
    )