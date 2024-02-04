#---------Open and Read Data----------
#-----Method-1
with open(r"C:\Users\MD. SHAMIM\Documents\GitHub\100-Days-of-Pyhon\Day-25 CSV and Pandas\weather_data.csv") as data_file:
    data = data_file.readlines()
    print(data)

#------Method-2
print("Method-2")
import csv 
with open(r"C:\Users\MD. SHAMIM\Documents\GitHub\100-Days-of-Pyhon\Day-25 CSV and Pandas\weather_data.csv") as data_file:
    data = csv.reader(data_file)
    for row in data:
        print(row)

#------Store specific data into the list
print("---------Store specific data into the list------")
import csv 
with open(r"C:\Users\MD. SHAMIM\Documents\GitHub\100-Days-of-Pyhon\Day-25 CSV and Pandas\weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temprature = []
    for row in data:
        if row[1] != "Temp":
            temprature.append(row[1])
    print(temprature)