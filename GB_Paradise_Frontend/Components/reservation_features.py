import reflex as rx
import json


with open("data/reservation_features.json", encoding="utf-8") as f:
    features = json.load(f)


def feature_card(feature):

    return rx.hstack(

        rx.box(
            "★",
            bg="#18B7C8",
            color="white",
            border_radius="50%",
            width="60px",
            height="60px",
            display="flex",
            align_items="center",
            justify_content="center",
        ),

        rx.vstack(

            rx.text(
                feature["title"],
                font_weight="bold",
                color="#023047",
            ),

            rx.text(
                feature["description"],
                color="#4A5568",
                font_size="0.9em",
            ),

            align_items="start",
        ),

        spacing="4",
        width="280px",
    )


def reservation_features():

    return rx.hstack(

        *[
            feature_card(feature)
            for feature in features
        ],

        justify="center",
        wrap="wrap",
        spacing="6",
        width="100%",
        margin_top="2em",
        margin_bottom="3em",
    )