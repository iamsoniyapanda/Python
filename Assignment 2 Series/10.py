#Find the nth term 2,4,3,4,15,…………………………
  # Function to calculate the nth term based on the observed pattern
def find_nth_term(n):
    if n % 2 == 0:
        return 4  # For even-indexed terms, return 4
    else:
        # For odd-indexed terms, return based on some multiplication pattern
        if n == 1:
            return 2  # The first term is 2
        elif n == 3:
            return 3  # The third term is 3
        else:
            # For higher odd-indexed terms, multiply previous odd-indexed terms
            return (n - 1) * (n - 2)

# Input from user for the value of n
n = int(input("Enter the value of n: "))

# Find the nth term
nth_term = find_nth_term(n)
print(f"The {n}th term in the series is: {nth_term}")
