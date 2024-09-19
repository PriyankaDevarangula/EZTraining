'''
item=[1,2,3,4,5,6,7]
profit=[5,10,15,7,8,9,4]
weight=[1,3,5,4,1,3,2]
d={}
for i in range(len(item)):
    while 

for i,j in d.items():
    print(i,":",j)

'''
'''

#knapsack error

price=list(map(float,input().split()))
weight=list(map(float,input().split())) 
profit=0
ratio_list=[]
max_weight=int(input("Enter weight: "))
for i in range(len(price)):
    ratio_list.append(price[i]/weight[i])

while max_weight>0:
    index=ratio_list.index(max(ratio_list))
    max_weight-=weight[index]
    ratio_list.pop(index)
    price.pop(index)
    weight.pop(index)

print(profit)

'''

#KNAPSACK

p=[5,10,15,7,8,9,4]
w=[1,3,5,4,1,3,2]
max_weight=30

l=[]
for i in range(len(p)):
    l.append(p[i]/w[i])

print(l)
sum=0

while max_weight!=0:
    #x=p_w.index(max(p_w))
    #weight=weight-w[x]
    #sum+=p[x]
    #p_w.pop
    #p_w.pop(x)
    #w.pop(x)
    index_val=l.index(max(l))
    print(index_val)
    sum+=p[index_val]
    max_weight-=w[index_val]
    l.pop(index_val)
    p.pop(index_val)
    w.pop(index_val)

print(sum)

