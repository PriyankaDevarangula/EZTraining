class Node:
    def __init__(self,data):
        self.value=data
        self.next=None
class Hashtable:
    def __init__(self):
        self.size=10
        self.table=[None]*self.size
    def insert(self, data):
        index=data%10
        if self.table[index] is None:
            self.table[index]=Node(index)
        curr=self.table[index]
        while curr.next is not None:
            curr=curr.next
        curr.next=Node(data)
    def display(self):
        for i in range(self.size):
            curr=self.table[i]
            while curr is not None:
                print(curr.value,"->",end=" ")
                curr=curr.next
            print(None)
data=[10,16,62,100,20,86,72,7,76,99]
hs=Hashtable()
for i in data:
    hs.insert(i)
hs.display()