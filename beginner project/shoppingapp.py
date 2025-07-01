def display_available_items(dct):
    print("\t\tAvailable Items:")
    print(f"{'S.no.':<15}{'Item':<15}{'Quantity':<15}{'Cost/Item':<15}")
    for index, row in dct.items():
        print(f"{index:<15}{row['item']:<15}{row['quantity']:<15}{row['cost/item']:<15}")

availableItems = {1:{'item':'biscuits','quantity':5,'cost/item':20.5},
                  2:{'item':'choclates','quantity':10,'cost/item':35},
                  3:{'item':'coffee','quantity':25,'cost/item':55},
                  4:{'item':'chips','quantity':10,'cost/item':50},
                  5:{'item':'cream','quantity':5,'cost/item':30}}
display_available_items(availableItems)



def abc(usercart):
    total = 0
    for item in usercart:
        if item=='biscuits':
            price = 20.5
        elif item=='choclates':
            price = 35
        elif item=='coffee':
            price = 55
        elif item=='chips':
            price = 50
        elif item=='cream':
            price = 30
        amount = price*usercart[item]
        total = total + amount 
        print(f"{item:<15}{usercart[item]:<15}{amount:<15}") 
    print(f"total amount ={total}") 

usercart={'biscuits':4,'choclates':5,'coffee':2,'chips':4}
print('\n\t\tUser Cart')
print(f"{'Item':<15}{'Quantity':<15}{'Amount':<15}")
abc(usercart)



