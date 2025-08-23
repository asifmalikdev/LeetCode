import re
text = "hello world"

print(re.match("hello", text))  
print(re.match("world", text))   
print("---------------------------------------------------------")

text = "hello world"
print(re.search("world", text))   # ✅ Match at position 6
