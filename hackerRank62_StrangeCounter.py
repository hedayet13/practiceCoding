a=int(input())
y=3
z=3
if a<=3:
    ans = 4 -a
else:
    for i in range(100):
        z=2*z
        y=y+z
        if a<=y:
            ans=y+1-a
            break
print(ans)