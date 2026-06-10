import reflex as rx


def contact_cta():

    return rx.center(

        rx.box(

            rx.hstack(

                rx.vstack(

                    rx.text(
                        "¿Listo para tu próxima aventura?",
                        color="#023047",
                        font_weight="bold",
                        font_size="2.8em",
                        line_height="1.1",
                    ),

                    rx.text(
                        """
                        Permítenos ayudarte a crear recuerdos
                        inolvidables alrededor del mundo.
                        """,
                        color="#023047",
                        max_width="520px",
                        font_size="1.1em",
                        line_height="1.8",
                    ),

                    rx.button(
                        "Comenzar ahora ✈",
                        bg="#0096C7",
                        color="white",
                        border_radius="30px",
                        padding_x="2em",
                        padding_y="0.9em",
                        font_weight="bold",
                        _hover={
                            "bg": "#0077B6",
                        },
                    ),

                    align_items="start",
                    spacing="4",
                ),

                rx.spacer(),

                rx.image(
                    src="/contact_cta.png",
                    width="340px",
                ),

                width="100%",
                align="center",
            ),

            bg="#DFF5FA",

            width="95%",
            max_width="1350px",

            padding="3em 4em",

            border_radius="35px",

            box_shadow="0 10px 25px rgba(0,0,0,0.06)",
        ),

        width="100%",

        margin_top="3em",
        margin_bottom="3em",
    )