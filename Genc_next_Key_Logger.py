a=int(input())
b=str(a)
c=""
for i in b:
    x=int(i)+96
    c=c+chr(x)
i=0
c1=""
z=b
b=b+"0"
while(i<len(z)):
    if(i==0):
        x = int(b[i]) + 96
        c1=c1+chr(x)
        i=i+1
    elif(i>=1):
        if(int(b[i]+b[i+1])<=26):
            x=int(b[i]+b[i+1])+97
            c1 = c1 + chr(x)
            i = i + 2
        else:
            x=int(b[i])+97
            c1 = c1 + chr(x)
            x = int(b[i+1]) + 96
            c1 = c1 + chr(x)
            i=i+2
c2=""
i=0
while(i<len(z)):
    if(int(b[i]+b[i+1])<=26):
        x = int(b[i] + b[i + 1]) + 97
        c2 = c2 + chr(x)
        i = i + 2
    else:
        x = int(b[i]) + 96
        c2 = c2 + chr(x)
        x = int(b[i + 1]) + 96
        c2 = c2 + chr(x)
        i = i + 2

print(c)
print(c1)
print(c2)

