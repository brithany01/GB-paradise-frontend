import reflex as rx

from ..Components.navbar import navbar
from ..Components.footer import footer

from ..Components.about_hero import about_hero
from ..Components.about_stats import about_stats
from ..Components.about_values import about_values
from ..Components.about_story import about_story
from ..Components.about_team import about_team
from ..Components.about_why_choose import about_why_choose
from ..Components.about_cta import about_cta


def about():

    return rx.box(

        navbar(),

        about_hero(),

        about_stats(),

        about_values(),

        rx.center(

            rx.hstack(

                about_story(),

                about_team(),

                about_why_choose(),

                align="start",
                justify="center",

                # Menos espacio entre columnas
                spacing="3",

                width="96%",
            ),

            width="100%",
            margin_top="2em",
            margin_bottom="3em",
        ),

        about_cta(),

        footer(),

        bg="#F8F9FA",
        width="100%",
        overflow_x="hidden",
    )