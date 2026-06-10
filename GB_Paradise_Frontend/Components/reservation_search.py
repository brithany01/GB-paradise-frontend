import reflex as rx


class ReservationState(rx.State):

    selected_tab: str = "packages"

    def show_packages(self):
        self.selected_tab = "packages"

    def show_hotels(self):
        self.selected_tab = "hotels"


def packages_form():

    return rx.hstack(

        rx.input(
            placeholder="¿A dónde quieres ir?",
            width="260px",
        ),

        rx.input(
            placeholder="Fecha de inicio",
            width="200px",
        ),

        rx.input(
            placeholder="Fecha de fin",
            width="200px",
        ),

        rx.select(
            ["1 persona", "2 personas", "3 personas", "4 personas"],
            placeholder="Personas",
            width="180px",
        ),

        rx.button(
            "🔍 Buscar disponibilidad",
            bg="#FFB703",
            color="white",
            width="260px",
            border_radius="12px",
        ),

        spacing="4",
        width="100%",
        justify="center",
    )


def hotels_form():

    return rx.vstack(

        rx.hstack(

            rx.input(
                placeholder="¿Dónde quieres hospedarte?",
                width="260px",
            ),

            rx.input(
                placeholder="Check-in",
                width="220px",
            ),

            rx.input(
                placeholder="Check-out",
                width="220px",
            ),

            rx.select(
                ["1 habitación", "2 habitaciones", "3 habitaciones"],
                placeholder="Habitaciones",
                width="180px",
            ),

            spacing="4",
        ),

        rx.hstack(

            rx.select(
                [
                    "1 adulto",
                    "2 adultos",
                    "3 adultos",
                    "4 adultos",
                ],
                placeholder="Huéspedes",
                width="260px",
            ),

            rx.button(
                "🔍 Buscar hoteles",
                bg="#FFB703",
                color="white",
                width="365px",
                border_radius="12px",
            ),

            spacing="4",
        ),

        spacing="4",
        width="100%",
        align_items="center",
    )


def reservation_search():

    return rx.box(

        rx.vstack(

            # TABS
            rx.hstack(

                rx.button(
                    "📦 Paquetes",
                    on_click=ReservationState.show_packages,
                    variant="ghost",
                    color=rx.cond(
                        ReservationState.selected_tab == "packages",
                        "#18B7C8",
                        "#023047",
                    ),
                    font_weight="bold",
                ),

                rx.button(
                    "🏨 Hoteles",
                    on_click=ReservationState.show_hotels,
                    variant="ghost",
                    color=rx.cond(
                        ReservationState.selected_tab == "hotels",
                        "#18B7C8",
                        "#023047",
                    ),
                    font_weight="bold",
                ),

                spacing="6",
                justify="center",
            ),

            rx.cond(
                ReservationState.selected_tab == "packages",
                packages_form(),
                hotels_form(),
            ),

            spacing="6",
            width="100%",
        ),

        bg="white",
        border_radius="28px",
        padding="2em",
        box_shadow="0 10px 30px rgba(0,0,0,0.08)",

        width="100%",
        max_width="1300px",

        # MÁS PEGADO AL HERO
        margin_top="-120px",

        margin_left="auto",
        margin_right="auto",

        position="relative",
        z_index="50",
    )