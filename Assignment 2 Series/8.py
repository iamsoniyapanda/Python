#1-x^2/2!+x^4/4!+…………………………………………….
import math

# Function to calculate the sum of the series 1 - x^2/2! + x^4/4! - x^6/6! + ... for n terms
def sum_series(x, n):
    total = 1  # Initialize total to 1 (the first term in the series)
    for i in range(1, n + 1):
        # Calculate the power of x and factorial for the current term
        exponent = 2 * i  # Exponent: 2, 4, 6, 8, ...
        factorial = math.factorial(exponent)  # Factorial: 2!, 4!, 6!, ...
        term = (x ** exponent) / factorial  # Current term: x^exponent / factorial
        if i % 2 == 0:
            total -= term  # Subtract for even i (negative term)
        else:
            total += term  # Add for odd i (positive term)
    return total

# Input from user for the value of x and n
x = float(input("Enter the value of x: "))  # x can be any real number
n = int(input("Enter the number of terms: "))  # n should be a positive integer

# Calculate and print the result
result = sum_series(x, n)
print(f"The result of the series 1 - x^2/2! + x^4/4! - x^6/6! + ... for x={x} and n={n} is: {result}")
