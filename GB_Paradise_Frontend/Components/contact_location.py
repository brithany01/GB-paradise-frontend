import reflex as rx


def contact_location():

    return rx.center(

        rx.box(

            rx.vstack(

                rx.heading(
                    "Nuestra ubicación",
                    font_size="2.6em",
                    font_weight="bold",
                    color="#023047",
                    text_align="center",
                    width="100%",
                ),

                rx.image(
                    src="/contact_map.png",
                    width="100%",
                    border_radius="20px",
                ),

                rx.vstack(

                    rx.text(
                        "Av. Winston Churchill 123",
                        color="#023047",
                        font_weight="bold",
                        font_size="1.3em",
                    ),

                    rx.text(
                        """
                        Plaza Lope de Vega, Local 201
                        Santo Domingo, República Dominicana
                        """,
                        color="gray",
                        font_size="1em",
                    ),

                    align_items="start",
                    spacing="1",
                    width="100%",
                ),

                rx.link(

                    rx.button(
                        "Ver en Google Maps",
                        bg="transparent",
                        color="#18B7C8",
                        border="2px solid #18B7C8",
                        border_radius="30px",
                        width="240px",
                        size="3",
                        _hover={
                            "bg": "#18B7C8",
                            "color": "white",
                        },
                    ),

                    href="https://maps.google.com/?q=Plaza+Lope+de+Vega+Santo+Domingo",
                    is_external=True,
                    text_decoration="none",
                ),

                rx.divider(),

                rx.heading(
                    "Síguenos en redes sociales",
                    size="5",
                    color="#023047",
                    text_align="center",
                    width="100%",
                ),

                rx.hstack(

                    rx.link(
                        rx.text("📘", font_size="2.2em"),
                        href="https://facebook.com",
                        is_external=True,
                    ),

                    rx.link(
                        rx.text("📸", font_size="2.2em"),
                        href="https://instagram.com",
                        is_external=True,
                    ),

                    rx.link(
                        rx.text("🐦", font_size="2.2em"),
                        href="https://x.com",
                        is_external=True,
                    ),

                    rx.link(
                        rx.text("▶️", font_size="2.2em"),
                        href="https://youtube.com",
                        is_external=True,
                    ),

                    rx.link(
                        rx.text("🎵", font_size="2.2em"),
                        href="https://tiktok.com",
                        is_external=True,
                    ),

                    spacing="6",
                    justify="center",
                    width="100%",
                ),

                spacing="5",
                align_items="center",
                width="100%",
            ),

            bg="white",

            padding="3em",

            border_radius="25px",

            box_shadow="0 8px 22px rgba(0,0,0,0.08)",

            width="100%",
            max_width="1600px",
        ),

        width="100%",
        bg="white",
    )