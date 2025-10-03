# @title Listas
# %% Dada a lista alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G'], utilize o fatiamento para extrair e imprimir uma
#sublista contendo apenas os elementos a partir do índice 2 até o índice 5 (exclusivo).
#alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

sub_alf = []
y = 0
for x, letra in enumerate(alfabeto):
    if x>= 2 and x<5:
        sub_alf.append(letra)

print(sub_alf)
# %% Forma melhorada de resolver o exercicio anterior

sub_alf.clear()
sub_alf = alfabeto[2:5]
print(sub_alf)


# %% Utilize a lista numeros = [3,6,9,12,15]
#a) Extraia e imprima todos os números ímpares (começando do índice 0 e pulando de 2 em 2).
#b) Imprima a lista completa em ordem inversa.

numeros = [3,6,9,12,15]

print(f"a) Todos os numeros impares da lista são :{numeros[0:5:2]}")
print(f"b) Lista em ordem inversa {numeros[::-1]}")


# %%

