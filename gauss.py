from typing import Tuple,Iterable
from copy import deepcopy


# line1 = line1 + line2
def sum_line(line1: list[int],line2: list[int]) -> None:
    for n,i in enumerate(line2):
        line1[n] = round(i + line1[n],3)

def dot_product(scalar: int, line: list[int]) -> list[int]:
    result = []
    for i in range(len(line)):
        result.append(round(line[i] * scalar,3))
    return result

def is_zero(start_point,col,matrix) -> Iterable[bool]:
    for i in range(len(matrix[0]) - start_point):
        yield matrix[start_point + i][col] == 0

# line1,line2 = line2,line1
def switch_line(matrix: list[list[int]], i_line1: int, i_line2: int):
    matrix[i_line1],matrix[i_line2] = matrix[i_line2],matrix[i_line1]

def calculate_scalar(pivot,a) -> int:
    return (-1)*(a/pivot)

def simplify(matrix,col,index_pivot) -> None:
    for i in range(1,(len(matrix) - col)): # i posizione relativo rispetto a list1
        if i + col > len(matrix):
            return
        if matrix[index_pivot + i][col] == 0:
            continue
        s = dot_product(calculate_scalar(matrix[index_pivot][col],matrix[index_pivot + i][col]),matrix[index_pivot])
        sum_line(matrix[index_pivot + i],s)


def gauss(matrix: list[list[int]]) -> Tuple[int, list[list[int]]]:
    #TODO: far funzionare l'algoritmo anche per matrici non quadrate
    if len(matrix[0]) != len(matrix):
        raise IndexError(f"The matrix must be a square. Lines = {len(matrix)} Collums = {len(matrix[0])}; {len(matrix)} != {len(matrix[0])}")
    matout = deepcopy(matrix)
    switch_count = 0
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
        
def invertible(matrix: list[list[int]], direct_calculation = False) -> bool:
    if not direct_calculation:
        matrix = gauss(matrix)
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

def cloneAndAppend(A: list[list[float]], b: list[list[float]]) ->list[list[float]]:
    outList=[]
    for i in range(len(A)):
      newRow=list(A[i])
      newRow.append(b[i][0])
      outList.append(newRow)
    return outList

def resultColumn(A: list[list[float]], b: list[list[float]]) ->list[float]:
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

def printMat(mat:list[list[int]]):
    s = str()
    le = 0
    for line in mat:
        for num in line:
                l = len(str(num))
                le = max(le,l)

    for line in mat:
        s+='\n'
        for numero in line:
            s+='  '
            toadd = str(numero)
            if len(toadd)<le:
                spaz = le-len(toadd)
                for i in range(spaz):
                    toadd+=' '
                
            s+=toadd
    print(s)

def antidiagonalTrasportation(matrix: list[list[int]]) -> list[list[int]]:
    matRev=[]
    for line in matrix:
        li = list(reversed(line))
        matRev.append(li)
    matRevOut = list(reversed(matRev))
    return matRevOut

def det(matrix: list[list[int]]) -> int:
    switch_count,matrix = gauss(matrix)
    det = pow(-1,switch_count)
    for i,line in enumerate(matrix):
        det *= line[i]
    return det


# classica matrice quadrata
square_matrix = [[1,3,1,-1],[3,9,4,1],[2,1,5,2],[0,1,-1,-1]]

# matrice non quadrata
general_matrix = [[2,-1,4,1,-2],[-2,1,-7,1,-1],[4,-2,5,4,-7]]

print(square_matrix)
s,mat=gauss(square_matrix)
print(mat)
print(square_matrix)
