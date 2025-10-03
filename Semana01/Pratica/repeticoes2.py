# ------------ while TRUE

#%%

boleto_acum = 0.0

while True:
    boleto = float(input("Digite o valor do boleto"))
    if boleto == 0:
        break
    boleto_acum = boleto_acum + boleto

print("Valor total a pagar : R$", boleto_acum)


# %%

empresa = "ESCOLA@gmail.com"

for letra in(empresa):
    if letra == ".":
        break
    print(letra)

# %%
