a=int(input()) #5
sum=0
c=list(map(int,input().split()))# 4 3 2 1 2
for i in c:
    sum=sum+i
if(sum % 4==0):
    print(sum//4)
else:
  print((sum//4)+1)
