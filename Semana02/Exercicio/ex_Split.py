#%% Você recebeu uma linha de dados de um arquivo CSV que lista nomes de países. Use a função
#split() para transformar a string registro_paises em uma lista, separando os nomes pela vírgula.
#registro_paises = "Brasil,Argentina,Chile,Uruguai,Paraguai"

registro_paises = "Brasil,Argentina,Chile,Uruguai,Paraguai"
lista = registro_paises.split(",")

print(lista)

# %%Receba um registro de funcionário onde os campos estão separados por ponto-e-vírgula. Quebre o registro e,
#em seguida, verifique se o salário (terceiro campo) é maior que 50000. Lembre-se de que os valores vêm como
#string e precisam ser convertidos para float para comparação numérica.
#Ex: registro_funcionario = "ID005;Maria Silva;12500.75;Contabilidade"

registro_funcionario = "ID005;Maria Silva;51500.75;Contabilidade"

registro = registro_funcionario.split(";")

if float(registro[2]) > 50000.00:
    print(registro)
# %%
