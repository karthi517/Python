pronlem 3
"""There is a range given n and m in which we have to find the count of all the prime pairs whose difference is 6. We have to find how many sets are there within a given range.
Output:
The output consists of a single line, print the count prime pairs in a given range. Else print"No Prime Pairs".
Constraints:
2<=n<=1000
n<=m<=2000
Sample Input:
4
30
Output:
6
Explanation:
(5, 11) (7, 13) (11, 17) (13, 19) (17, 23) (23, 29) . we have 6 prime pairs."""

################################################################################################################################################
Answer:
start=int(input())
end=int(input())
list=[]

for i in range(start,end+1):
    count=0
    k=i
    for j in range(2,i):
        if(i%j==0):
            count=0
            break
        else:
            count=count+1
    if(count!=0):
        list.append(k)

c=0
for i in list:
    for j in list:
        if(i-j==6):
            c+=1
print(c)





