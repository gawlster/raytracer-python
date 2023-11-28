from __future__ import annotations
from typing import Any, List

from numpy import Infinity
from vector import Vector, ColorVector
from log import log


MAX_RECURSION_DEPTH = 3


class Hit:
    didHit: bool
    isInsideSphere: bool
    hitDistance: float = Infinity
    hitPoint: Vector = Vector(Infinity, Infinity, Infinity)
    hitNormal: Vector = Vector(Infinity, Infinity, Infinity)

    hitObject: Any = None

    def __init__(self) -> None:
        self.didHit = False
        self.isInsideSphere = False

    def __repr__(self) -> str:
        return f"""
Hit(
    didHit: {self.didHit},
    hitDistance: {self.hitDistance}
    hitPoint: {self.hitPoint}
    hitNormal: {self.hitNormal}
    hitObject: {self.hitObject}
)
"""


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

    def cast(self, spheres: List, isShadowRay=False) -> Hit:
        hit = Hit()
        hit.hitDistance = Infinity
        for sphere in spheres:
            intersectPoint, intersectDistance, isInsideSphere = sphere.intersection(
                self, isShadowRay
            )
            if type(intersectPoint) == Vector and intersectDistance < hit.hitDistance:
                hit.didHit = True
                hit.isInsideSphere = isInsideSphere
                hit.hitDistance = intersectDistance
                hit.hitPoint = intersectPoint
                hit.hitObject = sphere
        if hit.didHit:
            hit.hitNormal = hit.hitObject.getNormal(hit.hitPoint, hit.isInsideSphere)
        return hit

    def _getAmbientColor(self, ambient: ColorVector, hit: Hit):
        return ambient * hit.hitObject.color * hit.hitObject.ambient

    def _getDiffuseColor(self, light, hit: Hit) -> ColorVector:
        L = (light.position - hit.hitPoint).normalize()
        return (
            hit.hitObject.color
            * light.color
            * hit.hitObject.diffuse
            * hit.hitNormal.dot(L)
        )

    def _reflect(self, I: Vector, N: Vector) -> Vector:
        return I - N * 2.0 * N.dot(I)

    def _getSpecularColor(self, light, hit: Hit):
        N = hit.hitNormal
        L = (light.position - hit.hitPoint).normalize()
        V = -hit.hitPoint.normalize()

        R = self._reflect(-L, N)
        try:
            reflectedDotViewShiny = max(R.dot(V), 0.0) ** hit.hitObject.nExponent
        except OverflowError:
            log.error(
                f"Caught overflow error calculating reflectedDotViewShiny: R: {R}, V: {V}, exp: {hit.hitObject.nExponent}"
            )
            reflectedDotViewShiny = 0.0

        return light.color * hit.hitObject.specular * reflectedDotViewShiny

    def trace(
        self, objects: List, lights: List, back: ColorVector, ambient: ColorVector, i=1
    ) -> ColorVector:
        if i > MAX_RECURSION_DEPTH:
            return ColorVector(0, 0, 0)

        hit = self.cast(objects)

        if not hit.didHit:
            if i == 1:
                return back
            else:
                return ColorVector(0, 0, 0)

        ambientColor = self._getAmbientColor(ambient, hit)

        diffuseColor = ColorVector(0, 0, 0)
        specularColor = ColorVector(0, 0, 0)
        for light in lights:
            shadowRay = Ray(hit.hitPoint, (light.position - hit.hitPoint).normalize())
            shadowHit = shadowRay.cast(objects, True)

            if True or not shadowHit.didHit:
                diffuseColor += self._getDiffuseColor(light, hit)
                specularColor += self._getSpecularColor(light, hit)

        reflectRayDir = self._reflect(self.direction.normalize(), hit.hitNormal)
        reflectRay = Ray(hit.hitPoint, reflectRayDir)
        reflectColor = (
            reflectRay.trace(objects, lights, back, ambient, i + 1)
            * hit.hitObject.reflect
        )

        # return ambientColor + diffuseColor
        return ambientColor + diffuseColor + specularColor + reflectColor
