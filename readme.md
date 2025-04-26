# Desafio - Individual: Criação de um Data Storytelling com Streamlit

## 1 - Acesse o seguinte conjunto de dados: [drive folder](https://drive.google.com/drive/folders/112HHSYO40aeP-RmLTo9uIevAZe22EUfy?usp=sharing);

## 2 - Analisem o conjunto de dados e definam objetivos de análise/visualizações!;

## 3 - A partir dele, implementem um storytelling simples que conte a história de valor que você deseja vender. Monte seu projeto no Colab ou VS Code com apoio do Streamlit e entregue via Teams o link da aplicação publicada;

## 4 - A narrativa deve ser concluída com possíveis soluções e insights para o objetivo de análise;

1. Gráfico de Barras (Desempenho dos Funcionários)
Visualize o desempenho médio dos funcionários por departamento.

import matplotlib.pyplot as plt

# Exemplo: Gráfico de barras para desempenho médio por departamento
avg_performance = df1.groupby('department')['performance_score'].mean()

st.subheader("Desempenho Médio por Departamento")
st.bar_chart(avg_performance)

2. Gráfico de Pizza (Saúde dos Funcionários)
Mostre a proporção de funcionários em diferentes categorias de saúde.

# Exemplo: Gráfico de pizza para categorias de saúde
health_counts = df2['health_category'].value_counts()

fig, ax = plt.subplots()
ax.pie(health_counts, labels=health_counts.index, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Garantir que o gráfico seja um círculo
st.subheader("Distribuição de Categorias de Saúde")
st.pyplot(fig)

3. Gráfico de Linha (Eficiência das Máquinas ao Longo do Tempo)
Analise a eficiência média das máquinas ao longo do tempo.

# Exemplo: Gráfico de linha para eficiência média ao longo do tempo
efficiency_over_time = df3.groupby('date')['efficiency'].mean()

st.subheader("Eficiência Média das Máquinas ao Longo do Tempo")
st.line_chart(efficiency_over_time)

4. Gráfico de Dispersão (Correlação entre Saúde e Desempenho)
Explore a relação entre a saúde dos funcionários e seu desempenho.

import seaborn as sns

# Exemplo: Gráfico de dispersão para saúde vs desempenho
fig, ax = plt.subplots()
sns.scatterplot(data=df2, x='health_score', y=df1['performance_score'], ax=ax)
ax.set_title("Correlação entre Saúde e Desempenho")
st.subheader("Correlação entre Saúde e Desempenho")
st.pyplot(fig)

5. Gráfico de Área (Tendências de Vendas)
Visualize as tendências de vendas ao longo do tempo.

# Exemplo: Gráfico de área para vendas ao longo do tempo
sales_over_time = df4.groupby('date')['sales'].sum()

st.subheader("Tendências de Vendas ao Longo do Tempo")
st.area_chart(sales_over_time)

Como Integrar no Streamlit
Adicione os códigos acima nas seções correspondentes do seu storytelling. Por exemplo:

# Seção 1: Desempenho dos Funcionários
st.header("1. Desempenho dos Funcionários")
st.write("Analisando o desempenho médio por departamento:")
avg_performance = df1.groupby('department')['performance_score'].mean()
st.bar_chart(avg_performance)