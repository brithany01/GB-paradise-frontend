import reflex as rx
import json


with open("data/contact_info.json", "r", encoding="utf-8") as f:
    contact_info_data = json.load(f)


def info_card(item):

    return rx.box(

        rx.hstack(

            rx.box(
                item["icon"],
                bg=item["color"],
                color="white",
                border_radius="50%",
                width="65px",
                height="65px",
                display="flex",
                align_items="center",
                justify_content="center",
                font_size="1.8em",
                flex_shrink="0",
            ),

            rx.vstack(

                rx.text(
                    item["title"],
                    font_weight="bold",
                    color="#023047",
                    font_size="1.05em",
                ),

                rx.text(
                    item["value"],
                    color="#023047",
                    font_weight="500",
                ),

                rx.text(
                    item["extra"],
                    color="gray",
                    font_size="0.85em",
                ),

                align_items="start",
                spacing="1",
            ),

            spacing="4",
            align="center",
        ),

        bg="white",

        padding="1.4em",

        border_radius="22px",

        box_shadow="0 6px 18px rgba(0,0,0,0.08)",

        width="310px",
    )


def contact_info():

    return rx.hstack(

        *[
            info_card(item)
            for item in contact_info_data
        ],

        justify="center",
        spacing="4",
        width="100%",
    )