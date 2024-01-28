from copy import deepcopy
from gauss import *

# classica matrice quadrata
square_matrix = to_fractions([[1,3,1,-1],[3,9,4,1],[2,1,5,2],[0,1,-1,-1]])

# matrice non quadrata
general_matrix = to_fractions([[2,-1,4,1,-2],[-2,1,-7,1,-1],[4,-2,5,4,-7]])

# matrice invertibile
invertible_matrix = to_fractions([[1,2,-1],[-2,0,1],[1,-1,0]])

def test_inversematrix():
    expected = to_fractions([[1,1,2],[1,1,1],[2,3,4]])
    assert expected == inversematrix(invertible_matrix)

def test_trasportation_for_square_matrix():
    expected = to_fractions([[1,3,2,0],[3,9,1,1],[1,4,5,-1],[-1,1,2,-1]])
    assert expected == trasportation(square_matrix)
    
def test_trasportation_for_non_square_matrix():
    expected = to_fractions([[2,-2,4],[-1,1,-2],[4,-7,5],[1,1,4],[-2,-1,-7]])
    assert expected == trasportation(general_matrix)

def test_gauss_test1():
    expected = to_fractions([[1, 3, 1, -1], [0, -5, 3, 4], [0, 0, 1, 4], [0, 0, 0, Fraction(7,5)]])
    switch,new_matrix = gauss(square_matrix)
    assert pow(-1,switch) == -1 # controllo se switch è pari
    assert expected == new_matrix
    
def test_sum_line():
    line1 = line_to_fractions([1,2,3,4])
    line2 = line_to_fractions([-1,-2,-3,-4])
    sum_line(line1,line2)
    assert line_to_fractions([0,0,0,0]) == line1
    line1 = line_to_fractions([3,6,-1,6])
    line2 = line_to_fractions([Fraction(1,2),Fraction(-1,2),1,-3])
    sum_line(line1,line2)
    assert line_to_fractions([Fraction(7,2), Fraction(11,2), 0, 3]) == line1
    
def test_dot_product():
    vector1 = line_to_fractions([1,7,3,2])
    scalar1 = 3
    expected1 = line_to_fractions([3,21,9,6])
    vector2 = line_to_fractions([2,8,4,2,6])
    scalar2 = Fraction(1,2)
    expected2 = line_to_fractions([1,4,2,1,3])
    assert expected1 == dot_product(scalar1,vector1)
    assert expected2 == dot_product(scalar2,vector2)
