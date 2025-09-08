
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)
print(x is y) 

a, b, c = [1, 2, 3]
print(a, b, c)

a = [1, 2, 3]
b = a * 2
print(b)

exapmle_dict = dict()
print(exapmle_dict)

def myFun(arg1, arg3, **kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


my_dict = {'arg1':1, 'arg2': 2}
myFun(**my_dict, arg3=3)


list3=[1,2,3,4,5,6]
print(id(list3))
list1 = [1, 2, 3]
list2 = [4, 5, 6]

list3 = list1 + list2
print(list3)   # [1, 2, 3, 4, 5, 6]
print(id(list3))
print(id([1,2,3,4,5,6]))


x = 201
class solution():
    x  = 10
    print(x)
    def prac(self):
        print("hello")
        for _ in range(10):
            self.x+=1  
    print("after",x)

obj  = solution()
print("after class object and before function")
obj.prac()
print(x)

my_dict = {"a": 1, "b": 2, "c": 3}

keys = my_dict.values()
print(keys)

print(my_dict["a"])
print(my_dict.get("d", 99))

my_dict["d"] = 768

print(my_dict)

my_dict = {"a": 1, "b": 2, "c": 3}
my_dict["some_key"] = None
print(my_dict)

for key,value in my_dict.items():
    print(key, value)


print(my_dict.pop(1,89))


x = [1, 2, 3]
y = x
y[0] = 10
print(id(x), id(y))

y = list(x)
print(id(x), id(y))


def outer_function(x):
    def inner_function():
        return x + 1
    return inner_function

closure = outer_function(5)
result = closure
print(result)


def mysterious_function(a, b=[]):
    b.append(a)
    return b

result1 = mysterious_function(1)
print(result1)
result2 = mysterious_function(2)
print(result2)
result3 = mysterious_function(3)
print(result3)
print(result1)
print(result1 + result2 + result3)

def power(x, n=2):
    return x ** n

result2 = power(2, 3)
print(result2)



# class CustomError(Exception):
#     def __init__(self, message):
#         super().__init__(message)

# raise CustomError("An example custom error.")