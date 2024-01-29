from tui import *

def getCongruence(numero:int,modulo:int)->int:
    return numero%modulo

def multiplyTable(insieme:list[int])->list[int]:
    table: list[list[int]] = [[] for _ in range(len(insieme))]
    for x in range(len(insieme)):
        for y in range(len(insieme)):
            table[x].append(insieme[x]*insieme[y])
    return table

def sumTable(insieme:list[any])->list[any]:
    table: list[list[int]] = [[] for _ in range(len(insieme))]
    for x in range(len(insieme)):
        for y in range(len(insieme)):
            table[x].append(insieme[x]+insieme[y])
    return table

somma = lambda x,y:(x+y,'+')
moltiplicazione = lambda x,y:(x*y,'*')

def multiplyTableCongruence(insieme:list[int],mod:int,operazione)->list[int]:
    table: list[list[int]] = [[] for _ in range(len(insieme))]
    for x in range(len(insieme)):
        table[x].append(insieme[x])
        for y in range(len(insieme)):
            risultato,segnop = operazione(insieme[x],insieme[y])
            table[x].append(getCongruence(risultato,mod))
    formatline = [segnop]+insieme
    tableout = [formatline]+table
    return tableout

def generatore(unita:int,limit:int,insPartenza:list[int]=None,partenza=0,operazione=somma)->list[list[int]]:
    if insPartenza == None: insPartenza = []
    for i in range(limit):
        insPartenza.append(unita*i)
    return insPartenza

def generatoreR(unita:int,limit:int,insPartenza:list[int],partenza=0,operazione=somma)->list[list[int]]:
    if insPartenza == None: insPartenza = []
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

