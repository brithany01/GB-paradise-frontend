import reflex as rx

from GB_Paradise_Frontend.Components.navbar import navbar
from GB_Paradise_Frontend.Components.footer import footer
from GB_Paradise_Frontend.Components.feauters_banner import features_banner

from GB_Paradise_Frontend.Components.destinations.samana.samana_hero import samana_hero
from GB_Paradise_Frontend.Components.destinations.samana.samana_info import samana_info
from GB_Paradise_Frontend.Components.destinations.samana.samana_includes import samana_includes
from GB_Paradise_Frontend.Components.destinations.samana.samana_gallery import samana_gallery
from GB_Paradise_Frontend.Components.destinations.samana.samana_offers import samana_offers


def samana():

    return rx.box(

        navbar(),

        samana_hero(),

        samana_info(),

        samana_includes(),

        samana_gallery(),

        samana_offers(),

        features_banner(),

        footer(),

        width="100%",

        bg="#F8FAFC",
    )