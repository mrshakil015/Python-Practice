city_of_bangladesh = ["Dhaka", "Gazipur","Bhola","Barisal","Chadpur","Khulna"]


print(city_of_bangladesh)
list_size = len(city_of_bangladesh)
print(list_size)
print(city_of_bangladesh[2])
print(city_of_bangladesh[-2])

#add an item to the end of the list
city_of_bangladesh.append("Rangpur")
print(city_of_bangladesh)

#Add another list item to the end of the list
city_of_bangladesh.extend(["Shylet","Noakhali"])
print(city_of_bangladesh)

#Insert an item at a given position
city_of_bangladesh.insert(4, "Nator")
print(city_of_bangladesh)

#Remove item from the list
city_of_bangladesh.remove("Bhola")
print(city_of_bangladesh)

#Sort the items of the list
city_of_bangladesh.sort()
print(city_of_bangladesh)

#Reverse the elements of the list
city_of_bangladesh.reverse()
print(city_of_bangladesh)

