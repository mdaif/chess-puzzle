import datetime

from helpers import king_danger, knight_danger


class ChessChallengeEngine(object):
    def __init__(self, pieces, board_width, board_height):
        self.pieces = sorted(
            pieces)  # sorting lexographically to make sure all possible
        # permutations of the same problem maps to the same input

        self.board_width = board_width
        self.board_height = board_height
        self.all_pieces = pieces  # won't be decremented at each step

    def execute(self):
        solutions = [[]]
        for row in range(self.board_height):
            if self.pieces:
                solutions, self.pieces = self.add_one_piece(self.pieces,
                                                            self.board_height,
                                                            solutions)
                # after first iteration, we can find the inserted pieces are
                #  less than the expected to be inserted.
                if len(solutions) < len(self.pieces):
                    return [[]]

        return solutions

    def add_one_piece(self, pieces, columns, prev_solutions):
        # print "previous solutions: ", prev_solutions
        current_piece = pieces[0]
        solutions = []
        seen = []

        for solution in prev_solutions:

            # the number of rows to be examined differs based on the type of
            #  piece being played ... we can always check for all rows but
            # it becomes very expensive when you have all queens and the
            # number of pieces > 7 (that's an imperical observation). That
            # is a corner case and we should then only examine the row next
            # to the row we already examined.
            rows = len(solution) + 2 if set(self.all_pieces) == set([
                'Queen']) and len(
                self.all_pieces) > 7 else self.board_height + 1
            for row in range(1, rows):
                for column in range(1, columns + 1):
                    if not self.under_attack(current_piece, row, column,
                                             solution):

                        result = sorted(
                            solution + [(current_piece, row, column)])
                        if result not in seen:
                            seen.append(result)
                            solutions.append(result)
        self.pieces = self.pieces[1:]
        return solutions, self.pieces

    @staticmethod
    def under_attack(current_piece, row, column, candidate_solution):
        for chess_piece in candidate_solution:

            attacking_piece, r, c = chess_piece
            if current_piece == 'Queen' or attacking_piece == 'Queen':
                if r == row:
                    return True  # Check row
                if c == column:
                    return True  # Check column
                if (column - c) == (row - r):
                    return True  # Check left diagonal
                if (column - c) == -(row - r):
                    return True  # Check right diagonal

            elif current_piece == 'King':
                if king_danger(r, c, row, column):
                    return True
                if attacking_piece == 'Rook':
                    if r == row:
                        return True  # Check row
                    if c == column:
                        return True  # Check column
                        # print
            elif current_piece == 'Rook':
                # print "r,c,row, col", r, c, row, column
                if r == row:
                    return True  # Check row
                if c == column:
                    return True  # Check column
                if attacking_piece == 'King':
                    if king_danger(r, c, row, column):
                        return True
                if attacking_piece == 'Knight':
                    if knight_danger(r, c, row, column):
                        return True

            elif current_piece == 'Knight':
                if knight_danger(r, c, row, column):
                    return True

                if attacking_piece == 'Bishop':
                    if (column - c) == (row - r):
                        return True  # Check left diagonal
                    if (column - c) == -(row - r):
                        return True  # Check right diagonal

            elif current_piece == 'Bishop' or attacking_piece == 'Bishop':
                if (column - c) == (row - r):
                    return True  # Check left diagonal
                if (column - c) == -(row - r):
                    return True  # Check right diagonal

                if attacking_piece == 'Knight':
                    if knight_danger(r, c, row, column):
                        return True

        return False


if __name__ == "__main__":
    start_time = datetime.datetime.now()
    #    pieces = ['Rook', 'Rook', 'Knight', 'Knight', 'Knight', 'Knight']
    # pieces = ['Knight', 'Knight', 'Bishop']
    pieces = ['Queen'] * 8

    challenge = ChessChallengeEngine(pieces, 8, 8)
    results = challenge.execute()
    for result in results:
        print result
    end_time = datetime.datetime.now()
    print "Program finished in approximately {} " \
          "seconds, number of unique solutions " \
          "found: {}".format((end_time - start_time).total_seconds(), 
                             len(results))
