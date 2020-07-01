# a=[4,2,6,1,10]
# quesPerPage=3
# page=0
# count=0
# l=0
# m=0
# for i in range(len(a)):
#     page=page+int(a[i]/quesPerPage)
#     z=list(range(1,a[i]+1))
#     for j in range(int(a[i]/quesPerPage),page+1):
#         for k in range(len(z[l:m+3])):
#             if j==z[k]:
#                 count+=1
#             l=l+3
#             m=m+3
#             if m>len(z):
#                 m=len(z)
#     l=0
#     m=0
#     if 0<a[i]%quesPerPage<quesPerPage:
#         page+=1
#         z = list(range(1, a[i] + 1))
#         for j in range(int(a[i] / quesPerPage), page + 1):
#             for k in range(len(z[l:m + 3])):
#                 if j == z[k]:
#                     count += 1
#                 l = l + 3
#                 m = m + 3
#                 if m > len(z):
#                     m = len(z)
#         l = 0
#         m = 0
# print(page)
# print(count)


NK = input().split()
N=int(NK[0])
K=int(NK[1])
T = list(map(int, input().rstrip().split()))

cnt = 0 # special problems
i = 0   # chapter number
j = 1   # page number
m = 1   # problem number

while i < N:
    if m <= j and j <= min(m + K - 1, T[i]):
        cnt += 1
    j += 1
    m += K
    if m > T[i]: # next chapter
        i += 1
        m = 1
print(cnt)