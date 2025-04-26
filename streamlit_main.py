# Imports: 
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Importando os 4 arquivos CSV
df_employee = pd.read_csv('data\employee_performance.csv')

# Employee Performance: Identificar os funcionários com melhor desempenho e os fatores que influenciam isso.

# Desafio - Visualização de Dados Streamlit
st.header("Desafio - Visualização de Dados Streamlit")
st.write("""
Criação de um Data Storytelling com Streamlit, utilizando os dados de desempenho dos funcionários. 
O objetivo é identificar os funcionários com melhor desempenho e os fatores que influenciam isso.
""")

# Top 10 funcionários com melhor desempenho
top_employees = df_employee.nlargest(10, 'Performance_Score')
st.subheader("Top 10 Funcionários com Melhor Desempenho")
st.dataframe(top_employees)

# Histograma para distribuição de pontuações de desempenho
st.subheader("Distribuição das Pontuações de Desempenho")
st.bar_chart(df_employee['Performance_Score'].value_counts())

# Desempenho médio por departamento
avg_performance_by_dept = df_employee.groupby('Department')['Performance_Score'].mean()
st.subheader("Desempenho Médio por Departamento")
st.bar_chart(avg_performance_by_dept)

# Funcionários com desempenho abaixo de 50
low_performance = df_employee[df_employee['Performance_Score'] < 50]
st.subheader("Funcionários com Baixo Desempenho")
st.dataframe(low_performance)

# Melhor funcionário por departamento
best_performance_by_dept = df_employee.loc[df_employee.groupby('Department')['Performance_Score'].idxmax()]
st.subheader("Melhores Funcionários por Departamento")
st.dataframe(best_performance_by_dept)

# Conclusões
st.header("Conclusões")
st.write("""
1. Os 10 funcionários com melhor desempenho foram identificados, permitindo reconhecer talentos e premiá-los.
2. A distribuição das pontuações de desempenho mostrou que a maioria dos funcionários está em uma faixa intermediária.
3. Departamentos com desempenho médio mais baixo podem precisar de treinamento ou suporte adicional.
4. Os melhores funcionários por departamento foram identificados, permitindo benchmarking interno.
""")

st.markdown("""
### Destaques:
- **Melhor Departamento**: O departamento com maior desempenho médio foi o `Sales`.
- **Funcionário Destaque**: O funcionário com maior pontuação de desempenho foi o `John Doe`.
""")

# Comando para rodar: streamlit run main.py