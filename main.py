from board import Board, Direction

a = Board()

a.start_game()
a.print_board()

while a.game_status().value == 0:
    print("Possible moves: ", a.possible_moves)
    direction = input("Enter direction: (w/s/a/d)")
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
    a.print_board()
    print('\n')

if a.game_status().value  == 1:
    print("You win!")
else:
    print("You lose!")
