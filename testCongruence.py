from congruence import *
from gauss import to_fractions


def test_multiplyTableCongruence():
    expected = [['*', 0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 2, 3, 4, 5, 6, 7, 8], [2, 0, 2, 4, 6, 8, 1, 3, 5, 7], [3, 0, 3, 6, 0, 3, 6, 0, 3, 6], [4, 0, 4, 8, 3, 7, 2, 6, 1, 5], [5, 0, 5, 1, 6, 2, 7, 3, 8, 4], [6, 0, 6, 3, 0, 6, 3, 0, 6, 3], [7, 0, 7, 5, 3, 1, 8, 6, 4, 2], [8, 0, 8, 7, 6, 5, 4, 3, 2, 1]]
    assert expected == multiplyTableCongruence(generatore(1,9),9,moltiplicazione)

