class Solution(object):
    def wordPattern(self, pattern, s):
        s = s.split()

        if len(pattern) != len(s):
            return False
        dict1 = {}
        for i in range(len(pattern)):
            if pattern[i] in dict1:
                if dict1[pattern[i]]  != s[i]:
                    return False
            else:
                if s[i] in dict1.values():
                    return False
                dict1[pattern[i]] = s[i]

        list1 = []
        for i in pattern:
            list1.append(dict1[i])

        return True if s==list1 else False

obj = Solution()
s = "dog cat cat dog"
p = "aaaa"
print(obj.wordPattern(p,s))

class A:
    def __init__(self):
        print("-> Entering A")
        print("<- Leaving A")

class B(A):
    def __init__(self):
        print("-> Entering B")
        super().__init__()  # Who does this call? Let's trace it!
        print("<- Leaving B")

class C(A):
    def __init__(self):
        print("-> Entering C")
        super().__init__()
        print("<- Leaving C")

class D(B,C):
    def __init__(self):
        print("-> Entering D")
        super().__init__()
        print("<- Leaving D")

# --- Execution ---
print("--- Printing the MRO of Class D ---")
for cls in D.__mro__:
    print(cls.__name__)

print("\n--- Instantiating Object D ---")
d_instance = D()
