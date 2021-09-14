char_a = "\\"
char_b = "|"
char_c = "/"
char_d = "_"

myString = ""
for x in range(100):
    for foo in range(randint(1, 7)):
        for bar in range(randint(1, 5)):
            myString += char_a
        for baz in range(randint(1, 5)):
            myString += char_b
        for baz in range(randint(1, 5)):
            myString += char_c
        for qux in range(randint(1, 5)):
            myString += char_d
    
print(myString)