import os
caminho = "novoarquivo.txt"

if os.path.exists(caminho):
    arq = open(caminho, 'a')
else:
    arq = open (caminho, 'a')

linha_add = input("Digite o nome do aluno: ")
linha_add = "\n" + linha_add

arq.write(linha_add)