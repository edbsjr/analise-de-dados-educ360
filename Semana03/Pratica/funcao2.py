def soma(pn1:int, pn2:int, pn3:int)->int:
    return pn1+pn2+pn3

def soma_lista(pval:list):
    return sum(pval)

def media(ptotal:float, pqt:int)->float:
    return ptotal / pqt

valores = [30,40,70,80]

print ( media(soma(10,20,30),3))
print(soma_lista(valores))
print(media(soma_lista(valores),len(valores)))