from typing import Any
from vector import Vector


class Hit:
    didHit: bool
    hitDistance: float
    hitPoint: Vector
    hitNormal: Vector
    reflectRay: Any

    hitObject: Any

    def __init__(self) -> None:
        self.didHit = False

    def calculateReflectedRay(self, origRay: Any) -> None:
        from ray import Ray

        origin = self.hitPoint + self.hitNormal * 0.001
        direction = origRay.direction - self.hitNormal * 2 * origRay.direction.dot(
            self.hitNormal
        )
        self.reflectVector = Ray(origin, direction)
