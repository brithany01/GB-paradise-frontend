import reflex as rx

from GB_Paradise_Frontend.Components.navbar import navbar


@rx.page(route="/reservation")
def reservation():
    return rx.box(
        navbar(),

        # Aquí irá todo tu contenido de reservas
        rx.text("Página de Reservas")
    )