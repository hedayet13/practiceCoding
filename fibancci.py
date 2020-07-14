
#recursive
def func(n):
    if n>=3:
        return func(n-1)+func(n-2)
    elif n==1 or n==2:
        return 1
#memorize
def func2(n):
    if n==1 or n==2:
        result= 1
    elif n>=3:
        result = func2(n-1)+func2(n-2)
    return result

#bottom up approach
def bottomup(n):
    if n==1 or n==2:
        return 1
    bottom_up=[None]*(n+1)
    bottom_up[1]=1
    bottom_up[2]=1
    for i in range(3,n+1):
        bottom_up[i]=bottom_up[i-1]+bottom_up[i-2]
    return bottom_up[n]
print(bottomup(1000))