import sys
import os

from gauss import printMat

def main():
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
    printMat(matrix)


if '__main__' == __name__:
    main()
