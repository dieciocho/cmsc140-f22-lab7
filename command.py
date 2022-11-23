import pandas as pd
data = pd.read_csv("city_temperature.csv")
data["HighTemp"] = data.groupby(by="Region")["AvgTemperature"].transform(max)
result = data[data["HighTemperature"] == data["HighTemp"]]
result = result.drop("HighTemp", axis="columns")
result.to_csv("city_maxtemp.csv", index=False)
