def comp_ext_price(item_quantity, item_price):
    ext_price = Item_quantity * Item_price

    if ext_price > 10000.00:
        discount = ext_price * 0.10
    else:
        discount = 0.0

    return ext_price

Total_ext_price = 0.0
r = input("Do you want to compute the extended price (y/n)?")

while r == "y":
    Item_quantity = float(input("Enter item quantity: "))
    Item_price = float(input("Enter item price: "))
    ext_price = comp_ext_price(Item_quantity, Item_price)
    Total_ext_price = Total_ext_price + ext_price
    print("Extended Price is $", ext_price)
    r = input("Do you want to compute the extended price (y/n)?")

print("Total extended price is $", Total_ext_price)