char_a = "/"
char_b = "|"
char_c = "\\"
char_d = "_"

myString = ""
for x in range(100):
    for foo in range(randint(1, 7)):
        if (random() > 0.75):
            for bar in range(randint(1, 7)):
                myString += char_a
        elif (random() > .5):
            for baz in range(randint(1, 7)):
                myString += char_b
        elif (random() > .25):
            for baz in range(randint(1, 7)):
                myString += char_b
        else:
            for qux in range(randint(1, 7)):
                myString += char_c
    
    
print(myString)