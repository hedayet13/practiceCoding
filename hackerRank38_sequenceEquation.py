n=int(input())
p=list(map(int,input().rstrip().split()))
for i in range(1,n+1):
    for x in range(len(p)):
        if i==p[x]:
            c=x+1
            d=p.index(c)
            print(d+1)