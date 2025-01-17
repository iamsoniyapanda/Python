
#1-1/2+1/3-1/4+………………………………………………..
# Function to calculate the sum of the series 1 - 1/2 + 1/3 - 1/4 + ... for n terms
def sum_series(n):
    total = 0  # Initialize total to 0
    for i in range(1, n + 1):
        # Alternate the sign by checking if the index i is odd or even
        if i % 2 == 1:
            total += 1 / i  # Add for odd i (positive term)
        else:
            total -= 1 / i  # Subtract for even i (negative term)
    return total

# Input from user for the value of n (number of terms)
n = int(input("Enter the number of terms: "))

# Calculate and print the result
result = sum_series(n)
print(f"The result of the series 1 - 1/2 + 1/3 - 1/4 + ... for n={n} is: {result}")
