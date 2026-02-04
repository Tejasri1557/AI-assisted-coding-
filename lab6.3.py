#create a python class named Student 
class Student:
    #initialize the class with name and age attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #method to display student details
    def display_details(self):
        print(f"Name: {self.name}, Age: {self.age}")
#create an instance of the Student class
student1 = Student("Alice", 20)
#call the display_details method to show student information
student1.display_details()
#add attibutes name,roll no,branch
student1.roll_no = "101"
student1.branch = "Computer Science"
#print the new attributes
print(f"Roll No: {student1.roll_no}, Branch: {student1.branch}")
#use __init__ to initialize attributes
student2 = Student("Bob", 22)
student2.roll_no = "102"
student2.branch = "Mechanical Engineering"
student2.display_details()
print(f"Roll No: {student2.roll_no}, Branch: {student2.branch}")
#add display_details() to print student info
student2.display_details()
print(f"Roll No: {student2.roll_no}, Branch: {student2.branch}")
student2.display_details()
#create on student object 
student3 = Student("Charlie", 21)
student3.roll_no = "103"
student3.branch = "Electrical Engineering"
student3.display_details()
print(f"Roll No: {student3.roll_no}, Branch: {student3.branch}")
#call display_details() method 
student3.display_details()
print(f"Roll No: {student3.roll_no}, Branch: {student3.branch}")


#task2
# Write a Python function that prints the first 10 multiples of a given number using a for loop.The number should be taken as user input.
def print_multiples():
    num = int(input("Enter a number: "))
    print(f"The first 10 multiples of {num} are:")
    for i in range(1, 11):
        print(num * i)
print_multiples()

# Write the same program to print the first 10 multiples of a given number,use a while loop
def print_multiples_while():
    num = int(input("Enter a number: "))
    print(f"The first 10 multiples of {num} are:")
    count = 1
    while count <= 10:
        print(num * count)
        count += 1
print_multiples_while()

#task 3
#Write a Python function to classify a person's age into groups: child, teenager, adult, and senior.
def classify_age():
    age = int(input("Enter the person's age: "))
    if age < 13:
        print("The person is a child.")
    elif 13 <= age < 20:
        print("The person is a teenager.")
    elif 20 <= age < 60:
        print("The person is an adult.")
    else:
        print("The person is a senior.")
classify_age()

#generate the same classification using alternative conditional structures (e.g.,simplified conditions or dictionary-based logic)
def classify_age_alternative():
    age = int(input("Enter the person's age: "))
    age_groups = {
        range(0, 13): "child",
        range(13, 20): "teenager",
        range(20, 60): "adult",
        range(60, 150): "senior"
    }
    for age_range, group in age_groups.items():
        if age in age_range:
            print(f"The person is a {group}.")
            break
classify_age_alternative()

#task 4:
#Generate a Python function sum_to_n(n) that finds the sum of the first n natural numbers using a for loop.
def sum_to_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
n = int(input("Enter a natural number n: "))
print(f"The sum of the first {n} natural numbers is: {sum_to_n(n)}")
#Generate the same sum using a while loop
def sum_to_n_while(n):
    total = 0
    count = 1
    while count <= n:
        total += count
        count += 1
    return total
n = int(input("Enter a natural number n: "))
print(f"The sum of the first {n} natural numbers is: {sum_to_n_while(n)}")
#Generate the same sum using the formula n(n+1)/2
def sum_to_n_formula(n):
    return n * (n + 1) // 2
n = int(input("Enter a natural number n: "))
print(f"The sum of the first {n} natural numbers is: {sum_to_n_formula(n)}")

#task5:
#Write a Python BankAccount class with deposit(), withdraw(), and check_balance() methods
class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def check_balance(self):
        print(f"Current balance: ${self.balance}")
# Create an instance of BankAccount
account = BankAccount(100)  # Initial balance of $100
account.check_balance()
account.deposit(50)
account.check_balance()
account.withdraw(30)
account.check_balance()
account.withdraw(150)  # Attempt to withdraw more than the balance
account.check_balance()
# Demonstrate the functionality of each method
account.deposit(-20)  # Attempt to deposit a negative amount
account.check_balance()
account.withdraw(50)
account.check_balance()
account.deposit(200)
account.check_balance()
account.withdraw(100)
account.check_balance()



