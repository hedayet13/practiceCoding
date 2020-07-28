a='aaabbbaaabbbaaabbbbaaabbbbb'
a=list(a)
x=1
count=0
z=1
for i in range(len(a)):
    y=x+1
    if a[i]==a[x]:
        count+=1
        x+=1
        if x==len(a):
            break
    elif y==len(a):
        break
    elif a[i]!=a[x] and a[x]==a[y]:
        if y==len(a):
            break
        x+=1
        if x==len(a):
            break
    else:
        x+=1
        if x==len(a):
            break
print(count)