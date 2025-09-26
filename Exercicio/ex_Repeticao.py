# %% - Use um loop para imprimir os números de 1 a 7.

for x in range(1,11):
    print(x)


    # %% - Use um loop para fazer uma contagem regressiva de 5 até 1, imprimindo cada número.

for x in range(5,0,-1):
    print(x)


# %%- Peça ao usuário para digitar um número e gere a tabuada desse número de 1 a 10 usando um loop

numero = int(input("Digite um número para apresentarmos a tabuada"))

for x in range(0,10):
    print(f"{numero} X {x+1} = {numero * (x+1)}")


# %% - Peça ao usuário para digitar números continuamente. O loop deve parar quando a
#soma dos números digitados ultrapassar 100 ou usuário digitar 0.
num = 1
acum = 0

while num != 0 and acum < 100: 
    num = int(input("Digite um número"))
    acum = acum + num
    print(f"Valor acumulado {acum}")
    

# %%
