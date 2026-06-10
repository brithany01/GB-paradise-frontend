import reflex as rx

from ..Components.navbar import navbar
from ..Components.footer import footer
from ..Components.feauters_banner import features_banner

from ..Components.experience_hero import experience_hero
from ..Components.experience_search import experience_search
from ..Components.experience_categories import experience_categories
from ..Components.experiences_grid import experience_grid


def experiences():

    return rx.box(

        navbar(),

        # HERO
        experience_hero(),

        # BUSCADOR
        experience_search(),

        # CATEGORÍAS
        experience_categories(),

        # GRID DE EXPERIENCIAS
        experience_grid(),

        # BENEFICIOS
        features_banner(),

        # FOOTER
        footer(),

        bg="#F8F9FA",
    )