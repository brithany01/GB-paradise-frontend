import reflex as rx

from ...Components.navbar import navbar
from ...Components.footer import footer

from ...Components.destinations.punta_cana.punta_cana_hero import punta_cana_hero
from ...Components.destinations.punta_cana.punta_cana_info import punta_cana_info
from ...Components.destinations.punta_cana.punta_cana_includes import punta_cana_includes
from ...Components.destinations.punta_cana.punta_cana_gallery import punta_cana_gallery
from ...Components.destinations.punta_cana.punta_cana_itinerary import punta_cana_itinerary
from ...Components.destinations.punta_cana.punta_cana_map import punta_cana_map
from ...Components.destinations.punta_cana.punta_cana_offers import punta_cana_offers
from ...Components.destinations.punta_cana.punta_cana_cta import punta_cana_cta


def punta_cana():

    return rx.box(

        # NAVBAR
        navbar(),

        # HERO
        punta_cana_hero(),

        # INFO FLOTANTE
        punta_cana_info(),

        rx.box(height="4em"),

        # ==========================
        # INCLUDES + GALLERY
        # ==========================
        rx.hstack(

            punta_cana_includes(),

            punta_cana_gallery(),

            width="100%",
            max_width="1400px",

            margin="0 auto",

            align="start",

            justify="between",

            spacing="8",

            padding_left="2em",
            padding_right="2em",
        ),

        rx.box(height="4em"),

        # ==========================
        # ITINERARIO + MAPA
        # ==========================
        rx.hstack(

            punta_cana_itinerary(),

            punta_cana_map(),

            width="100%",
            max_width="1400px",

            margin="0 auto",

            align="start",

            justify="between",

            spacing="8",

            padding_left="2em",
            padding_right="2em",
        ),

        rx.box(height="3em"),

        # ==========================
        # OFERTAS
        # ==========================
        rx.box(

            punta_cana_offers(),

            width="100%",

            max_width="1400px",

            margin="0 auto",

            padding_left="2em",
            padding_right="2em",
        ),

        rx.box(height="2em"),

        # ==========================
        # CTA
        # ==========================
        rx.box(

            punta_cana_cta(),

            width="100%",

            max_width="1400px",

            margin="0 auto",

            padding_left="2em",
            padding_right="2em",
        ),

        rx.box(height="3em"),

        # FOOTER
        footer(),

        width="100%",

        bg="#F8FAFC",
    )