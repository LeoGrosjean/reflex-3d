import base64
from math import radians, pi, cos, sin
from typing import Any

import bpy
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


def save_mesh_blender(name):
    import bpy
    # Deselect all objects
    bpy.ops.object.select_all(action='DESELECT')
    # Replace 'YourMeshName' with the name of your mesh object
    mesh_name = name
    mesh_object = bpy.data.objects[mesh_name]
    # Select the mesh object
    mesh_object.select_set(True)
    # Set the mesh as the active object
    bpy.context.view_layer.objects.active = mesh_object
    # Export the mesh as STL
    bpy.ops.export_mesh.stl(filepath=f"{name}.stl", use_selection=True)


def loop_collection(name):
    import bpy
    # Replace 'YourCollectionName' with the name of your collection
    collection_name = name
    collection = bpy.data.collections[collection_name]
    for obj in collection.objects:
        # Check if the object is a mesh
        if obj.type == 'MESH':
            # Perform your operations here
            # For example, printing the mesh name
            save_mesh_blender(obj.name)


def create_bent_text_trimesh(font_path, font_size, text_content, radius_x, radius_y, x_rotation=0, extrude=0.8):
    # Create Text Curve
    text_curve = bpy.data.curves.new(type="FONT", name="TextCurve")
    text_curve.body = text_content
    text_curve.font = bpy.data.fonts.load(font_path)
    text_curve.extrude = extrude  # Set extrusion
    text_curve.size = font_size

    # Create Text Object
    text_obj = bpy.data.objects.new("TextObject", text_curve)

    text_obj.data.align_x = 'CENTER'
    #text_obj.data.align_y = 'CENTER'
    bpy.context.collection.objects.link(text_obj)  # Link text object to the collection

    # Apply rotation on the X-axis
    text_obj.rotation_euler[0] = radians(x_rotation)
    text_obj.rotation_euler[2] = radians(180)

    # Add a Bezier circle
    bpy.ops.curve.primitive_bezier_circle_add()
    bezier_circle = bpy.context.object

    # Scale the circle to create an oval if necessary
    bezier_circle.scale.x = radius_x
    bezier_circle.scale.y = radius_y

    # Apply Curve Modifier to Text
    text_obj.modifiers.new(type="CURVE", name="CurveModifier").object = bezier_circle

    # Set the active object to text_obj for the triangulate operation
    bpy.context.view_layer.objects.active = text_obj
    bpy.context.view_layer.update()

    # Convert to mesh and triangulate
    bpy.ops.object.select_all(action='DESELECT')
    text_obj.select_set(True)
    bpy.ops.object.convert(target='MESH')
    bpy.ops.object.modifier_add(type='TRIANGULATE')

    # Get the triangulated mesh data
    mesh_data = bpy.data.meshes.new_from_object(text_obj.evaluated_get(bpy.context.evaluated_depsgraph_get()))

    # Extract mesh data
    vertices = [vert.co[:] for vert in mesh_data.vertices]
    faces = [[vertex for vertex in face.vertices] for face in mesh_data.polygons]

    # Create Trimesh object
    vertices_array = np.array(vertices)
    faces_array = np.array(faces)
    mesh_trimesh = trimesh.Trimesh(vertices=vertices_array, faces=faces_array)

    # Clean up
    bpy.data.objects.remove(text_obj)
    bpy.data.objects.remove(bezier_circle)
    bpy.data.meshes.remove(mesh_data)

    angle_x = np.radians(-12)
    rotation_matrix_x = trimesh.transformations.rotation_matrix(angle_x, [1, 0, 0])
    mesh_trimesh.apply_transform(rotation_matrix_x)

    angle_z = np.radians(-180)
    rotation_matrix_z = trimesh.transformations.rotation_matrix(angle_z, [0, 1, 0])
    mesh_trimesh.apply_transform(rotation_matrix_z)

    translation_vector = [0, -mesh_trimesh.bounds[1][1] / 2 + 2.8, 0]
    mesh_trimesh.apply_translation(translation_vector)

    return mesh_trimesh

# Example usage
# from reflex3d.api.mesh import create_bent_text_trimesh
# from reflex3d.mesh import rotate
# import trimesh
# BASE_1 = rotate(trimesh.load("reflex3d/mesh/base/text style 1 -  Arrow deco.stl"))
# mesh_trimesh = create_bent_text_trimesh(
#   r"C:\Users\Leo\PycharmProjects\npc\reflex3d\mesh\fonts\Android.ttf", 2 - 0.07, 'Your Text Here', 21, 21, 78, 0.6 - 0.1
# )
# (BASE_1 + mesh_trimesh).show()
# mesh_trimesh.fix_normals()
# mesh_trimesh.fill_holes()
# trimesh.boolean.difference([BASE_1, mesh_trimesh]).show()


def create_bent_text_trimesh2(font_path, text_content, radius_x, radius_y, x_rotation=0, extrude=0.1):
    # Create Text Curve
    text_curve = bpy.data.curves.new(type="FONT", name="TextCurve")
    text_curve.body = text_content
    text_curve.font = bpy.data.fonts.load(font_path)
    text_curve.extrude = extrude

    # Create Text Object
    text_obj = bpy.data.objects.new("TextObject", text_curve)
    bpy.context.collection.objects.link(text_obj)

    # Apply rotation on the X-axis
    text_obj.rotation_euler[0] = radians(x_rotation)

    # Create an Elliptical Path
    bezier_path = bpy.data.curves.new(type="CURVE", name="BezierPath")
    bezier_path.dimensions = '2D'
    spline = bezier_path.splines.new('NURBS')
    spline.use_cyclic_u = True

    # Number of points for the ellipse
    num_points = 8
    spline.points.add(num_points - 1)

    # Set points for the ellipse
    for i in range(num_points):
        angle = 2 * pi * i / num_points
        x = radius_x * cos(angle)
        y = radius_y * sin(angle)
        spline.points[i].co = (x, y, 0, 1)

    # Create Path Object
    path_obj = bpy.data.objects.new("PathObject", bezier_path)
    bpy.context.collection.objects.link(path_obj)

    # Apply Follow Path Constraint
    follow_path_constraint = text_obj.constraints.new(type='FOLLOW_PATH')
    follow_path_constraint.target = path_obj
    follow_path_constraint.use_curve_follow = True
    follow_path_constraint.offset_factor = 0  # Adjust as necessary

    # Update constraints and scene
    bpy.context.view_layer.update()

    # Apply all transformations and constraints
    bpy.context.view_layer.objects.active = text_obj
    bpy.ops.object.select_all(action='DESELECT')
    text_obj.select_set(True)
    bpy.ops.object.constraints_apply(visual=True)
    bpy.ops.object.convert(target='MESH')

    # Get the mesh data
    mesh_data = text_obj.data

    # Extract mesh data
    vertices = [vert.co[:] for vert in mesh_data.vertices]
    faces = [[vertex for vertex in face.vertices] for face in mesh_data.polygons]

    # Create Trimesh object
    vertices_array = np.array(vertices)
    faces_array = np.array(faces)
    mesh_trimesh = trimesh.Trimesh(vertices=vertices_array, faces=faces_array)

    # Clean up
    bpy.data.objects.remove(text_obj)
    bpy.data.objects.remove(path_obj)
    bpy.data.curves.remove(bezier_path)
    bpy.data.meshes.remove(mesh_data)

    return mesh_trimesh
