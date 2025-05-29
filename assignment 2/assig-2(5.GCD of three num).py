import math
a, b, c = map(int, input("Enter three numbers: ").split())
print("GCD:", math.gcd(math.gcd(a, b), c))
