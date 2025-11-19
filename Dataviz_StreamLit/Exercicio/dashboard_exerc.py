import pandas as pd
import plotly.express as px
import streamlit as st

# Demandas do cliente
# 1- Numero de consultas Geral e por Data (SelectBox)- Barra 
# 2- Por unidade as consultas - Dados - Especialidades

# layout
st.set_page_config(page_title="Painel de Consulta Medicas", layout="wide")
st.title("Painel de Consultas Medicas")
# st.write("Esta é a primeira linha do meu dashboard.")

# CSV
df = pd.read_csv("Dataviz_StreamLit/Pratica/consultas.csv", parse_dates=["dataconsulta"])
#df.info()

# Combo de datas
datas_unicas = sorted(df['dataconsulta'].dt.strftime("%d-%m-%Y").unique())
opcao_data = st.sidebar.selectbox("Selecione uma data", options=["Todas"]+ datas_unicas)

# Combo de Unidade
unidades = sorted(df['unidade'].unique())
opcao_unidade = st.sidebar.selectbox("Selecione a unidade", options=["Todas"]+ unidades)

# Aplicar filtros

df_filtrado = df.copy()

if opcao_data != "Todas":
    df_filtrado = df_filtrado[df_filtrado['dataconsulta'].dt.strftime("%d-%m-%Y") == opcao_data]

if opcao_unidade != "Todas":
    df_filtrado = df_filtrado[df_filtrado['unidade'] == opcao_unidade]

# Composição Graficos e tela
col1, col2 = st.columns(2)

# Grafico 1 - Consultas por Unidades - Barras

consulta_unidades = df_filtrado.groupby('unidade').size().reset_index(name='Total')

graf1 = px.bar(
        consulta_unidades,
        x= 'unidade',
        y= 'Total',
        hover_name= 'Total',
        #barmode='group',
        color= 'unidade',
        text= 'Total',
        title= f"Total de consultas medicas por unidades :{opcao_unidade} - (Data:{opcao_data}) "

)
graf1.update_layout(xaxis_title="Unidade", yaxis_title="Total de Consultas")
col1.plotly_chart(graf1, width='stretch')

# Grafico 2 - Consultas por Unidade x Mostrar as Especialidades - Barras

consulta_tipo = df_filtrado.groupby("tipoconsulta").size().reset_index(name='Total')
graf2 = px.bar(
        consulta_tipo,
        x ='Total',
        y='tipoconsulta',
        color='tipoconsulta',
        title="Consultas por Especialidade",
        text= 'Total'
)

graf2.update_layout(xaxis_title="Total de Consultas", yaxis_title="Tipo da Consulta")
col2.plotly_chart(graf2, width="stretch")

# Visao dos atendimentos

st.subheader(f"Registros : {opcao_unidade}")
st.dataframe(df_filtrado, width= 'stretch')