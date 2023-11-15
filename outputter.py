from typing import List
import array
from log import log
from vector import ColorVector


class Outputter:
    outFile: str
    width: int
    height: int
    _maxVal = 255
    _ppmHeader: str

    def __init__(self, outFile: str, width: int, height: int) -> None:
        self.outFile = outFile
        self.width = width
        self.height = height
        self._ppmHeader = f"P3\n{width} {height}\n{self._maxVal}\n"

    def _convertPixelArrayToPPM(self, data: List[List[ColorVector]]) -> str:
        outData = []
        for row in data:
            outRow = []
            for pixel in row:
                outRow.append(f"{pixel.r()} {pixel.g()} {pixel.b()}")
            outData.append(" ".join(outRow))

        print(len(outData))
        print(len(outData[1]))
        return "\n".join(outData)

    def writeFile(self, data: List[List[ColorVector]]):
        log.debug(f"Writing data to file {self.outFile}")
        with open("out.ppm", "wb") as out:
            out.write(bytearray(self._ppmHeader, "ascii"))
            out.write(bytearray(self._convertPixelArrayToPPM(data), "ascii"))
