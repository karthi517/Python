"""Q4. Write a program to print all the combinations of the given word with or without meaning (when unique characters are given).
Sample Input:
abc
Output:
abc
acb
bac
bca
cba
cab"""
#############################################################################################################################
from itertools import permutations
a=input()
perm = permutations(a)

# Print the obtained permutations
for i in list(perm):
     for j in range(len(i)):
             print(i[j],end="")
     print(end=" ")
