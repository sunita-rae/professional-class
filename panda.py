#pandas example
import pandas as pd
data={
    "Name ":["A","B","C"],
    "Marks" :[88,75,50]

}
df=pd.DataFrame(data)
print(df)
print("\n Description \n",df.describe())