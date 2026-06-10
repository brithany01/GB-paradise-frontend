import reflex as rx


def contact_hero():

    return rx.box(

        rx.box(
            width="100%",
            height="100%",
            position="absolute",
            top="0",
            left="0",
            background="""
            linear-gradient(
                90deg,
                rgba(255,255,255,0.95) 0%,
                rgba(255,255,255,0.88) 20%,
                rgba(255,255,255,0.55) 40%,
                rgba(255,255,255,0.10) 65%,
                rgba(255,255,255,0) 80%
            )
            """,
        ),

        rx.hstack(

            # IZQUIERDA
            rx.vstack(

                rx.image(
                    src="/contact_title.png",
                    width="820px",

                    # SUBIR MÁS EL TÍTULO
                    margin_top="-120px",

                    # DEJAR ESPACIO PARA EL TEXTO
                    margin_bottom="-80px",
                ),

                rx.text(
                    "¿Tienes preguntas o necesitas ayuda con tu viaje?",
                    color="#023047",
                    font_size="1.25em",
                    margin_left="120px",

                    # PEGADO AL LOGO
                    margin_top="-30px",
                ),

                rx.text(
                    "Nuestro equipo está listo para asistirte en todo lo que necesites.",
                    color="#023047",
                    font_size="1.25em",
                    font_weight="bold",
                    margin_left="120px",
                    margin_top="-8px",
                ),

                align_items="start",
                spacing="0",
                width="50%",
                z_index="20",
            ),

            rx.spacer(),

            # TARJETA DERECHA
            rx.box(

                rx.vstack(

                    rx.box(
                        "🎧",
                        bg="#18B7C8",
                        color="white",
                        border_radius="50%",
                        width="75px",
                        height="75px",
                        display="flex",
                        align_items="center",
                        justify_content="center",
                        font_size="2em",
                    ),

                    rx.text(
                        "Atención personalizada",
                        font_weight="bold",
                        color="#023047",
                        text_align="center",
                        font_size="1.2em",
                    ),

                    rx.text(
                        """
                        Te acompañamos en cada paso
                        de tu viaje para que sea
                        inolvidable.
                        """,
                        text_align="center",
                        color="#023047",
                        font_size="1em",
                    ),

                    spacing="3",
                    align="center",
                ),

                bg="white",
                padding="2.2em",
                border_radius="25px",
                width="290px",
                box_shadow="0 10px 25px rgba(0,0,0,0.10)",
                z_index="20",
            ),

            width="100%",
            align="center",
        ),

        background_image="url('/contact_hero_bg.png')",
        background_size="cover",
        background_position="center",

        width="100%",
        min_height="500px",

        border_radius="25px",

        padding="5em 5em 3em 6em",

        margin_top="1em",

        position="relative",
        overflow="hidden",
    )