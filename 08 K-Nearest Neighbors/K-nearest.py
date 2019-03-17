import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn import metrics

# using grid in Seaborn
sns.set_style('whitegrid')

data = pd.read_csv('KNN_Project_Data')

print(data.head())
print(data.columns.values)

# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
# ---------------------------------  DATA VISUALIZATION ---------------------------------
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------

# sns.pairplot(data, hue='TARGET CLASS')

# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
# --------------------------------- DATA PRE PROCESSING ---------------------------------
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------

# StandardScaler from Scikit learn to standardize for a common scale
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
# standardizing without the target values
scaler.fit(data.drop('TARGET CLASS', axis=1))

# obtaining the scaled features
scaled_features = scaler.transform(data.drop('TARGET CLASS', axis=1))

# creating a new DF with the scaled features and without the target class
scaled_data = pd.DataFrame(scaled_features, columns=data.columns[:-1])
print(scaled_data.head())

# plt.show()

# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
# ----------------------------------------- KNN -----------------------------------------
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------

y = data['TARGET CLASS']

X_train, X_test, y_train, y_test = train_test_split(scaled_data, y, test_size=0.3)

k = 1
knn = KNeighborsClassifier(n_neighbors=k)

knn.fit(X_train, y_train)
predictions = knn.predict(X_test)

print(classification_report(y_test, predictions))

# choosing the best 'k' with de elbow method
error_rate = []

for i in range(1, 40):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, y_train)
    pred_i = knn.predict(X_test)
    error_rate.append(np.mean(pred_i != y_test)) # avg error rate

# plotting the elbow
plt.figure(figsize=(10,6))
plt.plot(range(1, 40), error_rate, color='blue', linestyle='dashed', marker='o',
         markerfacecolor='red', markersize=10)
plt.title('Error Rate vs. K Value')
plt.xlabel('K')
plt.ylabel('Error Rate')

plt.show()

# run again de knn with the new 'k' value
k = 15
knn = KNeighborsClassifier(n_neighbors=k)

knn.fit(X_train, y_train)
predictions = knn.predict(X_test)

print(classification_report(y_test, predictions))
