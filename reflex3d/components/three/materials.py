import reflex as rx


class MeshStandardMaterial(rx.Component):
    library = "@react-three/fiber"
    tag = "meshStandardMaterial"
    color: rx.Var[str]
