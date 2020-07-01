keyboards =[4]
usb=[5]
maxi=5
list=[]
for i in keyboards:
    for j in usb:
        if i+j<=maxi:
            list.append(i+j)
        else:
            list.append(-1)
print(max(list))
