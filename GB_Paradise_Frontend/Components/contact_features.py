import reflex as rx
import json


with open("data/contact_features.json", "r", encoding="utf-8") as f:
    features_data = json.load(f)


def feature_card(feature):

    return rx.hstack(

        rx.box(
            feature["icon"],
            bg=feature["color"],
            color="white",
            border_radius="50%",
            width="55px",
            height="55px",
            display="flex",
            align_items="center",
            justify_content="center",
            font_size="1.4em",
        ),

        rx.vstack(

            rx.text(
                feature["title"],
                font_weight="bold",
                color="#023047",
            ),

            rx.text(
                feature["description"],
                color="gray",
                font_size="0.85em",
            ),

            align_items="start",
            spacing="1",
        ),

        spacing="3",
        align="center",
    )


def contact_features():

    return rx.center(

        rx.box(

            rx.hstack(

                *[
                    feature_card(feature)
                    for feature in features_data
                ],

                justify="between",
                width="100%",
            ),

            bg="#EAFBFD",
            border_radius="25px",
            padding="1.5em 2em",
            width="95%",
        ),

        width="100%",
        margin_bottom="3em",
    )