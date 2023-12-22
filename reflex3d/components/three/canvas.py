from typing import Union, Callable

import reflex as rx


class Canvas(rx.Component):
    library = "@react-three/fiber"
    tag = "Canvas"

    # Canvas size
    width: rx.Var[Union[int, str]]  # Width of the canvas (can be in pixels or percentage)
    height: rx.Var[Union[int, str]]  # Height of the canvas (can be in pixels or percentage)

    # Camera properties
    cameraFov: rx.Var[float]  # Field of view for the camera
    cameraAspect: rx.Var[float]  # Aspect ratio of the camera
    cameraNear: rx.Var[float]  # Near clipping plane
    cameraFar: rx.Var[float]  # Far clipping plane
    cameraPosition: rx.Var[list[float]]  # Camera position as [x, y, z]

    # Rendering options
    antialias: rx.Var[bool]  # Whether to perform antialiasing
    alpha: rx.Var[bool]  # Whether the canvas contains an alpha (transparency) buffer
    pixelRatio: rx.Var[float]  # The pixel ratio to be used by the renderer

    # Scene properties
    backgroundColor: rx.Var[Union[int, str]]  # Background color of the scene

    # Performance optimizations
    shadows: rx.Var[bool]  # Whether to render shadows
    dpr: rx.Var[Union[float, list[float]]]  # Device pixel ratio for performance optimization

    # Event handlers
    onClick: rx.Var[Callable]  # Function to call on canvas click
    onPointerMove: rx.Var[Callable]  # Function to call on pointer move over the canvas
