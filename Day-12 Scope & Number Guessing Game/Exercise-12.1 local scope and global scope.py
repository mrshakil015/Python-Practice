# Local Scope
def local_scope():
    value = 3
    print(f"Local variable inside function: {value}")
local_scope()

# Global Scope
value = 10
def global_scope():
    print(f"Global variable inside the function: {value}")
global_scope()
print(f"Global variable outside the function: {value}")

#Modify global variable

value = 5
def increase_value():
    print(f"Inside increase function: {value}")
    return value + 10
new_value = increase_value()
print(f"Modify value is: {new_value}")

