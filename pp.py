store =[
    {
        "name": "Samsung 55", 
        "price": 429.99, 
        "department": "Televisions",
     },

    {
        "name": "Iphone 18", 
        "price": 123, 
        "department": "Electronics",
     },
    
    {
        "name": "Iphone 20", 
        "price": 1000, 
        "department": "Electronics"} 
    ]






cart = []
while True:
    for index, item in enumerate(store):
        print(index, ":", item["name"], item["price"],item["department"])
    consumer = int(input("Buy What? "))
    cart.append(store[consumer])
    ask = input("Do You Want To Continue? ").upper()
    if ask == "NO":
        break

cost = 0
for things in cart:
    print(things["name"])
    cost += things["price"]
print(cost)



