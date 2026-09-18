import pandas as pd
from sklearn.preprocessing import StandardScaler
df=pd.read_csv("data/demo_agro_data.csv")
X=df.drop(columns="target")
print(StandardScaler().fit_transform(X).shape)
