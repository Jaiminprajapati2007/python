a=int(input("enter the first num?"))
b=int(input("enter the second num?"))
c=int(input("enter the third num?"))

if (a>b) and (a>c):
    print(a,"a is largest num")

    if(b>c):
        print(c,"c is smallest num")

    else:
        print(b,"b is smallest num")

elif (b>a) and (b>c):
    print(b,"b is largest num")

    if(a>c):
        print(c,"c is smallest num")

    else:
        print(a,"a is smallest num")

else (c>b) and (c>a):
    print(c,"c is largest num")

    if b>a:
        print(a,"a is smallest num")

    else:
        print(b,"b is smallest num")
