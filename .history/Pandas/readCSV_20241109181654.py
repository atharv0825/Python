import pandas as pd

df = pd.read_csv(r'C:\Users\Athar\OneDrive\Documents\Python\Pandas\tips.csv')

print(df.info())
print('------------------------------------------------------\n')
print(df.head())
print('------------------------------------------------------\n')
print(df.tail())
print('------------------------------------------------------\n')
print(df.describe())
print('------------------------------------------------------\n')
print(df.columns)
print('------------------------------------------------------\n')
# print(df.groupby('column_name').mean())
print('------------------------------------------------------\n')

