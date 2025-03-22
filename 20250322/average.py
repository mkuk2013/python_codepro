# Task : 5 Write an expression that calculates the average of three numbers.

num1 = int(input('Write first number: '))
num2 = int(input('Write second number: '))
num3 = int(input('Write third number: '))

# Formula for calculating the average of 3 numbers
result = (num1 + num2 + num3) / 3  

# Using :.2f to display the result with 2 decimal places
print(f'The average of {num1}, {num2}, and {num3} is {result:.2f}')