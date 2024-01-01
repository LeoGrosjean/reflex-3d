from math import pi
from typing import Any

import reflex as rx
from reflex.components import Tag
from reflex.utils import imports


class EllipseCurve(rx.Component):
    tag = "Test"

    radius: rx.Var[int | float]

    def _get_custom_code(self) -> str | None:
        return f"""
    function Test() {{
        const points = useMemo(() => new EllipseCurve(0, 0, 2, 2, 0, 2 * Math.PI, false, Math.PI).getPoints(100), [])
        return <Line points={{points}} color="turquoise" lineWidth={{1}} />
    }}
    """

    def _get_imports(self) -> imports.ImportDict:
        return rx.utils.imports.merge_imports(
            super()._get_imports() | {
                "react": {rx.vars.ImportVar(tag="useMemo")},
                "three": {rx.vars.ImportVar(tag="EllipseCurve")},
                "@react-three/drei": {rx.vars.ImportVar(tag="Line")},
            }
        )


class CurveModifier (rx.Component):
    library = "@react-three/drei"
    tag = "CurveModifier"

    radius: rx.Var[int | float]
    curve: rx.Var[rx.Component]

    def _get_custom_code(self) -> str | None:
        return f"""
import * as THREE from 'three';

const ellipseCurve = new THREE.EllipseCurve(0, 0, 2, 2, 0, 2 * Math.PI, false, Math.PI /2);
const points2D = ellipseCurve.getPoints(10);

const points3D = points2D.map(p => new THREE.Vector3(p.x, p.y, 0));

const catmullRomCurve = new THREE.CatmullRomCurve3(points3D);
"""

    def _get_imports(self) -> imports.ImportDict:
        return rx.utils.imports.merge_imports(
            super()._get_imports() | {
                "react": {rx.vars.ImportVar(tag="useMemo")},
            }
        )


class CatmullRomCurve(rx.Component):
    tag = 'catmullRomCurve'

    def render(self):
        return "catmullRomCurve"


class CurveModifierV2(rx.Component):
    library = "@react-three/drei"
    tag = "CurveModifier"

    radius: rx.Var[int | float]
    curve: rx.Var[rx.Component]
    onUpdate: rx.Var[rx.Component]

    def _get_custom_code(self) -> str | None:
        self.onUpdate = rx.Var.create(
            "self => self.applyMatrix4(rotationMatrix)",
            _var_is_local=False,
        )
        self.curve = rx.Var.create(
            "catmullRomCurve",
            _var_is_local=False,
        )
        return f"""
import * as THREE from 'three';

const ellipseCurve = new THREE.EllipseCurve(0, 0, 2, 2, 0, 2 * Math.PI, false, Math.PI /2);
const points2D = ellipseCurve.getPoints(10);
const angle = Math.PI; // 180 degrees in radians
const rotationMatrix = new THREE.Matrix4().makeRotationX(angle);
const points3D = points2D.map(p => new THREE.Vector3(p.x, 0, p.y));

const catmullRomCurve = new THREE.CatmullRomCurve3(points3D);
"""

    def _get_imports(self) -> imports.ImportDict:
        return rx.utils.imports.merge_imports(
            super()._get_imports() | {
                "react": {rx.vars.ImportVar(tag="useMemo")},
            }
        )
"""
import React, { useState, useEffect } from 'react';
import { Canvas } from '@react-three/fiber';
import { Text3D, CurveModifier } from '@react-three/drei';
import * as THREE from 'three';

function CurvedText({ text, font, curve, ...props }) {
  const [mesh, setMesh] = useState();

  useEffect(() => {
    // Update the mesh when text or font changes
    setMesh(
      <Text3D font={font} {...props}>
        {text}
      </Text3D>
    );
  }, [text, font, props]);

  return (
    <CurveModifier curve={curve}>
      {mesh}
    </CurveModifier>
  );
}

"""