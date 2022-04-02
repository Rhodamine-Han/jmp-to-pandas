#!/usr/bin/env python
# coding: utf-8

# In[11]:


##series

# import pandas as pd

# temp = pd.Series([-20, -10, 10, 20], index = ['Jan', 'Feb', 'Mar', 'Apr'])

# temp


# In[26]:




##Data Frame
# import pandas as pd


# data = {
#     'Uni' : ['Kyushu', 'Seoul', 'Tokyo'], 'Conpany' : ['LGinnotek', 'Samsung Electrics', 'SK hynics'], 'name' : ['Rhodamine', 'Ted', 'Hines']
# }

# #df stands for data frame
# df = pd.DataFrame(data, index = ['Student1', 'Student2', 'Student3'], columns = ['name', 'Uni'])

# df


# In[20]:




##index

#Data Frame
# import pandas as pd


# data = {
#     'Uni' : ['Kyushu', 'Seoul', 'Tokyo'], 'Conpany' : ['LGinnotek', 'Samsung Electrics', 'SK hynics'], 'name' : ['Rhodamine', 'Ted', 'Hines']
# }

#df stands for data frame
# df = pd.DataFrame(data, index = ['Student1', 'Student2', 'Student3'])

#reset
# df.index.name = 'students information'
# df.reset_index()

#reset and get rid of previous index
# df.index.name = 'students information'
# df.reset_index(drop=True, inplace=True)

#setting uni as the index
#inplace = setting those data as real data
# df.set_index('Uni', inplace=True)
# df

#sorting

# df.set_index('Uni', inplace=True)
# df.sort_index()


# In[13]:



##File reading and writting

#writting
# import pandas as pd

# data = {
#     'Uni' : ['Kyushu', 'Seoul', 'Tokyo'], 'Conpany' : ['LGinnotek', 'Samsung Electrics', 'SK hynics'], 'name' : ['Rhodamine', 'Ted', 'Hines']
# }

# df = pd.DataFrame(data, index = ['Student1', 'Student2', 'Student3'])

# df.to_csv('information.csv')

#reading

# import pandas as pd

# df = pd.read_excel('OS_test_sorter.xlsx', skiprows = 1, nrows = 10)

#df.head()
#df.tail(3)
#df['Unnamed: 2'].nlargest(3)


# In[22]:



##data selecting

# import pandas as pd

# df = pd.read_excel('OS_test_sorter.xlsx', skiprows = 1, nrows = 10)

# df[df.columns[-1]][0:5]


# In[82]:



##loc

# import pandas as pd

# df = pd.read_excel('OS_test_sorter.xlsx', index_col='OS1')
# #df.loc['D0N']
# df.loc['OS2':'OS3']


# In[60]:



# #iloc

# import pandas as pd

# df = pd.read_excel('OS_test_sorter.xlsx', index_col='OS1')
# #df.iloc[4,0]

# df.iloc[0:3,0:3]


# In[84]:



# #condition

import pandas as pd

df = pd.read_excel('OS_test_sorter.xlsx', index_col='OS1')

# list = (df[df.columns[-1]]>=0.1)

# df[list]

# df[df[df.columns[-1]]>=0.1]

print(df.loc[df[df.columns[-1]]>0.1])

