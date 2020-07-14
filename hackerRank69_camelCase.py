str= input()
x=list(str)
count = 0
for i in x:
    if i.isupper():
        count+=1
print(count+1)