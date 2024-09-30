import unittest
from io import StringIO
import sys

# Function to print the board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 9)  # Adjust width for 5x5 board

# Function to check for a win
def check_win(board, player):
    # Check rows
    for row in board:
        if all(s == player for s in row):
            return True
    # Check columns
    for col in range(5):
        if all(board[row][col] == player for row in range(5)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(5)) or all(board[i][4 - i] == player for i in range(5)):
        return True
    return False

# Function to check if the board is full (draw)
def check_draw(board):
    return all(board[row][col] != " " for row in range(5) for col in range(5))

# Function to play the game
def play_game():
    # Create the 5x5 board
    board = [[" " for _ in range(5)] for _ in range(5)]
    current_player = "X"
    
    while True:
        print_board(board)
        # Get the player's move
        row = int(input(f"Player {current_player}, enter the row (0-4): "))
        col = int(input(f"Player {current_player}, enter the column (0-4): "))

        # Check if the move is valid
        if board[row][col] != " ":
            print("That spot is already taken. Try again.")
            continue
        
        # Place the player's symbol on the board
        board[row][col] = current_player

        # Check for a win
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        # Check for a draw
        if check_draw(board):
            print_board(board)
           
