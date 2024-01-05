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
        return """
    function LoaderGltf({url}) {{
        const gltf = useGLTF(url)
        
        return (
            <primitive object={gltf.scene} children-0-castShadow />
        )
    }}
    """

    def _get_imports(self) -> imports.ImportDict:
        return rx.utils.imports.merge_imports(
            super()._get_imports() | {
                "react": {
                    rx.vars.ImportVar(tag="useRef"),
                },
                "@react-three/drei": {
                    rx.vars.ImportVar(tag="useGLTF")
                },

            }
        )

    def _render(self, props: dict[str, Any] | None = None) -> Tag:
        return Tag(name="LoaderGltf", props={"url": self.url})


class UseGLTF(rx.Component):
    url: rx.Var[str]
    tag = "Loader"

    def _get_custom_code(self) -> str | None:
        return """
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
function Loader({url}) {
    console.log(url)
    const gltf = useLoader(GLTFLoader, url)
    return (
        <primitive object={gltf.scene} position={[0, 1, 0]} children-0-castShadow />
    )
}
"""

    def _get_imports(self) -> imports.ImportDict:
        return rx.utils.imports.merge_imports(
            super()._get_imports() | {
                "react": {
                    rx.vars.ImportVar(tag="useRef"),
                },
                "@react-three/drei": {
                    rx.vars.ImportVar(tag="useGLTF")
                },
                "@react-three/fiber": {
                    rx.vars.ImportVar(tag="useLoader")
                },
            }
        )

    def _render(self, props: dict[str, Any] | None = None) -> Tag:
        return Tag(name="Loader", props={"url": self.url})


class CorruptedGLBLoader(rx.Component):
    url: rx.Var[str]

    def _get_custom_code(self) -> str | None:

        return """
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
const CorruptedGLBLoader = ({ url }) => {
  const [model, setModel] = useState();

  useEffect(() => {
    async function fetchAndCorrectModel(url) {
      const response = await fetch(url);
      const buffer = await response.arrayBuffer();
      const view = new Uint8Array(buffer);
      view[0] = 103;
      view[1] = 108;
      view[2] = 84;
      view[3] = 70;
      return buffer;
    }

    fetchAndCorrectModel(url).then(correctedBuffer => {
      const loader = new GLTFLoader();
      loader.parse(correctedBuffer, '', gltf => setModel(gltf.scene));
    });
  }, [url]);

  return model ? <primitive object={model} /> : null;
}
"""

    def _render(self, props: dict[str, Any] | None = None) -> Tag:
        return Tag(name="CorruptedGLBLoader", props={"url": self.url})

    def _get_imports(self) -> imports.ImportDict:
        return rx.utils.imports.merge_imports(
            super()._get_imports() | {
                "react": {
                    rx.vars.ImportVar(tag="useState"),
                    rx.vars.ImportVar(tag="useEffect"),
                },
            }
        )


class LoadGlbBytes(rx.Component):
    bytes_: rx.Var[str]

    def _get_custom_code(self) -> str | None:

        return """
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';

const LoadGlbBytes = ({ bytes_ }) => {
  const [model, setModel] = useState();

  useEffect(() => {
    const loader = new GLTFLoader();
    try {
      let binaryString = atob(bytes_)
      const len = binaryString.length;
      const bytes = new Uint8Array(len);
      for (let i = 0; i < len; i++) {
        bytes[i] = binaryString.charCodeAt(i);
      }
      bytes[0] = 103;
      bytes[1] = 108;
      bytes[2] = 84;
      bytes[3] = 70;
      loader.parse(bytes.buffer, '', gltf => setModel(gltf.scene));
    } catch (error) {
      console.error(error);
    }
  }, [bytes_])

  return model ? <primitive object={model} /> : null;
}
"""

    def _render(self, props: dict[str, Any] | None = None) -> Tag:
        return Tag(name="LoadGlbBytes", props={"bytes_": self.bytes_})

    def _get_imports(self) -> imports.ImportDict:
        return rx.utils.imports.merge_imports(
            super()._get_imports() | {
                "react": {
                    rx.vars.ImportVar(tag="useState"),
                    rx.vars.ImportVar(tag="useEffect"),
                },
            }
        )
