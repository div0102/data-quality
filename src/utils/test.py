import pandas as pd

df = pd.read_csv("C:\\Users\\bajpaid\\OneDrive - WWT\\Desktop\\tested.txt",delimiter=",",header=0)

print(df)
print(df.columns.values.tolist())