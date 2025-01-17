#Find the nth term 14,28,20,40,…………………………….
# Function to calculate the nth term based on the observed pattern
def find_nth_term(n):
    if n % 2 == 1:  # Odd indexed terms (1st, 3rd, 5th, ...)
        return 14 + 6 * ((n - 1) // 2)  # For odd indexed terms, increases by 6
    else:  # Even indexed terms (2nd, 4th, 6th, ...)
        return 28 + 12 * ((n - 1) // 2)  # For even indexed terms, increases by 12

# Input from user for the value of n
n = int(input("Enter the value of n: "))

# Find the nth term
nth_term = find_nth_term(n)
print(f"The {n}th term in the series is: {nth_term}")
