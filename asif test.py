x = 5
y = 5
#print(id(x))  #140710702044408
#print(id(y))  #140710702044408



lis1 = [1,2,3]
lis2 = [1,2,3]
lis3 = lis2
#print(id(lis1))   #2216803613952
#print(id(lis2))   #2216803497536
#print(id(lis3))   #2216803497536



exapmle_dict = dict()
#print(exapmle_dict)    {}



def greet(age, name):
    print(name, age)  #24 asif

age = 24
name = "asif"
#greet(name, age)

x = [1,2,3]
y = [1,2,3]
z = x

#print(id(x))  #2979899736960
#print(id(y))  #2979899737088
#print(id(z))  #2979899736960


x = 5
y = 6
#print(id(x))  #140711288395000
#print(id(y))  #140711288395032

x = "hello"
y = "hello"
#print(id(x))  #2139574722000
#print(id(y))  #2139574722000


x = 65
#print(id(x))  #140711288396920
x = 54
#print(id(x))  #140711288396568

x = "hello"
#print(id(x))  #1460078402880
x = "june"
#print(id(x))  #1460078403360


x = "hello"
#x[0] = "h"  #error

x = "hello"
x = x.upper()
#print(x)


x = 10
y = x
#print(id(x))  #140711288395160
#print(id(y))  #140711288395160
x = 20
#print(id(x))  #140711288395480
#print(id(y))  #140711288395160
#PROFFING The biggest proof: multiple references
print('eh')