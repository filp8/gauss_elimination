from typing import Tuple,Iterable,Any
from copy import deepcopy
from fractions import *
from tui import *

def line_to_fractions(line: list[Any]) -> list[Fraction]:
    nline = []
    for num in line:
        if type(num) != float:
            nline.append(Fraction(num))
        else:
            raise ValueError(f"Float type can create problems")
    return nline

def to_fractions(matrix: list[list[Any]]) -> list[list[Fraction]]:
    return [line_to_fractions(line) for line in matrix]

# line1 = line1 + line2
def sum_line(line1: list[Fraction],line2: list[Fraction]) -> None:
    for n,i in enumerate(line2):
        line1[n] = i + line1[n]

def dot_product(scalar: Fraction, line: list[Fraction]) -> list[Fraction]:
    result = []
    for i in range(len(line)):
        result.append(line[i] * scalar)
    return result

def is_zero(start_point,col,matrix) -> Iterable[Fraction]:
    numline = len(matrix)
    for i in range(numline - start_point):
        yield matrix[start_point + i][col] == 0

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
    """
    Check if a matrix is invertible.

    Parameters:
    matrix (list[list[Fraction]]): The matrix to be checked.
    direct_calculation (bool): Flag indicating whether to perform direct calculation or use Gaussian elimination first. Default is False.

    Returns:
    bool: True if the matrix is invertible, False otherwise.
    """
    if not direct_calculation:
        det,matrix = gauss(matrix)
    for i,line in enumerate(matrix):
        if line[i] == 0:
            return False
    return True

def trasportation(matrix: list[list[int]]) -> list[list[int]]:
    new_matrix: list[list[int]] = [[] for _ in range(len(matrix[0]))]
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
        outList.append(updKnown)
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

def det(matrix: list[list[Fraction]]) -> int:
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
        lcan = [Fraction(0)]*ncol
        lcan[i] = Fraction(1)
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

def matrixmoltiplication(matA:list[list[Fraction]],matB:list[list[Fraction]])->list[list[int]]:
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

# classica matrice quadrata
square_matrix = [[1.5,3,1,-1],[3,9,4,1],[2,1,5,2],[0,1,-1,-1]]

# matrice non quadrata
general_matrix = [[2,-1,4,1,-2],[-2,1,-7,1,-1],[4,-2,5,4,-7]]

# matrice invertibile 2x2
invmatrix1 = [[1,2],[2,3]]

# matrice invertibile e la sua inversa
matrix2 = [[1,2,-1],[-2,0,1],[1,-1,0]]
invmatrix2 = [[1,1,2],[1,1,1],[2,3,4]]
