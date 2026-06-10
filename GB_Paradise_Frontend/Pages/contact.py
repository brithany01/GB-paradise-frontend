import reflex as rx

from ..Components.navbar import navbar
from ..Components.footer import footer

from ..Components.contact_hero import contact_hero
from ..Components.contact_info import contact_info
from ..Components.contact_form import contact_form
from ..Components.contact_services import contact_services
from ..Components.contact_location import contact_location
from ..Components.contact_cta import contact_cta
from ..Components.contact_features import contact_features


def contact():

    return rx.box(

        navbar(),

        rx.box(height="95px"),

        # HERO
        contact_hero(),

        # CONTACTOS
        rx.center(

            contact_info(),

            width="100%",
            margin_top="-55px",
            position="relative",
            z_index="100",
        ),

        # FORMULARIO + SERVICIOS
        rx.center(

            rx.hstack(

                rx.box(
                    contact_form(),
                    width="55%",
                ),

                rx.box(
                    contact_services(),
                    width="40%",
                ),

                spacing="6",
                align="start",
                width="95%",
                justify="center",
            ),

            width="100%",
            margin_top="2.5em",
            margin_bottom="3em",
        ),

        # UBICACIÓN CENTRADA
        rx.center(

            rx.box(

                contact_location(),

                width="95%",
                max_width="1700px",
            ),

            width="100%",
            margin_bottom="3em",
        ),

        # CTA
        contact_cta(),

        # BENEFICIOS
        contact_features(),

        footer(),

        bg="#EAFBFD",
        width="100%",
        overflow_x="hidden",
    )