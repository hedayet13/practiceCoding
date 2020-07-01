n=int(input())
for iter in range(n):
    x=int(input())
    a=list(str(x))
    count=0
    for i in range(len(a)):
        if int(a[i])>0:
            if x%int(a[i])==0:
                count+=1
    print(count)