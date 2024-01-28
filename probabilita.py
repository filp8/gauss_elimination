from gauss import *

def markov(vet:list[Fraction],mat:list[list[Fraction]], n:int) -> list[Fraction]:
    v = [vet]
    print(v)
    for i in range(n):
        v = matrixmoltiplication(v,mat)
    return v


# matrici per markov
markovmat =to_fractions([['1/2','1/4','1/4'],['1/4','1/2','1/4'],['1/4','1/4','1/2']])
markovvet = [1,0,0]
