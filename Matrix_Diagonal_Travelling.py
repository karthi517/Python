a=[[0,1,1],[1,0,1],[2,1,0,8]]
count=0
x=0
for i in range(len(a)):
 if(len(a[i])>=count+1):
    val=a[0][0]
    if(a[i][count]==val):
        x=x+1
 count=count+1
if(x==len(a)):
    print("Diagonal are same")
else:
   print("no diagonal is not same")
