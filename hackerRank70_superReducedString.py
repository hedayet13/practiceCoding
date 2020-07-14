str = 'acdqglrfkqyuqfjkxyqvnrtysfrzrmzlygfveulqfpdbhlqdqrrqdqlhbdpfqluevfgylzmrzrfsytrnvqyxkjfquyqkfrlacdqj'
str=list(str)
str=sorted(str)
print(str)
x=0
y=1
for i in range(len(str)):
    if str[x]==str[y]:
        str.remove(str[y])
        str.remove(str[x])
    else:
        x+=1
        y+=1
    if  y>=len(str):
        break
if str==[]:
    print('Empty String')
else:
    print(''.join(str))

def superReducedString(s):
    j=1
    while(j<len(s)):
        if(s[j]==s[j-1]):
            s=s[0:j-1]+s[j+1:]
            j=1
        else:
            j=j+1
    if(len(s)!=0):
        print(s)
    else:
        print("Empty String")
s=input()
superReducedString(s)