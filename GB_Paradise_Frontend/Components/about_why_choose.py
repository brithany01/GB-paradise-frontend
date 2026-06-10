import reflex as rx


def about_why_choose():

    return rx.box(

        rx.vstack(

            rx.text(
                "¿Por qué elegirnos?",
                color="#023047",
                font_weight="bold",
                font_size="1.2em",
            ),

            rx.text(
                "✈ Viajes 100% personalizados",
                color="#023047",
            ),

            rx.text(
                "💰 Precios competitivos",
                color="#023047",
            ),

            rx.text(
                "📋 Reservas rápidas y seguras",
                color="#023047",
            ),

            rx.text(
                "🎧 Soporte en todo momento",
                color="#023047",
            ),

            rx.text(
                "⭐ Opiniones que nos respaldan",
                color="#023047",
            ),

            rx.hstack(

                rx.text(
                    "★★★★★",
                    color="#FDBA21",
                    font_size="1.2em",
                ),

                rx.text(
                    "4.8/5 en Google",
                    color="#023047",
                    font_weight="bold",
                ),

                spacing="2",
            ),

            spacing="4",
            align_items="start",
        ),

        bg="#EAFBFD",
        padding="1.5em",
        border_radius="24px",
        box_shadow="0 4px 12px rgba(0,0,0,0.06)",

        width="240px",
        min_width="240px",

        height="fit-content",
    )