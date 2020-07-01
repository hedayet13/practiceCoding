a=input()
k= int(input())
a=list(a)
# b=[]
# y=0
# for i in range(k):
#     b.append(a[y])
#     y+=1
#     if y==len(a):
#         y=0
# count=0
# for i in range(len(b)):
#     if b[i]=='a':
#         count+=1
# print(count)
count=0
count1=0
m= len(a)
if k%len(a)==0:
    for i in range(len(a)):
        if a[i]=='a':
            count+=1
    ans=int(k/len(a))*count
    print(ans)
else:
    for i in range(len(a)):
        if a[i]=='a':
            count+=1
    x= a[:k%len(a)]
    for i in range(len(x)):
        if x[i]=='a':
            count1+=1
    ans=int(k/len(a))*count+count1
    print(ans)