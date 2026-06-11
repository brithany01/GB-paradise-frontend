import reflex as rx

from GB_Paradise_Frontend.Components.navbar import navbar
from GB_Paradise_Frontend.Components.feauters_banner import features_banner
from GB_Paradise_Frontend.Components.footer import footer


from GB_Paradise_Frontend.Components.destinations.jarabacoa.jarabacoa_hero import jarabacoa_hero
from GB_Paradise_Frontend.Components.destinations.jarabacoa.jarabacoa_info import jarabacoa_info
from GB_Paradise_Frontend.Components.destinations.jarabacoa.jarabacoa_includes import jarabacoa_includes
from GB_Paradise_Frontend.Components.destinations.jarabacoa.jarabacoa_gallery import jarabacoa_gallery
from GB_Paradise_Frontend.Components.destinations.jarabacoa.jarabacoa_offers import jarabacoa_offers
from GB_Paradise_Frontend.Components.destinations.jarabacoa.jarabacoa_cta import jarabacoa_cta


def jarabacoa():

    return rx.box(

        # NAVBAR
        navbar(),

        # HERO
        jarabacoa_hero(),

        # INFO FLOTANTE
        jarabacoa_info(),

        # INCLUYE
        jarabacoa_includes(),

        # GALERÍA
        jarabacoa_gallery(),

        # OFERTAS
        jarabacoa_offers(),

        features_banner(),

        footer(),

        width="100%",

        bg="#F8FAFC",
    )