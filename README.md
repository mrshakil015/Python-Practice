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
