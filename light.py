from vector import ColorVector, Vector


class Light:
    name: str
    direction: Vector
    color: ColorVector

    def __init__(self, name: str, direction: Vector, color: ColorVector) -> None:
        self.name = name
        self.direction = direction
        self.color = color

    def __repr__(self) -> str:
        return f"""
Light(
    name: {self.name}
    direction: {self.direction}
    color: {self.color}
)"""
