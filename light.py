print("\tLight program")
light=False
while True:
    print("1.Turn on light")
    print("2.Turn off light")
    print("3.exit")
    user=int(input("Enter your choice ?"))
    if user==1:
        if light==True:
            print("The light is already on buddy")
        print("light's on")
        light=True
    elif user==2:
        if light==False:
            print("The light is already off buddy")
        print("light's off")
        light=False
    elif user==3:
        print("THANK YOU....!")
        exit()
            
