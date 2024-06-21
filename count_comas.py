'''
count the number of commas from the range of 0 to N and return the count
EXAMPLE :
input= 12,456,789
output=23912580

'''
#METHOD 1

def count_commas():
    num = int(input("Enter the number up to which the commas should be counted: "))
    if num < 1000:
        print(0)
    elif num < 1000000:
        print((num - 1000) + 1)
    else:
        commas_one = 999000
        commas_two = (num - 999999) * 2 
        total_commas = commas_one + commas_two
        print(total_commas)

count_commas()

#METHOD 2
def separators(n):
    count=0
    for i in range(1,n+1):
        if i>999 and i<=999999:
            count+=1
        elif i>999999 and i<=999999999:
            count+=2
        elif i>999999999 and i<=999999999999:
            count+=3
    print(count)

n=int(input("Enter number: "))
separators(n)