import reflex as rx


def offer_card(offer):

    return rx.link(

        rx.box(

            rx.box(

                rx.image(
                    src=offer["image"],
                    width="100%",
                    height="170px",
                    object_fit="cover",
                ),

                rx.badge(
                    offer["discount"],
                    color_scheme="orange",
                    position="absolute",
                    top="10px",
                    left="10px",
                    border_radius="20px",
                    padding="0.4em 0.8em",
                ),

                position="relative",
            ),

            rx.vstack(

                rx.text(
                    offer["title"],
                    font_weight="bold",
                    color="#023047",
                ),

                rx.text(
                    offer["description"],
                    color="gray",
                    font_size="0.9em",
                ),

                rx.hstack(

                    rx.text(
                        f"ANTES {offer['old_price']}",
                        text_decoration="line-through",
                        color="gray",
                        font_size="0.8em",
                    ),

                    rx.spacer(),

                    rx.text(
                        f"⭐ {offer['rating']}",
                        color="#023047",
                    ),

                    width="100%",
                ),

                rx.text(
                    f"AHORA {offer['price']}",
                    color="#00B4D8",
                    font_weight="bold",
                    font_size="1.1em",
                ),

                rx.button(
                    "Ver oferta",
                    width="100%",
                    bg="#12B3C7",
                    color="white",
                    border_radius="20px",
                ),

                align_items="start",
                spacing="2",
                padding="1em",
            ),

            bg="white",
            border_radius="20px",
            overflow="hidden",
            width="100%",
            max_width="320px",

            box_shadow="0 4px 15px rgba(0,0,0,0.08)",
        ),

        href=offer["route"],
        text_decoration="none",
    )