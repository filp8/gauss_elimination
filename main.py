from gauss import gauss
from tui import input_matrix,printMat

def main():
    matrix = input_matrix()
    printMat(gauss(matrix)[1])


if '__main__' == __name__:
    main()
