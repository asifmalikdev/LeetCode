lis = [1,2,3,43,5,33,42,3153,2,2,13,1,2,3,2,1,23,1]
freq_map = {}
for num in lis:
    freq_map[num] = freq_map.get(num,0)+1
print(freq_map)
#print(freq_map.get(0)+1)
print(freq_map.get(4234,4))