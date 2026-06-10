import reflex as rx


def about_cta():

    return rx.center(

        rx.box(

            rx.hstack(

                rx.image(
                    src="/about_cta.png",
                    width="180px",
                    height="110px",
                    object_fit="contain",
                ),

                rx.vstack(

                    rx.heading(
                        "Tu próxima aventura comienza con nosotros",
                        size="7",
                        color="#023047",
                    ),

                    rx.text(
                        "Permítenos ser parte de tus mejores recuerdos.",
                        color="#4A5568",
                    ),

                    align_items="start",
                    spacing="1",
                ),

                rx.spacer(),

                rx.button(
                    "Contáctanos ✈️",
                    bg="#18B7C8",
                    color="white",
                    border_radius="999px",
                    padding="0.8em 2em",
                ),

                rx.text(
                    "➰ ✈️",
                    font_size="2em",
                    color="#18B7C8",
                ),

                align="center",
                width="100%",
            ),

            bg="#EAFBFD",

            padding="1.8em 2.5em",

            border_radius="24px",

            width="85%",

            box_shadow="0 5px 15px rgba(0,0,0,0.06)",
        ),

        width="100%",

        margin_top="2em",
        margin_bottom="3em",
    )