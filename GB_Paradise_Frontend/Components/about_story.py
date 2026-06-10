import reflex as rx


def about_story():

    return rx.box(

        rx.vstack(

            rx.image(
                src="/about_beach.png",
                width="340px",
                height="230px",
                border_radius="22px",
                object_fit="cover",
            ),

            rx.text(
                "¿Quiénes somos?",
                color="#18B7C8",
                font_weight="bold",
                font_size="1.1em",
            ),

            rx.heading(
                "Somos GB Paradise Travel",
                font_size="3em",
                color="#023047",
                line_height="1.1",
            ),

            rx.text(
                """
                Somos una agencia de viajes apasionada por descubrir
                el mundo y compartir su magia. Nuestro equipo diseña
                experiencias únicas y personalizadas para cada viajero.
                """,
                color="gray",
                font_size="1em",
            ),

            rx.vstack(

                rx.hstack("✔", rx.text("Asesoría personalizada")),
                rx.hstack("✔", rx.text("Atención 24/7 durante tu viaje")),
                rx.hstack("✔", rx.text("Alianzas con los mejores proveedores")),
                rx.hstack("✔", rx.text("Experiencias auténticas y memorables")),

                spacing="2",
                align_items="start",
            ),

            align_items="start",
            spacing="3",
        ),

        width="28%",
        min_width="400px",
    )