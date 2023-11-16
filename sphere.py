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
        # rayOrigin = ray.origin - self.center
        # rayDirection = ray.direction.normalize()
        #
        # a = (
        #     ((rayDirection.x * rayDirection.x) / (self.scale.x * self.scale.x))
        #     + ((rayDirection.y * rayDirection.y) / (self.scale.y * self.scale.y))
        #     + ((rayDirection.z * rayDirection.z) / (self.scale.z * self.scale.z))
        # )
        # b = (
        #     ((2 * rayOrigin.x * rayDirection.x) / (self.scale.x * self.scale.x))
        #     + ((2 * rayOrigin.y * rayDirection.y) / (self.scale.y * self.scale.y))
        #     + ((2 * rayOrigin.z * rayDirection.z) / (self.scale.z * self.scale.z))
        # )
        # c = (
        #     ((rayOrigin.x * rayOrigin.x) / (self.scale.x * self.scale.x))
        #     + ((rayOrigin.y * rayOrigin.y) / (self.scale.y * self.scale.y))
        #     + ((rayOrigin.z * rayOrigin.z) / (self.scale.z * self.scale.z))
        #     - 1
        # )
        #
        # d = (b * b) - (4 * a * c)
        # if d < 0:
        #     return False
        #
        # intersect = Vector(
        #     self.center.x + d * rayDirection.x,
        #     self.center.y + d * rayDirection.y,
        #     self.center.z + d * rayDirection.z,
        # )
        # print(intersect)

        # Need to return the hitpoint here
        # return intersect

        l = self.center - ray.origin
        # inverse the scale transforms here??
        adj = l.dot(ray.direction / self.scale)
        d2 = l.dot(l) - (adj * adj)
        # radius2 = self.radius * self.radius
        # the 100 is wrong
        if d2 > 100:
            print(d2)
            # if d2 > radius2:
            # behind the camera
            return False
        thc = sqrt(100 - d2)
        # t0 and t1 are the intersections, return the one closest to ray origin
        t0 = adj - thc
        t1 = adj + thc
        # if there is not 2 intersections, return false
        if t0 < 0 and t1 < 0:
            return False
        distance = t0 if t0 < t1 else t1
        return ray.origin + ray.direction * self.scale * distance

    def getNormal(self, hitPosition: Vector):
        return (hitPosition - self.center).normalize()
