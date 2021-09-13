from itertools import combinations
N=int(input())
C=int(input())
TL1=list(map(int,input().split()))
TL2=list(map(int,input().split()))
list1=[]
list2=[]
for i in range(1,N+1):
    combi= combinations(TL1,i)
    for i in combi:
        list1.append(sum(i))
for i in range(1,N+1):
    combi= combinations(TL2,i)
    for i in combi:
        list2.append(sum(i))
max=0
for i in range(len(list2)):
    if(list2[i]<=C):
        if(max<list1[i]):
            max=list1[i]
print(max)
