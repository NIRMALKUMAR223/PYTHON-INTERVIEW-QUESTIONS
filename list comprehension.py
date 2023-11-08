
x=int(input("Enter number"))
y=int(input("Enter number"))
z=int(input("Enter number"))
n=int(input("Enter list"))
li=list()
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k!=n:
                a=[i,j,k]
                li.append(a)
print(li)
