# Tic-Tac-Toe AI (Minimax Algorithm)

This project is an AI-powered Tic-Tac-Toe game using the **Minimax algorithm with Alpha-Beta Pruning**.  
The AI plays optimally, meaning if you play perfectly, the game will always result in a **tie**! 🎮🤖  

## **Project Files**
- `runner.py` → Runs the **graphical user interface (GUI)** of the Tic-Tac-Toe game.
- `tictactoe.py` → Implements the **game logic and AI** using Minimax with Alpha-Beta Pruning.
- `test_tictactoe.py` → A test file to verify **individual functions** before running the game.

Changes Made to Fix the Code
 Issues in Original Code
Missing Implementations

tictactoe.py had several NotImplementedError functions, meaning the game logic wasn't working.
Minimax Algorithm Not Implemented

The AI didn't make optimal moves because minimax() wasn't implemented.
Terminal Board Detection Issue

The terminal(board) function had raise NotImplementedError, which caused a crash.
Deep Copy Issue in result(board, action)

The function needed to return a new board without modifying the existing one.
✅ Fixes and Improvements
Implemented all missing functions in tictactoe.py:

player(board), actions(board), result(board, action), winner(board), terminal(board), utility(board), and minimax(board).
Added Minimax Algorithm with Alpha-Beta Pruning for faster AI decision-making.

Fixed Terminal Board Check so the game detects a win/tie properly.

Optimized result(board, action) to avoid modifying the original board.

 Understanding the Hint Section
The assignment provided hints on:

Testing functions in a different file
 Implemented test_tictactoe.py to verify each function separately before running the full game.

Adding Helper Functions
Added a print_board(board) function in test_tictactoe.py to print board states for debugging.

Alpha-Beta Pruning
 Already implemented in the minimax(board) function to improve AI efficiency.

 Tic-Tac-Toe AI is Complete!
🏆 AI plays optimally (Minimax + Alpha-Beta Pruning)
✅ Fully implemented and tested
🎮 GUI interface for easy play
🛠️ Separate test file for debugging
