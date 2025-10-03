# %% Importe o módulo random (módulo nativo do Python).
#Gere uma lista de 5 números aleatórios no intervalo de 1 a 100 e imprima-a.

import random

lista = []

for x in range(0,5):
    lista.append(random.randint(1,100))

print(lista)

# %%
