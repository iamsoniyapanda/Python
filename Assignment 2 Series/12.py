#Find the nth term 0,0,2,1,4,2,6,3,8……………………….
# Function to calculate the nth term based on the observed pattern
def find_nth_term(n):
    if n % 2 == 1:  # Odd indexed terms (1st, 3rd, 5th, ...)
        return 2 * ((n - 1) // 2)  # Even numbers starting from 0
    else:  # Even indexed terms (2nd, 4th, 6th, ...)
        return (n // 2) - 1  # Natural numbers starting from 0

# Input from user for the value of n
n = int(input("Enter the value of n: "))

# Find the nth term
nth_term = find_nth_term(n)
print(f"The {n}th term in the series is: {nth_term}")
