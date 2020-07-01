pmds = input().split()
p=int(pmds[0])
m=int(pmds[1])
d=int(pmds[2])
s=int(pmds[3])
# p=20
# d=3
# m=6
# s=80

q=0
count=0
while q<=s:
    if p<=d:
        q=q+d
        if q<=s:
            count+=1
    else:
        q=q+p
        p=p-m
        if q<=s:
            count+=1
print(count)