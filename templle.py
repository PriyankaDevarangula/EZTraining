x=int(input("Enter no: "))
y=int(input("Enter number: "))
while True:
    if x==y:
        print(x)
        break
    elif x<=y:
        x,y=y,x
    else:
        temp=x-y
        x=y
        y=temp

