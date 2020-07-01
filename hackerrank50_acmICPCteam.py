nm=input().split()
n=int(nm[0])
m=int(nm[1])
a=[]
for _ in range(n):
    topic_item=input()
    a.append(topic_item)
# a=['10101','11100','11010','00101']
b=[]
c=[]
count=0
for i in range(len(a)):
    for j in range(len(a)):
        if i!=j and i<j:
            k=int(a[i])+int(a[j])
            b.append(k)
# print(b)
for i in range(len(b)):
    k=list(str(b[i]))
    # print(k)
    for j in range(len(k)):
        if int(k[j])!=0:
            count+=1
    c.append(count)
    count=0
ans1= max(c)
count=0
for i in range(len(c)):
    if c[i]==ans1:
        count+=1
ans2=count
print(ans1)
print(ans2)
# for i in range(len(a)):
#     b.append(list(a[i]))
# print(b)
#
# for i in range(len(b)):
#     for j in range(len(b)):
#         for k in range(len(b[i])):
#             for l in range(len(b[i])):
#                 if b[i][k]==b[j][l] and k==l and i!=j:
#

# for i in range(len(a)):
#     for k in range(len(a)):
#         for j in range(len(list(a[i]))):
#             if (list(int(a[i][j]))==1 or list(int(a[k][j]))==1)and k>i:
#                 print(list(a[i][j]))


def acmTeam(topic): # that the code which terminated between the time
    lid = sum = 0  # lowerindex of topics list

    uid = 1  # upperindex of the topics list
    fin = []

    while lid != len(topic) - 2:

        if uid > len(topic) - 1:
            lid += 1
            uid = lid + 1

        res = bin(int(topic[lid], 2) | int(topic[uid], 2))

        temp_count = res.count(str(1))
        uid += 1

        if temp_count >= sum:
            sum = temp_count
            fin.append(sum)

    return (sum, fin.count(sum))
