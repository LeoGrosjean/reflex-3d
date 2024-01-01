from typing import Any

import reflex as rx
from reflex.components.tags import Tag
from reflex.utils import imports


class CurvedText(rx.Component):
    library = "@react-three/drei"
    tag = "CurvedText"

    radius: rx.Var[int | float] = 5
    text: rx.Var[str]
    font: rx.Var[str]
    transpose_x: rx.Var[int | float] = 0

    def _get_custom_code(self) -> str | None:
        return """
function CurvedText({text, font, curve, radius, transposeX}) {
    const ellipseCurve_ = new EllipseCurve(0, 0, radius, radius, 0, 2 * Math.PI, false, (1 / 4) * Math.PI);
    const points2D_ = ellipseCurve_.getPoints(40);
    const points3D_ = points2D_.map(p => new Vector3(p.x, 0, p.y));

    const catmullRomCurve2 = new CatmullRomCurve3(points3D_);

    const matrix = new Matrix4();
    let rotationZ = new Matrix4().makeRotationZ(MathUtils.degToRad(180));
    let rotationX = new Matrix4().makeRotationX(MathUtils.degToRad(-10));

    matrix.multiply(rotationZ)
    matrix.multiply(rotationX)

    const [currentText, setCurrentText] = useState(text);
    const [currentFont, setCurrentFont] = useState(font);
    const [currentTransposeX, setCurrentTransposeX] = useState(transposeX);

    const textRef = useRef();

    const isMounted = useRef(false);

    useEffect(() => {
        if (isMounted.current) {
            if (textRef.current) {
                console.log(transposeX, currentTransposeX)
                const boundingBox = new Box3().setFromObject(textRef.current);

                const translation = new Matrix4().makeTranslation((-boundingBox.max.x / 2) + transposeX, 0, 0);
                matrix.multiply(translation)

                textRef.current.geometry.applyMatrix4(matrix)

                rotationZ = new Matrix4().makeRotationZ(MathUtils.degToRad(0));
                rotationX = new Matrix4().makeRotationX(MathUtils.degToRad(0));

                setCurrentTransposeX(transposeX)
            }
        } else {
            isMounted.current = true;
        }

    }, [textRef.current, text, font]);

    useEffect(() => {
        if (textRef.current) {
            let translation_x = new Matrix4().makeTranslation(-transposeX + currentTransposeX, 0, 0);
            textRef.current.geometry.applyMatrix4(translation_x)
            setCurrentTransposeX(transposeX)
        }
    }, [transposeX]);
    return (
        <><Suspense>
            <group rotation={[0, 0, 0]} position={[0, 0, 0]}>
                <CurveModifier curve={catmullRomCurve2}>
                    <Text3D ref={textRef} font={font} rotation={[0, 0, 0]} position={[0, 0, 0]} osef={transposeX}>
                        {text}
                        <meshStandardMaterial color={`lightgrey`}/>
                    </Text3D>
                </CurveModifier>
            </group>
        </Suspense></>
    );
}
"""

    def _get_imports(self) -> imports.ImportDict:
        return rx.utils.imports.merge_imports(
            super()._get_imports() | {
                "react": {
                    rx.vars.ImportVar(tag="useState"),
                    rx.vars.ImportVar(tag="useEffect"),
                    rx.vars.ImportVar(tag="useRef"),
                    rx.vars.ImportVar(tag="Suspense")
                },
                "@react-three/drei": {
                    rx.vars.ImportVar(tag="Text3D"),
                    rx.vars.ImportVar(tag="CurveModifier")
                },
                "three": {
                    rx.vars.ImportVar(tag="CatmullRomCurve3"),
                    rx.vars.ImportVar(tag="EllipseCurve"),
                    rx.vars.ImportVar(tag="Vector3"),
                    rx.vars.ImportVar(tag="Matrix4"),
                    rx.vars.ImportVar(tag="Box3"),
                    rx.vars.ImportVar(tag="MathUtils")
                },
                "three-subdivide": {
                    rx.vars.ImportVar(tag="LoopSubdivision"),
                }
            }
        )

    def _render(self, props: dict[str, Any] | None = None) -> Tag:
        return Tag(
            name="CurvedText",
            props={
                "text": self.text,
                "font": self.font,
                "radius": self.radius,
                "transposeX": self.transpose_x
            }
        )
