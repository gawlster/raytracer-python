from typing import Tuple, List
from vector import Vector


class Ray:
    origin: Vector
    direction: Vector

    def __init__(self, origin: Vector, direction: Vector) -> None:
        self.origin = origin
        self.direction = direction

    def __repr__(self) -> str:
        return f"""
Ray(
    origin: {self.origin}
    direction: {self.direction}
)"""

    def cast(self, spheres: List) -> Tuple:
        for sphere in spheres:
            intersect = sphere.intersection(self)
            if type(intersect) == Vector:
                return intersect, sphere
        return False, False
