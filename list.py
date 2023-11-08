#input[1,2,3,4,5,6,7,8,9,0]
#output[1,2,4,5,6,7,8,0]

var=list(input("Enter the list"))
out=[]
for i in var:
    if i==3 or i==9:
        continue
    out.append(i)
print(out)
