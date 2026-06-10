import reflex as rx
from datetime import datetime, timedelta


class CountdownState(rx.State):

    target_date: str = (
        datetime.now() + timedelta(days=2, hours=14, minutes=25)
    ).isoformat()

    current_time: str = datetime.now().isoformat()

    @rx.event
    def tick(self):
        self.current_time = datetime.now().isoformat()

    @rx.var
    def days(self) -> str:
        diff = (
            datetime.fromisoformat(self.target_date)
            - datetime.fromisoformat(self.current_time)
        )

        total = max(int(diff.total_seconds()), 0)

        return f"{total // 86400:02}"

    @rx.var
    def hours(self) -> str:
        diff = (
            datetime.fromisoformat(self.target_date)
            - datetime.fromisoformat(self.current_time)
        )

        total = max(int(diff.total_seconds()), 0)

        return f"{(total % 86400) // 3600:02}"

    @rx.var
    def minutes(self) -> str:
        diff = (
            datetime.fromisoformat(self.target_date)
            - datetime.fromisoformat(self.current_time)
        )

        total = max(int(diff.total_seconds()), 0)

        return f"{(total % 3600) // 60:02}"

    @rx.var
    def seconds(self) -> str:
        diff = (
            datetime.fromisoformat(self.target_date)
            - datetime.fromisoformat(self.current_time)
        )

        total = max(int(diff.total_seconds()), 0)

        return f"{total % 60:02}"


def countdown_box(number, label):

    return rx.vstack(

        rx.box(
            number,
            bg="#12B3C7",
            color="white",
            font_weight="bold",
            font_size="1.5em",
            border_radius="12px",
            padding="0.3em",
            width="52px",
            text_align="center",
        ),

        rx.text(
            label,
            color="white",
            font_size="0.75em",
            font_weight="medium",
        ),

        spacing="1",
        align="center",
    )


def offer_countdown():

    return rx.box(

        # Actualiza cada segundo
        rx.moment(
            interval=1000,
            on_change=CountdownState.tick,
        ),

        rx.text(
            "¡La promoción termina en!",
            color="white",
            font_weight="bold",
            font_size="1em",
            margin_bottom="0.6em",
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
        padding="1em",
        border_radius="20px",
        box_shadow="0 10px 25px rgba(0,0,0,0.15)",
        width="250px",
    )