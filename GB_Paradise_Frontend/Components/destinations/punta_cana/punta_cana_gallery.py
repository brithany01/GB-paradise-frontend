import reflex as rx
import json

with open("data/punta_cana.json", "r", encoding="utf-8") as file:
    DATA = json.load(file)

gallery = DATA["gallery"]


def punta_cana_gallery():

    return rx.vstack(

        rx.heading(
            "Galería del destino",
            size="6",
            color="#023047",
        ),

        rx.flex(

            *[
                rx.image(
                    src=image,

                    width="180px",
                    height="120px",

                    object_fit="cover",

                    border_radius="14px",

                    box_shadow="0 5px 15px rgba(0,0,0,0.10)",

                    transition="0.3s",

                    _hover={
                        "transform": "scale(1.03)"
                    }
                )

                for image in gallery
            ],

            gap="16px",
            wrap="wrap",

            width="100%",
        ),

        width="50%",
        align_items="start",
    )