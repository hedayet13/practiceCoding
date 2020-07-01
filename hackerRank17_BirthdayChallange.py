a= [ 1 ,2,1,3,2]
b = [3,2]
count = 0
for i in range(len(a)):
    if sum(a[i:i+b[1]]) == b[0]:
        count+=1
print(count)