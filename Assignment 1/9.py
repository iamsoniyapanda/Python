    *                    
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    * 

n = 5
for i in range(n):
    
    print(" " * (n - i - 1), end="")
    print("*", end="")
    if i != 0 and i != n - 1:
        print(" " * (2 * i - 1), end="")
    if i != 0 and i != n - 1:
        print("*", end="")
    print()

for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1), end="")
    
    print("*", end="")

    if i != 0:
        print(" " * (2 * i - 1), end="")

    if i != 0:
        print("*", end="")

    print()


