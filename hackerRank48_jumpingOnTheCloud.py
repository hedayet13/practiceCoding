n=int(input())
a= list(map(int,input().rstrip().split()))
# a=[0,0,1,0,0,1,0]
# for i in range(1,len(a)):
#     if a[i]==0 :
#         z=z+1
#         count+=1
#         if z==2:
#             count-=1
#             z=0
#     else:
#         z=0
# print(count)
i=0
res=0
while i<n-1:
    if  i+2<n and a[i+2]==0:
        i=i+2
        res+=1
    else:
        i=i+1
        res+=1
print(res)
