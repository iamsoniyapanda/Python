// Find the nth term a,b,b,c,c,c,……………………
# Function to find the nth term based on the observed pattern
def find_nth_term(n):
    # Initialize the letter counter and the count of occurrences
    letter = ord('a')  # Start with letter 'a' (ASCII value of 'a' is 97)
    count = 1  # The first letter appears 1 time
    
    # Loop to find the nth term
    while n > count:
        n -= count  # Subtract the number of occurrences of the current letter
        count += 1  # Increment the count for the next letter
        letter += 1  # Move to the next letter
    
    # Return the letter corresponding to the nth term
    return chr(letter)

# Input from user for the value of n
n = int(input("Enter the value of n: "))

# Find the nth term
nth_term = find_nth_term(n)
print(f"The {n}th term in the series is: {nth_term}")
