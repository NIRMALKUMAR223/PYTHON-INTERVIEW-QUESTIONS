def add(a,b):
    c=a+b
    return c
def sub(a,b):
    x=a-b
    return x
def mul(a,b):
    y=a*b
    return y
def div(a,b):
    z=a/b
    return z
print("1.ADDICTION")
print("2.SUBRACTION")
print("3.MULTIPICATION")
print("4.DIVISION")
print("5.EXIT")
u=int(input("Enter the choice:"))
if u==5:
    exit()
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
if u==1:
    c=add(a,b)
    print(c)
elif u==2:
    x=sub(a,b)
    print(x)
elif u==3:
    y=mul(a,b)
    print(y)
elif u==4:
    z=div(a,b)
    print(z)

