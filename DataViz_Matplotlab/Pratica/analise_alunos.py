#%%
import pandas as pd
#%% Inicio do Tratamento de dados alunos
df = pd.read_csv('https://raw.githubusercontent.com/profivan-ai/cdb-Python/refs/heads/main/arquivos/alunos_cursos.csv', sep=";") # df=DataFrame
#display(df)

# %% Verificando se existe dados nulos e tratando colunas
df.isnull().sum()
df_novo = df.drop('Projetos',axis=1)
# %% Gerando colunas Aprovado e Desempenho
df_novo["Aprovado"] = (df_novo["Nota"] >=7.5) & (df_novo["Presença"] >= 7.5)

def desempenho(nota):
    if nota >= 8:
        return 'alto'
    elif nota >=6:
        return 'medio'
    else:
        return 'baixo'
    
df_novo["Desempenho"] = (df_novo["Nota"].apply(desempenho))
df_novo

#%% 
media_notas = df_novo.groupby('Curso')['Nota'].mean().reset_index()
media_notas

# %%
aprov_curso = df_novo.groupby('Curso')['Aprovado'].sum().reset_index()
aprov_curso

# %% Importando Matplotlib
import matplotlib.pyplot as plt

# %% Gerando Grafico em Barra
df_novo['Curso'].value_counts().plot(
    kind='bar',
    color= 'purple',
    figsize=(8,5),
    title= "Numero de alunos por curso",
    xlabel="Curso",
    ylabel="Alunos",
    )
plt.tight_layout()
plt.show()

# %% Gerando Grafico em Pizza
df_novo['Desempenho'].value_counts().plot(
    kind='pie',
    figsize=(8,5),
    title = "Distribuição por Desempenho",
    ylabel = '',
    xlabel = '',
    autopct='%1.2f%%'    
    )
plt.tight_layout()
plt.show()

# %% Gerando Grafico em Linha
df_novo.groupby('Curso')['Nota'].plot(
    kind='line',
    legend=True,
    figsize=(8,5),
    title= "Frequencia das notas por curso",
    ylabel = 'Cursos',
    xlabel = 'Notas'
)
plt.tight_layout()
plt.show()
# %% Gerando Grafico em Linha por curso
curso = 'Excel'
df_novo[df_novo['Curso'] == curso].plot(
    kind='line',
    y='Nota',
    legend=True,
    figsize=(8,5),
    title= f"Frequencia das notas por curso de {curso}",
    ylabel = 'Cursos',
    xlabel = 'Notas'
)
plt.tight_layout()
plt.show()
# %% Gerando Mais informações - Medias por cursos (Barras)
import numpy as np
ax = media_notas.plot(
    kind='bar',
    x='Curso',
    figsize=(8,5),
    title= "Media de notas por curso",
    ylabel = 'Nota',
    xlabel = 'Curso',
    color= 'pink'
)
y_min = 0
y_max = 9
ax.grid(
    axis='y',              # Eixo y (linhas horizontais)
    alpha=0.6,             # Transparência
    linestyle='--',        # Linhas pontilhadas
    color='gray'           # Cor cinza
)
ax.set_yticks(np.arange(np.floor(y_min*2)/2, np.ceil(y_max*2)/2 + 0.25, 0.25))
plt.tight_layout()
plt.show()


#%% Medias por cursos (Barras)
media_notas.plot(
    kind= 'line',
    figsize= (8,5),
    title= ' Media de notas por curso',
    x = 'Curso',
    xlabel= 'Curso',
    ylabel='Nota',
    color = 'violet'
)
plt.tight_layout()
plt.show()

#%% Aprovados por curso
aprov_curso.plot(
    kind = 'pie',
    figsize=(8,5),
    labels=aprov_curso['Curso'],
    y='Aprovado',
    title='Distribuição de Aprovação',
    xlabel='',
    ylabel='',
    autopct= '%1.2f%%'
)
plt.tight_layout()
plt.show()
