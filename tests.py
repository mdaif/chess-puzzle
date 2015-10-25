from chess_challenge import ChessChallengeEngine
from helpers import king_danger, knight_danger, diagonals_danger, \
    row_or_column_danger
import unittest


class HelpersTest(unittest.TestCase):
    def setUp(self):
        self.row = 5
        self.column = 4

    def test_king_danger_1(self):
        """A dangerous move, both pieces on the same square, one is king"""
        danger = king_danger(self.row, self.column, self.row, self.column)
        self.assertTrue(danger)

    def test_king_danger_2(self):
        """A dangerous move, a king is one square to the left"""
        danger = king_danger(self.row, self.column, self.row - 1, self.column)
        self.assertTrue(danger)

    def test_king_danger_3(self):
        """A dangerous move, a king is one square to the right"""
        danger = king_danger(self.row, self.column, self.row + 1, self.column)
        self.assertTrue(danger)

    def test_king_danger_4(self):
        """A dangerous move, a king is one square up"""
        danger = king_danger(self.row, self.column, self.row, self.column - 1)
        self.assertTrue(danger)

    def test_king_danger_5(self):
        """A dangerous move, a king is one square down"""
        danger = king_danger(self.row, self.column, self.row, self.column + 1)
        self.assertTrue(danger)

    def test_king_danger_6(self):
        """A dangerous move, a king is one square north-east"""
        danger = king_danger(self.row, self.column, self.row + 1,
                             self.column - 1)
        self.assertTrue(danger)

    def test_king_danger_7(self):
        """A dangerous move, a king is one square north-west"""
        danger = king_danger(self.row, self.column, self.row - 1,
                             self.column - 1)
        self.assertTrue(danger)

    def test_king_danger_8(self):
        """A dangerous move, a king is one square south-west"""
        danger = king_danger(self.row, self.column, self.row - 1,
                             self.column + 1)
        self.assertTrue(danger)

    def test_king_danger_9(self):
        """A dangerous move, a king is one square south-east"""
        danger = king_danger(self.row, self.column, self.row + 1,
                             self.column + 1)
        self.assertTrue(danger)

    def test_king_danger_10(self):
        """A safe move .. finally !"""
        danger = king_danger(self.row, self.column, self.row + 2, self.column)
        self.assertFalse(danger)

    def test_knight_danger_1(self):
        """A dangerous move, a knight is on the end of an L-shaped distance"""
        danger = knight_danger(self.row, self.column, self.row + 1,
                               self.column - 2)
        self.assertTrue(danger)

    def test_knight_danger_2(self):
        """A dangerous move, a knight is on the end of an L-shaped distance"""
        danger = knight_danger(self.row, self.column, self.row + 2,
                               self.column - 1)
        self.assertTrue(danger)

    def test_knight_danger_3(self):
        """A dangerous move, a knight is on the end of an L-shaped distance"""
        danger = knight_danger(self.row, self.column, self.row + 1,
                               self.column + 2)
        self.assertTrue(danger)

    def test_knight_danger_4(self):
        """A dangerous move, a knight is on the end of an L-shaped distance"""
        danger = knight_danger(self.row, self.column, self.row - 1,
                               self.column + 2)
        self.assertTrue(danger)

    def test_knight_danger_5(self):
        """A dangerous move, a knight is on the end of an L-shaped distance"""
        danger = knight_danger(self.row, self.column, self.row - 2,
                               self.column + 1)
        self.assertTrue(danger)

    def test_knight_danger_6(self):
        """A dangerous move, a knight is on the end of an L-shaped distance"""
        danger = knight_danger(self.row, self.column, self.row - 2,
                               self.column - 1)
        self.assertTrue(danger)

    def test_knight_danger_7(self):
        """A dangerous move, a knight is on the end of an L-shaped distance"""
        danger = knight_danger(self.row, self.column, self.row - 1,
                               self.column - 2)
        self.assertTrue(danger)

    def test_knight_danger_8(self):
        """A safe move"""
        danger = knight_danger(self.row, self.column, self.row - 1,
                               self.column - 1)
        self.assertFalse(danger)

    def test_diagonals_danger_1(self):
        """Two pieces are placed on the same diagonal"""
        danger = diagonals_danger(self.row, self.column, self.row + 2,
                                  self.column - 2)
        self.assertTrue(danger)

    def test_diagonals_danger_2(self):
        """Two pieces are placed on the same diagonal"""
        danger = diagonals_danger(self.row, self.column, self.row + 2,
                                  self.column + 2)
        self.assertTrue(danger)

    def test_diagonals_danger_3(self):
        """Two pieces are placed on the same diagonal"""
        danger = diagonals_danger(self.row, self.column, self.row - 2,
                                  self.column + 2)
        self.assertTrue(danger)

    def test_diagonals_danger_4(self):
        """Two pieces are placed on the same diagonal"""
        danger = diagonals_danger(self.row, self.column, self.row - 2,
                                  self.column - 2)
        self.assertTrue(danger)

    def test_diagonals_danger_5(self):
        """Two pieces are NOT placed on the same diagonal"""
        danger = diagonals_danger(self.row, self.column, self.row,
                                  self.column - 2)
        self.assertFalse(danger)

    def row_or_column_danger_1(self):
        """Two pieces on the same row but different columns"""

        danger = row_or_column_danger(self.row, self.column, self.row,
                                      self.column + 5)
        self.assertTrue(danger)

    def row_or_column_danger_2(self):
        """Two pieces on the same column but different rows"""

        danger = row_or_column_danger(self.row, self.column, self.row + 5,
                                      self.column)
        self.assertTrue(danger)

    def row_or_column_danger_3(self):
        """Two pieces on different rows and columns"""

        danger = row_or_column_danger(self.row, self.column, self.row + 5,
                                      self.column + 3)
        self.assertFalse(danger)


class ChessChallengeTest(unittest.TestCase):
    def test_normal_8_queens(self):
        """Happy path, simplest version of the problem 8 queens, 8 * 8 board"""

        pieces = ['Queen'] * 8
        engine = ChessChallengeEngine(pieces, len(pieces), len(pieces))
        expected = [[('Queen', 1, 1), ('Queen', 2, 5), ('Queen', 3, 8),
                     ('Queen', 4, 6), ('Queen', 5, 3), ('Queen', 6, 7),
                     ('Queen', 7, 2), ('Queen', 8, 4)],
                    [('Queen', 1, 1), ('Queen', 2, 6), ('Queen', 3, 8),
                     ('Queen', 4, 3), ('Queen', 5, 7), ('Queen', 6, 4),
                     ('Queen', 7, 2), ('Queen', 8, 5)],
                    [('Queen', 1, 1), ('Queen', 2, 7), ('Queen', 3, 4),
                     ('Queen', 4, 6), ('Queen', 5, 8), ('Queen', 6, 2),
                     ('Queen', 7, 5), ('Queen', 8, 3)],
                    [('Queen', 1, 1), ('Queen', 2, 7), ('Queen', 3, 5),
                     ('Queen', 4, 8), ('Queen', 5, 2), ('Queen', 6, 4),
                     ('Queen', 7, 6), ('Queen', 8, 3)],
                    [('Queen', 1, 2), ('Queen', 2, 4), ('Queen', 3, 6),
                     ('Queen', 4, 8), ('Queen', 5, 3), ('Queen', 6, 1),
                     ('Queen', 7, 7), ('Queen', 8, 5)],
                    [('Queen', 1, 2), ('Queen', 2, 5), ('Queen', 3, 7),
                     ('Queen', 4, 1), ('Queen', 5, 3), ('Queen', 6, 8),
                     ('Queen', 7, 6), ('Queen', 8, 4)],
                    [('Queen', 1, 2), ('Queen', 2, 5), ('Queen', 3, 7),
                     ('Queen', 4, 4), ('Queen', 5, 1), ('Queen', 6, 8),
                     ('Queen', 7, 6), ('Queen', 8, 3)],
                    [('Queen', 1, 2), ('Queen', 2, 6), ('Queen', 3, 1),
                     ('Queen', 4, 7), ('Queen', 5, 4), ('Queen', 6, 8),
                     ('Queen', 7, 3), ('Queen', 8, 5)],
                    [('Queen', 1, 2), ('Queen', 2, 6), ('Queen', 3, 8),
                     ('Queen', 4, 3), ('Queen', 5, 1), ('Queen', 6, 4),
                     ('Queen', 7, 7), ('Queen', 8, 5)],
                    [('Queen', 1, 2), ('Queen', 2, 7), ('Queen', 3, 3),
                     ('Queen', 4, 6), ('Queen', 5, 8), ('Queen', 6, 5),
                     ('Queen', 7, 1), ('Queen', 8, 4)],
                    [('Queen', 1, 2), ('Queen', 2, 7), ('Queen', 3, 5),
                     ('Queen', 4, 8), ('Queen', 5, 1), ('Queen', 6, 4),
                     ('Queen', 7, 6), ('Queen', 8, 3)],
                    [('Queen', 1, 2), ('Queen', 2, 8), ('Queen', 3, 6),
                     ('Queen', 4, 1), ('Queen', 5, 3), ('Queen', 6, 5),
                     ('Queen', 7, 7), ('Queen', 8, 4)],
                    [('Queen', 1, 3), ('Queen', 2, 1), ('Queen', 3, 7),
                     ('Queen', 4, 5), ('Queen', 5, 8), ('Queen', 6, 2),
                     ('Queen', 7, 4), ('Queen', 8, 6)],
                    [('Queen', 1, 3), ('Queen', 2, 5), ('Queen', 3, 2),
                     ('Queen', 4, 8), ('Queen', 5, 1), ('Queen', 6, 7),
                     ('Queen', 7, 4), ('Queen', 8, 6)],
                    [('Queen', 1, 3), ('Queen', 2, 5), ('Queen', 3, 2),
                     ('Queen', 4, 8), ('Queen', 5, 6), ('Queen', 6, 4),
                     ('Queen', 7, 7), ('Queen', 8, 1)],
                    [('Queen', 1, 3), ('Queen', 2, 5), ('Queen', 3, 7),
                     ('Queen', 4, 1), ('Queen', 5, 4), ('Queen', 6, 2),
                     ('Queen', 7, 8), ('Queen', 8, 6)],
                    [('Queen', 1, 3), ('Queen', 2, 5), ('Queen', 3, 8),
                     ('Queen', 4, 4), ('Queen', 5, 1), ('Queen', 6, 7),
                     ('Queen', 7, 2), ('Queen', 8, 6)],
                    [('Queen', 1, 3), ('Queen', 2, 6), ('Queen', 3, 2),
                     ('Queen', 4, 5), ('Queen', 5, 8), ('Queen', 6, 1),
                     ('Queen', 7, 7), ('Queen', 8, 4)],
                    [('Queen', 1, 3), ('Queen', 2, 6), ('Queen', 3, 2),
                     ('Queen', 4, 7), ('Queen', 5, 1), ('Queen', 6, 4),
                     ('Queen', 7, 8), ('Queen', 8, 5)],
                    [('Queen', 1, 3), ('Queen', 2, 6), ('Queen', 3, 2),
                     ('Queen', 4, 7), ('Queen', 5, 5), ('Queen', 6, 1),
                     ('Queen', 7, 8), ('Queen', 8, 4)],
                    [('Queen', 1, 3), ('Queen', 2, 6), ('Queen', 3, 4),
                     ('Queen', 4, 1), ('Queen', 5, 8), ('Queen', 6, 5),
                     ('Queen', 7, 7), ('Queen', 8, 2)],
                    [('Queen', 1, 3), ('Queen', 2, 6), ('Queen', 3, 4),
                     ('Queen', 4, 2), ('Queen', 5, 8), ('Queen', 6, 5),
                     ('Queen', 7, 7), ('Queen', 8, 1)],
                    [('Queen', 1, 3), ('Queen', 2, 6), ('Queen', 3, 8),
                     ('Queen', 4, 1), ('Queen', 5, 4), ('Queen', 6, 7),
                     ('Queen', 7, 5), ('Queen', 8, 2)],
                    [('Queen', 1, 3), ('Queen', 2, 6), ('Queen', 3, 8),
                     ('Queen', 4, 1), ('Queen', 5, 5), ('Queen', 6, 7),
                     ('Queen', 7, 2), ('Queen', 8, 4)],
                    [('Queen', 1, 3), ('Queen', 2, 6), ('Queen', 3, 8),
                     ('Queen', 4, 2), ('Queen', 5, 4), ('Queen', 6, 1),
                     ('Queen', 7, 7), ('Queen', 8, 5)],
                    [('Queen', 1, 3), ('Queen', 2, 7), ('Queen', 3, 2),
                     ('Queen', 4, 8), ('Queen', 5, 5), ('Queen', 6, 1),
                     ('Queen', 7, 4), ('Queen', 8, 6)],
                    [('Queen', 1, 3), ('Queen', 2, 7), ('Queen', 3, 2),
                     ('Queen', 4, 8), ('Queen', 5, 6), ('Queen', 6, 4),
                     ('Queen', 7, 1), ('Queen', 8, 5)],
                    [('Queen', 1, 3), ('Queen', 2, 8), ('Queen', 3, 4),
                     ('Queen', 4, 7), ('Queen', 5, 1), ('Queen', 6, 6),
                     ('Queen', 7, 2), ('Queen', 8, 5)],
                    [('Queen', 1, 4), ('Queen', 2, 1), ('Queen', 3, 5),
                     ('Queen', 4, 8), ('Queen', 5, 2), ('Queen', 6, 7),
                     ('Queen', 7, 3), ('Queen', 8, 6)],
                    [('Queen', 1, 4), ('Queen', 2, 1), ('Queen', 3, 5),
                     ('Queen', 4, 8), ('Queen', 5, 6), ('Queen', 6, 3),
                     ('Queen', 7, 7), ('Queen', 8, 2)],
                    [('Queen', 1, 4), ('Queen', 2, 2), ('Queen', 3, 5),
                     ('Queen', 4, 8), ('Queen', 5, 6), ('Queen', 6, 1),
                     ('Queen', 7, 3), ('Queen', 8, 7)],
                    [('Queen', 1, 4), ('Queen', 2, 2), ('Queen', 3, 7),
                     ('Queen', 4, 3), ('Queen', 5, 6), ('Queen', 6, 8),
                     ('Queen', 7, 1), ('Queen', 8, 5)],
                    [('Queen', 1, 4), ('Queen', 2, 2), ('Queen', 3, 7),
                     ('Queen', 4, 3), ('Queen', 5, 6), ('Queen', 6, 8),
                     ('Queen', 7, 5), ('Queen', 8, 1)],
                    [('Queen', 1, 4), ('Queen', 2, 2), ('Queen', 3, 7),
                     ('Queen', 4, 5), ('Queen', 5, 1), ('Queen', 6, 8),
                     ('Queen', 7, 6), ('Queen', 8, 3)],
                    [('Queen', 1, 4), ('Queen', 2, 2), ('Queen', 3, 8),
                     ('Queen', 4, 5), ('Queen', 5, 7), ('Queen', 6, 1),
                     ('Queen', 7, 3), ('Queen', 8, 6)],
                    [('Queen', 1, 4), ('Queen', 2, 2), ('Queen', 3, 8),
                     ('Queen', 4, 6), ('Queen', 5, 1), ('Queen', 6, 3),
                     ('Queen', 7, 5), ('Queen', 8, 7)],
                    [('Queen', 1, 4), ('Queen', 2, 6), ('Queen', 3, 1),
                     ('Queen', 4, 5), ('Queen', 5, 2), ('Queen', 6, 8),
                     ('Queen', 7, 3), ('Queen', 8, 7)],
                    [('Queen', 1, 4), ('Queen', 2, 6), ('Queen', 3, 8),
                     ('Queen', 4, 2), ('Queen', 5, 7), ('Queen', 6, 1),
                     ('Queen', 7, 3), ('Queen', 8, 5)],
                    [('Queen', 1, 4), ('Queen', 2, 6), ('Queen', 3, 8),
                     ('Queen', 4, 3), ('Queen', 5, 1), ('Queen', 6, 7),
                     ('Queen', 7, 5), ('Queen', 8, 2)],
                    [('Queen', 1, 4), ('Queen', 2, 7), ('Queen', 3, 1),
                     ('Queen', 4, 8), ('Queen', 5, 5), ('Queen', 6, 2),
                     ('Queen', 7, 6), ('Queen', 8, 3)],
                    [('Queen', 1, 4), ('Queen', 2, 7), ('Queen', 3, 3),
                     ('Queen', 4, 8), ('Queen', 5, 2), ('Queen', 6, 5),
                     ('Queen', 7, 1), ('Queen', 8, 6)],
                    [('Queen', 1, 4), ('Queen', 2, 7), ('Queen', 3, 5),
                     ('Queen', 4, 2), ('Queen', 5, 6), ('Queen', 6, 1),
                     ('Queen', 7, 3), ('Queen', 8, 8)],
                    [('Queen', 1, 4), ('Queen', 2, 7), ('Queen', 3, 5),
                     ('Queen', 4, 3), ('Queen', 5, 1), ('Queen', 6, 6),
                     ('Queen', 7, 8), ('Queen', 8, 2)],
                    [('Queen', 1, 4), ('Queen', 2, 8), ('Queen', 3, 1),
                     ('Queen', 4, 3), ('Queen', 5, 6), ('Queen', 6, 2),
                     ('Queen', 7, 7), ('Queen', 8, 5)],
                    [('Queen', 1, 4), ('Queen', 2, 8), ('Queen', 3, 1),
                     ('Queen', 4, 5), ('Queen', 5, 7), ('Queen', 6, 2),
                     ('Queen', 7, 6), ('Queen', 8, 3)],
                    [('Queen', 1, 4), ('Queen', 2, 8), ('Queen', 3, 5),
                     ('Queen', 4, 3), ('Queen', 5, 1), ('Queen', 6, 7),
                     ('Queen', 7, 2), ('Queen', 8, 6)],
                    [('Queen', 1, 5), ('Queen', 2, 1), ('Queen', 3, 4),
                     ('Queen', 4, 6), ('Queen', 5, 8), ('Queen', 6, 2),
                     ('Queen', 7, 7), ('Queen', 8, 3)],
                    [('Queen', 1, 5), ('Queen', 2, 1), ('Queen', 3, 8),
                     ('Queen', 4, 4), ('Queen', 5, 2), ('Queen', 6, 7),
                     ('Queen', 7, 3), ('Queen', 8, 6)],
                    [('Queen', 1, 5), ('Queen', 2, 1), ('Queen', 3, 8),
                     ('Queen', 4, 6), ('Queen', 5, 3), ('Queen', 6, 7),
                     ('Queen', 7, 2), ('Queen', 8, 4)],
                    [('Queen', 1, 5), ('Queen', 2, 2), ('Queen', 3, 4),
                     ('Queen', 4, 6), ('Queen', 5, 8), ('Queen', 6, 3),
                     ('Queen', 7, 1), ('Queen', 8, 7)],
                    [('Queen', 1, 5), ('Queen', 2, 2), ('Queen', 3, 4),
                     ('Queen', 4, 7), ('Queen', 5, 3), ('Queen', 6, 8),
                     ('Queen', 7, 6), ('Queen', 8, 1)],
                    [('Queen', 1, 5), ('Queen', 2, 2), ('Queen', 3, 6),
                     ('Queen', 4, 1), ('Queen', 5, 7), ('Queen', 6, 4),
                     ('Queen', 7, 8), ('Queen', 8, 3)],
                    [('Queen', 1, 5), ('Queen', 2, 2), ('Queen', 3, 8),
                     ('Queen', 4, 1), ('Queen', 5, 4), ('Queen', 6, 7),
                     ('Queen', 7, 3), ('Queen', 8, 6)],
                    [('Queen', 1, 5), ('Queen', 2, 3), ('Queen', 3, 1),
                     ('Queen', 4, 6), ('Queen', 5, 8), ('Queen', 6, 2),
                     ('Queen', 7, 4), ('Queen', 8, 7)],
                    [('Queen', 1, 5), ('Queen', 2, 3), ('Queen', 3, 1),
                     ('Queen', 4, 7), ('Queen', 5, 2), ('Queen', 6, 8),
                     ('Queen', 7, 6), ('Queen', 8, 4)],
                    [('Queen', 1, 5), ('Queen', 2, 3), ('Queen', 3, 8),
                     ('Queen', 4, 4), ('Queen', 5, 7), ('Queen', 6, 1),
                     ('Queen', 7, 6), ('Queen', 8, 2)],
                    [('Queen', 1, 5), ('Queen', 2, 7), ('Queen', 3, 1),
                     ('Queen', 4, 3), ('Queen', 5, 8), ('Queen', 6, 6),
                     ('Queen', 7, 4), ('Queen', 8, 2)],
                    [('Queen', 1, 5), ('Queen', 2, 7), ('Queen', 3, 1),
                     ('Queen', 4, 4), ('Queen', 5, 2), ('Queen', 6, 8),
                     ('Queen', 7, 6), ('Queen', 8, 3)],
                    [('Queen', 1, 5), ('Queen', 2, 7), ('Queen', 3, 2),
                     ('Queen', 4, 4), ('Queen', 5, 8), ('Queen', 6, 1),
                     ('Queen', 7, 3), ('Queen', 8, 6)],
                    [('Queen', 1, 5), ('Queen', 2, 7), ('Queen', 3, 2),
                     ('Queen', 4, 6), ('Queen', 5, 3), ('Queen', 6, 1),
                     ('Queen', 7, 4), ('Queen', 8, 8)],
                    [('Queen', 1, 5), ('Queen', 2, 7), ('Queen', 3, 2),
                     ('Queen', 4, 6), ('Queen', 5, 3), ('Queen', 6, 1),
                     ('Queen', 7, 8), ('Queen', 8, 4)],
                    [('Queen', 1, 5), ('Queen', 2, 7), ('Queen', 3, 4),
                     ('Queen', 4, 1), ('Queen', 5, 3), ('Queen', 6, 8),
                     ('Queen', 7, 6), ('Queen', 8, 2)],
                    [('Queen', 1, 5), ('Queen', 2, 8), ('Queen', 3, 4),
                     ('Queen', 4, 1), ('Queen', 5, 3), ('Queen', 6, 6),
                     ('Queen', 7, 2), ('Queen', 8, 7)],
                    [('Queen', 1, 5), ('Queen', 2, 8), ('Queen', 3, 4),
                     ('Queen', 4, 1), ('Queen', 5, 7), ('Queen', 6, 2),
                     ('Queen', 7, 6), ('Queen', 8, 3)],
                    [('Queen', 1, 6), ('Queen', 2, 1), ('Queen', 3, 5),
                     ('Queen', 4, 2), ('Queen', 5, 8), ('Queen', 6, 3),
                     ('Queen', 7, 7), ('Queen', 8, 4)],
                    [('Queen', 1, 6), ('Queen', 2, 2), ('Queen', 3, 7),
                     ('Queen', 4, 1), ('Queen', 5, 3), ('Queen', 6, 5),
                     ('Queen', 7, 8), ('Queen', 8, 4)],
                    [('Queen', 1, 6), ('Queen', 2, 2), ('Queen', 3, 7),
                     ('Queen', 4, 1), ('Queen', 5, 4), ('Queen', 6, 8),
                     ('Queen', 7, 5), ('Queen', 8, 3)],
                    [('Queen', 1, 6), ('Queen', 2, 3), ('Queen', 3, 1),
                     ('Queen', 4, 7), ('Queen', 5, 5), ('Queen', 6, 8),
                     ('Queen', 7, 2), ('Queen', 8, 4)],
                    [('Queen', 1, 6), ('Queen', 2, 3), ('Queen', 3, 1),
                     ('Queen', 4, 8), ('Queen', 5, 4), ('Queen', 6, 2),
                     ('Queen', 7, 7), ('Queen', 8, 5)],
                    [('Queen', 1, 6), ('Queen', 2, 3), ('Queen', 3, 1),
                     ('Queen', 4, 8), ('Queen', 5, 5), ('Queen', 6, 2),
                     ('Queen', 7, 4), ('Queen', 8, 7)],
                    [('Queen', 1, 6), ('Queen', 2, 3), ('Queen', 3, 5),
                     ('Queen', 4, 7), ('Queen', 5, 1), ('Queen', 6, 4),
                     ('Queen', 7, 2), ('Queen', 8, 8)],
                    [('Queen', 1, 6), ('Queen', 2, 3), ('Queen', 3, 5),
                     ('Queen', 4, 8), ('Queen', 5, 1), ('Queen', 6, 4),
                     ('Queen', 7, 2), ('Queen', 8, 7)],
                    [('Queen', 1, 6), ('Queen', 2, 3), ('Queen', 3, 7),
                     ('Queen', 4, 2), ('Queen', 5, 4), ('Queen', 6, 8),
                     ('Queen', 7, 1), ('Queen', 8, 5)],
                    [('Queen', 1, 6), ('Queen', 2, 3), ('Queen', 3, 7),
                     ('Queen', 4, 2), ('Queen', 5, 8), ('Queen', 6, 5),
                     ('Queen', 7, 1), ('Queen', 8, 4)],
                    [('Queen', 1, 6), ('Queen', 2, 3), ('Queen', 3, 7),
                     ('Queen', 4, 4), ('Queen', 5, 1), ('Queen', 6, 8),
                     ('Queen', 7, 2), ('Queen', 8, 5)],
                    [('Queen', 1, 6), ('Queen', 2, 4), ('Queen', 3, 1),
                     ('Queen', 4, 5), ('Queen', 5, 8), ('Queen', 6, 2),
                     ('Queen', 7, 7), ('Queen', 8, 3)],
                    [('Queen', 1, 6), ('Queen', 2, 4), ('Queen', 3, 2),
                     ('Queen', 4, 8), ('Queen', 5, 5), ('Queen', 6, 7),
                     ('Queen', 7, 1), ('Queen', 8, 3)],
                    [('Queen', 1, 6), ('Queen', 2, 4), ('Queen', 3, 7),
                     ('Queen', 4, 1), ('Queen', 5, 3), ('Queen', 6, 5),
                     ('Queen', 7, 2), ('Queen', 8, 8)],
                    [('Queen', 1, 6), ('Queen', 2, 4), ('Queen', 3, 7),
                     ('Queen', 4, 1), ('Queen', 5, 8), ('Queen', 6, 2),
                     ('Queen', 7, 5), ('Queen', 8, 3)],
                    [('Queen', 1, 6), ('Queen', 2, 8), ('Queen', 3, 2),
                     ('Queen', 4, 4), ('Queen', 5, 1), ('Queen', 6, 7),
                     ('Queen', 7, 5), ('Queen', 8, 3)],
                    [('Queen', 1, 7), ('Queen', 2, 1), ('Queen', 3, 3),
                     ('Queen', 4, 8), ('Queen', 5, 6), ('Queen', 6, 4),
                     ('Queen', 7, 2), ('Queen', 8, 5)],
                    [('Queen', 1, 7), ('Queen', 2, 2), ('Queen', 3, 4),
                     ('Queen', 4, 1), ('Queen', 5, 8), ('Queen', 6, 5),
                     ('Queen', 7, 3), ('Queen', 8, 6)],
                    [('Queen', 1, 7), ('Queen', 2, 2), ('Queen', 3, 6),
                     ('Queen', 4, 3), ('Queen', 5, 1), ('Queen', 6, 4),
                     ('Queen', 7, 8), ('Queen', 8, 5)],
                    [('Queen', 1, 7), ('Queen', 2, 3), ('Queen', 3, 1),
                     ('Queen', 4, 6), ('Queen', 5, 8), ('Queen', 6, 5),
                     ('Queen', 7, 2), ('Queen', 8, 4)],
                    [('Queen', 1, 7), ('Queen', 2, 3), ('Queen', 3, 8),
                     ('Queen', 4, 2), ('Queen', 5, 5), ('Queen', 6, 1),
                     ('Queen', 7, 6), ('Queen', 8, 4)],
                    [('Queen', 1, 7), ('Queen', 2, 4), ('Queen', 3, 2),
                     ('Queen', 4, 5), ('Queen', 5, 8), ('Queen', 6, 1),
                     ('Queen', 7, 3), ('Queen', 8, 6)],
                    [('Queen', 1, 7), ('Queen', 2, 4), ('Queen', 3, 2),
                     ('Queen', 4, 8), ('Queen', 5, 6), ('Queen', 6, 1),
                     ('Queen', 7, 3), ('Queen', 8, 5)],
                    [('Queen', 1, 7), ('Queen', 2, 5), ('Queen', 3, 3),
                     ('Queen', 4, 1), ('Queen', 5, 6), ('Queen', 6, 8),
                     ('Queen', 7, 2), ('Queen', 8, 4)],
                    [('Queen', 1, 8), ('Queen', 2, 2), ('Queen', 3, 4),
                     ('Queen', 4, 1), ('Queen', 5, 7), ('Queen', 6, 5),
                     ('Queen', 7, 3), ('Queen', 8, 6)],
                    [('Queen', 1, 8), ('Queen', 2, 2), ('Queen', 3, 5),
                     ('Queen', 4, 3), ('Queen', 5, 1), ('Queen', 6, 7),
                     ('Queen', 7, 4), ('Queen', 8, 6)],
                    [('Queen', 1, 8), ('Queen', 2, 3), ('Queen', 3, 1),
                     ('Queen', 4, 6), ('Queen', 5, 2), ('Queen', 6, 5),
                     ('Queen', 7, 7), ('Queen', 8, 4)],
                    [('Queen', 1, 8), ('Queen', 2, 4), ('Queen', 3, 1),
                     ('Queen', 4, 3),
                     ('Queen', 5, 6), ('Queen', 6, 2), ('Queen', 7, 7),
                     ('Queen', 8, 5)]]
        result = engine.execute()
        self.assertEqual(expected, result)

    def test_3_bishops(self):
        expected = [[('Bishop', 1, 1), ('Bishop', 1, 2), ('Bishop', 1, 3)],
                    [('Bishop', 1, 1), ('Bishop', 1, 2), ('Bishop', 3, 1)],
                    [('Bishop', 1, 1), ('Bishop', 1, 2), ('Bishop', 3, 2)],
                    [('Bishop', 1, 1), ('Bishop', 1, 3), ('Bishop', 2, 1)],
                    [('Bishop', 1, 1), ('Bishop', 1, 3), ('Bishop', 2, 3)],
                    [('Bishop', 1, 1), ('Bishop', 1, 3), ('Bishop', 3, 2)],
                    [('Bishop', 1, 1), ('Bishop', 2, 1), ('Bishop', 2, 3)],
                    [('Bishop', 1, 1), ('Bishop', 2, 1), ('Bishop', 3, 1)],
                    [('Bishop', 1, 1), ('Bishop', 2, 3), ('Bishop', 3, 1)],
                    [('Bishop', 1, 1), ('Bishop', 3, 1), ('Bishop', 3, 2)],
                    [('Bishop', 1, 2), ('Bishop', 1, 3), ('Bishop', 3, 2)],
                    [('Bishop', 1, 2), ('Bishop', 1, 3), ('Bishop', 3, 3)],
                    [('Bishop', 1, 2), ('Bishop', 2, 2), ('Bishop', 3, 2)],
                    [('Bishop', 1, 2), ('Bishop', 3, 1), ('Bishop', 3, 2)],
                    [('Bishop', 1, 2), ('Bishop', 3, 1), ('Bishop', 3, 3)],
                    [('Bishop', 1, 2), ('Bishop', 3, 2), ('Bishop', 3, 3)],
                    [('Bishop', 1, 3), ('Bishop', 2, 1), ('Bishop', 2, 3)],
                    [('Bishop', 1, 3), ('Bishop', 2, 1), ('Bishop', 3, 3)],
                    [('Bishop', 1, 3), ('Bishop', 2, 3), ('Bishop', 3, 3)],
                    [('Bishop', 1, 3), ('Bishop', 3, 2), ('Bishop', 3, 3)],
                    [('Bishop', 2, 1), ('Bishop', 2, 2), ('Bishop', 2, 3)],
                    [('Bishop', 2, 1), ('Bishop', 2, 3), ('Bishop', 3, 1)],
                    [('Bishop', 2, 1), ('Bishop', 2, 3), ('Bishop', 3, 3)],
                    [('Bishop', 2, 1), ('Bishop', 3, 1), ('Bishop', 3, 3)],
                    [('Bishop', 2, 3), ('Bishop', 3, 1), ('Bishop', 3, 3)],
                    [('Bishop', 3, 1), ('Bishop', 3, 2), ('Bishop', 3, 3)]
                    ]

        pieces = ['Bishop', 'Bishop', 'Bishop']
        engine = ChessChallengeEngine(pieces, len(pieces), len(pieces))
        result = engine.execute()
        self.assertEqual(expected, result)

    def test_2_knights_1_bishop(self):
        expected = [[('Bishop', 1, 1), ('Knight', 1, 2), ('Knight', 1, 3)],
                    [('Bishop', 1, 1), ('Knight', 1, 2), ('Knight', 2, 1)],
                    [('Bishop', 1, 1), ('Knight', 1, 3), ('Knight', 3, 1)],
                    [('Bishop', 1, 1), ('Knight', 2, 1), ('Knight', 3, 1)],
                    [('Bishop', 1, 2), ('Knight', 1, 1), ('Knight', 1, 3)],
                    [('Bishop', 1, 2), ('Knight', 1, 1), ('Knight', 2, 2)],
                    [('Bishop', 1, 2), ('Knight', 1, 3), ('Knight', 2, 2)],
                    [('Bishop', 1, 2), ('Knight', 2, 2), ('Knight', 3, 2)],
                    [('Bishop', 1, 3), ('Knight', 1, 1), ('Knight', 1, 2)],
                    [('Bishop', 1, 3), ('Knight', 1, 1), ('Knight', 3, 3)],
                    [('Bishop', 1, 3), ('Knight', 1, 2), ('Knight', 2, 3)],
                    [('Bishop', 1, 3), ('Knight', 2, 3), ('Knight', 3, 3)],
                    [('Bishop', 2, 1), ('Knight', 1, 1), ('Knight', 2, 2)],
                    [('Bishop', 2, 1), ('Knight', 1, 1), ('Knight', 3, 1)],
                    [('Bishop', 2, 1), ('Knight', 2, 2), ('Knight', 2, 3)],
                    [('Bishop', 2, 1), ('Knight', 2, 2), ('Knight', 3, 1)],
                    [('Bishop', 2, 2), ('Knight', 1, 2), ('Knight', 2, 1)],
                    [('Bishop', 2, 2), ('Knight', 1, 2), ('Knight', 2, 3)],
                    [('Bishop', 2, 2), ('Knight', 1, 2), ('Knight', 3, 2)],
                    [('Bishop', 2, 2), ('Knight', 2, 1), ('Knight', 2, 3)],
                    [('Bishop', 2, 2), ('Knight', 2, 1), ('Knight', 3, 2)],
                    [('Bishop', 2, 2), ('Knight', 2, 3), ('Knight', 3, 2)],
                    [('Bishop', 2, 3), ('Knight', 1, 3), ('Knight', 2, 2)],
                    [('Bishop', 2, 3), ('Knight', 1, 3), ('Knight', 3, 3)],
                    [('Bishop', 2, 3), ('Knight', 2, 1), ('Knight', 2, 2)],
                    [('Bishop', 2, 3), ('Knight', 2, 2), ('Knight', 3, 3)],
                    [('Bishop', 3, 1), ('Knight', 1, 1), ('Knight', 2, 1)],
                    [('Bishop', 3, 1), ('Knight', 1, 1), ('Knight', 3, 3)],
                    [('Bishop', 3, 1), ('Knight', 2, 1), ('Knight', 3, 2)],
                    [('Bishop', 3, 1), ('Knight', 3, 2), ('Knight', 3, 3)],
                    [('Bishop', 3, 2), ('Knight', 1, 2), ('Knight', 2, 2)],
                    [('Bishop', 3, 2), ('Knight', 2, 2), ('Knight', 3, 1)],
                    [('Bishop', 3, 2), ('Knight', 2, 2), ('Knight', 3, 3)],
                    [('Bishop', 3, 2), ('Knight', 3, 1), ('Knight', 3, 3)],
                    [('Bishop', 3, 3), ('Knight', 1, 3), ('Knight', 2, 3)],
                    [('Bishop', 3, 3), ('Knight', 1, 3), ('Knight', 3, 1)],
                    [('Bishop', 3, 3), ('Knight', 2, 3), ('Knight', 3, 2)],
                    [('Bishop', 3, 3), ('Knight', 3, 1), ('Knight', 3, 2)]
                    ]
        pieces = ['Bishop', 'Knight', 'Knight']
        engine = ChessChallengeEngine(pieces, len(pieces), len(pieces))
        result = engine.execute()
        self.assertEqual(expected, result)

    def test_impossible_configuration(self):
        """8 queens in a 6 * 6 board"""

        expected = [[]]
        pieces = ['Queen'] * 8
        engine = ChessChallengeEngine(pieces, 6, 6)
        result = engine.execute()
        self.assertEqual(expected, result)

    def test_1_king_3_by_3_board(self):
        expected = [
            [('King', 1, 1)],
            [('King', 1, 2)],
            [('King', 1, 3)],
            [('King', 2, 1)],
            [('King', 2, 2)],
            [('King', 2, 3)],
            [('King', 3, 1)],
            [('King', 3, 2)],
            [('King', 3, 3)]
        ]
        pieces = ['King']
        engine = ChessChallengeEngine(pieces, 3, 3)
        result = engine.execute()
        self.assertEqual(expected, result)

    def test_1_queen_3_by_3_board(self):
        expected = [
            [('Queen', 1, 1)],
            [('Queen', 1, 2)],
            [('Queen', 1, 3)],
            [('Queen', 2, 1)],
            [('Queen', 2, 2)],
            [('Queen', 2, 3)],
            [('Queen', 3, 1)],
            [('Queen', 3, 2)],
            [('Queen', 3, 3)]
        ]
        pieces = ['Queen']
        engine = ChessChallengeEngine(pieces, 3, 3)
        result = engine.execute()
        self.assertEqual(expected, result)

    def test_2_kings_3_by_3_board(self):
        expected = [
            [('King', 1, 1), ('King', 1, 3)],
            [('King', 1, 1), ('King', 2, 3)],
            [('King', 1, 1), ('King', 3, 1)],
            [('King', 1, 1), ('King', 3, 2)],
            [('King', 1, 1), ('King', 3, 3)],
            [('King', 1, 2), ('King', 3, 1)],
            [('King', 1, 2), ('King', 3, 2)],
            [('King', 1, 2), ('King', 3, 3)],
            [('King', 1, 3), ('King', 2, 1)],
            [('King', 1, 3), ('King', 3, 1)],
            [('King', 1, 3), ('King', 3, 2)],
            [('King', 1, 3), ('King', 3, 3)],
            [('King', 2, 1), ('King', 2, 3)],
            [('King', 2, 1), ('King', 3, 3)],
            [('King', 2, 3), ('King', 3, 1)],
            [('King', 3, 1), ('King', 3, 3)]
        ]
        pieces = ['King', 'King']
        engine = ChessChallengeEngine(pieces, 3, 3)
        result = engine.execute()
        self.assertEqual(expected, result)

    def test_1_knight_3_by_3_board(self):
        expected = [
            [('Knight', 1, 1)],
            [('Knight', 1, 2)],
            [('Knight', 1, 3)],
            [('Knight', 2, 1)],
            [('Knight', 2, 2)],
            [('Knight', 2, 3)],
            [('Knight', 3, 1)],
            [('Knight', 3, 2)],
            [('Knight', 3, 3)]
        ]
        pieces = ['Knight']
        engine = ChessChallengeEngine(pieces, 3, 3)
        result = engine.execute()
        self.assertEqual(expected, result)

    def test_2_knights_3_by_3_board(self):
        expected = [
            [('Knight', 1, 1), ('Knight', 1, 2)],
            [('Knight', 1, 1), ('Knight', 1, 3)],
            [('Knight', 1, 1), ('Knight', 2, 1)],
            [('Knight', 1, 1), ('Knight', 2, 2)],
            [('Knight', 1, 1), ('Knight', 3, 1)],
            [('Knight', 1, 1), ('Knight', 3, 3)],
            [('Knight', 1, 2), ('Knight', 1, 3)],
            [('Knight', 1, 2), ('Knight', 2, 1)],
            [('Knight', 1, 2), ('Knight', 2, 2)],
            [('Knight', 1, 2), ('Knight', 2, 3)],
            [('Knight', 1, 2), ('Knight', 3, 2)],
            [('Knight', 1, 3), ('Knight', 2, 2)],
            [('Knight', 1, 3), ('Knight', 2, 3)],
            [('Knight', 1, 3), ('Knight', 3, 1)],
            [('Knight', 1, 3), ('Knight', 3, 3)],
            [('Knight', 2, 1), ('Knight', 2, 2)],
            [('Knight', 2, 1), ('Knight', 2, 3)],
            [('Knight', 2, 1), ('Knight', 3, 1)],
            [('Knight', 2, 1), ('Knight', 3, 2)],
            [('Knight', 2, 2), ('Knight', 2, 3)],
            [('Knight', 2, 2), ('Knight', 3, 1)],
            [('Knight', 2, 2), ('Knight', 3, 2)],
            [('Knight', 2, 2), ('Knight', 3, 3)],
            [('Knight', 2, 3), ('Knight', 3, 2)],
            [('Knight', 2, 3), ('Knight', 3, 3)],
            [('Knight', 3, 1), ('Knight', 3, 2)],
            [('Knight', 3, 1), ('Knight', 3, 3)],
            [('Knight', 3, 2), ('Knight', 3, 3)]
        ]
        pieces = ['Knight', 'Knight']
        engine = ChessChallengeEngine(pieces, 3, 3)
        result = engine.execute()
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
