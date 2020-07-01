nk=input().split()
n= int(nk[0])
k=int(nk[1])
a=list(map(int,input().rstrip().split()))
count =100
c=0
for i in range(len(a)):
    count-=1
    if a[c]==1:
        count-=2
    c=c+k
    if c>=len(a):
        break
print(count)