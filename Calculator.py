a=int(input("Enter the First Number:-"))
b=int(input("Enter the Second Number:-"))
opr=input("Enter the operator(+,-,*,/):-")
if opr=="+":
    print(a+b)
else:
    if opr=="-":
        print(a-b)

    if opr=="*":
            print(a*b)

    if opr=="/":
                print(a/b)

if opr!="+" and opr!="-" and opr!="*" and opr!="/":
   print("invalid opr")
            
