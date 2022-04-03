##condition

import pandas as pd

df = pd.read_excel('OS_test_sorter.xlsx', index_col='OS1')

# list = (df[df.columns[-1]]>=0.1)

# df[list]

print(df[df[df.columns[-1]]>=0.1])
# df.loc[df[df.columns[-1]]>0.1 &]
