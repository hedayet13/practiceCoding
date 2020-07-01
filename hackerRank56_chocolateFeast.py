t = int(input())
for iter in  range(t):
    ncm = input().split()
    n=int(ncm[0])
    c=int(ncm[1])
    m=int(ncm[2])
    # n=12
    # c=4
    # m=4
    x= int(n/c)
    z=x
    while z>=m:
        y=int(z/m)
        z=y+(z%m)
        x=x+y
    print(x)
