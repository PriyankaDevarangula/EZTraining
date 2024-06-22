'''

Space counter 
You have been gives the task of making the counter on a social media platform more userfriendly.your task is to find and return an integer value representing the count of the number of 
spaces in a gives string S. 
Input: 
A string: 
Output: 
Return an integer value representing the count of the number of space in a given string S. 

'''

s=input() 
c=0 
for i in s: 
    if i==" ": 
        c=c+1 

h=s.split() 
print(h) 
print(len(h)-1) 