import re
pwd = input("Enter password: ")
if len(pwd) >= 8 and re.search(r"\d", pwd) and re.search(r"[A-Za-z]", pwd):
    print("Valid password")
else:
    print("Invalid password")
