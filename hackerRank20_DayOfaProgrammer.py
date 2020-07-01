n=1996
if n<1918 and n%4==0: #for julian calender
    print('12.09.{:}'.format(n))
elif n==1918:  #because as german shift julian to georgian after 31st january the day is 14th february that means the gap is at least 13 days so the printing statement is looks odd
    print('26.09.1918')
elif n>1918 and (n%400==0 or (n%4==0 and n%100!=0)): #for georgian calender
    print('12.09.{:}'.format(n))
else:
    print('13.09.{:}'.format(n))