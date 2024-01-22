import base64
from typing import List
import reflex as rx
import trimesh

from reflex3d.api.mesh import create_bent_text_trimesh
from reflex3d.mesh import PROPS, rotate

BASE_0 = {'mesh': rotate(trimesh.load("reflex3d/mesh/base/necromundus.stl")), "metadata": ["necromundus"]}
BASE_1 = {'mesh': rotate(trimesh.load("reflex3d/mesh/base/text style 1 -  Arrow deco.stl")), "metadata": [""]}
BASE_2 = {'mesh': rotate(trimesh.load("reflex3d/mesh/base/text style 1 -  rounded deco.stl")), "metadata": []}
BASE_3 = {'mesh': rotate(trimesh.load("reflex3d/mesh/base/text style 1 - Castle.stl")), "metadata": []}
BASE_4 = {'mesh': rotate(trimesh.load("reflex3d/mesh/base/Text style 1 - D20.stl")), "metadata": []}
BASE_5 = {'mesh': rotate(trimesh.load("reflex3d/mesh/base/Text style 1 - Jewel.stl")), "metadata": []}
BASE_6 = {'mesh': rotate(trimesh.load("reflex3d/mesh/base/text style 1 - sign deco.stl")), "metadata": []}
BASE_7 = {'mesh': rotate(trimesh.load("reflex3d/mesh/base/Text style 1 - standard large rounded target 1.stl")), "metadata": []}
BASE_8 = {'mesh': rotate(trimesh.load("reflex3d/mesh/base/Text style 1 - standard large rounded target 2.stl")), "metadata": []}
BASE_9 = {'mesh': rotate(trimesh.load("reflex3d/mesh/base/Text style 1 - standard large rounded title 1.stl")), "metadata": []}
BASE_10 = {'mesh': rotate(trimesh.load("reflex3d/mesh/base/Text style 1 - standard large rounded title 2.stl")), "metadata": []}
BASE_11 = {'mesh': rotate(trimesh.load("reflex3d/mesh/base/Text style 1 - standard large rounded.stl")), "metadata": []}
BASE_12 = {'mesh': rotate(trimesh.load("reflex3d/mesh/base/Text style 1 - standard large title 1.stl")), "metadata": []}
BASE_13 = {'mesh': rotate(trimesh.load("reflex3d/mesh/base/Text style 1 - standard large title 2.stl")), "metadata": []}
BASE_14 = {'mesh': rotate(trimesh.load("reflex3d/mesh/base/Text style 1 - standard large.stl")), "metadata": []}
BASE_15 = {'mesh': rotate(trimesh.load("reflex3d/mesh/base/Text style 1 - standard narrow title 1.stl")), "metadata": []}
BASE_16 = {'mesh': rotate(trimesh.load("reflex3d/mesh/base/Text style 1 - standard narrow title 2.stl")), "metadata": []}
BASE_17 = {'mesh': rotate(trimesh.load("reflex3d/mesh/base/Text style 1 - standard narrow.stl")), "metadata": []}
BASE_18 = {'mesh': rotate(trimesh.load("reflex3d/mesh/base/Text style 2 -  Banner.stl")), "metadata": []}
BASE_19 = {'mesh': rotate(trimesh.load("reflex3d/mesh/base/text style 2 -  Underlined .stl")), "metadata": []}
BASE_20 = {'mesh': rotate(trimesh.load("reflex3d/mesh/base/text style 3 -  Arrow.stl")), "metadata": []}
BASE_21 = {'mesh': rotate(trimesh.load("reflex3d/mesh/base/text style 3 -  sign flat.stl")), "metadata": []}
BASE_22 = {'mesh': rotate(trimesh.load("reflex3d/mesh/base/text style 3 -  Title style 1.stl")), "metadata": []}
BASE_23 = {'mesh': rotate(trimesh.load("reflex3d/mesh/base/text style 3 -  Title style 2.stl")), "metadata": []}
BASE_24 = {'mesh': rotate(trimesh.load("reflex3d/mesh/base/text style 3 - simple.stl")), "metadata": []}

BASES = {
    "Text Style 1 -  Arrow Deco": BASE_1,
    "Text Style 1 -  Rounded Deco": BASE_2,
    "Text Style 1 - Castle": BASE_3,
    "Text Style 1 - D20": BASE_4,
    "Text Style 1 - Jewel": BASE_5,
    "Text Style 1 - Sign Deco": BASE_6,
    "Text Style 1 - Standard Large Rounded Target 1": BASE_7,
    "Text Style 1 - Standard Large Rounded Target 2": BASE_8,
    "Text Style 1 - Standard Large Rounded Title 1": BASE_9,
    "Text Style 1 - Standard Large Rounded Title 2": BASE_10,
    "Text Style 1 - Standard Large Rounded": BASE_11,
    "Text Style 1 - Standard Large Title 1": BASE_12,
    "Text Style 1 - Standard Large Title 2": BASE_13,
    "Text Style 1 - Standard Large": BASE_14,
    "Text Style 1 - Standard Narrow Title 1": BASE_15,
    "Text Style 1 - Standard Narrow Title 2": BASE_16,
    "Text Style 1 - Standard Narrow": BASE_17,
    "Text Style 2 -  Banner": BASE_18,
    "Text Style 2 -  Underlined ": BASE_19,
    "Text Style 3 -  Arrow": BASE_20,
    "Text Style 3 -  Sign Flat": BASE_21,
    "Text Style 3 -  Title Style 1": BASE_22,
    "Text Style 3 -  Title Style 2": BASE_23,
    "Text Style 3 - Simple": BASE_24,
    "Necromundus": BASE_0,
}


def init_mesh():
    mesh = BASE_1.get('mesh').copy()

    mutable_data = bytearray(mesh.export(file_type='glb'))
    mutable_data[0] = 0x01
    mutable_data[1] = 0x02
    mutable_data[2] = 0x03
    mutable_data[3] = 0x04
    base64_encoded_data = base64.b64encode(mutable_data)

    return base64_encoded_data.decode('utf-8')


class NpcState(rx.State):
    text: str = "Edit me !"

    fonts: List[str] = [
        "/fonts/Inter_Bold.json",
        "/fonts/Roboto_Regular.json",
        "/fonts/Android_Android.json"
    ]
    font: str = "/fonts/Inter_Bold.json"

    font_size: float = 2.5

    center_trigger: str

    radius: float = 21.5

    transpose_x: float = 0.
    transpose_y: float = 0.

    height: float = 1.1

    options: List[str] = list(PROPS.keys())
    option: List[str] = []

    stream_content: str = init_mesh()
    stream_content_dl: str = ""

    meshes: List[str] = list(BASES.keys())
    meshe: str = "Text Style 1 -  Arrow Deco"

    def set_option(self, value: str):
        self.stream_content_dl = ""
        if value in self.option:
            self.option.remove(value)
        else:
            self.option.append(value)
        self.stream_content = self.generate_mesh()

    @rx.var
    def get_height(self) -> float:
        return self.height

    @rx.var
    def get_center_trigger(self) -> str:
        return self.center_trigger

    @rx.var
    def get_radius(self) -> float:
        return self.radius

    @rx.var
    def get_text(self) -> str:
        return self.text

    def set_text(self, value: str):
        self.stream_content_dl = ""
        self.set_center_trigger(value + self.font)
        self.text = value

    @rx.var
    def get_font(self) -> str:
        return self.font

    @rx.var
    def get_font_size(self) -> float:
        return self.font_size

    def set_font(self, value: str):
        self.stream_content_dl = ""
        self.set_center_trigger(self.text + value)
        self.font = value

    @rx.var
    def get_transpose_x(self) -> float:
        return self.transpose_x

    @rx.var
    def get_transpose_y(self) -> float:
        return self.transpose_y

    @rx.cached_var
    def get_stream_content(self) -> str:
        return self.stream_content

    @rx.cached_var
    def get_stream_content_dl(self) -> str:
        return self.stream_content_dl

    @rx.var
    def get_mesh(self) -> str:
        return self.meshe

    def set_mesh(self, value: str):
        self.stream_content_dl = ""
        self.meshe = value
        self.stream_content = self.generate_mesh()

    def generate_mesh(self):

        mesh = BASES.get(self.meshe).get('mesh')
        for props in self.option:
            mesh += PROPS.get(props, {}).get('mesh')

        mutable_data = bytearray(mesh.export(file_type='glb'))
        mutable_data[0] = 0x01
        mutable_data[1] = 0x02
        mutable_data[2] = 0x03
        mutable_data[3] = 0x04
        base64_encoded_data = base64.b64encode(mutable_data)
        return base64_encoded_data.decode('utf-8')

    def generate_and_download_file(self):
        # Replace the following line with your file content generation logic
        mesh = BASES.get(self.meshe).get('mesh')
        for props in self.option:
            mesh += PROPS.get(props, {}).get('mesh')
        # Stream the file content
        text = create_bent_text_trimesh(
            font_path=r"C:\Users\Leo\PycharmProjects\npc\reflex3d\mesh\fonts\Android.ttf",
            font_size=self.font_size - 0.07,
            text_content=self.text,
            radius_x=self.radius - 0.5,
            radius_y=self.radius - 0.5,
            x_rotation=78,
            extrude=self.height - 0.1
        )
        self.stream_content_dl = base64.b64encode((mesh + text).export(file_type='stl')).decode('utf-8')