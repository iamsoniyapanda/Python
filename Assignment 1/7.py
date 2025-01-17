 1
1 1
1 2 1
1 3 3 1


n = 4
for i in range(n):
  print(" " * (n - i - 1), end="")
    
    number = 1  
    for j in range(i + 1):
        print(number, end=" ")
        number = number * (i - j) // (j + 1)
    print()
