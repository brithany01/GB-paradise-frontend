import reflex as rx
import json


with open("data/contact_services.json", "r", encoding="utf-8") as f:
    services_data = json.load(f)


def service_card(service):

    return rx.hstack(

        rx.box(
            service["icon"],
            bg=service["color"],
            color="white",
            border_radius="50%",
            width="55px",
            height="55px",
            display="flex",
            align_items="center",
            justify_content="center",
            font_size="1.4em",
            flex_shrink="0",
        ),

        rx.vstack(

            rx.text(
                service["title"],
                font_weight="bold",
                color="#023047",
            ),

            rx.text(
                service["description"],
                color="gray",
                font_size="0.85em",
            ),

            align_items="start",
            spacing="1",
        ),

        spacing="3",
        align="center",
    )


def contact_services():

    return rx.box(

        rx.vstack(

            rx.heading(
                "Estamos para ayudarte",
                size="6",
                color="#023047",
            ),

            rx.text(
                "Elige el canal que prefieras para comunicarte con nosotros.",
                color="gray",
                font_size="0.9em",
            ),

            rx.grid(

                *[
                    service_card(service)
                    for service in services_data
                ],

                columns="2",
                spacing="6",
                width="100%",
            ),

            spacing="5",
            align_items="start",
        ),

        bg="white",
        padding="2em",
        border_radius="25px",
        box_shadow="0 6px 18px rgba(0,0,0,0.08)",
        width="100%",
    )