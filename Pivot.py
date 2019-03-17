#Sarkis Mikaelian - COMP 541

import pandas as pd
import numpy as np

df= pd.read_csv(r'C:\Users\Serge Mikaelian\Documents\CSUN\COMP 541\GOOGLE.csv')
dtype={"Date": np.int32, "Open": np.float, "High": np.float, "Low": np.float, "Close": np.float, "change": np.float, "Volume": np.int32, "momentum": np.int32, "year": np.int32, "month": np.int32, "day": np.int32}


df.dropna()

grouped= df.groupby(['month', 'year'])
grouped1= df.groupby(['Volume', 'momentum'])
grouped2= df.groupby(['day', 'month'])
groupVol= df.groupby('Volume').mean()
groupChange= df.groupby('change').mean()


pivoted1= pd.pivot_table(df ,index=["Open","Close"], values=["change"])
pivoted2= pd.pivot_table(df ,index=["Open","Close"], values=["Volume"], aggfunc=[np.sum])
pivoted3= pd.pivot_table(df ,index=["Open","Close"], values=["Volume", "momentum", "change"], aggfunc=[np.mean])
pivoted4= pd.pivot_table(df ,index=["Open","Close"], values=["Volume", "momentum", "change"], columns=["High", "Low"], aggfunc=[np.mean], fill_value=0, margins= True, dropna= True)

print(pivoted4)
df.dtypes
