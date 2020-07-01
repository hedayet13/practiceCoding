bill= [3,10,2,9]
k=1
billCharged =7
bill.remove(bill[k])
billActual =int(sum(bill)/2)
if billActual ==billCharged:
    print('Bon Appetit')
else:
    extraCharge = billCharged-billActual
    print(extraCharge)