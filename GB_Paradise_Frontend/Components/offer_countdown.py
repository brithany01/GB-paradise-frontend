import reflex as rx
from datetime import datetime, timedelta


class CountdownState(rx.State):

    # Fecha objetivo (2 días, 14 horas y 25 minutos desde ahora)
    target_date: str = (
        datetime.now() + timedelta(days=2, hours=14, minutes=25)
    ).isoformat()

    @rx.var
    def days(self) -> str:
        diff = datetime.fromisoformat(self.target_date) - datetime.now()
        return f"{max(diff.days, 0):02}"

    @rx.var
    def hours(self) -> str:
        diff = datetime.fromisoformat(self.target_date) - datetime.now()
        hours = max(diff.seconds // 3600, 0)
        return f"{hours:02}"

    @rx.var
    def minutes(self) -> str:
        diff = datetime.fromisoformat(self.target_date) - datetime.now()
        minutes = max((diff.seconds % 3600) // 60, 0)
        return f"{minutes:02}"

    @rx.var
    def seconds(self) -> str:
        diff = datetime.fromisoformat(self.target_date) - datetime.now()
        seconds = max(diff.seconds % 60, 0)
        return f"{seconds:02}"


def countdown_box(number, label):

    return rx.vstack(

        rx.box(
            number,
            bg="#12B3C7",
            color="white",
            font_weight="bold",
            font_size="2em",
            border_radius="14px",
            padding="0.4em",
            width="75px",
            text_align="center",
        ),

        rx.text(
            label,
            color="white",
            font_size="0.85em",
            font_weight="medium",
        ),

        spacing="1",
        align="center",
    )


def offer_countdown():

    return rx.box(

        rx.text(
            "¡La promoción termina en!",
            color="white",
            font_weight="bold",
            font_size="1.15em",
            margin_bottom="0.8em",
            text_align="center",
        ),

        rx.hstack(

            countdown_box(CountdownState.days, "DÍAS"),

            countdown_box(CountdownState.hours, "HORAS"),

            countdown_box(CountdownState.minutes, "MIN"),

            countdown_box(CountdownState.seconds, "SEG"),

            spacing="2",
            justify="center",
        ),

        bg="#023047",
        padding="1.4em",
        border_radius="22px",
        box_shadow="0 10px 25px rgba(0,0,0,0.15)",
        width="340px",
    )