# %% - Declare duas variáveis, valor_a = 15 e valor_b = 15. Verifique se valor_a é menor que valor_b .
# Imprima o resultado booleano.

a = 15
b = 15

print(a < b)
# %% Declare palavra1 = "Olá" e palavra2 = "olá".
#Verifique se palavra1 é igual a palavra2 e se palavra1 é diferente de palavra2.
#Imprima os resultados das duas comparacoes (booleanos TRUE ou FALSE ).

palavra1 = "Olá"
palavra2 = "olá"
print(palavra1 == palavra2)
print(palavra1 != palavra2)


# %%- Um cliente tem direito a frete grátis se a compra for acima de 200 reais e o cliente for
#cadastrado.
#Atribua a cliente_cadastrado o valor True
#Receba via input o total da compra.
#Armazene em frete_gratis a condição BOOLEANA se total_compra > 200 e
#cliente_cadastrado = True .
#Imprima o valor (booleano) da variável frete_gratis.

cliente_cadastrado = True
valor_total = float(input("Digite o valor total da compra"))

if cliente_cadastrado == True and valor_total > 200:
    frete_gratis = True
else:
    frete_gratis = False

print(f"O frete para a compra é gratis {frete_gratis}")
# %%
