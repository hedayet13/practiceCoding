'''
by using this code u may count how many real number in this
arr = [1,2,3,4,5,4,3,2,1,3,4]
n=len(arr)
arr= sorted(arr)
print(arr)
list=[]
count =0
for i in range(n):
    for j in range(n):
        if arr[i] == arr[j] and i<j:
            list.append(arr[i])
            n=n-1
print(n)
print(list)
'''
ar = [1,2,3,4,5,4,3,2,1,3,4]
# ar = sorted(ar)
# list = []
# for i in range(len(ar)):
#     for j in range(len(ar)):
#         if ar[i]==ar[j]  and i<j:
#             list.append(ar[i])
# print(list)
# print(min(list))

counts=[0]*len(ar)
print(counts)
for i in range(len(ar)):
    counts[ar[i]-1]+=1
print(counts)
m=0
for i in range(len(ar)):
    if counts[i]>m:
        m=counts[i]
        mi=i
print(mi+1)
