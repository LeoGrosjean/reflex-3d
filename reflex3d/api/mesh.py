import base64
from typing import Any

import trimesh
import numpy as np
from fastapi.responses import Response
import reflex as rx


async def api_test():
    mesh = trimesh.load("reflex3d/mesh/base/base_1.stl")
    mesh += trimesh.load("reflex3d/mesh/props/sphere_top_bottom.stl")
    angle_x = np.radians(90)  # 30 degrees rotation around X-axis
    angle_y = np.radians(-180)  # 45 degrees rotation around Y-axis

    # Create rotation matrices
    rotation_matrix_x = trimesh.transformations.rotation_matrix(angle_x, [1, 0, 0])
    rotation_matrix_y = trimesh.transformations.rotation_matrix(angle_y, [0, 0, 1])
    mesh.apply_transform(rotation_matrix_x)
    mesh.apply_transform(rotation_matrix_y)
    headers = {
        'Content-Type': 'application/octet-stream',
        'Content-Disposition': 'attachment; filename="streaming.glb"'
    }
    glb_data = mesh.export(file_type='glb')
    mutable_data = bytearray(glb_data)
    mutable_data[0] = 0x01
    mutable_data[1] = 0x02
    mutable_data[2] = 0x03
    mutable_data[3] = 0x04

    modified_glb_data = bytes(mutable_data)
    return Response(content=modified_glb_data, media_type='model/gltf-binary', headers=headers)
