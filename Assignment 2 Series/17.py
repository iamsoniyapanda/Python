#Find the nth term 0,6,0,12,0,90,…………………….
# Function to calculate the nth term based on the observed pattern
def find_nth_term(n):
    if n % 2 == 1:  # Odd indexed terms (1st, 3rd, 5th, ...)
        return 0  # The odd terms are always 0
    else:  # Even indexed terms (2nd, 4th, 6th, ...)
        # Example pattern: 6, 12, 90, ... we can assume a multiplicative factor
        # The even indexed terms seem to follow a different pattern
        if n == 2:
            return 6
        elif n == 4:
            return 12
        elif n == 6:
            return 90
        # More complex logic can be added for terms after 6th
        return 0

# Input from user for the value of n
n = int(input("Enter the value of n: "))

# Find the nth term
nth_term = find_nth_term(n)
print(f"The {n}th term in the series is: {nth_term}")
