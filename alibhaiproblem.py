
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