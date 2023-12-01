two_digit_num = input("Type a two digit number: ")

#Check the data type of two digit number
print(type(two_digit_num))

#Get the first and second digits using subscripting then convert string to int.
a = two_digit_num[0]
b = two_digit_num[1]

#Add the two digits togeter
add_digit = int(a)+int(b)
print(add_digit)

#Subtract the two digits togeter
add_digit = int(a)-int(b)
print("Subtract: "+ str(add_digit))