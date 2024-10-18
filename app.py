import streamlit as st
import pandas as pd
import plotly.express as plt

st.set_page_config(page_title="Meu Primeiro App",
                   page_icon=":sparkles:",
                   menu_items={
                       'Get Help': 'https://ufpb.br/cdn',
                       'Report a bug': "https://forms.gle/mEhtstZUEsXiWGzg8",
                       'About': "# Meu Primeiro App. Experiência de desenvolvimento Web *low code*!" })
st.title("Meu Primeiro App")
with st.expander("Descrição da aplicação", False):
    st.markdown("""
    ## Dashboard de Vendas
    Os dados deste relatório são fictícios para fins de desenvolvimento inicial no `streamlit`.
    $Y_i = b_0 +b_1 X_{i1} + \delta_i$
                """)

# Dados de Vendas
df = pd.DataFrame({
    "Mês": ['Janeiro', 'Fevereiro', 'Março', 'Janeiro', 'Fevereiro', 'Março', 'Abril'],
    "Categoria": ["M", "M", "M", "E", "E", "E", "E"],
    "Vendas": [10,30,5,30,40,20,70]})

df["Categoria"] = df["Categoria"].map({'M': 'Móveis',
                                       'E': 'Eletrônicos'})

# Segmentações de dados
with st.sidebar:
    categoria = st.selectbox(label='Categoria', 
                             options=['Móveis','Eletrônicos'])
# Filtros
df_filtrado = df[df['Categoria']==categoria]

# Visualização de daddos
col1, col2 = st.columns(2)
with col1:
    st.metric('Faturamento total', f'R$ {df.Vendas.sum()} mil',
              help='Valores nominais das vendas brutas.')
    st.metric('Total de categorias', df.Categoria.nunique())
with col2:
    st.dataframe(df)

col1, col2 = st.columns(2)
with col1:
    st.bar_chart(df_filtrado, x='Mês', y='Vendas')
with col2:
    st.metric(f'Faturamento de {categoria}', 
            f'R$ {df_filtrado.Vendas.sum()} mil')
    st.dataframe(df_filtrado, hide_index=True)

fig = plt.bar(df_filtrado, x='Mês', y='Vendas')
st.plotly_chart(fig)