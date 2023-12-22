"""The canvas page."""
from reflex.style import Style

from npc.components.three.cameras import OrthographicCamera
from npc.components.three.canvas import Canvas
from npc.components.three.controls import OrbitControls
from npc.components.three.lights import PointLight, AmbientLight
from npc.components.three.lines import EllipseCurve, CurveModifier
from npc.components.three.loaders import GLTFLoader
from npc.components.three.materials import MeshStandardMaterial
from npc.components.three.mesh import Mesh, SphereGeometry
from npc.components.three.stagings import Center
from npc.components.three.text import Text3D
from npc.states.three import ThreeState
from npc.templates import template

import reflex as rx


@template(route="/canvas", title="Canvas")
def canvas() -> rx.Component:
    """The canvas page.

    Returns:
        The UI for the canvas page.
    """
    my_canvas = Canvas.create
    camera = OrthographicCamera.create
    controls = OrbitControls.create
    mesh = Mesh.create(
        SphereGeometry.create(),
        MeshStandardMaterial.create(color="hotpink"),
        on_click=ThreeState.increment
    )
    text3d = Text3D.create(
        MeshStandardMaterial.create(color="blue"),
        ThreeState.get_text,
        font=ThreeState.get_font
    )
    center = Center.create
    ambient_light = AmbientLight.create()
    point_light = PointLight.create(position=[-1, -1, -1])

    gltf_mesh = GLTFLoader.create(url=ThreeState.get_url)

    return rx.vstack(
        my_canvas(
            camera(
                controls(),  # enablePan=False),
                ambient_light,
                point_light,
                mesh,
                gltf_mesh,
                CurveModifier.create(
                    center(
                        text3d
                    ),
                ),
                EllipseCurve.create()
            ),
            # width="100%",
            # height="100%",
            style=Style(
                {
                    'width': "100%",
                    "height": "70vh"
                }
            )
        ),
        rx.input(
            on_change=ThreeState.set_text,
            placeholder=ThreeState.get_text,
        ),
        rx.select(
            ThreeState.fonts,
            on_change=ThreeState.set_font,
            default_value=ThreeState.fonts[0],
        ),
        rx.select(
            ThreeState.urls,
            on_change=ThreeState.set_url,
            default_value=ThreeState.urls[0],
        )
    )
