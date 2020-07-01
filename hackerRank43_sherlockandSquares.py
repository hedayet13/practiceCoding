import math

q=int(input())
for iter in range(q): #that is so time consuming
    ab=input().split()
    a=int(ab[0])
    b=int(ab[1])
    count=0
    for i in range(a,b+1):
        if math.sqrt(i)==int(math.sqrt(i)):
            count+=1

    print(count)

    for _ in range(q):  # less time consuming
        a, b = input().strip().split(' ')
        a = int(a)
        b = int(b)

        sqrtA = math.ceil(math.sqrt(a))
        sqrtB = math.floor(math.sqrt(b))

        print(sqrtB - sqrtA + 1)