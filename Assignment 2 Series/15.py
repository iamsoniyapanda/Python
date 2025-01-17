#Find the nth term 1,8,54,384,…………………………..
# Function to calculate the nth term based on the observed pattern
def find_nth_term(n):
    # Example formula: nth term is n^(n) times some scaling factor
    return n ** n  # Start with n^n pattern

# Input from user for the value of n
n = int(input("Enter the value of n: "))

# Find the nth term
nth_term = find_nth_term(n)
print(f"The {n}th term in the series is: {nth_term}")
