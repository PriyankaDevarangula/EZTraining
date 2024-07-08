l=[9,7,5,8,10,26,44,3,1]
for i in range(len(l)):
    key = l[i]
    j = i - 1
    while(j >= 0 and l[j] > key):
        l[j+1]=l[j]
        j -= 1
    l[j+1]=key
print(l)

