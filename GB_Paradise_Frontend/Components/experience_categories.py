import reflex as rx


def category_item(icon, color, title):

    return rx.vstack(

        rx.box(
            icon,
            bg=color,
            color="white",
            border_radius="50%",
            width="50px",
            height="50px",
            display="flex",
            align_items="center",
            justify_content="center",
            font_size="1.2em",
        ),

        rx.text(
            title,
            color="#023047",
            font_weight="600",
            font_size="0.9em",
        ),

        spacing="2",
        align="center",
    )


def experience_categories():

    return rx.center(

        rx.box(

            rx.hstack(

                category_item("✨", "#18B7C8", "Todas"),

                category_item("🏔️", "#8BC34A", "Aventura"),

                category_item("🌿", "#18B7C8", "Naturaleza"),

                category_item("🏛️", "#9C27B0", "Cultura"),

                category_item("🏖️", "#2979FF", "Playa"),

                category_item("🍴", "#FF9800", "Gastronomía"),

                category_item("🧘", "#E91E63", "Relax"),

                category_item("🐠", "#2962FF", "Vida marina"),

                spacing="8",
                justify="center",
                width="100%",
            ),

            bg="white",
            padding="1.5em 2em",
            border_radius="30px",
            box_shadow="0 8px 20px rgba(0,0,0,0.08)",
            width="90%",
            max_width="1200px",
        ),

        margin_top="2em",
        margin_bottom="2em",
        width="100%",
    )