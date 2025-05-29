s = "madam"
rev = ''
for char in s:
    rev = char + rev
print("Palindrome" if s == rev else "Not Palindrome")
