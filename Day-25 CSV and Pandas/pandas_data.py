import pandas as pd

data = pd.read_csv(r"C:\Users\MD. SHAMIM\Documents\GitHub\100-Days-of-Pyhon\Day-25 CSV and Pandas\weather_data.csv")
print(data)

print("Print specific column data:")
print(data["Temp"])

print("Convert data into dictionary:")
data_dict = data.to_dict()
print(data_dict)

print("Convert data into list:")
temp_list = data["Temp"].to_list()
print(temp_list)

print("Average of a list: ")
temp_ave = sum(temp_list)/len(temp_list)
print(round(temp_ave,2))

print("Maximum value of temputer: ", max(temp_list))
print("Median value of temputer: ",data["Temp"].median())

#--------Get Column--------
print("---------Get Column----------")
print(data.Condition)

#--------Get Row--------
print("---------Get Row----------")
print(data[data.Condition == "Sunny"])

#--------Get Maximum Row--------
print("---------Get Maximum Row----------")
print(data[data.Temp == max(data.Temp)])