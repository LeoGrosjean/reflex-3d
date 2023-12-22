from typing import Union, Any, Callable, List

import reflex as rx


class MeshOnClick(rx.Base):
    distance: float
    intersections: List[Any]


class Mesh(rx.Component):
    library = "@react-three/fiber"
    tag = "mesh"

    # Transformation properties
    position: rx.Var[list[float]]  # Position of the mesh in 3D space as [x, y, z]
    rotation: rx.Var[list[float]]  # Rotation of the mesh as Euler angles [x, y, z]
    scale: rx.Var[Union[float, list[float]]]  # Scale of the mesh, either uniform or as [x, y, z]

    # Material properties
    material: rx.Var[Any]  # Material to apply to the mesh (could be a Three.js material)

    # Geometry properties
    geometry: rx.Var[Any]  # Geometry of the mesh (could be a Three.js geometry)

    # Rendering properties
    castShadow: rx.Var[bool]  # Whether the mesh casts a shadow
    receiveShadow: rx.Var[bool]  # Whether the mesh receives shadows

    # Advanced properties
    visible: rx.Var[bool]  # Whether the mesh is visible
    userData: rx.Var[dict]  # Custom user data to store in the mesh
    on_click: rx.Var[Callable]  # Function to call on mesh click
    onPointerOver: rx.Var[Callable]  # Function to call when a pointer hovers over the mesh
    onPointerOut: rx.Var[Callable]  # Function to call when a pointer leaves the mesh

    def get_event_triggers(self) -> dict[str, Any]:

        def on_click_signature(data: MeshOnClick):
            return [
                data.distance,
                data.intersections
            ]

        return {
            **super().get_event_triggers(),
            "on_click": on_click_signature,
        }


class SphereGeometry(rx.Component):
    library = "@react-three/fiber"
    tag = "sphereGeometry"
