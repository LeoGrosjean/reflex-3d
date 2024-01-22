import trimesh
import numpy as np


def rotate(mesh):
    angle_x = np.radians(90)  # 30 degrees rotation around X-axis
    angle_y = np.radians(-180)  # 45 degrees rotation around Y-axis
    rotation_matrix_x = trimesh.transformations.rotation_matrix(angle_x, [1, 0, 0])
    rotation_matrix_y = trimesh.transformations.rotation_matrix(angle_y, [0, 0, 1])
    mesh.apply_transform(rotation_matrix_x)
    mesh.apply_transform(rotation_matrix_y)
    return mesh


PROPS_0 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Air Extraction Style 1.stl")), "metdata": []}
PROPS_1 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Air Extraction Style 2.stl")), "metdata": []}
PROPS_2 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Ball Clean Style 1.stl")), "metdata": []}
PROPS_3 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Ball Clean Style 2.stl")), "metdata": []}
PROPS_4 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Ball Metal Ring Style 1.stl")), "metdata": []}
PROPS_5 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Ball Metal Ring Style 2.stl")), "metdata": []}
PROPS_6 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Ball Metal Spike Style 1.stl")), "metdata": []}
PROPS_7 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Ball Metal Spike Style 2.stl")), "metdata": []}
PROPS_8 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Ball Spiked Metal Ring Style 1.stl")), "metdata": []}
PROPS_9 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Ball Spiked Metal Ring Style 2.stl")), "metdata": []}
PROPS_10 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Ball Spiked Style 1.stl")), "metdata": []}
PROPS_11 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Ball Spiked Style 2.stl")), "metdata": []}
PROPS_12 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Ball Stitched Style 1.stl")), "metdata": []}
PROPS_13 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Ball Stitched Style 2.stl")), "metdata": []}
PROPS_14 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Bolt Style 1.stl")), "metdata": []}
PROPS_15 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Bolt Style 2.stl")), "metdata": []}
PROPS_16 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Bolt Style 3.stl")), "metdata": []}
PROPS_17 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Bolt Style 4.stl")), "metdata": []}
PROPS_18 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Bolt Style 5.stl")), "metdata": []}
PROPS_19 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Bolt Style 6.stl")), "metdata": []}
PROPS_20 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Bolt Style 7.stl")), "metdata": []}
PROPS_21 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/High Tube Style 1.stl")), "metdata": []}
PROPS_22 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Imperium Style 1.stl")), "metdata": []}
PROPS_23 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Imperium Style 2.stl")), "metdata": []}
PROPS_24 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Joystick Controller Style 1.stl")), "metdata": []}
PROPS_25 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Joystick Controller Style 2.stl")), "metdata": []}
PROPS_26 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Lateral Controller 1 Style 1.stl")), "metdata": []}
PROPS_27 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Lateral Controller 1 Style 2.stl")), "metdata": []}
PROPS_28 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Lateral Controller 1 Style 3.stl")), "metdata": []}
PROPS_29 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Lateral Controller 2 Style 1.stl")), "metdata": []}
PROPS_30 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Lateral Controller 2 Style 2.stl")), "metdata": []}
PROPS_31 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Lateral Controller 2 Style 3.stl")), "metdata": []}
PROPS_32 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Lateral Controller 2 Style 4.stl")), "metdata": []}
PROPS_33 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Lateral Controller 2 Style 5.stl")), "metdata": []}
PROPS_34 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Lateral Controller 2 Style 6.stl")), "metdata": []}
PROPS_35 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Lateral Tube Style 1.stl")), "metdata": []}
PROPS_36 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Lateral Tube Style 10.stl")), "metdata": []}
PROPS_37 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Lateral Tube Style 2.stl")), "metdata": []}
PROPS_38 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Lateral Tube Style 3.stl")), "metdata": []}
PROPS_39 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Lateral Tube Style 4.stl")), "metdata": []}
PROPS_40 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Lateral Tube Style 5.stl")), "metdata": []}
PROPS_41 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Lateral Tube Style 6.stl")), "metdata": []}
PROPS_42 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Lateral Tube Style 7.stl")), "metdata": []}
PROPS_43 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Lateral Tube Style 8.stl")), "metdata": []}
PROPS_44 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Lateral Tube Style 9.stl")), "metdata": []}
PROPS_45 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Nuclear Style 1.stl")), "metdata": []}
PROPS_46 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Nuclear Style 2.stl")), "metdata": []}
PROPS_47 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Screw Style 1.stl")), "metdata": []}
PROPS_48 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Screw Style 2.stl")), "metdata": []}
PROPS_49 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Screw Style 3.stl")), "metdata": []}
PROPS_50 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Screw Style 4.stl")), "metdata": []}
PROPS_51 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Screw Style 5.stl")), "metdata": []}
PROPS_52 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Screw Style 6.stl")), "metdata": []}
PROPS_53 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Screw Style 7.stl")), "metdata": []}
PROPS_54 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Shape 3 Lights Style 1.stl")), "metdata": []}
PROPS_55 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Shape 3 Lights Style 2.stl")), "metdata": []}
PROPS_56 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Shield Style 1.stl")), "metdata": []}
PROPS_57 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Shield Style 2.stl")), "metdata": []}
PROPS_58 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Shield Style 3.stl")), "metdata": []}
PROPS_59 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Side Wheel Style 1.stl")), "metdata": []}
PROPS_60 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Side Wheel Style 2.stl")), "metdata": []}
PROPS_61 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Side Wheel Style 3.stl")), "metdata": []}
PROPS_62 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Side Wheel Style 4.stl")), "metdata": []}
PROPS_63 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Side Wheel Style 5.stl")), "metdata": []}
PROPS_64 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Side Wheel Style 6.stl")), "metdata": []}
PROPS_65 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Sphere Style 1.stl")), "metdata": []}
PROPS_66 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Sphere Style 2.stl")), "metdata": []}
PROPS_67 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Sphere Style 3.stl")), "metdata": []}
PROPS_68 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Sphere Style 4.stl")), "metdata": []}
PROPS_69 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Sphere Style 5.stl")), "metdata": []}
PROPS_70 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Sphere Style 6.stl")), "metdata": []}
PROPS_71 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Sphere Style 7.stl")), "metdata": []}
PROPS_72 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Sphere Style 8.stl")), "metdata": []}
PROPS_73 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Squeleton Head Style 1.stl")), "metdata": []}
PROPS_74 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Squeleton Head Style 2.stl")), "metdata": []}
PROPS_75 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Squeleton Head Style 3.stl")), "metdata": []}
PROPS_76 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Tubes Around Shape Style 1.stl")), "metdata": []}
PROPS_77 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Tubes Around Shape Style 2.stl")), "metdata": []}
PROPS_78 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Tubes Around Shape Style 3.stl")), "metdata": []}
PROPS_79 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Tubes Around Shape Style 4.stl")), "metdata": []}
PROPS_80 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Tubes Around Shape Style 5.stl")), "metdata": []}
PROPS_81 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Tubes Around Shape Style 6.stl")), "metdata": []}
PROPS_82 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Tubes Around Shape Style 7.stl")), "metdata": []}
PROPS_83 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Tubes To Front Style 1.stl")), "metdata": []}
PROPS_84 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Tubes To Front Style 2.stl")), "metdata": []}
PROPS_85 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Umbrella Style 1.stl")), "metdata": []}
PROPS_86 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Umbrella Style 2.stl")), "metdata": []}
PROPS_87 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Umbrella Style 3.stl")), "metdata": []}
PROPS_88 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Umbrella Style 4.stl")), "metdata": []}
PROPS_89 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Yin Yang Style 1.stl")), "metdata": []}
PROPS_90 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Yin Yang Style 2.stl")), "metdata": []}
PROPS_91 = {'mesh': rotate(trimesh.load("reflex3d/mesh/props/Yin Yang Style 3.stl")), "metdata": []}

PROPS = {
    "Air Extraction Style 1": PROPS_0,
    "Air Extraction Style 2": PROPS_1,
    "Ball Clean Style 1": PROPS_2,
    "Ball Clean Style 2": PROPS_3,
    "Ball Metal Ring Style 1": PROPS_4,
    "Ball Metal Ring Style 2": PROPS_5,
    "Ball Metal Spike Style 1": PROPS_6,
    "Ball Metal Spike Style 2": PROPS_7,
    "Ball Spiked Metal Ring Style 1": PROPS_8,
    "Ball Spiked Metal Ring Style 2": PROPS_9,
    "Ball Spiked Style 1": PROPS_10,
    "Ball Spiked Style 2": PROPS_11,
    "Ball Stitched Style 1": PROPS_12,
    "Ball Stitched Style 2": PROPS_13,
    "Bolt Style 1": PROPS_14,
    "Bolt Style 2": PROPS_15,
    "Bolt Style 3": PROPS_16,
    "Bolt Style 4": PROPS_17,
    "Bolt Style 5": PROPS_18,
    "Bolt Style 6": PROPS_19,
    "Bolt Style 7": PROPS_20,
    "High Tube Style 1": PROPS_21,
    "Imperium Style 1": PROPS_22,
    "Imperium Style 2": PROPS_23,
    "Joystick Controller Style 1": PROPS_24,
    "Joystick Controller Style 2": PROPS_25,
    "Lateral Controller 1 Style 1": PROPS_26,
    "Lateral Controller 1 Style 2": PROPS_27,
    "Lateral Controller 1 Style 3": PROPS_28,
    "Lateral Controller 2 Style 1": PROPS_29,
    "Lateral Controller 2 Style 2": PROPS_30,
    "Lateral Controller 2 Style 3": PROPS_31,
    "Lateral Controller 2 Style 4": PROPS_32,
    "Lateral Controller 2 Style 5": PROPS_33,
    "Lateral Controller 2 Style 6": PROPS_34,
    "Lateral Tube Style 1": PROPS_35,
    "Lateral Tube Style 10": PROPS_36,
    "Lateral Tube Style 2": PROPS_37,
    "Lateral Tube Style 3": PROPS_38,
    "Lateral Tube Style 4": PROPS_39,
    "Lateral Tube Style 5": PROPS_40,
    "Lateral Tube Style 6": PROPS_41,
    "Lateral Tube Style 7": PROPS_42,
    "Lateral Tube Style 8": PROPS_43,
    "Lateral Tube Style 9": PROPS_44,
    "Nuclear Style 1": PROPS_45,
    "Nuclear Style 2": PROPS_46,
    "Screw Style 1": PROPS_47,
    "Screw Style 2": PROPS_48,
    "Screw Style 3": PROPS_49,
    "Screw Style 4": PROPS_50,
    "Screw Style 5": PROPS_51,
    "Screw Style 6": PROPS_52,
    "Screw Style 7": PROPS_53,
    "Shape 3 Lights Style 1": PROPS_54,
    "Shape 3 Lights Style 2": PROPS_55,
    "Shield Style 1": PROPS_56,
    "Shield Style 2": PROPS_57,
    "Shield Style 3": PROPS_58,
    "Side Wheel Style 1": PROPS_59,
    "Side Wheel Style 2": PROPS_60,
    "Side Wheel Style 3": PROPS_61,
    "Side Wheel Style 4": PROPS_62,
    "Side Wheel Style 5": PROPS_63,
    "Side Wheel Style 6": PROPS_64,
    "Sphere Style 1": PROPS_65,
    "Sphere Style 2": PROPS_66,
    "Sphere Style 3": PROPS_67,
    "Sphere Style 4": PROPS_68,
    "Sphere Style 5": PROPS_69,
    "Sphere Style 6": PROPS_70,
    "Sphere Style 7": PROPS_71,
    "Sphere Style 8": PROPS_72,
    "Squeleton Head Style 1": PROPS_73,
    "Squeleton Head Style 2": PROPS_74,
    "Squeleton Head Style 3": PROPS_75,
    "Tubes Around Shape Style 1": PROPS_76,
    "Tubes Around Shape Style 2": PROPS_77,
    "Tubes Around Shape Style 3": PROPS_78,
    "Tubes Around Shape Style 4": PROPS_79,
    "Tubes Around Shape Style 5": PROPS_80,
    "Tubes Around Shape Style 6": PROPS_81,
    "Tubes Around Shape Style 7": PROPS_82,
    "Tubes To Front Style 1": PROPS_83,
    "Tubes To Front Style 2": PROPS_84,
    "Umbrella Style 1": PROPS_85,
    "Umbrella Style 2": PROPS_86,
    "Umbrella Style 3": PROPS_87,
    "Umbrella Style 4": PROPS_88,
    "Yin Yang Style 1": PROPS_89,
    "Yin Yang Style 2": PROPS_90,
    "Yin Yang Style 3": PROPS_91,
}