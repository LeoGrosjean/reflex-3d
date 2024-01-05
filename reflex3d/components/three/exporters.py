from typing import Any

import reflex as rx
from reflex.components.tags import Tag
from reflex.utils import imports


class STLViewer(rx.Component):

    def _get_custom_code(self) -> str | None:
        return """
import React, { useState, useEffect } from 'react';
import { useThree } from 'react-three-fiber';
import { STLExporter } from 'three/examples/jsm/exporters/STLExporter';

const STLViewer = () => {
    const { scene } = useThree();
    const [stl, setStl] = useState();

    useEffect(() => {
        setStl(new STLExporter().parse(scene));
    }, [scene]);

    return (
        <div className="stl">
            {"Exported STL:\n\n"}
            <pre>{stl}</pre>
        </div>
    );
};
"""

    def _render(self, props: dict[str, Any] | None = None) -> Tag:
        return Tag(
            name="STLViewer",
        )