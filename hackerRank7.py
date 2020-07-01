a = [1,2,3,-1,-2,-3,0,0]
length= len(a)
p=list()
n=list()
z=list()
for i in a :
    if i>0:
        p.append(i)
print("{:6f}".format(len(p)/length))
for i in a :
    if i<0:
        n.append(i)
print("{:}".format(len(n)/length))
for i in a :
    if i==0:
        z.append(i)
print("{:6f}".format(len(z)/length))