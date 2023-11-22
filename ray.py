from __future__ import annotations
import math
from typing import Any, List

from numpy import Infinity
from vector import Vector, ColorVector


MAX_RECURSION_DEPTH = 3


class Hit:
    didHit: bool
    hitDistance: float
    hitPoint: Vector
    hitNormal: Vector
    reflectRay: Ray

    hitObject: Any

    def __init__(self) -> None:
        self.didHit = False

    def calculateReflectedRay(self, origRay: Ray) -> None:
        from ray import Ray

        origin = self.hitPoint + self.hitNormal * 0.001
        direction = origRay.direction - self.hitNormal * 2 * origRay.direction.dot(
            self.hitNormal
        )
        self.reflectRay = Ray(origin, direction)


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
        if hit.didHit:
            hit.hitNormal = hit.hitObject.getNormal(hit.hitPoint)
            hit.calculateReflectedRay(self)
        return hit

    def trace(
        self, objects: List, lights: List, back: ColorVector, ambient: ColorVector, i=1
    ) -> ColorVector:
        if i >= MAX_RECURSION_DEPTH:
            return ColorVector(0, 0, 0)

        hit = self.cast(objects)

        if not hit.didHit:
            if i == 1:
                return back
            else:
                return ColorVector(0, 0, 0)

        ambientColor = ambient * hit.hitObject.color * hit.hitObject.ambient

        shadowColor = ColorVector(0, 0, 0)
        for light in lights:
            L = light.position - hit.hitPoint
            R = hit.hitNormal * 2 * (hit.hitNormal.dot(L)) - L
            shadowColor += (
                light.color
                * hit.hitObject.color
                * hit.hitObject.diffuse
                * (hit.hitNormal.dot(L))
            ) + (
                light.color
                * hit.hitObject.specular
                * R.dot(-self.direction) ** 0.5
                # * hit.hitObject.nSomething
            )

        # reflectColor = hit.reflectRay.trace(objects, lights, back, ambient, i + 1)

        return ambientColor + shadowColor
