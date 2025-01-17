#Find the nth term 1,1,2,6,24,………………………………
import math

# Function to calculate the nth term of the sequence (factorial)
def find_nth_term(n):
    return math.factorial(n)

# Input from user for the value of n
n = int(input("Enter the value of n: "))

# Find the nth term
nth_term = find_nth_term(n)
print(f"The {n}th term in the factorial series is: {nth_term}")
