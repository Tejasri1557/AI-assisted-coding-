# Create method to display student details with attributes name,roll number,marks,pass or fail based on marks
class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display_details(self):
        status = "Pass" if self.marks >= 40 else "Fail"
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Marks: {self.marks}")
        print(f"Status: {status}")
# Example usage
student1 = Student("Alice", 101, 85)
student2 = Student("Bob", 102, 35)
student1.display_details()
student2.display_details()
#Create method to compare marks with class average using if-else
class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display_details(self):
        status = "Pass" if self.marks >= 40 else "Fail"
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Marks: {self.marks}")
        print(f"Status: {status}")

    def compare_with_average(self, average_marks):
        if self.marks > average_marks:
            print(f"{self.name} has above average marks.")
        elif self.marks < average_marks:
            print(f"{self.name} has below average marks.")
        else:
            print(f"{self.name} has average marks.")
# Example usage
student1 = Student("Alice", 101, 85)
student2 = Student("Bob", 102, 35)
average_marks = 60
student1.display_details()
student1.compare_with_average(average_marks)
student2.display_details()
student2.compare_with_average(average_marks)

#TASK 2 
# Check if number is even using for loop if even print their squares 
for num in range(1, 11):
    if num % 2 == 0:
        print(f"{num} is even. Its square is {num ** 2}.")

#TASK3 
#create a python class for bankaccount with methods to deposit,withdraw and check balance
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def check_balance(self):
        print(f"Account holder: {self.account_holder}. Current balance: {self.balance}")
# Example usage
account = BankAccount("John Doe", 1000)
account.check_balance()
account.deposit(500)
account.withdraw(200)
account.check_balance()


#TASK4
#Define a list of dictionaries where each dictionary represents a student with name,score using while loop
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 35},
    {"name": "Charlie", "score": 60},
    {"name": "David", "score": 45}
]
index = 0
while index < len(students):
    student = students[index]
    print(f"Name: {student['name']}, Score: {student['score']}")
    index += 1
#print names of student who scored more than 75
print("Students who scored more than 75:")
index = 0
while index < len(students):
    student = students[index]
    if student['score'] > 75:
        print(student['name'])
    index += 1

#TASK5 
#writing a Python class named ShoppingCart with:An empty list to store items (each item may include name, price,quantity)
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price, quantity):
        self.items.append({"name": name, "price": price, "quantity": quantity})
        print(f"Added {quantity} of {name} at ${price} each to the cart.")
    def remove_item(self, name):
        self.items = [item for item in self.items if item['name'] != name]
        print(f"Removed {name} from the cart.")
    def view_cart(self):
        print("Shopping Cart Items:")
        for item in self.items:
            print(f"{item['quantity']} of {item['name']} at ${item['price']} each")
    def calculate_total(self):
        total = sum(item['price'] * item['quantity'] for item in self.items)
        print(f"Total cost: ${total}")
        return total
# Example usage
cart = ShoppingCart()
cart.add_item("Apple", 1.0, 5)
cart.add_item("Banana", 0.5, 10)
cart.view_cart()
cart.calculate_total()
cart.remove_item("Apple")
cart.view_cart()
cart.calculate_total()
# Methods to add items, remove items, view cart, and calculate total bill using a loop ,apply conditional discounts (e.g., discount if total exceeds acertain amount)
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price, quantity):
        self.items.append({"name": name, "price": price, "quantity": quantity})
        print(f"Added {quantity} of {name} at ${price} each to the cart.")

    def remove_item(self, name):
        self.items = [item for item in self.items if item['name'] != name]
        print(f"Removed {name} from the cart.")

    def view_cart(self):
        print("Shopping Cart Items:")
        for item in self.items:
            print(f"{item['quantity']} of {item['name']} at ${item['price']} each")

    def calculate_total(self):
        total = sum(item['price'] * item['quantity'] for item in self.items)
        if total > 100:
            discount = total * 0.1  # 10% discount
            total -= discount
            print(f"Applied discount of ${discount:.2f}")
        print(f"Total cost: ${total:.2f}")
        return total
# Example usage
cart = ShoppingCart()
cart.add_item("Apple", 1.0, 50)
cart.add_item("Banana", 0.5, 200)
cart.view_cart()
cart.calculate_total()
cart.remove_item("Apple")
cart.view_cart()
cart.calculate_total()
    