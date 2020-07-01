n=int(input())
a=list(map(int,input().rstrip().split()))
a=sorted(a)
count=0
k=[len(a)]
for i in range(len(a)):
    z=[]
    for j in range(len(a)):
        if a[i]!=0:
            x=a[j]-a[i]
            if x>0:
                z.append(x)
    k.append(len(z))
k=list(set(k))
y=0
for i in range(len(k)):
    z=k[len(k)-1-y]
    if z!=0:
        print(z)
    y+=1