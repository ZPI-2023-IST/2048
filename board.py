from node import Node
import random
from enum import Enum
import copy


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
    def __init__(self, rows=4, columns=4, board=None):
        if board:
            self.rows = len(board)
            self.cols = len(board[0])
            self.board = board
            self.empty_cells = sum([row.count(Node(None)) for row in self.board])
        else:
            self.rows = rows
            self.cols = columns
            self.board = [[Node(None) for _ in range(columns)] for _ in range(rows)]
            self.empty_cells = rows * columns
            self.spawn()
            self.spawn()
        self.possible_moves = []
        self.set_possible_moves()

    def print_board(self) -> Node(None):
        for row in self.board:
            print('|', end='')
            for elem in row:
                print(elem, end='|')
            print('\n')

    def start_game(self, rows=4, columns=4) -> None:
        self.__init__(rows, columns)

    def set_empty_cells(self) -> Node(None):
        self.empty_cells = sum([row.count(Node(None)) for row in self.board])
    
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

        while self.board[row_index][position] != Node(None):
            position += 1
            if position == self.cols:
                position = 0
                row_index += 1

        self.board[row_index][position] = Node(value)
        
    # [
    #   [Node(None), Node(None),    2, Node(None)],
    #   [Node(None), Node(None), Node(None), Node(None)],
    #   [Node(None),    4, Node(None),    2],
    #   [8,      16, Node(None),    2],
    # ]

    def set_possible_moves(self) -> None:
        moves = []

        if self.game_status() != State.ONGOING:
            return moves

        if self.move_left(save=False):
            moves.append(Direction.LEFT)
        if self.move_right(save=False):
            moves.append(Direction.RIGHT)
        if self.move_up(save=False):
            moves.append(Direction.UP)
        if self.move_down(save=False):
            moves.append(Direction.DOWN)

        self.possible_moves = moves

    def make_move(self, direction: Direction) -> None:
        if direction not in self.possible_moves:
            self.set_possible_moves()
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

    def move_left(self, save=True) -> bool:
        new_board = copy.deepcopy(self.board)
        for row in new_board:
            while Node(None) in row:
                row.remove(Node(None))
            for i, node in enumerate(row):
                if i == len(row) - 1:
                    pass
                elif node and node.value == row[i+1].value:
                    if node.double() == 2048:
                        print('gg')
                    row[i+1] = Node(None)
            while Node(None) in row:
                row.remove(Node(None))
            while len(row) < self.cols:
                row.append(Node(None))

        if new_board == self.board:
            return False
        if save:
            self.board = new_board
        return True
                    


    def move_right(self, save=True) -> bool:
        new_board = copy.deepcopy(self.board)
        for row in new_board:
            while Node(None) in row:
                row.remove(Node(None))
            for i, node in enumerate(row):
                if i == len(row) - 1:
                    continue
                elif node and node.value == row[i+1].value:
                    if node.double() == 2048:
                        print('gg')
                    row[i+1] = Node(None)
            while Node(None) in row:
                row.remove(Node(None))
            while len(row) < self.cols:
                row.insert(0, Node(None))
        if new_board == self.board:
            return False
        if save:
            self.board = new_board
        return True

    def transpose(self) -> None:
        self.board = list(map(list, zip(*self.board)))

    def move_up(self, save=True) -> bool:
        self.transpose()
        result = self.move_left(save)
        self.transpose()
        return result
    
    def move_down(self, save=True) -> bool:
        self.transpose()
        result = self.move_right(save)
        self.transpose()
        return result