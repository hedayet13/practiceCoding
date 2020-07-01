n=int(input())
arr=list(map(int,input().rstrip().split()))
l=[]
m=[]

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i]==arr[j] and i!=j:
            l.append(arr[i])
            break

for i in range(len(l)):
    count=0
    for j in range(len(l)):
        if l[i]==l[j]:
            count+=1
        m.append(count)
# max(m)
# print(max(m))
if m==[]:
    print(len(arr)-1)
else:
    print(len(arr)-max(m))
# print(l)