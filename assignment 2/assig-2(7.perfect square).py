import math
n = int(input("Enter number: "))
print("Perfect square" if math.isqrt(n)**2 == n else "Not perfect square")
