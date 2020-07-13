# ab= input().split()
# a=int(ab[0])
# b=int(ab[1])
# c=list(map(int,input().rstrip().split()))
a= 6
b= 6
c=[0,1,2,3,4,5]
print(c[-1])
l=[]
y=[]
for i in range(a):
    for j in range(b):
        if c[j]!=i:
            if c[j]>i:
                x=c[j]-i
                l.append(x)
            else:
                x=i-c[j]
                l.append(x)
        else:
            l.append(0)
    if len(l)>0:
        y.append(min(l))
        l=[]
# print(l)
print(max(y))

# plz use the below for time limit
def flatlandSpaceStations(n, c):
  c.sort()
  maxd = max(c[0], n-1 - c[-1])
  for i in range(len(c)-1):
    maxd = max((c[i+1]-c[i])//2, maxd)
  return maxd