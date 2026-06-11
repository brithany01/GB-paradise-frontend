import reflex as rx
import json

with open("data/bavaro.json", "r", encoding="utf-8") as file:
    DATA = json.load(file)

gallery = DATA["gallery"]


def gallery_image(image_path):

    return rx.box(

        rx.image(
            src=image_path,

            width="100%",

            height="140px",

            object_fit="cover",

            border_radius="18px",
        ),

        width="220px",

        transition="all 0.3s ease",

        _hover={
            "transform": "scale(1.03)"
        },
    )


def bavaro_gallery():

    return rx.vstack(

        # TITULO
        rx.vstack(

            rx.heading(
                "Galería del destino",
                color="#023047",
                size="5",
            ),

            rx.box(
                width="40px",
                height="4px",
                bg="#F6B800",
                border_radius="999px",
            ),

            spacing="2",

            align_items="center",
        ),

        # IMAGENES
        rx.hstack(

            *[
                gallery_image(image)
                for image in gallery
            ],

            spacing="3",

            justify="center",

            wrap="nowrap",

            width="100%",
        ),

        width="100%",

        max_width="1400px",

        margin="auto",

        padding_top="2rem",

        padding_bottom="2rem",

        align_items="center",
    )