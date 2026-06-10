import reflex as rx


def features_banner():
    return rx.box(

        rx.hstack(

            # Destinos increíbles
            rx.hstack(
                rx.box(
                    "✈️",
                    bg="#14B8C4",
                    color="white",
                    border_radius="50%",
                    padding="0.8em",
                    font_size="1.2em",
                ),

                rx.vstack(
                    rx.text(
                        "Destinos increíbles",
                        font_weight="bold",
                        color="#023047",
                    ),
                    rx.text(
                        "Los mejores lugares del Caribe\nen un solo lugar.",
                        font_size="0.85em",
                        color="#64748B",
                    ),
                    align_items="start",
                    spacing="1",
                ),

                spacing="3",
            ),

            rx.divider(orientation="vertical", height="50px"),

            # Reservas seguras
            rx.hstack(
                rx.box(
                    "🏨",
                    bg="#FFC107",
                    color="white",
                    border_radius="50%",
                    padding="0.8em",
                    font_size="1.2em",
                ),

                rx.vstack(
                    rx.text(
                        "Reservas seguras",
                        font_weight="bold",
                        color="#023047",
                    ),
                    rx.text(
                        "Tu información está protegida\nsiempre.",
                        font_size="0.85em",
                        color="#64748B",
                    ),
                    align_items="start",
                    spacing="1",
                ),

                spacing="3",
            ),

            rx.divider(orientation="vertical", height="50px"),

            # Pagos fáciles
            rx.hstack(
                rx.box(
                    "💳",
                    bg="#14B8C4",
                    color="white",
                    border_radius="50%",
                    padding="0.8em",
                    font_size="1.2em",
                ),

                rx.vstack(
                    rx.text(
                        "Pagos fáciles",
                        font_weight="bold",
                        color="#023047",
                    ),
                    rx.text(
                        "Múltiples métodos de pago\ncon total seguridad.",
                        font_size="0.85em",
                        color="#64748B",
                    ),
                    align_items="start",
                    spacing="1",
                ),

                spacing="3",
            ),

            rx.divider(orientation="vertical", height="50px"),

            # Experiencias únicas
            rx.hstack(
                rx.box(
                    "👥",
                    bg="#FFC107",
                    color="white",
                    border_radius="50%",
                    padding="0.8em",
                    font_size="1.2em",
                ),

                rx.vstack(
                    rx.text(
                        "Experiencias únicas",
                        font_weight="bold",
                        color="#023047",
                    ),
                    rx.text(
                        "Actividades exclusivas para ti\ny tu acompañante.",
                        font_size="0.85em",
                        color="#64748B",
                    ),
                    align_items="start",
                    spacing="1",
                ),

                spacing="3",
            ),

            justify="between",
            width="100%",
        ),

        bg="rgba(20,184,196,0.08)",
        border_radius="25px",
        padding="2em",
        width="100%",
        margin_top="2em",
        margin_bottom="2em",
    )