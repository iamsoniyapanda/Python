#11+2!+3!+…………….+n!
import math
def sum_factorials(n):
    total = 11 
    for i in range(2, n + 1):
        total += math.factorial(i)  
    return total

# Input from user for the value of n
n = int(input("Enter the value of n: "))

# Calculate and print the result
result = sum_factorials(n)
print(f"The result of 11 + 2! + 3! + ... + {n}! is: {result}")
