from typing import Tuple, List

from numpy import Infinity
from hit import Hit
from vector import Vector, ColorVector
from sphere import Sphere


MAX_RECURSION_DEPTH = 3


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

    def cast(self, spheres: List) -> Hit:
        hit = Hit()
        hit.hitDistance = Infinity
        for sphere in spheres:
            intersect, intersectDistance = sphere.intersection(self)
            if type(intersect) == Vector and intersectDistance < hit.hitDistance:
                hit.didHit = True
                hit.hitDistance = intersectDistance
                hit.hitPoint = intersect
                hit.hitObject = sphere
        hit.hitNormal = hit.hitObject.getNormal(hit.hitPoint)
        hit.calculateReflectedRay(self)
        return hit

    def trace(self, objects: List[Sphere], back: ColorVector, i=1) -> ColorVector:
        if i >= MAX_RECURSION_DEPTH:
            return ColorVector(0, 0, 0)

        hit = self.cast(objects)

        if not hit.didHit:
            return back

        reflectColor = self.trace(objects, back, i + 1)

        returnColor = hit.hitObject.color + reflectColor * hit.hitObject.reflect
        return returnColor
