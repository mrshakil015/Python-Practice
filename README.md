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

</details>
