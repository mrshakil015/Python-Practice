def prime_number(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print(f"It's a prime number")
    else:
        print(f"It's not prime number")
number = int(input("Enter an number: "))
prime_number(number)