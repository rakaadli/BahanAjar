import pandas as pd
sal = pd.read_csv('Salaries.csv')
print(sal.head())
print(sal.info())

print('Berapa gaji rata2?')
print(sal['BasePay'].mean())

print('Berapa overtimepay yang terbesar?')
print(sal['OvertimePay'].mean())

print('What is the job title JOSEPH DRISCOLL')
print(sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['JobTitle'])

#What is the name highest paid person
#print(sal[sal['TotalPayBenefits']== sal['TotalPayBenefits'].max()]) #['EmployeeName']
#kalau mau ambil namanya
#print(sal[sal['TotalPayBenefits']== sal['TotalPayBenefits'].max()]['EmployeeName'])
# or
print(sal.loc[sal['TotalPayBenefits'].idxmax()])

#what is the lowest paid person (including benefits)? 
#sal[sal['TotalPayBenefits']== sal['TotalPayBenefits'].min()] #['EmployeeName']
# or
print(sal.loc[sal['TotalPayBenefits'].idxmax()]['EmployeeName'])

## ITS NEGATIVE!! VERY STRANGE

#What was the average (mean) basepay of al employees per year?
print(sal.groupby('Year').mean()['BasePay'])

#How many unique job titles are there?
print(sal['JobTitle'].nunique())

#What are the top 5 most common jobs in this?
print(sal['JobTitle'].value_counts().head(5))

#How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with only one occurence in 2013?)
sum(sal[sal['Year']==2013]['JobTitle'].value_counts() == 1)

#How many people have the word Chief in their job title? (This is pretty tricky)
def chief_string(title):
    if 'chief' in title.lower():
        return True
    else:
        return False

print(sum(sal['JobTitle'].apply(lambda x: chief_string(x))))

#Bonus: Is there a correlation between length of the Job Title string and Salary?
sal['title_len'] = sal['JobTitle'].apply(len)
print(sal[['title_len','TotalPayBenefits']].corr())