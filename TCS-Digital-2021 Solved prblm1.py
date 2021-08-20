"""Q1. Problem statement:
Given two non-negative integers n1 and n2, where n1 <n2. The task is to find the total number of integers
in the range interval [n1, n2] [both inclusive] which have no repeated digits.
For e.g.
Suppose n1 = 11 and n2 = 15.
There is the number 11, which has repeated digits, but 12, 13, 14, and 15 have no repeated digits. So, the
output is 4.
Input Output
11 -- Value of n1
15 -- Value of n2 4
101 -- Value of n1
200 -- Value of n2 72"""

#####################################################################################################################################
input1=int(input())
input2=int(input())
c=0
for i in range(input1,input2):
    list1=[]
    count = 0
    while(i!=0):
        d=d%10
        if(d not in list1):
            list1.append(d)
            count=count+1
        else:
            count=0
        i//=10
    if(count!=0):
        c=c+1
print(c)

