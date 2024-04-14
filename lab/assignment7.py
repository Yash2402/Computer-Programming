# Concatenation
print("Concatenation: ")
first_name = "Yash"
last_name = "Sharma"

full_name = first_name + " " + last_name
print(full_name)

e = "e"
print("'e' * 3 =", e * 3)
print("'e' + 'e' =", e + e)
print()

# Slicing
print("Slicing: ")
string = "This is an example string"
print("string[start(default = 0):stop(not included):step(default = 1)]")
print("string[:4] =", string[:4])
print("string[2:9] =", string[2:9])
print("string[::2] =", string[::2])
print("string[4::3] =", string[4::3])
print("string[::-1] =", string[::-1])
print("string[::] =", string[::])
print()

# Splitting
print("Splitting: ")
string = "This is an example string"
l1 = string.split()
l2 = string.split("i")
print("string.split() =", l1)
print("string.split('i') =", l2)
print()

# Casing
print("Casing: ")
string = "tHis Is aN eXaMple sTRIng"
title_string = string.title()
upper_string = string.upper()
lower_string = string.lower()
swapcase_string = string.swapcase()
print("original string =", string)
print("string.title() =", title_string)
print("string.upper() =", upper_string)
print("string.lower() =", lower_string)
print("string.swapcase() =", swapcase_string)
print()

# Translation
print("Uses a dictionary with ascii codes to replace 83 (S) with 80 (P):")
mydict = {83: 80}
txt = "Hello Sam!"

print(txt, "----->", txt.translate(mydict))
print()


print("Regex: ")
import re


def validate_email(email):
    # Regular expression pattern for basic email validation
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    # Compile the pattern
    regex = re.compile(pattern)
    # Match the email against the pattern
    if regex.match(email):
        return True
    else:
        return False


# Test the function
emails = [
    "example@example.com",
    "user.name@example.co.jp",
    "user@domain-with-dash.com",
    "user123@example123.co.uk",
    "invalid-email.com",
    "user@example.",
    "@example.com",
    "user@example",
    "user@.com",
]

for email in emails:
    print(f"{email}: {validate_email(email)}")
