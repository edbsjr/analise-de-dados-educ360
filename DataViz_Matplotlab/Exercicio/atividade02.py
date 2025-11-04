#%%
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/profivan-ai/cdb-Python/refs/heads/main/arquivos/pacientes.csv')
df.drop('ID', axis=1, inplace=True)
ORDEM_MESES = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 
               'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
df['Mes'] = pd.Categorical(df['Mes'], categories=ORDEM_MESES, ordered=True)

# %%
def faixa_etaria(idade):
    if idade > 61:
        return '+61'
    elif idade >= 51:
        return '51-60'
    elif idade >= 41:
        return '41-50'
    elif idade >= 31:
        return '31-40'
    else:
        return 'Até 30'
df['Faixa'] = (df['Idade'].apply(faixa_etaria))
df.drop('Idade', axis=1, inplace=True)
ORDEM_FAIXA = ['Até 30', '31-40','41-50','51-60','+61']
df['Faixa'] = pd.Categorical(df['Faixa'], categories=ORDEM_FAIXA, ordered=True)

#%%Tratando nulos
df.isnull().sum()
media_glicose = df['Glicose'].mean()
media_glicose = round(media_glicose, 1)
media_pressao = df['Pressao'].mean()
media_pressao = round(media_pressao, 1)

df['Glicose'] = df['Glicose'].fillna(media_glicose)
df['Pressao'] = df['Pressao'].fillna(media_pressao)

# %% Importando Matplotlib
import matplotlib.pyplot as plt

# %%
df.groupby('Faixa')['Glicose'].mean().reset_index().plot(
    kind = 'bar',
    figsize = (8,5),
    legend = False,
    color = 'green',
    title = 'Media de Glicose por Faixa Etaria',
    xlabel = 'Faixa Etaria',
    ylabel = 'Nivel de Glicose',
    x = 'Faixa',
    rot = 0
)
plt.tight_layout()
plt.show()
# %%
df['Genero'].value_counts().plot(
    kind = 'pie',
    figsize=(8,5),
    title= 'Distribuição dos Pacientes por Gênero',
    ylabel= '',
    autopct='%1.1f%%'  
)
plt.tight_layout()
plt.show()

# %%
pressao_mes = df.groupby('Mes')['Pressao'].mean().reset_index()
ax = pressao_mes.plot(
    kind = 'line',
    figsize =(8,5),
    title = 'Evolução da Média da Pressão Arterial por Mes',
    legend=False,
    marker = 'o',
    rot= 45
)

ax.grid(axis='both', linestyle='--', alpha=0.7)
ax.set_xticks(pressao_mes.index)  # Define as posições dos ticks para o número de meses
ax.set_xticklabels(pressao_mes['Mes']) # Define os rótulos para os nomes dos meses
plt.tight_layout()
plt.show()
