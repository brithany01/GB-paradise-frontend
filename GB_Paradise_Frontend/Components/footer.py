import reflex as rx


def footer():
    return rx.box(

        rx.vstack(

            # Línea decorativa
            rx.box(
                width="120px",
                height="4px",
                bg="#00B4D8",
                border_radius="20px",
            ),

            rx.hstack(

                # LOGO + TEXTO
                rx.vstack(

                    rx.image(
                        src="/logo.png",
                        height="80px",
                        width="auto",
                    ),

                    rx.text(
                        "Tu paraíso comienza aquí.",
                        color="#5F6C7B",
                        font_size="0.95em",
                    ),

                    rx.text(
                        "Creamos experiencias inolvidables en los destinos más hermosos de República Dominicana.",
                        color="#7B8794",
                        max_width="320px",
                    ),

                    spacing="2",
                    align_items="start",
                    width="30%",
                ),

                rx.spacer(),

                # EXPLORA
                rx.vstack(

                    rx.text(
                        "Explora",
                        font_weight="bold",
                        color="#023047",
                        font_size="1.1em",
                    ),

                    rx.link(
                        "Destinos",
                        href="#",
                        color="#5F6C7B",
                        text_decoration="none",
                    ),

                    rx.link(
                        "Ofertas",
                        href="#",
                        color="#5F6C7B",
                        text_decoration="none",
                    ),

                    rx.link(
                        "Experiencias",
                        href="#",
                        color="#5F6C7B",
                        text_decoration="none",
                    ),

                    spacing="2",
                    align_items="start",
                ),

                # COMPAÑÍA
                rx.vstack(

                    rx.text(
                        "Compañía",
                        font_weight="bold",
                        color="#023047",
                        font_size="1.1em",
                    ),

                    rx.link(
                        "Sobre Nosotros",
                        href="#",
                        color="#5F6C7B",
                        text_decoration="none",
                    ),

                    rx.link(
                        "Contacto",
                        href="#",
                        color="#5F6C7B",
                        text_decoration="none",
                    ),

                    rx.link(
                        "Reservaciones",
                        href="#",
                        color="#5F6C7B",
                        text_decoration="none",
                    ),

                    spacing="2",
                    align_items="start",
                ),

                # CONTACTO
                rx.vstack(

                    rx.text(
                        "Contacto",
                        font_weight="bold",
                        color="#023047",
                        font_size="1.1em",
                    ),

                    rx.text(
                        "📍 Santo Domingo, RD",
                        color="#5F6C7B",
                    ),

                    rx.text(
                        "📞 +1 (829) 123-4567",
                        color="#5F6C7B",
                    ),

                    rx.text(
                        "✉️ info@gbparadise.com",
                        color="#5F6C7B",
                    ),

                    spacing="2",
                    align_items="start",
                ),

                width="100%",
                align="start",
                spacing="8",
            ),

            rx.divider(),

            rx.hstack(

                rx.text(
                    "© 2025 GB Paradise. Todos los derechos reservados.",
                    color="#7B8794",
                    font_size="0.9em",
                ),

                rx.spacer(),

                rx.hstack(
                    rx.text(
                        "📘",
                        font_size="1.4em",
                        cursor="pointer",
                    ),
                    rx.text(
                        "📸",
                        font_size="1.4em",
                        cursor="pointer",
                    ),
                    rx.text(
                        "🎵",
                        font_size="1.4em",
                        cursor="pointer",
                    ),
                    rx.text(
                        "▶️",
                        font_size="1.4em",
                        cursor="pointer",
                    ),
                    spacing="3",
                ),

                width="100%",
            ),

            spacing="5",
            width="100%",
        ),

        bg="white",
        border="1px solid rgba(0,180,216,0.08)",
        border_radius="35px",
        box_shadow="0 8px 25px rgba(0,0,0,0.05)",

        width="96%",
        max_width="1700px",

        margin="3em auto",

        padding="3em",
    )