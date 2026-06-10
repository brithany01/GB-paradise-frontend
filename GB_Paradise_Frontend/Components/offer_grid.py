import json
import reflex as rx

from .offer_card import offer_card


with open("assets/Data/ofertas.json", "r", encoding="utf-8") as file:
    offers = json.load(file)


def offers_grid():

    return rx.vstack(

        rx.center(

            rx.grid(

                *[
                    offer_card(offer)
                    for offer in offers
                ],

                columns="6",
                spacing="3",
            ),

            width="100%",
        ),

        width="100%",
        spacing="5",
        padding_top="0",
        padding_bottom="2em",
    )