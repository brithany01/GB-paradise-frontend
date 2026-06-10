import reflex as rx

from ..Components.navbar import navbar
from .destinatation_section import destinations_section
from ..Components.hero_features import hero_features
from ..Components.Serch_bar import search_bar
from ..Components.feauters_banner import features_banner
from ..Components.footer import footer


def home():
    return rx.box(

        # NAVBAR
        navbar(),

        # HERO
        rx.box(

            # Overlay degradado
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
                        src="/hero_title.png",
                        width="680px",
                        margin_bottom="-80px",
                    ),

                    rx.text(
                        "Descubre los destinos más increíbles y",
                        font_size="1.2em",
                        color="#023047",
                    ),

                    rx.text(
                        "vive experiencias inolvidables.",
                        font_size="1.2em",
                        color="#023047",
                        font_weight="bold",
                    ),

                    rx.hstack(

                        rx.button(
                            "✈️ Explorar Ofertas",
                            bg="#0096C7",
                            color="white",
                            border_radius="25px",
                            size="3",
                        ),

                        rx.button(
                            "Ver Destinos",
                            bg="white",
                            color="#023047",
                            border="2px solid #0096C7",
                            border_radius="25px",
                            size="3",
                        ),

                        spacing="3",
                    ),

                    align_items="start",
                    spacing="1",
                    width="40%",
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
            padding="4em 4em 4em 10em",

            margin_top="1em",
            margin_bottom="0",
            margin_left="0",
            margin_right="0",

            position="relative",
            overflow="hidden",
        ),

        # SEARCH BAR FLOTANTE
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
        destinations_section(),

        # BENEFICIOS
        features_banner(),

        # FOOTER
        footer(),

        bg="#F8F9FA",
    )

