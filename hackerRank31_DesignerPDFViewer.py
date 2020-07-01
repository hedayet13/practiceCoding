h = list(map(int,input().rstrip().split()))
word = input()
word = list(word)
list = []
final=[]
for c in range(97,123):
    list.append(chr(c))
for j in range(len(word)):
    for i in range(len(list)):
        if str(word[j])==str(list[i]):
            final.append(h[i])
print(max(final)*len(word))

