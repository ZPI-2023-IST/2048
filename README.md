# 2048

Implementation of 2048 game as a module used for final engineering project.

## Game representation

Game board is represented by **r * c** matrix, where **r** indicates number of rows and **c** stands for columns. Each cell contains a **Node** object whose *value* field contains either an integer or None when the cell should be empty.

## API

When using this module you can use following functions:

1. get_moves() -> list:

    Provides possible moves as a list of *w/s/a/d* characters meaning *up/down/left/right* respectively

2. make_move(move: tuple) -> bool:

    Returns True if move succeeded, False otherwise.

    Requires *move* in form of one element tuple, containing character mentioned above.

    Example: make_move('w',) will perform an upwards move.

3. get_state() -> State:

    Returns game state enum:  State.{*ONGOING* / *WON* / *LOST*}.

4. get_board() -> list:

    Returns current board state as a list of lists (rows).

5. start_game() -> None:

    Overwrites current object, invoking constructor with default values and resetting every variable.

## Package name

The package is named game2048