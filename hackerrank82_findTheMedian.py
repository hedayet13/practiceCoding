n=int(input())
a=list(map(int,input().rstrip().split()))

a=sorted(a)
x=len(a)//2
print(a[x])