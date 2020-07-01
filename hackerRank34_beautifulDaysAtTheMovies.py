ijk= input().split()
i = int(ijk[0])
j = int(ijk[1])
k = int(ijk[2])
count=0
for i in range(i,j+1):
    c=str(i)
    c="".join(reversed(c))
    c=int(c)
    division=abs(i-c)/k
    if division%2==0.0 or division%2==1.0:
        count+=1
print(count)