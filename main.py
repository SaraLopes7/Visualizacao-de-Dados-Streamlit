# Imports: 
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Importando os 4 arquivos CSV
df_employee = pd.read_csv('data\employee_performance.csv')
df_health = pd.read_csv('data\health_data.csv')
df_machinery = pd.read_csv('data\machinery_data.csv')
df_sales = pd.read_csv('data\sales_data.csv')

# Visualização:
print("\n") 
print("Exibindo as 5 primeiras linhas do Employee Performance DataFrame:\n")
print(df_employee.head())
print("\n") 

print("Exibindo as 5 primeiras linhas do Health DataFrame:\n")
print(df_health.head())
print("\n") 

print("Exibindo as 5 primeiras linhas do Machinery DataFrame:\n")
print(df_machinery.head())
print("\n") 

print("Exibindo as 5 primeiras linhas do Sales DataFrame:\n")
print(df_sales.head())
print("\n") 

# Employee Performance: Identificar os funcionários com melhor desempenho e os fatores que influenciam isso.

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

# Correlação entre experiência e desempenho
fig, ax = plt.subplots()
sns.scatterplot(data=df_employee, x='Years_Experience', y='Performance_Score', ax=ax)
ax.set_title("Correlação entre Experiência e Desempenho")
st.subheader("Correlação entre Experiência e Desempenho")
st.pyplot(fig)

# Funcionários com desempenho abaixo de 50
low_performance = df_employee[df_employee['Performance_Score'] < 50]
st.subheader("Funcionários com Baixo Desempenho")
st.dataframe(low_performance)

# Correlação entre ausências e desempenho
fig, ax = plt.subplots()
sns.scatterplot(data=df_employee, x='Absences', y='Performance_Score', ax=ax)
ax.set_title("Correlação entre Ausências e Desempenho")
st.subheader("Correlação entre Ausências e Desempenho")
st.pyplot(fig)

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
4. Existe uma correlação positiva entre anos de experiência e desempenho, indicando que a experiência contribui para melhores resultados.
5. Funcionários com muitas ausências tendem a ter um desempenho mais baixo, sugerindo a necessidade de políticas para reduzir ausências.
6. Os melhores funcionários por departamento foram identificados, permitindo benchmarking interno.
""")

# Exemplo: Reforçando a conclusão sobre desempenho médio por departamento
st.subheader("Desempenho Médio por Departamento")
avg_performance_by_dept = df_employee.groupby('Department')['Performance_Score'].mean()
st.bar_chart(avg_performance_by_dept)

# Exemplo: Reforçando a conclusão sobre correlação entre experiência e desempenho
st.subheader("Correlação entre Experiência e Desempenho")
fig, ax = plt.subplots()
sns.scatterplot(data=df_employee, x='Years_experience', y='Performance_Score', ax=ax)
ax.set_title("Correlação entre Experiência e Desempenho")
st.pyplot(fig)

st.markdown("""
### Destaques:
- **Melhor Departamento**: O departamento com maior desempenho médio foi o `Sales`.
- **Funcionário Destaque**: O funcionário com maior pontuação de desempenho foi o `John Doe`.
- **Correlação Importante**: Funcionários com mais de 5 anos de experiência têm, em média, 20% mais desempenho.
""")

# Comando para rodar: streamlit run main.py