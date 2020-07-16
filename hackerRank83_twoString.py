n=int(input())
for iter in range(n):
    a=input()
    # a='hello'
    a=set(list(a))
    b=input()
    # b='World'
    b=set(list(b))

    if a.intersection(b):
        print('YES')
    else:
        print('NO')