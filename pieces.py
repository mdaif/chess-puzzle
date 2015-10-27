"""Use OOP to define each chess piece's behavior in a class."""
from helpers import diagonals_danger, king_danger, knight_danger, \
    row_or_column_danger


class PieceType(object):
    """Enumerate all possible types of pieces."""

    Queen = 1
    King = 2
    Bishop = 3
    Knight = 4
    Rook = 5


class RepresentationMetaClass(type):
    """Enable custom representation for class objects."""

    def __str__(cls):
        """Represent the class object."""
        return cls.representation

    def __repr__(cls):
        """Represent the class object."""
        return cls.representation


class ChessPiece(object):
    """Provide a base class for Chess pieces."""

    __metaclass__ = RepresentationMetaClass

    piece_type = None
    representation = "ChessPiece"

    @classmethod
    def is_threatened(cls, attacking_piece, attacking_row, attacking_column,
                      row,
                      column):
        """Check if current piece is threatened by another piece.

        An abstract method, implemented at each class that extends
        ChessPiece, Each chess piece defines it's own behavior against the
        other pieces. Returns True if the piece is threatened.

        Arguments:
        attacking_piece -- A class that extends ChessPiece
        attacking_row -- the row at which the attacking piece is located.
        attacking_column -- the column at which the attacking piece is
        located.
        row -- the row at which the current piece is located.
        column -- the column at which the current piece is located.
        """
        pass

    @classmethod
    def _check_common_threats(cls, attacking_piece, attacking_row,
                              attacking_column, row,
                              column):
        """Check for threats from already allocated pieces.

        Arguments:
        attacking_piece -- A class that extends ChessPiece
        attacking_row -- the row at which the attacking piece is located.
        attacking_column -- the column at which the attacking piece is
        located.
        row -- the row at which the current piece is located.
        column -- the column at which the current piece is located.
        """
        if attacking_piece.piece_type == PieceType.Rook and \
                row_or_column_danger(attacking_row, attacking_column, row,
                                     column):
            return True

        elif attacking_piece.piece_type == PieceType.Queen and \
                (diagonals_danger(attacking_row, attacking_column, row,
                                  column) or row_or_column_danger(
                    attacking_row, attacking_column, row, column)):
            return True

        elif attacking_piece.piece_type == PieceType.Bishop and \
                diagonals_danger(attacking_row, attacking_column, row,
                                 column):
            return True

        elif attacking_piece.piece_type == PieceType.Knight and knight_danger(
                attacking_row, attacking_column, row, column):
            return True

        elif attacking_piece.piece_type == PieceType.King and king_danger(
                attacking_row, attacking_column, row, column):
            return True

        return False


class Queen(ChessPiece):
    """Extend ChessPiece to implement a Queen.

    class variables:
    piece_type -- a numeric value that represents a queen
    representation -- a string to be displayed when printing to console.

    Methods:
    is_threatened -- class method
    """

    piece_type = PieceType.Queen
    representation = 'Queen'
    comparison_factor = 1  # Queen eliminates a row, a column,
    # both diagonals from next piece's comparisons, so queens should come
    # first.

    @classmethod
    def is_threatened(cls, attacking_piece, attacking_row, attacking_column,
                      row,
                      column):
        """Override ChessPiece is_threatened abstract class method."""
        if diagonals_danger(attacking_row, attacking_column, row, column) or \
                row_or_column_danger(attacking_row, attacking_column, row,
                                     column):
            return True

        # Queen can only be threatened by a knight, as an optimization,
        # let it check for knight attacks only.
        if attacking_piece.piece_type == PieceType.Knight and knight_danger(
                attacking_row, attacking_column, row, column):
            return True

        return False


class King(ChessPiece):
    """Extend ChessPiece to implement a King.

    class variables:
    piece_type -- a numeric value that represents a king
    representation -- a string to be displayed when printing to console.

    Methods:
    is_threatened -- class method
    """

    piece_type = PieceType.King
    representation = 'King'
    comparison_factor = 4  # Kings eliminate the least amount of future
    # comparisons so it comes last.

    @classmethod
    def is_threatened(cls, attacking_piece, attacking_row, attacking_column,
                      row, column):
        """Override ChessPiece is_threatened abstract class method."""
        if king_danger(attacking_row, attacking_column, row, column):
            return True

        if cls._check_common_threats(attacking_piece, attacking_row,
                                     attacking_column, row, column):
            return True
        return False


class Rook(ChessPiece):
    """Extend ChessPiece to implement a Rook.

    class variables:
    piece_type -- a numeric value that represents a rook
    representation -- a string to be displayed when printing to console.

    Methods:
    is_threatened -- class method
    """

    piece_type = PieceType.Rook
    representation = 'Rook'
    comparison_factor = 2  # Rooks eliminate a row and a column making
    # them
    #  the strongest after the queen.

    @classmethod
    def is_threatened(cls, attacking_piece, attacking_row, attacking_column,
                      row,
                      column):
        """Override ChessPiece is_threatened abstract class method."""
        if row_or_column_danger(attacking_row, attacking_column, row, column):
            return True

        if cls._check_common_threats(attacking_piece, attacking_row,
                                     attacking_column, row, column):
            return True
        return False


class Knight(ChessPiece):
    """Extend ChessPiece to implement a Knight.

    class variables:
    piece_type -- a numeric value that represents a knight
    representation -- a string to be displayed when printing to console.

    Methods:
    is_threatened -- class method
    """

    piece_type = PieceType.Knight
    representation = 'Knight'
    comparison_factor = 3  # Knights eliminate 7 positions, making them the
    #  in position after bishops and rooks.

    @classmethod
    def is_threatened(cls, attacking_piece, attacking_row, attacking_column,
                      row,
                      column):
        """Override ChessPiece is_threatened abstract class method."""
        if knight_danger(attacking_row, attacking_column, row, column):
            return True

        if cls._check_common_threats(attacking_piece, attacking_row,
                                     attacking_column, row, column):
            return True
        return False


class Bishop(ChessPiece):
    """Extend ChessPiece to implement a Bishop.

    class variables:
    piece_type -- a numeric value that represents a bishop
    representation -- a string to be displayed when printing to console.

    Methods:
    is_threatened -- class method
    """

    piece_type = PieceType.Bishop
    representation = "Bishop"
    comparison_factor = 2  # Bishops eliminate two diagonals, making them
    # as powerful as rooks.

    @classmethod
    def is_threatened(cls, attacking_piece, attacking_row, attacking_column,
                      row,
                      column):
        """Override ChessPiece is_threatened abstract class method."""
        if diagonals_danger(attacking_row, attacking_column, row, column):
            return True

        if cls._check_common_threats(attacking_piece, attacking_row,
                                     attacking_column, row, column):
            return True
        return False
