import reflex as rx
import json


with open("data/team.json", "r", encoding="utf-8") as f:
    team_data = json.load(f)


def team_card(member):

    return rx.box(

        rx.vstack(

            rx.box(

                rx.image(
                    src=member["image"],
                    width="115px",
                    height="115px",
                    border_radius="14px",
                    object_fit="cover",
                ),

                overflow="hidden",
                border_radius="14px",
            ),

            rx.text(
                member["name"],
                font_weight="bold",
                color="#023047",
                font_size="0.95em",
                text_align="center",
            ),

            rx.text(
                member["role"],
                color="gray",
                font_size="0.8em",
                text_align="center",
            ),

            spacing="2",
            align="center",
        ),

        bg="white",
        padding="1em",
        border_radius="18px",
        box_shadow="0 5px 15px rgba(0,0,0,0.06)",

        width="160px",

        cursor="pointer",
        transition="all 0.3s ease",

        _hover={
            "transform": "translateY(-10px)",
            "box_shadow": "0 15px 30px rgba(0,0,0,0.15)",
        },
    )


def about_team():

    return rx.box(

        rx.vstack(

            rx.heading(
                "Nuestro Equipo",
                size="7",
                color="#023047",
            ),

            rx.hstack(

                *[
                    team_card(member)
                    for member in team_data
                ],

                spacing="3",
                justify="center",
            ),

            spacing="4",
            align="center",
        ),

        width="46%",
    )