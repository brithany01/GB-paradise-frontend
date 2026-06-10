import reflex as rx


def experience_card(exp):

    return rx.box(

        rx.image(
            src=exp["image"],
            width="100%",
            height="140px",
            object_fit="cover",
        ),

        rx.vstack(

            rx.text(
                exp["title"],
                font_weight="bold",
                color="#023047",
                font_size="0.95em",
            ),

            rx.text(
                exp["location"],
                color="gray",
                font_size="0.8em",
            ),

            rx.text(
                exp["price"],
                color="#18B7C8",
                font_weight="bold",
                font_size="1.15em",
            ),

            align_items="start",
            spacing="1",
            padding="0.8em",
        ),

        bg="white",

        border_radius="18px",

        overflow="hidden",

        width="220px",

        box_shadow="0 5px 15px rgba(0,0,0,0.08)",

        transition="all 0.2s ease",

        _hover={
            "transform": "translateY(-5px)",
            "box_shadow": "0 10px 25px rgba(0,0,0,0.12)",
        },
    )