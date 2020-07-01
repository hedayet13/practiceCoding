a= [2 , 4]
b= [16,32,96]

maxA = max(a)
minB = min(b)
count = 0
for num in range(maxA, minB +1):
    left = all([num % numA == 0 for numA in a])
    # print(num,left)
    right = all([numB % num == 0 for numB in b])
    # print(num ,right)
    count += left*right

print(count)
print(maxA)
print(minB)
# print(range(4,17))
# print(True*True)
# print(True*False)
# print(False*False)
# print(False*True)

