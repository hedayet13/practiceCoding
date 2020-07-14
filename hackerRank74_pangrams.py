# a='We promptly judged antique ivory buckles for the next prize'.lower()
# a='We promptly judged antique ivory buckles for the prize'
a=input().lower()
a=list(a)
# print(a)
b='abcdefghijklmnopqrstuvwxyz'
b=list(b)
count=0
for i in range(len(b)):
    if b[i] in a:
        count+=1
if count ==26:
    print('pangrams')
else:print('not pangram')