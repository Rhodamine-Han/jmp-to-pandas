import pandas as pd

df = pd.read_csv('OS_test_sorter.csv')
#df = pd.read_csv('OS_test_sorter.csv', index_col='OS1')

#in this case, you can get the data with boolean type!
#print(df['OS1'].str.startswith('D'))

#!!!!!important!!!!!!!
#If there is Na, NaN raw > need to ad na=False part.
#print(df[df['OS1'].str.contains('D0N', na=False)])


#exception
#print(df[~df['OS1'].str.contains('D0N', na=False)])

#how to filter with list
# list1 = ['D0N', 'D1N']
# print(df[df['OS1'].isin(list1)])

#capital str > lower

df['OS1'] = df['OS1'].str.lower()

print(df)