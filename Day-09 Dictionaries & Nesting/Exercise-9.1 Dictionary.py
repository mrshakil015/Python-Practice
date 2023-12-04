programmming_dictionary = {
    "Bug": "This is bug section.",
    "Function": "This is function section."
}

#Print dictionary key into the list
print("Dictionary keys is: ",list(programmming_dictionary.keys()))

#Print dictionary value into the list
print("Dictionary values is: ",list(programmming_dictionary.values()))

#returns the value of specified key
print("Specified value: ",programmming_dictionary.get("Bug"))

#Update the dictionary
programmming_dictionary.update({"Error":"This is error"})
print("Updated dictionary: ",programmming_dictionary)

#Adding new items to dictionary
programmming_dictionary["Loop"] = "This is loop section."
print("After adding: ", programmming_dictionary)

#Edit an item in a dictionary
programmming_dictionary["Loop"] = "Edit loop item"
print("After Editing: ", programmming_dictionary)

#Print dictionary key using loop
print("Key is: ")
for key in programmming_dictionary:
    print(key)

#Print dictionary value using loop
print("Value is: ")
for key in programmming_dictionary:
    print(programmming_dictionary[key])