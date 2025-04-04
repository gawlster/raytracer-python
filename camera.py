from math import log, tan, radians
from typing import Tuple
from ray import Ray
from vector import Vector


class Camera:
    position = Vector(0, 0, 0)
    screenSize: Vector
    fov = 120

    def __init__(self, resolution: Tuple[int, int]) -> None:
        self.screenSize = Vector(resolution[0], resolution[1], 0)

    def getDirection(self, vec: Vector) -> Ray:
        x = self.screenSize.x / 2 * ((2 * vec.x / self.screenSize.x) - 1)
        y = self.screenSize.y / 2 * ((2 * vec.y / self.screenSize.y) - 1)
        z = self.screenSize.y / tan(radians(self.fov) / 2)
        return Ray(self.position, Vector(x, -y, -z).normalize())
