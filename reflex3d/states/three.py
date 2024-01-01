from numbers import Number
from typing import List

import reflex as rx

from reflex3d.components.three.mesh import MeshOnClick


class ThreeState(rx.State):
    clicked: bool
    count: int = 0

    text: str = "Edit me !"

    fonts: List[str] = [
        "/fonts/Inter_Bold.json",
        "/fonts/Roboto_Regular.json",
        "/fonts/Android_Android.json"
    ]
    font: str = "/fonts/Inter_Bold.json"

    urls: List[str] = [
        "/gltf/BoxAnimated.gltf",
        "/gltf/Poimandres.gltf",
        "https://vazxmixjsiawhamofees.supabase.co/storage/v1/object/public/models/low-poly-spaceship/model.gltf",
        "/gltf/test2.glb"]
    url: str = "/gltf/BoxAnimated.gltf"

    center_trigger: str

    radius: float = 3.

    distance: float

    intersections: List = ["Not clicked yet"]

    transpose_x: float = 0.

    def increment(self, distance: MeshOnClick, intersections: MeshOnClick):
        self.distance = distance
        self.intersections = intersections
        self.count += 1

    @rx.var
    def get_distance(self) -> float:
        return self.distance

    @rx.var
    def get_intersections(self) -> str:
        return str(self.intersections[0])

    @rx.var
    def get_count(self) -> str:
        return self.count

    @rx.var
    def get_center_trigger(self) -> str:
        return self.center_trigger

    @rx.var
    def get_text(self) -> str:
        return self.text

    def set_text(self, value: str):
        self.set_center_trigger(value + self.font)
        self.text = value

    @rx.var
    def get_font(self) -> str:
        return self.font

    def set_font(self, value: str):
        self.set_center_trigger(self.text + value)
        self.font = value

    @rx.var
    def get_url(self) -> str:
        return self.url

    @rx.var
    def get_radius(self) -> float:
        return self.radius

    @rx.var
    def get_transpose_x(self) -> float:
        print(self.transpose_x)
        return self.transpose_x
