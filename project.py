store = dict[("TV", 100),("Computer", 200),("Phone",150)]
print(store)
buyer = input("What Would You Like To Buy: ").upper()

if buyer == "TV":
    tv = store.index("TV")
    print(tv)
elif buyer == "COMPUTER":
    print("You Purchased A Computer")
elif buyer == "PHONE":
    print("You Purchased A Phone")

