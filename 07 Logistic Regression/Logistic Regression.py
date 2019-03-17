import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn import metrics

# using grid in Seaborn
sns.set_style('whitegrid')

data = pd.read_csv('advertising.csv')

print(data.head())
print(data.describe())
print(data.info())
print(data.columns.values)

# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
# ---------------------------------  DATA VISUALIZATION ---------------------------------
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------

# histogram
sns.distplot(a=data['Age'], kde=False, bins=30)

# jointplot
sns.jointplot(x='Age', y='Area Income', data=data)
sns.jointplot(x='Age', y='Daily Time Spent on Site', data=data, kind="kde")
sns.jointplot(x='Daily Time Spent on Site', y='Daily Internet Usage', data=data)

#pairplot
sns.pairplot(data=data, hue='Clicked on Ad')

# plt.show()

# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
# --------------------------------- LOGISTIC REGRESSION ---------------------------------
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------

numeric_data = data.select_dtypes(include=np.number)
X = numeric_data.drop(['Clicked on Ad'], axis=1)
y = data['Clicked on Ad']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

logistic = LogisticRegression()
logistic.fit(X_train, y_train)

predictions = logistic.predict(X_test)

print(classification_report(y_test, predictions))
