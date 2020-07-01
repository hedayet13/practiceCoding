a= [3,4,21,36,10,28,35,5,24,42]
countMax =0
countMin=0
min=a[0]
max=a[0]
for i in range(len(a)):
    if a[i]<min:
        min = a[i]
        countMin+=1
    if a[i]>max:
        max=a[i]
        countMax+=1
print(countMax)
print(countMin)