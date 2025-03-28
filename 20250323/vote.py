# Task: Use >= to check if a person is eligible to vote (age >= 18).

age = int(input('Type your age: '))

if age >= 18:
    print(f"Your age is {age}, and you're eligible to vote.")
else:
    print(f"Your age is {age}, and you're not eligible to vote.")
