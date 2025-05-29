a, b = 4, 6
lcm = max(a, b)
while True:
    if lcm % a == 0 and lcm % b == 0:
        print("LCM is", lcm)
        break
    lcm += 1
