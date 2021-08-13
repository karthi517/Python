a=[[0,1,1],[1,0,1],[2,1,5]]
c=[]
x=a[0][-1]
for i in range(len(a)):
    for j in range(len(a[i])):
        if(j==len(a[i])-1):
           if(a[i][-1]==x):
              c.append(a[i][-1])

if(len(a)==len(c)):
    print("Last coloumns are same")
else:
    print("Last coloumns are differnt")

