import reflex as rx


def hero_features():
    return rx.vstack(

        # Viaja fácil
        rx.hstack(

            rx.box(
                "✈️",
                bg="#12B3C7",
                color="white",
                border_radius="50%",
                width="55px",
                height="55px",
                display="flex",
                align_items="center",
                justify_content="center",
                font_size="1.2em",
                flex_shrink="0",
            ),

            rx.vstack(

                rx.text(
                    "Viaja fácil",
                    font_weight="bold",
                    color="#023047",
                    font_size="1em",
                ),

                rx.text(
                    "Reservas rápidas y seguras",
                    font_size="0.8em",
                    color="#64748B",
                ),

                align_items="start",
                spacing="1",
            ),

            spacing="3",
            width="100%",
            align="center",
        ),

        rx.divider(),

        # Mejores precios
        rx.hstack(

            rx.box(
                "🛡️",
                bg="#FFC107",
                color="white",
                border_radius="50%",
                width="55px",
                height="55px",
                display="flex",
                align_items="center",
                justify_content="center",
                font_size="1.2em",
                flex_shrink="0",
            ),

            rx.vstack(

                rx.text(
                    "Mejores precios",
                    font_weight="bold",
                    color="#023047",
                    font_size="1em",
                ),

                rx.text(
                    "Ofertas exclusivas cada día",
                    font_size="0.8em",
                    color="#64748B",
                ),

                align_items="start",
                spacing="1",
            ),

            spacing="3",
            width="100%",
            align="center",
        ),

        rx.divider(),

        # Atención 24/7
        rx.hstack(

            rx.box(
                "🎧",
                bg="#0096C7",
                color="white",
                border_radius="50%",
                width="55px",
                height="55px",
                display="flex",
                align_items="center",
                justify_content="center",
                font_size="1.2em",
                flex_shrink="0",
            ),

            rx.vstack(

                rx.text(
                    "Atención 24/7",
                    font_weight="bold",
                    color="#023047",
                    font_size="1em",
                ),

                rx.text(
                    "Estamos contigo en cada paso",
                    font_size="0.8em",
                    color="#64748B",
                ),

                align_items="start",
                spacing="1",
            ),

            spacing="3",
            width="100%",
            align="center",
        ),

        spacing="3",

        padding="1.2em",

        bg="white",

        border_radius="22px",

        box_shadow="0 8px 25px rgba(0,0,0,0.10)",

        width="260px",

        margin_top="70px",

        z_index="10",
    )