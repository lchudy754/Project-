Since the midterm, I started by fixing the bug that broke the game if the user input the wrong number. I then fixed the hardcoded numbers "5,4,9" that were pointed out in the midterm comments by adding the variable "BOARD_SIZE". In a seperate file is the updated code that edited this fixed one, allowing the user to input numbers N,k and making an NxN board where the goal is to get k in a row.I also redid the tests for this updated code which should hopefully work better now. My next steps in the coming week are to try to have the computer play against itself.

5x5 Tic Tac  Toe Game. This is a two-player tic-tac-toe game on an expanded 5x5 board. This is expanded from the original project code that had a 3x3 board. 
The players take turns to place their marks (X or O) on the board by selecting row 0-4 and column 0-4, and the game checks for wins or draws after each move. 
Players win when getting 5 in a row of their mark in any direction: horizontally, vertically, or diagonally. 
The code will not let a player put their mark where there is one already, and it will check for wins or a draw (full board) after each move that a player makes. 
Player X goes first, and then player O follows.

In the github, there is the basic code, a test suite, the answers to the questions from the project guidelines, and this readme. 

