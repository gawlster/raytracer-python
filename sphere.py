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
    nSomething: float

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
        nSomething: float,
    ) -> None:
        self.name = name
        self.center = center
        self.scale = scale
        self.color = color
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.reflect = reflect
        self.nSomething = nSomething

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
    nSomething: {self.nSomething}
)"""

    def intersection(self, ray: Ray) -> Tuple[Vector, float] | Tuple[bool, bool]:
        # todo
        newRayDir = Vector(
            ray.direction.x / self.scale.x,
            ray.direction.y / self.scale.y,
            ray.direction.z / self.scale.z,
        )
        newRayOrigin = Vector(
            ray.origin.x - self.center.x / self.scale.x,
            ray.origin.y - self.center.y / self.scale.y,
            ray.origin.z - self.center.z / self.scale.z,
        )
        a = newRayDir.dot(newRayDir)
        b = 2 * newRayOrigin.dot(newRayDir)
        c = newRayOrigin.dot(newRayOrigin) - 1

        discriminant = b * b - 4 * a * c
        if discriminant <= 0:
            return False, False

        nearestIntersectionDistance = (-b - sqrt(discriminant)) / (2 * a)
        if nearestIntersectionDistance >= 0:
            return (
                Vector(
                    ray.origin.x + nearestIntersectionDistance * ray.direction.x,
                    ray.origin.y + nearestIntersectionDistance * ray.direction.y,
                    ray.origin.z + nearestIntersectionDistance * ray.direction.z,
                ),
                nearestIntersectionDistance,
            )

        return False, False

    def getNormal(self, hitPosition: Vector):
        return Vector(
            hitPosition.x - self.center.x / self.scale.x,
            hitPosition.y - self.center.y / self.scale.y,
            -1 * (hitPosition.z - self.center.z / self.scale.z),
        ).normalize()
