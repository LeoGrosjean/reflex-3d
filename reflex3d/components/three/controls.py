from typing import Callable

import reflex as rx


class OrbitControls(rx.Component):
    library = "@react-three/drei"
    tag = "OrbitControls"

    # Target to orbit around
    target: rx.Var[list[float]]  # The target to orbit around [x, y, z]

    # Zoom and rotate settings
    enableZoom: rx.Var[bool]  # Whether zooming is enabled
    zoomSpeed: rx.Var[float]  # Speed of zooming
    enableRotate: rx.Var[bool]  # Whether rotation is enabled
    rotateSpeed: rx.Var[float]  # Speed of rotation

    # Panning settings
    enablePan: rx.Var[bool]  # Whether panning is enabled
    panSpeed: rx.Var[float]  # Speed of panning
    screenSpacePanning: rx.Var[bool]  # Whether panning uses screen space directions

    # Limits
    minDistance: rx.Var[float]  # Minimum distance for zooming
    maxDistance: rx.Var[float]  # Maximum distance for zooming
    minPolarAngle: rx.Var[float]  # Minimum polar angle for orbiting
    maxPolarAngle: rx.Var[float]  # Maximum polar angle for orbiting

    # Damping (inertia)
    enableDamping: rx.Var[bool]  # Whether to use damping (inertia)
    dampingFactor: rx.Var[float]  # Damping inertia factor

    # Event handlers
    onChange: rx.Var[Callable]  # Function to call when controls change
    onStart: rx.Var[Callable]  # Function to call when interaction starts
    onEnd: rx.Var[Callable]  # Function to call when interaction ends
