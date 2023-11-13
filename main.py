from enum import Enum
import sys
from typing import Dict, List, Literal
from sphere import Sphere
from log import log
from vector import ColorVector, Vector


SPHERE_NAME: int = 1
SPHERE_CENTER: Dict[str, int] = {"x": 2, "y": 3, "z": 4}
SPHERE_SCALE = {"x": 5, "y": 6, "z": 7}
SPHERE_RADIUS = 8
SPHERE_COLOR = {"r": 9, "g": 10, "b": 11}
SPHERE_AMBIENT = 12
SPHERE_DIFFUSE = 13
SPHERE_SPECULAR = 14
SPHERE_NSOMETHING = 15


class Main:
    fileLines: List[str] = []
    spheres: List[Sphere] = []

    def __init__(self, filename: str) -> None:
        log.debug(f"Initing new raytracer based on data in {filename}")
        self._readFile(filename)
        self._createSpheres()

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
            log.debug(f"{line.split()}")
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
        pass


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise Exception("Invalid arguments. Usage: python main.py dataFile.txt")
    runner = Main(sys.argv[1])
