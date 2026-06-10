import reflex as rx


def experience_search():

    return rx.center(

        rx.box(

            rx.hstack(

                rx.input(
                    placeholder="¿Qué experiencia buscas?",
                    width="280px",
                    size="3",
                ),

                rx.select(
                    ["Todos los destinos", "Punta Cana", "Samaná", "Puerto Plata"],
                    placeholder="Destino",
                    width="180px",
                ),

                rx.input(
                    type="date",
                    width="180px",
                ),

                rx.select(
                    ["1 persona", "2 personas", "3 personas", "4+ personas"],
                    placeholder="Personas",
                    width="180px",
                ),

                rx.button(
                    "🔍 Buscar experiencias",
                    bg="#FDBA21",
                    color="white",
                    size="3",
                    border_radius="14px",
                    padding_x="1.4em",
                ),

                spacing="2",
                align="center",
                justify="center",
            ),

            bg="white",
            padding="1.5em",
            border_radius="24px",
            box_shadow="0 8px 20px rgba(0,0,0,0.08)",
        ),

        width="100%",

        margin_top="-35px",

        position="relative",
        z_index="200",
    )