'''
normal way for big sorting is a slower process
'''
# a=8
# b=[1,212,424,4512,123243214321132]
a=int(input())
b = []

for _ in range(a):
    unsorted_item = int(input())
    b.append(unsorted_item)
# b= list(map(int,input().rstrip().split()))
# print(b)
b=sorted(b)
for i in b:
    print(i)
# print(sorted(b))



'''
bucket strip (faster process)
'''
n = int(input().strip())
bucket = {}

# read all integers as strings, store them by length in the bucket
for _ in range(n):
    number = input().strip()
    length = len(number)

    # create new bucket for length
    if not length in bucket:
        bucket[length] = []

    bucket[length].append(number)

# read from the bucket in ascending order
for key in sorted(bucket):
    for value in sorted(bucket[key]):
        print(value)