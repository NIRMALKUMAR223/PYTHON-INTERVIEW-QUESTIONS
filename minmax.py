def smallest(n):
    min=n[0]
    for i in n:
        if min>i:
            min=i
    print("The minimum is ",min)

def largestmumber(x):
    max=0
    for i in x:
        if i > max:
            max=i
    print("The largest is",max)

lis=list(map(int,input(">>>>").split()))
largestmumber(lis)
smallest(lis)