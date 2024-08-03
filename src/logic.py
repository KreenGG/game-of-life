import logging

from cell import Cell

logger = logging.getLogger(__name__)


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

    def get_board(self) -> list[list[Cell]]:
        return self.board

    def spawn_cell(self, pos: tuple[int, int]):
        cell: Cell = self.board[pos[1]][pos[0]]
        cell.make_alive()
        logger.debug(f"Cell spawned at x = {pos[0]}, y = {pos[1]}")
