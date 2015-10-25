"""Chess Challenge is a module that aims to solve a (REALLY)  generalized
version of the famous 8-queens puzzle"""

import datetime

from helpers import king_danger, knight_danger, diagonals_danger, \
    row_or_column_danger


class ChessChallengeEngine(object):
    """ChessChallengeEngine is the core component of the module,
    it is initialized by the chess pieces to be put on the chess board,
    the board width, and the board height, running execute method results in
    calculating the unique configurations of the pieces placement on the
    board"""

    def __init__(self, pieces, board_width, board_height):
        self.pieces = sorted(
            pieces)  # sorting lexicographically to make sure all possible
        # permutations of the same problem maps to the same input

        self.board_width = board_width
        self.board_height = board_height
        self.all_pieces = pieces  # won't be decremented at each step

    def execute(self):
        """The main engine's method, when called it runs the chess puzzle
        algorithm, returning all unique configurations of the chess pieces
        on the chess board"""
        solutions = [[]]
        for _ in range(self.board_height):  # for each row of the board
            if self.pieces:
                solutions, self.pieces = self._add_one_piece(self.pieces,
                                                             self.board_height,
                                                             solutions)
                # after first iteration, we can find the inserted pieces are
                #  less than the expected to be inserted.
                if len(solutions) < len(self.pieces):
                    return [[]]

        return solutions

    def _add_one_piece(self, pieces, columns, prev_solutions):
        """Internal method, used by execute method to scan the board for
        possible attacks of already placed pieces, it's run each time a new
        piece is added."""
        current_piece = pieces[0]
        solutions = []
        seen = []

        for solution in prev_solutions:

            # the number of rows to be examined differs based on the type of
            #  piece being played ... we can always check for all rows but
            # it becomes very expensive when you have all queens and the
            # number of pieces > 7 (that's an empirical observation). That
            # is a corner case and we should then only examine the row next
            # to the row we already examined.
            rows = len(solution) + 2 if set(self.all_pieces) == set([
                'Queen']) and len(
                self.all_pieces) > 7 else self.board_height + 1
            for row in range(1, rows):
                for column in range(1, columns + 1):
                    if not self._under_attack(current_piece, row, column,
                                              solution):

                        result = sorted(
                            solution + [(current_piece, row, column)])
                        if result not in seen:
                            seen.append(result)
                            solutions.append(result)
        self.pieces = self.pieces[1:]
        return solutions, self.pieces

    @staticmethod
    def _under_attack(current_piece, row, column, candidate_solution):
        """Internal method, each time _add_one_piece finds a potential
        location (indicated by row, column) it calls this method to make
        sure it's safe to place the current piece. Different types of
        attacks are determined based on the current piece's type and each
        other piece located in each sub-solution found so far"""
        for chess_piece in candidate_solution:

            attacking_piece, attacking_row, attacking_column = chess_piece
            if current_piece == 'Queen' or attacking_piece == 'Queen':

                if diagonals_danger(row, column, attacking_row,
                                    attacking_column) or \
                        row_or_column_danger(row, column, attacking_row,
                                             attacking_column):
                    return True

                if attacking_piece == 'Knight':
                    if knight_danger(attacking_row, attacking_column, row,
                                     column):
                        return True

            elif current_piece == 'King':
                if king_danger(attacking_row, attacking_column, row, column):
                    return True
                if attacking_piece == 'Rook' and \
                        row_or_column_danger(row, column, attacking_row,
                                             attacking_column):
                    return True

                elif attacking_piece == 'Queen' and (diagonals_danger(row,
                                                                     column, attacking_row,
                                    attacking_column) or row_or_column_danger(row, column, attacking_row,
                                             attacking_column)):
                    return True

                elif attacking_piece == 'Bishop' and diagonals_danger(row,
                                                                     column, attacking_row,
                                    attacking_column):
                    return True

                elif attacking_piece == 'Knight' and knight_danger(
                        attacking_row, attacking_column, row, column):
                    return True

            elif current_piece == 'Rook':
                if row_or_column_danger(row, column, attacking_row,
                                        attacking_column):
                    return True

                if attacking_piece == 'King' and king_danger(attacking_row,
                                                             attacking_column,
                                                             row, column):
                    return True

                elif attacking_piece == 'Knight' and knight_danger( \
                        attacking_row, attacking_column, row,
                        column):
                    return True

                elif attacking_piece == 'Queen' and (diagonals_danger(row,
                                                                     column, attacking_row,
                                    attacking_column) or row_or_column_danger(row, column, attacking_row,
                                             attacking_column)):
                    return True

                elif attacking_piece == 'Bishop' and diagonals_danger(row,
                                                                     column, attacking_row,
                                    attacking_column):
                    return True

            elif current_piece == 'Knight':
                if knight_danger(attacking_row, attacking_column, row, column):
                    return True

                if attacking_piece == 'Bishop' and \
                        diagonals_danger(row, column, attacking_row,
                                         attacking_column):
                    return True

                elif attacking_piece == 'King' and king_danger(attacking_row,
                                                             attacking_column,
                                                             row, column):
                    return True

                elif attacking_piece == 'Rook' and \
                        row_or_column_danger(row, column, attacking_row,
                                             attacking_column):
                    return True

                elif attacking_piece == 'Queen' and (diagonals_danger(row,
                                                                     column, attacking_row,
                                    attacking_column) or row_or_column_danger(row, column, attacking_row,
                                             attacking_column)):
                    return True

            elif current_piece == 'Bishop' or attacking_piece == 'Bishop':
                if diagonals_danger(row, column, attacking_row,
                                    attacking_column):
                    return True

                if attacking_piece == 'Knight':
                    if knight_danger(attacking_row, attacking_column, row,
                                     column):
                        return True
                    
                elif attacking_piece == 'King' and king_danger(attacking_row,
                                                             attacking_column,
                                                             row, column):
                    return True

                elif attacking_piece == 'Rook' and \
                        row_or_column_danger(row, column, attacking_row,
                                             attacking_column):
                    return True

                elif attacking_piece == 'Queen' and (diagonals_danger(row,
                                                                     column, attacking_row,
                                    attacking_column) or row_or_column_danger(row, column, attacking_row,
                                             attacking_column)):
                    return True
        return False


def main():
    """"main method, it's run if the module is executed"""

    start_time = datetime.datetime.now()
    #    pieces = ['Rook', 'Rook', 'Knight', 'Knight', 'Knight', 'Knight']
    # pieces = ['Knight', 'Knight', 'Bishop']
    input_pieces = ['Queen'] * 8

    challenge = ChessChallengeEngine(input_pieces, 8, 8)
    end_results = challenge.execute()
    for end_result in end_results:
        print end_result
    end_time = datetime.datetime.now()
    print "Program finished in approximately {} " \
          "seconds, number of unique solutions " \
          "found: {}".format((end_time - start_time).total_seconds(),
                             len(end_results))


if __name__ == "__main__":
    main()
