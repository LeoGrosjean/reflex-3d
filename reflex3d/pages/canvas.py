"""The canvas page."""
from reflex.style import Style

from reflex3d.components.three.cameras import OrthographicCamera
from reflex3d.components.three.canvas import Canvas
from reflex3d.components.three.controls import OrbitControls
from reflex3d.components.three.lights import PointLight, AmbientLight
from reflex3d.components.three.lines import EllipseCurve, CurveModifier, CatmullRomCurve, CurveModifierV2
from reflex3d.components.three.loaders import GLTFLoader
from reflex3d.components.three.materials import MeshStandardMaterial
from reflex3d.components.three.mesh import Mesh, SphereGeometry
from reflex3d.components.three.stagings import Center
from reflex3d.components.three.text import Text3D
from reflex3d.javascript.onchange.text import HelloTest
from reflex3d.states.three import ThreeState
from reflex3d.templates import template

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
        font=ThreeState.get_font,
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
                CurveModifierV2.create(
                    center(
                        text3d,
                        cacheKey=ThreeState.get_center_trigger
                    ),
                ),
                center(
                    text3d,
                    cacheKey=ThreeState.get_center_trigger
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
            # default_value=ThreeState.fonts[0],
        ),
        rx.select(
            ThreeState.urls,
            on_change=ThreeState.set_url,
            # default_value=ThreeState.urls[0],
        )
    )
