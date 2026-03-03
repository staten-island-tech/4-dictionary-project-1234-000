user = input("Sentence:").upper()
char_to_count = "T"
count = user.count(char_to_count)
print("T",count)
char_to_count2 = "S"
count2 = user.count(char_to_count2)
print("S",count2)

if count >= count2:
    print("English")
else:
    print("French")


