import cmath
a, b, c = map(float, input("Enter a, b, c: ").split())
d = cmath.sqrt(b**2 - 4*a*c)
print("Roots:", (-b + d)/(2*a), "and", (-b - d)/(2*a))
