# diagonal difference


a= [[1,2,3],
    [4,5,6],
    [7,8,9]]
b=len(a)
k=1
diag1= 0
diag2=0
# print(a[0][1])
for i in range(b):
    diag1 = diag1+a[i][i]
for j in range(b):
    diag2 = diag2+a[j][j-k]
    k=k+2
print(abs(diag2-diag1))
# print(a[0][0-1])
# print(a[1][1-3])
# print(a[2][2-5])