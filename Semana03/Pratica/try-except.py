'''try:
    x = 12 / 0
except Exception as erro:
    print("Erro: ", erro)
'''

try:
    open("C:/Users/Carlos/Documents/Projetos/curso_python/Semana03/Pratica/dados.txt")
except Exception as erro:
    print("Novo Error: ", erro)