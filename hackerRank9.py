'''
mini max some
'''

arr = [1,3,2,4,5]
arr.sort()
length = len(arr)
mini=0
max =0
for i in range(length-1):
    mini=mini+arr[i]
for i in range(1,length):
    max = max +arr[i]
print(mini,max)
print (sum(arr)-(max(arr))), (sum(arr)-(min(arr)))