nk = input().split()
n= int(nk[0])
k= int(nk[1])
height = list(map(int,input().rstrip().split()))
list=[]
for i in range(n):
    if height[i]>k:
        list.append(height[i])
if len(list)>0:
    final= max(list) - k
    print(final)
else:
    print(0)