from tui import *

def getCongruenge(numero:int,modulo:int)->int:
    return numero%modulo

def multiplyTable(insieme:list[int])->list[int]:
    table: list[list[int]] = [[] for _ in range(len(insieme))]
    for x in range(len(insieme)):
        for y in range(len(insieme)):
            table[x].append(insieme[x]*insieme[y])
    return table

def multiplyTableCongruence(insieme:list[int],mod:int)->list[int]:
    table: list[list[int]] = [[] for _ in range(len(insieme))]
    for x in range(len(insieme)):
        for y in range(len(insieme)):
            table[x].append(getCongruenge(insieme[x]*insieme[y],mod))
    return table


ins1 = [0,1,2,3,4,5,6]
printMat(multiplyTable(ins1))
printMat(multiplyTableCongruence(ins1,7))