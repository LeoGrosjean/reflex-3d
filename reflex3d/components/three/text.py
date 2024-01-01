from typing import Any, Callable

import reflex as rx


class Text3DModel(rx.Base):
    distance: float


class Text3D(rx.Component):
    """
    docs https://drei.pmnd.rs/?path=/docs/abstractions-text3d--docs
    """
    library = "@react-three/drei"
    tag = "Text3D"
    lib_dependencies: list[str] = ["three-stdlib"]

    # Text content
    text: rx.Var[str]  # The text to be displayed

    # Font properties
    font: rx.Var[str]  # Path to the font file (usually a .json or .typeface.json file)
    fontSize: rx.Var[float]  # Size of the text
    lineHeight: rx.Var[float]  # Thickness of the text

    # Position and orientation
    position: rx.Var[list[float]]  # Position of the text in 3D space as [x, y, z]
    rotation: rx.Var[list[float]]  # Rotation of the text as Euler angles [x, y, z]

    # Text styling
    curveSegments: rx.Var[int]  # Number of segments for curved letters
    bevelEnabled: rx.Var[bool]  # Whether bevel is enabled for the text
    bevelThickness: rx.Var[float]  # Thickness of the bevel
    bevelSize: rx.Var[float]  # Size of the bevel
    lineHeight: rx.Var[float]  # Line height in Three.js units, default is 0
    letterSpacing: rx.Var[float]  # Letter spacing factor, default is 1
    smooth: rx.Var[float]  # Tolerance level for merging vertices and computing normals

    # Material
    material: rx.Var[Any]  # Material to apply to the text (could be a Three.js material)

    # Event handlers
    onClick: rx.Var[Callable]  # Function to call on text click
    onPointerOver: rx.Var[Callable]  # Function to call when a pointer hovers over the text
    onPointerOut: rx.Var[Callable]  # Function to call when a pointer leaves the text

    rotateY: rx.Var[dict]