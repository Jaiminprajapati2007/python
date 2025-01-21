def ls():

 a=int(input("Enter the first number:"))
 b=int(input("Enter the second number:"))
 c=int (input ("Enter third number:"))

 if a>b and a>c:
     print("a is largest number")

     if b>c:
        print("c is smallest")

     else:
        print("b is smallest")

 if b>a and b>c:
    print("b is largest number")

    if a>c:
        print(" is smallest")

    else:
        print("a is smallest")

 if c>b and c>a:
    print("c is largest number")

    if b>a:
        print("a is smallest")

    else:
        print("b is smallest")

 elif a==b and b==c:
    print("all are equal")

 elif a==b or b==c or c==a:
    print("two are equal")

ls()
