import os
import sys

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

def input_matrix() -> list[list[int]]:
    matrix: list[list[int]] = []
    i = 0
    while True:
        matrix.append([])
        line = input("> ")
        if (line == "e") | (line == "end"):
            break
        for literal in line.split():
            try:
                matrix[i].append(int(literal))
            except ValueError:
                print(f"[INPUT ERROR] '{literal}' is not a base 10 number",file=sys.stderr)
                os._exit(1)
        if i == 0:
            i += 1
            continue
        if len(matrix[i - 1]) != len(matrix[i]):
            print(f"[INPUT ERROR] Matrix lines have different lenghts",file=sys.stderr)
            os._exit(1)
        i += 1
    matrix.pop() # the last element is an empty list
    return matrix 
