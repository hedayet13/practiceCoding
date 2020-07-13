# a=4
# b=6
# c=[1,4,5,7,9,12]
a=int(input())
b=int(input())
c=list(map(int,input().rstrip().split()))

for i in range(len(c)):
    if c[i]/a==1:
        print(i)