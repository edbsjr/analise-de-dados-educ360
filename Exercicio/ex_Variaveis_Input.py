# %% - Declare uma variável chamada nome_cidade com o valor "São Paulo" e uma variável
#chamada temperatura com o valor 23.5. Em seguida, exiba o tipo de cada variável
#usando a função type().

nome_cidade = "São Paulo"
temperatura = 23.5

print("Variavel nome_cidade do tipo= ", type(nome_cidade))
print("Variavel temperatura do tipo= ", type(temperatura))


# %%- Peça ao usuário para digitar o número de alunos em uma turma e armazene-o em uma
#variável, garantindo que seja do tipo inteiro. Em seguida, imprima o número de alunos

numero_alunos = int(input("Digite a quantidade de alunos da turma: "))

print(f"O numero total de alunos é {numero_alunos}")


# %% - Peça ao usuário para digitar o preço unitário de um item (que pode ter casas decimais)
#e armazene-o em uma variável, garantindo que seja do tipo float. Imprima o preço
#digitado.

preco_produto = float(input("Digite o valor unitario do item. "))

print(f"O valor unitario do item é {preco_produto}")

# %% - Peça ao usuário para digitar um número e exiba a raiz quadrada desse número.

numero_raiz = int(input("Digite um numero: "))

print(f"O número {numero_raiz} tem a raiz quadrada de {numero_raiz**(1/2)}")
# %%
