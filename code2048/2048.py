from Game import Game, State
from board import Board


class game2048(Game):
    def __init__(self, board: Board = None, rows: int = 4, cols: int = 4) -> None:
        self.board = board if board else Board(rows, cols)

    def get_moves(self) -> list:
        return list(self.board.possible_moves.values())

    def make_move(self, move: tuple) -> bool:
        if move[0] in self.get_moves():
            self.board.make_move(move)
            return True
        return False

    def get_state(self) -> State:
        return self.board.game_status()

    def get_board(self) -> list:
        return self.board.board

    def start_game(self) -> None:
        self.board = Board()
