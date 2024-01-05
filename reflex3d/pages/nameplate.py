"""The canvas page."""
from functools import partial

from reflex.style import Style

from reflex3d.components.chakra.inputs import numberinputimproved
from reflex3d.components.three.cameras import OrthographicCamera
from reflex3d.components.three.canvas import Canvas
from reflex3d.components.three.controls import OrbitControls
from reflex3d.components.three.lights import PointLight
from reflex3d.components.three.loaders import LoadGlbBytes

from reflex3d.components.three.modifiers import CurvedText
from reflex3d.components.three.stagings import Center

from reflex3d.states.mesh import NpcState
from reflex3d.templates import template

import reflex as rx

my_canvas = Canvas.create
camera = OrthographicCamera.create
controls = OrbitControls.create
point_light = PointLight.create(position=[0, 70, 25], intensity=20000.)
point_light2 = PointLight.create(position=[0, -10, 25], intensity=500.)

partial_canvas = partial(
    my_canvas,
    controls(enablePan=False, enableZoom=True),
    point_light,
    point_light2,
    orthographic=True,
    camera={
        "position": [0, 125, 300],
        "zoom": 20
    },
    style=Style(
        {
            'width': "100%",
            "height": "70vh",
            "border": "2px solid black",
        }
    )
)
center = Center.create


@template(route="/nameplate", title="Nameplate")
def nameplate() -> rx.Component:
    """The nameplate page.

    Returns:
        The UI for the nameplate page.
    """

    return rx.vstack(
        rx.vstack(
            rx.input(
                on_change=NpcState.set_text,
                placeholder=NpcState.get_text,
            ),
            rx.select(
                NpcState.fonts,
                on_change=NpcState.set_font,
            ),

        ),

        partial_canvas(
            LoadGlbBytes.create(bytes_=NpcState.get_stream_content),
            CurvedText.create(
                text=NpcState.get_text,
                font=NpcState.get_font,
                size=NpcState.get_font_size,
                radius=NpcState.get_radius,
                transpose_x=NpcState.get_transpose_x,
                height=NpcState.get_height
            ),
        ),
        rx.vstack(
            numberinputimproved(
                name="font height",
                on_change=NpcState.set_height,
                default_value=NpcState.height,
                step=0.1
                # default_value=NpcState.fonts[0],
            ),
            numberinputimproved(
                name="font size",
                on_change=NpcState.set_font_size,
                default_value=NpcState.font_size,
                step=0.1
                # default_value=NpcState.fonts[0],
            ),
            numberinputimproved(
                name="move middle text left right",
                on_change=NpcState.set_transpose_x,
                default_value=NpcState.transpose_x,
                type_="range",
                min_=-15,
                max_=15,
                step=0.1,
            ),
        ),
    )
