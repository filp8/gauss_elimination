from gauss import *

# classica matrice quadrata
square_matrix = [[1,3,1,-1],[3,9,4,1],[2,1,5,2],[0,1,-1,-1]]

# matrice non quadrata
general_matrix = [[2,-1,4,1,-2],[-2,1,-7,1,-1],[4,-2,5,4,-7]]

def test_trasportation_for_square_matrix():
    expected = [[1,3,2,0],[3,9,1,1],[1,4,5,-1],[-1,1,2,-1]]
    assert expected == trasportation(square_matrix)
    
def test_trasportation_for_non_square_matrix():
    expected = [[2,-2,4],[-1,1,-2],[4,-7,5],[1,1,4],[-2,-1,-7]]
    assert expected == trasportation(general_matrix)

def test_gauss_test1():
    expected = [[1, 3, 1, -1], [0.0, -5.0, 3.0, 4.0], [0.0, 0.0, 1.0, 4.0], [0.0, 0.0, 0.0, 1.4]]
    assert expected == gauss(square_matrix)
    
def test_sum_line():
    line1 = [1,2,3,4]
    line2 = [-1,-2,-3,-4]
    sum_line(line1,line2)
    assert [0,0,0,0] == line1
    line1 = [3,6,-1,6]
    line2 = [0.5,-0.5,1,-3]
    sum_line(line1,line2)
    assert [3.5, 5.5, 0, 3] == line1
    
def test_dot_product():
    vector1 = [1,7,3,2]
    scalar1 = 3
    expected1 = [3,21,9,6]
    vector2 = [2,8,4,2,6]
    scalar2 = 1/2
    expected2 = [1,4,2,1,3]
    assert expected1 == dot_product(scalar1,vector1)
    assert expected2 == dot_product(scalar2,vector2)
