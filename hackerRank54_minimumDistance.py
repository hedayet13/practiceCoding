n=int(input())
a= list(map(int,input().rstrip().split()))

# a=[7,1,3,4,1,7]
l=[]
for i in range(len(a)):
    for j in range(len(a)):
        if a[i]==a[j] and i!=j:
            l.append(abs(i-j))
if not l==[]:
    print(min(l))
else:
    print(-1)