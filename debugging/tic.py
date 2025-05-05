#!/usr/bin/python3

def print_board(board):
    """
    Prints the current state of the Tic-Tac-Toe board.
    Each row is printed with spaces between the cells, and horizontal lines are drawn.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Checks if there is a winner in the current state of the Tic-Tac-Toe board.
    
    Returns:
        bool: True if there's a winner, False otherwise.
    """
    # Check rows for winner
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns for winner
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals for winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def check_draw(board):
    """
    Checks if the game is a draw, i.e., the board is full and there's no winner.
    
    Returns:
        bool: True if the game is a draw, False otherwise.
    """
    for row in board:
        if " " in row:
            return False  # If there is any empty space, the game is not a draw
    return True  # The board is full and no winner, so it's a draw

def tic_tac_toe():
    """
    Main game loop for Tic-Tac-Toe.
    Alternates between players "X" and "O" and checks for a winner or draw after each move.
    """
    board = [[" "]*3 for _ in range(3)]  # Create a 3x3 board
    player = "X"  # Start with player "X"
    
    while True:
        print_board(board)  # Print the current board
        try:
            row, col = map(int, input(f"Enter row and column (0, 1, or 2) for player {player}: ").split())
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid input. Row and column must be between 0 and 2.")
                continue
        except ValueError:
            print("Invalid input. Please enter two integers separated by a space.")
            continue

        if board[row][col] == " ":
            board[row][col] = player  # Place the player's symbol
            if check_winner(board):
                print_board(board)
                print(f"Player {player} wins!")
                break  # Exit the loop when there's a winner
            if check_draw(board):
                print_board(board)
                print("The game is a draw!")
                break  # Exit the loop if the game is a draw
            player = "O" if player == "X" else "X"  # Alternate between players
        else:
            print("That spot is already taken! Try again.")

if __name__ == "__main__":
    tic_tac_toe()

