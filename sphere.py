from math import sqrt
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
        self, ray: Ray, isShadowRay: bool
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

        nearestIntersectionDistance = (-b - sqrt(discriminant)) / (2 * a)
        intersectionPoint = ray.origin + ray.direction * nearestIntersectionDistance
        if not isShadowRay and intersectionPoint.z > -1:
            isInsideSphere = True
            nearestIntersectionDistance = (-b + sqrt(discriminant)) / (2 * a)
            intersectionPoint = ray.origin + ray.direction * nearestIntersectionDistance
        if nearestIntersectionDistance >= 0.0001:
            return (intersectionPoint, nearestIntersectionDistance, isInsideSphere)

        return False, False, False

    def getNormal(self, hitPosition: Vector, isInsideSphere: bool) -> Vector:
        transformedHitPoint = (hitPosition - self.center) / self.scale
        return transformedHitPoint if not isInsideSphere else -transformedHitPoint
