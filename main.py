import array
import sys
from typing import Dict, List, Tuple
from light import Light
from outputter import Outputter
from sphere import Sphere
from log import log
from vector import ColorVector, Vector


SPHERE_NAME = 1
SPHERE_CENTER = {"x": 2, "y": 3, "z": 4}
SPHERE_SCALE = {"x": 5, "y": 6, "z": 7}
SPHERE_RADIUS = 8
SPHERE_COLOR = {"r": 9, "g": 10, "b": 11}
SPHERE_AMBIENT = 12
SPHERE_DIFFUSE = 13
SPHERE_SPECULAR = 14
SPHERE_NSOMETHING = 15

LIGHT_NAME = 1
LIGHT_POSITION = {"x": 2, "y": 3, "z": 4}
LIGHT_COLOR = {"r": 5, "g": 6, "b": 7}


class Main:
    fileLines: List[str] = []
    spheres: List[Sphere] = []
    lights: List[Light] = []

    near: int
    left: int
    right: int
    bottom: int
    top: int
    resolution: Tuple[int, int]
    back: Tuple[int, int, int]
    ambient: Tuple[float, float, float]
    outFile: str

    pixels: List[List[ColorVector]]

    def __init__(self, filename: str) -> None:
        log.debug(f"Initing new raytracer based on data in {filename}")
        self._readFile(filename)
        self._createSpheres()
        self._createLights()
        self._getMiscValues()
        self.pixels = [
            [ColorVector(1, 0, 0) for _ in range(self.resolution[0])]
            for _ in range(self.resolution[1])
        ]
        outputter = Outputter(self.outFile, self.resolution[0], self.resolution[1])
        outputter.writeFile(self.pixels)

    def _setMiscValue(self, key, value) -> None:
        match key:
            case "NEAR":
                self.near = int(value.split().pop())
            case "LEFT":
                self.left = int(value.split().pop())
            case "RIGHT":
                self.right = int(value.split().pop())
            case "BOTTOM":
                self.bottom = int(value.split().pop())
            case "TOP":
                self.top = int(value.split().pop())
            case "RES":
                self.resolution = (
                    int(value.split().pop()),
                    int(value.split().pop()),
                )
            case "BACK":
                self.back = (
                    int(value.split().pop()),
                    int(value.split().pop()),
                    int(value.split().pop()),
                )
            case "AMBIENT":
                self.ambient = (
                    float(value.split().pop()),
                    float(value.split().pop()),
                    float(value.split().pop()),
                )
            case "OUTPUT":
                self.outFile = value.split().pop()
            case _:
                pass

    def _readFile(self, filename: str) -> None:
        with open(filename, "r") as fd:
            self.fileLines = fd.readlines()
            for i, line in enumerate(self.fileLines):
                self.fileLines[i] = line.rstrip()

        log.debug(f"Read file into list: {log.formatListForString(self.fileLines)}")

    def _createSpheres(self) -> None:
        log.debug("Creating spheres")
        for line in self.fileLines:
            if not line.startswith("SPHERE "):
                continue
            data = line.split()
            self.spheres.append(
                Sphere(
                    data[SPHERE_NAME],
                    Vector(
                        float(data[SPHERE_CENTER["x"]]),
                        float(data[SPHERE_CENTER["y"]]),
                        float(data[SPHERE_CENTER["z"]]),
                    ),
                    Vector(
                        float(data[SPHERE_SCALE["x"]]),
                        float(data[SPHERE_SCALE["y"]]),
                        float(data[SPHERE_SCALE["z"]]),
                    ),
                    float(data[SPHERE_RADIUS]),
                    ColorVector(
                        float(data[SPHERE_COLOR["r"]]),
                        float(data[SPHERE_COLOR["g"]]),
                        float(data[SPHERE_COLOR["b"]]),
                    ),
                    float(data[SPHERE_AMBIENT]),
                    float(data[SPHERE_DIFFUSE]),
                    float(data[SPHERE_SPECULAR]),
                    float(data[SPHERE_NSOMETHING]),
                )
            )

        log.debug(f"Spheres list: {self.spheres}")

    def _createLights(self) -> None:
        log.debug("Creating lights")
        for line in self.fileLines:
            if not line.startswith("LIGHT "):
                continue
            data = line.split()
            self.lights.append(
                Light(
                    data[LIGHT_NAME],
                    Vector(
                        float(data[LIGHT_POSITION["x"]]),
                        float(data[LIGHT_POSITION["y"]]),
                        float(data[LIGHT_POSITION["z"]]),
                    ),
                    ColorVector(
                        float(data[LIGHT_COLOR["r"]]),
                        float(data[LIGHT_COLOR["g"]]),
                        float(data[LIGHT_COLOR["b"]]),
                    ),
                )
            )

        log.debug(f"Lights list: {self.lights}")

    def _getMiscValues(self) -> None:
        valuesStillToGet = [
            "NEAR",
            "LEFT",
            "RIGHT",
            "BOTTOM",
            "TOP",
            "RES",
            "BACK",
            "AMBIENT",
            "OUTPUT",
        ]

        for line in self.fileLines:
            for value in valuesStillToGet:
                if line.startswith(value):
                    self._setMiscValue(value, line)
                    valuesStillToGet.remove(value)

        log.debug(
            f"""Got misc scene values:
[
    near: {self.near},
    left: {self.left},
    right: {self.right},
    bottom: {self.bottom},
    top: {self.top},
    resolution: {self.resolution},
    back: {self.back},
    ambient: {self.ambient},
    outFile: {self.outFile}
]"""
        )


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise Exception("Invalid arguments. Usage: python main.py dataFile.txt")
    runner = Main(sys.argv[1])
