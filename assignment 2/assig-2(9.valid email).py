import re
email = input("Enter email: ")
print("Valid email" if re.match(r"[^@]+@[^@]+\.[^@]+", email) else "Invalid email")
