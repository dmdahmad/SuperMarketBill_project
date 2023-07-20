from datetime import datetime

name=input("Enter your name:")
#lists of items
lists='''
Rice     Rs 20/kg
Sugar    Rs 30/kg
Salt     Rs 50/kg
Oil      Rs 105/litre
Tomato   Rs 50/kg
Onion    Rs 55/kg
Drinks   Rs 50/litre
'''

#delaration
price=0
pricelist=[]
totalprice=0
finalfinalprice=0
ilist=[]
qlist=[]
plist=[]

#rates for items
items={
    'Rice':20,
    'Sugar':30,
    'Salt':50,
    'Oil':105,
    'Tomato':50,
    'Onion':55,
    'Drinks':50
}
option=int(input("For list of items press 1 : "))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("If you want to buy 1 or 2 for exit : ")) 
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your items : ")
        quantity=int(input("Enter quantity : "))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("Sorry you entered item is not avaiable")
    else:
        print("You entered wrong number")
    inp=input("Can i bill the items yes or n : ")
    if inp=='yes':
        pass
        if finalamount!=0:
            print(26*"=","AA super market",26*"=")
            print(25*" ","    VIZAG      ",)
            print("Name:",name,25*" ","Date",datetime.now())
            print(73*"-")
            print(format("S.No.","<15"),format("Items","<15"),format("Quantity","<15"),format("Price","<15"))
            for i in range(len(pricelist)):
               print(format(i,"<15"),format(ilist[i],"<15"),format(qlist[i],"<15"),plist[i],"-/Rs")
            print(73*"-")
            print(50*" ","totalamount:",'Rs.',totalprice)
            print(50*" "," gst amount:",'Rs.',gst)
            print(48*" ","-"*25)
            print(50*" ",'finalamount:','Rs.',finalamount)
            print(73*"-")
            print("*"*25,"thanks for visiting","*"*25)
            print("*"*25,"  Have a nice day  ","*"*25)
            print("\n")
            


 