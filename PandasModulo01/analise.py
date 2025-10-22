# %% Importando base de dados
import pandas as pd

origem = "https://raw.githubusercontent.com/ivansanchespetrucci/python-pandas/refs/heads/main/base_automoveis.csv"

dados = pd.read_csv(origem)

# %% 1.1 Forma de expor dados
display(dados) # expoem utilizando DISPLAY

# %% 1.2 o head (topo a lista)
print(dados.head()) # expoem utilizando PRINT 

# %% 1.3 a calda da lista
dados.tail(10) # expoem utilizando defaut

# %% 1.4 Tipos de dados
type(dados)

# %% numero de linhas e colunas
dados.shape

dados.columns

# %% informacoes da tabela 
dados.info()

# %% Explorando dados

dados[['modelo']]

# %% duas informacoes
dados[['modelo', 'montadora']]

# %% Analise dos dados - EDA
dados['ano_fabricacao'].mean()

# %%
dados.groupby('montadora').mean(numeric_only=True)

# %%
dados.groupby('montadora')['valor_mercado'].mean()

# %%
dados.groupby('montadora')[['valor_mercado']].mean().sort_values('valor_mercado',ascending=False))

# %%
dados.groupby('montadora')[['valor_mercado']].mean().sort_values('valor_mercado',ascending=True).head(3)
# %% Analise de dados - Percentual
dados_montadora = dados.groupby('montadora')[['valor_mercado']].mean().sort_values('valor_mercado',ascending=True)
dados_montadora.plot(kind='bar', figsize=(10,5), color='blue')

# %%
dados2 = dados.montadora.value_counts()
dados2.plot(kind='barh')

# %%
dados.montadora.value_counts(normalize=True)

# %% Verificar Valores Nulos

dados.isnull().sum()

# %%

dados = dados.fillna(0)

# %%
dados.isnull().sum()
# %% Aplicar filtros
dados.montadora.unique()
filtro = ["Ford", "Toyota"]
# %% Aplicar filtros
dados.query('montadora == "Ford"')
# %% Aplicar filtros
dados_pesq = dados.query('@filtro in montadora')
dados_montadora = dados_pesq.groupby('montadora')[['valor_mercado']].mean().sort_values('valor_mercado')
dados_montadora.plot(kind='barh')
# %% Aplicar filtros Ano e valor
dados_filtro_ano = dados_pesq['ano_fabricacao'] >= 2020
dados_pesq[dados_filtro_ano]

# %%
