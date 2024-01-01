"""The canvas page."""
from functools import partial
from math import pi

from reflex.style import Style

from reflex3d.components.three.cameras import OrthographicCamera
from reflex3d.components.three.canvas import Canvas
from reflex3d.components.three.controls import OrbitControls
from reflex3d.components.three.lights import PointLight, AmbientLight
from reflex3d.components.three.lines import EllipseCurve, CurveModifier, CatmullRomCurve, CurveModifierV2
from reflex3d.components.three.loaders import GLTFLoader
from reflex3d.components.three.materials import MeshStandardMaterial
from reflex3d.components.three.mesh import Mesh, SphereGeometry
from reflex3d.components.three.modifiers import CurvedText
from reflex3d.components.three.stagings import Center
from reflex3d.components.three.text import Text3D
from reflex3d.javascript.onchange.text import HelloTest
from reflex3d.states.three import ThreeState
from reflex3d.templates import template

import reflex as rx

my_canvas = Canvas.create
camera = OrthographicCamera.create
controls = OrbitControls.create
ambient_light = AmbientLight.create()
point_light = PointLight.create(position=[-1, -1, -1])

partial_canvas = partial(
    my_canvas,
    camera(
        controls(),  # enablePan=False),
        ambient_light,
    ),
    style=Style(
        {
            'width': "100%",
            "height": "70vh",
            "border": "2px solid black",
        }
    )
)
center = Center.create


@template(route="/canvas", title="Canvas")
def canvas() -> rx.Component:
    """The canvas page.

    Returns:
        The UI for the canvas page.
    """

    mesh = Mesh.create(
        SphereGeometry.create(),
        MeshStandardMaterial.create(color="hotpink"),
        on_click=ThreeState.increment
    )
    text3d = Text3D.create(
        MeshStandardMaterial.create(color="Aqua"),
        ThreeState.get_text,
        font=ThreeState.get_font,
        rotateY={'angle': pi},
    )

    gltf_mesh = GLTFLoader.create(url=ThreeState.get_url)

    return rx.vstack(
        rx.heading("Render a sphere mesh with point light"),
        rx.text("Click on the sphere !"),
        rx.hstack(
            rx.vstack(
                rx.hstack(
                    rx.text("Count"),
                    rx.code_block(f"{ThreeState.get_count}")
                ),
                rx.hstack(
                    rx.text("Camera distance from mesh"),
                    rx.code_block(f"{ThreeState.get_distance}")
                ),
                rx.hstack(
                    rx.text("Intersections"),
                    rx.code_block(
                        f"{ThreeState.get_intersections[:80]} "
                        f"..."
                        f" {ThreeState.get_intersections[-80:]}",
                        wrap_long_lines=True
                    )
                ),
                style=Style(
                    {
                        'width': "50%",
                    }
                )
            ),
            partial_canvas(
                mesh,
                point_light,
            ),
        ),
        rx.spacer(),
        rx.heading('Load dynamic gltf'),

        partial_canvas(
            gltf_mesh,
        ),
        rx.select(
            ThreeState.urls,
            on_change=ThreeState.set_url,
            name="Select Gltf"
            # default_value=ThreeState.urls[0],
        ),

        rx.spacer(),
        rx.heading('Edit Text and Font with dynamic recenter'),

        partial_canvas(
            center(
                text3d,
                cacheKey=ThreeState.get_center_trigger
            ),
        ),
        rx.vstack(
            rx.input(
                on_change=ThreeState.set_text,
                placeholder=ThreeState.get_text,
            ),
            rx.select(
                ThreeState.fonts,
                on_change=ThreeState.set_font,
                # default_value=ThreeState.fonts[0],
            ),

        ),
        rx.spacer(),
        rx.heading('Curve Text based on Ellipse'),

        partial_canvas(
            CurveModifierV2.create(
                text3d,
            ),

            CurvedText.create(
                text=ThreeState.get_text,
                font=ThreeState.get_font,
                radius=ThreeState.get_radius,
                transpose_x=ThreeState.get_transpose_x,
            ),
            EllipseCurve.create()
        ),
        rx.vstack(
            rx.number_input(
                on_change=ThreeState.set_radius,
                default_value=ThreeState.radius
                # default_value=ThreeState.fonts[0],
            ),
            rx.slider(
                on_change=ThreeState.set_transpose_x,
                default_value=ThreeState.transpose_x,
                type_="range",
                min_=-10,
                max_=10,
                step=0.2,
            ),
        ),

    )
