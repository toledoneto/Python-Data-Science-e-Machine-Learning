import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# data meaning
# * Avg. Session Length: Average session of in-store style advice sessions.
# * Time on App: Average time spent on App in minutes
# * Time on Website: Average time spent on Website in minutes
# * Length of Membership: How many years the customer has been a member.

# using grid in Seaborn
sns.set_style('whitegrid')

# carregado dados
customers = pd.read_csv("Ecommerce Customers")

# relevant information
# print(customers.head())
# print(customers.info())
# print(customers.describe())
# print(customers.columns.values)

# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
# ---------------------------------  DATA VISUALIZATION ---------------------------------
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------

# jointplot to compare the Time on Website and Yearly Amount Spent columns
# sns.jointplot(x='Time on Website', y='Yearly Amount Spent', data=customers)

# jointplot to compare the Time on App and Yearly Amount Spent columns
# sns.jointplot(x='Time on App', y='Yearly Amount Spent', data=customers)

# jointplot to create a 2D hex bin plot comparing Time on App and Length of Membership
# sns.jointplot(x='Time on App', y='Length of Membership', data=customers, kind="hex")

# pairplot of entire data
# sns.pairplot(data=customers)
# based in the pairplot, seems that 'Length of Membership' is the most currelated feature with 'Yearly Amount Spent'

# facetgrid
# sns.lmplot(data=customers, x='Length of Membership', y='Yearly Amount Spent')

# plt.show()

# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
# ---------------------------------- LINEAR REGRESSION ----------------------------------
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------

# collectiong only numeric fields
numeric_customers = customers.select_dtypes(include=np.number)
print(numeric_customers.head())

# data
X = numeric_customers.drop(['Yearly Amount Spent'], axis = 1)
# labels
y = customers['Yearly Amount Spent']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

linearRegression = LinearRegression()

linearRegression.fit(X_train, y_train)

print(linearRegression.coef_)

results = linearRegression.predict(X_test)

plt.figure()
plt.scatter(y_test, results)
plt.xlabel('Y Test')
plt.ylabel('Y Predicted')


print('MAE:', metrics.mean_absolute_error(y_test, results))
print('MSE:', metrics.mean_squared_error(y_test, results))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, results)))

# residuals
sns.distplot((y_test-results), bins=50)

coeffecients = pd.DataFrame(linearRegression.coef_, X.columns)
coeffecients.columns = ['Coeffecient']
print(coeffecients)

plt.show()
