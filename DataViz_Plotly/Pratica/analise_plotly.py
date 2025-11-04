#%%
import plotly.express as px

px.line(x=[1,2,3,4,5,6,7,8,9,10], y=[10,50,15,12,10,30,50,90,10,20], title='Grafico do tipo XY')

# %% Atividade com Pandas
import pandas as pd
import numpy as np
#%% Grafico de Linha
df = px.data.gapminder().query("continent=='Americas' and year >= 2000")
px.line(df, x='year', y ='lifeExp', title='Expectativa de Vida',color='country')

# %% Grafico de Linha
df = pd.read_csv('https://raw.githubusercontent.com/profivan-ai/cdb-Python/refs/heads/main/arquivos/viagens.csv', sep=';')
df_meses = df.groupby(['mes'], sort=False).mean().reset_index()
#px.line(df_meses,x='mes', y='viagens', title='Media de viagens por mes',color='ano')
px.line(df,x='mes', y='viagens', title='Viagens por mes',color='ano')

# %% 
df = pd.read_csv('https://raw.githubusercontent.com/profivan-ai/cdb-Python/refs/heads/main/arquivos/compras.csv', sep=';')
df
# %% Grafico de Barras
df_dia = df.groupby("dia",sort=False).agg({"valor": np.sum}).reset_index()
#df_dia
px.bar(df_dia, x = "dia", y = "valor", title = "Compras por dia da Semana", color = "dia")

# %% Grafico de Barras
df_dia = df.groupby(["dia", "sexo"], sort=False).agg({"valor": np.sum}).reset_index()
px.bar(df_dia, x = "dia", y = "valor",title = "Compras por dia da Semana por Publico", color = "sexo", barmode="group", text="valor")

# %% Grafico de Barras
df_dia = df.groupby(["dia", "sexo"], sort=False).agg({"valor": np.sum}).reset_index()
px.bar(df_dia, x = "valor", y = "dia",title = "Compras por dia da Semana por Publico", color = "sexo", barmode="group", orientation="h", hover_name="valor")

# %% Grafico de Barras - Apresenta certa dificuldade. Sugerido estruturar melhor os dados
df_dia = df.groupby(["dia","clube"], sort=False).agg({"valor": np.sum}).reset_index()
px.bar(df_dia, x = "dia", y = "valor",title = "Compras por dia da Semana por Publico", color = "clube", text="valor", barmode= "group", )

#%% Grafico de Barras Agrupando Membros Clube
df = pd.read_csv('https://raw.githubusercontent.com/profivan-ai/cdb-Python/refs/heads/main/arquivos/compras2.csv', sep=';')
df_dia = df.groupby(["dia","clube"], sort=False).agg({"valor": np.sum}).reset_index()
px.bar(df_dia, x = "dia", y = "valor",title = "Compras por dia da Semana por Publico", color = "clube", text="valor", barmode= "group", )

#%% Grafico de Pizza
df_agrupado = df.groupby("dia", sort=False).agg({"valor": np.sum}).reset_index()
px.pie(df_agrupado, values="valor", names="dia", title="Compras separadas por dia da semana",opacity=0.5, color_discrete_sequence= px.colors.sequential.RdBu)

# %%
