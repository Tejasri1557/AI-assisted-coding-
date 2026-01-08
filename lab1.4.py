#write a program to check whether the given number is prime or not without using functions 
#task-01
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")


#task 2
#generate optimized version of code to check whether the given number is prime or not using functions
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
number = int(input("Enter a number: "))
if is_prime(number):
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")


#generate fibonocci series using iterative functions in a given range
def fibonacci_iterative(n):
    seq = []
    a, b = 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq
terms_iterative = int(input("Enter the number of terms for Fibonacci series (iterative): "))
print("Fibonacci series (iterative):", fibonacci_iterative(terms_iterative))


#generate fibonocci series using recursive functions in a given range
def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seq = fibonacci_recursive(n - 1)
        seq.append(seq[-1] + seq[-2])
        return seq
terms_recursive = int(input("Enter the number of terms for Fibonacci series (recursive): "))
print("Fibonacci series (recursive):", fibonacci_recursive(terms_recursive))






