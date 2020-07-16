q=int(input())

for iter in range(q):
    a=input()

    # a='aaabbbaaabbbaaabbbbaaabbbbb'
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


'''
easiest way 
'''

t = int(input())

for i in range(t):
    x = input()

    count = 0

    for i in range(1, len(x)):
        if x[i-1] == x[i]:
            count += 1

    print (count)