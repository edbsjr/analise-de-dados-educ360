#-----------Variaveis booleano -------------

print("4 > 5?", 4 > 5)
print("4 < 5?", 4 < 5)
print("4 = 5?", 4 == 5)
print("Eduardo = Eduardo", "Eduardo" == "Eduardo")
print("Eduardo = Bruno", "Eduardo" == "Bruno")
print("Eduardo diferente Eduardo", "Eduardo" != "Eduardo")

#%%
# and or

a = 5
b = 8
c = 4

if(a > c and b < c):
    print("Verdadeiro")
else:
    print("Falso")

# %%

print("a > b and c < a =", a > b and c < a)
print("a > b or c < a =", a > b or c < a)
print("not c < a =", not(c < a))

# %%
