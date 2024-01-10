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

def generatore(unita:int,limit:int,insPartenza:list[int]=[],partenza=0,operazione=somma)->list[list[int]]:
    for i in range(limit):
        insPartenza.append(unita*i)
    return insPartenza

def generatoreR(unita:int,limit:int,insPartenza:list[int]=[],partenza=0,operazione=somma)->list[list[int]]:
    if partenza == 0 and limit>0:
        insPartenza.append(0)
        last,segno = operazione(partenza,unita)
        insPartenza.append(last)
        generatoreR(unita,limit-2,insPartenza,last,operazione)
    elif limit>0:
        last,segno = operazione(partenza,unita)
        insPartenza.append(last)
        generatoreR(unita,limit-1,insPartenza,last,operazione)
    return insPartenza

