#1*2*3+2*3*4+……………………………….+n*(n+1)*(n+2)
# Function to calculate the sum of the series 1*2*3 + 2*3*4 + 3*4*5 + ... + n*(n+1)*(n+2)
def sum_series(n):
    total = 0  # Initialize total to 0
    for i in range(1, n + 1):
        total += i * (i + 1) * (i + 2)  # Add the current term i*(i+1)*(i+2)
    return total

# Input from user for the value of n (number of terms)
n = int(input("Enter the value of n: "))

# Calculate and print the result
result = sum_series(n)
print(f"The result of the series 1*2*3 + 2*3*4 + ... for n={n} is: {result}")
