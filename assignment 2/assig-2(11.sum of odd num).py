nums = list(map(int, input("Enter numbers: ").split()))
print("Sum of odds:", sum(n for n in nums if n % 2 != 0))
