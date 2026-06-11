import reflex as rx

from GB_Paradise_Frontend.Components.navbar import navbar
from GB_Paradise_Frontend.Components.footer import footer
from GB_Paradise_Frontend.Components.feauters_banner import features_banner

from GB_Paradise_Frontend.Components.destinations.isla_saona.isla_saona_hero import isla_saona_hero
from GB_Paradise_Frontend.Components.destinations.isla_saona.isla_saona_info import isla_saona_info
from GB_Paradise_Frontend.Components.destinations.isla_saona.isla_saona_includes import isla_saona_includes
from GB_Paradise_Frontend.Components.destinations.isla_saona.isla_saona_gallery import isla_saona_gallery
from GB_Paradise_Frontend.Components.destinations.isla_saona.isla_saona_offers import isla_saona_offers


def isla_saona():

    return rx.box(

        navbar(),

        isla_saona_hero(),

        isla_saona_info(),

        isla_saona_includes(),

        isla_saona_gallery(),

        isla_saona_offers(),

        features_banner(),

        footer(),

        width="100%",

        bg="#F8FAFC",
    )