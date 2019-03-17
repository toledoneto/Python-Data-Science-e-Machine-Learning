# For this project we will attempt to use KMeans Clustering to cluster Universities into to two groups:
# * Private and
# * Public.
# It is very important to note, we actually have the labels for this data set, but we will NOT use them for the KMeans
# clustering algorithm, since that is an unsupervised learning algorithm.
#
# When using the Kmeans algorithm under normal circumstances, it is because you don't have labels.
# In this case we will use the labels to try to get an idea of how well the algorithm performed,
# but you won't usually do this for Kmeans, so the classification report and confusion matrix at the end,
# don't truly make sense in a real world setting!.

# The Data
#
# We will use a data frame with 777 observations on the following 18 variables.
#
#     Private A factor with levels No and Yes indicating private or public university
#     Apps Number of applications received
#     Accept Number of applications accepted
#     Enroll Number of new students enrolled
#     Top10perc Pct. new students from top 10% of H.S. class
#     Top25perc Pct. new students from top 25% of H.S. class
#     F.Undergrad Number of fulltime undergraduates
#     P.Undergrad Number of parttime undergraduates
#     Outstate Out-of-state tuition
#     Room.Board Room and board costs
#     Books Estimated book costs
#     Personal Estimated personal spending
#     PhD Pct. of faculty with Ph.D.’s
#     Terminal Pct. of faculty with terminal degree
#     S.F.Ratio Student/faculty ratio
#     perc.alumni Pct. alumni who donate
#     Expend Instructional expenditure per student
#     Grad.Rate Graduation rate

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import classification_report, confusion_matrix

# using grid in Seaborn
sns.set_style('whitegrid')

data = pd.read_csv('College_Data', index_col=0)

print(data.head())
print(data.info())
print(data.columns.values)

# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
# ---------------------------------  DATA VISUALIZATION ---------------------------------
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------

# sns.scatterplot(x='Room.Board', y='Grad.Rate', hue='Private', data=data)
# sns.scatterplot(x='Outstate', y='F.Undergrad', hue='Private', data=data)
#
# sns.set_style('darkgrid')
# g = sns.FacetGrid(data, hue="Private", palette='coolwarm', size=6, aspect=2)
# g = g.map(plt.hist, 'Outstate', bins=20, alpha=0.7)
#
# sns.set_style('darkgrid')
# g = sns.FacetGrid(data, hue="Private", palette='coolwarm', size=6, aspect=2)
# g = g.map(plt.hist, 'Grad.Rate', bins=20, alpha=0.7)

# there seems to be a private school with a graduation rate of higher than 100%.What is the name of that school?
print(data[data['Grad.Rate'] > 100])

# setting this school's Grad Rate to 100 so it makes sense
data['Grad.Rate']['Cazenovia College'] = 100
# re run the graph above
sns.set_style('darkgrid')
g = sns.FacetGrid(data, hue="Private", palette='coolwarm', size=6, aspect=2)
g = g.map(plt.hist, 'Grad.Rate', bins=20, alpha=0.7)


# plt.show()

# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
# --------------------------------------- K-means ---------------------------------------
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------

X = data.drop('Private', axis=1)
# choose 2 clusters because there are only two possible outcomes: Private and Public
kms = KMeans(n_clusters=2)
kms.fit(X)

# clusters centers
print(kms.cluster_centers_)

# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
# ----------------------------------  Evaluating Model ----------------------------------
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------


# Remember: this don't make sense in a real application, but this is an exercise (y)
def converter(cluster):
    if cluster=='Yes':
        return 1
    else:
        return 0


data['Cluster'] = data['Private'].apply(converter)

print(confusion_matrix(data['Cluster'], kms.labels_))
print(classification_report(data['Cluster'], kms.labels_))
