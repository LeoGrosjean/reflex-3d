from enum import Enum

from pydantic import BaseModel


class Vector3(BaseModel):
    x: float
    y: float
    z: float


class EulerOrder(Enum):
    XYZ = "XYZ"
    YXZ = "YXZ"
    ZXY = "ZXY"
    ZYX = "ZYX"
    YZX = "YZX"
    XZY = "XZY"


class Euler(BaseModel):
    x: float
    y: float
    z: float
    order: EulerOrder = 'XYZ'


class Quaternion(BaseModel):
    x: float
    y: float
    z: float
    w: float


class Matrix4(BaseModel):
    n11: float = 1.0
    n12: float = 0.0
    n13: float = 0.0
    n14: float = 0.0
    n21: float = 0.0
    n22: float = 1.0
    n23: float = 0.0
    n24: float = 0.0
    n31: float = 0.0
    n32: float = 0.0
    n33: float = 1.0
    n34: float = 0.0
    n41: float = 0.0
    n42: float = 0.0
    n43: float = 0.0
    n44: float = 1.0

    def elements(self) -> list[float]:
        return [
            self.n11, self.n12, self.n13, self.n14,
            self.n21, self.n22, self.n23, self.n24,
            self.n31, self.n32, self.n33, self.n34,
            self.n41, self.n42, self.n43, self.n44,
        ]
