from board import Board, Direction
from node import Node

a = Board(
    
    board=[
      [Node(2), Node(4),Node(16), Node(4)],
      [Node(8), Node(32), Node(2), Node(16)],
      [Node(4),Node(64), Node(16),Node(4)],
      [Node(2),Node(8), Node(32),Node(64)],
    ]
)

a.print_board()

while a.game_status().value == 0:
    print("Possible moves: ", a.possible_moves.keys())
    direction = input("Enter direction: (w/s/a/d)")
    try:
        match direction:
            case "w":
                a.make_move(Direction.UP)
            case "s":
                a.make_move(Direction.DOWN)
            case "a":
                a.make_move(Direction.LEFT)
            case "d":
                a.make_move(Direction.RIGHT)
            case _:
                print("Invalid input")
                print(direction)
                continue
    except ValueError:
        print("Invalid move")
        continue
    a.print_board()
    print('\n')

if a.game_status().value  == 1:
    print("You win!")
else:
    print("You lose!")
