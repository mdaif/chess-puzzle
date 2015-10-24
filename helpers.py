import math


def king_danger(x1, y1, x2, y2):
    return math.fabs(x1 - x2) <= 1 and math.fabs(y1 - y2) <= 1


def knight_danger(x1, y1, x2, y2):
    deltas = [(-1, -2), (1, -2), (-2, -1), (2, -1), (-2, 1), (2, 1), (-1, 2), (1, 2)]
    return (x1 == x2 and y1 == y2) or any((x2 - x1, y2 - y1) == delta for delta in deltas)
