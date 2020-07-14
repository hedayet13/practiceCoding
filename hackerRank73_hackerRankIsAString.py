n=int(input())
for q in range(n):
    a=input()
    a=list(a)
    b='hackerrank'
    b=list(b)
    l=[]
    j=0
    for i in range(len(b)):
        while j<len(a):
            if b[i]== a[j]:
                l.append(b[i])
                j+=1
                break
            else:
                j+=1
    if l==b:
        print('YES')
    else:
        print('NO')
