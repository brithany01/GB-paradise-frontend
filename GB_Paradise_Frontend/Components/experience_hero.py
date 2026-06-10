import reflex as rx


def experience_hero():

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
                rgba(255,255,255,0.85) 20%,
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
                    src="/experiences_title.png",
                    width="720px",
                    margin_top="-60px",
                    margin_bottom="-90px",
                ),

                rx.text(
                    "Actividades únicas para conectar con la naturaleza,",
                    color="#023047",
                    font_size="1.25em",
                    margin_left="120px",
                ),

                rx.text(
                    "la cultura y la aventura.",
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

                    rx.hstack(
                        rx.box(
                            "✈️",
                            bg="#18B7C8",
                            color="white",
                            border_radius="50%",
                            padding="0.7em",
                        ),

                        rx.vstack(
                            rx.text(
                                "Experiencias únicas",
                                font_weight="bold",
                            ),

                            rx.text(
                                "Actividades exclusivas en cada destino",
                                font_size="0.9em",
                                color="gray",
                            ),

                            align_items="start",
                        ),

                        align="center",
                    ),

                    rx.divider(),

                    rx.hstack(
                        rx.box(
                            "🛡️",
                            bg="#FDBA21",
                            color="white",
                            border_radius="50%",
                            padding="0.7em",
                        ),

                        rx.vstack(
                            rx.text(
                                "Guías expertos",
                                font_weight="bold",
                            ),

                            rx.text(
                                "Profesionales locales a tu servicio",
                                font_size="0.9em",
                                color="gray",
                            ),

                            align_items="start",
                        ),

                        align="center",
                    ),

                    rx.divider(),

                    rx.hstack(
                        rx.box(
                            "🎧",
                            bg="#18B7C8",
                            color="white",
                            border_radius="50%",
                            padding="0.7em",
                        ),

                        rx.vstack(
                            rx.text(
                                "Atención 24/7",
                                font_weight="bold",
                            ),

                            rx.text(
                                "Estamos contigo en cada paso",
                                font_size="0.9em",
                                color="gray",
                            ),

                            align_items="start",
                        ),

                        align="center",
                    ),

                    spacing="4",
                    align_items="start",
                ),

                bg="white",
                padding="1.5em",
                border_radius="24px",
                box_shadow="0 10px 25px rgba(0,0,0,0.10)",
                width="320px",
                z_index="20",
            ),

            width="100%",
            align="center",
        ),

        background_image="url('/experiences_bg.png')",
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