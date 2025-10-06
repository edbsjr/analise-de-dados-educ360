def calc(pn1:float, pn2:float)->float:
    """
    pn1:
    é o primeiro valor
    
    pn2:
    é o segundo valor

    result:
    é o resultado da soma que retorna
    """
    result = pn1 + pn2
    return result


n1 = int(input("Digite o valor 1"))
n2 = int(input("Digite o valor 2"))

res = calc(n1, n2)

print(res)


