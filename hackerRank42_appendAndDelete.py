
'''
i couldnt have submit this code because of headache.. plez try it later

'''


n= input()
o= input()
a=int(input())
l=list(n)
m=list(o)
e=[]
if n==o:
    l=list(n)
    x=2*len(l)+1
    if x==a:
        print('Yes')
    else:
        print('No')
else:
    for i in range(len(m)):
        if l[0]==m[0]:
            l.remove(l[0])
            m.remove(m[0])
    x=(len(l)+len(m))
    if x==a:
        print('Yes')
    else:
        print('No')