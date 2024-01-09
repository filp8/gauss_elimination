from tui import *

def getCongruenge(numero:int,modulo:int)->int:
    return numero%modulo

def multiplyTable(insieme:list[int])->list[int]:
    table: list[list[int]] = [[] for _ in range(len(insieme))]
    for x in range(len(insieme)):
        for y in range(len(insieme)):
            table[x].append(insieme[x]*insieme[y])
    return table

somma = lambda x,y:x+y,'+'
moltiplicazione = lambda x,y:(x*y,'*')

def multiplyTableCongruence(insieme:list[int],mod:int,operazione=moltiplicazione)->list[int]:
    table: list[list[int]] = [[] for _ in range(len(insieme))]
    for x in range(len(insieme)):
        table[x].append(insieme[x])
        for y in range(len(insieme)):
            table[x].append(getCongruenge(operazione(insieme[x],insieme[y])[0],mod))
    formatline = [operazione(1,1)[1]]+insieme
    tableout = [formatline]+table
    return tableout

def generatore(unita:int,operazione=moltiplicazione,limit=int,partenza=0,insPartenza = [])->list[list[int]]:
    for i in range(limit):
        insPartenza.append(partenza+i)
    return insPartenza



u8 = [1,3,5,7]
z4 = [0,1,2,3]
ins1 = [0,1,2,3,4,5,6]
printMat(multiplyTable(ins1))
printMat(multiplyTableCongruence(ins1,7))

printMat(multiplyTableCongruence(u8,8,somma))
printMat(multiplyTableCongruence(z4,4))
