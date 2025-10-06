import os
caminho = "arquivo.txt"

if os.path.exists(caminho):
    with open(caminho, 'r') as arq:
        x = 0
        for linha in arq:
            print(linha.rstrip())
            x= x+1
        print(f"Total de Registros :{x}")

else:
    arq = open (caminho, 'w')

print(list(open(caminho, 'r')))