import base64
from typing import List
import numpy as np
import reflex as rx
import trimesh


MESH_1 = trimesh.load("reflex3d/mesh/base/base_1.stl")
MESH_2 = trimesh.load("reflex3d/mesh/props/sphere_top_bottom.stl")

di = {
    "choix 1": MESH_1,
    "choix 2": MESH_2,
}


def init_mesh():
    mesh = MESH_1.copy()
    mesh += MESH_2.copy()

    angle_x = np.radians(90)
    angle_y = np.radians(-180)
    rotation_matrix_x = trimesh.transformations.rotation_matrix(angle_x, [1, 0, 0])
    rotation_matrix_y = trimesh.transformations.rotation_matrix(angle_y, [0, 0, 1])
    mesh.apply_transform(rotation_matrix_x)
    mesh.apply_transform(rotation_matrix_y)

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

    font_size: float = 3.

    center_trigger: str

    radius: float = 20.476

    transpose_x: float = 0.
    transpose_y: float = 0.

    height: float = 1.1

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
        self.set_center_trigger(value + self.font)
        self.text = value

    @rx.var
    def get_font(self) -> str:
        return self.font

    @rx.var
    def get_font_size(self) -> float:
        return self.font_size

    def set_font(self, value: str):
        self.set_center_trigger(self.text + value)
        self.font = value

    @rx.var
    def get_transpose_x(self) -> float:
        return self.transpose_x

    @rx.var
    def get_transpose_y(self) -> float:
        return self.transpose_y

    stream_content: str = init_mesh()

    @rx.cached_var
    def get_stream_content(self) -> str:
        return self.stream_content


    meshes: List[str] = list(di.keys())
    meshe: str = "choix 1"

    @rx.var
    def get_mesh(self) -> str:
        return self.meshe

    def set_mesh(self, value: str):
        print(value)
        self.meshe = value
        self.stream_content = self.generate_mesh()

    def generate_mesh(self):
        print(f"ici {self.meshe}")
        mesh = di.get(self.meshe).copy()
        print(mesh.metadata.get('file_name'))
        #mesh = MESH_1.copy()
        #mesh += MESH_2.copy()
        angle_x = np.radians(90)  # 30 degrees rotation around X-axis
        angle_y = np.radians(-180)  # 45 degrees rotation around Y-axis
        # Create rotation matrices
        rotation_matrix_x = trimesh.transformations.rotation_matrix(angle_x, [1, 0, 0])
        rotation_matrix_y = trimesh.transformations.rotation_matrix(angle_y, [0, 0, 1])
        mesh.apply_transform(rotation_matrix_x)
        mesh.apply_transform(rotation_matrix_y)
        mutable_data = bytearray(mesh.export(file_type='glb'))
        mutable_data[0] = 0x01
        mutable_data[1] = 0x02
        mutable_data[2] = 0x03
        mutable_data[3] = 0x04
        base64_encoded_data = base64.b64encode(mutable_data)
        return base64_encoded_data.decode('utf-8')
