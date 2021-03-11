

mainBoard = ( "      |       |      \n"
              "  1   |   2   |  3   \n"
              "------|-------|------\n"
              "  4   |   5   |  6   \n"
              "------|-------|------\n"
              "  7   |   8   |  9   \n"
              "      |       |       ")
displayBoard = ( "      |       |      \n"
                 "      |       |      \n"
                 "------|-------|------\n"
                 
                 "      |       |      \n"
                 "------|-------|------\n"
                 "      |       |      \n"
                 "      |       |       ")
a=list(mainBoard)
b=list(displayBoard)
z=[]
for i in range(len(a)):
      if a[i].isdigit()==True:
            z.append(i)
print ("which one You want to choose!! \n"
       "For x type 0 \n"
       "For o type 1")
player = ['x','o']
number = int(input())
if number == 0 or number ==1:
    player =player[number]
print(player)

print(mainBoard)

iter = 0
numberRange = list(range(1,10))
while iter<9:
    if player== 'x':
        print('put yout number!!! Player: X')
        number = int(input())
        if number in numberRange:
            b.pop(z[number-1])
            b.insert(z[number-1],'x')
            listTostr= ''.join(map(str,b))
            print(listTostr)
            numberRange.remove(number)
            player = 'o'
            iter+=1
        else:
            print('Please select another number between 0 to 9')
    print (numberRange)
    if player== 'o':
        print('put yout number!!! Player O')
        number = int(input())
        if number in numberRange:
            b.pop(z[number - 1])
            b.insert(z[number - 1], 'o')
            listTostr = ''.join(map(str, b))
            print(listTostr)
            numberRange.remove(number)
            player = 'x'
            iter+=1
        else:
            print('Please select another number between 0 to 9')
