import logging
import random
from copy import copy

from cell import Cell

logger = logging.getLogger(__name__)
logger.level = logging.DEBUG


class GameLogic:
    def __init__(self) -> None:
        self.board: list[list[Cell]] = [[]]

    def init_board(self, rows: int, cols: int) -> list[list[Cell]]:
        for row in range(0, rows):
            self.board.append([])
            for col in range(0, cols):
                self.board[row].append(Cell(col, row))
        logger.info("Board initialized succesfully")
        return self.board

    def random_board(self, density: float) -> list[list[Cell]]:
        for row in self.board:
            for cell in row:
                if random.uniform(0, 1) < density:
                    cell.make_alive()
        return self.board

    def get_board(self) -> list[list[Cell]]:
        return self.board

    def check_neighbours(self, cell: Cell) -> int:
        # TODO: Отрефакторить этот ужас

        neighbours_count = 0

        x = cell.x
        y = cell.y

        try:
            neighbours_count += 1 if self.board[y - 1][x - 1].is_alive else 0
        except IndexError:
            ...

        try:
            neighbours_count += 1 if self.board[y - 1][x].is_alive else 0
        except IndexError:
            ...

        try:
            neighbours_count += 1 if self.board[y - 1][x + 1].is_alive else 0
        except IndexError:
            ...

        try:
            neighbours_count += 1 if self.board[y][x - 1].is_alive else 0
        except IndexError:
            ...

        try:
            neighbours_count += 1 if self.board[y][x + 1].is_alive else 0
        except IndexError:
            ...

        try:
            neighbours_count += 1 if self.board[y + 1][x - 1].is_alive else 0
        except IndexError:
            ...

        try:
            neighbours_count += 1 if self.board[y + 1][x].is_alive else 0
        except IndexError:
            ...

        try:
            neighbours_count += 1 if self.board[y + 1][x + 1].is_alive else 0
        except IndexError:
            ...

        return neighbours_count

    def get_next_board(self) -> list[list[Cell]]:
        next_board : list[list[Cell]] = [[]]

        for y ,row in enumerate(self.board):
            next_board.append([])
            for _, cell in enumerate(row):
                next_board[y].append(copy(cell))


        for row in next_board:
            for cell in row:
                neighbours_count = self.check_neighbours(cell)

                if cell.is_alive and neighbours_count not in (2, 3):
                    cell.make_dead()
                elif not cell.is_alive and neighbours_count == 3:
                    cell.make_alive()

        self.board = next_board.copy()
        return self.board

    def spawn_cell(self, pos: tuple[int, int]):
        self.board[pos[1]][pos[0]].make_alive()
        cell = self.board[pos[1]][pos[0]]
        logger.debug(f"{cell} spawned")
