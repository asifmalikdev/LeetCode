count = 0
def recu_1_to_():
    global count
    print(id(count),count)
    if count == 4:
        print(id(count),count,"ghjf")
        return
    count+=1
    recu_1_to_()
#recu_1_to_s()
count = 10
def recu_n_to_1():
    global count
    print(count)
    if count !=1:
        count-=1
        recu_n_to_1()
    return   
#recu_n_to_1()

def recu_n_to_0(x:int)->int:
    if x <1:
        return "hello"
    print(x)
    x-=1
    return recu_n_to_0(x)
x = 10
#print(recu_n_to_0(x))




def bt_1_to_n(x:int)->int:
    if x<1:
        return
    bt_1_to_n(x-1)
    print(x)

#bt_1_to_n(10)




def bt_n_to_1(x:int)->int:
    if x>10:
        return
    bt_n_to_1(x+1)
    print(x)
#bt_n_to_1(1)