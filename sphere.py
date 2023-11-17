from math import sqrt
from ray import Ray
from vector import Vector, ColorVector


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

    def intersection(self, ray: Ray) -> Vector | bool:
        offsetRayOrigin = ray.origin - self.center
        a = ray.direction.dot(ray.direction)
        b = 2 * offsetRayOrigin.dot(ray.direction)
        c = offsetRayOrigin.dot(offsetRayOrigin) - 1

        discriminant = b * b - 4 * a * c
        if discriminant <= 0:
            return False

        nearestIntersection = (-b - sqrt(discriminant)) / (2 * a)
        if nearestIntersection >= 0:
            return Vector(0, 0, 0)

        return False

    def getNormal(self, hitPosition: Vector):
        return (hitPosition - self.center).normalize()
