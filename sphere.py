from vector import Vector, ColorVector


class Sphere:
    name: str
    center: Vector
    scale: Vector
    radius: float
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
        radius: float,
        color: ColorVector,
        ambient: float,
        diffuse: float,
        specular: float,
        nSomething: float,
    ) -> None:
        self.name = name
        self.center = center
        self.scale = scale
        self.radius = radius
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
    radius: {self.radius}
    color: {self.color}
    ambient: {self.ambient}
    diffuse: {self.diffuse}
    specular: {self.specular}
    nSomething: {self.nSomething}
)"""
