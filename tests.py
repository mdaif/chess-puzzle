"""Test helper functions and main functionality."""
import unittest

from chess_challenge import ChessChallengeEngine
from helpers import king_danger, knight_danger, diagonals_danger, \
    row_or_column_danger
from pieces import King, Queen, Rook, Knight, Bishop


class HelpersTest(unittest.TestCase):
    """Test helper functions."""

    def setUp(self):
        """Set up variables across each unit test."""
        self.row = 5
        self.column = 4

    def test_king_danger_1(self):
        """Check dangerous move.

        both pieces on the same square, one is king.
        """
        danger = king_danger(self.row, self.column, self.row, self.column)
        self.assertTrue(danger)

    def test_king_danger_2(self):
        """Check dangerous move.

        a king is one square to the left.
        """
        danger = king_danger(self.row, self.column, self.row - 1, self.column)
        self.assertTrue(danger)

    def test_king_danger_3(self):
        """Check dangerous move.

        a king is one square to the right.
        """
        danger = king_danger(self.row, self.column, self.row + 1, self.column)
        self.assertTrue(danger)

    def test_king_danger_4(self):
        """Check dangerous move.

        a king is one square up.
        """
        danger = king_danger(self.row, self.column, self.row, self.column - 1)
        self.assertTrue(danger)

    def test_king_danger_5(self):
        """Check dangerous move.

        a king is one square down.
        """
        danger = king_danger(self.row, self.column, self.row, self.column + 1)
        self.assertTrue(danger)

    def test_king_danger_6(self):
        """Check dangerous move.

        a king is one square north-east.
        """
        danger = king_danger(self.row, self.column, self.row + 1,
                             self.column - 1)
        self.assertTrue(danger)

    def test_king_danger_7(self):
        """Check dangerous move.

        a king is one square north-west.
        """
        danger = king_danger(self.row, self.column, self.row - 1,
                             self.column - 1)
        self.assertTrue(danger)

    def test_king_danger_8(self):
        """Check dangerous move.

        a king is one square south-west.
        """
        danger = king_danger(self.row, self.column, self.row - 1,
                             self.column + 1)
        self.assertTrue(danger)

    def test_king_danger_9(self):
        """Check dangerous move.

        a king is one square south-east.
        """
        danger = king_danger(self.row, self.column, self.row + 1,
                             self.column + 1)
        self.assertTrue(danger)

    def test_king_danger_10(self):
        """Check safe move."""
        danger = king_danger(self.row, self.column, self.row + 2, self.column)
        self.assertFalse(danger)

    def test_knight_danger_1(self):
        """Check dangerous move.

        a knight is on the end of an L-shaped distance.
        """
        danger = knight_danger(self.row, self.column, self.row + 1,
                               self.column - 2)
        self.assertTrue(danger)

    def test_knight_danger_2(self):
        """Check dangerous move.

        a knight is on the end of an L-shaped distance.
        """
        danger = knight_danger(self.row, self.column, self.row + 2,
                               self.column - 1)
        self.assertTrue(danger)

    def test_knight_danger_3(self):
        """Check dangerous move.

        a knight is on the end of an L-shaped distance.
        """
        danger = knight_danger(self.row, self.column, self.row + 1,
                               self.column + 2)
        self.assertTrue(danger)

    def test_knight_danger_4(self):
        """Check dangerous move.

        a knight is on the end of an L-shaped distance.
        """
        danger = knight_danger(self.row, self.column, self.row - 1,
                               self.column + 2)
        self.assertTrue(danger)

    def test_knight_danger_5(self):
        """Check dangerous move.

        a knight is on the end of an L-shaped distance.
        """
        danger = knight_danger(self.row, self.column, self.row - 2,
                               self.column + 1)
        self.assertTrue(danger)

    def test_knight_danger_6(self):
        """Check dangerous move.

        a knight is on the end of an L-shaped distance.
        """
        danger = knight_danger(self.row, self.column, self.row - 2,
                               self.column - 1)
        self.assertTrue(danger)

    def test_knight_danger_7(self):
        """Check dangerous move.

        a knight is on the end of an L-shaped distance.
        """
        danger = knight_danger(self.row, self.column, self.row - 1,
                               self.column - 2)
        self.assertTrue(danger)

    def test_knight_danger_8(self):
        """Check safe move."""
        danger = knight_danger(self.row, self.column, self.row - 1,
                               self.column - 1)
        self.assertFalse(danger)

    def test_diagonals_danger_1(self):
        """Check two pieces are placed on the same diagonal."""
        danger = diagonals_danger(self.row, self.column, self.row + 2,
                                  self.column - 2)
        self.assertTrue(danger)

    def test_diagonals_danger_2(self):
        """Check two pieces are placed on the same diagonal."""
        danger = diagonals_danger(self.row, self.column, self.row + 2,
                                  self.column + 2)
        self.assertTrue(danger)

    def test_diagonals_danger_3(self):
        """Check two pieces are placed on the same diagonal."""
        danger = diagonals_danger(self.row, self.column, self.row - 2,
                                  self.column + 2)
        self.assertTrue(danger)

    def test_diagonals_danger_4(self):
        """Check two pieces are placed on the same diagonal."""
        danger = diagonals_danger(self.row, self.column, self.row - 2,
                                  self.column - 2)
        self.assertTrue(danger)

    def test_diagonals_danger_5(self):
        """Check two pieces are NOT placed on the same diagonal."""
        danger = diagonals_danger(self.row, self.column, self.row,
                                  self.column - 2)
        self.assertFalse(danger)

    def row_or_column_danger_1(self):
        """Check two pieces on the same row but different columns."""
        danger = row_or_column_danger(self.row, self.column, self.row,
                                      self.column + 5)
        self.assertTrue(danger)

    def row_or_column_danger_2(self):
        """Check two pieces on the same column but different rows."""
        danger = row_or_column_danger(self.row, self.column, self.row + 5,
                                      self.column)
        self.assertTrue(danger)

    def row_or_column_danger_3(self):
        """Check two pieces on different rows and columns."""
        danger = row_or_column_danger(self.row, self.column, self.row + 5,
                                      self.column + 3)
        self.assertFalse(danger)


class ChessChallengeTest(unittest.TestCase):
    """Test core functionality of ChessChallengeEngine."""

    def test_normal_8_queens(self):
        """Happy path, 8 queens, 8 * 8 board."""
        pieces = [Queen] * 8
        engine = ChessChallengeEngine(pieces, len(pieces), len(pieces))
        expected = [[(Queen, 1, 1), (Queen, 2, 5), (Queen, 3, 8),
                     (Queen, 4, 6), (Queen, 5, 3), (Queen, 6, 7),
                     (Queen, 7, 2), (Queen, 8, 4)],
                    [(Queen, 1, 1), (Queen, 2, 6), (Queen, 3, 8),
                     (Queen, 4, 3), (Queen, 5, 7), (Queen, 6, 4),
                     (Queen, 7, 2), (Queen, 8, 5)],
                    [(Queen, 1, 1), (Queen, 2, 7), (Queen, 3, 4),
                     (Queen, 4, 6), (Queen, 5, 8), (Queen, 6, 2),
                     (Queen, 7, 5), (Queen, 8, 3)],
                    [(Queen, 1, 1), (Queen, 2, 7), (Queen, 3, 5),
                     (Queen, 4, 8), (Queen, 5, 2), (Queen, 6, 4),
                     (Queen, 7, 6), (Queen, 8, 3)],
                    [(Queen, 1, 2), (Queen, 2, 4), (Queen, 3, 6),
                     (Queen, 4, 8), (Queen, 5, 3), (Queen, 6, 1),
                     (Queen, 7, 7), (Queen, 8, 5)],
                    [(Queen, 1, 2), (Queen, 2, 5), (Queen, 3, 7),
                     (Queen, 4, 1), (Queen, 5, 3), (Queen, 6, 8),
                     (Queen, 7, 6), (Queen, 8, 4)],
                    [(Queen, 1, 2), (Queen, 2, 5), (Queen, 3, 7),
                     (Queen, 4, 4), (Queen, 5, 1), (Queen, 6, 8),
                     (Queen, 7, 6), (Queen, 8, 3)],
                    [(Queen, 1, 2), (Queen, 2, 6), (Queen, 3, 1),
                     (Queen, 4, 7), (Queen, 5, 4), (Queen, 6, 8),
                     (Queen, 7, 3), (Queen, 8, 5)],
                    [(Queen, 1, 2), (Queen, 2, 6), (Queen, 3, 8),
                     (Queen, 4, 3), (Queen, 5, 1), (Queen, 6, 4),
                     (Queen, 7, 7), (Queen, 8, 5)],
                    [(Queen, 1, 2), (Queen, 2, 7), (Queen, 3, 3),
                     (Queen, 4, 6), (Queen, 5, 8), (Queen, 6, 5),
                     (Queen, 7, 1), (Queen, 8, 4)],
                    [(Queen, 1, 2), (Queen, 2, 7), (Queen, 3, 5),
                     (Queen, 4, 8), (Queen, 5, 1), (Queen, 6, 4),
                     (Queen, 7, 6), (Queen, 8, 3)],
                    [(Queen, 1, 2), (Queen, 2, 8), (Queen, 3, 6),
                     (Queen, 4, 1), (Queen, 5, 3), (Queen, 6, 5),
                     (Queen, 7, 7), (Queen, 8, 4)],
                    [(Queen, 1, 3), (Queen, 2, 1), (Queen, 3, 7),
                     (Queen, 4, 5), (Queen, 5, 8), (Queen, 6, 2),
                     (Queen, 7, 4), (Queen, 8, 6)],
                    [(Queen, 1, 3), (Queen, 2, 5), (Queen, 3, 2),
                     (Queen, 4, 8), (Queen, 5, 1), (Queen, 6, 7),
                     (Queen, 7, 4), (Queen, 8, 6)],
                    [(Queen, 1, 3), (Queen, 2, 5), (Queen, 3, 2),
                     (Queen, 4, 8), (Queen, 5, 6), (Queen, 6, 4),
                     (Queen, 7, 7), (Queen, 8, 1)],
                    [(Queen, 1, 3), (Queen, 2, 5), (Queen, 3, 7),
                     (Queen, 4, 1), (Queen, 5, 4), (Queen, 6, 2),
                     (Queen, 7, 8), (Queen, 8, 6)],
                    [(Queen, 1, 3), (Queen, 2, 5), (Queen, 3, 8),
                     (Queen, 4, 4), (Queen, 5, 1), (Queen, 6, 7),
                     (Queen, 7, 2), (Queen, 8, 6)],
                    [(Queen, 1, 3), (Queen, 2, 6), (Queen, 3, 2),
                     (Queen, 4, 5), (Queen, 5, 8), (Queen, 6, 1),
                     (Queen, 7, 7), (Queen, 8, 4)],
                    [(Queen, 1, 3), (Queen, 2, 6), (Queen, 3, 2),
                     (Queen, 4, 7), (Queen, 5, 1), (Queen, 6, 4),
                     (Queen, 7, 8), (Queen, 8, 5)],
                    [(Queen, 1, 3), (Queen, 2, 6), (Queen, 3, 2),
                     (Queen, 4, 7), (Queen, 5, 5), (Queen, 6, 1),
                     (Queen, 7, 8), (Queen, 8, 4)],
                    [(Queen, 1, 3), (Queen, 2, 6), (Queen, 3, 4),
                     (Queen, 4, 1), (Queen, 5, 8), (Queen, 6, 5),
                     (Queen, 7, 7), (Queen, 8, 2)],
                    [(Queen, 1, 3), (Queen, 2, 6), (Queen, 3, 4),
                     (Queen, 4, 2), (Queen, 5, 8), (Queen, 6, 5),
                     (Queen, 7, 7), (Queen, 8, 1)],
                    [(Queen, 1, 3), (Queen, 2, 6), (Queen, 3, 8),
                     (Queen, 4, 1), (Queen, 5, 4), (Queen, 6, 7),
                     (Queen, 7, 5), (Queen, 8, 2)],
                    [(Queen, 1, 3), (Queen, 2, 6), (Queen, 3, 8),
                     (Queen, 4, 1), (Queen, 5, 5), (Queen, 6, 7),
                     (Queen, 7, 2), (Queen, 8, 4)],
                    [(Queen, 1, 3), (Queen, 2, 6), (Queen, 3, 8),
                     (Queen, 4, 2), (Queen, 5, 4), (Queen, 6, 1),
                     (Queen, 7, 7), (Queen, 8, 5)],
                    [(Queen, 1, 3), (Queen, 2, 7), (Queen, 3, 2),
                     (Queen, 4, 8), (Queen, 5, 5), (Queen, 6, 1),
                     (Queen, 7, 4), (Queen, 8, 6)],
                    [(Queen, 1, 3), (Queen, 2, 7), (Queen, 3, 2),
                     (Queen, 4, 8), (Queen, 5, 6), (Queen, 6, 4),
                     (Queen, 7, 1), (Queen, 8, 5)],
                    [(Queen, 1, 3), (Queen, 2, 8), (Queen, 3, 4),
                     (Queen, 4, 7), (Queen, 5, 1), (Queen, 6, 6),
                     (Queen, 7, 2), (Queen, 8, 5)],
                    [(Queen, 1, 4), (Queen, 2, 1), (Queen, 3, 5),
                     (Queen, 4, 8), (Queen, 5, 2), (Queen, 6, 7),
                     (Queen, 7, 3), (Queen, 8, 6)],
                    [(Queen, 1, 4), (Queen, 2, 1), (Queen, 3, 5),
                     (Queen, 4, 8), (Queen, 5, 6), (Queen, 6, 3),
                     (Queen, 7, 7), (Queen, 8, 2)],
                    [(Queen, 1, 4), (Queen, 2, 2), (Queen, 3, 5),
                     (Queen, 4, 8), (Queen, 5, 6), (Queen, 6, 1),
                     (Queen, 7, 3), (Queen, 8, 7)],
                    [(Queen, 1, 4), (Queen, 2, 2), (Queen, 3, 7),
                     (Queen, 4, 3), (Queen, 5, 6), (Queen, 6, 8),
                     (Queen, 7, 1), (Queen, 8, 5)],
                    [(Queen, 1, 4), (Queen, 2, 2), (Queen, 3, 7),
                     (Queen, 4, 3), (Queen, 5, 6), (Queen, 6, 8),
                     (Queen, 7, 5), (Queen, 8, 1)],
                    [(Queen, 1, 4), (Queen, 2, 2), (Queen, 3, 7),
                     (Queen, 4, 5), (Queen, 5, 1), (Queen, 6, 8),
                     (Queen, 7, 6), (Queen, 8, 3)],
                    [(Queen, 1, 4), (Queen, 2, 2), (Queen, 3, 8),
                     (Queen, 4, 5), (Queen, 5, 7), (Queen, 6, 1),
                     (Queen, 7, 3), (Queen, 8, 6)],
                    [(Queen, 1, 4), (Queen, 2, 2), (Queen, 3, 8),
                     (Queen, 4, 6), (Queen, 5, 1), (Queen, 6, 3),
                     (Queen, 7, 5), (Queen, 8, 7)],
                    [(Queen, 1, 4), (Queen, 2, 6), (Queen, 3, 1),
                     (Queen, 4, 5), (Queen, 5, 2), (Queen, 6, 8),
                     (Queen, 7, 3), (Queen, 8, 7)],
                    [(Queen, 1, 4), (Queen, 2, 6), (Queen, 3, 8),
                     (Queen, 4, 2), (Queen, 5, 7), (Queen, 6, 1),
                     (Queen, 7, 3), (Queen, 8, 5)],
                    [(Queen, 1, 4), (Queen, 2, 6), (Queen, 3, 8),
                     (Queen, 4, 3), (Queen, 5, 1), (Queen, 6, 7),
                     (Queen, 7, 5), (Queen, 8, 2)],
                    [(Queen, 1, 4), (Queen, 2, 7), (Queen, 3, 1),
                     (Queen, 4, 8), (Queen, 5, 5), (Queen, 6, 2),
                     (Queen, 7, 6), (Queen, 8, 3)],
                    [(Queen, 1, 4), (Queen, 2, 7), (Queen, 3, 3),
                     (Queen, 4, 8), (Queen, 5, 2), (Queen, 6, 5),
                     (Queen, 7, 1), (Queen, 8, 6)],
                    [(Queen, 1, 4), (Queen, 2, 7), (Queen, 3, 5),
                     (Queen, 4, 2), (Queen, 5, 6), (Queen, 6, 1),
                     (Queen, 7, 3), (Queen, 8, 8)],
                    [(Queen, 1, 4), (Queen, 2, 7), (Queen, 3, 5),
                     (Queen, 4, 3), (Queen, 5, 1), (Queen, 6, 6),
                     (Queen, 7, 8), (Queen, 8, 2)],
                    [(Queen, 1, 4), (Queen, 2, 8), (Queen, 3, 1),
                     (Queen, 4, 3), (Queen, 5, 6), (Queen, 6, 2),
                     (Queen, 7, 7), (Queen, 8, 5)],
                    [(Queen, 1, 4), (Queen, 2, 8), (Queen, 3, 1),
                     (Queen, 4, 5), (Queen, 5, 7), (Queen, 6, 2),
                     (Queen, 7, 6), (Queen, 8, 3)],
                    [(Queen, 1, 4), (Queen, 2, 8), (Queen, 3, 5),
                     (Queen, 4, 3), (Queen, 5, 1), (Queen, 6, 7),
                     (Queen, 7, 2), (Queen, 8, 6)],
                    [(Queen, 1, 5), (Queen, 2, 1), (Queen, 3, 4),
                     (Queen, 4, 6), (Queen, 5, 8), (Queen, 6, 2),
                     (Queen, 7, 7), (Queen, 8, 3)],
                    [(Queen, 1, 5), (Queen, 2, 1), (Queen, 3, 8),
                     (Queen, 4, 4), (Queen, 5, 2), (Queen, 6, 7),
                     (Queen, 7, 3), (Queen, 8, 6)],
                    [(Queen, 1, 5), (Queen, 2, 1), (Queen, 3, 8),
                     (Queen, 4, 6), (Queen, 5, 3), (Queen, 6, 7),
                     (Queen, 7, 2), (Queen, 8, 4)],
                    [(Queen, 1, 5), (Queen, 2, 2), (Queen, 3, 4),
                     (Queen, 4, 6), (Queen, 5, 8), (Queen, 6, 3),
                     (Queen, 7, 1), (Queen, 8, 7)],
                    [(Queen, 1, 5), (Queen, 2, 2), (Queen, 3, 4),
                     (Queen, 4, 7), (Queen, 5, 3), (Queen, 6, 8),
                     (Queen, 7, 6), (Queen, 8, 1)],
                    [(Queen, 1, 5), (Queen, 2, 2), (Queen, 3, 6),
                     (Queen, 4, 1), (Queen, 5, 7), (Queen, 6, 4),
                     (Queen, 7, 8), (Queen, 8, 3)],
                    [(Queen, 1, 5), (Queen, 2, 2), (Queen, 3, 8),
                     (Queen, 4, 1), (Queen, 5, 4), (Queen, 6, 7),
                     (Queen, 7, 3), (Queen, 8, 6)],
                    [(Queen, 1, 5), (Queen, 2, 3), (Queen, 3, 1),
                     (Queen, 4, 6), (Queen, 5, 8), (Queen, 6, 2),
                     (Queen, 7, 4), (Queen, 8, 7)],
                    [(Queen, 1, 5), (Queen, 2, 3), (Queen, 3, 1),
                     (Queen, 4, 7), (Queen, 5, 2), (Queen, 6, 8),
                     (Queen, 7, 6), (Queen, 8, 4)],
                    [(Queen, 1, 5), (Queen, 2, 3), (Queen, 3, 8),
                     (Queen, 4, 4), (Queen, 5, 7), (Queen, 6, 1),
                     (Queen, 7, 6), (Queen, 8, 2)],
                    [(Queen, 1, 5), (Queen, 2, 7), (Queen, 3, 1),
                     (Queen, 4, 3), (Queen, 5, 8), (Queen, 6, 6),
                     (Queen, 7, 4), (Queen, 8, 2)],
                    [(Queen, 1, 5), (Queen, 2, 7), (Queen, 3, 1),
                     (Queen, 4, 4), (Queen, 5, 2), (Queen, 6, 8),
                     (Queen, 7, 6), (Queen, 8, 3)],
                    [(Queen, 1, 5), (Queen, 2, 7), (Queen, 3, 2),
                     (Queen, 4, 4), (Queen, 5, 8), (Queen, 6, 1),
                     (Queen, 7, 3), (Queen, 8, 6)],
                    [(Queen, 1, 5), (Queen, 2, 7), (Queen, 3, 2),
                     (Queen, 4, 6), (Queen, 5, 3), (Queen, 6, 1),
                     (Queen, 7, 4), (Queen, 8, 8)],
                    [(Queen, 1, 5), (Queen, 2, 7), (Queen, 3, 2),
                     (Queen, 4, 6), (Queen, 5, 3), (Queen, 6, 1),
                     (Queen, 7, 8), (Queen, 8, 4)],
                    [(Queen, 1, 5), (Queen, 2, 7), (Queen, 3, 4),
                     (Queen, 4, 1), (Queen, 5, 3), (Queen, 6, 8),
                     (Queen, 7, 6), (Queen, 8, 2)],
                    [(Queen, 1, 5), (Queen, 2, 8), (Queen, 3, 4),
                     (Queen, 4, 1), (Queen, 5, 3), (Queen, 6, 6),
                     (Queen, 7, 2), (Queen, 8, 7)],
                    [(Queen, 1, 5), (Queen, 2, 8), (Queen, 3, 4),
                     (Queen, 4, 1), (Queen, 5, 7), (Queen, 6, 2),
                     (Queen, 7, 6), (Queen, 8, 3)],
                    [(Queen, 1, 6), (Queen, 2, 1), (Queen, 3, 5),
                     (Queen, 4, 2), (Queen, 5, 8), (Queen, 6, 3),
                     (Queen, 7, 7), (Queen, 8, 4)],
                    [(Queen, 1, 6), (Queen, 2, 2), (Queen, 3, 7),
                     (Queen, 4, 1), (Queen, 5, 3), (Queen, 6, 5),
                     (Queen, 7, 8), (Queen, 8, 4)],
                    [(Queen, 1, 6), (Queen, 2, 2), (Queen, 3, 7),
                     (Queen, 4, 1), (Queen, 5, 4), (Queen, 6, 8),
                     (Queen, 7, 5), (Queen, 8, 3)],
                    [(Queen, 1, 6), (Queen, 2, 3), (Queen, 3, 1),
                     (Queen, 4, 7), (Queen, 5, 5), (Queen, 6, 8),
                     (Queen, 7, 2), (Queen, 8, 4)],
                    [(Queen, 1, 6), (Queen, 2, 3), (Queen, 3, 1),
                     (Queen, 4, 8), (Queen, 5, 4), (Queen, 6, 2),
                     (Queen, 7, 7), (Queen, 8, 5)],
                    [(Queen, 1, 6), (Queen, 2, 3), (Queen, 3, 1),
                     (Queen, 4, 8), (Queen, 5, 5), (Queen, 6, 2),
                     (Queen, 7, 4), (Queen, 8, 7)],
                    [(Queen, 1, 6), (Queen, 2, 3), (Queen, 3, 5),
                     (Queen, 4, 7), (Queen, 5, 1), (Queen, 6, 4),
                     (Queen, 7, 2), (Queen, 8, 8)],
                    [(Queen, 1, 6), (Queen, 2, 3), (Queen, 3, 5),
                     (Queen, 4, 8), (Queen, 5, 1), (Queen, 6, 4),
                     (Queen, 7, 2), (Queen, 8, 7)],
                    [(Queen, 1, 6), (Queen, 2, 3), (Queen, 3, 7),
                     (Queen, 4, 2), (Queen, 5, 4), (Queen, 6, 8),
                     (Queen, 7, 1), (Queen, 8, 5)],
                    [(Queen, 1, 6), (Queen, 2, 3), (Queen, 3, 7),
                     (Queen, 4, 2), (Queen, 5, 8), (Queen, 6, 5),
                     (Queen, 7, 1), (Queen, 8, 4)],
                    [(Queen, 1, 6), (Queen, 2, 3), (Queen, 3, 7),
                     (Queen, 4, 4), (Queen, 5, 1), (Queen, 6, 8),
                     (Queen, 7, 2), (Queen, 8, 5)],
                    [(Queen, 1, 6), (Queen, 2, 4), (Queen, 3, 1),
                     (Queen, 4, 5), (Queen, 5, 8), (Queen, 6, 2),
                     (Queen, 7, 7), (Queen, 8, 3)],
                    [(Queen, 1, 6), (Queen, 2, 4), (Queen, 3, 2),
                     (Queen, 4, 8), (Queen, 5, 5), (Queen, 6, 7),
                     (Queen, 7, 1), (Queen, 8, 3)],
                    [(Queen, 1, 6), (Queen, 2, 4), (Queen, 3, 7),
                     (Queen, 4, 1), (Queen, 5, 3), (Queen, 6, 5),
                     (Queen, 7, 2), (Queen, 8, 8)],
                    [(Queen, 1, 6), (Queen, 2, 4), (Queen, 3, 7),
                     (Queen, 4, 1), (Queen, 5, 8), (Queen, 6, 2),
                     (Queen, 7, 5), (Queen, 8, 3)],
                    [(Queen, 1, 6), (Queen, 2, 8), (Queen, 3, 2),
                     (Queen, 4, 4), (Queen, 5, 1), (Queen, 6, 7),
                     (Queen, 7, 5), (Queen, 8, 3)],
                    [(Queen, 1, 7), (Queen, 2, 1), (Queen, 3, 3),
                     (Queen, 4, 8), (Queen, 5, 6), (Queen, 6, 4),
                     (Queen, 7, 2), (Queen, 8, 5)],
                    [(Queen, 1, 7), (Queen, 2, 2), (Queen, 3, 4),
                     (Queen, 4, 1), (Queen, 5, 8), (Queen, 6, 5),
                     (Queen, 7, 3), (Queen, 8, 6)],
                    [(Queen, 1, 7), (Queen, 2, 2), (Queen, 3, 6),
                     (Queen, 4, 3), (Queen, 5, 1), (Queen, 6, 4),
                     (Queen, 7, 8), (Queen, 8, 5)],
                    [(Queen, 1, 7), (Queen, 2, 3), (Queen, 3, 1),
                     (Queen, 4, 6), (Queen, 5, 8), (Queen, 6, 5),
                     (Queen, 7, 2), (Queen, 8, 4)],
                    [(Queen, 1, 7), (Queen, 2, 3), (Queen, 3, 8),
                     (Queen, 4, 2), (Queen, 5, 5), (Queen, 6, 1),
                     (Queen, 7, 6), (Queen, 8, 4)],
                    [(Queen, 1, 7), (Queen, 2, 4), (Queen, 3, 2),
                     (Queen, 4, 5), (Queen, 5, 8), (Queen, 6, 1),
                     (Queen, 7, 3), (Queen, 8, 6)],
                    [(Queen, 1, 7), (Queen, 2, 4), (Queen, 3, 2),
                     (Queen, 4, 8), (Queen, 5, 6), (Queen, 6, 1),
                     (Queen, 7, 3), (Queen, 8, 5)],
                    [(Queen, 1, 7), (Queen, 2, 5), (Queen, 3, 3),
                     (Queen, 4, 1), (Queen, 5, 6), (Queen, 6, 8),
                     (Queen, 7, 2), (Queen, 8, 4)],
                    [(Queen, 1, 8), (Queen, 2, 2), (Queen, 3, 4),
                     (Queen, 4, 1), (Queen, 5, 7), (Queen, 6, 5),
                     (Queen, 7, 3), (Queen, 8, 6)],
                    [(Queen, 1, 8), (Queen, 2, 2), (Queen, 3, 5),
                     (Queen, 4, 3), (Queen, 5, 1), (Queen, 6, 7),
                     (Queen, 7, 4), (Queen, 8, 6)],
                    [(Queen, 1, 8), (Queen, 2, 3), (Queen, 3, 1),
                     (Queen, 4, 6), (Queen, 5, 2), (Queen, 6, 5),
                     (Queen, 7, 7), (Queen, 8, 4)],
                    [(Queen, 1, 8), (Queen, 2, 4), (Queen, 3, 1),
                     (Queen, 4, 3),
                     (Queen, 5, 6), (Queen, 6, 2), (Queen, 7, 7),
                     (Queen, 8, 5)]]
        result = engine.execute()
        self.assertEqual(sorted(expected), sorted(result))

    def test_3_bishops_3_by_3_board(self):
        """Test 3 bishops, 3 by 3 board."""
        expected = [[(Bishop, 1, 1), (Bishop, 1, 2), (Bishop, 1, 3)],
                    [(Bishop, 1, 1), (Bishop, 1, 2), (Bishop, 3, 1)],
                    [(Bishop, 1, 1), (Bishop, 1, 2), (Bishop, 3, 2)],
                    [(Bishop, 1, 1), (Bishop, 1, 3), (Bishop, 2, 1)],
                    [(Bishop, 1, 1), (Bishop, 1, 3), (Bishop, 2, 3)],
                    [(Bishop, 1, 1), (Bishop, 1, 3), (Bishop, 3, 2)],
                    [(Bishop, 1, 1), (Bishop, 2, 1), (Bishop, 2, 3)],
                    [(Bishop, 1, 1), (Bishop, 2, 1), (Bishop, 3, 1)],
                    [(Bishop, 1, 1), (Bishop, 2, 3), (Bishop, 3, 1)],
                    [(Bishop, 1, 1), (Bishop, 3, 1), (Bishop, 3, 2)],
                    [(Bishop, 1, 2), (Bishop, 1, 3), (Bishop, 3, 2)],
                    [(Bishop, 1, 2), (Bishop, 1, 3), (Bishop, 3, 3)],
                    [(Bishop, 1, 2), (Bishop, 2, 2), (Bishop, 3, 2)],
                    [(Bishop, 1, 2), (Bishop, 3, 1), (Bishop, 3, 2)],
                    [(Bishop, 1, 2), (Bishop, 3, 1), (Bishop, 3, 3)],
                    [(Bishop, 1, 2), (Bishop, 3, 2), (Bishop, 3, 3)],
                    [(Bishop, 1, 3), (Bishop, 2, 1), (Bishop, 2, 3)],
                    [(Bishop, 1, 3), (Bishop, 2, 1), (Bishop, 3, 3)],
                    [(Bishop, 1, 3), (Bishop, 2, 3), (Bishop, 3, 3)],
                    [(Bishop, 1, 3), (Bishop, 3, 2), (Bishop, 3, 3)],
                    [(Bishop, 2, 1), (Bishop, 2, 2), (Bishop, 2, 3)],
                    [(Bishop, 2, 1), (Bishop, 2, 3), (Bishop, 3, 1)],
                    [(Bishop, 2, 1), (Bishop, 2, 3), (Bishop, 3, 3)],
                    [(Bishop, 2, 1), (Bishop, 3, 1), (Bishop, 3, 3)],
                    [(Bishop, 2, 3), (Bishop, 3, 1), (Bishop, 3, 3)],
                    [(Bishop, 3, 1), (Bishop, 3, 2), (Bishop, 3, 3)]
                    ]

        pieces = [Bishop, Bishop, Bishop]
        engine = ChessChallengeEngine(pieces, len(pieces), len(pieces))
        result = engine.execute()
        self.assertEqual(sorted(expected), sorted(result))

    def test_2_knights_1_bishop_3_by_3_board(self):
        """Test 2 knights, 1 bishop, 3 by 3 board."""
        expected = [[(Bishop, 1, 1), (Knight, 1, 2), (Knight, 1, 3)],
                    [(Bishop, 1, 1), (Knight, 1, 2), (Knight, 2, 1)],
                    [(Bishop, 1, 1), (Knight, 1, 3), (Knight, 3, 1)],
                    [(Bishop, 1, 1), (Knight, 2, 1), (Knight, 3, 1)],
                    [(Bishop, 1, 2), (Knight, 1, 1), (Knight, 1, 3)],
                    [(Bishop, 1, 2), (Knight, 1, 1), (Knight, 2, 2)],
                    [(Bishop, 1, 2), (Knight, 1, 3), (Knight, 2, 2)],
                    [(Bishop, 1, 2), (Knight, 2, 2), (Knight, 3, 2)],
                    [(Bishop, 1, 3), (Knight, 1, 1), (Knight, 1, 2)],
                    [(Bishop, 1, 3), (Knight, 1, 1), (Knight, 3, 3)],
                    [(Bishop, 1, 3), (Knight, 1, 2), (Knight, 2, 3)],
                    [(Bishop, 1, 3), (Knight, 2, 3), (Knight, 3, 3)],
                    [(Bishop, 2, 1), (Knight, 1, 1), (Knight, 2, 2)],
                    [(Bishop, 2, 1), (Knight, 1, 1), (Knight, 3, 1)],
                    [(Bishop, 2, 1), (Knight, 2, 2), (Knight, 2, 3)],
                    [(Bishop, 2, 1), (Knight, 2, 2), (Knight, 3, 1)],
                    [(Bishop, 2, 2), (Knight, 1, 2), (Knight, 2, 1)],
                    [(Bishop, 2, 2), (Knight, 1, 2), (Knight, 2, 3)],
                    [(Bishop, 2, 2), (Knight, 1, 2), (Knight, 3, 2)],
                    [(Bishop, 2, 2), (Knight, 2, 1), (Knight, 2, 3)],
                    [(Bishop, 2, 2), (Knight, 2, 1), (Knight, 3, 2)],
                    [(Bishop, 2, 2), (Knight, 2, 3), (Knight, 3, 2)],
                    [(Bishop, 2, 3), (Knight, 1, 3), (Knight, 2, 2)],
                    [(Bishop, 2, 3), (Knight, 1, 3), (Knight, 3, 3)],
                    [(Bishop, 2, 3), (Knight, 2, 1), (Knight, 2, 2)],
                    [(Bishop, 2, 3), (Knight, 2, 2), (Knight, 3, 3)],
                    [(Bishop, 3, 1), (Knight, 1, 1), (Knight, 2, 1)],
                    [(Bishop, 3, 1), (Knight, 1, 1), (Knight, 3, 3)],
                    [(Bishop, 3, 1), (Knight, 2, 1), (Knight, 3, 2)],
                    [(Bishop, 3, 1), (Knight, 3, 2), (Knight, 3, 3)],
                    [(Bishop, 3, 2), (Knight, 1, 2), (Knight, 2, 2)],
                    [(Bishop, 3, 2), (Knight, 2, 2), (Knight, 3, 1)],
                    [(Bishop, 3, 2), (Knight, 2, 2), (Knight, 3, 3)],
                    [(Bishop, 3, 2), (Knight, 3, 1), (Knight, 3, 3)],
                    [(Bishop, 3, 3), (Knight, 1, 3), (Knight, 2, 3)],
                    [(Bishop, 3, 3), (Knight, 1, 3), (Knight, 3, 1)],
                    [(Bishop, 3, 3), (Knight, 2, 3), (Knight, 3, 2)],
                    [(Bishop, 3, 3), (Knight, 3, 1), (Knight, 3, 2)]
                    ]
        pieces = [Bishop, Knight, Knight]
        engine = ChessChallengeEngine(pieces, len(pieces), len(pieces))
        result = engine.execute()
        self.assertEqual(sorted(expected), sorted(result))

    def test_impossible_configuration(self):
        """Test 8 queens in a 6 * 6 board."""
        expected = [[]]
        pieces = [Queen] * 8
        engine = ChessChallengeEngine(pieces, 6, 6)
        result = engine.execute()
        self.assertEqual(sorted(expected), sorted(result))

    def test_1_king_3_by_3_board(self):
        """Test 1 king, 3 by 3 board."""
        expected = [
            [(King, 1, 1)],
            [(King, 1, 2)],
            [(King, 1, 3)],
            [(King, 2, 1)],
            [(King, 2, 2)],
            [(King, 2, 3)],
            [(King, 3, 1)],
            [(King, 3, 2)],
            [(King, 3, 3)]
        ]
        pieces = [King]
        engine = ChessChallengeEngine(pieces, 3, 3)
        result = engine.execute()
        self.assertEqual(sorted(expected), sorted(result))

    def test_1_queen_3_by_3_board(self):
        """Test 1 queen, 3 by 3 board."""
        expected = [
            [(Queen, 1, 1)],
            [(Queen, 1, 2)],
            [(Queen, 1, 3)],
            [(Queen, 2, 1)],
            [(Queen, 2, 2)],
            [(Queen, 2, 3)],
            [(Queen, 3, 1)],
            [(Queen, 3, 2)],
            [(Queen, 3, 3)]
        ]
        pieces = [Queen]
        engine = ChessChallengeEngine(pieces, 3, 3)
        result = engine.execute()
        self.assertEqual(sorted(expected), sorted(result))

    def test_2_kings_3_by_3_board(self):
        """Test 2 kings, 3 by 3 board."""
        expected = [
            [(King, 1, 1), (King, 1, 3)],
            [(King, 1, 1), (King, 2, 3)],
            [(King, 1, 1), (King, 3, 1)],
            [(King, 1, 1), (King, 3, 2)],
            [(King, 1, 1), (King, 3, 3)],
            [(King, 1, 2), (King, 3, 1)],
            [(King, 1, 2), (King, 3, 2)],
            [(King, 1, 2), (King, 3, 3)],
            [(King, 1, 3), (King, 2, 1)],
            [(King, 1, 3), (King, 3, 1)],
            [(King, 1, 3), (King, 3, 2)],
            [(King, 1, 3), (King, 3, 3)],
            [(King, 2, 1), (King, 2, 3)],
            [(King, 2, 1), (King, 3, 3)],
            [(King, 2, 3), (King, 3, 1)],
            [(King, 3, 1), (King, 3, 3)]
        ]
        pieces = [King, King]
        engine = ChessChallengeEngine(pieces, 3, 3)
        result = engine.execute()
        self.assertEqual(sorted(expected), sorted(result))

    def test_1_knight_3_by_3_board(self):
        """Test 1 knight, 3 by 3 board."""
        expected = [
            [(Knight, 1, 1)],
            [(Knight, 1, 2)],
            [(Knight, 1, 3)],
            [(Knight, 2, 1)],
            [(Knight, 2, 2)],
            [(Knight, 2, 3)],
            [(Knight, 3, 1)],
            [(Knight, 3, 2)],
            [(Knight, 3, 3)]
        ]
        pieces = [Knight]
        engine = ChessChallengeEngine(pieces, 3, 3)
        result = engine.execute()
        self.assertEqual(sorted(expected), sorted(result))

    def test_2_knights_3_by_3_board(self):
        """Test 2 knights, 3 by 3 board."""
        expected = [
            [(Knight, 1, 1), (Knight, 1, 2)],
            [(Knight, 1, 1), (Knight, 1, 3)],
            [(Knight, 1, 1), (Knight, 2, 1)],
            [(Knight, 1, 1), (Knight, 2, 2)],
            [(Knight, 1, 1), (Knight, 3, 1)],
            [(Knight, 1, 1), (Knight, 3, 3)],
            [(Knight, 1, 2), (Knight, 1, 3)],
            [(Knight, 1, 2), (Knight, 2, 1)],
            [(Knight, 1, 2), (Knight, 2, 2)],
            [(Knight, 1, 2), (Knight, 2, 3)],
            [(Knight, 1, 2), (Knight, 3, 2)],
            [(Knight, 1, 3), (Knight, 2, 2)],
            [(Knight, 1, 3), (Knight, 2, 3)],
            [(Knight, 1, 3), (Knight, 3, 1)],
            [(Knight, 1, 3), (Knight, 3, 3)],
            [(Knight, 2, 1), (Knight, 2, 2)],
            [(Knight, 2, 1), (Knight, 2, 3)],
            [(Knight, 2, 1), (Knight, 3, 1)],
            [(Knight, 2, 1), (Knight, 3, 2)],
            [(Knight, 2, 2), (Knight, 2, 3)],
            [(Knight, 2, 2), (Knight, 3, 1)],
            [(Knight, 2, 2), (Knight, 3, 2)],
            [(Knight, 2, 2), (Knight, 3, 3)],
            [(Knight, 2, 3), (Knight, 3, 2)],
            [(Knight, 2, 3), (Knight, 3, 3)],
            [(Knight, 3, 1), (Knight, 3, 2)],
            [(Knight, 3, 1), (Knight, 3, 3)],
            [(Knight, 3, 2), (Knight, 3, 3)]
        ]
        pieces = [Knight, Knight]
        engine = ChessChallengeEngine(pieces, 3, 3)
        result = engine.execute()
        self.assertEqual(sorted(expected), sorted(result))

    def test_4_knights_2_rooks_4_by_4_board(self):
        """Test 4 knights, 2 rooks, 4 x 4 board.

        One of the given examples.
        """
        expected = [
            [(Knight, 1, 1), (Knight, 1, 3), (Knight, 3, 1),
             (Knight, 3, 3), (Rook, 2, 2), (Rook, 4, 4)],
            [(Knight, 1, 1), (Knight, 1, 3), (Knight, 3, 1),
             (Knight, 3, 3), (Rook, 2, 4), (Rook, 4, 2)],
            [(Knight, 1, 2), (Knight, 1, 4), (Knight, 3, 2),
             (Knight, 3, 4), (Rook, 2, 1), (Rook, 4, 3)],
            [(Knight, 1, 2), (Knight, 1, 4), (Knight, 3, 2),
             (Knight, 3, 4), (Rook, 2, 3), (Rook, 4, 1)],
            [(Knight, 2, 1), (Knight, 2, 3), (Knight, 4, 1),
             (Knight, 4, 3), (Rook, 1, 2), (Rook, 3, 4)],
            [(Knight, 2, 1), (Knight, 2, 3), (Knight, 4, 1),
             (Knight, 4, 3), (Rook, 1, 4), (Rook, 3, 2)],
            [(Knight, 2, 2), (Knight, 2, 4), (Knight, 4, 2),
             (Knight, 4, 4), (Rook, 1, 1), (Rook, 3, 3)],
            [(Knight, 2, 2), (Knight, 2, 4), (Knight, 4, 2),
             (Knight, 4, 4), (Rook, 1, 3), (Rook, 3, 1)]
        ]

        pieces = [Knight, Knight, Knight, Knight, Rook, Rook]
        engine = ChessChallengeEngine(pieces, 4, 4)
        result = engine.execute()
        self.assertEqual(sorted(expected), sorted(result))

    def test_2_kings_1_rook_3_by_3_board(self):
        """Test 2 kings, 1 rook, 3 by 3 board.

        One of the given examples.
        """
        expected = [
            [(King, 1, 1), (King, 1, 3), (Rook, 3, 2)],
            [(King, 1, 1), (King, 3, 1), (Rook, 2, 3)],
            [(King, 1, 3), (King, 3, 3), (Rook, 2, 1)],
            [(King, 3, 1), (King, 3, 3), (Rook, 1, 2)],

        ]

        pieces = [King, King, Rook]
        engine = ChessChallengeEngine(pieces, 3, 3)
        result = engine.execute()
        self.assertListEqual(sorted(expected), sorted(result))

    def test_1_queen_1_knight_3_by_3_board(self):
        """Test 1 queen, 1 knight, 3 by 3 board.

        That should result in 0 valid configurations
        """
        expected = []
        pieces = [Knight, Queen]
        engine = ChessChallengeEngine(pieces, 3, 3)
        result = engine.execute()
        self.assertListEqual(sorted(expected), sorted(result))

    def test_1_queen_1_knight_4_by_4_board(self):
        """Test 1 queen, 1 knight, 4 by 4 board."""
        expected = [
            [(Knight, 1, 1), (Queen, 2, 4)],
            [(Knight, 1, 1), (Queen, 3, 4)],
            [(Knight, 1, 1), (Queen, 4, 2)],
            [(Knight, 1, 1), (Queen, 4, 3)],
            [(Knight, 1, 2), (Queen, 4, 1)],
            [(Knight, 1, 2), (Queen, 4, 3)],
            [(Knight, 1, 2), (Queen, 4, 4)],
            [(Knight, 1, 3), (Queen, 4, 1)],
            [(Knight, 1, 3), (Queen, 4, 2)],
            [(Knight, 1, 3), (Queen, 4, 4)],
            [(Knight, 1, 4), (Queen, 2, 1)],
            [(Knight, 1, 4), (Queen, 3, 1)],
            [(Knight, 1, 4), (Queen, 4, 2)],
            [(Knight, 1, 4), (Queen, 4, 3)],
            [(Knight, 2, 1), (Queen, 1, 4)],
            [(Knight, 2, 1), (Queen, 3, 4)],
            [(Knight, 2, 1), (Queen, 4, 4)],
            [(Knight, 2, 4), (Queen, 1, 1)],
            [(Knight, 2, 4), (Queen, 3, 1)],
            [(Knight, 2, 4), (Queen, 4, 1)],
            [(Knight, 3, 1), (Queen, 1, 4)],
            [(Knight, 3, 1), (Queen, 2, 4)],
            [(Knight, 3, 1), (Queen, 4, 4)],
            [(Knight, 3, 4), (Queen, 1, 1)],
            [(Knight, 3, 4), (Queen, 2, 1)],
            [(Knight, 3, 4), (Queen, 4, 1)],
            [(Knight, 4, 1), (Queen, 1, 2)],
            [(Knight, 4, 1), (Queen, 1, 3)],
            [(Knight, 4, 1), (Queen, 2, 4)],
            [(Knight, 4, 1), (Queen, 3, 4)],
            [(Knight, 4, 2), (Queen, 1, 1)],
            [(Knight, 4, 2), (Queen, 1, 3)],
            [(Knight, 4, 2), (Queen, 1, 4)],
            [(Knight, 4, 3), (Queen, 1, 1)],
            [(Knight, 4, 3), (Queen, 1, 2)],
            [(Knight, 4, 3), (Queen, 1, 4)],
            [(Knight, 4, 4), (Queen, 1, 2)],
            [(Knight, 4, 4), (Queen, 1, 3)],
            [(Knight, 4, 4), (Queen, 2, 1)],
            [(Knight, 4, 4), (Queen, 3, 1)],
        ]
        pieces = [Knight, Queen]
        engine = ChessChallengeEngine(pieces, 4, 4)
        result = engine.execute()
        self.assertListEqual(sorted(expected), sorted(result))

    def test_1_rook_1_bishop_3_by_3_board(self):
        """Test 1 rook 1 bishop 3 by 3 board."""
        expected = [
            [(Bishop, 1, 1), (Rook, 2, 3)],
            [(Bishop, 1, 1), (Rook, 3, 2)],
            [(Bishop, 1, 2), (Rook, 3, 1)],
            [(Bishop, 1, 2), (Rook, 3, 3)],
            [(Bishop, 1, 3), (Rook, 2, 1)],
            [(Bishop, 1, 3), (Rook, 3, 2)],
            [(Bishop, 2, 1), (Rook, 1, 3)],
            [(Bishop, 2, 1), (Rook, 3, 3)],
            [(Bishop, 2, 3), (Rook, 1, 1)],
            [(Bishop, 2, 3), (Rook, 3, 1)],
            [(Bishop, 3, 1), (Rook, 1, 2)],
            [(Bishop, 3, 1), (Rook, 2, 3)],
            [(Bishop, 3, 2), (Rook, 1, 1)],
            [(Bishop, 3, 2), (Rook, 1, 3)],
            [(Bishop, 3, 3), (Rook, 1, 2)],
            [(Bishop, 3, 3), (Rook, 2, 1)],
        ]
        pieces = [Bishop, Rook]
        engine = ChessChallengeEngine(pieces, 3, 3)
        result = engine.execute()
        self.assertListEqual(sorted(expected), sorted(result))

    def test_2_rooks_3_by_3_board(self):
        """Test two rooks on the same board."""
        expected = [
            [(Rook, 1, 1), (Rook, 2, 2)],
            [(Rook, 1, 1), (Rook, 2, 3)],
            [(Rook, 1, 1), (Rook, 3, 2)],
            [(Rook, 1, 1), (Rook, 3, 3)],
            [(Rook, 1, 2), (Rook, 2, 1)],
            [(Rook, 1, 2), (Rook, 2, 3)],
            [(Rook, 1, 2), (Rook, 3, 1)],
            [(Rook, 1, 2), (Rook, 3, 3)],
            [(Rook, 1, 3), (Rook, 2, 1)],
            [(Rook, 1, 3), (Rook, 2, 2)],
            [(Rook, 1, 3), (Rook, 3, 1)],
            [(Rook, 1, 3), (Rook, 3, 2)],
            [(Rook, 2, 1), (Rook, 3, 2)],
            [(Rook, 2, 1), (Rook, 3, 3)],
            [(Rook, 2, 2), (Rook, 3, 1)],
            [(Rook, 2, 2), (Rook, 3, 3)],
            [(Rook, 2, 3), (Rook, 3, 1)],
            [(Rook, 2, 3), (Rook, 3, 2)],
        ]
        pieces = [Rook, Rook]
        engine = ChessChallengeEngine(pieces, 3, 3)
        result = engine.execute()
        self.assertListEqual(sorted(expected), sorted(result))

    def test_1_queen_1_rook_3_by_3_board(self):
        """Test 1 queen, 1 rook 3 by 3 board."""
        expected = [
            [(Queen, 1, 1), (Rook, 2, 3)],
            [(Queen, 1, 1), (Rook, 3, 2)],
            [(Queen, 1, 2), (Rook, 3, 1)],
            [(Queen, 1, 2), (Rook, 3, 3)],
            [(Queen, 1, 3), (Rook, 2, 1)],
            [(Queen, 1, 3), (Rook, 3, 2)],
            [(Queen, 2, 1), (Rook, 1, 3)],
            [(Queen, 2, 1), (Rook, 3, 3)],
            [(Queen, 2, 3), (Rook, 1, 1)],
            [(Queen, 2, 3), (Rook, 3, 1)],
            [(Queen, 3, 1), (Rook, 1, 2)],
            [(Queen, 3, 1), (Rook, 2, 3)],
            [(Queen, 3, 2), (Rook, 1, 1)],
            [(Queen, 3, 2), (Rook, 1, 3)],
            [(Queen, 3, 3), (Rook, 1, 2)],
            [(Queen, 3, 3), (Rook, 2, 1)],
        ]

        pieces = [Queen, Rook]
        engine = ChessChallengeEngine(pieces, 3, 3)
        result = engine.execute()
        self.assertListEqual(sorted(expected), sorted(result))

    def test_1_king_1_bishop_3_by_3_board(self):
        """Test 1 king, 1 bishop, 3 by 3 board."""
        expected = [
            [(Bishop, 1, 1), (King, 1, 3)],
            [(Bishop, 1, 1), (King, 2, 3)],
            [(Bishop, 1, 1), (King, 3, 1)],
            [(Bishop, 1, 1), (King, 3, 2)],
            [(Bishop, 1, 2), (King, 3, 1)],
            [(Bishop, 1, 2), (King, 3, 2)],
            [(Bishop, 1, 2), (King, 3, 3)],
            [(Bishop, 1, 3), (King, 1, 1)],
            [(Bishop, 1, 3), (King, 2, 1)],
            [(Bishop, 1, 3), (King, 3, 2)],
            [(Bishop, 1, 3), (King, 3, 3)],
            [(Bishop, 2, 1), (King, 1, 3)],
            [(Bishop, 2, 1), (King, 2, 3)],
            [(Bishop, 2, 1), (King, 3, 3)],
            [(Bishop, 2, 3), (King, 1, 1)],
            [(Bishop, 2, 3), (King, 2, 1)],
            [(Bishop, 2, 3), (King, 3, 1)],
            [(Bishop, 3, 1), (King, 1, 1)],
            [(Bishop, 3, 1), (King, 1, 2)],
            [(Bishop, 3, 1), (King, 2, 3)],
            [(Bishop, 3, 1), (King, 3, 3)],
            [(Bishop, 3, 2), (King, 1, 1)],
            [(Bishop, 3, 2), (King, 1, 2)],
            [(Bishop, 3, 2), (King, 1, 3)],
            [(Bishop, 3, 3), (King, 1, 2)],
            [(Bishop, 3, 3), (King, 1, 3)],
            [(Bishop, 3, 3), (King, 2, 1)],
            [(Bishop, 3, 3), (King, 3, 1)]
        ]
        pieces = [King, Bishop]
        engine = ChessChallengeEngine(pieces, 3, 3)
        result = engine.execute()
        self.assertListEqual(sorted(expected), sorted(result))

    def test_king_knight(self):
        """Test 1 King, 1 Knight, 3 by 3 board."""
        expected = [
            [(King, 1, 3), (Knight, 1, 1)],
            [(King, 3, 1), (Knight, 1, 1)],
            [(King, 3, 3), (Knight, 1, 1)],
            [(King, 3, 2), (Knight, 1, 2)],
            [(King, 1, 1), (Knight, 1, 3)],
            [(King, 3, 1), (Knight, 1, 3)],
            [(King, 3, 3), (Knight, 1, 3)],
            [(King, 2, 3), (Knight, 2, 1)],
            [(King, 2, 1), (Knight, 2, 3)],
            [(King, 1, 1), (Knight, 3, 1)],
            [(King, 1, 3), (Knight, 3, 1)],
            [(King, 3, 3), (Knight, 3, 1)],
            [(King, 1, 2), (Knight, 3, 2)],
            [(King, 1, 1), (Knight, 3, 3)],
            [(King, 1, 3), (Knight, 3, 3)],
            [(King, 3, 1), (Knight, 3, 3)]
        ]
        pieces = [King, Knight]
        engine = ChessChallengeEngine(pieces, 3, 3)
        result = engine.execute()
        self.assertListEqual(sorted(expected), sorted(result))

    def test_bishop_queen(self):
        """Test 1 bishop, 1 queen, 3 by 3 board."""
        expected = [
            [(Bishop, 2, 3), (Queen, 1, 1)],
            [(Bishop, 3, 2), (Queen, 1, 1)],
            [(Bishop, 3, 1), (Queen, 1, 2)],
            [(Bishop, 3, 3), (Queen, 1, 2)],
            [(Bishop, 2, 1), (Queen, 1, 3)],
            [(Bishop, 3, 2), (Queen, 1, 3)],
            [(Bishop, 1, 3), (Queen, 2, 1)],
            [(Bishop, 3, 3), (Queen, 2, 1)],
            [(Bishop, 1, 1), (Queen, 2, 3)],
            [(Bishop, 3, 1), (Queen, 2, 3)],
            [(Bishop, 1, 2), (Queen, 3, 1)],
            [(Bishop, 2, 3), (Queen, 3, 1)],
            [(Bishop, 1, 1), (Queen, 3, 2)],
            [(Bishop, 1, 3), (Queen, 3, 2)],
            [(Bishop, 1, 2), (Queen, 3, 3)],
            [(Bishop, 2, 1), (Queen, 3, 3)],

        ]
        pieces = [Bishop, Queen]
        engine = ChessChallengeEngine(pieces, 3, 3)
        result = engine.execute()
        self.assertListEqual(sorted(expected), sorted(result))
        
if __name__ == '__main__':
    unittest.main()
