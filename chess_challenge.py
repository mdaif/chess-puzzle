"""Solve a generalized version of the 8-queens puzzle.

The core functionality of the module is the ChessChallengeEngine class. The
input is provided via argparse parser.
"""

from pieces import King, Queen, Rook, Bishop, Knight
import argparse
import datetime


class ChessChallengeEngine(object):
    """Manage chess challenge solution.

    ChessChallengeEngine is the core component of the module,
    it is initialized by the chess pieces to be put on the chess board,
    the board width, and the board height, running execute public method
    results in calculating the unique configurations of the pieces
    placement on the board
    """

    def __init__(self, pieces, board_width, board_height):
        """Initialize ChessChallengeEngine with pieces, board size.

        Arguments:
        pieces -- a list of chess pieces
        board_width -- width of the board
        board_height -- height of the board
        """
        self.pieces = sorted(pieces, key=str)
        # sorting lexicographically to make sure all possible
        # permutations of the same problem maps to the same input

        self.board_width = board_width
        self.board_height = board_height
        self.all_pieces = pieces  # won't be decremented at each step

    def execute(self):
        """Return all unique configurations."""
        solutions = [[]]

        # we check if all the pieces are exhausted when all the board rows
        # are checked, if not , we start over.
        while self.pieces:
            for _ in range(self.board_height):  # for each row of the board
                solutions = \
                    self._add_one_piece(self.board_height,
                                        solutions)
                # after first iteration, we can find the inserted pieces are
                #  less than the expected to be inserted.
                if len(solutions) < len(self.pieces):
                    return [[]]

                if not self.pieces:
                    return solutions

        return []

    def _add_one_piece(self, columns, prev_solutions):
        """Add next chess piece to a safe place on the board.

        Arguments:
        pieces -- list of remaining chess pieces to be placed.
        columns -- the upper bound of columns to be scanned for a threat.
        prev_solutions -- a list of all the previously calculated safe
        positions.
        """
        print "#"
        current_piece = self.pieces[0]
        rows = self.board_height + 1
        solutions = []
        seen = set()

        for solution in prev_solutions:
            for row in range(1, rows):
                for column in range(1, columns + 1):
                    if not self._under_attack(current_piece, row, column,
                                              solution):

                        result = sorted(
                            solution + [(current_piece, row, column)],
                            key=str)
                        hashable_result = str(result)
                        if hashable_result not in seen:
                            seen.add(hashable_result)
                            solutions.append(result)
        self.pieces = self.pieces[1:]
        return solutions

    @staticmethod
    def _under_attack(current_piece, row, column, candidate_solution):
        """Check if the position is safe.

        Internal method, each time _add_one_piece finds a potential
        location (indicated by row, column) it calls this method to make
        sure it's safe to place the current piece. Different types of
        attacks are determined based on the current piece's type and each
        other piece located in each sub-solution found so far

        Arguments:
        current_piece -- the type of the current piece (Knight, Queen, .. etc)
        row -- the next row to be scanned for threats.
        column -- the next column to be scanned for threats.
        candidate_solution -- one of the safe solutions calculated so far.
        """
        for chess_piece in candidate_solution:

            attacking_piece, attacking_row, attacking_column = chess_piece
            if current_piece.is_threatened(attacking_piece, attacking_row,
                                           attacking_column, row, column):
                return True

        return False


def main():
    """"run if the file is executed as a standalone app."""
    parser = argparse.ArgumentParser(description='Find all unique '
                                                 'configurations of a set of '
                                                 'normal chess pieces on a '
                                                 'chess board')
    parser.add_argument('-n', action="store", type=int, default=3,
                        help="board width", required=True)
    parser.add_argument('-m', action="store", type=int, default=3,
                        help="board height", required=True)
    parser.add_argument('--kings', action="store", type=int, default=0,
                        help="Number of kings")
    parser.add_argument('--queens', action="store", type=int, default=0,
                        help="Number of queens")
    parser.add_argument('--bishops', action="store", type=int, default=0,
                        help="Number of bishops")
    parser.add_argument('--knights', action="store", type=int, default=0,
                        help="Number of knights")
    parser.add_argument('--rooks', action="store", type=int, default=0,
                        help="number of rooks")

    input_args = parser.parse_args()
    board_width = input_args.__dict__.pop('n')
    board_height = input_args.__dict__.pop('m')
    args_to_pieces = {'kings': King, 'queens': Queen, 'bishops': Bishop,
                      'knights': Knight, 'rooks': Rook}
    input_pieces = []
    for piece_name, piece_count in input_args.__dict__.items():
        input_pieces.extend([args_to_pieces[piece_name]
                             for _ in range(piece_count)])
    start_time = datetime.datetime.now()
    challenge = ChessChallengeEngine(input_pieces, board_width, board_height)
    end_results = challenge.execute()
    for end_result in end_results:
        print end_result
    end_time = datetime.datetime.now()
    print "Program finished in approximately {} " \
          "seconds, number of unique solutions " \
          "found: {}".format((end_time - start_time).total_seconds(),
                             int(len(end_results)))

if __name__ == "__main__":
    main()
