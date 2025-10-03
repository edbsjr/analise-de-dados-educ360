#%% Crie um dicionário chamado aluno contendo chaves para nome, idade e curso. Imprima o nome
#do aluno acessando-o diretamente pela chave.

dicio_aluno = {
            "Nome":"Eduardo Pereira", 
            "Idade":20, 
            "Curso":"Analise de Dados"
            }

print(dicio_aluno["Nome"])

# %%Crie um dicionário chamado estoque com alguns produtos. Peça ao usuário que digite um nome de produto.
#Antes de tentar imprimir o preço, verifique se a chave digitada existe no dicionário para evitar erros.

estoque = {
    "TV":           1500.00,
    "Celular":      2500.00,
    "Computador":   3500.00,
    "Tablet":       1000.00,
    "Fone":         100.00
}

produto = input("Digite o produto")

if produto in estoque:
    print(f"O produto {produto} custa R${estoque[produto]}") 
else:
    print(f"Produto '{produto}' não encontrado no catálogo.")
# %%
