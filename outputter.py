import array
from log import log


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
        self._ppmHeader = f"P6 {width} {height} {self._maxVal}\n"

    def writeFile(self, data: array.ArrayType):
        log.debug(f"Writing data to file {self.outFile}")
        with open("out.ppm", "wb") as out:
            out.write(bytearray(self._ppmHeader, "ascii"))
            data.tofile(out)
