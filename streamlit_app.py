import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar os dados
df = pd.read_csv("data/employee_performance.csv")

# Título do Dashboard
st.title('Data Storytelling - Análise Interativa')

# Explicação inicial
st.markdown("""
## Análise do Desempenho e Salários dos Funcionários
Dashboard feito para explorar a relação entre o desempenho dos funcionários, horas de treinamento, departamentos e salários.
""")


# Filtro de Performance (Slider)
st.subheader('Filtrar Dados por Performance')
min_performance = int(df['Performance_Score'].min())
max_performance = int(df['Performance_Score'].max())

performance_filter = st.slider(
    'Selecione a faixa de Performance Score', 
    min_performance, max_performance, 
    (min_performance, max_performance),
    key="performance_slider"  # Chave única para o slider de Performance
)

# Filtrar os dados com base no Performance Score
df_filtered = df[(df['Performance_Score'] >= performance_filter[0]) & (df['Performance_Score'] <= performance_filter[1])]

# Exibir o número de registros filtrados
st.write(f'Dados filtrados: {df_filtered.shape[0]} registros')

# Criar o gráfico de distribuição de Performance com Matplotlib
fig, ax = plt.subplots()
sns.histplot(df_filtered['Performance_Score'], kde=True, ax=ax)
st.pyplot(fig)

# Filtro de Departamento (SelectBox)
department = st.selectbox('Selecione um Departamento', df['Department'].unique(), key="department_selectbox")

# Filtrar os dados pelo Departamento selecionado
df_department = df[df['Department'] == department]

# Exibir o salário médio no departamento selecionado
salario_medio = df_department['Salary'].mean()
st.subheader(f'Salário Médio no Departamento: {department}')
st.write(f'Salário médio: R${salario_medio:.2f}')

# Criar o gráfico de Boxplot de Salário por Departamento com Matplotlib
fig, ax = plt.subplots()
sns.boxplot(x=df_department['Salary'], ax=ax)
st.pyplot(fig)

# Exibindo a correlação entre Treinamento e Desempenho
correlation = df['Training_Hours'].corr(df['Performance_Score'])
st.subheader('Correlação entre Treinamento e Desempenho')
st.write(f'A correlação entre as horas de treinamento e o desempenho é de {correlation:.2f}.')

# Criar o gráfico de Dispersão entre Treinamento e Desempenho com Matplotlib
fig, ax = plt.subplots()
sns.scatterplot(x='Training_Hours', y='Performance_Score', data=df, ax=ax)
st.pyplot(fig)

# Opção para escolher o tipo de gráfico (Histograma ou Boxplot)
grafico_tipo = st.radio(
    'Escolha o tipo de gráfico para Distribuição de Performance',
    ('Histograma', 'Boxplot'),
    key="grafico_tipo_radio"  # Chave única para o radio button
)

if grafico_tipo == 'Histograma':
    st.subheader('Distribuição do Desempenho (Histograma)')
    fig, ax = plt.subplots()
    sns.histplot(df_filtered['Performance_Score'], kde=True, ax=ax)
    st.pyplot(fig)
elif grafico_tipo == 'Boxplot':
    st.subheader('Distribuição do Desempenho (Boxplot)')
    fig, ax = plt.subplots()
    sns.boxplot(x=df_filtered['Performance_Score'], ax=ax)
    st.pyplot(fig)

# Filtro combinado (Departamento + Performance)
st.subheader('Filtro Combinado: Departamento e Performance')
department_filter = st.selectbox('Selecione um Departamento para Análise', df['Department'].unique(), key="department_combined_selectbox")
performance_filter_combined = st.slider(
    'Selecione a faixa de Performance Score', 
    min_performance, max_performance, 
    (min_performance, max_performance),
    key="performance_combined_slider"  # Chave única para o slider combinado
)

# Filtrando os dados combinados
df_combined = df[(df['Department'] == department_filter) & 
                 (df['Performance_Score'] >= performance_filter_combined[0]) & 
                 (df['Performance_Score'] <= performance_filter_combined[1])]

# Exibir o gráfico combinado de Boxplot por Departamento
st.write(f'Dados filtrados para o Departamento: {department_filter} com Performance Score entre {performance_filter_combined[0]} e {performance_filter_combined[1]}')
fig, ax = plt.subplots()
sns.boxplot(x='Department', y='Salary', data=df_combined, ax=ax)
st.pyplot(fig)

# Exibindo informações adicionais
average_salary = df['Salary'].mean()
st.subheader('Média de Salário')
st.write(f'O salário médio de todos os funcionários é R${average_salary:.2f}')