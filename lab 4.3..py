#Generate code for take user input and check wheather it is leap year are not
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

year = int(input("Enter a year: "))
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

#TASK2
#generate code for taking user input and converting centimeters to inches use correct mathematical formula like example:1 cm = 0.393701 inches

def cm_to_inches(cm):
    inches = cm * 0.393701
    return inches

cm = float(input("Enter length in centimeters: "))
inches = cm_to_inches(cm)
print(f"Length in inches: {inches}")


# Generate code for taking user input full name and print format first,last examples like "John Smith" → "Smith, John" and "Anita Rao" → "Rao, Anita"
# Taking user input for full name
full_name = input("Enter your full name (first last): ")                                                                        
# Splitting the full name into first and last names
first_name, last_name = full_name.split()   
# Formatting and printing the name in "Last, First" format
formatted_name = f"{last_name}, {first_name}"
print(formatted_name)
# Example usage:
# Input: John Smith → Output: Smith, John                   
# Input: Anita Rao → Output: Rao, Anita

# Generate code for taking user input full name and print format first,last examples like "John Smith" → "Smith, John" and "Anita Rao" → "Rao, Anita"
# Taking user input for full name
full_name = input("Enter your full name (first last): ")                                                                        
# Splitting the full name into first and last names
first_name, last_name = full_name.split()   
# Formatting and printing the name in "Last, First" format
formatted_name = f"{last_name}, {first_name}"
print(formatted_name)
# Example usage:
# Input: John Smith → Output: Smith, John                   
# Input: Anita Rao → Output: Rao, Anita

# Generate code for user input string and count the number of vowels in it
# Taking user input for a string    
#user_input = input("Enter a string: ")                                                                        
# Defining a function to count vowels in the input string   
#def count_vowels(input_string): 
   # vowels = "aeiouAEIOU"
   #for char in input_string:
        #if char in vowels:

         #   count += 1
    #return count
# Counting vowels in the user input string
#vowel_count = count_vowels(user_input)      
# Printing the number of vowels found
#print(f"Number of vowels in the input string: {vowel_count}")
# Taking user input for a string    
user_input = input("Enter a string: ")                                                                        
# Defining a function to count vowels in the input string
def count_vowels(input_string): 
    vowels = "aeiouAEIOU"
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count
# Counting vowels in the user input string
vowel_count = count_vowels(user_input)
# Printing the number of vowels found
print(f"Number of vowels in the input string: {vowel_count}")
# Example usage:    
# Input: apple → Output: 2                   
# Input: Orange → Output: 3

#Generate code for function that reads a text file and returns the number of lines in the file.
def count_lines(filename):
    with open(filename, 'r') as file:
        return sum(1 for line in file)  
# Example usage:
# Assuming 'example.txt' is a text file in the same directory   
line_count = count_lines('example.txt')
print(f"Number of lines in the file: {line_count}") 
# Example usage:    
# If 'example.txt' contains 5 lines → Output: 5