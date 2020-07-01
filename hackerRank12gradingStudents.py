score = [73,67,38,33,79]

'''
it returns int error in hacker rank ,, try to use range (length(score))
'''
for i in score:
    if i>=38:
        if i%5 ==3:
            i = i + 2
        elif i%5==4:
            i = i+1
        else:
            i=i
    else:
        i=i
    score = i
    print(score)