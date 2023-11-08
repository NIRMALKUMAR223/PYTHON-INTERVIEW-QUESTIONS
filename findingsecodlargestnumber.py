lis=[4,3,2,1]
final=[]
while lis:
    fist=lis[0]
    for i in range(len(lis)):
        if lis[i]<fist:
            fist=lis[i]
    final.append(fist)
    lis.remove(fist)
second = len(final)-2
print("The second largest element is",final[second])