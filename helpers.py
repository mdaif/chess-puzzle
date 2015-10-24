"""A collection of helper functions to be used by the main module"""
import math


def king_danger(row_1, column_1, row_2, column_2):
    """Checks the distance between a king and another piece, it returns True
    if the distance is less than or equal one square to all directions"""
    return math.fabs(row_1 - row_2) <= 1 and math.fabs(
        column_1 - column_2) <= 1


def knight_danger(row_1, column_1, row_2, column_2):
    """Checks if the locations between a knight and another piece,
    it checks for the combinations of L-shape positions and returns True if
    one of them is found."""
    deltas = [(-1, -2), (1, -2), (-2, -1), (2, -1), (-2, 1), (2, 1), (-1, 2),
              (1, 2)]
    return (row_1 == row_2 and column_1 == column_2) or any(
        (row_2 - row_1, column_2 - column_1) == delta for delta in deltas)
