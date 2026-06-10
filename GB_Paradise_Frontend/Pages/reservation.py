import reflex as rx

from GB_Paradise_Frontend.Components.navbar import navbar
from GB_Paradise_Frontend.Components.footer import footer

from GB_Paradise_Frontend.Components.reservation_hero import reservation_hero
from GB_Paradise_Frontend.Components.reservation_search import reservation_search
from GB_Paradise_Frontend.Components.reservation_steps import reservation_steps
from GB_Paradise_Frontend.Components.reservation_benefits import reservation_benefits
from GB_Paradise_Frontend.Components.reservation_cta import reservation_cta
from GB_Paradise_Frontend.Components.reservation_features import reservation_features


@rx.page(route="/reservation")
def reservation():

    return rx.box(

        navbar(),

        rx.box(height="100px"),

        reservation_hero(),

        reservation_search(),

        rx.hstack(

            rx.box(
                reservation_steps(),
                width="75%",
            ),

            rx.box(
                reservation_benefits(),
                width="25%",
                padding_top="5em",
            ),

            align="start",
            spacing="6",
            width="100%",
            max_width="1400px",
            margin="0 auto",
            padding="0 2em",
        ),

        rx.box(
            reservation_cta(),
            max_width="1400px",
            margin="0 auto",
            padding="0 2em",
        ),

        rx.box(
            reservation_features(),
            max_width="1400px",
            margin="0 auto",
            padding="0 2em",
        ),

        footer(),

        bg="#F8FAFC",
        min_height="100vh",
    )