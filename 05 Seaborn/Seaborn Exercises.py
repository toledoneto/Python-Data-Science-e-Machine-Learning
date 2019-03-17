import seaborn as sns
import matplotlib.pyplot as plt

# criando um grid para podermos olhar melhor os gráficos do sns
sns.set_style('whitegrid')

titanic = sns.load_dataset('titanic')

print(titanic.head())
print(titanic.info())

# jointplot nos trás a relação entre duas variáveis juntamente com o histograma de cada uma delas
# nesse caso, veremos um grande concentração na faixa etária entre ~15 a 55 anos,
# e uma concentração de pessoas que pagaram a menor taxa
sns.jointplot(titanic['fare'], titanic['age'])
plt.show()

# distplot nos ajuda ver a distribução de apenas uma variável
# * bins: número de divisões
# * kde: curvatura sobre as divisões
sns.distplot(titanic['fare'], bins=30, kde=False, color='red')
plt.show()

# boxplot ns dá a concentração por 'quartis', ou seja, por 25% da amostra. Fora, temos os outliers
sns.boxplot(x='class', y='age', data=titanic, palette='rainbow')
plt.show()

# violin plot e swarmplot
sns.violinplot(x='class', y='age', data=titanic)
plt.show()
sns.swarmplot(x='class', y='age', data=titanic)
plt.show()

# countplot
sns.countplot(x='sex', data=titanic)
plt.show()

# heatmap
sns.heatmap(titanic.corr(), cmap='coolwarm')
plt.title('titanic.corr()')
plt.show()

# facegrid
g = sns.FacetGrid(data=titanic, col='sex')
g.map(plt.hist, 'age')
plt.show()
