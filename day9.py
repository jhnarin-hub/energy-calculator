import pandas as pd

data =  {
"name": ["Fridge", "TV", "Fan", "Lights", "Laptop", "Iron"],
"watts": [150, 100, 60, 40, 65, 1000],
"hours": [24, 5, 8, 6, 4, 1],
"rooms": ["kitchen", "living", "bedroom", "living", "bedroom", "bedroom"],
}

df = pd.DataFrame(data)
df["kwh"] = df["watts"] * df["hours"] / 1000
df["cost N"] = df["kwh"] * 63
print(df)
print("------------------")
print(df["watts"])
print("------------------")
print(df["watts"].sum())
print(df["watts"].max())
print("------------------------------")
print("Total_kwh", df["kwh"].sum(), "kwh")
print("------------------------------")
print("total daily cost:", df["cost N"].sum())
heavy = df[df["kwh"] > 1]
print(heavy)
print(df[(df["kwh"] > 0.4) & (df["rooms"] == "living")])
ranked = df.sort_values("kwh", ascending=False)
print(ranked)
print(ranked.iloc[0]["name"])
by_room = df.groupby("rooms")["kwh"].sum()
print(by_room)
df.to_csv("appliances.csv", index=False)
df2 = pd.read_csv("appliances.csv")
print(df2.head())

