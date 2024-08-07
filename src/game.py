import logging
import sys

import pygame
from cell import Cell
from config import config
from logic import GameLogic
from pygame.color import THECOLORS
from pygame.event import Event
from utils import convert_to_coords

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((config.width, config.heigth))
        self.game_logic = GameLogic()
        self.is_started = False

    def _draw_board(self, board: list[list[Cell]], cell_size: int) -> None:
        for row in board:
            for cell in row:
                rect = pygame.Rect(
                    cell.x * cell_size, cell.y * cell_size, cell_size, cell_size
                )
                pygame.draw.rect(
                    self.screen,
                    THECOLORS["black"] if cell.is_alive else THECOLORS["white"],
                    rect,
                    width=0,
                )
        pygame.display.flip()

    def _draw_start_button(self) -> None:
        x = config.width - 100
        y = 10
        width = 90
        height = 50

        self.start_button = pygame.Rect(
            x, y, width, height
        )

        pygame.draw.rect(
            self.screen,
            THECOLORS["yellow"],
            self.start_button,
        )
        pygame.display.flip()

    def _draw_next_step_button(self):
        x = config.width - 100
        y = 100
        width = 90
        height = 50

        self.next_step_button = pygame.Rect(
            x, y, width, height
        )

        pygame.draw.rect(
            self.screen,
            THECOLORS["red"],
            self.next_step_button,
        )
        pygame.display.flip()

    def _init_game(self):
        rows = config.rows
        cols = config.cols
        cell_size = config.cell_size

        board = self.game_logic.init_board(rows, cols)
        self.game_logic.random_board(config.density)

        self._draw_board(board, cell_size)
        self._draw_start_button()
        self._draw_next_step_button()

        pygame.display.flip()
        logger.info("Game succesfully initialized")

    def _change_game_state(self):
        self.is_started = not self.is_started
        if self.is_started:
            logger.info("Game started")
        else:
            logger.info("Game stopped")

    def _handle_event(self, event: Event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Spawn cell event handler
        if event.type == pygame.MOUSEBUTTONUP:
            pos = convert_to_coords(pygame.mouse.get_pos())
            if pos[0] >= config.cols or pos[1] >= config.rows:
                pass
            else:
                self.game_logic.spawn_cell(pos)
                pygame.display.flip()

        # Start game event handler
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.start_button.collidepoint(event.pos):
                self._change_game_state()

        # Next step event handler
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.next_step_button.collidepoint(event.pos):
                self._update_game()

    def _update_game(self):
        next_board = self.game_logic.get_next_board()
        self._draw_board(next_board, config.cell_size)
        pygame.display.flip()

    def run(self):
        self._init_game()
        while True:
            for event in pygame.event.get():
                self._handle_event(event)

            if self.is_started:
                self._update_game()
            else:
                self._draw_board(self.game_logic.get_board(), config.cell_size)
