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

# %% 1.5numero de linhas e colunas
print(dados.shape)

print(dados.columns) #exibe todas as colunas

# %% 1.5 informacoes da tabela 
dados.info()

# %% 2.1 Explorando dados

#dados['modelo'] # Duas formas diferentes de visualizar a coluna

dados[['modelo']]

# %% 2.2 duas colunas
dados[['modelo', 'montadora']]
#dados['modelo', 'montadora'] #ESSA VERSAO NAO FUNCIONA

# %% 3 Analise dos dados - EDA
dados['valor_mercado'].mean() # media

# %% 3.1 Agrupando dados
#dados.groupby('montadora').mean(numeric_only=True) # perde o index
dados.groupby('montadora').mean(numeric_only=True).reset_index() #reorganiza o index


# %% 3.1.1 Agrupando mais dados
dados.groupby('montadora')[['valor_mercado','ano_fabricacao']].mean().reset_index()

# %% 3.1.2 Agrupando dados com apenas uma colunas
dados.groupby('montadora')['valor_mercado'].mean().reset_index()

# %% 3.2 Ordenando dados Ancendentes 
display(dados.groupby('montadora').mean(numeric_only=True).sort_values('valor_mercado',ascending=False).reset_index())

# %% 3.3 Ordenando dados descendentes
dados.groupby('montadora')[['valor_mercado']].mean().sort_values('valor_mercado',ascending=True).reset_index()

# %% 4 Analise de dados
display (dados.groupby('montadora')[['valor_mercado']].mean().sort_values('valor_mercado',ascending=True).reset_index()) # note o reset_index nao ocorre no proximo comando

dados_montadora = dados.groupby('montadora')[['valor_mercado']].mean().sort_values('valor_mercado',ascending=True)

# %% 4.1 imprimindo grafico
dados_montadora.plot(kind='bar', figsize=(10,5), color='blue')

# %% 4.2 Conta numeros de cada montadora  e coloca em grafico padronizado
print(dados.montadora.value_counts()) 
dados2 = dados.montadora.value_counts()
dados2.plot(kind='bar')

# %% 4.3 transforma em porcentagem
dados.montadora.value_counts(normalize=True) 

# %%
dados.fillna(0)

# %% 5 Verificar Valores Nulos
dados.isnull().sum()

# %% 5.1 transforma dados nulos em 0
dados_tratados = dados.fillna(0)
display(dados_tratados)
# %% 5.2 conferindo a correcao. Nao indicada pois impacta resultados
dados_tratados.isnull().sum()
#dados_tratados['valor_mercado'].mean()

# %% 5.3 Tratamento correto para o caso
media_arredondada = round(dados['valor_mercado'].mean(), 2)
dados_tratados = dados.fillna(media_arredondada)

dados_tratados['valor_mercado'].mean()
# %% 6 Aplicar filtros
display(dados_tratados.montadora.unique())
filtro = ["Ford", "Toyota", "Honda"]

# %% 6.1 Aplicar filtros
dados_tratados.query('montadora == "Ford"')

# %% 6.2 Aplicar filtros
dados_pesq = dados_tratados.query('@filtro in montadora')
dados_montadora = dados_pesq.groupby('montadora')[['valor_mercado']].mean().sort_values('valor_mercado')
dados_montadora.plot(kind='barh')

# %% 6.3 Aplicar filtros Ano e valor
dados_filtro_ano = dados_pesq['ano_fabricacao'] > 2021
selecao = dados_pesq[dados_filtro_ano]
display(selecao)
# %% 7 Salvar dados
selecao.to_csv('pesq_claudio.csv')

# %% 7.1 Conferindo
conferindo = pd.read_csv('pesq_claudio.csv')
display(conferindo) # Coluna unnamed existindo
# %% 7.2 Corrigindo
selecao.to_csv('pesq_claudio.csv', index=False)
conferindo = pd.read_csv('pesq_claudio.csv')
display(conferindo)

# %%
