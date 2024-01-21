import pandas as pd
import requests
import json
data = requests.get("https://fruityvice.com/api/fruit/all")
results = json.loads(data.text)
print(pd.DataFrame(results))
df2 = pd.json_normalize(results)
print(df2)
cherry = df2.loc[df2["name"] == 'Cherry']
res = (cherry.iloc[0]['family']) , (cherry.iloc[0]['genus'])
print(res)
banana = df2.loc[df2["name"]=='Banana']
res2 = banana.iloc[0]['nutritions.calories']
print(res2)
