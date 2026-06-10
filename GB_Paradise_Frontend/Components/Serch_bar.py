import reflex as rx


def search_bar():
    return rx.hstack(

        # Destino
        rx.vstack(
            rx.text(
                "📍 ¿A dónde quieres ir?",
                font_weight="600",
                color="#023047",
            ),
            rx.text(
                "Escribe tu destino",
                color="#64748B",
                font_size="0.9em",
            ),
            align_items="start",
            spacing="1",
        ),

        rx.divider(orientation="vertical", height="50px"),

        # Fecha inicio
        rx.vstack(
            rx.text(
                "📅 Fecha de inicio",
                font_weight="600",
                color="#023047",
            ),
            rx.text(
                "Selecciona fecha",
                color="#64748B",
                font_size="0.9em",
            ),
            align_items="start",
            spacing="1",
        ),

        rx.divider(orientation="vertical", height="50px"),

        # Fecha fin
        rx.vstack(
            rx.text(
                "📅 Fecha de fin",
                font_weight="600",
                color="#023047",
            ),
            rx.text(
                "Selecciona fecha",
                color="#64748B",
                font_size="0.9em",
            ),
            align_items="start",
            spacing="1",
        ),

        rx.divider(orientation="vertical", height="50px"),

        # Personas
        rx.vstack(
            rx.text(
                "👤 Personas",
                font_weight="600",
                color="#023047",
            ),
            rx.text(
                "1 persona",
                color="#64748B",
                font_size="0.9em",
            ),
            align_items="start",
            spacing="1",
        ),

        rx.spacer(),

        rx.button(
            "🔍 Buscar",
            bg="#FFB703",
            color="white",
            border_radius="25px",
            padding_x="2em",
            size="3",
        ),

        width="100%",
        max_width="1050px",
        bg="white",
        padding="1.5em 2em",
        border_radius="40px",
        box_shadow="0 8px 25px rgba(0,0,0,0.10)",
        align="center",
    )