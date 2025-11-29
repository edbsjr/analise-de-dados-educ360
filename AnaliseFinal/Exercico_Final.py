# %% Imports importantes
import sqlite3
import os
import pandas as pd

# %% Estabelecendo conexao com o banco
# --- 1. CONFIGURAÇÃO DO ARQUIVO ---
pasta_atual = os.path.dirname(os.path.abspath(__file__))
# Garante que o banco seja criado na pasta correta, independente de onde você roda o script
caminho_sql = os.path.join(pasta_atual, "script.sql")
caminho_db = os.path.join(pasta_atual, "banco.db")

try:
    with open(caminho_sql, 'r', encoding='utf-8') as arquivo:
        sql_lido = arquivo.read() # Lê todo o texto do arquivo para uma variável
        print(f"📖 Arquivo SQL lido com sucesso: {caminho_sql}")

    # --- 3. EXECUÇÃO NO BANCO ---
    with sqlite3.connect(caminho_db) as conn:
        cursor = conn.cursor()
        cursor.executescript(sql_lido) # Executa o texto que lemos do arquivo
        print(f"✅ Banco de dados '{caminho_db}' atualizado com sucesso!")

except FileNotFoundError:
    print("❌ Erro: O arquivo 'script_banco.sql' não foi encontrado na mesma pasta.")
except sqlite3.Error as e:
    print(f"❌ Erro de SQL ao executar o script: {e}")

### ETAPA 1 - OBSERVANDO DADOS - PRODUTOS
#%% Tipo de dados
cursor.execute("PRAGMA table_info(produtos)")
colunas = cursor.fetchall()

print(f"{'ID':<5} | {'Nome da Coluna':<20} | {'Tipo':<10}")
print("-" * 40)

for col in colunas:
    print(f"{col[0]:<5} | {col[1]:<20} | {col[2]:<10}")

# %% Analisando Dados
query_sel = "select * from produtos"
cursor.execute(query_sel)
print(f"{'ID':<3} | {'Nome Produto':<20} | {'Categoria':<15} | {'Preco':<8}")
print("-" * 60)
for linha in cursor:
    print(f"{str(linha[0]):<3} | {str(linha[1]):<20} | {str(linha[2]):<15} | {str(linha[3]):<8}")

# %% Verificando nulos
# 1. Descobre os nomes das colunas dinamicamente
cursor.execute("PRAGMA table_info(produtos)")
# O resultado vem como tuplas, o nome é o índice 1
lista_colunas = [linha[1] for linha in cursor.fetchall()]

print(f"{'Coluna':<20} | {'Qtd Nulos':<10}")
print("-" * 35)

# 2. Loop para verificar cada coluna automaticamente
for coluna in lista_colunas:
    # Monta a query dinamicamente (f-string)
    # CUIDADO: Só faça isso com nomes de colunas que VOCÊ controla, para evitar SQL Injection
    query = f"SELECT COUNT(*) FROM produtos WHERE {coluna} IS NULL"
    
    cursor.execute(query)
    qtd_nulos = cursor.fetchone()[0] # Pega o número retornado
    
    # Só imprime se tiver nulos (ou imprime todos se preferir)
    if qtd_nulos > 0:
        print(f"{coluna:<20} | {qtd_nulos:<10} ⚠️")
    else:
        print(f"{coluna:<20} | {qtd_nulos:<10}")


### ETAPA 1 - OBSERVANDO DADOS - VENDAS
#%% Tipo de dados
cursor.execute("PRAGMA table_info(vendas)")
colunas = cursor.fetchall()

print(f"{'ID':<5} | {'Nome da Coluna':<20} | {'Tipo':<10}")
print("-" * 40)

for col in colunas:
    print(f"{col[0]:<5} | {col[1]:<20} | {col[2]:<10}")

# %% Analisando Dados
query_sel = "select * from vendas"
cursor.execute(query_sel)
print(f"{'ID':<3} |{'ID Prod':<6} | {'Quant':<5} | {'Data Venda':<8} | {'Desconto':<8}")
print("-" * 60)
for linha in cursor:
    print(f"{str(linha[0]):<3} | {str(linha[1]):<6} | {str(linha[2]):<5} | {str(linha[3]):<8} | {str(linha[4]):<8}")
# %% Verificando nulos
# 1. Descobre os nomes das colunas dinamicamente
cursor.execute("PRAGMA table_info(vendas)")
# O resultado vem como tuplas, o nome é o índice 1
lista_colunas = [linha[1] for linha in cursor.fetchall()]

print(f"{'Coluna':<20} | {'Qtd Nulos':<10}")
print("-" * 35)

# 2. Loop para verificar cada coluna automaticamente
for coluna in lista_colunas:
    # Monta a query dinamicamente (f-string)
    # CUIDADO: Só faça isso com nomes de colunas que VOCÊ controla, para evitar SQL Injection
    query = f"SELECT COUNT(*) FROM vendas WHERE {coluna} IS NULL"
    
    cursor.execute(query)
    qtd_nulos = cursor.fetchone()[0] # Pega o número retornado
    
    # Só imprime se tiver nulos (ou imprime todos se preferir)
    if qtd_nulos > 0:
        print(f"{coluna:<20} | {qtd_nulos:<10} ⚠️")
    else:
        print(f"{coluna:<20} | {qtd_nulos:<10}")


### ETAPA 2 - UNINDO TABELAS
#%% JOIN
query_join ="""
SELECT 
    v.data_venda, 
    p.nome_produto, 
    p.categoria,
    v.quantidade, 
    p.preco_unitario, 
    v.desconto,
    (v.quantidade * (IFNULL(p.preco_unitario, 0) - IFNULL(v.desconto, 0))) AS total_venda
FROM vendas v 
LEFT JOIN produtos p ON v.id_produto = p.id_produto
"""
# Executando e imprimindo para testar
cursor.execute(query_join)
dados = cursor.fetchall()

### ETAPA 3 — Importação no Python
# %% Transformando em DATAFRAME com PANDAS
df_dados = pd.DataFrame(dados, columns=['data','produto','categoria','quantidade','preco_unitario','desconto','total'])

### ETAPA 4 - Valores Nulos
# %% Tratando valores nulos
df_dados.isnull().sum()
#%%

colunas_numericas = ['quantidade', 'preco_unitario', 'desconto', 'total']
for col in colunas_numericas:
    df_dados[col] = pd.to_numeric(df_dados[col], errors='coerce')
    
df_dados = df_dados.dropna(subset=['preco_unitario']) # Desconsiderando produto sem Preco Unitario

df_dados['desconto'] = df_dados['desconto'].fillna(0.0) # Descontos NULOS tratados como 0

df_dados['quantidade'] = df_dados['quantidade'].fillna(1.0) # Quantidade NULO tratado com 1

df_dados['categoria'] = df_dados['categoria'].fillna("Indefinido") # Categorias NULO como Indefinido

calculo_completo = (df_dados['quantidade'].fillna(0) * df_dados['preco_unitario']) - df_dados['desconto'].fillna(0)
df_dados['total'] = df_dados['total'].fillna(calculo_completo) # Tratando Total NULO

print(df_dados.isnull().sum())

###ETAPA 5 - Analise dos dados
#%% - Adicionando nova coluna
df_dados['perc_desconto'] = (df_dados['desconto'] / df_dados['total']) * 100
df_dados['perc_desconto'] = df_dados['perc_desconto'].fillna(0) # Segurança
df_dados['tem_desconto'] = df_dados['desconto'].apply(lambda x: 'Com Desconto' if x > 0 else 'Preço Cheio')


#%% 
faturamento_total = df_dados['total'].sum() #Total de Vendas realizadas
quantidade_total = df_dados['quantidade'].sum() # Quantidade de itens vendidos
media_vendas = df_dados['total'].mean() # Ticket medio de venda
ticket_medio = faturamento_total / quantidade_total # Preço Medio item
print(f"Faturamento Total: R$ {faturamento_total:.2f}")
print(f"Ticket Médio: R$ {ticket_medio:.2f}")
print(f"Preço Médio por Item: R$ {preco_medio_item:.2f}")
#%%
#Faturamento Total por Categoria
faturamento_categoria = df_dados.groupby('categoria')['total'].sum().sort_values(ascending=False).reset_index()
#Faturamento Medio por Categoria
faturamento_medio_categoria = df_dados.groupby('categoria')['total'].mean().sort_values(ascending=False).reset_index()
#Volume por dia
volume_dia = df_dados.groupby('data')['total'].sum().sort_values(ascending=False).reset_index()

# %% ETAPA 6 — Visualizações
import plotly.express as px

#%% 1 - Grafico 
#px.bar(faturamento_categoria, x='categoria', y='total', title='Faturamento Total por Categoria', text='total', color='categoria')
#px.pie(faturamento_medio_categoria, values= 'total', names='categoria', title='Distribuicao de Vendas por Categoria', color='categoria')
px.pie(faturamento_categoria, 
       values= 'total', 
       names='categoria', 
       title='Distribuicao de Vendas por Categoria', 
       color='categoria')

#%% 2- Grafico
px.bar(
    volume_dia, 
    x='data', 
    y='total', 
    color='total', 
    title="Vendas Diárias")

#%% - Grafico Bonus
px.scatter(
    df_dados, 
    x='perc_desconto', 
    y='total', 
    color='categoria',
    size='quantidade', # Bolinha maior se vendeu mais itens
    title='Impacto do Desconto no Valor Total da Venda',
    hover_data=['produto'],
    labels={'perc_desconto': '% de Desconto Concedido', 'total': 'Faturamento Real'}
)

#%% ETAPA 7 - Conclusao
cursor.close()
# %%
# A análise de desempenho destaca a liderança absoluta da categoria Informática, 
# que atingiu R$ 22.020 em vendas, criando uma margem expressiva sobre a segunda
#  colocada Telefonica (R$ 8.200). No entanto, a granularidade desta análise foi 
# parcialmente comprometida pela presença de uma Categoria Indefinida na terceira 
# posição (R$6050), evidenciando a necessidade de melhorias na coleta de dados.
# O negócio registrou um ticket médio de R$ 658,36, mas chama a atenção o fato de 
# que itens com menores percentuais de desconto mantiveram altos volumes de saída.
#  Isso sugere uma baixa sensibilidade ao preço promocional, indicando que a 
# estratégia de descontos teve impacto irrelevante no impulsionamento das vendas.