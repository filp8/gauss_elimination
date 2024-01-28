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

def test_line_to_fractions():
    expected = [Fraction(1, 1), Fraction(1, 2), Fraction(1, 3),Fraction(1, 4),Fraction(1, 5)]
    assert expected == line_to_fractions(['1/1','1/2','1/3','1/4','1/5'])

def test_to_fractions():
    expected = [[Fraction(1, 1), Fraction(1, 2), Fraction(1, 3), Fraction(1, 4), Fraction(1, 5)], [Fraction(1, 6), Fraction(1, 7), Fraction(1, 8), Fraction(1, 9), Fraction(1, 10)], [Fraction(1, 11), Fraction(1, 12), Fraction(1, 13), Fraction(1, 14), Fraction(1, 15)], [Fraction(1, 16), Fraction(1, 17), Fraction(1, 18), Fraction(1, 19), Fraction(1, 20)], [Fraction(1, 21), Fraction(1, 22), Fraction(1, 23), Fraction(1, 24), Fraction(1, 25)]]
    assert expected == to_fractions([['1/1','1/2','1/3','1/4','1/5'],['1/6','1/7','1/8','1/9','1/10'],['1/11','1/12','1/13','1/14','1/15'],['1/16','1/17','1/18','1/19','1/20'],['1/21','1/22','1/23','1/24','1/25']])

def test_switch_line():
    expected = [[2, -1, 4, 1, -2], [4, -2, 5, 4, -7], [-2, 1, -7, 1, -1]]
    assert expected == switch_line([[2,-1,4,1,-2],[-2,1,-7,1,-1],[4,-2,5,4,-7]],1,2)

def test_calculate_scalar():
    expected = Fraction(-9,8)
    assert expected == calculate_scalar(Fraction(2,3),Fraction(3,4))

def test_invertible():
    expected = True
    assert expected == invertible(invertible_matrix)

def test_antidiagonalTrasportation():
    expected = [[-1, -1, 1, 0], [2, 5, 1, 2], [1, 4, 9, 3], [-1, 1, 3, 1]]
    assert expected == antidiagonalTrasportation([[1,3,1,-1],[3,9,4,1],[2,1,5,2],[0,1,-1,-1]])

def test_matRigToCol():
    expected = [[1, 3, 2, 0], [3, 9, 1, 1], [1, 4, 5, -1], [-1, 1, 2, -1]]
    assert expected == matRigToCol([[1,3,1,-1],[3,9,4,1],[2,1,5,2],[0,1,-1,-1]])

def test_matrixmoltiplication():
    expected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    assert expected == matrixmoltiplication([[1,2,-1],[-2,0,1],[1,-1,0]],[[1,1,2],[1,1,1],[2,3,4]])

#TODO test per is_zero ??
#TODO test per simplify ??
#TODO test per cloneAndAppend ??
#TODO test per resultColumn ??
#TODO test per det ??



