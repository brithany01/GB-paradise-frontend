import reflex as rx

from ..Components.navbar import navbar
from ..Components.footer import footer
from ..Components.hero_features import hero_features
from ..Components.Serch_bar import search_bar
from ..Components.feauters_banner import features_banner
from ..Components.destinations_grid import destinations_grid


def destinations():

    return rx.box(

        navbar(),

        # HERO
        rx.box(

            # Overlay igual al Home
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
                    rgba(255,255,255,0.78) 8%,
                    rgba(255,255,255,0.88) 18%,
                    rgba(255,255,255,0.78) 28%,
                    rgba(255,255,255,0.48) 40%,
                    rgba(255,255,255,0.15) 52%,
                    rgba(255,255,255,0) 62%
                )
                """,
                border_radius="25px",
            ),

            rx.hstack(

                # CONTENIDO IZQUIERDO
                rx.vstack(

                    rx.image(
                        src="/destination_tittle.png",
                        width="520px",
                        margin_bottom="-20px",
                    ),

                    rx.text(
                        "Descubre playas paradisíacas, montañas",
                        font_size="1.2em",
                        color="#023047",
                    ),

                    rx.text(
                        "majestuosas, cultura vibrante y aventuras únicas.",
                        font_size="1.2em",
                        color="#023047",
                    ),

                    align_items="start",
                    spacing="2",
                    width="45%",
                    position="relative",
                    z_index="10",
                ),

                rx.spacer(),

                hero_features(),

                width="100%",
                height="100%",
                align="center",
            ),

            background_image="url('/bg.png')",
            background_size="cover",
            background_position="center",

            width="100%",

            border_radius="25px",

            min_height="650px",

            padding="4em 4em 4em 8em",

            margin_top="1em",
            margin_bottom="0",
            margin_left="0",
            margin_right="0",

            position="relative",
            overflow="hidden",
        ),

        # SEARCH BAR
        rx.center(

            rx.box(
                search_bar(),
                margin_top="-110px",
                position="relative",
                z_index="200",
            ),

            width="100%",
        ),

        # DESTINOS
        destinations_grid(),

        # BENEFICIOS
        features_banner(),

        # FOOTER
        footer(),

        bg="#F8F9FA",
    )