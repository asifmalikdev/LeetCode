from collections import Counter

words = "hello asif this is me".split()
print("printing first time",words)
freq = {}
words = "".join(words)
print("printing second time",words)
for letter in words:
    freq[letter] = freq.get(letter, 0) + 1
print(freq)

# for word in words:

    
# Using curly braces
d = {"a": 1, "b": 2}

# Using dict() constructor
d2 = dict(x=10, y=20, c = 1)

print(d, d2, id(d2["c"]), id(d["a"]))
d2=d2|d
print(d2)