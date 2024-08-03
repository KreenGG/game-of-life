import sys
import pygame
import logging
from pygame.color import THECOLORS
from cell import Cell
from config import config
from logic import GameLogic
from utils import convert_to_coords


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class Game():
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((config.width, config.heigth))
        self.game_logic = GameLogic()
    
    def _draw_board(self, board: list[list[Cell]], cell_size: int) -> None:
        for row in board:
            for cell in row:
                rect = pygame.Rect(cell.x * cell_size, cell.y * cell_size, cell_size, cell_size)
                pygame.draw.rect(
                    self.screen, 
                    THECOLORS["black"] if cell.is_alive else THECOLORS["white"], 
                    rect, 
                    width=0
                )
    
    def _init_game(self):
        rows = config.rows
        cols = config.cols
        cell_size = config.cell_size
        
        board = self.game_logic.init_board(rows, cols)
        self._draw_board(board, cell_size)
        
        logger.info("Game succesfully initialized")
    

    def run(self):
        self._init_game()
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = convert_to_coords(pygame.mouse.get_pos())
                    logger.debug(f"MouseUP at {pos=}")
                    if pos[0] >= config.cols or pos[1] >= config.rows:
                        pass
                    else:
                        self.game_logic.spawn_cell(pos)

            self._draw_board(self.game_logic.get_board(), config.cell_size)
            pygame.display.flip()