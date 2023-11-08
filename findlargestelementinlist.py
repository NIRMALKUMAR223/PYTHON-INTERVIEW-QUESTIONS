list1=int(input('Enter the size of list: '))
user=[]
for i in range(list1):
    i1=int(input('Enter the element: '))
    user.append(i1)
user.sort()
print('The largest number is:',user[-1])
