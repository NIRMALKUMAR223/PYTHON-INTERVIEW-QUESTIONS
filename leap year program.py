user=int(input("Enter the number "))
if (user%4==0 and user%100!=0)or (user%100==0 and user%400==0):
    print("The given input is leap year..!")
else:
    print("not leap year")
