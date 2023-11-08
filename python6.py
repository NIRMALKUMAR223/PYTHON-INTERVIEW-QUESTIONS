number=int(input('Enter the range: '))
for i in range(1,number):
    for h in range(2,i):
        if i%h==0:
            break
    else:
        print(i)
