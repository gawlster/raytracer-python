from vector import Vector, ColorVector


class Sphere:
    center: Vector
    radius: int | float
    color: ColorVector

    def __init__(self, center: Vector, radius: int | float, color: ColorVector) -> None:
        self.center = center
        self.radius = radius
        self.color = color
