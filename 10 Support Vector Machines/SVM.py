# For this series of lectures, we will be using the famous Iris flower data set.
#
# The Iris flower data set or Fisher's Iris data set is a multivariate data set introduced by
# Sir Ronald Fisher in the 1936 as an example of discriminant analysis.
#
# The data set consists of 50 samples from each of three species of Iris
# (Iris setosa, Iris virginica and Iris versicolor), so 150 total samples.
# Four features were measured from each sample: the length and the width of the sepals and petals, in centimeters.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier

# using grid in Seaborn
sns.set_style('whitegrid')

iris = sns.load_dataset('iris')

print(iris.head())
print(iris.info())
print(iris.columns.values)

# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
# ---------------------------------  DATA VISUALIZATION ---------------------------------
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------

# sns.pairplot(data=iris, hue='species')

setosa = iris[iris['species'] == 'setosa']
sns.kdeplot(setosa['sepal_width'], setosa['sepal_length'], cmap="plasma", shade=True, shade_lowest=False)
# plt.show()

# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
# ----------------------------------------- SVM -----------------------------------------
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------

X = iris.drop('species', axis=1)
y = iris['species']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)

svm = SVC()

svm.fit(X_train, y_train)

predictions = svm.predict(X_test)

print(classification_report(y_test, predictions))
print(confusion_matrix(y_test, predictions))

# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
# ------------------------------------- Grid Search -------------------------------------
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------

param_grid = {'C': [0.1,1, 10, 100], 'gamma': [1,0.1,0.01,0.001]}

grid = GridSearchCV(SVC(), param_grid, refit=True, verbose=2)
grid.fit(X_train, y_train)

grid_predictions = grid.predict(X_test)

print(confusion_matrix(y_test, grid_predictions))

print(classification_report(y_test, grid_predictions))
