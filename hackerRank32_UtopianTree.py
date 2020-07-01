t=int(input())
for t_iter in range(t):
    n=int(input())
    c=1
    for i in range(n):
        if i%2==1:
            c=c+1
        else:
            c=c*2
    print(c)