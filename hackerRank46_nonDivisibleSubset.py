# a=[19,10,12,10,24,25,22]
# # b=4
# n,k = input().rstrip().split()
# n=int(n)
# k=int(k)
# a= list(map(int,input().rstrip().split()))
# l=[]
# for i in range(len(a)):
#     for j in range(len(a)):
#         if ((a[i]+a[j])%k)!=0 and i!=j:
#             l.append(a[i])
#             l.append(a[j])
#         elif (a[i]+a[j])%k==0 and i!=j:
#             l.remove(a[i])
#             l.remove(a[j])
# print(l)
# print(len(list(set(l))))
read = lambda: map(int, input().split())

n, k = read()
a = list(read())
cnt = [0] * k
for x in a:
    cnt[x % k] += 1
print(cnt)
ans = min(cnt[0], 1)
print(ans)
for rem in range(1, (k + 1) // 2):
    ans += max(cnt[rem], cnt[k - rem])
    print(ans)
if k % 2 == 0:
    ans += min(cnt[k // 2], 1)

print(ans)