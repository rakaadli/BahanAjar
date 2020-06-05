import seaborn as sns
import matplotlib.pyplot as plt

'''
DATA
'''
#kita akan load dataset tips oiriginal dari seaborn
tips = sns.load_dataset('tips')
print(tips)

sns.distplot(tips['total_bill'])
sns.distplot(tips['total_bill'],kde=False,bins=30)
plt.show()