# Tic-Tac-Toe AI — Minimax & Alpha-Beta Pruning

A command-line Tic-Tac-Toe game where you play against an unbeatable AI. The project implements the AI opponent two ways — plain **Minimax** and **Minimax with Alpha-Beta pruning** — to compare correctness and efficiency.

## How It Works
- The board is a 3x3 grid; the human plays `X`, the AI plays `O`.
- The AI evaluates all possible future game states using recursive game-tree search:
  - **Minimax** (`tictactoe_minimax.py`): explores the entire game tree to guarantee optimal play.
  - **Alpha-Beta Pruning** (`tictactoe_alphabeta.py`): explores the same tree but cuts off branches that can't affect the final decision, and lets you choose between Minimax or Alpha-Beta at runtime while tracking how many branches were pruned.
- Win/draw detection checks all rows, columns, and both diagonals.

## Files
| File | Description |
|---|---|
| `tictactoe_minimax.py` | Tic-Tac-Toe with a standard Minimax AI |
| `tictactoe_alphabeta.py` | Tic-Tac-Toe with a menu to choose Minimax or Alpha-Beta pruning, plus a prune counter |

## Run It
```bash
python tictactoe_minimax.py
# or
python tictactoe_alphabeta.py
```
You'll be prompted for a row and column (0–2) on your turn; the AI responds automatically.

## Sample Output
```
  0   1   2
0 X |   |
  --+---+--
1   | O |
  --+---+--
2   |   |

Enter row (0-2): 2
Enter column (0-2): 0
...
Computer wins!
```

## Why Alpha-Beta Pruning?
Both algorithms produce identical (optimal) moves, but Alpha-Beta skips branches that can't change the outcome, reducing the number of nodes evaluated compared to plain Minimax — useful for larger search spaces where full Minimax becomes expensive.
