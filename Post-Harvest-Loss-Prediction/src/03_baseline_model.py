import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
df=pd.read_csv("data/demo_agro_data.csv"); X=df.drop(columns="target"); y=df.target
X1,X2,y1,y2=train_test_split(X,y,test_size=.25,random_state=42)
m=RandomForestRegressor(n_estimators=100,random_state=42).fit(X1,y1)
print("MAE",mean_absolute_error(y2,m.predict(X2)))
