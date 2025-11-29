# %% Importe
import sqlite3

#%% Conexão
conn = sqlite3.connect('banco.db')
cursor = conn.cursor()

# %% Create Table
query = "create table  inscricoes (nome TEXT NOT NULL, email TEXT NOT NULL, curso TEXT NOT NULL, idade INT)"
cursor.execute(query)

# %% Select
query_sel = "select * from inscricoes"
cursor.execute(query_sel)
for linha in cursor:
    print(linha)

# %% Insert
query_ins = "insert into inscricoes values('Eduardo', 'Email@email.com', 'Python', 26 )"
cursor.execute(query_ins)
conn.commit()

# %% Insert Lista

dados = [
    ('Eduardo', 'eduardo@email.com', 'Python', 26),
    ('Maria Silva', 'maria.silva@gmail.com', 'Java', 30),
    ('João Pedro', 'joao_souza@outlook.com', 'Excel', 22),
    ('Ana Clara', 'ana.dev@tech.com', 'Excel', 28),
    ('Pedro Henrique', 'pedro123@yahoo.com.br', 'Java#', 35),
    ('Lucas Ferreira', 'lucas_ferreira@uol.com.br', 'Java', 24),
    ('Carla Moraes', 'carla.moraes@empresa.net', 'React', 29),
    ('Felipe Gomes', 'felipe.gomes@email.com', 'Excel', 31),
    ('Beatriz Costa', 'bia.z@protonmail.com', 'UX Design', 25),
    ('Marcos Paulo', 'marcos_paulo@bol.com.br', 'Excel', 27),
    ('Juliana Lima', 'juli.ana@gmail.com', 'Python', 33),
    ('Roberto Dias', 'beto.dias@live.com', 'Excel Avançado', 40)
]

query_ins = "insert into inscricoes values (?,?,?,?)"
cursor.executemany(query_ins, dados)
conn.commit

# %% insert via arquivo.
arquivo = "arquivo.txt"
for linha in open(arquivo, 'r'):
    registro = linha.split(",")
    print(registro)
    query_ins = "insert into inscricoes values(?,?,?,?)"
    cursor.execute(query_ins, registro)
conn.commit()
# %% Exclusao
query_del = "delete from inscricoes"
cursor.execute(query_del)
conn.commit()

# %% Uptade
query_upd = "update inscricoes set idade = 99 where curso = 'Python'"
cursor.execute(query_upd)
conn.commit()

#%% Select + Recursos

query_sel = "select nome, email, curso from inscricoes where curso like '%Excel%' or idade >=30"
cursor.execute(query_sel)
for linha in cursor:
    print(linha)

#%% Select + dados
query_sel = "select * from inscricoes where curso like '%Excel%' or idade >=30"
cursor.execute(query_sel)
dados = cursor.fetchone()
for linha in dados:
    print(linha)
dados = cursor.fetchmany(3)
for linha in dados:
    print(linha)
    # fetchone um por vez
    # fetchmany traz o numero de resultados requisitados
    # fetchall traz todos

#%% Relatorio String Formatada

print("\nConsulta de Inscritos")
print("\nDados da Tabela Inscricoes")
print("-"*80)
#print("Nome\t\tEmail\t\tCurso\t\tIdade")
print("{:30}{:30}{:15}{:5}".format("Nome","Email","Curso","Idade"))
print("-"*80)
query_sel = "select * from inscricoes"
cursor.execute(query_sel)
dados = cursor.fetchall()      
for linha in dados:
    print("{:30}{:30}{:15}{:5}".format(linha[0],linha[1],linha[2],linha[3]))
print("="*80)
print("Foram encontrados {} registros".format(len(dados)))


#%% Manipulacao dos dados - DELETE
#query_del = "delete from inscricoes where idade >= 85"
query_del = "delete from inscricoes"
cursor.execute(query_del)
conn.commit()
#%% Manipulacao dos dados - Insert
arquivo = "arquivo.txt"

for linha in open(arquivo, 'r'):
    registro = linha.split(",")
    query_ins = "insert into inscricoes values(?,?,?,?)"
    cursor.execute(query_ins, registro)
conn.commit()

#%% Manipulacao dos dados - Select 
query_sel = "select curso, count(*) from inscricoes group by curso order by curso desc"
#query_sel = "select * from inscricoes"
cursor.execute(query_sel)
dados = cursor.fetchall()
for linha in dados:
    print(linha)

# %% Manipulacao dos dados - update
query_upd = "update inscricoes set idade = 55 where email = 'gabriel.oliveira@uol.com.br'"
cursor.execute(query_upd)
conn.commit()

#%% Modelagem e Joins - Integridade Relacional Create Table
query = "create table  cursos (id TEXT, nomecurso TEXT, instrutor TEXT)"
cursor.execute(query)

#%% Modelagem e Joins - Integridade Relacional Inserir dados Curso
dados = [
    ('1','Java', 'Denilson'),
    ('2','Python', 'Ivan'),
    ('3','Excel', 'Evan'),
    ('4','SQL', 'Fabio'),
    ('5','HTML', 'Renata')
]
query_ins = "insert into cursos values (?,?,?)"
cursor.executemany(query_ins, dados)
conn.commit()

#%% Modelagem e Joins - Integridade Relacional Select dados Curso
query_sel = "select * from cursos"
cursor.execute(query_sel)
dados = cursor.fetchall()
for linha in dados:
    print(linha)

#%% Modelagem e Joins - Integridade Relacional Alterar inscricoes com base na tabela curso
query_upd = "UPDATE inscricoes SET curso = ("
query_upd = query_upd + "SELECT id FROM cursos c WHERE c.nomecurso = inscricoes.curso) "
query_upd = query_upd + "WHERE EXISTS (SELECT 1 FROM cursos c WHERE c.nomecurso = inscricoes.curso)"
cursor.execute(query_upd)

#%% Modelagem e Joins - Select com Join
query_sel = "SELECT i.nome, i.email, i.idade, c.nomecurso, c.instrutor FROM inscricoes i JOIN cursos c ON c.id = i.curso"
cursor.execute(query_sel)
dados =cursor.fetchall()
for linha in dados:
    print(linha)

# %% Modelagem e Joins - Criar um dataframe
import pandas as pd
df_dados = pd.DataFrame(dados, columns=['nome', 'email', 'idade', 'curso', 'instrutor'])
df_dados

# %% Fechamento
conn.close()
