import struct

from .block import Block
from .exceptions import FileIndexError


class SuperSideSector(Block):
    """Relative file super side sector block (1581)."""
    MAX_SIDE_SECTOR_LINKS = 126

    def clear_side_sectors(self):
        self.set(2, 0xfe)
        self.set(3, bytes(0xfd))

    def add_side_sector(self, side_sector):
        for idx in range(0, self.MAX_SIDE_SECTOR_LINKS*2, 2):
            if self.get(idx+3) == 0:
                self.set(idx+3, struct.pack('<BB', side_sector.track, side_sector.sector))
                return

        raise FileIndexError("Super side sector full")
