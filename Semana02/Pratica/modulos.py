# -------Modulo interno
#%%
from infos import empresa

print(empresa)
# %%
# --------Modulo Python

import random
numeros = []
for x in range(0,10):
    numeros.append(random.randint(1,100))

numeros
par = 0
impar = 0

for x in range(0,10):
    if numeros[x] % 2 == 0:
        print(numeros[x], "é par")
        par = par + 1
    else:
        print(numeros[x], "é impar")
        impar = impar + 1

print("Quantidade de numero pares :   ", par)
print("Quantidade de numero impares : ", impar)
# %%
