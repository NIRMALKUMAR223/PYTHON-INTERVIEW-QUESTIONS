print('\tWelcome to RollerCoaster')
while True:
    try:
        n=input('\nEnter your name:')
        name=n.title()
        he=int(input('Enter your heigth in centimeter:'))
        if he<=120:
            print(f'your heigth is {he} cm so,You are not eligible!!!')
            break
        elif he>120:
            try:
                age=int(input('Enter your age:'))
                if age>=100:
                    print("\a")
                    print(name+' you are going to face struggles with the ride,so we cannot allow you sir')
                    print('Thankyou for coming,sir')
                elif age<=10:
                    print(name+f' Your ticket amount is RS.100')
                    break
                elif age<=18:
                    print(name+f' Your ticket amount is RS.150')
                    break
                else:
                    print(name+f' Your ticket amount is RS.200')
                    break
            except ValueError:
                print('invalid input..')
    except ValueError:
        print('wrong input\n\n')
    print('\t\tDo you want to rerun the program\n1.yes\n2.no')
    k=int(input("Enter your choice:"))
    if k==0:
        break
print('Thankyou visit again!!')
