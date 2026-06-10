"""GB Paradise App"""

import reflex as rx

from .Pages.home import home
from .Pages.destinations import destinations
from .Pages.offers import offers
from .Pages.experiences import experiences
from .Pages.about import about
from .Pages.contact import contact
from .Pages.reservation import reservation


class State(rx.State):
    """The app state."""
    pass


app = rx.App()

app.add_page(
    home,
    route="/",
    title="GB Paradise"
)

app.add_page(
    destinations,
    route="/destinations",
    title="Destinos | GB Paradise"
)

app.add_page(
    offers,
    route="/offers",
    title="Ofertas | GB Paradise"
)

app.add_page(
    experiences,
    route="/experiences",
    title="Experiencias | GB Paradise"
)

app.add_page(
    about,
    route="/about",
    title="Sobre Nosotros | GB Paradise"
)

app.add_page(
    contact,
    route="/contact",
    title="Contacto | GB Paradise"
)

app.add_page(
    reservation,
    route="/reservation",
    title="Reservas | GB Paradise"
)