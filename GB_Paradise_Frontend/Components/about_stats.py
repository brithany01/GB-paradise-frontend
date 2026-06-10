import reflex as rx


def stat_item(icon, number, text):

    return rx.hstack(

        rx.box(
            icon,
            bg="#18B7C8",
            color="white",
            border_radius="50%",
            width="65px",
            height="65px",
            display="flex",
            align_items="center",
            justify_content="center",
            font_size="1.8em",
        ),

        rx.vstack(

            rx.text(
                number,
                color="white",
                font_weight="bold",
                font_size="2.1em",
            ),

            rx.text(
                text,
                color="white",
                font_size="0.95em",
            ),

            spacing="0",
            align_items="start",
        ),

        spacing="3",
        align="center",
    )


def about_stats():

    return rx.center(

        rx.box(

            rx.hstack(

                stat_item(
                    "👥",
                    "+10,000",
                    "Viajeros felices",
                ),

                stat_item(
                    "🧳",
                    "+500",
                    "Destinos increíbles",
                ),

                stat_item(
                    "📅",
                    "+8 Años",
                    "De experiencia",
                ),

                stat_item(
                    "🏆",
                    "4.8/5",
                    "Calificación promedio",
                ),

                justify="between",
                width="100%",
            ),

            bg="#022B5B",

            width="1080px",

            padding="1.8em 3em",

            border_radius="24px",

            box_shadow="0 10px 25px rgba(0,0,0,0.18)",
        ),

        width="100%",

        margin_top="-35px",

        position="relative",

        z_index="300",
    )