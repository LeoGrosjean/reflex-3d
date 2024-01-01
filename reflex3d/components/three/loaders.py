from typing import Callable, Any

import reflex as rx
from reflex.components.tags import Tag
from reflex.style import Style
from reflex.utils import imports
from reflex.utils.imports import ImportVar


class GLTFLoader(rx.Component):
    tag = "LoaderGltf"
    url: rx.Var[str]

    def _get_custom_code(self) -> str | None:
        return f"""
    function LoaderGltf({{url}}) {{
        const gltf = useGLTF(url)
        window['scene'] = gltf.scene
        return (
            <primitive object={{gltf.scene}} children-0-castShadow />
        )
    }}
    """

    def _get_imports(self) -> imports.ImportDict:
        return rx.utils.imports.merge_imports(
            super()._get_imports() | {
                "react": {rx.vars.ImportVar(tag="useRef")},
                "@react-three/drei": {rx.vars.ImportVar(tag="useGLTF")},
            }
        )

    def _render(self, props: dict[str, Any] | None = None) -> Tag:
        return Tag(name="LoaderGltf", props={"url": self.url})


class UseGLTF(rx.Component):
    url: rx.Var[str]
    tag = "Loader"

    def _get_custom_code(self) -> str | None:
        return f"""
import {{ useRef }} from "react"
import {{ useLoader }} from '@react-three/fiber'
import {{ GLTFLoader }} from 'three/addons/loaders/GLTFLoader.js'
    
function Loader({{url}}) {{
    console.log(url)
    const gltf = useLoader(GLTFLoader, url)
    return (
        <primitive object={{gltf.scene}} position={{[0, 1, 0]}} children-0-castShadow />
    )
}}
"""

    def _render(self, props: dict[str, Any] | None = None) -> Tag:
        return Tag(name="Loader", props={"url": self.url})
