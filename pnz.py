p=[]
n=[]
z=[]
lis=int(input("Enter the number"))
for i in lis:
    if lis<0:
        n.append(i)
    elif lis>0:
        p.append(i)
    elif lis==0:
        z.append(i)
    else:
        print("0")
