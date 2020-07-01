p = int(input())
q = int(input())
l = []
if p == 1:
    print(1, end=" ")
for i in range(p, q + 1):
    x = (list(str(i ** 2)))
    c = len(x) / 2
    if (len(x) % 2 == 0 or 1) and i!=3 and i !=2 and i!=1:
        y = ''.join(x[:int(c)])
        z = ''.join(x[int(c):])
        if (int(y) + int(z)) == i:
            l.append(i)
if l==[]:
    print('INVALID RANGE')
for i in range(len(l)):
    print(l[i], end=' ')
