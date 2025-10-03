# %%------Exercicio Listas
#Crie uma lista chamada vendas contendo alguns valores.
# Calcule e imprima:
# a) A soma total dos valores.
# b) O maior e o menor valor.
# c) O número total de itens na lista.
# vendas=[1,2,3,6]

vendas = []
venda = 1
while venda != 0:
   venda = float(input("Digite o valor da venda"))
   if venda != 0:
      vendas.append(venda)
   else:
      print(f"Vendas adicionadas são {vendas} ")
print(f"a) Somatório das vendas = {sum(vendas)}")
print(f"b) O maior e o menor valor, são respectivamente {max(vendas)} e {min(vendas)}")
print(f"c) O número total de itens na lista é {len(vendas)}")

# %% Utilize a lista vendas do exercício anterior. Adicione o valor 500 ao final da lista e, em seguida, insira o valor 999
# na segunda posição (índice 1). Imprima a lista após as modificações.

vendas.append(500)
vendas.insert(1,999)
print(vendas)

# %%
