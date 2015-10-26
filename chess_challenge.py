"""Solve a generalized version of the 8-queens puzzle.

The core functionality of the module is the ChessChallengeEngine class. The
input is provided via argparse parser.
"""

import datetime
from pieces import King, Queen, Rook, Bishop, Knight


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
        for _ in range(len(self.pieces)):
            for _ in range(self.board_height):  # for each row of the board
                solutions, self.pieces = \
                    self._add_one_piece(self.pieces, self.board_height,
                                        solutions)
                # after first iteration, we can find the inserted pieces are
                #  less than the expected to be inserted.
                if len(solutions) < len(self.pieces):
                    return [[]]

                if not self.pieces:
                    return solutions

        #return solutions

    def _add_one_piece(self, pieces, columns, prev_solutions):
        """Add next chess piece to a safe place on the board.

        Arguments:
        pieces -- list of remaining chess pieces to be placed.
        columns -- the upper bound of columns to be scanned for a threat.
        prev_solutions -- a list of all the previously calculated safe
        positions.
        """
        current_piece = pieces[0]
        solutions = []
        seen = set()

        for solution in prev_solutions:

            # the number of rows to be examined differs based on the type of
            #  piece being played ... we can always check for all rows but
            # it becomes very expensive when you have all queens and the
            # number of pieces > 7 (that's an empirical observation). That
            # is a corner case and we should then only examine the row next
            # to the row we already examined.
            rows = len(solution) + 2 if set(self.all_pieces) == {Queen} \
                                        and len(
                self.all_pieces) > 7 else self.board_height + 1
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
        return solutions, self.pieces

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
    start_time = datetime.datetime.now()
    input_pieces = [King, Bishop]
    challenge = ChessChallengeEngine(input_pieces, 3, 3)
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
