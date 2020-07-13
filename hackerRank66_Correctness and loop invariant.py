a=int(input())
b= list(map(int,input().rstrip().split()))

c=sorted(b)
print(*c)