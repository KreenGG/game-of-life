from math import floor
from config import config
import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def convert_to_coords(pos: tuple):
    converted_coords = (floor(pos[0] / config.cell_size), floor(pos[1] / config.cell_size))
    logger.debug(f"Converted {pos=} in {converted_coords}")
    return converted_coords