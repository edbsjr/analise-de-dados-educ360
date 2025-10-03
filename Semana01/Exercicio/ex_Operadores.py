# %% Dois numeros quaisquer

num1 = float(input("Digite o 1º número:"))
num2 = float(input("Digite o 2º número:"))

print("Soma =>          ",num1, " + ", num2, " = ", num1 + num2)
print("Subtração =>     ",num1, " - ", num2, " = ", num1 - num2)
print("Multiplicação => ",num1, " x ", num2, " = ", num1 * num2)
if num2 == 0:
    print("Não é possivel dividir por 0")
else:
    print("Divisão =>       ",num1, " / ", num2, " = ", num1 / num2)
# %% Parte inteira da divisão

print(" A parte inteira da divisão :")
print(num1," / ", num2, " = ", num1 // num2 )
print(" O resto da divisão :")
print(num1," / ", num2, " = ", num1 % num2 )


# %% Potencia do numero

print("A potenciação dos numeros:")
print(num1, "elevado a ", num2, " = ", num1 ** num2)

# %% Resultado da expressão

print("Qual o resultado da expressão 10 + 6 * 2?")
print(10 + 6 * 2)

# %%
