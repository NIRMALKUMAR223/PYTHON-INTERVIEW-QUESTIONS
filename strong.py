def strongnumber(number):
    count=1
    for first in str(number):
        for second in range(1,int(first)):
            count*=second
    if count==num:
        print("The given number is an strong integer",count)
    else:
        print(f"The given number {num} not an strong integer")

num=int(input())
strongnumber(num)
