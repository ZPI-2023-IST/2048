from board import Board, Direction

a = Board()

a.start_game()
a.print_board()

while True:
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
    print("Empty cells: ", a.empty_cells)
    print("Game status: ", a.game_status())
    if a.game_status() == "LOST":
        break
    elif a.game_status() == "WON":
        print("You won!")
        break
    print('\n')
