from __future__ import annotations
from typing import Tuple
from math import sqrt
from numpy import clip
from log import log


class Vector:
    x: float
    y: float
    z: float

    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self) -> str:
        return f"Vector(x: {self.x}, y: {self.y}, z: {self.z})"

    def __add__(self, addend: Vector | float) -> Vector:
        if type(addend) == int or type(addend) == float:
            return Vector(self.x + addend, self.y + addend, self.z + addend)
        elif type(addend) == Vector:
            return Vector(self.x + addend.x, self.y + addend.y, self.z + addend.z)
        log.warn("You are adding a vector with an unsupported variable type!")
        return self

    def __sub__(self, subtrahend: Vector | float) -> Vector:
        if type(subtrahend) == int or type(subtrahend) == float:
            return Vector(self.x - subtrahend, self.y - subtrahend, self.z - subtrahend)
        elif type(subtrahend) == Vector:
            return Vector(
                self.x - subtrahend.x, self.y - subtrahend.y, self.z - subtrahend.z
            )
        log.warn("You are subtracting a vector with an unsupported variable type!")
        return self

    def __mul__(self, factor: Vector | float) -> Vector:
        if type(factor) == int or type(factor) == float:
            return Vector(self.x * factor, self.y * factor, self.z * factor)
        elif type(factor) == Vector:
            return Vector(self.x * factor.x, self.y * factor.y, self.z * factor.z)
        log.warn("You are multiplying a vector with an unsupported variable type!")
        return self

    def __truediv__(self, divisor: Vector | float) -> Vector:
        if type(divisor) == int or type(divisor) == float:
            return Vector(
                self.x / (divisor + 0.00000001),
                self.y / (divisor + 0.00000001),
                self.z / (divisor + 0.00000001),
            )
        elif type(divisor) == Vector:
            return Vector(
                self.x / (divisor.x + 0.00000001),
                self.y / (divisor.y + 0.00000001),
                self.z / (divisor.z + 0.00000001),
            )
        log.warn("You are dividing a vector with an unsupported variable type!")
        return self

    def __pow__(self, exponent: Vector | float) -> Vector:
        if type(exponent) == int or type(exponent) == float:
            return Vector(self.x**exponent, self.y**exponent, self.z**exponent)
        elif type(exponent) == Vector:
            return Vector(
                self.x**exponent.x, self.y**exponent.y, self.z**exponent.z
            )
        log.warn("You are powering a vector with an unsupported variable type!")
        return self

    def __gt__(self, other: Vector | float) -> bool:
        if type(other) == int or type(other) == float:
            return self.magnitude() > other
        if type(other) == Vector:
            return self.magnitude() > other.magnitude()
        log.warn("You are comparing a vector with an unsupported variable type!")
        return False

    def __lt__(self, other: Vector | float) -> bool:
        if type(other) == int or type(other) == float:
            return self.magnitude() < other
        if type(other) == Vector:
            return self.magnitude() < other.magnitude()
        log.warn("You are comparing a vector with an unsupported variable type!")
        return False

    def __gte__(self, other: Vector | float) -> bool:
        if type(other) == int or type(other) == float:
            return self.magnitude() >= other
        if type(other) == Vector:
            return self.magnitude() >= other.magnitude()
        log.warn("You are comparing a vector with an unsupported variable type!")
        return False

    def __lte__(self, other: Vector | float) -> bool:
        if type(other) == int or type(other) == float:
            return self.magnitude() <= other
        if type(other) == Vector:
            return self.magnitude() <= other.magnitude()
        log.warn("You are comparing a vector with an unsupported variable type!")
        return False

    def __eq__(self, other: object) -> bool:
        if (
            not isinstance(other, Vector)
            and not isinstance(other, int)
            and not isinstance(other, float)
        ):
            return NotImplemented
        if type(other) == int or type(other) == float:
            return self.magnitude() == other
        if type(other) == Vector:
            return self.magnitude() == other.magnitude()
        log.warn("You are comparing a vector with an unsupported variable type!")
        return False

    def __neg__(self) -> Vector:
        return Vector(-self.x, -self.y, -self.z)

    def __pos__(self) -> Vector:
        return Vector(+self.x, +self.y, +self.z)

    def __float__(self) -> float:
        return float(self.magnitude())

    def __int__(self) -> int:
        return int(self.magnitude())

    def dot(self, factor: Vector | float) -> float:
        if type(factor) == int or type(factor) == float:
            return self.x * factor + self.y * factor + self.z * factor
        elif type(factor) == Vector:
            return self.x * factor.x + self.y * factor.y + self.z * factor.z
        log.warn("You are multiplying a vector with an unsupported variable type!")
        return self.x + self.y + self.z

    def cross(self, factor: Vector) -> Vector:
        return Vector(
            (self.y * factor.z) - (self.z * factor.y),
            (self.z * factor.x) - (self.x * factor.z),
            (self.x * factor.y) - (self.y * factor.x),
        )

    def magnitude(self) -> float:
        return sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def normalize(self) -> Vector:
        return self / self.magnitude()

    def reflect(self, normal: Vector) -> Vector:
        return self - normal * (self.dot(normal)) * 2


class ColorVector(Vector):
    def r(self) -> float:
        return int(clip(self.x, 0, 1) * 255)

    def g(self) -> float:
        return int(clip(self.y, 0, 1) * 255)

    def b(self) -> float:
        return int(clip(self.z, 0, 1) * 255)

    def __repr__(self) -> str:
        return f"""
ColorVector(
    r: {self.r()}
    g: {self.g()}
    b: {self.b()}
)"""

    def __add__(self, addend: Vector | ColorVector | float) -> ColorVector:
        if type(addend) == int or type(addend) == float:
            return ColorVector(self.x + addend, self.y + addend, self.z + addend)
        elif type(addend) == Vector or type(addend) == ColorVector:
            return ColorVector(self.x + addend.x, self.y + addend.y, self.z + addend.z)
        log.warn("You are adding a vector with an unsupported variable type!")
        return self

    def __mul__(self, factor: Vector | ColorVector | float | int) -> ColorVector:
        if type(factor) == int or type(factor) == float:
            return ColorVector(self.x * factor, self.y * factor, self.z * factor)
        elif type(factor) == Vector or type(factor) == ColorVector:
            return ColorVector(self.x * factor.x, self.y * factor.y, self.z * factor.z)
        log.warn("You are multiplying a vector with an unsupported variable type!")
        return self

    def isSameColor(self, other: ColorVector):
        return self.r() == other.r() and self.g() == other.g() and self.b() == other.b()
