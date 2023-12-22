import reflex as rx
from typing import Callable, Union, Any

from reflex3d.typings.three import Vector3, Euler, Quaternion, Matrix4


class Center(rx.Component):
    """
    docs : https://drei.pmnd.rs/?path=/docs/staging-center--docs
    """
    library = "@react-three/drei"
    tag = "Center"
    alias = "CenterThree"
    # Transformation properties
    position: rx.Var[Vector3]
    up: rx.Var[Vector3]
    scale: rx.Var[Vector3]
    rotation: rx.Var[Euler]
    quaternion: rx.Var[Quaternion]
    matrix: rx.Var[Matrix4]

    # Other properties
    visible: rx.Var[bool]  # Visibility
    castShadow: rx.Var[bool]  # Casts shadow
    receiveShadow: rx.Var[bool]  # Receives shadow
    userData: rx.Var[dict] # Custom user data
    raycast: rx.Var[Callable]  # Custom raycasting function

    # Event handlers
    onClick: rx.Var[Callable]  # Click event handler
    onPointerOver: rx.Var[Callable]  # Pointer over event handler
    onPointerOut: rx.Var[Callable]  # Pointer out event handler
    # ... other event handlers ...

    # Centering specific properties
    disableX: rx.Var[bool]  # Disable centering along X-axis
    disableY: rx.Var[bool]  # Disable centering along Y-axis
    disableZ: rx.Var[bool]  # Disable centering along Z-axis
    precise: rx.Var[bool]  # Precise centering control
    onCentered: rx.Var[Callable]  # Callback after centering
    cacheKey: rx.Var[Any]  # Cache key for recalculations
