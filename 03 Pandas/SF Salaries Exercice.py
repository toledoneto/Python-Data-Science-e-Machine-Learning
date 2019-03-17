# importing Pandas
import pandas as pd

# reading csv
data = pd.read_csv('Salaries.csv')


# ------ EXC 1 : Check the head of the DataFrame.
print(data.head())
print('\n')

# ------ EXC 2 : Use the .info() method to find out how many entries there are.
print(data.info())
print('\n')

# ------ EXC 3 : What is the average BasePay ?
print(data['BasePay'].mean())
print('\n')

# ------ EXC 4 : What is the highest amount of OvertimePay in the dataset ?
print(data['OvertimePay'].max())
print('\n')

# ------ EXC 5 : What is the job title of JOSEPH DRISCOLL ?
print(data[(data.EmployeeName == 'JOSEPH DRISCOLL')]['JobTitle'])
print('\n')

# ------ EXC 6 : How much does JOSEPH DRISCOLL make (including benefits)?
print(data[(data.EmployeeName == 'JOSEPH DRISCOLL')]['TotalPay'])
print('\n')

# ------ EXC 7 : What is the name of highest paid person (including benefits)?
print(data[(data.TotalPay == data['TotalPay'].max())])
print('\n')

# ------ EXC 8 : What is the name of lowest paid person (including benefits)?
print(data[(data.TotalPay == data['TotalPay'].min())])
print('\n')

# ------ EXC 9 : What was the average (mean) BasePay of all employees per year? (2011-2014) ?
print(data.groupby(['Year'])['BasePay'].mean())
print('\n')

# ------ EXC 10 : How many unique job titles are there?
print(data['JobTitle'].nunique())
print('\n')

# ------ EXC 11 : What are the top 5 most common jobs?
print(data['JobTitle'].value_counts().head())
print('\n')

# ------ EXC 12 : How many Job Titles were represented by only one person in 2013?
print(sum(data[data['Year']==2013]['JobTitle'].value_counts() == 1))
print('\n')


# ------ EXC 13 : How many people have the word Chief in their job title?
def chief_string(title):
    if 'chief' in title.lower():
        return True
    else:
        return False


print(sum(data['JobTitle'].apply(lambda x: chief_string(x))))
print('\n')

# ------ EXC 14 : Is there a correlation between length of the Job Title string and Salary?
data['title_len'] = data['JobTitle'].apply(len)
print(data[['title_len','TotalPayBenefits']].corr()) # No correlation.
print('\n')
