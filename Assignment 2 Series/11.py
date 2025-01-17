#Find the nth term 3,5,33,35,53,……………………..
# Function to calculate the nth term based on the observed pattern
def find_nth_term(n):
    if n % 2 == 1:  # Odd indexed terms
        # For odd-indexed terms, the pattern is 3, 33, 53, ...
        return 3 + 30 * ((n - 1) // 2)
    else:  # Even indexed terms
        # For even-indexed terms, the pattern is 5, 35, 65, ...
        return 5 + 30 * ((n - 1) // 2)

# Input from user for the value of n
n = int(input("Enter the value of n: "))

# Find the nth term
nth_term = find_nth_term(n)
print(f"The {n}th term in the series is: {nth_term}")
