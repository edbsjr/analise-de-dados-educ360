import pandas as pd
import plotly.express as px
import streamlit as st

#Exercicio proposto.
#Realizar melhorias no codigo.
#Adicionar outro grafico Mostrando o Faturamento por unidade
#Alterar a Consulta por Especialidade para grafico de pizza
#Adicionar Contador de Totais de Consultas, unidades ativas e faturamento no campo superior

# layout
st.set_page_config(page_title="Painel de Consulta Medicas", layout="wide")
st.title("📊Painel de Consultas Medicas")
# st.write("Esta é a primeira linha do meu dashboard.")

#Função para carregar dados
@st.cache_data #Mantem o carregamento em cache, melhora a performace
def carregar_dados():
    try:
        dados = pd.read_csv("Dataviz_StreamLit/Pratica/consultas.csv", parse_dates=["dataconsulta"])
        return dados
    except FileNotFoundError:
        st.error("❌ Erro: O arquivo 'consultas.csv' não foi encontrado. Verifique o caminho.")
        st.stop() # Interrompe o script aqui para não dar outros erros")
    except Exception as e:
        st.error(f"❌ Erro inesperado ao ler o arquivo: {e}")
        st.stop()

df = carregar_dados()

# FILTROS (SIDEBARS)
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
upcol1, upcol2, upcol3 = st.columns(3)
col1, col2, col3 = st.columns(3)


def criar_card(titulo, valor, prefixo=""):
    return f"""
    <div style="text-align: center;
                border: 1px solid #CCC; 
                border-radius: 10px;
                box-shadow: 0px 0px 5px Aquamarine; 
                padding: 10px; 
                color: Aquamarine;">
        <h5 style="color: gray; margin: 0;">{titulo}</h5>
        <h2>{prefixo} {valor}</h2>
    </div>
    """

# Box Superior 1 - Total de Consultas (Com HTML para centralizar)
total_consultas = df_filtrado.shape[0]
upcol1.markdown(criar_card("Total de Consultas", total_consultas), unsafe_allow_html=True)

# Box Superior 2 - Unidades ativas
unidades_ativas = df_filtrado['unidade'].unique().shape[0]
upcol2.markdown(criar_card("Unidades Ativas", unidades_ativas), unsafe_allow_html=True)

#Box Superior 3 - Total de Faturamento
soma_vendas = df_filtrado['valor'].sum()
valor_arredondado = round(soma_vendas, 2)
faturamento_total = f"R$ {valor_arredondado:,.2f}"
upcol3.markdown(criar_card("Faturamento Total", faturamento_total,prefixo="R$"), unsafe_allow_html=True)

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
        color_discrete_sequence= px.colors.qualitative.Bold,
        title= f"📈Total de consultas medicas por unidades :{opcao_unidade} - (Data:{opcao_data}) "
)
graf1.update_layout(xaxis_title="Unidade", yaxis_title="Total de Consultas")
col1.plotly_chart(graf1, width='stretch')

# Grafico 2 - Consultas por Unidade x Mostrar as Especialidades - Barras
consulta_tipo = df_filtrado.groupby("tipoconsulta").size().reset_index(name='Total')
graf2 = px.pie(
        consulta_tipo,
        values='Total',
        names='tipoconsulta',
        title="🩺Consultas por Especialidade", 
        color_discrete_sequence= px.colors.qualitative.Safe,
        opacity= 0.9
)
col2.plotly_chart(graf2, width="stretch")


# Grafico 3 - Total de Faturamento por unidade
consulta_faturamento = df_filtrado.groupby('unidade').sum('valor').reset_index()
graf3 = px.bar(
        consulta_faturamento,
        x= 'unidade',
        y= 'valor',
        hover_name= 'valor',
        #barmode='group',
        color= 'unidade',
        text= 'valor',
        color_discrete_sequence= px.colors.qualitative.T10,
        title= f"🧾Faturamento Total por Unidade : {opcao_unidade} - (Data: {opcao_data}) "
)
graf3.update_layout(xaxis_title="Unidade", yaxis_title="Faturamento")
graf3.update_traces(texttemplate='R$ %{text:.2s}', textposition='outside')
col3.plotly_chart(graf3, width='stretch')

# Visao dos atendimentos

st.subheader(f"📄Registros : {opcao_unidade}")
st.dataframe(df_filtrado, width= 'stretch')
