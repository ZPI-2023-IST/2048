from node import Node
import random
from enum import Enum


class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

class State(Enum):
    ONGOING = 0
    WON = 1
    LOST = 2

class Board:
    def __init__(self, rows=4, columns=4):
        self.rows = rows
        self.cols = columns
        self.board = [[None for _ in range(columns)] for _ in range(rows)]
        self.empty_cells = rows * columns
        self.spawn()
        self.spawn()
        self.possible_moves = []
        self.set_possible_moves()

    def print_board(self) -> None:
        for row in self.board:
            print(row)

    def start_game(self, rows=4, columns=4) -> None:
        self.__init__(rows, columns)

    def set_empty_cells(self) -> None:
        self.empty_cells = sum([row.count(None) for row in self.board])
    
    def game_status(self) -> State:
        if self.empty_cells > 0:
            return State.ONGOING
        else:
            return State.LOST
    
    def spawn(self) -> None:
        status = self.game_status()
        if status == State.LOST:
            raise ValueError("Cannot spawn a new node on a full board")
        if status == State.WON:
            raise ValueError("Cannot spawn a new node after winning")
        
        value = 4 if random.randint(1, 10) == 10 else 2
        position = random.randint(0, self.empty_cells - 1)
        row_index = int(position/self.rows)
        position %= self.rows

        while self.board[row_index][position] is not None:
            position += 1
            if position == self.cols:
                position = 0
                row_index += 1

        self.board[row_index][position] = Node(value)
        
    # [
    #   [None, None,    2, None],
    #   [None, None, None, None],
    #   [None,    4, None,    2],
    #   [8,      16, None,    2],
    # ]

    def set_possible_moves(self) -> None:
        moves = []

        if self.game_status() != State.ONGOING:
            return moves

        for row in self.board:
            none_count = row.count(None)
            if none_count == 0 or row[-none_count:].count(None) == none_count:
                continue
            moves.append(Direction.RIGHT)
            break

        for row in self.board:
            none_count = row.count(None)
            if none_count == 0 or row[:none_count].count(None) == none_count:
                continue
            moves.append(Direction.LEFT)
            break

        for i in range(self.cols):
            none_count = sum([row[i] is None for row in self.board])
            if none_count == 0 or [row[i] for row in self.board][-none_count:].count(None) == none_count:
                continue
            moves.append(Direction.DOWN)
            break

        for i in range(self.cols):
            none_count = sum([row[i] is None for row in self.board])
            if none_count == 0 or [row[i] for row in self.board][:none_count].count(None) == none_count:
                continue
            moves.append(Direction.UP)
            break

        self.possible_moves = moves

    def make_move(self, direction: Direction) -> None:
        if direction not in self.possible_moves:
            print(self.possible_moves)
            raise ValueError("Invalid direction")
        
        match direction:
            case Direction.UP:
                self.move_up()
                self.spawn()
                self.set_possible_moves()
            case Direction.DOWN:
                self.move_down()
                self.spawn()
                self.set_possible_moves()
            case Direction.LEFT:
                self.move_left()
                self.spawn()
                self.set_possible_moves()
            case Direction.RIGHT:
                self.move_right()
                self.spawn()
                self.set_possible_moves()

    def move_left(self) -> None:
        for row in self.board:
            while None in row:
                row.remove(None)
            for i, node in enumerate(row):
                if i == len(row) - 1:
                    pass
                elif node and node.value == row[i+1].value:
                    if node.double() == 2048:
                        print('gg')
                    row[i+1] = None
            while None in row:
                row.remove(None)
            while len(row) < self.cols:
                row.append(None)
                    

    def move_right(self) -> None:
        for row in self.board:
            while None in row:
                row.remove(None)
            for i, node in enumerate(row):
                if i == len(row) - 1:
                    continue
                elif node and node.value == row[i+1].value:
                    if node.double() == 2048:
                        print('gg')
                    row[i+1] = None
            while None in row:
                row.remove(None)
            while len(row) < self.cols:
                row.insert(0, None)

    def transpose(self) -> None:
        self.board = list(map(list, zip(*self.board)))

    def move_up(self) -> None:
        self.transpose()
        self.move_left()
        self.transpose()
    
    def move_down(self) -> None:
        self.transpose()
        self.move_right()
        self.transpose()