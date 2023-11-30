from math import sqrt
from light import Light
from ray import Ray
from vector import Vector, ColorVector
from typing import Tuple


class Sphere:
    name: str
    center: Vector
    scale: Vector
    color: ColorVector
    ambient: float
    diffuse: float
    specular: float
    reflect: float
    nExponent: float
    nearPlane: float

    def __init__(
        self,
        name: str,
        center: Vector,
        scale: Vector,
        color: ColorVector,
        ambient: float,
        diffuse: float,
        specular: float,
        reflect: float,
        nExponent: float,
        nearPlane: float,
    ) -> None:
        self.name = name
        self.center = center
        self.scale = scale
        self.color = color
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.reflect = reflect
        self.nExponent = nExponent
        self.nearPlane = nearPlane

    def __repr__(self) -> str:
        return f"""
Sphere(
    name: {self.name}
    center: {self.center}
    scale: {self.scale}
    color: {self.color}
    ambient: {self.ambient}
    diffuse: {self.diffuse}
    specular: {self.specular}
    nExponent: {self.nExponent}
)"""

    def intersection(
        self, ray: Ray, light: Light
    ) -> Tuple[Vector, float, bool] | Tuple[bool, bool, bool]:
        isInsideSphere = False
        transformedRayDir = ray.direction / self.scale
        transformedRayOrigin = (ray.origin - self.center) / self.scale
        a = transformedRayDir.dot(transformedRayDir)
        b = 2 * transformedRayOrigin.dot(transformedRayDir)
        c = transformedRayOrigin.dot(transformedRayOrigin) - 1

        discriminant = b * b - 4 * a * c
        if discriminant <= 0:
            return False, False, False

        t1 = (-b - sqrt(discriminant)) / (2 * a)
        t2 = (-b + sqrt(discriminant)) / (2 * a)

        t = min(t1, t2)

        if ray.isShadowRay:
            if (t1 > 0 and t1 < light.position - ray.origin) or (
                t2 > 0 and t2 < light.position - ray.origin
            ):
                # return value doesn't matter, just needs to count as a hit
                return ray.origin, 1, ray.isInsideSphere
            return False, False, False

        if (ray.origin + ray.direction * t).z > -self.nearPlane:
            t = max(t1, t2)
            isInsideSphere = True
        else:
            isInsideSphere = ray.isShadowRay

        if t < 0.0001:
            return False, False, False

        return (ray.origin + ray.direction * t, t, isInsideSphere)

    def getNormal(self, hitPosition: Vector, isInsideSphere: bool) -> Vector:
        transformedHitPoint = (
            (hitPosition - self.center) / self.scale**2
        ).normalize()
        return transformedHitPoint if not isInsideSphere else -transformedHitPoint
