lis=[1,4,57,5,9,6,4,69,4,8,4,7]
sample=[]
while lis:
    temp=lis[0]
    for i in range(len(lis)):
        if lis[i]<temp:
            temp=lis[i]
    sample.append(temp)
    lis.remove(temp)
print(lis)
