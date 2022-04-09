##loc

import pandas as pd

df = pd.read_excel('OS_test_sorter.xlsx', index_col='OS1')
#df.loc['D0N']
print(df.loc['OS2':'OS3'])