#1+x+x^2+x^3+……………………………………+x^n
# Function to calculate the sum of the series 1 + x + x^2 + x^3 + ... + x^n
def sum_series(x, n):
    total = 0  # Initialize total to 0
    for i in range(n + 1):
        total += x ** i  # Add the current term x^i
    return total

# Input from user for the value of x and n
x = float(input("Enter the value of x: "))  # x can be any real number
n = int(input("Enter the value of n: "))    # n should be a non-negative integer

# Calculate and print the result
result = sum_series(x, n)
print(f"The result of the series 1 + x + x^2 + x^3 + ... + x^{n} is: {result}")
