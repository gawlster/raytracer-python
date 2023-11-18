from vector import ColorVector, Vector


class Light:
    name: str
    position: Vector
    color: ColorVector

    def __init__(self, name: str, position: Vector, color: ColorVector) -> None:
        self.name = name
        self.position = position
        self.color = color

    def __repr__(self) -> str:
        return f"""
Light(
    name: {self.name}
    direction: {self.position}
    color: {self.color}
)"""
