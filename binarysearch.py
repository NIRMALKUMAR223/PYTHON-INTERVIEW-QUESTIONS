def binarysearch(lis,n,lower,upper):
    mid=(lower+upper)//2
    if lower>=lis[0] and lower<len(lis):
        if lis[mid]==n:
            print("value found",lis[mid])
        elif lis[mid]>n:
            binarysearch(lis,n,lower+1,upper)
        elif lis[mid]<n:
            binarysearch(lis,n,lower-1,upper)
    else:
        print("The value not found",n)         
lis=[]
for i in range(10+1):
    first1=int(input("Enter the number: "))
    lis.append(first1)
lis.sort()
upper=len(lis)
lower=0
n=int(input("search number: "))
binarysearch(lis,n,lower,upper)
