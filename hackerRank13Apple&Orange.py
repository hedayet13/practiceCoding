s= 7
t= 11
a= 5
b= 15
apples = [-2,2,1,4]
oranges = [5,-6]

count1 = 0
count2= 0
for i in range(len(apples)):
    num = a + apples[i]
    if s<=num<=t:
        count1 = count1 +1
print(count1)
for i in range(len(oranges)):
    num = b + oranges[i]
    if s<=num<=t:
        count2 = count2 +1
print(count2)