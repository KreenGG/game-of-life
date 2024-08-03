from dataclasses import dataclass
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@dataclass
class Cell:
    x: int
    y: int
    is_alive: bool = False
    
    def make_alive(self) -> None:
        self.is_alive = True
        logger.debug(f"Cell made alive at x = {self.x}, y = {self.y}")
    
    def make_dead(self) -> None:
        self.is_alive = False
        print(self.x, self.y, self.is_alive)
        