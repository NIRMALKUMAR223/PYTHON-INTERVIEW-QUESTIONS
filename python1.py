d1=int(input('Enter the number: '))
d2=int(input('Enter another number: '))
rem=d1%d2
while rem!=0:
    d1=d2
    d2=rem
    rem=d1%d2
print('The greater common diviser:',d2)
