
'''
first one is slow process .. next one in fast process
'''

# z='aaabbccddd'
z=input()
n=int(input())
queries =[]
for _ in range(n):
    item = int(input())
    queries.append(item)
# x=12
z=sorted(list(z))
arr='abcdefghijklmnopqrstuvwxyz'
arr=list(arr)
count=0
for k in range(len(queries)):
    x=queries[k]
    l=[]
    for i in range(len(arr)):
        count=0
        for j in range(len(z)):
            if arr[i]==z[j]:
                count+=(i+1)
            if count==x:
                l.append(x)
    if l!=[]:
        print("YES")
    else:print('NO')

#for fast process
def weightedUniformStrings(s, queries):
    a=ord(s[0])-96
    leng=set()
    s=s+"_"
    for i in range(1,len(s)):
        leng.add(a)
        if s[i]==s[i-1]:
            a+=(ord(s[i])-96)
        else:
            a=(ord(s[i])-96)
    return ["Yes" if i in leng else "No" for i in queries]