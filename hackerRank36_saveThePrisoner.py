t= int(input())
for iter in range(t):
    nms= input().split()
    n=int(nms[0])
    m=int(nms[1])
    s=int(nms[2])
    # count=s-1
    # for j in range(1,m+1):
    #     count=count+1
    #     if count>n:
    #         count=1
    # print(count)

    count= (m%n)+(s-1)
    print(count)

    count= (((s - 1 + m - 1) % n) + 1)
    print(count,'\n')
