from node import Node
import random
from enum import Enum
import copy

from Game import State


class Direction(Enum):
    UP = 'w'
    DOWN = 's'
    LEFT = 'a'
    RIGHT = 'd'

class Board:
    def __init__(self, rows=4, columns=4, board=None):
        if board:
            self.rows = len(board)
            self.cols = len(board[0])
            self.board = board
            self.empty_cells = sum([row.count(Node(None)) for row in self.board])
        else:
            if rows < 2 or columns < 2:
                raise ValueError("Board must be at least 2x2")
            self.rows = rows
            self.cols = columns
            self.board = [[Node(None) for _ in range(columns)] for _ in range(rows)]
            self.empty_cells = rows * columns
            self.spawn()
            self.spawn()
        self.possible_moves = {}
        self.set_possible_moves()

    def print_board(self) -> None:
        for row in self.board:
            print('|', end='')
            for elem in row:
                print(elem, end='|')
            print('\n')

    def set_empty_cells(self) -> None:
        self.empty_cells = sum([row.count(Node(None)) for row in self.board])

    def has_won(self) -> bool:
        for row in self.board:
            for node in row:
                if node and node.value == 2048:
                    return True
        return False
    
    def game_status(self) -> State:
        if self.empty_cells > 0 or self.possible_moves:
            return State.ONGOING
        if self.has_won():
            return State.WON
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
        position_2 = position % self.rows

        try:
            while self.board[row_index][position_2] != Node(None):
                position_2 += 1
                if position_2 == self.cols:
                    position_2 = 0
                    row_index += 1
        except IndexError:
            self.print_board()
            print(self.empty_cells, position, row_index, position_2)
            quit(1)

        self.board[row_index][position_2] = Node(value)
        self.empty_cells -= 1

    def set_possible_moves(self) -> None:
        if self.game_status() != State.ONGOING:
            self.possible_moves = {}

        self.possible_moves = {}

        self.move_left()
        self.move_right()
        self.move_up()
        self.move_down()

    def make_move(self, direction: Direction) -> None:
        if direction not in self.possible_moves:
            self.set_possible_moves()
            raise ValueError("Invalid direction")
        
        match direction:
            case Direction.UP:
                self.board = self.possible_moves[Direction.UP]
            case Direction.DOWN:
                self.board = self.possible_moves[Direction.DOWN]
            case Direction.LEFT:
                self.board = self.possible_moves[Direction.LEFT]
            case Direction.RIGHT:
                self.board = self.possible_moves[Direction.RIGHT]
        self.set_empty_cells()
        self.spawn()
        self.empty_cells -= 1
        self.set_possible_moves()

    def move_left(self, transposed=False) -> None:
        new_board = copy.deepcopy(self.board)
        comparable = copy.deepcopy(self.board)
        if transposed:
            comparable = self.transpose(comparable)
            new_board = self.transpose(new_board)
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

        direction = Direction.UP if transposed else Direction.LEFT
        if new_board == comparable:
            try:
                self.possible_moves.pop(direction)
            except KeyError:
                pass
        else:
            if transposed:
                new_board = self.transpose(new_board)
            self.possible_moves[direction] = new_board


    def move_right(self, transposed=False) -> None:
        new_board = copy.deepcopy(self.board)
        comparable = copy.deepcopy(self.board)
        if transposed:
            new_board = self.transpose(new_board)
            comparable = self.transpose(comparable)
        for row in new_board:
            while Node(None) in row:
                row.remove(Node(None))
            for i, node in enumerate(row):
                if i == len(row) - 1:
                    continue
                elif node and node.value == row[i+1].value:
                    node.double()
                    row[i+1] = Node(None)
            while Node(None) in row:
                row.remove(Node(None))
            while len(row) < self.cols:
                row.insert(0, Node(None))

        direction = Direction.DOWN if transposed else Direction.RIGHT
        if new_board == comparable:
            try:
                self.possible_moves.pop(direction)
            except KeyError:
                pass
        else:
            if transposed:
                new_board = self.transpose(new_board)
            self.possible_moves[direction] = new_board
    
    def transpose(self, board) -> list:
        return list(map(list, zip(*board)))

    def move_up(self) -> None:
        self.move_left(True)
    
    def move_down(self) -> None:
        self.move_right(True)