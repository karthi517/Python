def listsort(list):
 for i in range(len(list)):
   for j in range(len(list[i])-1,0,-1):
      for k in range(j):
         if list[i][k]>list[i][k+1]:
            temp = list[i][k]
            list[i][k] = list[i][k+1]
            list[i][k+1] = temp
list = [[13,5,6],[6,2,9],[3,9,2],[-5,-8,67]]
listsort(list)
print(list)
