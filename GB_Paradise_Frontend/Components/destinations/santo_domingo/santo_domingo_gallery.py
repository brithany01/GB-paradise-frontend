import reflex as rx
import json

with open("data/santo_domingo.json", "r", encoding="utf-8") as file:
    DATA = json.load(file)

gallery = DATA["gallery"]


def gallery_image(image_path):

    return rx.box(

        rx.image(
            src=image_path,

            width="100%",

            height="180px",

            object_fit="cover",

            border_radius="20px",
        ),

        width="240px",

        flex_shrink="0",

        transition="all 0.3s ease",

        _hover={
            "transform": "scale(1.03)"
        },
    )


def santo_domingo_gallery():

    return rx.vstack(

        # TITULO
        rx.vstack(

            rx.heading(
                "Galería del destino",
                color="#023047",
                size="6",
            ),

            rx.box(
                width="60px",
                height="4px",
                bg="#F6B800",
                border_radius="999px",
            ),

            spacing="2",

            align_items="center",
        ),

        # GALERIA
        rx.hstack(

            *[
                gallery_image(image)
                for image in gallery
            ],

            spacing="4",

            justify="center",

            wrap="nowrap",

            width="100%",
        ),

        width="100%",

        max_width="1500px",

        margin="auto",

        padding_top="2rem",

        padding_bottom="3rem",

        align_items="center",
    )