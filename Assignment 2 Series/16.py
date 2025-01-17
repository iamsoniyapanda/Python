#Find the nth term 5,13,25,41,61,…………………….
# Function to calculate the nth term of the sequence
def find_nth_term(n):
    # The quadratic formula derived from the system of equations is:
    # a_n = 2n^2 + 3n
    return 2 * n**2 + 3 * n

# Input from user for the value of n
n = int(input("Enter the value of n: "))

# Find the nth term
nth_term = find_nth_term(n)
print(f"The {n}th term in the series is: {nth_term}")
