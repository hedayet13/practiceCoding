a=[1,2,2,3,1,2]
maximum = 0
for i in a:
    c=a.count(i)
    d=a.count(i-1)
    c=c+d
    if c>maximum:
        maximum=c
print(maximum)
# n,a = input(),list(map(int,input().split()))
print(max(a.count(x)+a.count(x+1) for x in a))