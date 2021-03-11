arr=[[1, 1, 1, 0, 0, 0],
     [0, 1, 0, 0 ,0 ,0],
     [1 ,1 ,1 ,0 ,0 ,0],
     [0 ,0 ,2 ,4, 4, 0],
     [0 ,0 ,0 ,2 ,0 ,0],
     [0 ,0 ,1 ,2 ,4 ,0]]

lst =[]
for i in range(len(arr[0])):
    for j in range(len(arr[0])):
        if j<len(arr[0])-2 and i<len(arr[0])-2:
            sum = arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            lst.append(sum)

print(max(lst))

