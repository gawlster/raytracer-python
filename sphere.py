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
        nSomething: float,
    ) -> None:
        self.name = name
        self.center = center
        self.scale = scale
        self.color = color
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
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
        l = self.center - ray.origin
        adj = l.dot(ray.direction)
        d2 = l.dot(l) - (adj * adj)
        radius2 = self.radius * self.radius
        if d2 > radius2:
            return False
        thc = sqrt(radius2 - d2)
        t0 = adj - thc
        t1 = adj + thc
        if t0 < 0 and t1 < 0:
            return False
        distance = t0 if t0 < t1 else t1
        return ray.origin + ray.direction * distance

    def getNormal(self, hitPosition: Vector):
        return (hitPosition - self.center).normalize()
