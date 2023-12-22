import reflex as rx
from reflex.components.tags import Tag


class ModelGltf(rx.Component):
    library = "/utils/state"
    tag = "ModelGltf"

    # ref: pc.Var[str] = ""

    def _get_custom_code(self) -> str | None:
        return '''
        import { useLoader } from "@react-three/fiber";

        import { GLTFLoader } from "three/examples/jsm/loaders/GLTFLoader";
        import { Suspense } from "react";
        const gltf = useLoader(GLTFLoader, "http://localhost:3000/gltf/Poimandres.gltf");
        '''

    def render(self) -> Tag:
        return ("<Suspense><primitive object={gltf.scene} scale={0.4} /></Suspense>")