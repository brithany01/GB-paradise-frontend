import reflex as rx


def contact_form():

    return rx.box(

        rx.vstack(

            rx.heading(
                "Envíanos un mensaje",
                size="6",
                color="#023047",
            ),

            rx.text(
                "Completa el formulario y te contactaremos pronto.",
                color="gray",
                font_size="0.9em",
            ),

            rx.hstack(

                rx.input(
                    placeholder="Nombre completo",
                    width="100%",
                    border_radius="12px",
                ),

                rx.input(
                    placeholder="Correo electrónico",
                    width="100%",
                    border_radius="12px",
                ),

                width="100%",
                spacing="4",
            ),

            rx.hstack(

                rx.input(
                    placeholder="Teléfono",
                    width="100%",
                    border_radius="12px",
                ),

                rx.input(
                    placeholder="Asunto",
                    width="100%",
                    border_radius="12px",
                ),

                width="100%",
                spacing="4",
            ),

            rx.text_area(
                placeholder="Mensaje",
                min_height="140px",
                width="100%",
                border_radius="12px",
            ),

            rx.button(
                "Enviar mensaje ✈",
                bg="#18B7C8",
                color="white",
                border_radius="30px",
                width="220px",
                size="3",
            ),

            rx.text(
                "🔒 Tu información está protegida y solo será utilizada para ayudarte.",
                color="gray",
                font_size="0.8em",
            ),

            width="100%",
            spacing="4",
            align_items="start",
        ),

        bg="white",
        padding="2em",
        border_radius="25px",
        box_shadow="0 6px 18px rgba(0,0,0,0.08)",
        width="100%",
    )