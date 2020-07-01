nd=input().split()
n=int(nd[0])
d=int(nd[1])
a= list(map(int,input().rstrip().split()))
# a=[1,2,4,5,7,8,10]
# print(a[0:3])
'''
toughest way .. it will terminated for looooooonnnngg arraay
'''
count=0
for i in range(len(a)):
    for j in range(len(a)):
        j+=i
        if j<len(a) and i!=j:
            for k in range(len(a)):
                k+=j
                if k<len(a) and j!=k:
                    if (a[j]-a[i]==d) and (a[k]-a[j]==d):
                        count+=1
print(count)



'''
most easiest way is below
'''
gc=0
for i in range(n):
    if a[i]+d in a and a[i]+2*d in a:
        gc+=1
print (gc)