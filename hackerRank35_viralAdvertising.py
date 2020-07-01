n=int(input())
start =5
c=0
for i in range(1,n+1):
    if i==1:
        a=int(5/2)
        b=a*3
        c=c+a
    else:
        a=int(b/2)
        b=a*3
        c=c+a
print(c)