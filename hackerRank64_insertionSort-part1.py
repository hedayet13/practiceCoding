a=5
b=[2,4,1,8,3]
# a=int(input())
# b= list(map(int,input().rstrip().split()))
x=b[len(b)-1]
for i in range(2,len(b)+1):
    if x<b[-i]:
        b[-i+1]=b[-i]
        print(*b)
    else:
        b[-i+1]=x
        print(*b)


        
def insertionSort1(n, arr):
    i = n-1
    val = arr[i]
    while(i>0 and val<arr[i-1]):
        arr[i] = arr[i-1]
        print(*arr)
        i-=1
    arr[i] = val
    print(*arr)