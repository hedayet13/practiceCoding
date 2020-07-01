a = [5,6,7]
b= [3,6,10]
alice=0
bob = 0
length = len(a)
for i in range(length):
    if (a[i]>b[i]):
        alice =alice +1
    elif (a[i]<b[i]):
        bob=bob+1
print(alice,bob)
print(len(a))

