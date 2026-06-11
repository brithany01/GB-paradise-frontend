"""GB Paradise App"""

import reflex as rx

from .Pages.home import home
from .Pages.destinations import destinations
from .Pages.offers import offers
from .Pages.experiences import experiences
from .Pages.about import about
from .Pages.contact import contact
from .Pages.reservation import reservation

# DESTINO PUNTA CANA
from .Pages.destination_pages.punta_cana import punta_cana
from .Pages.destination_pages.jarabacoa import jarabacoa
from .Pages.destination_pages.isla_saona import isla_saona
from .Pages.destination_pages.samana import samana
from .Pages.destination_pages.santo_domingo import santo_domingo
from .Pages.destination_pages.bavaro import bavaro


class State(rx.State):
    """The app state."""
    pass


app = rx.App()

# HOME
app.add_page(
    home,
    route="/",
    title="GB Paradise"
)

# DESTINOS
app.add_page(
    destinations,
    route="/destinations",
    title="Destinos | GB Paradise"
)

# PUNTA CANA (PRUEBA)
app.add_page(
    punta_cana,
    route="/punta-cana",
    title="Punta Cana Paradise | GB Paradise"
)

# OFERTAS
app.add_page(
    offers,
    route="/offers",
    title="Ofertas | GB Paradise"
)

# EXPERIENCIAS
app.add_page(
    experiences,
    route="/experiences",
    title="Experiencias | GB Paradise"
)

# SOBRE NOSOTROS
app.add_page(
    about,
    route="/about",
    title="Sobre Nosotros | GB Paradise"
)

# CONTACTO
app.add_page(
    contact,
    route="/contact",
    title="Contacto | GB Paradise"
)

# RESERVAS
app.add_page(
    reservation,
    route="/reservation",
    title="Reservas | GB Paradise"
)


app.add_page(
    jarabacoa,
    route="/jarabacoa",
    title="Jarabacoa Adventure | GB Paradise"
)

app.add_page(
    isla_saona,
    route="/isla-saona",
    title="Isla Saona Premium | GB Paradise"
)

app.add_page(
    samana,
    route="/samana",
    title="Samaná Experience | GB Paradise"
)

app.add_page(
    santo_domingo,
    route="/santo-domingo",
    title="Santo Domingo Colonial | GB Paradise"
)

app.add_page(
    bavaro,
    route="/bavaro",
    title="Bávaro All Inclusive | GB Paradise"
)