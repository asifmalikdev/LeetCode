text = "  hello, Python 123!  "

# 1. Case Conversion
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title:", text.title())
cap = "hello asif malik"
cap = cap.capitalize()
print("Capitalize:", text.capitalize(), cap)
print("Swapcase:", text.swapcase())
print("-" * 40)

# 2. Searching & Finding
print("Find 'Python':", text.find("Python"))
print("rFind 'o':", text.rfind("o"))
print("Count 'o':", text.count("o"))
print("Index 'Python':", text.index("Python"))
print("-" * 40)

# 3. Checking Content
sample = "Python123"
print("isalnum:", sample.isalnum())
print("isalpha:", "Python".isalpha())
print("isdigit:", "12345".isdigit())
print("isspace:", "   ".isspace())
print("islower:", "python".islower())
print("isupper:", "PYTHON".isupper())
print("istitle:", "Python Is Fun".istitle())
print("-" * 40)
text = "hello Python this is Python in parallel Python"
# 4. Modifying & Replacing
print("Replace 'Python' with 'World':", text.replace("Python", "World"))
print("Strip whitespace:", text.strip())
print("Left Strip:", text.lstrip())
print("Right Strip:", text.rstrip())
print("-" * 40)

# 5. Splitting & Joining
print("Split by space:", text.split())
print("Split by comma:", text.split(","))
print("Splitlines:", "Hello\nWorld".splitlines())
words = ["Python", "is", "fun"]
print("Join words with '-':", " ".join(words))
print("-" * 40)

# 6. Formatting
name = "Asif"
age = 25
print("Format:", "My name is {} and I am {} years old.".format(name, age))
print("Format Map:", "Name: {name}, Age: {age}".format_map({"name": name, "age": age}))
print("zfill:", "42".zfill(5))
print("center:", "Python".center(20, "*"))
print("ljust:", "Python".ljust(20, "-"))
print("rjust:", "Python".rjust(20, "-"))
print("-" * 40)

# 7. Encoding & Decoding
encoded = text.encode()
print("Encoded:", encoded)
print("Decoded:", encoded.decode())
