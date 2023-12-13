from unittest import TestCase
from code2048.board import Board, Direction
from code2048.node import Node


class TestBoard(TestCase):
    def test_init(self):
        with self.assertRaises(ValueError):
            Board(0, 0)
        with self.assertRaises(ValueError):
            Board(0, 2)
        with self.assertRaises(ValueError):
            Board(2, 0)
        with self.assertRaises(ValueError):
            Board(-2, 2)
        with self.assertRaises(ValueError):
            Board(2, -2)

        a = Board(2, 2)

        self.assertEqual(a.rows, 2)
        self.assertEqual(a.cols, 2)
        self.assertEqual(a.empty_cells, 2)

        b = Board(4, 4)

        self.assertEqual(b.rows, 4)
        self.assertEqual(b.cols, 4)
        self.assertEqual(b.empty_cells, 14)

        c = Board(board=[[Node(2), Node(4)], [Node(8), Node(16)]])
        self.assertEqual(c.rows, 2)
        self.assertEqual(c.cols, 2)
        self.assertEqual(c.empty_cells, 0)
        self.assertEqual(c.possible_moves, {})

    def test_spawn(self):
        a = Board(2, 2)

        self.assertEqual(a.empty_cells, 2)
        a.spawn()
        self.assertEqual(a.empty_cells, 1)
        a.spawn()
        self.assertEqual(a.empty_cells, 0)

        with self.assertRaises(ValueError):
            a.spawn()

    def test_possible_moves(self):
        board_no_moves = [
            [Node(2), Node(4), Node(16), Node(4)],
            [Node(8), Node(32), Node(2), Node(16)],
            [Node(4), Node(64), Node(16), Node(4)],
            [Node(2), Node(8), Node(32), Node(64)],
        ]

        a = Board(board=board_no_moves)
        self.assertEqual(a.possible_moves, {})

        with self.assertRaises(ValueError):
            a.make_move(Direction.UP)

        board_all_moves_full = [
            [Node(2), Node(2), Node(16), Node(4)],
            [Node(8), Node(32), Node(2), Node(16)],
            [Node(4), Node(64), Node(16), Node(4)],
            [Node(2), Node(8), Node(16), Node(64)],
        ]
        b = Board(board=board_all_moves_full)
        self.assertEqual(len(b.possible_moves), 4)

        board_all_moves_empty = [
            [Node(None), Node(None), Node(None), Node(None)],
            [Node(None), Node(2), Node(2), Node(None)],
            [Node(None), Node(2), Node(2), Node(None)],
            [Node(None), Node(None), Node(None), Node(None)],
        ]

        c = Board(board=board_all_moves_empty)
        self.assertEqual(len(c.possible_moves), 4)

    def test_transpose(self):
        board = [
            [Node(2), Node(2), Node(None), Node(4)],
            [Node(None), Node(None), Node(None), Node(None)],
            [Node(None), Node(None), Node(None), Node(None)],
            [Node(None), Node(None), Node(None), Node(None)],
        ]

        expected_board = [
            [Node(2), Node(None), Node(None), Node(None)],
            [Node(2), Node(None), Node(None), Node(None)],
            [Node(None), Node(None), Node(None), Node(None)],
            [Node(4), Node(None), Node(None), Node(None)],
        ]

        a = Board(board=board)
        a.board = a.transpose(a.board)

        self.assertEqual(a.board, expected_board)

    def test_move_right(self):
        board=[
            [Node(None),Node(None), Node(None),Node(None)],
            [Node(2),Node(None), Node(None),Node(2)],
            [Node(None),Node(None), Node(None),Node(2)],
            [Node(None),Node(None), Node(None),Node(None)],
        ]

        expected_board = [
            [Node(None),Node(None), Node(None),Node(None)],
            [Node(None),Node(None), Node(None),Node(4)],
            [Node(None),Node(None), Node(None),Node(2)],
            [Node(None),Node(None), Node(None),Node(None)],
        ]

        a = Board(board=board)
        a.move_right()
        self.assertEqual(a.possible_moves[Direction.RIGHT], expected_board)

        
    def test_move_left(self):
        board=[
            [Node(None),Node(None), Node(None),Node(None)],
            [Node(2),Node(None), Node(None),Node(2)],
            [Node(None),Node(None), Node(None),Node(2)],
            [Node(None),Node(None), Node(None),Node(None)],
        ]

        expected_board = [
            [Node(None),Node(None), Node(None),Node(None)],
            [Node(4),Node(None), Node(None),Node(None)],
            [Node(2),Node(None), Node(None),Node(None)],
            [Node(None),Node(None), Node(None),Node(None)],
        ]

        a = Board(board=board)
        a.move_left()
        self.assertEqual(a.possible_moves[Direction.LEFT], expected_board)

    def test_move_up(self):
        board=[
            [Node(None),Node(None), Node(None),Node(None)],
            [Node(2),Node(None), Node(None),Node(2)],
            [Node(None),Node(None), Node(None),Node(2)],
            [Node(None),Node(None), Node(None),Node(None)],
        ]

        expected_board = [
            [Node(2),Node(None), Node(None),Node(4)],
            [Node(None),Node(None), Node(None),Node(None)],
            [Node(None),Node(None), Node(None),Node(None)],
            [Node(None),Node(None), Node(None),Node(None)],
        ]

        a = Board(board=board)
        a.move_up()
        self.assertEqual(a.possible_moves[Direction.UP], expected_board)

    def test_move_down(self):
        board=[
            [Node(None),Node(None), Node(None),Node(None)],
            [Node(2),Node(None), Node(None),Node(2)],
            [Node(None),Node(None), Node(None),Node(2)],
            [Node(None),Node(None), Node(None),Node(None)],
        ]

        expected_board = [
            [Node(None),Node(None), Node(None),Node(None)],
            [Node(None),Node(None), Node(None),Node(None)],
            [Node(None),Node(None), Node(None),Node(None)],
            [Node(2),Node(None), Node(None),Node(4)],
        ]

        a = Board(board=board)
        a.move_down()
        self.assertEqual(a.possible_moves[Direction.DOWN], expected_board)