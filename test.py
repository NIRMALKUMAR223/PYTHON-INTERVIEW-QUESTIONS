count=0
while True:
    n=int(input("::>>>"))
    if n%2==0:
        print("EVEN")
        break
    else:
        print("Enter again")
    count+=1
print(count)