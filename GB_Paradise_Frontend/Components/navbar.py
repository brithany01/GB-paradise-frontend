import reflex as rx


def navbar():
    return rx.center(

        rx.box(

            rx.hstack(

                # Logo
                rx.image(
                    src="/logo.png",
                    height="70px",
                    width="auto",
                ),

                rx.spacer(),

                # Menú
                rx.hstack(

                    rx.link(
                        "🏠 Inicio",
                        href="/",
                        color="#00B4D8",
                        font_weight="600",
                        text_decoration="none",
                        white_space="nowrap",
                    ),

                    rx.link(
                        "📍 Destinos",
                        href="/destinations",
                        color="#023047",
                        text_decoration="none",
                        white_space="nowrap",
                    ),

                    rx.link(
                        "🎟️ Ofertas",
                        href="/offers",
                        color="#023047",
                        text_decoration="none",
                        white_space="nowrap",
                    ),

                    rx.link(
                        "⚙️ Experiencias",
                        href="/experiences",
                        color="#023047",
                        text_decoration="none",
                        white_space="nowrap",
                    ),

                    rx.link(
                        "🎯 Sobre Nosotros",
                        href="/about",
                        color="#023047",
                        text_decoration="none",
                        white_space="nowrap",
                    ),

                    rx.link(
                        "📞 Contacto",
                        href="/contact",
                        color="#023047",
                        text_decoration="none",
                        white_space="nowrap",
                    ),

                    spacing="3",
                ),

                rx.spacer(),

                # Botón Reservar
                rx.link(

                    rx.button(
                        "✈️ Reservar ahora",
                        bg="#FFC857",
                        color="white",
                        border_radius="14px",
                        padding_x="1.4em",
                        padding_y="0.6em",
                        cursor="pointer",
                        _hover={
                            "bg": "#F4B400",
                        },
                    ),

                    href="/reservation",
                    text_decoration="none",
                ),

                width="100%",
                align="center",
            ),

            bg="white",
            width="96%",
            max_width="1700px",
            padding="0.4em 2em",
            border_radius="24px",
            box_shadow="0 6px 18px rgba(0,0,0,0.08)",

            position="fixed",
            top="10px",
            left="50%",
            transform="translateX(-50%)",
            z_index="9999",
        ),

        width="100%",
        padding_top="0.5em",
    )