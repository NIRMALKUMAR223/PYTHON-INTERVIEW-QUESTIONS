def op(oor,n):
    if n<4:
        return 0
    if oor[0].isdigit():
        return 0
    cap=0
    num=0
    for i in range(n):
        if oor[i]==" " or oor[i]=="/":
            return 0
        if oor[i]>='A' and oor[i]<='Z':
            cap+=1
        elif oor[i].isdigit():
            num+=1
    if num and cap >0:
        return 1
    else:
        return 0
inputt=input()
n=len(inputt)
print(op(inputt,n))