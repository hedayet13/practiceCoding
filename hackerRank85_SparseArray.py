lst1=['aba','baba','aba','xzxb']
lst2=['aba','xzxb','ab']

lst =[]
for i in range(len(lst2)):
    count = 0
    for j in range(len(lst1)):
        if lst1[j]==lst2[i]:
            count+=1

    print(count)
