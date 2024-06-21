'''

In the given array find the smallest positive element and print the element

'''


#METHOD 1
def min_positive():
    m=999
    lis=[5,7,-10,-3,0,3,-5]
    for i in lis:
        if i<m:
            if i>0:
                m=i
            else:
                continue
    if m==999:
        return 0
    else:
        return m
    
print(min_positive())

#METHOD 2

def small(l):
    res=999
    for i in l:
        if i>0 and i<res:
            res=i
    print(res)
            
l=[-3,6,-4,2,-5,-3,7]
small(l)