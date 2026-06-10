import reflex as rx
import json
from pathlib import Path


def get_featured_offer():

    json_path = Path("assets") / "Data" / "ofertas.json"

    with open(json_path, "r", encoding="utf-8") as file:
        ofertas = json.load(file)

    return ofertas[0]


featured = get_featured_offer()


def featured_offer():

    return rx.center(

        rx.hstack(

            # IMAGEN
            rx.box(

                rx.box(
                    "⭐ OFERTA DE LA SEMANA",
                    position="absolute",
                    top="10px",
                    left="10px",
                    bg="#FFB703",
                    color="white",
                    font_weight="bold",
                    font_size="0.8em",
                    padding="0.5em 1em",
                    border_radius="25px",
                    z_index="5",
                ),

                rx.image(
                    src=featured["image"],
                    width="100%",
                    height="100%",
                    object_fit="cover",
                ),

                width="38%",
                height="100%",
                position="relative",
                overflow="hidden",
            ),

            # INFORMACIÓN
            rx.box(

                rx.vstack(

                    rx.text(
                        featured["title"],
                        font_size="1.4em",
                        font_weight="bold",
                        color="#023047",
                    ),

                    rx.text(
                        featured["description"],
                        color="#64748B",
                        font_size="0.85em",
                    ),

                    rx.text(
                        "Disfruta de playas paradisíacas y experiencias inolvidables.",
                        color="#475569",
                        font_size="0.8em",
                    ),

                    rx.hstack(

                        rx.text(
                            "🍽️ Almuerzo incluido",
                            font_size="0.75em",
                        ),

                        rx.text(
                            "🚌 Transporte",
                            font_size="0.75em",
                        ),

                        rx.text(
                            "🧑‍💼 Guía",
                            font_size="0.75em",
                        ),

                        spacing="3",
                        margin_top="0.5em",
                    ),

                    align_items="start",
                    spacing="2",
                ),

                width="28%",
                padding="1em",
            ),

            # PRECIO
            rx.box(

                rx.vstack(

                    rx.box(
                        featured["discount"],
                        bg="#FFB703",
                        color="#023047",
                        font_weight="bold",
                        font_size="1.2em",
                        border_radius="10px",
                        padding="0.4em 0.8em",
                    ),

                    rx.text(
                        "ANTES",
                        font_size="0.7em",
                        color="#64748B",
                    ),

                    rx.text(
                        featured["old_price"],
                        text_decoration="line-through",
                        font_size="0.8em",
                        color="#64748B",
                    ),

                    rx.text(
                        "AHORA",
                        color="#14B8C4",
                        font_weight="bold",
                        font_size="0.8em",
                    ),

                    rx.text(
                        featured["price"],
                        font_size="1.6em",
                        font_weight="bold",
                        color="#14B8C4",
                    ),

                    rx.button(
                        "Reservar ahora",
                        bg="#14B8C4",
                        color="white",
                        border_radius="20px",
                        size="2",
                    ),

                    spacing="2",
                    align="center",
                ),

                width="14%",
                padding="0.8em",
            ),

            # PROMOCIÓN
            rx.box(

                rx.vstack(

                    rx.text(
                        "Ahorra hasta",
                        font_weight="bold",
                        color="#023047",
                        font_size="0.9em",
                    ),

                    rx.text(
                        "RD$5,000",
                        color="#14B8C4",
                        font_weight="bold",
                        font_size="1.8em",
                    ),

                    rx.text(
                        "en reservas realizadas",
                        color="#64748B",
                        font_size="0.7em",
                        text_align="center",
                    ),

                    rx.button(
                        "Ver promociones",
                        bg="#14B8C4",
                        color="white",
                        border_radius="20px",
                        size="2",
                    ),

                    spacing="2",
                    align="center",
                    justify="center",
                ),

                width="20%",
                padding="0.8em",
                border_left="1px dashed #14B8C4",
            ),

            width="100%",
            max_width="1050px",
            height="180px",
            bg="white",
            border_radius="25px",
            overflow="hidden",
            box_shadow="0 8px 20px rgba(0,0,0,0.08)",
        ),

        width="100%",
    )