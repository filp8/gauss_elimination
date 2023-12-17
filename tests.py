from gauss import *

# classica matrice quadrata
square_matrix = [[1,3,1,-1],[3,9,4,1],[2,1,5,2],[0,1,-1,-1]]

# matrice non quadrata TODO: crearla
general_matrix = [[]]

def test_trasportation_for_square_matrix():
    expected = [[1,3,2,0],[3,9,1,1],[1,4,5,-1],[-1,1,2,-1]]
    assert expected == trasportation(square_matrix)
    
def test_trasportation_for_non_square_matrix():
    #TODO
    pass

def test_gauss_test1():
    #TODO: levare matrice che fa questo output di merda
    expected = [[1, 3, 1, -1], [0.0, -5.0, 3.0, 4.0], [0.0, 0.0, 1.0, 4.0], [0.0, 0.0, 0.0, 1.3999999999999997]]
    assert expected == gauss(square_matrix)
    
def test_dot_product():
    vector1 = [1,7,3,2]
    scalar1 = 3
    expected1 = [3,21,9,6]
    vector2 = [2,8,4,2,6]
    scalar2 = 1/2
    expected2 = [1,4,2,1,3]
    assert expected1 == dot_product(scalar1,vector1)
    assert expected2 == dot_product(scalar2,vector2)
