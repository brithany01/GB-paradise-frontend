import reflex as rx


def destination_card(destination):

    return rx.link(

        rx.box(

            # IMAGEN
            rx.box(

                rx.image(
                    src=destination["image"],
                    width="100%",
                    height="110px",
                    object_fit="cover",
                ),

                rx.badge(
                    destination["category"],
                    position="absolute",
                    top="8px",
                    left="8px",
                    color_scheme="cyan",
                    border_radius="20px",
                    size="1",
                ),

                position="relative",
            ),

            # CONTENIDO
            rx.vstack(

                rx.text(
                    destination["title"],
                    font_weight="bold",
                    font_size="0.92em",
                    color="#023047",
                    line_height="1.2",
                ),

                rx.text(
                    destination["description"],
                    color="#64748B",
                    font_size="0.78em",
                ),

                rx.hstack(

                    rx.text(
                        destination["price"],
                        color="#00B4D8",
                        font_weight="bold",
                        font_size="0.9em",
                    ),

                    rx.spacer(),

                    rx.text(
                        f"⭐ {destination['rating']}",
                        color="#023047",
                        font_size="0.8em",
                    ),

                    width="100%",
                ),

                align_items="start",
                spacing="1",
                padding="0.8em",
            ),

            bg="white",

            border_radius="18px",

            overflow="hidden",

            width="190px",

            box_shadow="0 4px 15px rgba(0,0,0,0.06)",

            transition="all 0.25s ease",

            _hover={
                "transform": "translateY(-6px)",
                "box_shadow": "0 10px 20px rgba(0,0,0,0.12)",
            },
        ),

        href=destination["route"],
        text_decoration="none",
    )