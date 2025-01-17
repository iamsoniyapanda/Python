#1+2+11+26+47+……………………………………………..
# Function to calculate the nth term based on the quadratic pattern
def generate_series(n):
    series = []
    for i in range(1, n + 1):
        term = 3 * i * i - 2 * i + 0  # Using the derived formula
        series.append(term)
    return series

# Input from user for the number of terms
n = int(input("Enter the number of terms: "))

# Generate the series and print it
series = generate_series(n)
print("The series is:", series)
