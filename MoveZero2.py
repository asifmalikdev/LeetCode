arr = [1,0,2,3,0,3,4,0,2,3,0,0,1,0]
i = len(arr)-1
print(arr[i])
for j in range(len(arr)-(len(arr)-i)-1):
    if arr[j] == 0:
        arr[i],arr[j] = arr[j],arr[i]
        i-=1
        print(i,arr[j])

print(arr)