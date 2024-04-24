d = {'chips': 50, 'snacks': 80, 'chocolate': 50}

total = {}

    
def userInputValues():
    while True:
        print("Here is list of products we have in our store: ", list(d.keys()))
        userItem = input("Enter the item you want to buy: ")           
        userQty = int(input("Enter the unit of quantity you want to buy: "))
        if(userItem not in list(d.keys())):
            print('Wrong item selected...')
        else:
            findTotal(userItem, userQty)
        if(input("Do you wish to continue and buy products? Y/N: ").lower() != 'y'):
            print("Thank you for visiting our store")
            break


def findTotal(useritem, userqty):
    qtyValue = 0
    if(total.get(useritem) is not None):
        qtyValue = total.get(useritem)
        total[useritem] = qtyValue + userqty
    else:
        total[useritem] = userqty

def printTotal():
    totalprice = 0
    print("Here's a list of items you selected: \n")
    print("Items \t Qty \t PerUnitPrice \t  Amt")
    for key, value in total.items():
        unitPrice = d.get(key)
        price = value * unitPrice
        print("{key} \t {value} \t {unitPrice} \t\t {price}".format(key = key, value = value,unitPrice = unitPrice, price = price ))
        totalprice += price
    print("Your total amount is {totalprice}".format(totalprice = totalprice));

print("Welcome to our store")
userInputValues()
printTotal()