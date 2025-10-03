#%%
#----------dicionario
dicio = {"Nome":"Eduardo",
        "Idade":30,
        "Sexo":"Masculino",
        "Linguagens":["Java","Python","C#","React","JavaScript"],
        "Empregos":[
            {"Empresa":"ComercialLojas",    "Cargo":"Vendendor"},
            {"Empresa":"IndustriaFabrica",  "Cargo":"Gerente"},
            {"Empresa":"ServiçoSalao",      "Cargo":"Atendente"},
            ]
        }

print(dicio["Empregos"][-1]["Cargo"])

#%%
print(dicio["Linguagens"])
dicio["Nome"] = "Pereira"
dicio["Idade"] = 18


for chave in dicio.values():
   print(chave)
# %%
