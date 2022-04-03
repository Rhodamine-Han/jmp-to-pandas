#iloc

import pandas as pd

df = pd.read_excel('OS_test_sorter.xlsx', index_col='OS1')
#df.iloc[4,0]

print(df.iloc[0:3,0:1])