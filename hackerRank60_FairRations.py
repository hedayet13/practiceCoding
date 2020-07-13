n,c,a=int(input()),0,list(map(int,input().split()))
for i in range(0,len(a)-1):
    if a[i]%2!=0 :
        c=c+2
        a[i+1]=a[i+1]+1
print(c if a[-1]%2==0 else 'NO')