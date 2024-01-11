from gauss import gauss
from tui import input_matrix,printMat

def main():
    #matrix = input_matrix()
    matrix =[[1, 1, 0, 0],[0, 1, 1, 0],[1, 0, 1, 0],[1, 1, 1, 0]]
    printMat(gauss(matrix)[1])


if '__main__' == __name__:
    main()
