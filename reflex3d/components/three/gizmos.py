from typing import Any

import reflex as rx
from reflex.components.tags import Tag
from reflex.utils import imports


class Ground(rx.Component):

    def _get_custom_code(self) -> str | None:
        return """
function Ground() {
  const gridConfig = {
    cellSize: 0.5,
    cellThickness: 0.5,
    cellColor: '#6f6f6f',
    sectionSize: 3,
    sectionThickness: 1,
    sectionColor: '#9d4b4b',
    fadeDistance: 300,
    fadeStrength: 1,
    followCamera: false,
    infiniteGrid: true
  }
  return <Grid position={[0, -0.01, 0]} args={[10.5, 10.5]} {...gridConfig} />
}
"""

    def _get_imports(self) -> imports.ImportDict:
        return rx.utils.imports.merge_imports(
            super()._get_imports() | {
                "@react-three/drei": {
                    rx.vars.ImportVar(tag="Grid"),
                },
            }
        )

    def _render(self, props: dict[str, Any] | None = None) -> Tag:
        return Tag(
            name="Ground",
        )
