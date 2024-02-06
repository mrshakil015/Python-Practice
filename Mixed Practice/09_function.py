def my_function1():
    print("Hello, This function.")
my_function1()

def my_function2(fname, lname):
    print(fname + " "+ lname)
my_function2("Md.","Shakil")

#Arbitrary Arguments
def my_function3(*name):
    print("The adult child is: ", name[2])
my_function3("Rahim", "Karim","Abdul")

#Keyword Arguments
def my_function4(name1, name2, name3):
    print("The first child is: "+ name1)
    print("The second child is: "+ name2)
    print("The third child is: "+ name3)
my_function4(name1= "Rahim", name2= "Karim", name3= "Abdul")

def print_sum(num1, num2):
    print("Result: ",num1 + num2)
print_sum(5,8)

def print_sum2(num1, num2=20):
    print("Result: ",num1 + num2)
print_sum2(5)
