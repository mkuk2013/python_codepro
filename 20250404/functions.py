# 1️⃣ Basic Function Creation
def welcome():
    print("Welcome to Python Programming!")

# 2️⃣ Function with Parameters
def multiply(a, b):
    return a * b

# 3️⃣ Function to Check Even or Odd
def is_even(n):
    return n % 2 == 0

# 4️⃣ Factorial Function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# 5️⃣ Reverse a String
def reverse_string(s):
    return s[::-1]

# 6️⃣ Use map() with Lambda
numbers = [2, 4, 6, 8]
squared_numbers = list(map(lambda x: x ** 2, numbers))

# 7️⃣ Find the Maximum Using reduce()
from functools import reduce
numbers = [3, 7, 1, 9, 2]
max_number = reduce(lambda a, b: a if a > b else b, numbers)

# Test the functions
welcome()
print(multiply(5, 3))
print(is_even(4), is_even(7))
print(factorial(5))
print(reverse_string("Python"))
print(squared_numbers)
print(max_number)



#  Homework Challenge
# 🔹 Write a function that takes a list of numbers and returns the sum of only the even numbers.



def sum_of_evens(numbers):
    return sum(filter(lambda num: num % 2 == 0, numbers))

# Test the function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum_of_evens(numbers))  # Output: 30 (2 + 4 + 6 + 8 + 10)