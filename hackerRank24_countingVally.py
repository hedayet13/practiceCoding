a=['U','D','D',"D",'U','D','U','U','U']
up=0
count=0
for i in range(len(a)):
    if a[i]=='U':
        up+=1
    else:
        up-=1
    if a[i]=='U' and up==0:
        count+=1
print(count)