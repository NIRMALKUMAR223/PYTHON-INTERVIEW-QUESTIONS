def fo(n):
    str=""
    for i in n:
        if i=="a":
            str+="p"
        elif i=="p": 
            str+="a"
        else:
            str+=i
    print(str)
n="apples"
fo(n)