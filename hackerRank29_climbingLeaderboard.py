a=[100,100,50,40,40,20,10]
a=set(a)
a=list(sorted(a,reverse=True))
for i in range(len(b)):

    for  j in range(len(a)):
        if b[i]==a[j]:
            print(b[i],a[j],j+1)
            break
        elif b[i]>a[j]:
            print(b[i],a[j],j+1)
            break
        elif b[i]< min(a):
            print(b[i],min(a),len(a)+1)
            break


        # if b[j]>=a[i]:
        #     print(b[j],a[i])

        # print(count2)
# rank = dict()
# for i in range(len(a)):
#     rank[i+1]=a[i]
#
# print(rank)
import sys

if __name__ == "__main__":
    n = int(input().strip())
    scores = sorted(list(set(list(map(int, input().strip().split(' '))))), reverse=True)
    m = int(input().strip())
    alice = list(map(int, input().strip().split(' ')))
    scores.append(0)
    l = len(scores)
    # Write Your Code Here
    for a in alice:
        while (l > 0) and (a >= scores[l-1]):
            l -= 1
        print(l+1)