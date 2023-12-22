from typing import Callable, Union

import reflex as rx


class OrthographicCamera(rx.Component):
    library = "@react-three/drei"
    tag = "OrthographicCamera"

    # Camera frustum properties
    left: rx.Var[float]  # Camera frustum left plane
    right: rx.Var[float]  # Camera frustum right plane
    top: rx.Var[float]  # Camera frustum top plane
    bottom: rx.Var[float]  # Camera frustum bottom plane
    near: rx.Var[float]  # Camera frustum near plane
    far: rx.Var[float]  # Camera frustum far plane

    # Transformation properties
    position: rx.Var[list[float]]  # Position of the camera in 3D space as [x, y, z]
    rotation: rx.Var[list[float]]  # Rotation of the camera as Euler angles [x, y, z]
    lookAt: rx.Var[Union[list[float], None]]  # The point to look at [x, y, z]

    # Camera properties
    zoom: rx.Var[float]  # Zoom factor of the camera
    aspect: rx.Var[float]  # Aspect ratio of the camera

    # Event handlers
    onClick: rx.Var[Callable]  # Function to call on camera click
    onPointerMove: rx.Var[Callable]  # Function to call on pointer move over the camera
