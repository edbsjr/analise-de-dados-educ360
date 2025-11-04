#%%
import seaborn as sns
import matplotlib.pyplot as plt
#%%
dados = sns.load_dataset("tips")
dados
#%%
#dados.describe(include="all")
dados.info()

#%% Grafico de Disperção
sns.scatterplot(x="total_bill", y="tip", data= dados)
plt.title("Relação entre Total da Conta e Gorjeta")
plt.show()
# %%
sns.regplot(x="total_bill", y="tip", data=dados)
plt.title("Relação entre Total da Conta e Gorjeta")
plt.show()

#%%
sns.barplot(x="day", y="tip",data=dados, estimator="sum", palette= "pastel")
plt.title("Gorjeta por dia da Semana")
plt.show()

#%% Bloxplot
sns.boxenplot(x="day", y="total_bill", data=dados)
plt.title("Distribuição de valor das contas por dia")
plt.show()

#%% Histograma

sns.histplot(data=dados, x="total_bill", bins=10, kde=True, color="orange")
plt.title("Histograma das Contas")
plt.show()

#%% Violino
sns.violinplot(x = "day", y="tip", data=dados)
plt.title("Distribuição das Gorjetas por dia")
plt.show()

# %% linhas
op ="Male"
dados2 = dados.sex == op
sns.lineplot(x="total_bill", y="tip", data=dados[dados2], marker= "o")
plt.title(f"Relação entre Total da Conta e Gorjeta - Sexo {op}")
plt.show()

# %% linhas
sns.lineplot(x="total_bill", y="tip", data=dados, marker= "o", hue="sex")
plt.title("Relação entre Total da Conta e Gorjeta")
plt.show()

#%%
import pandas as pd

#%%
df = pd.read_csv("https://raw.githubusercontent.com/profivan-ai/cdb-Python/refs/heads/main/arquivos/alunos_cursos.csv", sep=";")
df.info()
#%%
sns.countplot(x="Curso", data=df)
plt.title("Total de Alunos por Curso")
plt.show()
# %%
var_curso = "Python"
var_curso2 = "Excel"

df_curso = (df.Curso == var_curso) | (df.Curso == var_curso2)
sns.lineplot(x="Nota", y="Aluno",data=df[df_curso], marker = "o", hue="Curso")
plt.title(f"Media de Nota por Curso - {var_curso} - {var_curso2}")
plt.grid(True)
plt.show()