import json
import reflex as rx

from .destinatation_card import destination_card


with open("assets/Data/destinations.json", "r", encoding="utf-8") as file:
    destinations = json.load(file)


def destinations_grid():

    return rx.vstack(

        # TITULO
        rx.vstack(

            rx.hstack(

                rx.text(
                    "❈❈",
                    color="#14B8C4",
                ),

                rx.heading(
                    "Explora Nuestros Destinos",
                    color="#023047",
                    size="7",
                ),

                rx.text(
                    "❈❈",
                    color="#14B8C4",
                ),

                spacing="3",
                justify="center",
                align="center",
            ),

            rx.box(
                width="40px",
                height="4px",
                bg="#FFC857",
                border_radius="10px",
            ),

            spacing="1",
            align="center",
        ),

        # GRID DESTINOS
        rx.center(

            rx.grid(

                *[
                    destination_card(destination)
                    for destination in destinations
                ],

                columns="6",
                spacing="3",
                width="fit-content",
            ),

            width="100%",
        ),

        rx.link(

            rx.button(
                "🌴 ¿Por qué elegir nuestros destinos?",
                bg="#00B4D8",
                color="white",
                border_radius="30px",
                box_shadow="0 4px 15px rgba(0,0,0,0.08)",
                size="3",
            ),

            href="/why-destinations",
            text_decoration="none",
        ),

        width="100%",
        padding_top="3em",
        padding_bottom="3em",

        align="center",
        spacing="5",
    )