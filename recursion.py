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

