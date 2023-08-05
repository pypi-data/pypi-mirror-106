from .exceptions import DiskFullError
from .file import File
from .relative_file import RelativeFile
from .super_side_sector import SuperSideSector


class D81RelativeFile(RelativeFile):
    def get_first_block(self):
        data_block = File.get_first_block(self)
        side_sector = self.get_first_side_sector(data_block)
        if side_sector is None:
            self.image.free_block(data_block)
            raise DiskFullError()

        block = self.image.alloc_next_block(side_sector.track, side_sector.sector)
        if block is None:
            self.image.free_block(data_block)
            self.image.free_block(side_sector)
            raise DiskFullError()

        super_side_sector = SuperSideSector(self.image, block.track, block.sector)
        super_side_sector.clear_side_sectors()
        super_side_sector.set_next_block(side_sector)
        super_side_sector.add_side_sector(side_sector)
        self.entry.side_sector_ts = (super_side_sector.track, super_side_sector.sector)
        self.entry.size += 1
        return data_block
