def tes(a):
    print(id(a))
    a = a+5
    print(id(a))

a = 4
print(id(a))
tes(a)