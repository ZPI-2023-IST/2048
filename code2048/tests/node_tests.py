from unittest import TestCase
from code2048.node import Node


class TestNode(TestCase):
    def create_node(self):
        with self.assertRaises(ValueError):
            Node(3)
        with self.assertRaises(ValueError):
            Node(0)
        with self.assertRaises(ValueError):
            Node(-2)

        a = Node(2)
        b = Node(4)

        self.assertEqual(a.value, 2)
        self.assertEqual(b.value, 4)

    def test_double(self):
        a = Node(2)
        b = Node(4)

        self.assertEqual(a.double(), 4)
        self.assertEqual(b.double(), 8)
