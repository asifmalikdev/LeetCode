def mystery_function(x):
    print(x)
    return x if x > 0 else mystery_function(-x)

result = mystery_function(-5)
print(result)
x = -5
print(-x)
def outer_function(x):
    def inner_function():
        return x + 1
    return inner_function

closure = outer_function(5)
print(type(closure))
result = closure()
print(type(result))
print(result)




def mysterious_function(a, b=[]):
    b.append(a)
    print("b is ",b)
    return b

result1 = mysterious_function(1)
print("result 1", result1, id(result1))
result2 = mysterious_function(2)
print("result 2", result2, id(result2))
print("result 1", result1)
result3 = mysterious_function(3)
print("result 3", result3, id(result3))
print(result1 + result2 + result3)








def some_function(*args, **kwargs):
    print(args,kwargs)
    return args, kwargs

result = some_function(1, 2, a=3, b=4)
print(result)







x = [1, 2, 3]
y = x *2
print(x,y)






x = [1, 2, 3]
y = x + [4, 5]
z = x.extend([4, 5])
print(x, y, z)

x = 6
y = 6
print(x is y)




class ABC():
    def __init__(self,name,salary):
        self.name1 = name
        self.salary1 = salary

p1 = ABC("ASIF",5000)
print(p1.name1)
