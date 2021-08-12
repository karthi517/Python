from itertools import combinations

list1 = [[]]
l = [1,2,3,4]
for i in range(1,len(l)+1):
    combi= combinations(l,i)
    for i in combi:
        list1.append(list(i))
print(list1)
