print("\t\t......HOSTAL MEMBERS......")
while True:
    print("\n0.VIEW THE LIST")
    print("1.ADD STUDENT..")
    print("2.DELETE STUDENT..")
    print("3.SEARCH STUDENT..")
    print("4.EXIT..")
    try:
        jim=int(input("ENTER YOUR CHOICE:"))
        k=list(["NIRMAL","MADESH","ROSHAN","KISHORE","KISHORE KUMAR","CHAKARAVARTHI","MUTHU GANESH","BALA","KARTHI"])
        if jim==0:
            print(k)
        elif jim==1:
            u=input("WHICH USER YOU WANT TO ADD:")
            u=u.upper()
            k.extend(u)
            print("YOU SUCCESFULLY ADDED TO LIST... "+u)
            dd=int(input("DO YOU WANT TO PRINT THE LIST"))
            print("1.SEE THE LIST")
            print("2.EXIT")
            if dd==1:
                print(k)
            else:
                exit()
        elif jim==2:
            print(k)
            pi=input("ENTER THE NAME WHICH YOU WANT TO DELETE..?")
            ji=pi.upper()
            k.remove(ji)
            ww=input("DO YOU WANT TO PRINT THE LIST")
            print("1.SEE THE LIST")
            print("2.EXIT")
            if ww==1:
                print(k)
            else:
                exit()
        elif jim==3:
            print(k)
            hi=input("ENTER THE NAME WHICH YOU WANT TO SEARCH..?")
            g=hi.upper()
            for i in k:
                if i == g:
                    print(f"YEAH,{g} THE NAME FOUND")
                    exit()  
        else:
            exit()
    except ValueError:
        print("PLEASE ENTER CORRECT VALUE..")
    print("1.Yes")
    print("2.No")
    s=int(input("Enter your choice:"))
    if s==2:
        exit()
