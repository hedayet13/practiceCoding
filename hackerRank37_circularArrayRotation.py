nkq= input().split()
n=int(nkq[0])
k = int(nkq[1])
q = int(nkq[2])
a = list(map(int, input().rstrip().split()))
queries = []
for _ in range(q):
    queries_item = int(input())
    queries.append(queries_item)
if len(a)<k:
    z= k%len(a)
else:
    z=k
list=a[-z:]+a[:-z]
for i in queries:
    print(list[i])