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

