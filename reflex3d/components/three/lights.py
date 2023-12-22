from typing import Union

import reflex as rx


class PointLight(rx.Component):
    library = "@react-three/fiber"
    tag = "pointLight"

    position: rx.Var[list[int]]
    color: rx.Var[Union[int, str]]  # hexadecimal color of the light
    intensity: rx.Var[float]  # numeric value of the light's strength
    distance: rx.Var[float]  # maximum range of the light
    decay: rx.Var[float]  # how the light dims with distance

    # Shadow properties
    castShadow: rx.Var[bool]  # whether the light casts shadows
    shadowMapWidth: rx.Var[int]  # width of the shadow map
    shadowMapHeight: rx.Var[int]  # height of the shadow map
    shadowCameraNear: rx.Var[float]  # near plane of the shadow camera
    shadowCameraFar: rx.Var[float]  # far plane of the shadow camera
    shadowCameraFov: rx.Var[float]  # field of view of the shadow camera
    shadowBias: rx.Var[float]  # bias applied to shadows to prevent artefacts
    shadowRadius: rx.Var[float]  # blur radius for shadows


class AmbientLight (rx.Component):
    library = "@react-three/fiber"
    tag = "ambientLight "
