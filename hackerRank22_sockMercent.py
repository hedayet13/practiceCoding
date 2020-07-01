a=[1,2,1,2,1,3,2]
print(a.count(1))
pairs = 0

for element in set(a):
    pairs += a.count(element) //2
print(pairs)