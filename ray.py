from typing import Tuple, List

from numpy import Infinity
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
        closestIntersectionDistance = Infinity
        cur: Tuple = (False, False)
        for sphere in spheres:
            intersect, intersectDistance = sphere.intersection(self)
            if (
                type(intersect) == Vector
                and intersectDistance < closestIntersectionDistance
            ):
                cur = intersect, sphere
        return cur
