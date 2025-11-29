#%% Conexao com o supabase
from supabase import create_client
import os
from dotenv import load_dotenv

# 1. Carrega as senhas do arquivo .env
load_dotenv() 

# 2. Pega os valores
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase = create_client(url, key)

#%% Leitura dos dados

lojas = supabase.table("lojas").select("*").execute()
dados = lojas.data

# %% Leitura dos dados - criando data frame
import pandas as pd
df_lojas = pd.DataFrame(dados)
df_lojas

#%% Manipulando dados no Supabase via Python - Select com where
lojas = supabase.table("lojas").select("*").eq("unidade","ES").execute()
lojas

# %% Manipulando dados no Supabase insert
lojas = supabase.table("lojas").insert({"unidade":"ES","faturamento":9999,"mes":1}).execute()

#%% Manipulando dados no Supabase update
#lojas = supabase.table("lojas").update({"faturamento":10000}).eq("unidade","ES").execute()
lojas = supabase.table("lojas").update({"faturamento":11000}).match({"unidade":"ES", "mes":1}).execute()

#%% Manipulando dados no Supabase delete
lojas = supabase.table("lojas").delete().match({"unidade":"ES","mes":1}).execute()
# %%
