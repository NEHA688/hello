# Function to find the greatest of three numbers
def find_greatest(a, b, c):
    greatest = max(a, b, c)
    return greatest

# Taking input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Finding and displaying the greatest number
greatest = find_greatest(num1, num2, num3)
print(f"The greatest number is: {greatest}")
# This is my second repo
