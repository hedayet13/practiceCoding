k=3
n=6
ar=[1,3,2,6,1,2]
count = 0
for i in range(n):
    for j in  range(n):
        if (ar[i]+ar[j])%k ==0 and i<j:
            count+=1
print(count)
