from Game import Game, State
from board import Board


class game2048(Game):
    def __init__(self, board: Board = None, rows: int = 4, cols: int = 4) -> None:
        self.board = board if board else Board(rows, cols)

    def get_moves(self) -> list:
        """
        Provides possible moves as a list of w/s/a/d characters meaning up/down/left/right respectively
        """
        return list(self.board.possible_moves.values())

    def make_move(self, move: tuple) -> bool:
        """
        Returns True if move succeeded, False otherwise.

        Requires move in form of one element tuple, containing character mentioned above.

        Example: make_move('w',) will perform an upwards move.
        """

        if move[0] in self.get_moves():
            self.board.make_move(move)
            return True
        return False

    def get_state(self) -> State:
        """
        Returns game state enum:  State.{ONGOING / WON / LOST}.
        """
        return self.board.game_status()

    def get_board(self) -> list:
        """
        Returns current board state as a list of lists (rows).
        """
        return self.board.board

    def start_game(self) -> None:
        """
        Overwrites current object, invoking constructor with default values and resetting every variable.
        """
        self.board = Board()
