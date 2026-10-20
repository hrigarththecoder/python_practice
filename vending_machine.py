item=("tea","juice","coffee")
stock={"tea":2,"juice":1,"coffee":0}
order_count={}
served_item=set()
order=True

while order==True:
    user=input("WHAT WOULD U LIKE TO ORDER? ")
    if stock.get(item,0)>0:
        stock[item]-=1
        order_count[item]=order_count.get(item,0)+1
        served_item.add(item)
    elif user.lower()=="nothing":
        break
    else:
        print("NOT AVAILABLE")

print("ORDERED ITEMS",order_count)
print("DIFFERENT ITEMS SERVED",served_item)
print("REMAINING STOCK",stock)
