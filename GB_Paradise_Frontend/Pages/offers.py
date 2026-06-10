import reflex as rx

from ..Components.navbar import navbar
from ..Components.footer import footer
from ..Components.feauters_banner import features_banner
from ..Components.offer_countdown import offer_countdown
from ..Components.offer_grid import offers_grid
from ..Components.featured_offer import featured_offer


def offers():

    return rx.box(

        navbar(),

        # HERO
        rx.box(

            rx.box(
                width="100%",
                height="100%",
                position="absolute",
                top="0",
                left="0",
                background="""
                linear-gradient(
                    90deg,
                    rgba(255,255,255,0) 0%,
                    rgba(255,255,255,0.80) 10%,
                    rgba(255,255,255,0.92) 22%,
                    rgba(255,255,255,0.75) 35%,
                    rgba(255,255,255,0.20) 55%,
                    rgba(255,255,255,0) 70%
                )
                """,
            ),

            # CIRCULO 35%
            rx.image(
                src="/offer_discount_badge.png",
                width="380px",
                position="absolute",
                top="70px",
                right="-10px",
                z_index="20",
            ),

            rx.hstack(

                # IZQUIERDA
                rx.vstack(

                    rx.image(
                        src="/offers_title.png",
                        width="520px",
                    ),

                    rx.text(
                        "Descubre descuentos exclusivos",
                        font_size="1.2em",
                        color="#023047",
                        margin_top="-100px",
                    ),

                    rx.text(
                        "en los destinos más increíbles.",
                        font_size="1.2em",
                        color="#023047",
                        font_weight="bold",
                    ),

                    align_items="start",

                    spacing="0",

                    width="40%",

                    # MÁS ABAJO PARA QUE EL TÍTULO NO LO TAPE EL NAVBAR
                    margin_top="55px",

                    z_index="10",
                ),

                rx.spacer(),

                # CONTADOR
                rx.box(
                    offer_countdown(),

                    margin_top="60px",

                    # UN POCO MÁS A LA DERECHA
                    margin_right="430px",

                    z_index="20",
                ),

                width="100%",
                align="center",
            ),

            background_image="url('/offers_bg.png')",
            background_size="cover",
            background_position="center",

            width="100%",
            min_height="720px",

            border_radius="25px",

            padding="4em 4em 4em 8em",

            margin_top="1em",

            position="relative",
            overflow="hidden",
        ),

        # OFERTA DESTACADA
        rx.center(

            featured_offer(),

            width="100%",

            margin_top="-220px",
            margin_bottom="0",

            position="relative",
            z_index="300",
        ),

        # TITULO
        rx.box(

            rx.heading(
                "Todas las Ofertas",
                size="8",
                color="#023047",
            ),

            width="100%",

            margin_top="5em",
            margin_left="3em",
            margin_bottom="0.5em",
        ),

        # GRID
        rx.box(

            offers_grid(),

            width="100%",
            margin_top="0",
        ),

        # BENEFICIOS
        features_banner(),

        # FOOTER
        footer(),

        bg="#F8F9FA",
    )