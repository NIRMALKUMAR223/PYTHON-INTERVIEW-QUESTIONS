a=[]
n=int(input('Enter the element times'))
for i in range(1,n+1):
    variable=int(input('enter the element: '))
    a.append(variable)
a.sort()
print('The largest element is ',a[n-1])
 
