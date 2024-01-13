from gauss import gauss
from tui import input_matrix,printMat

def main():
    matrix = input_matrix()
    matrix = [[1,2,3],[3,2,1],[3,1,2]]
    printMat(gauss(matrix)[1])


if '__main__' == __name__:
    main()
