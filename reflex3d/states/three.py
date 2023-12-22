from typing import List

import reflex as rx

from reflex3d.components.three.mesh import MeshOnClick


class ThreeState(rx.State):
    clicked: bool
    count: int = 0

    text: str = "Lt. Testimus le Grand"

    fonts: List[str] = ["/fonts/Inter_Bold.json", "/fonts/Roboto_Regular.json", "/fonts/Android_Android.json"]
    font: str = "/fonts/Inter_Bold.json"

    urls: List[str] = ["/gltf/BoxAnimated.gltf", "/gltf/Poimandres.gltf", "https://vazxmixjsiawhamofees.supabase.co/storage/v1/object/public/models/low-poly-spaceship/model.gltf"]
    url: str = "/gltf/BoxAnimated.gltf"

    def increment(self, distance: MeshOnClick, intersections: MeshOnClick):
        print(distance)
        print(intersections)
        self.count += 1
        print(self.count)

    @rx.var
    def get_text(self) -> str:
        return self.text

    @rx.var
    def get_font(self) -> str:
        return self.font

    @rx.var
    def get_url(self) -> str:
        return self.url