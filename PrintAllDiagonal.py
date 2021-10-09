a=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
for i in range(len(a)):
    row=0
    col=i
    while(col>=0):
        print(a[row][col],end=" ")
        col=col-1
        row=row+1
    print()
for i in range(1,len(a)):
    row=i
    col=len(a)-1
    while(row<len(a)):
        print(a[row][col],end=" ")
        col=col-1
        row=row+1
    print()
for i in range(len(a)):
    row=i
    col=len(a)-1
    while(row>=0):
        print(a[row][col],end=" ")
        row=row-1
        col=col-1
    print()
for i in range(1,len(a)):
    row=i
    col=0
    while(row<=len(a)-1):
        print(a[row][col],end=" ")
        row=row+1
        col=col+1
    print()
