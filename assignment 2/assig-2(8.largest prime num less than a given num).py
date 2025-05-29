def is_prime(n):
    return all(n % i != 0 for i in range(2, int(n**0.5)+1)) and n > 1

n = int(input("Enter number: "))
for i in range(n-1, 1, -1):
    if is_prime(i):
        print("Largest prime less than", n, "is", i)
        break
