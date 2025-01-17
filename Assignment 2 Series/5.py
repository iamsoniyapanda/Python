#1*3+3*5+………………………………………………….
# Function to calculate the sum of the series 1*3 + 3*5 + 5*7 + ... + (2n-1)*(2n+1)
def sum_series(n):
    total = 0  # Initialize total to 0
    for i in range(1, n + 1):
        total += (2 * i - 1) * (2 * i + 1)  # Add the term (2n-1)*(2n+1)
    return total

# Input from user for the value of n (number of terms)
n = int(input("Enter the number of terms (n): "))

# Calculate and print the result
result = sum_series(n)
print(f"The result of the series 1*3 + 3*5 + ... for n={n} is: {result}")
