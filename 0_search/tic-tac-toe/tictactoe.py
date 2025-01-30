"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    # Count the number of X's and O's on the board
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)

    # Decide whose turn is it
    if x_count == o_count:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    possible_actions = set()

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    # Check if the action is valid
    if action not in actions(board):
        raise Exception("Invalid action!")

    # Create a deep copy of the board
    new_board = [row[:] for row in board]

    # Determine whose turn it is
    current_player = player(board)

    # Apply the move to the new board
    i, j = action
    new_board[i][j] = current_player

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # Check rows for a winner
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]

    # Check columns for a winner
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]

    # Check diagonals for a winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]

    # If no winner, return None
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    # Check if there's a winner
    if winner(board) is not None:
        return True

    # Check if the board is full
    for row in board:
        if EMPTY in row:
            return False

    # If no winner and no empty spaces, the game is over
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    game_winner = winner(board)

    if game_winner == X:
        return 1
    elif game_winner == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    # Check if the board is in a terminal state
    if terminal(board):
        return None

    current_player = player(board)

    # Decide optimal move
    if current_player == X:
        best_action = None
        best_value = -math.inf
        for action in actions(board):
            value = min_value(result(board, action))
            if value > best_value:
                best_value = value
                best_action = action
        return best_action
    else:
        best_action = None
        best_value = math.inf
        for action in actions(board):
            value = max_value(result(board, action))
            if value < best_value:
                best_value = value
                best_action = action
        return best_action


def max_value(board):
    """
    Finds the maximum utility value for X.
    """
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):
    """
    Finds the minimum utility value for O.
    """
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v


def main():
    # Initialize the board
    board = initial_state()

    print("Initial board:")
    for row in board:
        print(row)

    while not terminal(board):
        # Get the current player's turn
        current_player = player(board)
        print(f"\nIt's {current_player}'s turn!")

        if current_player == X or current_player == O:
            # Minimax suggestion (AI move)
            action = minimax(board)
            print(f"{current_player} chooses action: {action}")
            board = result(board, action)

        # Print the board after each move
        print("\nCurrent board:")
        for row in board:
            print(row)

    # Game over
    print("\nGame over!")
    game_winner = winner(board)
    if game_winner:
        print(f"The winner is {game_winner}!")
    else:
        print("It's a tie!")


if __name__ == "__main__":
    main()
