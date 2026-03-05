x = input("Input :").upper()

count = 0

for letter in x:
    if letter == "H" and "O" and "N" and "I":
        print(count + 1)
        count = 0
    else:
        print(0)



