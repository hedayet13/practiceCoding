'''
birthday cake challenge
'''

ar = [3,1,2,3,3,2,3]
age = max(ar)
count = 0
for i in ar:
    if i%age==0:
        count = count +1
print(count)