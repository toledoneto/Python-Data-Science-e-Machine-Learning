# import pandas
import pandas as pd

ecom = pd.read_csv('Ecommerce Purchases')

# Check the head of the DataFrame.
print(ecom.head())
print('\n')

# How many rows and columns are there?
print("Number of columns: " + str(len(ecom.columns)))
print('\n')

# dataframe info
print(ecom.info())
print('\n')

# What is the average Purchase Price?
print(ecom['Purchase Price'].mean())
print('\n')

# What were the highest and lowest purchase prices?
print("highest: " + str(ecom['Purchase Price'].max()))
print("lowest: " + str(ecom['Purchase Price'].min()))
print('\n')

# How many people have English 'en' as their Language of choice on the website?
print(ecom[(ecom['Language'] == 'en')].count())
print('\n')

# How many people have the job title of "Lawyer"?
print(ecom[(ecom['Job'] == 'Lawyer')].count())
print('\n')

# How many people made the purchase during the AM and how many people made the purchase during PM?
print((ecom['AM or PM']).value_counts())
print('\n')

# What are the 5 most common Job Titles?
print((ecom['Job']).value_counts().head())
print('\n')

# Someone made a purchase that came from Lot: "90 WT" , what was the Purchase Price for this transaction?
print(ecom[ecom['Lot'] == "90 WT"]['Purchase Price'])
print('\n')

# What is the email of the person with the following Credit Card Number: 4926535242672853?
print(ecom[ecom['Credit Card'] == 4926535242672853]['Email'])
print('\n')

# How many people have American Express as their Credit Card Provider AND made a purchase above $95 ?
print(str(sum(ecom[ecom['CC Provider'] == 'American Express']['Purchase Price'] > 95)) + " people")
print('\n')


# How many people have a credit card that expires in 2025?
def yearExpire(date):
    return date.split('/')[-1]


print(str(sum(ecom['CC Exp Date'].apply(lambda x: yearExpire(x)) == '25')) + " people")
print('\n')


# What are the top 5 most popular email providers/hosts (e.g. gmail.com, yahoo.com, etc...)
def emailProvider(email):
    return email.split('@')[-1]


print(ecom['Email'].apply(lambda x: emailProvider(x)).value_counts().head())
