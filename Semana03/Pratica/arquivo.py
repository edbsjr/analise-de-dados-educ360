
conteudo = open("novoarquivo.txt", 'a')
conteudo.write("\nLinha adicionada")
linhas = conteudo.read()

print(linhas)


