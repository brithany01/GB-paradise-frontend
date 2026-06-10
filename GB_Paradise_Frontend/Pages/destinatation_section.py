import json
import reflex as rx

from ..Components.destinatation_card import destination_card


with open("assets/data/offers.json", "r", encoding="utf-8") as file:
    offers = json.load(file)


def destinations_section():

    return rx.vstack(

        # TÍTULO
        rx.vstack(

            rx.hstack(

                rx.text(
                    "❈❈",
                    color="#14B8C4",
                    font_size="1em",
                ),

                rx.heading(
                    "Destinos Populares",
                    color="#023047",
                    size="7",
                    font_weight="700",
                ),

                rx.text(
                    "❈❈",
                    color="#14B8C4",
                    font_size="1em",
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

        # TARJETAS + FLECHAS
        rx.hstack(

            # Flecha izquierda
            rx.button(
                "❮",

                on_click=rx.call_script(
                    """
                    document.getElementById('destinations-carousel')
                    .scrollBy({
                        left: -300,
                        behavior: 'smooth'
                    });
                    """
                ),

                border_radius="50%",
                bg="white",
                color="#00B4D8",
                width="55px",
                height="55px",
                box_shadow="0 4px 15px rgba(0,0,0,0.12)",
                flex_shrink="0",
            ),

            # Contenedor de tarjetas
            rx.box(

                rx.hstack(
                    *[
                        destination_card(destination)
                        for destination in offers
                    ],

                    spacing="4",
                    width="max-content",
                ),

                id="destinations-carousel",

                width="100%",
                overflow_x="auto",
                overflow_y="hidden",

                style={
                    "scrollbarWidth": "none",
                    "-ms-overflow-style": "none",
                    "scrollBehavior": "smooth",
                },
            ),

            # Flecha derecha
            rx.button(
                "❯",

                on_click=rx.call_script(
                    """
                    document.getElementById('destinations-carousel')
                    .scrollBy({
                        left: 300,
                        behavior: 'smooth'
                    });
                    """
                ),

                border_radius="50%",
                bg="white",
                color="#00B4D8",
                width="55px",
                height="55px",
                box_shadow="0 4px 15px rgba(0,0,0,0.12)",
                flex_shrink="0",
            ),

            width="100%",
            align="center",
            spacing="4",
        ),

        width="100%",
        padding="3em",
        align="center",
    )