"""
#CHAINING

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class hash:
    def __init__(self):
        self.size=10
        self.table=[None]*self.size

    def insert(self,data):
        index=data%10
        if self.table[index] is None:
            self.table[index]=Node(data)
        else:
            n=self.table[index]
            while n.next is not None:
                n=n.next
            n.next=Node(data)


    def display(self):
        for i in range(self.size):
            n=self.table[i]
            while n is not None:
                print(n.data,end=" ")
                n=n.next
            print(None)

data=[10,16,62,100,20,86,72,7,76,99]
hs=hash()
for i in data:
    hs.insert(i)
hs.display()

print()
print()
print()

"""
# LINEAR PROBING

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * self.size

    def insert(self, data):
        index1 = data % self.size
        index2 = 8 - (data % 8)
        i = 0
        while self.table[(index1 + i * index2) % self.size] is not None:
            i += 1
            if i >= self.size:
                # If we have checked all slots and found no empty one
                raise Exception("HashTable is full")

        index = (index1 + i * index2) % self.size
        self.table[index] = data


    # def search(self,start_index,data):
    #     temp=start_index
    #     while start_index!=temp:
    #         index1=data%self.size
    #         index2=8-(data%8)
    #         index=(index1+(self.i+1*index2))%self.size
    #         if index==0:
    #             self.i+=1
    #             continue
    #     return index


# m=[20,34,45,70,56,81,104,37,36,39]
# x=HashTable(11)
# for p in m:
#     x.insert(p)
# print(x.table)

"""
# CHAINNG USING DICTONARY

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class hash:
    def __init__(self,size):
        self.size=size
        self.d={}
        for i in range(1,size):
            self.d[i]=None

    def display(self):
        for i,j in self.d.items():
            print(i,":",j)

    def insert(self,data):
        index=data%self.size
        if index in self.d.keys():
            self.d[index].append(data)


   

data=[10,16,62,100,20,86,72,7,76,99]
hs=hash(10)
for i in data:
    hs.insert(i)
hs.display()

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class hash:
    def __init__(self,size):
        self.size=size
        self.d={}
        for i in range(1,size):
            self.d[i]=None

    def display(self):
        for i in self.d.values():
            if i==None:
                print(self.d[i].values())
            else:
                n=self.d.values()
                while n.next is not None:
                    print(n.data,end=" ")
                    n=n.next
            

    def insert(self,data):
        index=data%self.size

        if index in self.d.keys():

            if self.d.values()==None:
                self.d[index]=Node(data)
            else:
                n=self.d.values()

                while n.next is not None:
                    n=n.next
                n.next=Node(data)
                

data=[10,16,62,100,20,86,72,7,76,99]
hs=hash(10)
for i in data:
    hs.insert(i)
hs.display()
"""

q=4
i=3
for x in zip(range(q-1,-1,-1),range(i-1,-1,-1)):
    print(x)