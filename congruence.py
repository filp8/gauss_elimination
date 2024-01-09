from tui import *

def getCongruenge(numero:int,modulo:int)->int:
    return numero%modulo

def multiplyTable(insieme:list[int])->list[int]:
    table: list[list[int]] = [[] for _ in range(len(insieme))]
    for x in range(len(insieme)):
        for y in range(len(insieme)):
            table[x].append(insieme[x]*insieme[y])
    return table

somma = lambda x,y:(x+y,'+')
moltiplicazione = lambda x,y:(x*y,'*')

def multiplyTableCongruence(insieme:list[int],mod:int,operazione)->list[int]:
    table: list[list[int]] = [[] for _ in range(len(insieme))]
    for x in range(len(insieme)):
        table[x].append(insieme[x])
        for y in range(len(insieme)):
            #print(type(insieme[x]))
            #print(type(operazione))
            risultato,segnop = operazione(insieme[x],insieme[y])
            #print(risultato)
            table[x].append(getCongruenge(risultato,mod))
    formatline = [segnop]+insieme
    tableout = [formatline]+table
    return tableout

def generatore(unita:int,limit:int,insPartenza:list[int]=[],partenza=0,operazione=somma,)->list[list[int]]:
    for i in range(limit):
        insPartenza.append(partenza+i)
    return insPartenza



print(generatore(1,100))


u8 = [1,3,5,7]
z4 = [0,1,2,3]
ins1 = [0,1,2,3,4,5,6]


printMat(multiplyTable(ins1))
printMat(multiplyTableCongruence(ins1,7,moltiplicazione))

printMat(multiplyTableCongruence(u8,8,somma))
printMat(multiplyTableCongruence(z4,4,moltiplicazione))
