d1= 9
m1= 6
y1=2015
d2=6
m2=6
y2=2015
hackos=0
if d1>d2 and m1==m2 and y1==y2:
    hackos= 15*(d1-d2)
if m1>m2 and y1==y2 :
    hackos=(500*(m1-m2))
if y1>y2:
    hackos=(10000*(y1-y2))
print(hackos)