# %% - Peça ao usuário para digitar um número. Se o número for positivo, imprima "Número positivo!".

numero_positivo = int(input("Digite um numero inteiro qualquer"))

if numero_positivo >= 0:
    print("Número Positivo!")

# %% - Peça ao usuário para digitar o turno em que estuda ('M' para manhã, 'N' para noite). Se
#for 'M', imprima "Bom dia!". Caso contrário (para qualquer outro valor, incluindo 'N'),
#imprima "Boa noite!".

horario = input("Digite o horario que estuda ('M' para manhã, 'N' para noite) :")

if horario == "M":
    print("Bom dia!")
elif horario == "N":
    print("Boa noite!")

# %% - Peça ao usuário para digitar uma temperatura em Celsius.
 #◦ Se a temperatura for maior que 30, imprima "Está muito quente!".
 #◦ Se for menor que 10, imprima "Está muito frio!".
 #◦ Caso contrário (entre 10 e 30, inclusive), imprima "Temperatura agradável.".

temperatura = float(input("Digite uma temperatura em Celsius"))

if temperatura >30:
    print("Esta muito quente!")
elif temperatura < 10:
    print("Esta muito frio!")
else:
    print("Temperatura esta agradevel.")

# %% - Peça ao usuário para digitar um número inteiro.
# ◦ Se o número for par, verifique se ele é maior que 10.
# ▪ Se for par e maior que 10, imprima "Número par e grande!".
# ▪ Se for par mas não maior que 10 (ou seja, menor ou igual a 10), imprima "Número par e pequeno.".
# ◦ Se o número for ímpar, imprima "Número ímpar.".

numero = int(input("Digite um número inteiro : "))

if numero % 2 == 0 and numero > 10:
    print(f"Numero {numero} é par e grande")
elif numero % 2 == 0 and numero <= 10:
    print(f"Numero {numero} é par e pequeno")
else:
    print(f"Numero {numero} é impar")

# %%
