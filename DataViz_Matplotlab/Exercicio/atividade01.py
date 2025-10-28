# %%
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/profivan-ai/cdb-Python/refs/heads/main/arquivos/vendas_loja.csv')
ORDEM_MESES = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 
               'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
df['Mes'] = pd.Categorical(df['Mes'], categories=ORDEM_MESES, ordered=True)
# %%
df.drop("ID", axis=1,inplace=True) # Remove coluna ID
# %% Tratando valores nulos
media_vendas = df['Vendas'].mean()
media_vendas = round(media_vendas, 2)
df['Vendas'] = df['Vendas'].fillna(media_vendas) #Atribui media total para as vendas nao preenchidas
df['Regiao'] = df['Regiao'].fillna('Indefinida') #Define vendas indefinidas

#%%
import matplotlib.pyplot as plt

#%%
df.groupby('Categoria')[['Vendas']].sum().reset_index().plot(
    kind='bar',
    color='skyblue',
    legend=False,
    x='Categoria',
    figsize=(8,5),
    title= "Total de Vendas por Categoria",
    xlabel="Categoria",
    rot=0,                  # Define o escrito na horizontal
    edgecolor='black',      # Define a cor da borda
    linewidth=0.5,          # Define a espessura da borda
    ylabel="Vendas (R$)",
    )
plt.tight_layout()
plt.show()

#%%
df.groupby('Regiao')[['Vendas']].sum().reset_index().plot(
    kind='pie',
    legend=True,
    title='Distribuição de Vendas por Região',
    figsize=(8,5),
    y = 'Vendas',
    labels = df['Regiao'],
    ylabel = '',
    xlabel = '',
    autopct='%1.2f%%' 
)
plt.tight_layout()
plt.show()

# %%
vendas_mes = df.groupby('Mes')[['Vendas']].sum().reset_index()
ax = vendas_mes.plot(
    kind='line',
    figsize=(8,5),
    color='blue',
    x='Mes',
    title = 'Evolução de Vendas no Ano',
)
ax.grid(axis='both', linestyle='--', alpha=0.7)
ax.set_xticks(vendas_mes.index)  # Define as posições dos ticks para o número de meses
ax.set_xticklabels(vendas_mes['Mes']) # Define os rótulos para os nomes dos meses
ax.tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()
# %%
