a=[[1,2,3],[3,4,5],[4,5,6,4],[2,2,2,2]]
result=a[-1].count(a[-1][0])==len(a[-1])
if(result):
    print("Equal")
else:
    print("Not Equal")
