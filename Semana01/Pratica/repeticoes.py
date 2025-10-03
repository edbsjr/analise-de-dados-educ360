#-------------repetições--------------
#%%
n = int(input("Vamos imprimir de quantos numeros"))
i = 0

while i < n:
    print(i)
    i = i + 1 
# %%
i = 0
print("Taboada de '",n,"'x 10")
while (i < n):
    print(n, " x ", i+1, " = ",  n * (i+1))
    i = i + 1
# %%
#Ordem descrecente
for x in range(10,0,-1):
    print(x)
# %%
#Ordem crescente
for x in range(1,10,1):
    print(x)
# %%