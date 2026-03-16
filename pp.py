
item =[
    {"name": "Samsung 55", 
     "price": "$429.99", 
     "department": "Televisions",},

    {"name": "Iphone 18", 
     "price": "$123", 
     "department": "Electronics",},
    
    {"name": "Iphone 20", 
     "price": "$1000", 
     "department": "Electronics"} 
    ]

print(item[0]["name"],item[0]["price"],item[0]["department"])
print(item[1]["name"],item[1]["price"],item[1]["department"])
print(item[2]["name"],item[2]["price"],item[2]["department"])

price = 0
count = 0

buyer = input("Buy What? ").upper()
if buyer == "SAMSUNG 55":
    print("Samsung 55")
    price += float(429.99)
elif buyer == "IPHONE 18":
    print("Iphone 18")
    price += int(123)
elif buyer == "IPHONE 20":
    print("Iphone 20")
    price += int(1000)
while True:
    user = input("Do you want to continue? yes/no ").lower()
    if user == "no":
        print(buyer)
        if count >= 1:
            print(buy2)
        print("$", price)
        break
    else:
        if user == "yes":
            count += 1
            buy2 = input("What Else? ").upper()
            if buy2 == "SAMSUNG 55":
                print("Samsung 55")
                price += float(429.99)
            elif buy2 == "IPHONE 18":
                print("Iphone 18")
                price += int(123)
            elif buy2 == ("IPHONE 20"):
                print("Iphone 20")
                price += int(1000)





