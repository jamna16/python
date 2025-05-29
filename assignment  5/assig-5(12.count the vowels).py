s = "hello world"
count = 0
for char in s:
    if char in 'aeiouAEIOU':
        count += 1
print("Vowel count:", count)
