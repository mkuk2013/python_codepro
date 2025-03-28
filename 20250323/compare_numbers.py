# Task: Compare the values of three different variables using > and <

# Get inputs from the user
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

# Check if all three numbers are equal
if a == b == c:
    print("All three numbers are equal.")
else:
    # Check if two numbers are equal
    if a == b:
        print(f"{a} and {b} are the same.")
    if a == c:
        print(f"{a} and {c} are the same.")
    if b == c:
        print(f"{b} and {c} are the same.")

    # Determine the largest number
    if a > b and a > c:
        print(f"{a} is the largest number.")
    elif b > a and b > c:
        print(f"{b} is the largest number.")
    else:
        print(f"{c} is the largest number.")