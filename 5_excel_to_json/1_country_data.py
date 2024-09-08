import pandas as pd

df = pd.read_excel("europe.xlsx")

df.to_json("europe.json", orient="records")
# df.to_json("europe.json", orient="records", lines=True)

df.to_csv("europe.csv")
# df.to_csv("europe.csv", index=False)

