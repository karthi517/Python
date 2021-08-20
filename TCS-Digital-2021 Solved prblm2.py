Problem 2: Question
"""Given an array Arr[] of N integers and a positive integer K. The task is to cyclically rotate the array
clockwise by K.
Note: Keep the first position of the array unaltered.
Example Input Output Explanation

Example 1
5 -- Value of N
{10, 20, 30, 40, 50} -- Elements of Arr[] 2 -- Value of K
40 50 10 20 30
Arr[] = {10, 20, 30, 40,50} and K = 2 (Twocyclical rotations)
After 1st rotation = {10,50, 20, 30, 40}
After 2nd rotation = {10,40, 50, 20, 30}

Example 2


4 -- Value of N
{10, 20, 30, 40} -- Elements of Arr[] 1 -- Value of K
40 10 20 30
Arr[] = {10, 20, 30, 40} and K=1 (One cyclical rotation)
After 1st rotation = {10,40, 20, 30}

Constraints
● 1 < N <=100
● -100 <= Arr[i] <=100
● 1 <=K <=100

Input format for testing
● The candidate should write the code to accept the inputs separated by a new line.
● First Input: Accept a single positive integer value for N representing the size of Arr[]
● Second Input: Accept N number of integer values separated by a new line, as elements of Arr[]
● Third input: Accept a single positive integer value for K representing the number of rotations.
Output format for testing
● The output must be N integer numbers separated by a single space character.
● Additional messages in the output will result in the failure of test cases.
Instructions
● The system does not allow any kind of hard-coded input value/ values.
● The written program code by the candidate will be verified against the input which are supplied
from the system."""
###########################################################################################################################################################
#Answer
n=int(input())
list1=list(map(int,input().split()))
k=int(input())
rotate=-k
x=list1[rotate:]
y=list1[:rotate]
z=x+y
for i in z:
    print(i,end=" ")
