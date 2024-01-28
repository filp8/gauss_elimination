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


#TODO test per is_zero ??








def test_to_fractions():
    expected = [[Fraction(1, 1), Fraction(1, 2), Fraction(1, 3), Fraction(1, 4), Fraction(1, 5)], [Fraction(1, 6), Fraction(1, 7), Fraction(1, 8), Fraction(1, 9), Fraction(1, 10)], [Fraction(1, 11), Fraction(1, 12), Fraction(1, 13), Fraction(1, 14), Fraction(1, 15)], [Fraction(1, 16), Fraction(1, 17), Fraction(1, 18), Fraction(1, 19), Fraction(1, 20)], [Fraction(1, 21), Fraction(1, 22), Fraction(1, 23), Fraction(1, 24), Fraction(1, 25)]]
    assert expected == to_fractions([['1/1','1/2','1/3','1/4','1/5'],['1/6','1/7','1/8','1/9','1/10'],['1/11','1/12','1/13','1/14','1/15'],['1/16','1/17','1/18','1/19','1/20'],['1/21','1/22','1/23','1/24','1/25']])




# line1,line2 = line2,line1
def switch_line(matrix: list[list[Fraction]], i_line1: int, i_line2: int):
    matrix[i_line1],matrix[i_line2] = matrix[i_line2],matrix[i_line1]

def calculate_scalar(pivot:Fraction,a:Fraction) -> Fraction:
    return (Fraction(-1))*(a/pivot)

def simplify(matrix:list[list[Fraction]],col,index_pivot):
    for i in range(1,(len(matrix) - col)): # i posizione relativo rispetto a list1
        if i + col > len(matrix):
            return
        if matrix[index_pivot + i][col] == 0:
            continue
        s = dot_product(calculate_scalar(matrix[index_pivot][col],matrix[index_pivot + i][col]),matrix[index_pivot])
        sum_line(matrix[index_pivot + i],s)


def gauss(matrix: list[list[Fraction]]) -> Tuple[int, list[list[Fraction]]]:
    if not (isinstance(matrix, list) and all(isinstance(line, list) and all(isinstance(e, Fraction) for e in line) for line in matrix)):
        matrix = to_fractions(matrix)
    switch_count = 0
    matout = deepcopy(matrix)
    for i,line in enumerate(matout):
        pivot = line[i]
        if pivot == 0:
            if all(is_zero(i + 1,i,matout)):
                continue
            else:
                switch_count += 1
                i_not_zero = 0
                for n,line1 in enumerate(matout[i:], start=i):
                    if line1[i] != 0:
                        i_not_zero = n
                        break
                switch_line(matout,i,i_not_zero)
        simplify(matout,i,i)
    return switch_count,matout
        
def invertible(matrix: list[list[Fraction]], direct_calculation = False) -> bool:
    if not direct_calculation:
        det,matrix = gauss(matrix)
    for i,line in enumerate(matrix):
        if line[i] == 0:
            return False
    return True

def trasportation(matrix: list[list[Fraction]]) -> list[list[Fraction]]:
    new_matrix: list[list[Fraction]] = [[] for _ in range(len(matrix[0]))]
    for line in matrix:
        for i,new_line in zip(line,new_matrix):
            new_line.append(i)
    return new_matrix

def cloneAndAppend(A: list[list[Fraction]], b: list[list[Fraction]]) ->list[list[Fraction]]:
    outList=[]
    for i in range(len(A)):
      newRow=list(A[i])
      newRow.append(b[i][0])
      outList.append(newRow)
    return outList

def resultColumn(A: list[list[Fraction]], b: list[list[Fraction]]) ->list[Fraction]:
    Ab=cloneAndAppend(A, b)
    gauss(Ab)
    print("gauss(Ab) =", Ab)

    outList=[]

    colCount=len(A)
    for j in reversed(range(colCount)):
        i=j #diagonale principale
        a_ij=Ab[i][j]
        b_i=Ab[i][-1]
        updKnown=b_i/a_ij
        outList.append([updKnown])
        for k in range(j):
            coefToNull=A[k][j]
            Ab[k][-1]-=updKnown*coefToNull

    outList.reverse()
    return  outList

def antidiagonalTrasportation(matrix: list[list[Fraction]]) -> list[list[Fraction]]:
    matRev=[]
    for line in matrix:
        li = list(reversed(line))
        matRev.append(li)
    matRevOut = list(reversed(matRev))
    return matRevOut

def det(matrix: list[list[Fraction]]) -> Fraction:
    switch_count,matrix = gauss(matrix)
    det = pow(-1,switch_count)
    for i,line in enumerate(matrix):
        det *= line[i]
    return det

def inversematrix(matrix: list[list[Fraction]]) -> list[list[Fraction]]:
    if len(matrix[0]) != len(matrix):
        raise IndexError(f"The matrix must be a square. Lines = {len(matrix)} Collums = {len(matrix[0])}; {len(matrix)} != {len(matrix[0])}")
    if not(invertible(matrix)):
        raise IndexError(f"The matrix is not invertible.")
    matout = deepcopy(matrix)
    nline = len(matrix)
    ncol = len(matrix[0])
    for i,line in enumerate(matout):
        lcan = [0]*ncol
        lcan[i] = 1
        line+=lcan
    det,matout = gauss(matout)
    matoutcol = matRigToCol(matout) 
    matsx = matoutcol[0:ncol]
    matdx = matoutcol[ncol:]
    matsx = matRigToCol(matsx)
    matdx = matRigToCol(matdx)
    matsx = antidiagonalTrasportation(matsx)
    matdx = antidiagonalTrasportation(matdx)
    matouttrasp = []
    for i,linesx in enumerate(matsx):
            matouttrasp.append(linesx+matdx[i])
    det,matouttraspg=gauss(matouttrasp)
    for i,line in enumerate(matouttraspg):
        if line[i]!=1 and line[i]!=0:
            div = line[i]
            nline = []
            for num in line:
                nline.append(num/div)
            matouttraspg[i]=nline
    finalmat = antidiagonalTrasportation(matRigToCol(matRigToCol(matouttraspg)[ncol:]))
    return finalmat

def matRigToCol(matrix: list[list[Fraction]]) -> list[list[Fraction]]:
    matout = []
    for i,col in enumerate(matrix[0]):
        colonna = []
        for rig in matrix:
            colonna.append(rig[i])
        matout.append(colonna)
    return matout

def matrixmoltiplication(matA:list[list[Fraction]],matB:list[list[Fraction]])->list[list[Fraction]]:
    matB = matRigToCol(matB)
    matout = []
    for line in matA:
        lout = []
        for col in matB:
            nout = 0
            for i,numa in enumerate(line):
                nout += numa * col[i]
            lout.append(nout)
        matout.append(lout)
    return matout
