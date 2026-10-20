#wWAP FOR ORDERING FOOD FROM CANTEEN

item_count=0
expense=0
while True:
    user=float(input("ENTER PRICE OF ITEM & WRITE 0.00 TO EXIT: "))
    if (user==0.00)or(user==0):
        break
    elif user<0:
        print("enter valid price pls")
        continue
    else:
        print("OK GOT IT")
        item_count+=1
        expense+=user
print("TOTAL ITEMS ORDERED:",item_count)
print("TOTAL COST:",expense)
print("THANK U")