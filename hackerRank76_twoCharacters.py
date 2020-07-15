


a=int(input())
b=input()
b1=list(b)
b=list(set(b1))
# print(len(b))
z=[]
for i in range(len(b)):
    x=0
    while x <len(b):
        if i<x:
            # print(b[i],b[x])
            l=[]
            for j in range(len(b1)):
                if b1[j]==b[i]:
                    l.append(b[i])
                elif b1[j]==b[x]:
                    l.append(b[x])

            # print(l)
            n=1
            for m in range(len(l)):
                if l[m]!=l[n]:
                    n+=1
                    if n==len(l):
                        # print(l)
                        z.append(len(l))
                        break
                else:
                    break
            # for m in range(len(l)):
            #     n=1
            #     while n<len(l):
            #         if m<n and l[m]==l[n] and n==m+1:
            #             print(l)
            #             # z.append(l)
            #         n+=1


        x+=1
if z==[]:
    print(0)
else:print(max(z))