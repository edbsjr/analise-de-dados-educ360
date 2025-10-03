# ------------------listas ---------------
#%%
dados = [10,40,20,50]

type(dados)

print(dados)

#%%

for x in range(4):
    print(dados[x])

# %%

dados[3] = 60

print(dados[-1])

# %%
print("Soma ", sum(dados))
print("Maior ", max(dados))
print("Menor ", min(dados))
print("Media ", sum(dados) / len(dados))

print("Classificado decrescente  ", sorted(dados, reverse=True))
# %%
