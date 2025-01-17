#1/1!+2/2!+3/3!+…………+n/n!
import math

# Function to calculate the sum of the series 1/1! + 2/2! + ... + n/n!
def sum_series(n):
    total = 0  # Initialize total to 0
    for i in range(1, n + 1):
        total += i / math.factorial(i)  # Add the current term i/i!
    return total

# Input from user for the value of n
n = int(input("Enter the value of n: "))

# Calculate and print the result
result = sum_series(n)
print(f"The result of the series 1/1! + 2/2! + 3/3! + ... + {n}/{n}! is: {result}")
