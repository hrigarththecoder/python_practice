num=int(input("enter: "))
if num<=1:
    print("not")
elif num==2:
    print("yes only even prime")
else:
    for i in range(2,num+1):
        if num%i==0:
            print("not")
            break
        else:
            print("prime")
            break


