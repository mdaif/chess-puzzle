# chess-puzzle
A generalized version of 8-queens problem, with asymmetric board, and kings, queens, bishops, rooks, and knights are allowed.

# Quick Start
After you clone the repo you can run the application to calculate the number of unique configurations of placing 2 rooks and 4 knights on a 4x4 chess board.

```
  python chess_challenge.py -width 4 -height 4 --rooks 2 --knights 4
```

The width argument is the board width and is required.
The height argument is the board height and is required.
The --queens option is the number of queens placed on the board.
The --bishops option is the number of bishops placed on the board.

After you run the command it will display all the unique configurations along with the time spent in the calculations.

```
[(Knight, 2, 2), (Knight, 2, 4), (Knight, 4, 2), (Knight, 4, 4), (Rook, 1, 1), (Rook, 3, 3)]
[(Knight, 2, 1), (Knight, 2, 3), (Knight, 4, 1), (Knight, 4, 3), (Rook, 1, 2), (Rook, 3, 4)]
[(Knight, 2, 2), (Knight, 2, 4), (Knight, 4, 2), (Knight, 4, 4), (Rook, 1, 3), (Rook, 3, 1)]
[(Knight, 2, 1), (Knight, 2, 3), (Knight, 4, 1), (Knight, 4, 3), (Rook, 1, 4), (Rook, 3, 2)]
[(Knight, 1, 2), (Knight, 1, 4), (Knight, 3, 2), (Knight, 3, 4), (Rook, 2, 1), (Rook, 4, 3)]
[(Knight, 1, 1), (Knight, 1, 3), (Knight, 3, 1), (Knight, 3, 3), (Rook, 2, 2), (Rook, 4, 4)]
[(Knight, 1, 2), (Knight, 1, 4), (Knight, 3, 2), (Knight, 3, 4), (Rook, 2, 3), (Rook, 4, 1)]
[(Knight, 1, 1), (Knight, 1, 3), (Knight, 3, 1), (Knight, 3, 3), (Rook, 2, 4), (Rook, 4, 2)]
Program finished in approximately 0.055071 seconds, number of unique solutions found: 8
```

Running the chess_challenge script with -h option will display all available options.

```
usage: chess_challenge.py [-h] -width WIDTH -height HEIGHT [--kings KINGS]
                          [--queens QUEENS] [--bishops BISHOPS]
                          [--knights KNIGHTS] [--rooks ROOKS]

Find all unique configurations of a set of normal chess pieces on a chess
board

optional arguments:
  -h, --help         show this help message and exit
  -width WIDTH       board width
  -height HEIGHT     board height
  --kings KINGS      Number of kings
  --queens QUEENS    Number of queens
  --bishops BISHOPS  Number of bishops
  --knights KNIGHTS  Number of knights
  --rooks ROOKS      number of rooks
```
