import reflex as rx

from GB_Paradise_Frontend.Components.navbar import navbar
from GB_Paradise_Frontend.Components.footer import footer
from GB_Paradise_Frontend.Components.feauters_banner import features_banner

from GB_Paradise_Frontend.Components.destinations.bavaro.bavaro_hero import bavaro_hero
from GB_Paradise_Frontend.Components.destinations.bavaro.bavaro_info import bavaro_info
from GB_Paradise_Frontend.Components.destinations.bavaro.bavaro_includes import bavaro_includes
from GB_Paradise_Frontend.Components.destinations.bavaro.bavaro_gallery import bavaro_gallery
from GB_Paradise_Frontend.Components.destinations.bavaro.bavaro_offers import bavaro_offers


def bavaro():

    return rx.box(

        navbar(),

        bavaro_hero(),

        bavaro_info(),

        bavaro_includes(),

        bavaro_gallery(),

        bavaro_offers(),

        features_banner(),

        footer(),

        width="100%",

        bg="#F8FAFC",
    )