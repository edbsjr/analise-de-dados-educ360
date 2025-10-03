#%% Acessando Elementos e Manipulando uma Lista Dentro da Tupla
#Crie uma tupla que contenha uma string, um número inteiro e, no terceiro elemento, uma lista de nomes.
#Acesse o primeiro nome dentro dessa lista.
#Acrescente o nome Felipe ao final da lista dos nomes.
#dados_empresa = ("Matriz 01", 2023, ["Alice", "Roberto", "Carla"]) 

dados_empresa = ("Matriz 01", 2023, ["Alice", "Roberto", "Carla"])

print(f"O primeiro nome da lista dentro da tupla é {dados_empresa[2][0]}")
dados_empresa[2].append("Felipe")
print(dados_empresa[2])
# %%
