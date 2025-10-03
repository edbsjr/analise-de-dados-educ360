# --------------decisões ----------------

#%%
n1 = input("Digite a 1a nota")
n2 = input("Digite a 2a nota")
media = (float(n1) +float(n2)) / 2
print(media)

# %%
if media >= 7:
    if media == 10:
        print("Nota Maxima atingida. Parabens")
    ano = int(input("Digite o ano que cursa"))
    if ano == 3:
        print("Diplomado")
    else:
        print("Aprovado")
elif media >= 3:
    print("Faça outra prova")
else:
    print("Reprovado")
print("Final do Programa")
# %%
