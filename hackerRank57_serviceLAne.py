nt =input().split()
n= int(nt[0])
t= int(nt[1])
width = list(map(int,input().rstrip().split()))
cases=[]
for _ in range(t):
    cases.append(list(map(int,input().rstrip().split())))

for i in cases:
    # n=[2,3,1,2,3,2,3,3]
    # cases=[0,7]
    l=[]
    for j in range(i[0],i[1]+1):
        l.append(width[j])
    print(min(l))