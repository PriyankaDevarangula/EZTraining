n=5
l=[1,2,3,4,5]
m=[]
for i in range(0,len(l)):
    if l[i]==l[-1]:
        m.append(l[i])
    else:
        p=l[:i]
        pri=l[i:]
        dif=sum(pri)-sum(p)
        m.append(dif)
m.append(m[0])
m.pop(0)
print(m)