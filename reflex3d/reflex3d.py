"""Welcome to Reflex!."""

from reflex3d import styles

# Import all the pages.
from reflex3d.api.mesh import api_test
from reflex3d.pages import *

import reflex as rx



# Create the app and compile it.
app = rx.App(style=styles.base_style)
app.add_page(canvas, route="/canvas")
app.api.add_api_route("/items/glb", api_test)
app.compile()

