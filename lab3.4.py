#task-01:Zero shot prompt-Fibbonocci series 
#write a python function to print the first n fibonocci numbers 
def fibonacci(n):
    a, b = 0, 1
    fib_sequence = []
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence
n = int(input("Enter the number of terms: "))
print("Fibonacci series:", fibonacci(n))

#task 2:one shot prompt-List reversal function
#write a python code to reverse list using slicing or loop
def reverse_list(lst):
    return lst[::-1]  # Using slicing to reverse the list
input_list = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
reversed_list = reverse_list(input_list)
print("Reversed list:", reversed_list)

#task 3:Few shot prompt-String pattern matching 
#write a python code for how to check if a string starts with a capital letter and ends with a period
def check_string_pattern(s):
    starts_with_capital = s[0].isupper() if s else False
    ends_with_period = s.endswith('.') if s else False
    return starts_with_capital, ends_with_period

input_string = input("Enter a string: ")
starts_with_capital, ends_with_period = check_string_pattern(input_string)
print(f"Starts with capital letter: {starts_with_capital}")
print(f"Ends with period: {ends_with_period}")

#task 4:zero shot vs few shot-Email validator 
#write a python code to write an email validation function using zero shot 
import re
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None
email_input = input("Enter an email address: ")

if is_valid_email(email_input):
    print("Valid email address")
else:
    print("Invalid email address")
#write a python code to write an email validation function using few shot
import re
def validate_email(email):
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(email_pattern, email):
        return True
    else:
        return False
email_to_check = input("Enter an email address: ")
if validate_email(email_to_check):
    print("The email address is valid.")
else:
    print("The email address is invalid.")

#task5:prompt tuning-summing digits of a number 
#Prompt Style 1: Generic Task Prompt
#Write a Python function named sum_of_digits that takes an integer as input and returns the sum of its digits. The function should handle positive integers and return an integer result.
def sum_of_digits(num):
    return sum(int(digit) for digit in str(abs(num)))
number = int(input("Enter an integer: "))
result = sum_of_digits(number)
print("Sum of digits:", result)
#Prompt Style 2: Task + Input/Output
#Write a Python function called sum_of_digits(n) that calculates the sum of the digits of a given number
def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))
number = int(input("Enter an integer: "))
result = sum_of_digits(number)
print("Sum of digits:", result)
