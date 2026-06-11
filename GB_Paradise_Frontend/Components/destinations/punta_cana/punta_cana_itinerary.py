import reflex as rx
import json

with open("data/punta_cana.json", "r", encoding="utf-8") as file:
    DATA = json.load(file)

itinerary = DATA["itinerary"]


def itinerary_day(day):

    return rx.hstack(

        rx.vstack(

            rx.box(
                day["day"],

                bg="#18B7C8",
                color="white",

                width="50px",
                height="50px",

                border_radius="50%",

                display="flex",
                align_items="center",
                justify_content="center",

                font_weight="bold",
                font_size="0.8em",
            ),

            rx.box(
                width="2px",
                height="120px",
                bg="#F6B800",
            ),

            spacing="0",
            align="center",
        ),

        rx.vstack(

            *[
                rx.hstack(

                    rx.text(
                        item["time"],
                        width="90px",
                        font_weight="600",
                        color="#334155",
                        font_size="0.8em",
                    ),

                    rx.text(
                        item["title"],
                        font_weight="600",
                        color="#0F172A",
                        font_size="0.85em",
                    ),

                    spacing="4",
                    width="100%",
                )

                for item in day["items"]
            ],

            spacing="4",
            width="100%",
            align_items="start",
        ),

        spacing="4",
        width="100%",
        align="start",
    )


def punta_cana_itinerary():

    return rx.vstack(

        rx.heading(
            "Itinerario sugerido",
            size="5",
            color="#023047",
        ),

        *[
            itinerary_day(day)
            for day in itinerary
        ],

        width="50%",
        align_items="start",
    )