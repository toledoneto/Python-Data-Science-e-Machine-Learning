# For this project we will be exploring publicly available data from LendingClub.com. Lending Club connects people who need money (borrowers) with people who have money (investors). Hopefully, as an investor you would want to invest in people who showed a profile of having a high probability of paying you back. We will try to create a model that will help predict this.
#
# Lending club had a very interesting year in 2016, so let's check out some of their data and keep the context in mind. This data is from before they even went public.
#
# We will use lending data from 2007-2010 and be trying to classify and predict whether or not the borrower paid back their loan in full. You can download the data from here or just use the csv already provided. It's recommended you use the csv provided as it has been cleaned of NA values.
#
# Here are what the columns represent:
#
#     credit.policy: 1 if the customer meets the credit underwriting criteria of LendingClub.com, and 0 otherwise.
#     purpose: The purpose of the loan (takes values "credit_card", "debt_consolidation", "educational", "major_purchase", "small_business", and "all_other").
#     int.rate: The interest rate of the loan, as a proportion (a rate of 11% would be stored as 0.11). Borrowers judged by LendingClub.com to be more risky are assigned higher interest rates.
#     installment: The monthly installments owed by the borrower if the loan is funded.
#     log.annual.inc: The natural log of the self-reported annual income of the borrower.
#     dti: The debt-to-income ratio of the borrower (amount of debt divided by annual income).
#     fico: The FICO credit score of the borrower.
#     days.with.cr.line: The number of days the borrower has had a credit line.
#     revol.bal: The borrower's revolving balance (amount unpaid at the end of the credit card billing cycle).
#     revol.util: The borrower's revolving line utilization rate (the amount of the credit line used relative to total credit available).
#     inq.last.6mths: The borrower's number of inquiries by creditors in the last 6 months.
#     delinq.2yrs: The number of times the borrower had been 30+ days past due on a payment in the past 2 years.
#     pub.rec: The borrower's number of derogatory public records (bankruptcy filings, tax liens, or judgments).


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier

# using grid in Seaborn
sns.set_style('whitegrid')

loans = pd.read_csv('loan_data.csv')

print(loans.head())
print(loans.info())
print(loans.columns.values)

# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
# ---------------------------------  DATA VISUALIZATION ---------------------------------
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------

# The FICO® Score helps lenders make accurate, reliable and fast credit risk decisions across the customer lifecycle.
# The credit risk score rank-orders consumers by how likely they are to pay their credit obligations as agreed
# a histogram of two FICO distributions on top of each other, one for each credit.policy outcome

plt.figure(figsize=(10,6))
loans[loans['credit.policy'] == 1]['fico'].hist(alpha=0.5, color='blue',
                                              bins=30, label='Credit.Policy=1')
loans[loans['credit.policy'] == 0]['fico'].hist(alpha=0.5, color='red',
                                              bins=30, label='Credit.Policy=0')
plt.legend()
plt.xlabel('FICO')

# a histogram of two FICO distributions on top of each other, one for each not.fully.paid outcome
plt.figure(figsize=(10,6))
loans[loans['not.fully.paid'] == 1]['fico'].hist(alpha=0.5, color='blue',
                                              bins=30, label='not.fully.paid=1')
loans[loans['not.fully.paid'] == 0]['fico'].hist(alpha=0.5, color='red',
                                              bins=30, label='not.fully.paid=0')
plt.legend()
plt.xlabel('FICO')

# countplot using seaborn showing the counts of loans by purpose, with the color hue defined by not.fully.paid.
plt.figure(figsize=(10, 6))
sns.countplot(x='purpose', hue='not.fully.paid', data=loans, palette='Set1')

# trend between FICO score and interest rate
sns.jointplot(x='fico', y='int.rate', data=loans)

# lmplots to see if the trend differed between not.fully.paid and credit.policy
sns.lmplot(x="fico", y="int.rate", col="not.fully.paid", data=loans, hue='credit.policy', palette='Set1')

# plt.show()

# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
# --------------------------------- DATA PRE PROCESSING ---------------------------------
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------

# categorical feature
print('----------------------------------------------------------')
cat_feats = ['purpose']
# pd.get_dummies will turn the categorical features into a 0/1 False/True numerical column
final_data = pd.get_dummies(loans, columns=cat_feats, drop_first=True)
# print(final_data.head())
# print(final_data.info())
# print(final_data.columns.values)

# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
# ------------------------------------ Decision Tree ------------------------------------
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------

X = final_data.drop('not.fully.paid', axis=1)
y = final_data['not.fully.paid']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=101)

dtree = DecisionTreeClassifier()
dtree.fit(X_train, y_train)

predictions = dtree.predict(X_test)

print(classification_report(y_test, predictions))

print(confusion_matrix(y_test, predictions))

# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
# ------------------------------------ Random Forest ------------------------------------
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------

# n_estimators is the number of trees in the forest
rforest = RandomForestClassifier(n_estimators=600)
rforest.fit(X_train, y_train)

rforest_predictions = rforest.predict(X_test)

print(classification_report(y_test, rforest_predictions))

print(confusion_matrix(y_test, rforest_predictions))
