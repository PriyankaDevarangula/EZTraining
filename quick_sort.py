"""
If i found to be smaller than pivot, Then increase j by one and swap it by i
If i found to be bigger than pivot i will do ntg
"""

def divide(l,low,high):
    #1 2 3 4 5 6 7  8 9 10 11 12
    pivot=l[high]
    i=low-1
    for j in range(low,high):
        if l[j]<=pivot:
            i+=1
            l[i],l[j]=l[j],l[i]
    l[i+1],l[high]=l[high],l[i+1]
    return i+1

def quicksort(l,low,high):
    if low<high:
        pi=divide(l,low,high)
        print(pi,low,high)
        quicksort(l,low,pi-1)
        quicksort(l,pi+1,high)
    return



if __name__=="__main__":
    l=list(map(int,input().split()))
    low=0
    high=len(l)-1
    print(low,high)
    quicksort(l,low,high)
    print(l)