# Welcome to the NLP Project for this section of the course. In this NLP project you will be attempting to classify
# Yelp Reviews into 1 star or 5 star categories based off the text content in the reviews.
#
# We will use the Yelp Review Data Set from Kaggle.
#
# Each observation in this dataset is a review of a particular business by a particular user.
#
# The "stars" column is the number of stars (1 through 5) assigned by the reviewer to the business.
# (Higher stars is better.) In other words, it is the rating of the business by the person who wrote the review.
#
# The "cool" column is the number of "cool" votes this review received from other Yelp users.
#
# All reviews start with 0 "cool" votes, and there is no limit to how many "cool" votes a review can receive.
# In other words, it is a rating of the review itself, not a rating of the business.
#
# The "useful" and "funny" columns are similar to the "cool" column.

import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import  TfidfTransformer
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import classification_report, confusion_matrix

# using grid in Seaborn
sns.set_style('whitegrid')

data = pd.read_csv('yelp.csv')

# counting how many words are in each text in each row
data['text length'] = data['text'].apply(len)
print(data.head())
print(data.info())
print(data.columns.values)

# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
# ---------------------------------  DATA VISUALIZATION ---------------------------------
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------

# FacetGrid from the seaborn library to create a grid of 5 histograms of text length based off of the star ratings
# g = sns.FacetGrid(data, col='stars')
# g.map(plt.hist, 'text length')

# boxplot of text length for each star category
# sns.boxplot(data=data, x='stars', y='text length')

# countplot of the number of occurrences for each type of star rating
# sns.countplot(x='stars', data=data)

# groupby to get the mean values of the numerical columns
numeric = data.select_dtypes(include=np.number)
numeric_group = numeric.groupby(['stars']).mean()

# correlation between groups
correlated_numeric = numeric_group.corr()
# print(correlated_numeric.head())

sns.heatmap(data=correlated_numeric, annot=True)

# plt.show()

# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
# ----------------------------------------- NLP -----------------------------------------
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------

# To make things a little easier, go ahead and only grab reviews that were either 1 star or 5 stars.
# Dataframe called yelp_class that contains the columns of yelp dataframe but for only the 1 or 5 star reviews
yelp_class = data[(data.stars == 1) | (data.stars == 5)]
print(yelp_class.head())
print(yelp_class.info())
print(yelp_class.columns.values)

# two objects X and y.
# *(features) = X  will be the 'text' column of yelp_class
# *(target) = y will be the 'stars' column of yelp_class
X = yelp_class['text']
y = yelp_class['stars']

# create a CountVectorizer object.
cv = CountVectorizer()
X = cv.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

# and create an instance of MultinomialNB estimator
mnb = MultinomialNB()
mnb.fit(X_train, y_train)

# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
# ----------------------------------  Evaluating Model ----------------------------------
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
predictions = mnb.predict(X_test)

print(classification_report(y_test, predictions))
print(confusion_matrix(y_test, predictions))

# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
# -------------------------------- Using Text Processing --------------------------------
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
# pipeline with the following steps:CountVectorizer(), TfidfTransformer(),MultinomialNB()
pipeline = Pipeline([
    ('bow', CountVectorizer()),  # strings to token integer counts
    # ('tfidf', TfidfTransformer()),  # integer counts to weighted TF-IDF scores
    ('classifier', MultinomialNB()),  # train on TF-IDF vectors w/ Naive Bayes classifier
])

X = yelp_class['text']
y = yelp_class['stars']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

# fit the pipeline to the training data.
# Remember you can't use the same training data as last time because that data has already been vectorized.
# We need to pass in just the text and labels
pipeline.fit(X_train, y_train)

predictions = pipeline.predict(X_test)

print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))
