"""collect all helper functions to be used by the main module"""
import math


def king_danger(attacking_row, attacking_column, row, column):
    """Check if a piece is safe from a king.

    returns True if the distance is less than or equal one square from all
    directions

    Arguments:
    row -- first piece's row number
    column -- first piece's column number
    attacking_row -- second piece's row number
    attacking_column -- second piece-s column number
    """
    return math.fabs(row - attacking_row) <= 1 and math.fabs(
        column - attacking_column) <= 1


def knight_danger(row, column, attacking_row, attacking_column):
    """Check if a piece is safe from a knight.

    Check if the locations between a knight and another piece,
    it checks for the combinations of L-shape positions and returns True if
    one of them is found.

    Arguments:
    row -- first piece's row number
    column -- first piece's column number
    attacking_row -- second piece's row number
    attacking_column -- second piece-s column number
    """

    return (row == attacking_row and column == attacking_column) or any(
        (attacking_row - row, attacking_column - column) == delta for delta in
        [(-1, -2), (1, -2), (-2, -1), (2, -1), (-2, 1), (2, 1), (-1, 2),
         (1, 2)])


def diagonals_danger(attacking_row, attacking_column, row, column):
    """Check safety of pieces on the same diagonals, both left and right ones.

    Arguments:
    row -- first piece's row number
    column -- first piece's column number
    attacking_row -- second piece's row number
    attacking_column -- second piece-s column number
    """
    return True if (column - attacking_column) == (row - attacking_row) or \
                   (column - attacking_column) == -(
                   row - attacking_row) else False


def row_or_column_danger(attacking_row, attacking_column, row, column):
    """Check safety of pieces on the same row or the
    same column

    Arguments:
    row -- first piece's row number
    column -- first piece's column number
    attacking_row -- second piece's row number
    attacking_column -- second piece-s column number
    """
    return True if attacking_row == row or attacking_column == column else \
        False
