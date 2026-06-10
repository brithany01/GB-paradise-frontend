import reflex as rx


def about_hero():

    return rx.box(

        # Overlay blanco degradado
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
                    src="/about_title.png",
                    width="620px",
                ),

                rx.text(
                    """
                    En GB Paradise Travel, creemos que cada viaje
                    tiene el poder de transformar vidas y crear
                    recuerdos que duran para siempre.
                    """,
                    color="#023047",
                    font_size="1.15em",
                    max_width="500px",
                    line_height="1.8",
                    margin_top="-10px",
                ),

                align_items="start",
                spacing="1",

                # Posición similar a la referencia original
                margin_left="30px",

                z_index="20",
            ),

            rx.spacer(),

            # TARJETA MISIÓN
            rx.box(

                rx.vstack(

                    rx.box(
                        "♡",
                        bg="#18B7C8",
                        color="white",
                        border_radius="50%",
                        width="70px",
                        height="70px",
                        display="flex",
                        align_items="center",
                        justify_content="center",
                        font_size="2em",
                    ),

                    rx.text(
                        "Nuestra misión",
                        font_weight="bold",
                        font_size="1.4em",
                        color="#023047",
                    ),

                    rx.text(
                        """
                        Hacer que cada viaje sea una experiencia
                        inolvidable, conectando personas con los
                        lugares más extraordinarios del mundo.
                        """,
                        text_align="center",
                        color="#023047",
                        font_size="0.95em",
                        line_height="1.8",
                    ),

                    rx.box(
                        width="50px",
                        height="4px",
                        bg="#18B7C8",
                        border_radius="999px",
                    ),

                    spacing="4",
                    align_items="center",
                ),

                bg="white",
                padding="2em",
                border_radius="28px",
                box_shadow="0 10px 25px rgba(0,0,0,0.10)",
                width="280px",
                z_index="20",
            ),

            width="100%",
            align="center",
        ),

        background_image="url('/about_bg.png')",
        background_size="cover",
        background_position="center",

        width="100%",
        min_height="560px",

        border_radius="25px",

        padding="5em 6em 5em 6em",

        margin_top="1em",

        position="relative",
        overflow="hidden",
    )