def op(n):
    count=0
    string=""
    for i in n:
        if i=="-":
            count+=1
        else:
            string+=i
    print("- "*count,string)
na="hello-nirmal-hello-"
op(na)