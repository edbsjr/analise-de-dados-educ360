# %%--------------Exercicio para Pratica de Dicionario ---------------

produto = input("Digite o nome do produto")

catalogo = {
    "TV":       {"Valor": 1500.00},
    "Celular":  {"Valor": 2500.00},
    "Computador": {"Valor": 3500.00},
    "Tablet":   {"Valor": 1000.00},
    "Fone":     {"Valor": 100.00},
}

if produto in catalogo:
    print(f"O produto {produto} custa R${catalogo[produto]["Valor"]}") 
else:
    print(f"Produto '{produto}' não encontrado no catálogo.")
# %%
