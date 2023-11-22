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

        origin = self.hitPoint + self.hitNormal * 0.0001
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

        pixelColor = ColorVector(0, 0, 0)
        for light in lights:
            lightVector = (light.position - hit.hitPoint).normalize()
            cosTheta = hit.hitPoint.normalize().dot(lightVector)
            if cosTheta <= 0.0:
                cosTheta = 0.0

            pixelColor += hit.hitObject.color * hit.hitObject.diffuse * cosTheta

            incomingVector = (hit.hitPoint - light.position).normalize()
            myDot = incomingVector.dot(hit.hitNormal.normalize())
            myLen = 2.0 * myDot

            tempNormal = hit.hitNormal.normalize() * myLen
            reflect = (tempNormal + incomingVector).normalize()

            mySpec = max(-reflect.dot(incomingVector), 0)
            mySpec = mySpec**50
            specularColor = hit.hitObject.color * hit.hitObject.specular * mySpec
            pixelColor += specularColor

        reflectColor = (
            hit.reflectRay.trace(objects, lights, back, ambient, i + 1)
            * hit.hitObject.reflect
        )

        return ambientColor + pixelColor + reflectColor
