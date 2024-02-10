# 100-Days-of-Pyhon

<details>
  <summary><b> Python Random Module</b></summary>
The random module in Python is a built-in module that provides various functions for generating random numbers and making random choices. It is commonly used for tasks such as generating random data, shuffling sequences, simulating random events, and more. The random module uses a pseudorandom number generator to produce random numbers.

You can import the random module using the following statement:
  ```python
import random
```
The <strong>random</strong> module provides the following functions:
  - <code>random():</code> Returns a random floating-point number between 0 and 1 (inclusive of 0, but exclusive of 1).
    ```python
    import random
    ```
  - <code>seed(a=None):</code> Initializes the random number generator with a seed value. If a is not specified, it uses the current system time.
    ```python
    import random
    
    random.seed(42)
    random_number = random.random()
    print(random_number)
    ```
  - <code>randrange(start, stop=None, step=1):</code> Returns a randomly selected element from the specified range. The start parameter is the starting point of the range (inclusive), stop is the endpoint of the range (exclusive), and step is the step value (optional).
    ```python
    import random
    
    random_number = random.randrange(1, 10, 2)
    print(random_number)
    ```
  - <code>randint(a, b):</code> Returns a random integer between a and b (inclusive of both a and b).
    ```python
    import random
    
    random_number = random.randint(1, 100)
    print(random_number)
    ```
  - <code>choice(seq):</code> Returns a randomly chosen element from a non-empty sequence seq, such as a list or a tuple.
    ```python
    import random
    
    my_list = [1, 2, 3, 4, 5]
    random_element = random.choice(my_list)
    print(random_element)
    ```
  - <code>shuffle(seq):</code> Randomly shuffles (rearranges) the elements in a sequence seq in place.
    ```python
    import random

    my_list = [1, 2, 3, 4, 5]
    random.shuffle(my_list)
    print(my_list)
    ```
  - <code>sample(population, k):</code> Returns a random selection of k unique elements from the specified population without replacement.
    ```python
    import random

    my_list = [1, 2, 3, 4, 5]
    random_selection = random.sample(my_list, 3)
    print(random_selection)
    ```
  - <code>random_uniform(a, b):</code> Returns a random floating-point number between a and b (inclusive of a, but exclusive of b).
    ```python
    import random

    random_number = random.random_uniform(0.5, 1.5)
    print(random_number)
    ```
  - <code>random_normal(mean=0.0, stddev=1.0):</code> Returns a random floating-point number with a normal distribution. The mean parameter is the mean value, and the stddev parameter is the standard deviation.
    ```python
    import random

    random_number = random.random_normal(mean=0, stddev=1)
    print(random_number)
    ```
  - <code>random_gauss(mean, stddev):</code> Equivalent to random.normalvariate(mean, stddev).
    ```python
    import random

    random_number = random.random_gauss(mean=0, stddev=1)
    print(random_number)
    ```
  - <code>getrandbits(k):</code> Returns a random integer with k random bits.
    ```python
    import random

    random_bits = random.getrandbits(4)
    print(random_bits)
    ```
  - <code>uniform(a, b):</code> Equivalent to random.uniform(a, b).
    ```python
    import random

    random_number = random.uniform(0.5, 1.5)
    print(random_number)
    ```
</details>

<details>
<summary><b>Important Note</b></summary>

+ <b>What do you mean by "Unhashable"?</b>
  An object is considered "unhashable" in Python if it is mutable, meaning its state can be modified after creation. Unhashable objects cannot be used as keys in dictionaries or as elements in sets because these data structures require elements to have stable and unique hash values. Examples of unhashable objects include lists, dictionaries, and other mutable types.
+ 
</details>

<details>
<summary><b>Important Links:</b></summary>


Here are some FREE resources that can help you learn end-to-end Python :

- 🎓 Learn Python: https://lnkd.in/eb4ke-9P
- 🔨 Python Projects: https://lnkd.in/eNWBfNzk
- 🚸 DSA with Python: http://bit.ly/3G3Dh0V
- 🌐 Learn Flask: https://lnkd.in/eqAg3jZP
- 🔧 Flask Projects: https://lnkd.in/eqnf7h-W
- 🔄 Learn REST API with Flask: https://lnkd.in/e-TTahQf
- 🧩 Learn Multithreading & Asyncio: https://lnkd.in/e_99Jiwp
- 🚦 Gunicorn & Nginx with Flask: https://lnkd.in/eWxgTNdB
- ✅ TDD with Python & Flask: https://lnkd.in/eMjweHuZ
- 📚 Basic RDBMS: https://lnkd.in/ebkPd8-q
- 🔍 Learn SQL: https://sqlbolt.com/ & W3Schools.com
- 🐘 PostgreSQL with Python: https://lnkd.in/esKUqNdt
- 🎁 Flask App with PostgreSQL: https://lnkd.in/eTzpcwNc
- 💻 Basics of Bash: https://lnkd.in/eZnG8cP6
- 🐳 Basics of Docker: https://lnkd.in/eFEK_aXW
- 🚢 Deploy Flask App with Docker: https://lnkd.in/eTjnFW8Y
- 🌟 GIT & GitHub: https://lnkd.in/ejshTxFw
- 🎨 Python Portfolio on Github: https://lnkd.in/eB2AanXj
- 📄 Python Resume Ideas: https://lnkd.in/e_Fb7uNi

</details>

<details>
<summary><b>List & Tuple in Python</b></summary>

### **Lists in Python**
---
A build-in data type that stores set of values. it can store elements of different types (integer, float, string, etc.).
</details>

<details>
<summary><b>Dictionary & Set in Python</b></summary>

### **Set in Python:**
---
Set is the collection of unordered items. Sets are mutable. But each element in the set must be unique & immutable. Set always ignore the duplicate items. Acceptable value of set:
+ boolean
+ int
+ float
+ str
+ tuple

**Note:** Set doesn't support list and dict. Beacuase list and dict are mutable. Set doesn't return error for duplicate items.
```python
#Syntax
mySet = {1,2,3,4,"Hello"}
```
```python
#create empty set
mySet = set()
```
#### **Set Methods:**
---
+ <code>set.add(el):</code> This method used to adds an element of the set.
  ```python
  #Create empty set
  mySet = set()

  #Add element into the set
  mySet.add("Python")
  mySet.add(121)

  #print set
  print(mySet)
  ```
+ <code>set.remove(el):</code> This method to remove a specific element.
  ```python
  mySet = {"Python","JavaScript",99,"Java"}
  mySet.remove("Python")
  print(mySet)
  ```
+ <code>set.clear():</code> This method used to removes all elements from the set.
  ```python
  mySet = {"Python","JavaScript",99,"Java"}
  mySet.clear()
  print(mySet)
  ```
+ <code>set.update(el):</code> This method to add multiple elements (iterable) to the set.
  ```python
  mySet = {"Python","JavaScript",99,"Java"}
  mySet.update([7, 8, 9])
  print(mySet)
  ```
+ <code>set.pop():</code> This method used to removes a random value.
  ```python
  mySet = {"Python","JavaScript",99,"Java"}
  print(mySet.pop())
  ```
+ <code>set.union(set2):</code> This method is used to perform the combines of two or more sets. The method returns a new set containing all unique elements from the sets involved.
  ```python
  mySet = {"Python","JavaScript",99}
  mySet2 = {7,8,"Java"}
  print(mySet.union(mySet2))
  ```
+ <code>set.intersection(set2):</code> This method is used to combines the common values of two or more sets.
  ```python
  mySet = {"Python","JavaScript",99}
  mySet2 = {7,99,"Python"}
  print(mySet.intersection(mySet2))
  ```
</details>

<details>
<summary><b>Loops in Python</b></summary>

### **While Loop:**
---

In Python, a while loop is used to repeatedly execute a block of code as long as a specified condition is true.

```python
#Syntax
while condition:
  #some code
```

```python
#Example
count = 1
while count<=5:
  print(count)
  count+=1

#Print from list
myList = ["ironman","spiderman","superman","batman"]
idx=0
while idx < len(myList):
  print(myList[idx])
  idx+=1
```

**Search for a number from tuple using loop:**

```python
  myTuple = (10,2,9,16,25)

  src=16
  i=0
  while i < (len(myTuple)):
    if myTuple[i]  == src:
      print("Search value present in index: ",i)
    i+=1
```
#### **Break & Continue:**
---
**<code>Break:</code>** It is used to terminate the loop when encountered.

```python
  myTuple = (10,2,9,16,25)

  src=16
  i=0
  while i < (len(myTuple)):
    if myTuple[i]  == src:
      print("Search value present in index: ",i)
      break
    i+=1
print("End of the loop")
```

**<code>Continue:</code>** It is used to terminates execution in the current iteration & continues execution of the loop with the next iteration.

```python
i = 1
while i<=5:
    if(i==3):
        i+=1
        continue
    print(i)
    i+=1
print("End of the loop")
```
### **For Loop:**
---
"For Loop" used for sequential traversal. For traversing list, string, tuples etc.

**Syntax:**
```python
for variable in iterable:
  #some work


#for loop with else:
for variable in iterable:
  #some work
else:
  #work when loop ends
```
**Example:**
```python
myList = [10,20,30,40]
for ele in myList:
  print(ele)
```
```python
myList = [10,20,30,40]
for ele in myList:
  print(ele)
else:
  print("End loop")
```

#### **range():**
---
Range functions returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
```python
range(start?,stop,step?)
```
```python
for el in range(5):
  print(el)

for el in range(1,5):
  print(el)

for el in range(1,5,2):
  print(el)
```

#### **Pass Statement:**
---
"pass" is a null statement that does nothing. It is used as a placeholder for future code.

```python
#Syntax
for el in range(10):
  pass
```
</details>

<details>
<summary><b>Functions in Python</b></summary>
A function is a block of reusable code that performs a specific task. Functions help in organizing code, making it more modular, readable, and easier to maintain.

```python
#Syntax
def func_name(param1, param2..):
  #some work
  return val

func_name(arg1, arg2) #function call
```
```python
myList = [2,3,4,5]
def myFunction(myList):
    for item in myList:
        print(item, end=" ")
myFunction(myList)
```

Mainly there are two types of function in python:
+ <b>Built-in Functions:</b> These are functions that are built into the Python language and are always available for use without the need to import any module. Examples include <code>print(), len(), range(), type(), sum(),</code> etc.
+ <b>User defined Functions: </b>These are functions defined by the user to perform specific tasks. You define them using the <code> def</code> keyword followed by the function name and parameters. These are the functions you create yourself to modularize your code and make it more readable and reusable.

### <b>Recursion</b>
---
Recursion in Python refers to the process in which a function calls itself directly or indirectly to solve a problem. Here a function calls itself repeatedly.


</details>

<details>
<summary><b>File I/O in Python</b></summary>

Python refers to the process of reading from and writing to files on the file system. Python provides several built-in functions and methods for performing file I/O operations.

#### <b>Types of all files:</b>
+ Text Files: .txt, .docx, .log etc.
+ Binary Files: .mp4, .mov, .png, .jpeg etc.

#### **Character & Meaning:**
+ <code>'r' :</code> open for reading(default)
+ <code>'r+' :</code> open and writing, it overwrite the file from starting not truncating the file.
+ <code>'w' :</code> open for writing, truncating the file first
+ <code>'w+' :</code> read and overwrite file, also truncating
+ <code>'x' :</code> create a new file and open it for writing
+ <code>'a' :</code> open for writing, appending to the end of the file if it exists
+ <code>'a+' :</code> read and append file
+ <code>'b' :</code> binary mode
+ <code>'t' :</code> text mode (default)
+ <code>'+' :</code> open a disk file for updating (reading and writing)

### <b>File I/O Operations</b>
---
### <b>Opening a File:</b>
To open a file in Python, we use the open() function, which takes two arguments: the file path and the mode. The mode specifies whether we want to read from ('r'), write to ('w'), or append to ('a') the file, among other options.
```python
#Syntax
file = open("file_name", "mode")
```

```python
#Another Syntax
with open("demo.txt", "a") as file:
  data = file.read()
```

```python
#Example
file = open('demo.txt', 'r')
data = file.read()
#Or
with open('demo.txt', 'r') as file:
  data = file.read()
```

### <b>Reading a File:</b>
Once the file is opened, you can read its contents using methods like <code>read(), readline(), or readlines().</code>

```python
# Read the entire contents of the file
content = file.read()
print(content)

# Read one line at a time
line = file.readline()
print(line)

# Read all lines into a list
lines = file.readlines()
print(lines)
```
### <b>Read & Write FIle:</b>
The <code>'r+' </code> mode in file handling refers to opening a file for both reading and writing without truncating the file. When you open a file in <code> 'r+' </code> mode, the file must exist; otherwise, Python will raise a FileNotFoundError.

```python
file = open('example.txt', 'r+')

# Reading data
print("Reading data:")
print(file.read())

# Moving the file pointer
file.seek(0)  # Move the pointer to the beginning of the file

# Writing data
file.write("Appending some more data.\n")

file.close()
```
### <b>Writing a File:</b>
To write data to a file, we need to open it in write mode ('w'). we can then use the write() method to write data to the file. When we write a file that time it overwrites the entire file. That means it remove the all previous text then write/add new text.

```python
# Open a file for writing
file = open('example.txt', 'w')

# Write data to the file
file.write("Hello, world!\n")
file.write("This is a test.\n")

# Close the file
file.close()
```
### <b>Read & Write File:</b>
The 'w+' mode in file handling refers to opening a file for both reading and writing. When you open a file in 'w+' mode, the file is created if it doesn't exist, or if it already exists, its contents are overwritten.

```python
file = open('example.txt', 'w+')

# Writing data
file.write("Writing some data.\n")

# Reading data
file.seek(0)  # Move the pointer to the beginning of the file
print("Reading data:")
print(file.read())

file.close()
```

### <b>Appending to a File:</b>
To append data to an existing file, we open it in append mode ('a'). We can then use the write() method as with write mode. When we append data, that data add at the end of the file.

```python
file = open("example.txt","a")
file.write("This is append method.")
file.close()
```

### <b>Read and Append File:</b>
The 'a+' mode in file handling refers to opening a file for both reading and appending. When we open a file in 'a+' mode, the file's pointer is initially positioned at the end of the file, so any write operations will append data to the end of the file. 

```python
file = open('File Operation/demo.txt', 'a+')

# Reading existing content
print("Reading existing content:")
file.seek(0)  # Move the pointer to the beginning of the file
print(file.read())

# Appending data
file.write("Appending some more data.\n")

file.close()
```


### <b>Deleting a File</b>
---
To delete a file in Python, we can use the os module. Module (like a code library) is a file written by another programmer that generally has a functions we can use.

```python
import os
os.remove(filename)
```
### <b>Practice some question</b>
---

<b>Qs. Finding Word form the file:</b>

```python
word = "Python"
with open("file.txt", "r") as f:
  data = f.read()
  if(word in data):
    print("Found")
  else:
    print("Not Found")
```

<b>Qs. Replae word from file</b>

```python
with open("file.txt", "r") as f:
  data = f.read()

new_data = data.replace("Java", "Python")
print(new_data)
```

<b>Qs. Find in which line of the file does the word "python" occur first.</b>

```python
def check_for_line():
  word = "python"
  data = True
  line_no = 1
  with open("file.txt","r") as f:
    while data:
      data = f.readline()
      if(word in data):
        print(line_no)
        return
      line_no +=1
  return print("Not found")

check_for_line()
```

</details>

<details>
<summary><b>OOP in Python</b></summary>
Object-oriented programming (OOP) in Python is a programming paradigm that revolves around the concept of "objects," which can contain data (attributes) and code (methods). Python supports OOP principles such as encapsulation, inheritance, and polymorphism.

### **Class & Object in Python**
---
Class is a blueprint for creating objects.

```python
#create class
class Student:
  name = "Mr. Rahim"

#creating object(instance)
s1 = Student()
print(s1.name)
```

</details>