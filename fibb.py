c=int(input("Enter the number:"))
a=1
b=0
for i in range(c+1):
    result=a+b
    a=b
    b=result
    print(result)
