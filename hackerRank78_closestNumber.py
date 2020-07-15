n=int(input())
a=sorted(list(map(int,input().rstrip().split())))
# a=[5,4,3,2]
l=[]
for i in range(len(a)):
    for j in range(len(a)):
        if i!=j:
            x=a[i]-a[j]
            if x>0:
                l.append(x)
# print(min(l))
z=[]
for i in range(len(a)):
    for j in range(len(a)):
        if i!=j:
            x=a[i]-a[j]
            if x==int(min(l)):
                z.append(a[j])
                z.append(a[i])
print(*sorted(z))



'''
for skipping the timing out
'''
def closestNumbers(arr):
    arr.sort()
    min_dif = abs(arr[0]-arr[1])
    ans = []
    for i in range(len(arr)-1):
        d = abs(arr[i]-arr[i+1])
        if d==min_dif:
            ans += [arr[i], arr[i+1]]
            min_dif =d
        elif d<min_dif:
            ans = [arr[i], arr[i+1]]
            min_dif =d
    return ans

input()
print(*closestNumbers(list(map(int,input().split()))))