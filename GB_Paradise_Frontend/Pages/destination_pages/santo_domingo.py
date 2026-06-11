import reflex as rx

from GB_Paradise_Frontend.Components.navbar import navbar
from GB_Paradise_Frontend.Components.footer import footer
from GB_Paradise_Frontend.Components.feauters_banner import features_banner

from GB_Paradise_Frontend.Components.destinations.santo_domingo.santo_domingo_hero import santo_domingo_hero
from GB_Paradise_Frontend.Components.destinations.santo_domingo.santo_domingo_info import santo_domingo_info
from GB_Paradise_Frontend.Components.destinations.santo_domingo.santo_domingo_includes import santo_domingo_includes
from GB_Paradise_Frontend.Components.destinations.santo_domingo.santo_domingo_gallery import santo_domingo_gallery
from GB_Paradise_Frontend.Components.destinations.santo_domingo.santo_domingo_offers import santo_domingo_offers


def santo_domingo():

    return rx.box(

        navbar(),

        santo_domingo_hero(),

        santo_domingo_info(),

        santo_domingo_includes(),

        santo_domingo_gallery(),

        santo_domingo_offers(),

        features_banner(),

        footer(),

        width="100%",

        bg="#F8FAFC",
    )