a= input()
a= list(a)
count=0
for i in range(len(a)):
    if a[i]=='S' or a[i] =='O' :
        continue
    else:
        count+=1
print(count)


s=input().strip()
print(sum(1 for i in range(len(s)) if s[i]!="SOS"[i%3]))