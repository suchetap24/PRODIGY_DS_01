import seaborn as sns
import matplotlib.pyplot as plt
tip=sns.load_dataset('tips')
print(tip.head())
print(tip.shape)
print(tip.isnull().sum())
sns.barplot(x='day',y='total_bill',data=tip,hue='smoker',palette='pink')
plt.show()
sns.scatterplot(x='tip',y='total_bill',data=tip)
plt.show()